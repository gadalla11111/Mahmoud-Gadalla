#!/usr/bin/env python3
"""crawl4ai_mcp — a proof-of-concept MCP server that wraps Crawl4AI.

It exposes Crawl4AI's web scraping as MCP tools that return **LLM-ready
Markdown**, so any MCP client (Claude Code, ruflo, Codex, …) can turn a URL
into clean context with one tool call. Transport is stdio (local use).

Tools
-----
- ``crawl4ai_scrape_url``     : one URL   -> Markdown (or JSON with metadata)
- ``crawl4ai_scrape_many``    : N URLs    -> per-URL Markdown/JSON (concurrent)
- ``crawl4ai_extract_schema`` : one URL   -> structured JSON via a CSS schema
- ``crawl4ai_deep_crawl``     : start URL -> BFS-crawl linked pages to depth N
- ``crawl4ai_screenshot``     : one URL   -> full-page PNG saved to disk
- ``crawl4ai_capture_pdf``    : one URL   -> full-page PDF saved to disk

Env config: ``CRAWL4AI_STORAGE_STATE`` = a saved Playwright session file (from
``save_session.py``) to scrape logged-in; ``CRAWL4AI_PROXY`` = a proxy URL routed
for every request; ``CRAWL4AI_OUTPUT_DIR`` = where screenshots/PDFs are written
(defaults to the system temp dir).

Crawl4AI is imported **lazily** on first tool call, so this module stays
importable — and the MCP server registrable/inspectable — before the heavy
Playwright browser runtime is installed (`crawl4ai-setup`). Run
``python server.py --selfcheck`` to list the registered tools without a
browser.

This is a PoC: six focused tools, not full Crawl4AI coverage.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import tempfile
from enum import Enum
from types import SimpleNamespace
from typing import Any, Optional
from urllib.parse import urlparse

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("crawl4ai_mcp")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
DEFAULT_TIMEOUT_MS = 30_000
MAX_URLS = 20
# Guard against dumping an enormous page straight into the model's context.
MAX_MARKDOWN_CHARS = 200_000
# Optional path to a Playwright storage-state file (cookies + localStorage) that
# makes every scrape run as a logged-in session. Configured via env (not a tool
# input, so an agent can't point it at arbitrary files); created by save_session.py.
STORAGE_STATE_ENV = "CRAWL4AI_STORAGE_STATE"
# Optional proxy URL (e.g. "http://user:pass@host:port") routed for every scrape.
PROXY_ENV = "CRAWL4AI_PROXY"


class ResponseFormat(str, Enum):
    """Output format for tool responses."""

    MARKDOWN = "markdown"
    JSON = "json"


# ---------------------------------------------------------------------------
# Input models
# ---------------------------------------------------------------------------
def _require_http_url(value: str) -> str:
    """Validate and normalise a single http(s) URL (shared by both models)."""
    value = (value or "").strip()
    if not (value.startswith("http://") or value.startswith("https://")):
        raise ValueError(f"url must start with http:// or https:// (got '{value}')")
    return value


class ScrapeUrlInput(BaseModel):
    """Input for scraping a single URL."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    url: str = Field(
        ...,
        description="Absolute http(s) URL to scrape, e.g. 'https://example.com'.",
        min_length=1,
        max_length=2048,
    )
    css_selector: Optional[str] = Field(
        default=None,
        description="Optional CSS selector to keep only matching regions "
        "(e.g. 'article', 'main .content'). Omit to scrape the whole page.",
        max_length=500,
    )
    fit_markdown: bool = Field(
        default=True,
        description="Return Crawl4AI's pruned 'fit' Markdown (main content only) "
        "instead of the full raw Markdown. Turn off to keep nav/boilerplate.",
    )
    bypass_cache: bool = Field(
        default=False,
        description="Bypass Crawl4AI's local cache and re-fetch the live page.",
    )
    timeout_ms: int = Field(
        default=DEFAULT_TIMEOUT_MS,
        description="Per-page navigation timeout in milliseconds.",
        ge=1_000,
        le=120_000,
    )
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="'markdown' returns just the content; 'json' returns content "
        "plus metadata (final url, http status, success).",
    )

    @field_validator("url")
    @classmethod
    def _validate_url(cls, v: str) -> str:
        return _require_http_url(v)


