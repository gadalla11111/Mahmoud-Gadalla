"""
automate.py - Master orchestrator for the qoder-plugins-publish workflow.

Subcommands:
    setup    Check Python deps (playwright, gh) and offer to install
    prep     Regenerate zips + submission_manifest.json + INDEX.md
    submit   Submit all 16 plugins to the Qoder apphub (Playwright)
    deps     Pull Dependabot alerts from the mirror repo
    status   Show pipeline state (zips, manifest, session, deps)
    all      Run prep + submit (login must already be done)

Examples:
    python automate.py setup
    python automate.py prep
    python automate.py submit
    python automate.py submit --start-from consulting-delivery
    python automate.py deps --top 20
    python automate.py status
    python automate.py all
"""

import argparse
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

BASE = Path(__file__).parent
PLUGINS_DIR = BASE / 'plugins'
ZIPS_DIR = BASE / 'zips'
INDEX_PATH = BASE / 'INDEX.md'
MANIFEST_PATH = BASE / 'submission_manifest.json'
STORAGE_PATH = BASE / '.qoder_session'
SUBMIT_SCRIPT = BASE / 'apphub_bulk_submit.py'
GH = Path(r'C:\Program Files\GitHub CLI\gh.exe')


def log(msg, level='info'):
    icons = {'info': '[*]', 'ok': '[+]', 'warn': '[!]', 'err': '[-]'}
    print(f'{icons.get(level, "[*]")} {msg}')


def check_deps():
    """Check Python deps. Return dict of {tool: installed_bool}."""
    deps = {}

    # Python deps
    try:
        import playwright  # noqa: F401
        deps['playwright'] = True
    except ImportError:
        deps['playwright'] = False

    # gh CLI
    deps['gh'] = GH.exists()
    deps['gh_auth'] = False
    if deps['gh']:
        try:
            r = subprocess.run([str(GH), 'auth', 'status'], capture_output=True, text=True, timeout=10)
            deps['gh_auth'] = 'Logged in' in r.stdout or 'Logged in' in r.stderr
        except Exception:
            pass

    # Git
    deps['git'] = shutil.which('git') is not None

    return deps


def cmd_setup():
    log('Checking dependencies...')
    deps = check_deps()
    for tool, ok in deps.items():
        log(f'  {tool}: {"installed" if ok else "MISSING"}',
            level='ok' if ok else 'warn')

    if not deps['playwright']:
        log('Installing playwright...')
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'playwright'], check=True)
        log('Installing chromium browser...')
        subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'], check=True)

    if not deps['gh']:
        log('gh CLI not found at expected path. Run: winget install GitHub.cli', level='warn')

    if deps['gh'] and not deps['gh_auth']:
        log('gh is installed but not authenticated. Run:', level='warn')
        log(f'  "{GH}" auth login', level='warn')

    log('Setup complete.', level='ok')


def cmd_prep():
    """Regenerate zips + manifest + INDEX from plugin state."""
    log('Regenerating zips...')
    ZIPS_DIR.mkdir(exist_ok=True)
    for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
        if not plugin_dir.is_dir():
            continue
        manifest = plugin_dir / '.qoder-plugin' / 'plugin.json'
        if not manifest.exists():
            continue
        zip_path = ZIPS_DIR / f'{plugin_dir.name}.zip'
        if zip_path.exists():
            zip_path.unlink()
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
            zf.write(manifest, arcname=f'{plugin_dir.name}/plugin.json')
            for f in sorted(plugin_dir.rglob('*')):
                if not f.is_file() or f == manifest:
                    continue
                arc = f'{plugin_dir.name}/{str(f.relative_to(plugin_dir)).replace(chr(92), "/")}'
                zf.write(f, arc)
    log(f'Built {len(list(ZIPS_DIR.glob("*.zip")))} zips', level='ok')

    log('Regenerating submission_manifest.json...')
    # Hand-curated field structure (mimics APPHUB_SUBMISSION.md format).
    plugins = []
    for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
        mjf = plugin_dir / '.qoder-plugin' / 'plugin.json'
        if not mjf.exists():
            continue
        m = json.loads(mjf.read_text(encoding='utf-8'))
        plugins.append({
            'name': plugin_dir.name,
            'displayEn': m.get('displayNameEn') or m.get('displayName', plugin_dir.name),
            'displayCn': m.get('displayName', plugin_dir.name),
            'descEn': m.get('descriptionEn') or m.get('description', ''),
            'category': m.get('qoderMarket', {}).get('category') or 'Productivity',
            'categoryKey': (m.get('qoderMarket', {}).get('category') or 'productivity').lower().replace(' ', '-'),
        })
    manifest = {'contact': 'gadalla111@gmail.com', 'plugins': plugins}
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
    log(f'Wrote {MANIFEST_PATH.name} ({len(plugins)} plugins)', level='ok')

    log('Regenerating INDEX.md...')
    # Reuse the apphub prep script logic.
    sys.path.insert(0, str(Path.home() / 'AppData' / 'Local' / 'Temp'))
    try:
        import apphub_prep  # type: ignore
        log('INDEX.md regenerated via apphub_prep', level='ok')
    except ImportError:
        log('apphub_prep.py not in temp dir; INDEX.md not regenerated', level='warn')

    log('Prep complete.', level='ok')


