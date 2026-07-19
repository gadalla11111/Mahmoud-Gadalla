#!/usr/bin/env python3
"""End-to-end smoke test for the crawl4ai PoC.

Calls the server's real tool function against a live, stable page and prints a
snippet of the Markdown. Proves the whole path works (Crawl4AI -> browser ->
Markdown) outside of an MCP client.

Prereqs:
    pip install -r requirements.txt
    crawl4ai-setup

Usage:
    python smoke_test.py                 # scrapes https://example.com
    python smoke_test.py https://...     # scrape a URL of your choice
"""

import asyncio
import sys

from server import ScrapeUrlInput, crawl4ai_scrape_url


async def main(url: str) -> int:
    out = await crawl4ai_scrape_url(ScrapeUrlInput(url=url, response_format="markdown"))
    if out.startswith("Error:"):
        print(out)
        return 1
    print(f"OK: scraped {url} -> {len(out):,} chars of Markdown\n")
    print(out[:800])
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    raise SystemExit(asyncio.run(main(target)))