class ScrapeManyInput(BaseModel):
    """Input for scraping several URLs concurrently."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    urls: list[str] = Field(
        ...,
        description="List of absolute http(s) URLs to scrape concurrently "
        f"(1–{MAX_URLS}).",
        min_length=1,
        max_length=MAX_URLS,
    )
    fit_markdown: bool = Field(
        default=True,
        description="Return pruned 'fit' Markdown instead of raw Markdown.",
    )
    bypass_cache: bool = Field(
        default=False,
        description="Bypass Crawl4AI's local cache and re-fetch live pages.",
    )
    timeout_ms: int = Field(
        default=DEFAULT_TIMEOUT_MS,
        description="Per-page navigation timeout in milliseconds.",
        ge=1_000,
        le=120_000,
    )
    response_format: ResponseFormat = Field(
        default=ResponseFormat.JSON,
        description="'json' returns a per-URL array with status + markdown; "
        "'markdown' concatenates the pages under '# <url>' headers.",
    )

    @field_validator("urls")
    @classmethod
    def _validate_urls(cls, v: list[str]) -> list[str]:
        return [_require_http_url(u) for u in v]


class FieldType(str, Enum):
    """How to read a field's value from its matched element."""

    TEXT = "text"
    ATTRIBUTE = "attribute"
    HTML = "html"


class FieldSpec(BaseModel):
    """One field to pull out of each matched record."""

    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    name: str = Field(
        ...,
        description="Output key for this field (e.g. 'title', 'price').",
        min_length=1,
        max_length=100,
    )
    selector: str = Field(
        ...,
        description="CSS selector relative to the record's base_selector.",
        min_length=1,
        max_length=500,
    )
    type: FieldType = Field(
        default=FieldType.TEXT,
        description="'text' (inner text), 'attribute' (requires `attribute`), or 'html'.",
    )
    attribute: Optional[str] = Field(
        default=None,
        description="Attribute to read when type='attribute' (e.g. 'href', 'src').",
        max_length=100,
    )

    @model_validator(mode="after")
    def _require_attribute(self) -> "FieldSpec":
        if self.type is FieldType.ATTRIBUTE and not self.attribute:
            raise ValueError(
                "field type 'attribute' requires an `attribute` name (e.g. 'href')"
            )
        return self


class ExtractSchemaInput(BaseModel):
    """Input for CSS-schema structured extraction."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    url: str = Field(
        ...,
        description="Absolute http(s) URL to extract from.",
        min_length=1,
        max_length=2048,
    )
    base_selector: str = Field(
        ...,
        description="CSS selector matching each repeating record on the page "
        "(e.g. 'div.product', 'article', 'tr.row').",
        min_length=1,
        max_length=500,
    )
    fields: list[FieldSpec] = Field(
        ...,
        description="Fields to extract from each matched record (1–50).",
        min_length=1,
        max_length=50,
    )
    bypass_cache: bool = Field(
        default=False,
        description="Bypass Crawl4AI's cache and re-fetch the live page.",
    )
    timeout_ms: int = Field(
        default=DEFAULT_TIMEOUT_MS,
        description="Per-page navigation timeout in milliseconds.",
        ge=1_000,
        le=120_000,
    )

    @field_validator("url")
    @classmethod
    def _validate_url(cls, v: str) -> str:
        return _require_http_url(v)


class DeepCrawlInput(BaseModel):
    """Input for a bounded breadth-first deep crawl."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    url: str = Field(
        ...,
        description="Absolute http(s) URL to start crawling from.",
        min_length=1,
        max_length=2048,
    )
    max_depth: int = Field(
        default=1,
        description="How many link-hops from the start URL to follow "
        "(0 = start page only; 1 = start page + its direct links).",
        ge=0,
        le=3,
    )
    max_pages: int = Field(
        default=10,
        description="Hard cap on total pages fetched (safety limit).",
        ge=1,
        le=50,
    )
    include_external: bool = Field(
        default=False,
        description="Follow links to other domains too "
        "(default: stay on the start URL's domain).",
    )
    fit_markdown: bool = Field(
        default=True,
        description="Return pruned 'fit' Markdown per page.",
    )
    timeout_ms: int = Field(
        default=DEFAULT_TIMEOUT_MS,
        description="Per-page navigation timeout in milliseconds.",
        ge=1_000,
        le=120_000,
    )

    @field_validator("url")
    @classmethod
    def _validate_url(cls, v: str) -> str:
        return _require_http_url(v)


