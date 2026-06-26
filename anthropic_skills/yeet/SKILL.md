---
name: yeet
description: Stage, commit, push, and open (or update) a GitHub pull request in one flow. Handles branch creation off main, conventional-commit messages, repo checks, upstream-tracking push, PR-template discovery, and draft/ready state — including reusing an existing PR if one is already open for the branch.
auto-trigger:
  - '"yeet", "ship it", "commit and open a PR", "push this and make a PR"'
  - local changes are ready and need to become a commit + PR in one step
  - end of a task where the deliverable is a pushed PR
do-not-trigger:
  - fixing failing CI on an existing PR (use gh-fix-ci)
  - addressing review comments on an existing PR (use gh-address-comments)
  - committing without opening a PR, or when the user hasn't asked to push
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []
---

# yeet — commit, push, and open a PR in one flow

Stage, commit, push, and open a GitHub PR in one flow.

## Environment note

No `gh` CLI here — use git for commit/push and the **GitHub MCP tools** (`mcp__github__*`) for the PR:
- `create_pull_request` (set `draft: true` per repo convention)
- `list_pull_requests` (head branch filter) — detect an existing open PR to update instead
- `update_pull_request` — edit title/body or flip draft→ready

Always push with `git push -u origin <branch>`. Retry network failures with exponential backoff (2s, 4s, 8s, 16s).

## Workflow

1. **Branch.** If on the default branch (`main`/`master`), create a feature branch first — never commit straight to default. Otherwise stay on the current branch.
2. **Stage & commit.** Stage changes and commit with a conventional message: `<type>(<scope>): <subject>` where type ∈ `feat | fix | docs | style | refactor | test | chore`. Honor the repo's commit-trailer requirements.
3. **Checks.** Run the repo's checks/linters (the pre-commit hook here is DiffGate). Install deps only if needed. Fix or surface failures before pushing.
4. **Push.** `git push -u origin <branch>` with backoff retries.
5. **PR.** Discover a template in priority order: `.github/pull_request_template.md` → `.github/PULL_REQUEST_TEMPLATE.md` → files under a `PULL_REQUEST_TEMPLATE/` dir. Then:
   - **No open PR** → create a **draft** PR, body filled from the template.
   - **Existing open PR** → update it, preserving meaningful existing content.

## PR body conventions

- Explain the **why** before the **what**.
- Backticks for code/paths; fenced blocks for transcripts/logs; GitHub permalinks for referenced code.
- No generic filler in verification sections — state what was actually run.
- Preserve existing PR content when updating rather than overwriting.
