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

Both are `readOnly` / `openWorld` (they fetch external pages; they don't log
in, submit forms, or write anything).

## Layout

```
crawl4ai-mcp-poc/
├── server.py         # the FastMCP server (2 tools + lazy Crawl4AI adapter)
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
two tools then show up alongside ruflo's own MCP tools.

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

- **Auth / anti-bot.** This PoC does plain read-only scraping. It does **not**
  log in — so it does not solve authenticated walls like the Instagram post in
  the other research thread. For that you'd add a Crawl4AI browser profile with
  a saved session (Crawl4AI supports it), or reach for `browser-use`; either way
  mind the target site's ToS.
- **Not yet implemented (deliberately):** structured/CSS-schema extraction,
  deep crawling (follow links to depth N), screenshots, and per-request proxy
  config. Crawl4AI supports all of these — add them as further tools when the
  PoC graduates.
- **No evals yet.** A natural follow-up (per the `mcp-builder` skill) is a small
  eval set that asks a model to answer questions only answerable by scraping.
