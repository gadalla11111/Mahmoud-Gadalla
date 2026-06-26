---
name: sentry-python-setup
description: Set up the Sentry SDK in a Python application (Django, Flask, FastAPI, or plain Python) — error monitoring, tracing, profiling, and logging. Matches this repo's Python stack (uv, claude_agent_sdk).
auto-trigger:
  - '"add Sentry to this Python app", "set up error monitoring", "install Sentry SDK"'
  - onboarding a Python service/app to Sentry
do-not-trigger:
  - AI/LLM agent monitoring specifically (use sentry-setup-ai-monitoring)
  - a non-Python project (use the matching platform setup skill)
  - fixing an existing issue (use sentry-fix-issues)
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# sentry-python-setup — Sentry SDK for Python

**Prerequisite:** a Sentry project DSN.

## Workflow

1. **Detect the framework** — Django, Flask, FastAPI, or plain Python. Install `sentry-sdk` (via `uv add sentry-sdk` in this repo).
2. **Initialize** `sentry_sdk.init()` at app startup with the DSN. Enable the framework integration automatically detected by the SDK.
3. **Turn on tracing/profiling** — set `traces_sample_rate` (and `profiles_sample_rate` if profiling). Start conservative in production.
4. **Wire logging** — route the app's logging into Sentry so breadcrumbs and error events are captured.
5. **Verify** — trigger a test exception and confirm the event lands in Sentry.

## Notes

- Never commit the DSN if it's treated as a secret — load from env (`.env`, never committed).
- Keep sample rates explicit; don't default to 100% tracing in production.
- For Claude/LLM agent code, layer `sentry-setup-ai-monitoring` on top of this base setup.