def cmd_submit(start_from=None):
    if not SUBMIT_SCRIPT.exists():
        log(f'{SUBMIT_SCRIPT.name} missing', level='err')
        sys.exit(1)
    args = [sys.executable, str(SUBMIT_SCRIPT)]
    if start_from:
        args += ['--start-from', start_from]
    subprocess.run(args)


def cmd_deps(top=10):
    deps = check_deps()
    if not deps['gh']:
        log('gh CLI not installed', level='err')
        sys.exit(1)
    if not deps['gh_auth']:
        log('gh not authenticated. Run: ' + str(GH) + ' auth login', level='err')
        sys.exit(1)

    log(f'Fetching Dependabot alerts (top {top})...')
    r = subprocess.run([
        str(GH), 'api',
        'repos/gadalla11111/Mahmoud-Gadalla/dependabot/alerts?per_page=100&state=open'
    ], capture_output=True, text=True)
    if r.returncode != 0:
        log(f'gh api failed: {r.stderr}', level='err')
        sys.exit(1)
    alerts = json.loads(r.stdout)

    # Cluster by package.
    clusters = {}
    for a in alerts:
        pkg = a.get('dependency', {}).get('package', {}).get('name', '?')
        sev = a.get('security_advisory', {}).get('severity', '?')
        clusters.setdefault(pkg, {}).setdefault(sev, []).append(a)

    print(f'\nTotal open alerts: {len(alerts)}')
    print(f'Distinct packages: {len(clusters)}\n')
    print(f'{"Package":<35} {"crit":>5} {"high":>5} {"mod":>5} {"low":>5} {"total":>6}')
    print('-' * 65)
    rows = []
    for pkg, sevs in clusters.items():
        c = len(sevs.get('critical', []))
        h = len(sevs.get('high', []))
        m = len(sevs.get('moderate', []))
        l = len(sevs.get('low', []))
        rows.append((pkg, c, h, m, l, c + h + m + l))
    rows.sort(key=lambda r: (-r[1], -r[2], -r[5]))
    for pkg, c, h, m, l, t in rows[:top]:
        print(f'{pkg:<35} {c:>5} {h:>5} {m:>5} {l:>5} {t:>6}')


def cmd_status():
    log('Pipeline status:')
    deps = check_deps()
    log(f'  Python playwright: {"installed" if deps["playwright"] else "MISSING"}',
        level='ok' if deps['playwright'] else 'warn')
    log(f'  gh CLI:            {"installed" if deps["gh"] else "MISSING"}',
        level='ok' if deps['gh'] else 'warn')
    log(f'  gh auth:           {"logged in" if deps["gh_auth"] else "NOT logged in"}',
        level='ok' if deps['gh_auth'] else 'warn')

    n_zips = len(list(ZIPS_DIR.glob('*.zip'))) if ZIPS_DIR.exists() else 0
    n_plugins = len([p for p in PLUGINS_DIR.iterdir() if p.is_dir()]) if PLUGINS_DIR.exists() else 0
    log(f'  Plugins staged:    {n_plugins}', level='ok' if n_plugins == 16 else 'warn')
    log(f'  Zips built:        {n_zips}', level='ok' if n_zips == 16 else 'warn')
    log(f'  Manifest:          {"present" if MANIFEST_PATH.exists() else "missing"}',
        level='ok' if MANIFEST_PATH.exists() else 'warn')
    log(f'  INDEX.md:          {"present" if INDEX_PATH.exists() else "missing"}',
        level='ok' if INDEX_PATH.exists() else 'warn')
    log(f'  Apphub session:    {"saved" if STORAGE_PATH.exists() else "not yet (run --login)"}',
        level='ok' if STORAGE_PATH.exists() else 'warn')


def main():
    parser = argparse.ArgumentParser(description='qoder-plugins-publish orchestrator')
    sub = parser.add_subparsers(dest='cmd', required=True)

    sub.add_parser('setup', help='Check + install Python deps')
    sub.add_parser('prep', help='Regenerate zips + manifest + INDEX')

    p_submit = sub.add_parser('submit', help='Submit plugins to apphub')
    p_submit.add_argument('--start-from', metavar='PLUGIN_NAME')

    p_deps = sub.add_parser('deps', help='Pull Dependabot alerts')
    p_deps.add_argument('--top', type=int, default=10, help='Show top N packages (default 10)')

    sub.add_parser('status', help='Show pipeline state')
    sub.add_parser('all', help='Run prep + submit (requires prior --login)')

    args = parser.parse_args()
    if args.cmd == 'setup':
        cmd_setup()
    elif args.cmd == 'prep':
        cmd_prep()
    elif args.cmd == 'submit':
        cmd_submit(args.start_from)
    elif args.cmd == 'deps':
        cmd_deps(args.top)
    elif args.cmd == 'status':
        cmd_status()
    elif args.cmd == 'all':
        cmd_prep()
        cmd_submit()


if __name__ == '__main__':
    main()