---
name: sipcode
description: >
  Token economics toolkit for Claude Code sessions. Routes to the right
  sub-tool based on the user's question:
  - "how much will X cost?" → estimate (pre-flight prediction)
  - "where did my tokens go?" → why (session forensics)
  - "is sipcode actually saving me tokens?" → impact (A/B savings verifier)
  - "prove the headline savings claim" → benchmark (reproducibility proof)
  Use when the user asks about token spend, session cost, or Sipcode itself.
auto-trigger:
  - "how much will this cost", "estimate tokens", "token budget"
  - before starting an L or XL task chain
  - "audit token spend", "why did this cost so much"
do-not-trigger:
  - quick single-turn exchanges
  - sub-100-token tasks

---

# Sipcode — Token Economics Toolkit

Four sub-tools, one entry point. Match the user's question to the right tool below.

---

## estimate — Pre-flight cost prediction

**Triggers**: "how much will X cost?", "is this worth running on Opus?", "estimate the refactor"

Call `sipcode:estimate_task_cost` with:
- `task`: natural-language task description (≥3 chars)
- `cwd`: absolute path to the project root (ask if not provided)

**Presenting results**:
- Show all three models (Opus / Sonnet / Haiku) side-by-side.
- Surface the confidence band honestly — if `confidence: "low"`, say the estimate is heuristic-only.
- Recommend a model grounded in the cost spread: Haiku if within ~10% of Sonnet; Opus if task spans 5+ files.
- Never invent precision. Round to whole cents unless sub-$0.10.

---

## why — Session forensics

**Triggers**: "where did my tokens go?", "audit my last session", "why was that so expensive?"

Call `sipcode:audit_latest_session`. If the user names a session ID prefix, pass it as `session_id`; otherwise omit.

**Presenting results**:
- Lead with the **output ratio** (% of total tokens that were actual code output; 0.3–2% is typical).
- Surface the top 3 leaks with their dollar cost.
- The "RECOVERABLE" number is **potential**, not realized — say so explicitly.
- If session > $10 or output ratio < 0.2%, call it out.
- Do NOT extrapolate one session's savings across many sessions.

---

## impact — Savings verifier

**Triggers**: "is sipcode actually saving me tokens?", "show me the impact", "prove sipcode is working"

Call `sipcode:verify_sipcode_impact`.

**Respect the integrity contract** — key response fields:
- `status`: `"measured"` | `"insufficient-post-data"` | `"no-install-marker"` | `"no-baseline"` | `"no-post-sessions"` | `"window-asymmetry-<N>d-vs-<M>d"`
- `delta`: present **only** when `status === "measured"`. Never compute a savings number when delta is null — the windows aren't comparable.
- `headline`: trust this and surface it verbatim.
- `warningReason`: explains why delta is null when it is.

**When `status === "measured"`**: lead with output-ratio change. Mention token + dollar savings as secondary. Include window-length caveat.

**When `status !== "measured"`**: present the headline and `notes` next-step. Never invent a number. If the user pushes back, explain the structural reason and suggest `since: "YYYY-MM-DD"` or running `sipcode rules --install`.

---

## benchmark — Reproducibility proof

**Triggers**: "what's the proof?", "how much does sipcode actually save?", "run the benchmark"

This is a CLI command, not an MCP tool. Tell the user to run in their terminal:

```
npx sipcode benchmark
```

Quick smoke test (3 tasks, ~15s):
```
npx sipcode benchmark --quick
```

**When they report back**:
- Headline: **median savings %** across 20 tasks (target ~62.6%, typical range 37.4%–80.6%).
- Surface the source breakdown:
  - ~30% from S001 smart manifest
  - ~34% from S021 output compression
  - ~36% from S030 read-once cache
- These are **simulation numbers** against a locked corpus, not a live Claude A/B. Methodology is at `benchmark/METHODOLOGY.md`.
- If measured savings differ significantly from 62.6%, treat it as a real workload signal, not a bug.
