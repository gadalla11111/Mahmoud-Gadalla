---
name: gh-fix-ci
description: Diagnose and fix failing GitHub Actions checks on the open PR for the current branch. Verifies access, resolves the PR, fetches failing-check logs, summarizes the failure, drafts a fix plan, and implements only after explicit approval. Scoped to GitHub Actions — external CI providers (Buildkite, CircleCI) are out of scope; report only their details URL.
auto-trigger:
  - '"fix CI", "fix the failing checks", "CI is red", "make CI pass"'
  - a PR has failing GitHub Actions checks that need diagnosis
  - babysitting/autofixing a PR after a webhook reports a check failure
do-not-trigger:
  - addressing human review comments on a PR (use gh-address-comments)
  - opening a fresh commit + PR from local changes (use yeet)
  - failures from non-GitHub-Actions providers (report the details URL only)
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---

# gh-fix-ci — fix failing GitHub Actions checks

Diagnose and fix failing GitHub Actions checks on the open PR for the current branch.

## Environment note

This repo runs in a remote environment without the `gh` CLI. Use the **GitHub MCP tools** (`mcp__github__*`) for all GitHub access:
- `pull_request_read` with `method: get_status` / `get_check_runs` — resolve check state
- `get_job_logs` / `actions_get` — fetch failing-run logs
- `pull_request_read` with `method: get` — resolve the PR from the current branch

If `gh` is available in a different environment, the equivalent flow is `gh pr checks`, `gh run view --log-failed`.

## Workflow

1. **Resolve the PR.** Determine the current branch and find its open PR (`list_pull_requests` filtered by head branch, or the PR number if the user gave one).
2. **Inspect checks.** Call `get_check_runs` and `get_status`. Identify every check with `conclusion: failure`. Skip non-GitHub-Actions checks — report their `details_url` and move on.
3. **Fetch logs.** For each failing Actions check, pull the job logs (`get_job_logs`, prefer `failed_only` / tail the relevant snippet). Extract the minimal failing snippet plus the run URL.
4. **Summarize.** Present, per failing check: the check name, the failure snippet, and the run URL. Lead with the root cause, not the raw log.
5. **Plan.** Draft a concrete fix plan. For anything non-trivial, surface the plan and **wait for explicit approval before editing code.**
6. **Implement → re-check.** Apply the approved fix, commit, push, then re-read check status to confirm green. If still red, re-diagnose from step 2.

## Rules

- Never edit code before the user approves the plan (unless the task is an explicit "kick it until green" autofix loop).
- One root cause at a time — don't blanket-rewrite to chase a red check.
- Re-check status after every push; the loop's terminal state is all-green or a diagnosed out-of-scope failure.
