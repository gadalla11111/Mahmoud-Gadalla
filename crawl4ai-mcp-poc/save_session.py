#!/usr/bin/env python3
"""Create a saved browser session for authenticated Crawl4AI scraping.

Opens a real (headed) browser so you can log in by hand, then writes Playwright
"storage state" (cookies + localStorage) to a JSON file. Point the MCP server at
that file via the ``CRAWL4AI_STORAGE_STATE`` env var and every scrape reuses the
logged-in session.

Prereqs:
    pip install -r requirements.txt
    crawl4ai-setup          # (or: python -m playwright install chromium)

Usage:
    python save_session.py <login_url> <output.json>
    # e.g.
    python save_session.py https://example.com/login session.json

Then:
    export CRAWL4AI_STORAGE_STATE="$PWD/session.json"
    python server.py        # scrapes now run authenticated

Notes:
    - Needs a display (headed browser); run it on your workstation, not a
      headless CI box.
    - Respect each site's Terms of Service and automation/anti-bot policies.
      Some sites (e.g. Instagram) actively disallow automated logins.
    - Sessions expire — regenerate when scrapes start returning logged-out
      pages.
"""

import sys


def main(start_url: str, out_path: str) -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "Playwright is not installed. Run:\n"
            "  pip install -r requirements.txt && crawl4ai-setup",
            file=sys.stderr,
        )
        return 1

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(start_url)
        print(f"A browser window opened at {start_url}.")
        print("Log in / navigate as needed, then press Enter here to save the session...")
        input()
        context.storage_state(path=out_path)
        browser.close()

    print(
        f"\nSaved session to {out_path}. Use it with:\n"
        f'  export CRAWL4AI_STORAGE_STATE="{out_path}"'
    )
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python save_session.py <login_url> <output.json>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
