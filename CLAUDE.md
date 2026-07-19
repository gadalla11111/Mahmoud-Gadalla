# CLAUDE.md

Guidance for AI assistants (Claude Code and others) working in this repository.

## What this repository is

This is **not a single application** — it is a personal **aggregation repository**
(`gadalla11111/mahmoud-gadalla`) that collects several **independent, self-contained
AI-agent / plugin projects** side by side. There is no root build, no shared package
graph, and no single test suite. Each top-level directory is its own project with its
own toolchain, conventions, and (in one case) its own `CLAUDE.md`.

Treat the top-level directories as separate repos that happen to live together. Before
doing anything, identify **which sub-project** a task belongs to and work inside that
sub-project's tooling — do not try to build or test the repo as a whole.

## Repository map

```
Mahmoud-Gadalla/
├── ruflo/                  # Vendored + customized "Ruflo" (ruvnet/claude-flow) v3.28.0
│                           #   Enterprise AI agent orchestration meta-harness.
│                           #   TypeScript (primary) + Rust workspace + Python.
│                           #   HAS ITS OWN CLAUDE.md + AGENTS.md — defer to them.
├── qoder-plugins-publish/  # 16 authored Qoder plugins + Python publishing automation
├── rulebook-ai/            # Python package "rulebook-ai" — manifest + lockfile only
│                           #   (pyproject.toml + uv.lock; source not vendored here)
├── social_media_review/    # A content-strategy deliverable (markdown, not code)
├── research/               # Reference research briefs on external tools (markdown, not code)
├── crawl4ai-mcp-poc/       # PoC: MCP server wrapping Crawl4AI (Python/FastMCP, stdio)
└── uv.lock                 # ⚠ Orphaned lockfile (see "Known loose ends")
```

## Where do I work? (task routing)

| If the task concerns…                                        | Go to…                    |
|--------------------------------------------------------------|---------------------------|
| Agent orchestration, swarms, MCP, the `ruflo`/`claude-flow` CLI, its plugins | `ruflo/` (read `ruflo/CLAUDE.md` first) |
| Publishing / packaging the Chinese-market business plugins   | `qoder-plugins-publish/`  |
| The `rulebook-ai` Python package (deps, lockfile)            | `rulebook-ai/`            |
| Social-media / content-review writing                        | `social_media_review/`    |
| Reference research / evaluations of external tools & repos    | `research/`               |
| Building/using the Crawl4AI MCP scraping server (PoC)         | `crawl4ai-mcp-poc/`       |

If a request is ambiguous about which project it targets, ask before editing — these
projects are unrelated and a change in one is meaningless in another.

---

## Sub-project: `ruflo/`

### What it is
A **vendored and periodically re-synced copy** of ruvnet's **Ruflo / claude-flow** —
an "agent meta-harness for Claude Code and Codex" that adds 100+ specialized agents,
swarm coordination, self-learning memory, federation, and MCP integration. The npm
`package.json` is named `claude-flow` and currently sits at **v3.28.0** (branding is
"Ruflo"; version strings differ across manifests, e.g. `.claude-plugin/plugin.json`
still reads `claude-flow` `2.5.0`). The git history shows this tree is refreshed in
bulk (e.g. `Update ruflo: v3.5.0 -> v3.28.0`), so treat most of it as **upstream code**.

### ⚠ It has its own CLAUDE.md — use it
`ruflo/CLAUDE.md` (large, authoritative) and `ruflo/AGENTS.md` are the real source of
truth for anything inside `ruflo/`. **Read `ruflo/CLAUDE.md` before working there.** It
documents the swarm orchestration model, 3-tier model routing, the V3 CLI (26 commands),
the 60+ agent types, the SendMessage/teams comms system, and its behavioral rules. Do
not re-derive those conventions from this file — defer to the nested one.

### Layout (high level)
- `v3/` — the active V3 implementation. Notable: `v3/@claude-flow/{cli,shared,guidance}`
  (published TS packages), `v3/crates/` (Rust), `v3/mcp/`, `v3/agents/`, `v3/plugins/`,
  `v3/src/`, `v3/__tests__/`.
