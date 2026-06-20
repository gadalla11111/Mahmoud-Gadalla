# Agent Harness Instructions

## Session scope
- Work on ONE feature per session. Read `PROGRESS.md` first; pick the first item with `"passes": false`.
- At session start: re-read `PROGRESS.md` and `test-results.json`.
- At session end: `commit-on-stop.sh` will auto-commit, but prefer committing at meaningful checkpoints yourself.

## Evidence requirement
Before writing any result to `test-results.json`, you MUST open at least one piece of evidence:
- A screenshot in `screenshots/`
- A log file
- The actual `test-results.json` to read its current state

The `verify-gate.sh` hook enforces this. It will block your write if you skip it.

## Handoff
Update `PROGRESS.md` as you work. Structure:
```
## Feature: <name>
Status: IN_PROGRESS | DONE
Last action: <what you did>
Next: <what remains>
```

## Kill switch
If `AGENT_STOP` exists at the project root, all tool calls are blocked. The operator placed it there intentionally.

## Steering
If `STEER.md` exists, read it — the operator wants to redirect you mid-run. It will be shown once and cleared.