class PageCaptureInput(BaseModel):
    """Input for capturing a page as an image or PDF (url + timeout only)."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    url: str = Field(
        ...,
        description="Absolute http(s) URL to capture.",
        min_length=1,
        max_length=2048,
    )
    timeout_ms: int = Field(
        default=DEFAULT_TIMEOUT_MS,
        description="Per-page navigation timeout in milliseconds.",
        ge=1_000,
        le=120_000,
    )

    @field_validator("url")
    @classmethod
    def _validate_url(cls, v: str) -> str:
        return _require_http_url(v)


# ---------------------------------------------------------------------------
# Crawl4AI adapter (lazy import + shared helpers)
# ---------------------------------------------------------------------------
def _import_crawl4ai() -> SimpleNamespace:
    """Import Crawl4AI on demand, with an actionable error if it's missing.

    Returns a namespace of the Crawl4AI classes this server uses, so callers
    read them by attribute (``c4.AsyncWebCrawler``) instead of unpacking a
    positional tuple.
    """
    try:
        from crawl4ai import (  # noqa: PLC0415  (intentional lazy import)
            AsyncWebCrawler,
            BrowserConfig,
            CacheMode,
            CrawlerRunConfig,
            JsonCssExtractionStrategy,
        )
    except ImportError as exc:  # pragma: no cover - depends on environment
        raise RuntimeError(
            "Crawl4AI is not installed. Set the PoC up first:\n"
            "  pip install -r requirements.txt\n"
            "  crawl4ai-setup      # installs the Playwright browser runtime\n"
            f"(original import error: {exc})"
        ) from exc
    return SimpleNamespace(
        AsyncWebCrawler=AsyncWebCrawler,
        BrowserConfig=BrowserConfig,
        CacheMode=CacheMode,
        CrawlerRunConfig=CrawlerRunConfig,
        JsonCssExtractionStrategy=JsonCssExtractionStrategy,
    )


def _auth_kwargs() -> dict[str, str]:
    """BrowserConfig kwargs for a saved auth session, or ``{}`` if none configured.

    Pure (env + filesystem only) so it can be unit-tested without Crawl4AI.
    Raises if the env var points at a path that does not exist.
    """
    state = os.environ.get(STORAGE_STATE_ENV)
    if not state:
        return {}
    if not os.path.isfile(state):
        raise RuntimeError(
            f"{STORAGE_STATE_ENV} is set to '{state}', but no such file exists. "
            "Create a session with `python save_session.py <login_url> <out.json>`."
        )
    return {"storage_state": state}


def _proxy_kwargs() -> dict[str, Any]:
    """BrowserConfig kwargs for a proxy, or ``{}`` if CRAWL4AI_PROXY is unset.

    Pure (env + urlparse only). Uses Crawl4AI's non-deprecated ``proxy_config``
    (a plain dict BrowserConfig accepts), splitting any ``user:pass@`` credentials
    out of the URL into separate fields.
    """
    proxy = os.environ.get(PROXY_ENV)
    if not proxy:
        return {}
    parsed = urlparse(proxy)
    if parsed.hostname:
        server = f"{parsed.scheme or 'http'}://{parsed.hostname}"
        if parsed.port:
            server += f":{parsed.port}"
    else:
        server = proxy  # not a standard URL; hand it over verbatim
    config: dict[str, str] = {"server": server}
    if parsed.username:
        config["username"] = parsed.username
    if parsed.password:
        config["password"] = parsed.password
    return {"proxy_config": config}


def _browser_config(c4: SimpleNamespace):
    """Headless BrowserConfig with any configured saved session and/or proxy."""
    return c4.BrowserConfig(headless=True, **_auth_kwargs(), **_proxy_kwargs())


def _extract_markdown(result: Any, fit: bool) -> str:
    """Pull Markdown out of a Crawl4AI result across SDK versions.

    Newer Crawl4AI returns a ``MarkdownGenerationResult`` (``.fit_markdown`` /
    ``.raw_markdown``); older versions return a plain string.
    """
    md = getattr(result, "markdown", None)
    if md is None:
        return ""
    if fit:
        text = getattr(md, "fit_markdown", None) or getattr(md, "raw_markdown", None) or str(md)
    else:
        text = getattr(md, "raw_markdown", None) or str(md)
    text = text or ""
    if len(text) > MAX_MARKDOWN_CHARS:
        text = text[:MAX_MARKDOWN_CHARS] + (
            f"\n\n[...truncated at {MAX_MARKDOWN_CHARS:,} chars — "
            "narrow the page with `css_selector`...]"
        )
    return text


def _result_to_dict(result: Any, fit: bool) -> dict[str, Any]:
    """Normalise a Crawl4AI result into a compact, JSON-serialisable dict."""
    success = bool(getattr(result, "success", False))
    return {
        "url": getattr(result, "url", None),
        "success": success,
        "status_code": getattr(result, "status_code", None),
        "error_message": getattr(result, "error_message", None) or None,
        "markdown": _extract_markdown(result, fit) if success else "",
    }


def _crawl_error(exc: Exception, where: str) -> str:
    """Format an unexpected crawl failure into an actionable message.

    All tool error returns start with the literal ``Error:`` prefix so callers
    (and the smoke test) can detect failure uniformly.
    """
    return (
        f"Error: could not scrape {where}: {type(exc).__name__}: {exc}. "
        "If this looks like a timeout, raise `timeout_ms`; if it's a browser/"
        "Playwright error, run `crawl4ai-setup` to install the matching browser."
    )


async def _crawl(
    urls: list[str],
    *,
    fit: bool,
    bypass_cache: bool,
    timeout_ms: int,
    css_selector: Optional[str] = None,
) -> list[Any]:
    """Open a headless crawler and run one (``arun``) or many (``arun_many``)."""
    c4 = _import_crawl4ai()
    run_config = c4.CrawlerRunConfig(
        cache_mode=c4.CacheMode.BYPASS if bypass_cache else c4.CacheMode.ENABLED,
        page_timeout=timeout_ms,
        css_selector=css_selector,
    )
    async with c4.AsyncWebCrawler(config=_browser_config(c4)) as crawler:
        if len(urls) == 1:
            return [await crawler.arun(url=urls[0], config=run_config)]
        return list(await crawler.arun_many(urls=urls, config=run_config))


async def _crawl_extract(
    url: str, *, schema: dict[str, Any], bypass_cache: bool, timeout_ms: int
) -> Any:
    """Run a single crawl with a CSS-schema extraction strategy attached."""
    c4 = _import_crawl4ai()
    run_config = c4.CrawlerRunConfig(
        cache_mode=c4.CacheMode.BYPASS if bypass_cache else c4.CacheMode.ENABLED,
        page_timeout=timeout_ms,
        extraction_strategy=c4.JsonCssExtractionStrategy(schema),
    )
    async with c4.AsyncWebCrawler(config=_browser_config(c4)) as crawler:
        return await crawler.arun(url=url, config=run_config)


def _import_bfs_strategy():
    """Import Crawl4AI's BFS deep-crawl strategy across SDK layouts."""
    try:
        from crawl4ai.deep_crawling import BFSDeepCrawlStrategy  # noqa: PLC0415
        return BFSDeepCrawlStrategy
    except ImportError:
        try:
            from crawl4ai import BFSDeepCrawlStrategy  # noqa: PLC0415
            return BFSDeepCrawlStrategy
        except ImportError as exc:
            raise RuntimeError(
                "This Crawl4AI version doesn't expose BFSDeepCrawlStrategy for deep "
                "crawling. Upgrade crawl4ai, or pass an explicit URL list to "
                f"crawl4ai_scrape_many instead. ({exc})"
            ) from exc