- `plugins/` — **37** first-party `ruflo-*` Claude Code plugins (e.g. `ruflo-core`,
  `ruflo-swarm`, `ruflo-sparc`, `ruflo-security-audit`, …).
- `.claude-plugin/` — Claude Code **plugin marketplace** manifest (`marketplace.json`,
  ~35 plugins) + `plugin.json` + hooks. This makes `ruflo/` installable as a marketplace.
- `.claude/`, `.agents/`, `.harness/` — agent/harness runtime config.
- `bin/`, `scripts/`, `services/` (`cognitum-analytics`), `docs/`, `tests/`, `verification/`.
- `Cargo.toml` — a **Rust workspace** with members `v3/crates/ruflo-federation-peer` and
  `v3/plugins/gastown-bridge` (the manifest comment notes ruflo is primarily TypeScript
  and this exists so analyzers see the Rust components).

### Toolchain & commands (run inside `ruflo/`)
- **Node ≥ 20**, ES modules. Package manager artifacts for both npm (`package-lock.json`)
  and pnpm (`pnpm-lock.yaml`) are present.
- `npm run build` (`tsc`), `npm run dev` (`tsx watch src/index.ts`).
- `npm test` (`vitest`), `npm run test:security` (`vitest run v3/__tests__/security/`).
- `npm run lint` builds/lints inside `v3/@claude-flow/cli`.
- `npm run security:audit` (`npm audit --audit-level high`).
- Rust components build with `cargo build` from `ruflo/` (workspace root).

### Working rule
This is upstream-tracking code. Prefer **minimal, surgical** changes and follow the
patterns already in the touched files. A local edit here can be overwritten on the next
bulk re-sync — if a change must survive, make that explicit in the commit message.

---

## Sub-project: `qoder-plugins-publish/`

### What it is
A **staging + publishing pipeline** for **16 Qoder-produced plugins** authored by
Mahmoud Gadalla, targeting Chinese-market professional domains (1688/Alibaba Cloud
seller tooling, consulting, contract management, corporate finance & tax, corporate
legal, equity research, investment banking, marketing, PE/VC, product design/management,
litigation, wealth management, tech services). Source of truth for the catalog is
`INDEX.md`; per-plugin submission metadata is in `submission_manifest.json`.

### Layout
```
qoder-plugins-publish/
├── plugins/<name>/               # 16 self-contained, publishable plugins
│   ├── .qoder-plugin/plugin.json # Plugin manifest (bilingual name/description)
│   ├── .mcp.json                 # Connector / MCP server config
│   ├── CONNECTORS.md             # Connector documentation
│   ├── README.md / README_EN.md  # User docs (Chinese + English)
│   ├── assets/icon.svg
│   └── skills/<skill>/SKILL.md   # Individual skills (+ scripts/, references/)
├── automate.py                   # Master orchestrator (setup/prep/submit/deps/status/all)
├── apphub_bulk_submit.py         # Playwright submitter for the Qoder apphub
├── submission_manifest.json      # 16 plugins' submission data (name, display, category)
├── INDEX.md                      # Generated catalog of the 16 plugins
├── EXCLUSIONS.md                 # What was intentionally NOT copied in, and why
└── APPHUB_SUBMISSION.md          # Manual submission prep pack
```

### Publishing workflow (run inside `qoder-plugins-publish/`)
The pipeline is driven by `automate.py`:
```
python automate.py setup    # check deps (playwright, gh CLI) and offer to install
python automate.py prep     # regenerate zips + submission_manifest.json + INDEX.md
python automate.py submit   # submit all 16 plugins via Playwright (login must be done)
python automate.py status   # show pipeline state (zips, manifest, session, deps)
python automate.py all      # prep + submit
```
`apphub_bulk_submit.py --login` opens a browser to log into qoder.com once (cookies are
saved to `.qoder_session` for reuse); `--start-from <plugin>` resumes an interrupted run.
Requires `pip install playwright && playwright install chromium`.

### Conventions & gotchas
- **Chinese content is first-class.** Many plugin/skill directory names and `SKILL.md`
  files use Chinese characters (e.g. `skills/合同对比/SKILL.md`). Keep everything UTF-8;
  when listing files with git, `git config core.quotepath false` gives readable names.
