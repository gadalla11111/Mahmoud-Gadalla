"""
apphub_bulk_submit.py - Bulk-submit 16 plugins to the Qoder apphub.

Setup (one-time):
    pip install playwright
    playwright install chromium

Usage:
    # Step 1: log in to qoder.com once. Browser opens, you log in manually,
    # cookies saved to .qoder_session for reuse.
    python apphub_bulk_submit.py --login

    # Step 2: submit all 16 plugins.
    python apphub_bulk_submit.py

    # Step 3 (if it crashes): resume from a specific plugin.
    python apphub_bulk_submit.py --start-from consulting-delivery

Selectors:
    The form field names below are best-guess based on the apphub form
    labels you saw ("Display name", "Description", "Category", "Contact",
    "Plugin file"). After your first --login run, inspect the page DOM
    (right-click → Inspect) and adjust SELECTORS if any are wrong.

Required files (siblings of this script):
    submission_manifest.json   - 16 plugins' submission data
    zips/<plugin>.zip          - one zip per plugin
"""

import argparse
import json
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

BASE = Path(__file__).parent
ZIPS_DIR = BASE / 'zips'
MANIFEST_PATH = BASE / 'submission_manifest.json'
STORAGE_PATH = BASE / '.qoder_session'
APPHUB_BASE = 'https://qoder.com/account/apphub-publications'

# Field selectors — adjust after first inspection if needed.
SELECTORS = {
    'display_name':  'input[name="displayName"], input[placeholder*="Display" i]',
    'description':   'textarea[name="description"], textarea[placeholder*="Description" i]',
    'category':      'select[name="category"], [role="combobox"]',
    'contact':       'input[name="contact"], input[placeholder*="Email" i], input[placeholder*="GitHub" i]',
    'zip_upload':    'input[type="file"]',
    'submit':        'button[type="submit"], button:has-text("Submit"), button:has-text("Publish")',
    'success':       'text=/success|submitted|published/i',
}


def load_manifest():
    if not MANIFEST_PATH.exists():
        sys.exit(f'Missing {MANIFEST_PATH.name}. Run prep step first.')
    return json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))


def cmd_login():
    """Open browser, let user log in to qoder.com, save cookies."""
    print('Opening browser for manual login...')
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(APPHUB_BASE)
        print(f'\n>>> Log in to qoder.com in the browser window.')
        print(f'>>> Navigate to {APPHUB_BASE} when done.')
        print(f'>>> This script will save your cookies and close when it detects the page.\n')
        try:
            # Wait up to 5 min for user to log in and reach the publications page.
            page.wait_for_url(f'**{APPHUB_BASE.rsplit("/", 1)[-1]}**', timeout=300_000)
            context.storage_state(path=str(STORAGE_PATH))
            print(f'Session saved to {STORAGE_PATH}')
        except PWTimeout:
            print('Timed out waiting for login. Run --login again.')
        browser.close()


def submit_one(page, plugin):
    """Submit a single plugin. Returns True on success, raises on failure."""
    print(f"  -> {plugin['name']}", end=' ', flush=True)
    page.goto(APPHUB_BASE + '/new', wait_until='networkidle')

    # Wait for form to render.
    page.wait_for_selector(SELECTORS['display_name'], timeout=30_000)

    # Fill text fields.
    page.fill(SELECTORS['display_name'], plugin['displayEn'])
    page.fill(SELECTORS['description'], plugin['descEn'])

    # Category — may be a <select> or a custom combobox.
    try:
        page.select_option(SELECTORS['category'], value=plugin['categoryKey'])
    except Exception:
        # Fallback: click the combobox then the option by text.
        page.click(SELECTORS['category'])
        page.click(f'text="{plugin["category"]}"')

    # Contact.
    page.fill(SELECTORS['contact'], plugin['contact'])

    # Upload zip.
    zip_path = ZIPS_DIR / f"{plugin['name']}.zip"
    if not zip_path.exists():
        raise FileNotFoundError(f'Missing zip: {zip_path}')
    page.set_input_files(SELECTORS['zip_upload'], str(zip_path))

    # Submit.
    page.click(SELECTORS['submit'])

    # Wait for confirmation. Adjust selector if needed.
    page.wait_for_selector(SELECTORS['success'], timeout=60_000)
    print('OK')
    return True


def cmd_submit(start_from=None):
    plugins = load_manifest()
    if start_from:
        plugins = [p for p in plugins if p['name'] >= start_from]
    if not plugins:
        sys.exit('No plugins to submit (check --start-from filter).')

    if not STORAGE_PATH.exists():
        sys.exit(f'Missing {STORAGE_PATH.name}. Run --login first.')

    print(f'Submitting {len(plugins)} plugins...')
    submitted = []
    failed = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(storage_state=str(STORAGE_PATH))
        page = context.new_page()
        for plugin in plugins:
            try:
                submit_one(page, plugin)
                submitted.append(plugin['name'])
            except Exception as e:
                print(f'FAIL: {e}')
                failed.append((plugin['name'], str(e)))
                # Save session state in case we want to resume.
                context.storage_state(path=str(STORAGE_PATH))
        browser.close()

    print(f'\nSubmitted: {len(submitted)}/{len(plugins)}')
    if failed:
        print(f'Failed: {len(failed)}')
        for name, err in failed:
            print(f'  - {name}: {err[:100]}')
        if submitted:
            print(f'\nResume from next one:')
            last = submitted[-1]
            idx = next(i for i, p in enumerate(load_manifest()) if p['name'] == last)
            nxt = load_manifest()[idx + 1]['name'] if idx + 1 < len(load_manifest()) else None
            if nxt:
                print(f'  python apphub_bulk_submit.py --start-from {nxt}')
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Bulk-submit plugins to Qoder apphub.')
    parser.add_argument('--login', action='store_true', help='Open browser for manual login')
    parser.add_argument('--start-from', metavar='PLUGIN_NAME', help='Resume from this plugin')
    args = parser.parse_args()

    if args.login:
        cmd_login()
    else:
        cmd_submit(args.start_from)


if __name__ == '__main__':
    main()