async def _deep_crawl(
    url: str,
    *,
    max_depth: int,
    max_pages: int,
    include_external: bool,
    timeout_ms: int,
) -> list[Any]:
    """BFS-crawl from ``url`` and return up to ``max_pages`` page results."""
    c4 = _import_crawl4ai()
    bfs = _import_bfs_strategy()
    try:
        strategy = bfs(
            max_depth=max_depth, include_external=include_external, max_pages=max_pages
        )
    except TypeError:  # older signature without max_pages
        strategy = bfs(max_depth=max_depth, include_external=include_external)
    run_config = c4.CrawlerRunConfig(
        cache_mode=c4.CacheMode.ENABLED,
        page_timeout=timeout_ms,
        deep_crawl_strategy=strategy,
        stream=False,
    )
    async with c4.AsyncWebCrawler(config=_browser_config(c4)) as crawler:
        results = await crawler.arun(url=url, config=run_config)
    results = results if isinstance(results, list) else [results]
    return results[:max_pages]  # enforce cap even if the SDK ignored max_pages


async def _crawl_screenshot(url: str, *, timeout_ms: int) -> Any:
    """Load ``url`` with screenshot capture enabled and return the result."""
    c4 = _import_crawl4ai()
    run_config = c4.CrawlerRunConfig(
        cache_mode=c4.CacheMode.BYPASS,  # a screenshot wants the live page
        page_timeout=timeout_ms,
        screenshot=True,
    )
    async with c4.AsyncWebCrawler(config=_browser_config(c4)) as crawler:
        return await crawler.arun(url=url, config=run_config)