- Each `plugins/<name>/` must stay **self-contained and publishable** on its own.
- `.gitignore` here excludes **regeneratable** artifacts: `zips/*.zip`, runtime `data/`,
  `cache/`, `.qoder-plugin/installation_state.json`. Don't commit those.
- The Playwright form `SELECTORS` in `apphub_bulk_submit.py` are best-guess and may need
  adjustment after inspecting the live apphub form DOM.
- `automate.py` assumes the GitHub CLI at a Windows path (`C:\Program Files\GitHub CLI\gh.exe`)
  — this pipeline was authored to run on Windows.

### Note on the Qoder vs Claude Code plugin formats
`ruflo/plugins/*` are **Claude Code** plugins (`.claude-plugin/`). `qoder-plugins-publish/plugins/*`
are **Qoder** plugins (`.qoder-plugin/plugin.json`, `skills/<name>/SKILL.md`). They share
the "plugin with skills" shape but are different ecosystems — don't cross conventions.

---

## Sub-project: `rulebook-ai/`

### What it is
The dependency manifest + lockfile for the Python package **`rulebook-ai` v0.2.1**
("AI rulebook management for large language models"). **Only `pyproject.toml` and
`uv.lock` are checked in here** — the actual package source (`src/rulebook_ai/`, `tests/`)
is **not vendored in this repo**, even though `pyproject.toml` references them (packages
under `src/`, a `rulebook-ai` console script, `tests/` for pytest). So this directory is
effectively the project's **packaging metadata only**.

### Toolchain (from `pyproject.toml`)
- **uv**-managed, `requires-python >= 3.11`, setuptools build backend.
- Lint/format: **ruff** (line length 100). Types: **mypy** (strict-ish). Tests: **pytest**
  with `unit` / `integration` markers, orchestrated via **tox** (`unit`, `integration` envs).
- Notable deps: `anthropic`, `openai`, `google-generativeai`, `playwright`, `duckduckgo-search`.
- Regenerate the lock with `uv lock` (the repo history shows periodic `uv lock --upgrade`).

Because the source isn't present, most real code work on `rulebook-ai` happens in its
upstream repo — here you can update dependencies/lockfile but cannot run its tests.

---

## Sub-project: `social_media_review/`

