---
name: claude-md-audit
description: >
  Three-in-one CLAUDE.md maintenance skill. Audits every CLAUDE.md in the
  project for: (1) broken @-imports and markdown links, (2) drift against
  the last week of git history (deleted files, renamed paths, removed deps),
  (3) tech stack sections out of sync with manifest files. Read-only —
  returns punch lists and diff summaries, never edits. Use when asked
  "is my CLAUDE.md accurate?", "check my docs for staleness", "are
  the @-imports still valid?", or as part of a weekly sync routine.
allowed-tools: [Read, Glob, Grep, "Bash(find:*)", "Bash(cat:*)", "Bash(git log:*)", "Bash(git diff:*)", "Bash(git status:*)", "Bash(test:*)", "Bash(ls:*)"]
argument-hint: "[--links] [--drift] [--deps] [--all] [days=7] [manifest-path]"
auto-trigger:
  - "audit CLAUDE.md", "is my CLAUDE.md good", "improve project instructions"
  - CLAUDE.md has grown large or conflicts with actual behaviour
  - onboarding a new project
do-not-trigger:
  - day-to-day coding tasks
  - when instructions are working fine

---

# CLAUDE.md Audit

Three read-only sub-checks, run together or individually via flags. Default (no flags): run all three.

---

## --links — Broken @-imports and markdown links

Check every CLAUDE.md in the project:

```bash
find . -name "CLAUDE.md" -not -path "*/node_modules/*"
```

For each file:
1. Extract all `@path` imports (lines matching `@[./~]`)
2. Extract all markdown links: `[text](path)` where path is a file reference (not URL)
3. For each path: `test -f <resolved-path>` — report missing as broken
4. Return: `file:line → broken path` for every failure

Output format:
```
## Broken Links
CLAUDE.md:12  @./docs/setup.md  ← file not found
README.md:45  [guide](docs/old.md)  ← file not found
```

---

## --drift — CLAUDE.md drift against git history

Check every CLAUDE.md against the last N days (default 7) of git history:

```bash
git log --since="7 days ago" --name-status --oneline
```

Flag CLAUDE.md sections that reference:
- Files deleted in the last N days: `git log --diff-filter=D --name-only`
- Files renamed: `git log --diff-filter=R --name-status`
- Dependencies removed from manifests (cross-reference with --deps)

Output format:
```
## Drift Findings
CLAUDE.md:34  references "src/auth/legacy.py" — deleted 3 days ago (commit abc1234)
CLAUDE.md:67  references "utils/helpers.ts" — renamed to "utils/common.ts" (commit def5678)
```

---

## --deps — Tech stack section vs. manifests

Detect manifest files and diff against Tech Stack sections in CLAUDE.md:

Manifests to check:
- `package.json` → `dependencies` + `devDependencies`
- `requirements.txt` / `pyproject.toml` → packages
- `go.mod` → module dependencies
- `Cargo.toml` → `[dependencies]`

For each CLAUDE.md with a "Tech Stack" or "Dependencies" section:
- Extract listed items
- Compare against current manifest
- Report: added (in manifest, not in CLAUDE.md), removed (in CLAUDE.md, not in manifest), renamed

Output format:
```
## Dependency Drift
Added (in manifest, missing from CLAUDE.md):  fastapi 0.110.0
Removed (in CLAUDE.md, not in manifest):       flask
```

---

## Rules

- **Read-only**: never edit any file. Return findings as a punch list only.
- **Skip gracefully**: if a source is unavailable (no git history, no manifest), note the gap and continue.
- **Under 60 lines output**: if findings exceed this, group by severity (broken / stale / minor).
- **No false positives**: only flag paths that are actually missing, not just changed.
