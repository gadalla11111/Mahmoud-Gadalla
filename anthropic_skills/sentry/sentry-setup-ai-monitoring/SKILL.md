---
name: sentry-setup-ai-monitoring
description: Instrument AI/LLM agent monitoring with Sentry — capture model calls, token usage, latency, and errors for OpenAI, Anthropic, and LangChain integrations. Directly relevant to Claude-agent code in this repo (claude_agent_sdk, managed_agents).
auto-trigger:
  - '"monitor my AI agent", "track token usage / LLM latency", "instrument Anthropic/OpenAI calls"'
  - adding observability to Claude/LLM agent code
do-not-trigger:
  - general (non-AI) Sentry SDK setup (use a sentry setup skill)
  - fixing an existing issue (use sentry-fix-issues)
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# sentry-setup-ai-monitoring — instrument LLM agents

**Prerequisite:** the Sentry SDK for the project's language installed and initialized (Python here).

## What it captures

Model calls, token usage, latency, and errors across **OpenAI, Anthropic, and LangChain** integrations.

## Workflow

1. **Detect** the AI framework(s) in use — for this repo, the Anthropic SDK in `claude_agent_sdk/` and `managed_agents/`.
2. **Enable AI monitoring** in the Sentry init — turn on the relevant integration and set the traces sample rate so spans are captured.
3. **Wrap agent entry points** so each model call becomes a monitored span with token/latency attributes.
4. **Verify** — run a sample call and confirm the AI monitoring spans appear in Sentry.

## Notes

- Don't log full prompts/completions if they may contain sensitive data — sample or redact.
- Token + latency attributes are the high-value signal; capture those even when sampling bodies out.
- Pairs with this repo's cost work: Sentry latency/token spans complement `sipcode` token economics.
