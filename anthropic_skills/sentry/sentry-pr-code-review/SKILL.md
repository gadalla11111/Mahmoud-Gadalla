---
name: sentry-pr-code-review
description: Review a pull request for issues detected by Sentry's Seer bug-prediction, surfacing likely production bugs before merge. Uses the Sentry MCP to pull predicted issues for the PR's changes and cross-reference them against the diff.
auto-trigger:
  - '"review this PR with Sentry", "check for predicted bugs", "Seer review"'
  - pre-merge review where Sentry Seer bug prediction is available
do-not-trigger:
  - fixing an already-reported production issue (use sentry-fix-issues)
  - general code review with no Sentry/Seer context (use change-impact / ultracode review phase)
allowed-tools: Read, Grep, Glob, Bash
---

# sentry-pr-code-review — Seer bug-prediction PR review

**Prerequisite:** the Sentry MCP server configured, with Seer bug prediction enabled for the org/repo.

## Workflow

1. **Resolve the PR** and its changed files.
2. **Pull Seer predictions** for the PR via the Sentry MCP — likely bugs introduced by the diff.
3. **Cross-reference** each prediction against the actual changed code; discard false positives with a one-line reason.
4. **Report** the surviving predictions ranked by severity, each with the file/line and the suggested fix.
5. **Optionally fix** the high-confidence ones after approval (hand off to `sentry-fix-issues` style root-cause discipline).

## Rules

- Treat Seer output as a signal, not a verdict — confirm against the code before flagging.
- Don't block the PR on low-confidence predictions; surface them as notes.
