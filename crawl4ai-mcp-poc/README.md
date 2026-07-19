# crawl4ai-mcp-poc

A minimal **proof-of-concept MCP server that wraps [Crawl4AI](https://github.com/unclecode/crawl4ai)**,
turning any URL into **LLM-ready Markdown** through two MCP tools. Built to
validate the top recommendation from
[`research/web-scraping-tooling-scan-2026-07.md`](../research/web-scraping-tooling-scan-2026-07.md):
*crawl4ai — OSS Python, MCP-native, stealth + auth, LLM-markdown — as the
default scrape→markdown engine.*

It's intentionally small: one file (`server.py`), two read-only tools, stdio
transport. It's a **starting skeleton** you can drop into Claude Code or
`ruflo`, not a productionised server.

## What it exposes

| Tool | Does | Key args |
|------|------|----------|
| `crawl4ai_scrape_url` | One URL → Markdown (JS-rendered, boilerplate stripped) | `url`, `css_selector`, `fit_markdown`, `bypass_cache`, `timeout_ms`, `response_format` |
| `crawl4ai_scrape_many` | 1–20 URLs → per-URL Markdown/JSON, concurrent | `urls`, `fit_markdown`, `bypass_cache`, `timeout_ms`, `response_format` |
| `crawl4ai_extract_schema` | One URL → structured JSON records via a CSS schema | `url`, `base_selector`, `fields[]` (name/selector/type/attribute), `bypass_cache`, `timeout_ms` |

Both are `readOnly` / `openWorld` (they fetch external pages; they don't log
in, submit forms, or write anything).

## Layout

```
crawl4ai-mcp-poc/
├── server.py         # the FastMCP server (3 tools + lazy Crawl4AI adapter)
├── save_session.py   # capture a login session for authenticated scraping
├── requirements.txt  # mcp[cli] + crawl4ai
├── smoke_test.py     # live end-to-end check (scrapes example.com)
├── .mcp.json         # example Claude Code registration
└── README.md
```

## Setup

```bash
cd crawl4ai-mcp-poc
python -m venv .venv && source .venv/bin/activate      # optional but recommended
pip install -r requirements.txt
crawl4ai-setup        # installs the Playwright browser runtime Crawl4AI drives
```

## Verify

```bash
# 1) Structural check — lists the registered tools, no browser needed:
python server.py --selfcheck
#    crawl4ai_mcp: 2 tool(s) registered
#      - crawl4ai_scrape_url: Fetch a single web page and return it as LLM-ready Markdown.
#      - crawl4ai_scrape_many: Scrape several URLs concurrently and return their Markdown.

# 2) Live end-to-end check — actually scrapes a page:
python smoke_test.py                    # -> prints Markdown from example.com
python smoke_test.py https://news.ycombinator.com

# 3) Interactive — poke the tools in the MCP Inspector:
npx @modelcontextprotocol/inspector python server.py
```

> `--selfcheck` only needs `mcp` + `pydantic` (Crawl4AI is imported lazily), so
> it works before `crawl4ai-setup`. The live checks need the full setup.

**Troubleshooting the live checks.** If a scrape returns
`Error: ... BrowserType.launch: Executable doesn't exist ...` or Playwright
prints "run `playwright install`", the installed Playwright's pinned browser
build doesn't match what's on disk. Fix it with `crawl4ai-setup` (preferred) or
`python -m playwright install chromium-headless-shell`. The `--selfcheck` above
still passes in that state — only the live browser fetch is affected.

## Register it

**Claude Code** — copy [`.mcp.json`](./.mcp.json) into your project (edit the
absolute path + interpreter), or:

```bash
claude mcp add crawl4ai -- /abs/path/to/.venv/bin/python /abs/path/to/crawl4ai-mcp-poc/server.py
```

**ruflo** — register it the same way you wire any stdio MCP server into the
harness (point the command at the venv's `python` and this `server.py`); the
three tools then show up alongside ruflo's own MCP tools.

## Authenticated scraping (saved session)

By default the tools scrape anonymously. To scrape **behind a login**, capture a
browser session once and point the server at it:

```bash
# 1) Log in by hand; save cookies + localStorage to a file:
python save_session.py https://SITE/login session.json

# 2) Tell the server to use it — every scrape now runs authenticated:
export CRAWL4AI_STORAGE_STATE="$PWD/session.json"
python server.py
```

The session path is read from the **environment** (not a tool argument), so an
agent can't point the server at arbitrary files and credentials never pass
through the model. Sessions expire — re-run `save_session.py` when scrapes start
coming back logged-out.

> **On the Instagram thread:** this makes *authenticated* scraping possible, but
> logging a bot into Instagram still runs into its ToS, 2FA, and checkpoints.
> `save_session.py` needs you to complete a real login by hand, and IG may still
> block automated reuse — treat it as "possible with care", not "solved".

## Design notes

- **Lazy Crawl4AI import.** `server.py` imports `crawl4ai` only on the first
  tool call, so the module stays importable (and the server registrable) before
  the heavy browser runtime is installed. A missing dependency returns an
  actionable "run `crawl4ai-setup`" message instead of crashing on import.
- **`fit_markdown` by default.** Returns Crawl4AI's pruned main-content Markdown
  to keep model context lean; set `fit_markdown=false` for the raw page.
- **Context guard.** Markdown output is capped at 200k chars with a truncation
  marker, so a giant page can't blow up the client's context — narrow it with
  `css_selector` instead.
- **Version-tolerant.** Markdown extraction handles both the newer
  `MarkdownGenerationResult` object and the older plain-string return.

## Caveats & next steps

- **Auth / anti-bot.** Scraping is read-only. It **can** run behind a login via
  a saved session (see "Authenticated scraping" above), but it still doesn't
  defeat hard anti-bot walls or sites like Instagram that disallow automated
  logins — mind each site's ToS, and reach for `browser-use` for genuinely
  agentic, interactive navigation.
- **Not yet implemented (deliberately):** deep crawling (follow links to depth
  N), screenshots, LLM-based extraction, and per-request proxy config. Crawl4AI
  supports all of these — add them as further tools when the PoC graduates.
- **No evals yet.** A natural follow-up (per the `mcp-builder` skill) is a small
  eval set that asks a model to answer questions only answerable by scraping.
