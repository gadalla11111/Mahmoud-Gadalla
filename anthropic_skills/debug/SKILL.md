---
name: debug
description: >
  Systematic debugging skill. Use when the user has a bug, failure, or
  unexpected behavior they need diagnosed. Follows scientific method:
  gather symptoms → form hypotheses → test in isolation → confirm root
  cause → fix. Supports --diagnose-only mode to separate diagnosis from
  fix. Uses subagents to isolate investigation context from conversation.
allowed-tools: [Read, Bash, Grep, Glob, Write, AskUserQuestion, Task]
argument-hint: "[--diagnose] [issue description]"
---

# Debug

Systematic debugging using scientific method. Isolates investigation into a subagent to keep main context lean and preserve the conversation for human decisions.

**Flags**:
- `--diagnose` — find root cause only, do not apply a fix. Returns a Root Cause Report. Use when you want to validate before committing.

---

## Phase 0 — Check for active sessions

Before starting new investigation:
```bash
ls .debug/*.md 2>/dev/null | grep -v resolved | head -5
```
If active sessions exist and no new issue was described: list them (status, hypothesis, next action) and ask which to resume or whether to start new.

---

## Phase 1 — Gather symptoms

Use AskUserQuestion for each (don't ask all at once):

1. **Expected behavior** — what should happen?
2. **Actual behavior** — what happens instead?
3. **Error messages** — paste exact text or describe
4. **Timeline** — when did this start? Did it ever work?
5. **Reproduction** — minimal steps to trigger

Confirm readiness before proceeding.

---

## Phase 2 — Investigation

Create `.debug/{slug}.md` to track state across context resets.

```markdown
# Debug: {slug}
## Symptoms
[filled from Phase 1]

## Hypotheses
| # | Hypothesis | Status | Evidence |
|---|---|---|---|

## Investigation log
[timestamped findings]

## Root cause
[when found]
```

Work through hypotheses in priority order (most likely first):

- Read relevant source files, configs, logs
- Run minimal reproduction steps
- Eliminate hypotheses with evidence, not assumptions
- Each step addresses ONE specific question

### Incremental testing rule
Do not fix multiple things at once. Each test changes exactly one variable. Document what was tested and what the result was.

---

## Phase 3 — Root cause report

Before applying any fix:

```
## Root Cause Found

**Issue**: [slug]
**Root cause**: [specific statement — file:line or system behavior]
**Confidence**: High / Medium / Low
**Evidence**: [list of specific findings]
**Files involved**: [list]

## Fix strategies
1. [Preferred] — [rationale]
2. [Alternative] — [tradeoffs]
```

Present to user. In `--diagnose` mode: stop here and offer options (fix now / plan fix / manual).

---

## Phase 4 — Fix

Only after root cause is confirmed:

- Apply minimal change that addresses the root cause
- Do not fix adjacent issues in the same change
- Run relevant tests to confirm green
- Update `.debug/{slug}.md` with fix summary and mark resolved

```markdown
## Resolution
**Fix applied**: [what changed, file:line]
**Tests run**: [commands and results]
**Status**: RESOLVED
```

---

## Checkpoint protocol

If investigation hits a human-verify point (e.g., "does this reproduce on your machine?"):
- Pause and present a checkpoint with: what was checked, what was found, what needs human confirmation
- After user responds, continue or adjust hypotheses

---

## Rules

- **Ground findings in evidence**: every anomaly must cite a specific file, line, commit, or log entry
- **No speculation without evidence**: if data is insufficient, say so and ask for more
- **Root cause before fix**: never apply a fix without a confirmed root cause
- **Idempotent fixes**: prefer changes that are safe to apply twice
- **One change at a time**: never bundle multiple fixes in a single step
