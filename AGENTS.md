# AGENTS.md

Guidance for AI assistants (Claude Code, Qoder, Copilot, and others) working in this repository.

## What this repository is

This is **not a single application** — it is a personal **aggregation repository** (`gadalla11111/Mahmoud-Gadalla`) that collects several **independent, self-contained AI-agent / plugin projects** side by side. There is no root build, no shared package graph, and no single test suite. Each top-level directory is its own project with its own toolchain, conventions, and (in some cases) its own `AGENTS.md` or `CLAUDE.md`.

**Treat the top-level directories as separate repos that happen to live together.** Before doing anything, identify **which sub-project** a task belongs to and work inside that sub-project's tooling — do not try to build or test the repo as a whole.

## Repository map

```
Mahmoud-Gadalla/
├── ruflo/                  # Vendored AI agent orchestration meta-harness (TypeScript + Rust + Python)
│                           # HAS ITS OWN CLAUDE.md + AGENTS.md - defer to them
├── qoder-plugins-publish/  # 16 authored Qoder plugins + Python publishing automation
├── rulebook-ai/            # Python package "rulebook-ai" - manifest + lockfile only
├── social_media_review/    # Content-strategy deliverable (markdown, not code)
├── research/               # Reference research briefs (markdown, not code)
├── crawl4ai-mcp-poc/       # PoC: MCP server wrapping Crawl4AI (Python/FastMCP, stdio)
├── CLAUDE.md               # AI guidance for the root-level repo
├── AGENTS.md               # This file
└── uv.lock                 # Orphaned lockfile
```

## Task routing

| If the task concerns... | Go to... |
|---|---|
| Agent orchestration, swarms, MCP, the `ruflo` CLI, its plugins | `ruflo/` (read `ruflo/CLAUDE.md` first) |
| Publishing / packaging the Qoder plugins | `qoder-plugins-publish/` |
| The `rulebook-ai` Python package (deps, lockfile) | `rulebook-ai/` |
| Social-media / content-review writing | `social_media_review/` |
| Reference research / evaluations of external tools | `research/` |
| Building/using the Crawl4AI MCP scraping server (PoC) | `crawl4ai-mcp-poc/` |

If a request is ambiguous about which project it targets, **ask before editing** — these projects are unrelated and a change in one is meaningless in another.

## General rules for AI assistants

1. **Read sub-project AGENTS.md/CLAUDE.md first** — each sub-project has its own conventions.
2. **Never run cross-project builds** — there is no root `package.json`, `pyproject.toml`, or CI pipeline.
3. **Do not modify `ruflo/` upstream code** without explicit instruction — it is vendored and periodically re-synced.
4. **Keep PRs focused on a single sub-project** — do not mix changes across sub-projects.
5. **Match existing style** in each sub-project independently.
6. **Identify yourself** as an AI assistant in any commit messages or PR descriptions you generate.