A single deliverable: `kuji-eg-content-review.md` — a content-strategy **swipe file /
genre teardown** for kuji.eg ("Claude & AI, made practical for marketers and developers").
This is **documentation/writing, not code**. Edit it as prose; there is nothing to build
or test. Heads-up: it cites skill paths like `anthropic_skills/social-audit` and
`anthropic_skills/claude-api` that were removed with the ANA Blueprint (see "Known loose
ends") and **no longer resolve in-tree** — treat them as historical references, not live paths.

---

## Sub-project: `research/`

Reference material, not code: dated markdown **research briefs / evaluations of external
tools and repositories** (e.g. `ai-agent-tooling-scan-2026-07.md`, a scan of external
AI/agent/dev-tooling projects mapped to this repo's sub-projects). Nothing here is
vendored, integrated, or built — these are notes to inform decisions. Add new scans as
`research/<topic>-<YYYY-MM>.md`; there is nothing to build or test.

---

## Sub-project: `crawl4ai-mcp-poc/`

A **self-contained proof-of-concept MCP server** (Python / FastMCP, stdio) that wraps
[Crawl4AI](https://github.com/unclecode/crawl4ai) to turn URLs into LLM-ready Markdown —
built to validate the top pick from `research/web-scraping-tooling-scan-2026-07.md`. It
exposes six tools (`crawl4ai_scrape_url`, `crawl4ai_scrape_many`,
`crawl4ai_extract_schema`, `crawl4ai_deep_crawl`, `crawl4ai_screenshot`,
`crawl4ai_capture_pdf`) and can scrape behind a login via a saved session
(`CRAWL4AI_STORAGE_STATE` + `save_session.py`) or through a proxy (`CRAWL4AI_PROXY`).

- **Toolchain:** Python 3.11+. `pip install -r requirements.txt` (into a venv), then
  `crawl4ai-setup` to install the Playwright browser Crawl4AI drives.
- **Verify:** `python server.py --selfcheck` lists the tools without a browser (Crawl4AI is
  imported lazily); `python smoke_test.py` does a live scrape. Register with Claude Code via
  its `.mcp.json` / `claude mcp add`.
- **Scope:** deliberately minimal — read-only scraping, no auth/deep-crawl/screenshots. See
  its own `README.md`. Self-contained; don't wire its deps into other sub-projects.

---

## Repository-wide conventions

### Git & branching
- Development for the current task happens on the branch
  **`claude/claude-md-documentation-5pyioo`**; do not push to `main` or another branch
  without explicit permission.
- Push with `git push -u origin <branch>`; on network failure, retry with exponential
  backoff. After pushing, open a **draft PR** if one isn't already open for the branch.
- If this branch's PR is already merged, treat follow-up work as a fresh change: restart
  the branch from the latest default branch rather than stacking onto merged history.

### Encoding
UTF-8 throughout. Chinese (and other non-ASCII) content is normal here — never "fix"
it to ASCII. Prefer the dedicated file/search tools, which handle Unicode cleanly.

### Vendored / large trees
`ruflo/` and `qoder-plugins-publish/plugins/` contain thousands of files (ruflo alone is
~5k tracked files). When searching, **scope to the relevant sub-project** rather than the
whole repo, and lean on `Grep`/`Glob` instead of shelling out to `find`/`grep`.

### Don't invent a root build
There is no root `package.json`, no root `pyproject.toml`, no Makefile, and no combined
CI that builds everything. Never run a "build the repo" step at the root — always `cd`
into the specific sub-project and use its documented commands.

## Known loose ends (be aware, don't be surprised)

- **Root `uv.lock` is orphaned.** It locks an editable project named `anthropic-cookbook`
  (v0.1.0, deps include `claude-agent-sdk`, `jupyter`, `voyageai`, …), but there is **no
  root `pyproject.toml`** in the repo (not tracked, not ignored — simply absent). Treat
  the root `uv.lock` as **stale metadata**; it does not describe a buildable project here.
  Don't rely on it, and flag it rather than acting on it if a task seems to depend on it.
- **`rulebook-ai/` has no source** (manifest + lock only), as noted above.
- **Version strings drift inside `ruflo/`** across `package.json` (3.28.0), the plugin
  manifest (2.5.0), and doc headers — this is expected for a bulk-vendored upstream tree.
- **Git history shows a larger, since-removed system — don't try to revive it uninvited.**
  Before today's four sub-projects were assembled, this repo hosted an **"ANA Blueprint"**
  self-evolving-agent project: `ANA_BLUEPRINT.md`, a ~338-line root `CLAUDE.md` full of
  routing tables, an `anthropic_skills/<name>/SKILL.md` skill library, a `.memory/` store,
  a `ClaudeForge/` tree, and a `.github/workflows/ana-blueprint.yml` CI loop. It was
  **intentionally stripped out** in the `Finalize` commit (`29779d0b`). So `git log` /
  `git show` will surface files, skills, and conventions that **do not exist in the current
  tree**. Treat them as deliberately-removed history, not as scaffolding to restore — if a
  task seems to want that system back, confirm first.

## Quick reference: per-project entry points

| Project                   | Read first                          | Build/run                                  |
|---------------------------|-------------------------------------|--------------------------------------------|
| `ruflo/`                  | `ruflo/CLAUDE.md`, `ruflo/README.md`| `npm run build` / `npm test` (Node ≥ 20); `cargo build` |
| `qoder-plugins-publish/`  | `README.md`, `INDEX.md`             | `python automate.py <setup\|prep\|submit\|status\|all>` |
| `rulebook-ai/`            | `pyproject.toml`                    | `uv lock` (no source to run here)          |
| `social_media_review/`    | `kuji-eg-content-review.md`         | n/a (prose)                                |
| `research/`               | `ai-agent-tooling-scan-2026-07.md`  | n/a (prose)                                |
| `crawl4ai-mcp-poc/`       | `crawl4ai-mcp-poc/README.md`        | `python server.py --selfcheck`; `smoke_test.py` |
