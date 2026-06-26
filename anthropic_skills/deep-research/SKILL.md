---
name: deep-research
description: >
  Exhaustive multi-cycle research skill for complex topics requiring structured
  investigation across many sources. Use when the user asks for thorough
  investigation of a topic — not a quick lookup. Conducts structured research
  cycles (landscape → deep investigation → verification → synthesis) with
  mandatory clarification before starting and user-approval of the plan before
  executing. Trigger on: "research X thoroughly", "comprehensive overview",
  "due diligence", "literature review", "technology survey", "deep dive into".
  Requires: WebSearch and WebFetch tools (or Brave/Tavily MCP if available).
  WHEN TO USE THIS vs ultra-search: deep-research = structured cycles on a
  complex topic with synthesis into a report. ultra-search = maximum breadth on
  a specific question fast. If unsure, deep-research for decisions, ultra-search
  for lookups.
allowed-tools: [WebSearch, WebFetch, Bash, Read, Write]
auto-trigger:
  - complex multi-step research question spanning many sources
  - "research X thoroughly"
  - "give me a comprehensive overview of"
  - due-diligence research for a business or technical decision
  - literature review or technology survey
  - "deep dive"
  - "thorough investigation"
  - "exhaustive research"
do-not-trigger:
  - quick one-source lookup (use ultra-search)
  - factual questions answerable from training knowledge
  - when the user needs breadth fast without a synthesis report (use ultra-search)
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []
---

# Deep Research

Transforms a research question into an exhaustive, evidence-based report through systematic cycles. Quality over speed — this is the expensive path, used when quick search isn't enough and a synthesized judgment is needed.

---

## deep-research vs ultra-search — choose once, don't switch mid-task

| Signal | Use deep-research | Use ultra-search |
|---|---|---|
| Output needed | Synthesized report with confidence levels | Structured source list with findings |
| Topic type | Complex, multi-faceted, decision-driving | Specific question, fast lookup |
| Time horizon | Hours to days of real work | Minutes |
| Verification needed | Yes — claims cross-checked across themes | Partial — de-duplication only |
| Typical chain position | First in: `deep-research → prove-claims → prd-generator` | First in: `ultra-search → prove-claims → output` |

If the user needs both breadth AND a report, start with ultra-search for the landscape pass, then feed findings into deep-research synthesis.

---

## Phase 0 — Clarify (always first)

Ask 2–3 focused questions before doing anything:
- What decision or action does this research feed?
- How deep? (survey / comprehensive / exhaustive)
- Any sources, time ranges, domains, or languages to exclude?
- Is there a target audience for the report (technical / executive / general)?

Reflect understanding back to the user. Wait for confirmation before proceeding.

---

## Phase 1 — Research Plan

Present to the user before executing:
- 3–5 major themes identified for investigation
- Key questions per theme
- Tool sequence (which search tool for which pass)
- Source tier targets (see below)
- Estimated depth (number of cycles)
- Confidence threshold you'll use (default: Medium = 2+ independent sources)

Wait for user approval. Adjust based on feedback.

---

## Source Tier Hierarchy

Apply this to every claim you make:

| Tier | Type | Examples | Weight |
|---|---|---|---|
| **T1 Primary** | Original data, official docs, peer-reviewed papers | Company filings, RFC specs, academic journals, official APIs | Highest |
| **T2 Secondary** | Analysis of primary sources | Industry reports (Gartner, McKinsey), expert commentary, established tech blogs | Medium |
| **T3 Tertiary** | Aggregated/curated summaries | Wikipedia, comparison sites, news summaries | Low — use to find T1/T2, not as evidence |
| **T0 Unverified** | Unattributed, single-source, opinion without evidence | Anonymous forums, marketing copy, social media | Flag explicitly; never cite as fact |

Every claim in the report must be tagged with its source tier. Never present T3 or T0 as primary evidence.

---

## Phase 2 — Research Cycles (per theme)

Each theme requires all three steps. Don't synthesize until all themes are done.

### Step A — Landscape (broad, T2–T3 ok for orientation)

- Use WebSearch / Brave Search with `max_results=20`
- Goal: map the space, not settle it. Extract patterns, trends, initial hypotheses, knowledge gaps
- Note contradictions — they're the most valuable signal for what to investigate next
- Output: 5–10 bullet findings + list of gaps for Step B

### Step B — Deep Investigation (targeted, T1–T2 required)

- Use WebFetch / Tavily `search_depth="advanced"` targeting gaps identified in Step A
- Minimum 5 reasoning steps before forming conclusions
- Seek: expert opinions, contrarian views, quantitative data, edge cases, failure modes
- For each key claim: find a T1 or T2 source. If you can't, it goes to Unverified.

### Step C — Verification (mandatory, never skip)

- Cross-validate every key claim across ≥2 independent sources at T2 or above
- Flag unverifiable claims explicitly with `⚠ UNVERIFIED — reason`
- Note source recency — outdated T1 sources can be worse than fresh T2
- Resolve contradictions explicitly: don't silently pick one, explain the disagreement

### Dead-End Protocol

If a theme yields insufficient evidence after Steps A + B:
1. State clearly: "Insufficient evidence found for [theme] — [N] searches returned no T1/T2 sources"
2. Recommend alternative approaches (different search terms, primary source contact, paid reports)
3. Continue with remaining themes — don't block synthesis on one dry well

---

## Confidence Scoring

Tag every major finding with a confidence level:

| Level | Criteria |
|---|---|
| **High** | ≥3 independent T1/T2 sources agree; no significant contradictions |
| **Medium** | 2 T2 sources agree; or 1 T1 source with no contradictions |
| **Low** | Single source, or sources disagree on key points |
| **Unverified** | No T1/T2 source found; claim comes from T3 or T0 only |

State the confidence level prominently in the report — not buried in footnotes.

---

## Phase 3 — Synthesis

Combine findings across all themes. Aim for insight, not transcription.

```markdown
## Executive Summary
[3–5 bullets: the most important findings and their confidence levels]

## Theme 1: [Name]
### Findings
[Key conclusions with confidence tags]
### Evidence
[Source citations: Title, URL, Tier, Date accessed]
### Confidence: High / Medium / Low / Unverified

[repeat per theme]

## Cross-Theme Patterns
[What emerged across themes that wasn't visible in any single theme]

## Contradictions and Open Questions
[Where sources disagree — explain the disagreement, don't resolve it silently]

## Source Quality Notes
[Which sources were T1, which were T2, any notable gaps]

## Recommended Next Steps
[What decisions this enables, what still needs investigation]
```

---

## Tool Hierarchy

| Task | Preferred tool |
|---|---|
| Broad landscape | WebSearch (Brave: `max_results=20`) |
| Deep targeted | WebFetch (Tavily: `search_depth="advanced"`) |
| Known URL retrieval | WebFetch direct |
| Primary source content | WebFetch direct on official URL |
| Fallback (no MCP) | Bash `curl` — note limitation in report |

When MCP servers aren't available, state the limitation in the report's Source Quality Notes.

---

## Quality Gates

- Every claim: cite a source URL + tier, or tag `⚠ UNVERIFIED — reason`
- No extrapolation beyond what evidence supports
- Contradictions between sources: surfaced and explained, never silently resolved
- Dry themes: acknowledged with alternative recommendations, not omitted
- Confidence levels: present in the executive summary, not just buried in body

After synthesis, offer to pipe the findings into `prove-claims` for any specific claim that needs triple-source verification before use in a high-stakes document.
