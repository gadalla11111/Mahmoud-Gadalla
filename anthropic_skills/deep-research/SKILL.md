---
name: deep-research
description: >
  Exhaustive multi-cycle research skill. Use when the user asks for thorough
  investigation of a complex topic — not a quick lookup. Conducts structured
  research cycles (landscape → deep investigation → synthesis) with mandatory
  clarification before starting and user-approval of the plan before executing.
  Requires: WebSearch and WebFetch tools (or Brave/Tavily MCP if available).
allowed-tools: [WebSearch, WebFetch, Bash, Read, Write]
auto-trigger:
  - complex multi-step research question spanning many sources
  - "research X thoroughly", "give me a comprehensive overview of"
  - due-diligence research for a business or technical decision
  - literature review or technology survey
do-not-trigger:
  - quick one-source lookup
  - factual questions answerable from memory

---

# Deep Research

Transforms a research question into an exhaustive, evidence-based report through systematic cycles. Quality over speed — this is the expensive path, used when quick search isn't enough.

---

## Phase 0 — Clarify (always first)

Ask 2–3 focused questions before doing anything:
- What decision or action does this research feed?
- How deep? (survey / comprehensive / exhaustive)
- Any sources, time ranges, or domains to exclude?

Reflect understanding back to the user. Wait for confirmation before proceeding.

---

## Phase 1 — Research plan

Present to the user before executing:
- 3–5 major themes identified for investigation
- Key questions per theme
- Tool sequence (which search tool for which pass)
- Estimated depth (number of cycles)

Wait for user approval.

---

## Phase 2 — Research cycles (per theme)

Each theme requires all three steps:

### Step A — Landscape (broad)
- Use WebSearch / Brave Search with `max_results=20` for broad context
- Extract: key patterns, underlying trends, initial hypotheses, critical uncertainties
- Note: knowledge gaps, contradictions, areas needing verification

### Step B — Deep investigation (targeted)
- Use WebFetch / Tavily `search_depth="advanced"` targeting identified gaps
- Minimum 5 reasoning steps before forming conclusions
- Identify: expert opinions, contrarian views, edge cases, quantitative data

### Step C — Verification
- Cross-validate key claims across ≥2 independent sources
- Flag unverifiable claims explicitly
- Note source quality (primary / secondary / opinion)

---

## Phase 3 — Synthesis

Combine findings across all themes into a structured report:

```
## Executive Summary
[3–5 bullet key findings]

## Theme 1: [Name]
### Findings
### Evidence
### Confidence level (High / Medium / Low)

[repeat per theme]

## Contradictions and open questions
## Source quality notes
## Recommended next steps
```

---

## Tool hierarchy

| Task | Preferred tool |
|---|---|
| Broad context | WebSearch (Brave: `max_results=20`) |
| Deep targeted | WebFetch (Tavily: `search_depth="advanced"`) |
| Known URL retrieval | WebFetch directly |
| Interactive verification | Bash `curl` if no MCP available |

When MCP servers aren't available, use WebSearch + WebFetch and note the limitation.

---

## Quality gates

- Every claim must cite a source URL or "unverified — reason"
- No extrapolation beyond what evidence supports
- Contradictions between sources must be surfaced, not silently resolved
- If a theme yields insufficient evidence: say so and recommend additional approaches