async def _crawl_pdf(url: str, *, timeout_ms: int) -> Any:
    """Load ``url`` with PDF capture enabled and return the result."""
    c4 = _import_crawl4ai()
    run_config = c4.CrawlerRunConfig(
        cache_mode=c4.CacheMode.BYPASS,  # a fresh PDF wants the live page
        page_timeout=timeout_ms,
        pdf=True,
    )
    async with c4.AsyncWebCrawler(config=_browser_config(c4)) as crawler:
        return await crawler.arun(url=url, config=run_config)


def _output_dir() -> str:
    """Directory to write captures to (CRAWL4AI_OUTPUT_DIR or the temp dir)."""
    out = os.environ.get("CRAWL4AI_OUTPUT_DIR") or tempfile.gettempdir()
    os.makedirs(out, exist_ok=True)
    return out


def _url_slug(url: str) -> str:
    """Stable, filesystem-safe short name for a URL."""
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------
@mcp.tool(
    name="crawl4ai_scrape_url",
    annotations={
        "title": "Scrape a URL to Markdown",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def crawl4ai_scrape_url(params: ScrapeUrlInput) -> str:
    """Fetch a single web page and return it as LLM-ready Markdown.

    Renders JavaScript via a headless browser (Crawl4AI/Playwright), strips
    boilerplate, and returns clean Markdown suitable for feeding to a model or
    a RAG pipeline. Read-only; it does not log in, submit forms, or modify
    anything.

    Args:
        params (ScrapeUrlInput): Validated input containing:
            - url (str): absolute http(s) URL to scrape.
            - css_selector (Optional[str]): keep only matching regions.
            - fit_markdown (bool): pruned main-content Markdown (default True).
            - bypass_cache (bool): re-fetch instead of using the cache.
            - timeout_ms (int): per-page navigation timeout (1000–120000).
            - response_format (ResponseFormat): 'markdown' or 'json'.

    Returns:
        str: For 'markdown', the page Markdown (possibly truncated with a
        marker). For 'json', an object:
        {
            "url": str,            # final URL after redirects
            "success": bool,
            "status_code": int|null,
            "error_message": str|null,
            "markdown": str        # empty on failure
        }
        On failure returns a string beginning with "Error: ".

    Examples:
        - "Get me the readable text of https://example.com" -> url=that.
        - "Just the <article> of this blog post" -> css_selector="article".
        - Don't use for content behind a login — this tool doesn't authenticate.
    """
    try:
        result = (
            await _crawl(
                [params.url],
                fit=params.fit_markdown,
                bypass_cache=params.bypass_cache,
                timeout_ms=params.timeout_ms,
                css_selector=params.css_selector,
            )
        )[0]
    except RuntimeError as exc:  # missing dependency -> actionable setup message
        return f"Error: {exc}"
    except Exception as exc:  # noqa: BLE001 - surface any crawl failure to the agent
        return _crawl_error(exc, params.url)

    if not getattr(result, "success", False):
        return (
            f"Error: failed to scrape {params.url} "
            f"(status {getattr(result, 'status_code', None)}): "
            f"{getattr(result, 'error_message', None) or 'unknown error'}"
        )

    if params.response_format is ResponseFormat.MARKDOWN:
        return _extract_markdown(result, params.fit_markdown) or (
            f"(no extractable content at {params.url})"
        )
    return json.dumps(_result_to_dict(result, params.fit_markdown), indent=2, ensure_ascii=False)


@mcp.tool(
    name="crawl4ai_scrape_many",
    annotations={
        "title": "Scrape multiple URLs to Markdown",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def crawl4ai_scrape_many(params: ScrapeManyInput) -> str:
    """Scrape several URLs concurrently and return their Markdown.

    Same engine as ``crawl4ai_scrape_url`` but batched through Crawl4AI's
    ``arun_many`` for throughput. Read-only. Individual pages can fail without
    failing the whole batch — check each entry's ``success``.

    Args:
        params (ScrapeManyInput): Validated input containing:
            - urls (list[str]): 1–20 absolute http(s) URLs.
            - fit_markdown (bool): pruned main-content Markdown (default True).
            - bypass_cache (bool): re-fetch instead of using the cache.
            - timeout_ms (int): per-page navigation timeout (1000–120000).
            - response_format (ResponseFormat): 'json' (default) or 'markdown'.

    Returns:
        str: For 'json', an object:
        {
            "count": int,          # URLs processed
            "succeeded": int,
            "results": [
                {"url": str, "success": bool, "status_code": int|null,
                 "error_message": str|null, "markdown": str}
            ]
        }
        For 'markdown', each page's Markdown concatenated under a
        "# <url>" header. On a dependency/setup error returns "Error: ...".

    Examples:
        - "Summarize these three docs pages" -> urls=[...], response_format="markdown".
        - "Fetch these 10 URLs and tell me which 404'd" -> response_format="json".
    """
    try:
        results = await _crawl(
            params.urls,
            fit=params.fit_markdown,
            bypass_cache=params.bypass_cache,
            timeout_ms=params.timeout_ms,
        )
    except RuntimeError as exc:  # missing dependency -> actionable setup message
        return f"Error: {exc}"
    except Exception as exc:  # noqa: BLE001
        return _crawl_error(exc, f"{len(params.urls)} URLs")

    dicts = [_result_to_dict(r, params.fit_markdown) for r in results]

    if params.response_format is ResponseFormat.MARKDOWN:
        blocks = []
        for d in dicts:
            body = d["markdown"] if d["success"] else (
                f"_Error: {d['error_message'] or 'failed'} (status {d['status_code']})_"
            )
            blocks.append(f"# {d['url']}\n\n{body}")
        return "\n\n---\n\n".join(blocks)

    payload = {
        "count": len(dicts),
        "succeeded": sum(1 for d in dicts if d["success"]),
        "results": dicts,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


@mcp.tool(
    name="crawl4ai_extract_schema",
    annotations={
        "title": "Extract structured records via a CSS schema",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def crawl4ai_extract_schema(params: ExtractSchemaInput) -> str:
    """Extract repeating structured records from a page using a CSS schema.

    Instead of Markdown, this returns typed JSON: for every element matching
    ``base_selector`` it reads each declared field by its CSS ``selector``.
    Ideal for lists/tables/cards (products, search results, rows) where you want
    clean columns rather than prose. Selector-based, so no LLM tokens are spent
    on the extraction itself. Read-only.

    Args:
        params (ExtractSchemaInput): Validated input containing:
            - url (str): absolute http(s) URL.
            - base_selector (str): selector for each repeating record.
            - fields (list[FieldSpec]): each with name, selector, type
              ('text' | 'attribute' | 'html'), and attribute (when
              type='attribute').
            - bypass_cache (bool), timeout_ms (int).

    Returns:
        str: JSON object:
        {
            "url": str,
            "base_selector": str,
            "count": int,          # records found
            "records": [ {"<field name>": "<value>", ...}, ... ]
        }
        On failure, a string starting with "Error: ".

    Examples:
        - Product grid -> base_selector="div.product", fields=[
            {"name": "title", "selector": "h2"},
            {"name": "url", "selector": "a", "type": "attribute", "attribute": "href"}]
        - Don't use for articles/prose — use crawl4ai_scrape_url for Markdown.
    """
    schema = {
        "name": "extraction",
        "baseSelector": params.base_selector,
        "fields": [
            {
                "name": f.name,
                "selector": f.selector,
                "type": f.type.value,
                **({"attribute": f.attribute} if f.type is FieldType.ATTRIBUTE else {}),
            }
            for f in params.fields
        ],
    }
    try:
        result = await _crawl_extract(
            params.url,
            schema=schema,
            bypass_cache=params.bypass_cache,
            timeout_ms=params.timeout_ms,
        )
    except RuntimeError as exc:  # missing dependency / bad session file
        return f"Error: {exc}"
    except Exception as exc:  # noqa: BLE001
        return _crawl_error(exc, params.url)

    if not getattr(result, "success", False):
        return (
            f"Error: failed to load {params.url} "
            f"(status {getattr(result, 'status_code', None)}): "
            f"{getattr(result, 'error_message', None) or 'unknown error'}"
        )

    raw = getattr(result, "extracted_content", None)
    try:
        records = json.loads(raw) if raw else []
    except (TypeError, ValueError):
        records = []
    payload = {
        "url": getattr(result, "url", params.url),
        "base_selector": params.base_selector,
        "count": len(records) if isinstance(records, list) else 0,
        "records": records,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


@mcp.tool(
    name="crawl4ai_deep_crawl",
    annotations={
        "title": "Deep-crawl linked pages to depth N",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def crawl4ai_deep_crawl(params: DeepCrawlInput) -> str:
    """Breadth-first crawl from a start URL, following links to depth N.

    Fetches the start page, then its links, and so on up to ``max_depth`` —
    capped at ``max_pages`` total (a hard safety limit) — and returns Markdown
    for each page. Stays on the start URL's domain unless ``include_external``
    is set. Read-only. Use this for "grab this docs section / site area"; use
    ``crawl4ai_scrape_many`` when you already have the exact URL list.

    Args:
        params (DeepCrawlInput): Validated input containing:
            - url (str): start URL.
            - max_depth (int): link-hops to follow (0–3).
            - max_pages (int): total-page cap (1–50).
            - include_external (bool): allow off-domain links.
            - fit_markdown (bool): pruned Markdown per page.
            - timeout_ms (int): per-page navigation timeout.

    Returns:
        str: JSON object:
        {
            "start_url": str,
            "max_depth": int,
            "count": int,          # pages returned (<= max_pages)
            "pages": [
                {"url": str, "depth": int|null, "success": bool,
                 "status_code": int|null, "markdown": str}
            ]
        }
        On failure, a string starting with "Error: ".
    """
    try:
        results = await _deep_crawl(
            params.url,
            max_depth=params.max_depth,
            max_pages=params.max_pages,
            include_external=params.include_external,
            timeout_ms=params.timeout_ms,
        )
    except RuntimeError as exc:  # missing dependency / unsupported SDK feature
        return f"Error: {exc}"
    except Exception as exc:  # noqa: BLE001
        return _crawl_error(exc, params.url)

    pages = []
    for r in results:
        meta = getattr(r, "metadata", None) or {}
        success = bool(getattr(r, "success", False))
        pages.append(
            {
                "url": getattr(r, "url", None),
                "depth": meta.get("depth"),
                "success": success,
                "status_code": getattr(r, "status_code", None),
                "markdown": _extract_markdown(r, params.fit_markdown) if success else "",
            }
        )
    payload = {
        "start_url": params.url,
        "max_depth": params.max_depth,
        "count": len(pages),
        "pages": pages,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


@mcp.tool(
    name="crawl4ai_screenshot",
    annotations={
        "title": "Screenshot a page to a PNG file",
        "readOnlyHint": False,  # writes a PNG to the local filesystem
        "destructiveHint": False,
        "idempotentHint": False,  # re-fetches the live page; content may differ
        "openWorldHint": True,
    },
)
async def crawl4ai_screenshot(params: PageCaptureInput) -> str:
    """Capture a full-page PNG screenshot and save it to disk.

    Renders the page in the headless browser and writes a full-page PNG to
    ``CRAWL4AI_OUTPUT_DIR`` (or the system temp dir). Returns the file path and
    size — not the image bytes — to keep the model's context small; open or send
    the file to view it. (A variant could return an MCP image for inline
    rendering.) Read-only with respect to the target site; it does write one
    local file.

    Args:
        params (PageCaptureInput): Validated input containing:
            - url (str): URL to screenshot.
            - timeout_ms (int): per-page navigation timeout.

    Returns:
        str: JSON object:
        {
            "url": str,
            "screenshot_path": str,   # local PNG path
            "bytes": int
        }
        On failure, a string starting with "Error: ".
    """
    try:
        result = await _crawl_screenshot(params.url, timeout_ms=params.timeout_ms)
    except RuntimeError as exc:
        return f"Error: {exc}"
    except Exception as exc:  # noqa: BLE001
        return _crawl_error(exc, params.url)

    if not getattr(result, "success", False):
        return (
            f"Error: failed to load {params.url} "
            f"(status {getattr(result, 'status_code', None)}): "
            f"{getattr(result, 'error_message', None) or 'unknown error'}"
        )
    b64 = getattr(result, "screenshot", None)
    if not b64:
        return (
            f"Error: no screenshot was captured for {params.url} "
            "(the page may not have finished rendering)."
        )
    try:
        data = base64.b64decode(b64)
    except (ValueError, TypeError) as exc:
        return f"Error: could not decode screenshot for {params.url}: {exc}"

    path = os.path.join(_output_dir(), f"{_url_slug(params.url)}.png")
    with open(path, "wb") as handle:
        handle.write(data)
    return json.dumps(
        {"url": params.url, "screenshot_path": path, "bytes": len(data)},
        indent=2,
        ensure_ascii=False,
    )


@mcp.tool(
    name="crawl4ai_capture_pdf",
    annotations={
        "title": "Save a page as a PDF file",
        "readOnlyHint": False,  # writes a PDF to the local filesystem
        "destructiveHint": False,
        "idempotentHint": False,  # re-fetches the live page; content may differ
        "openWorldHint": True,
    },
)
async def crawl4ai_capture_pdf(params: PageCaptureInput) -> str:
    """Render a page and save it as a PDF file.

    Loads the page in the headless browser and writes a full PDF to
    ``CRAWL4AI_OUTPUT_DIR`` (or the system temp dir). Returns the file path and
    size rather than the bytes, to keep the model's context small — open or send
    the file to view it. Read-only with respect to the target site; it writes
    one local file.

    Args:
        params (PageCaptureInput): Validated input containing:
            - url (str): URL to capture.
            - timeout_ms (int): per-page navigation timeout.

    Returns:
        str: JSON object:
        {
            "url": str,
            "pdf_path": str,   # local PDF path
            "bytes": int
        }
        On failure, a string starting with "Error: ".
    """
    try:
        result = await _crawl_pdf(params.url, timeout_ms=params.timeout_ms)
    except RuntimeError as exc:
        return f"Error: {exc}"
    except Exception as exc:  # noqa: BLE001
        return _crawl_error(exc, params.url)

    if not getattr(result, "success", False):
        return (
            f"Error: failed to load {params.url} "
            f"(status {getattr(result, 'status_code', None)}): "
            f"{getattr(result, 'error_message', None) or 'unknown error'}"
        )
    raw = getattr(result, "pdf", None)
    if not raw:
        return (
            f"Error: no PDF was captured for {params.url} "
            "(the page may not have finished rendering)."
        )
    if isinstance(raw, str):  # some SDK builds return base64 text
        try:
            data = base64.b64decode(raw)
        except (ValueError, TypeError) as exc:
            return f"Error: could not decode PDF for {params.url}: {exc}"
    else:
        data = raw

    path = os.path.join(_output_dir(), f"{_url_slug(params.url)}.pdf")
    with open(path, "wb") as handle:
        handle.write(data)
    return json.dumps(
        {"url": params.url, "pdf_path": path, "bytes": len(data)},
        indent=2,
        ensure_ascii=False,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def _selfcheck() -> int:
    """List registered tools without starting the stdio server or a browser."""
    import asyncio

    tools = asyncio.run(mcp.list_tools())
    print(f"{mcp.name}: {len(tools)} tool(s) registered")
    for tool in tools:
        print(f"  - {tool.name}: {(tool.description or '').splitlines()[0]}")
    return 0


if __name__ == "__main__":
    import sys

    if "--selfcheck" in sys.argv:
        raise SystemExit(_selfcheck())
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        raise SystemExit(0)
    mcp.run()  # stdio transport
