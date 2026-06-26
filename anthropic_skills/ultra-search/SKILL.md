---
name: ultra-search
description: >
  Maximum-coverage search skill. Automatically combines multiple search tools
  in parallel — broad context, deep extraction, direct URL retrieval — without
  requiring the user to name which tool to use. Use when a simple WebSearch
  isn't enough and the user needs comprehensive, source-documented results fast.
  Trigger on: "find everything about X", "search thoroughly", "leave no stone
  unturned", "competitive research", "prior searches returned insufficient results".
  WHEN TO USE THIS vs deep-research: ultra-search = maximum breadth on a specific
  question, fast, structured source list. deep-research = complex topic,
  multi-cycle structured investigation, synthesized judgment report. If the user
  needs a decision-quality report with confidence levels, use deep-research.
  If the user needs a comprehensive source sweep fast, use ultra-search.
allowed-tools: [WebSearch, WebFetch, Bash, Read, Write]
auto-trigger:
  - exhaustive search across many sources needed
  - "find everything about X", "search thoroughly", "leave no stone unturned"
  - prior searches returned insufficient results
  - competitive or market research requiring breadth
  - fast lookup needing multiple tool passes
do-not-trigger:
  - single-source quick lookup
  - narrow technical questions answerable in one search
  - when a synthesized report with confidence levels is needed (use deep-research)
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Ultra Search

Maximizes search coverage by automatically routing queries across all available tools in parallel. Activates whenever the task is multi-faceted or a single search pass is clearly insufficient.

---

## ultra-search vs deep-research — choose once

| Signal | Use ultra-search | Use deep-research |
|---|---|---|
| Output needed | Comprehensive source list + findings | Synthesized report with confidence levels |
| Speed | Fast — parallel passes | Slow — structured cycles |
| Topic type | Specific question, breadth needed | Complex, multi-faceted, decision-driving |
| Verification | De-duplication + contradiction flagging | Full cross-validation per theme |
| Typical chain | `ultra-search → prove-claims → output skill` | `deep-research → prove-claims → prd-generator` |

When both breadth and a report are needed: run ultra-search first, feed its findings into deep-research's synthesis phase.

---

## Step 1 — Decompose (before searching)

Break the query into core components:
- Identify key concepts, sub-questions, and relationships
- Determine which passes cover which aspects
- Plan: which queries run in parallel vs. which depend on prior results

---

## Step 2 — Parallel Primary Search (spawn all in one turn)

Run all non-dependent queries simultaneously. Don't serialize what can run in parallel.

| Pass | Tool | Config | Purpose |
|---|---|---|---|
| Broad context | WebSearch (Brave) | `max_results=20` | Landscape, high-signal sources |
| Deep targeted | WebFetch (Tavily) | `search_depth="advanced"` | Academic, technical, specialist content |
| Alternative framing | WebSearch | Different query phrasing | Catch what first framing missed |
| Recency pass | WebSearch | Filter: past 6–12 months | Fast-moving topics, breaking developments |

Document every query string used — reproducibility matters.

---

## Step 3 — Content Retrieval (sequential, for known URLs)

After parallel passes surface promising sources:
- Use WebFetch direct URL for any T1 source identified (official docs, papers, filings)
- Retrieve full page content, not just snippets
- Prioritize sources that appeared in ≥2 parallel passes (convergent signal)

---

## Step 4 — Source Triage

Before synthesis, triage what you found:

| Tier | Type | Treatment |
|---|---|---|
| **T1 Primary** | Official docs, original data, peer-reviewed | Lead finding — cite directly |
| **T2 Secondary** | Expert analysis, established reports | Supporting evidence |
| **T3 Tertiary** | Summaries, aggregators | Use to find T1/T2, not as evidence |
| **T0 Unverified** | Single-source, anon, marketing | Flag explicitly: `⚠ UNVERIFIED` |

Contradiction rule: if T1 and T2 disagree, surface the disagreement — don't pick one silently.

---

## Step 5 — Synthesis

Combine findings across all passes. Organize by topic, not by tool.

```markdown
## Summary
[1–2 sentences: what was found and with what confidence]

## Findings
### [Topic 1]
- [Finding] — [Source Title](URL) [Tier]
- [Finding] — [Source Title](URL) [Tier]

### [Topic 2]
...

## Contradictions
[Where sources disagree — explain, don't resolve]

## Gaps
[What the search didn't find — topics with insufficient coverage]

## Sources
| # | Title | URL | Tier | Tool | Date |
|---|---|---|---|---|---|
```

---

## Tool Usage Rules

| Tool | When |
|---|---|
| WebSearch (Brave) | Initial broad pass, general context, pagination with offset |
| WebFetch (Tavily) | Deeper analysis, academic/technical, content extraction |
| WebFetch direct | When URL is already known from a prior pass |
| Bash `curl` | Fallback when MCP tools unavailable — note in output |

**Always use multiple tools.** A single-tool result is a draft, not a finished search.

---

## Source Documentation (mandatory)

Every result must include:
- Full URL
- Title
- Tier (T1/T2/T3/T0)
- Tool used to retrieve it
- Date accessed

Quote only what is directly retrievable. Flag inferred or synthesized content.

---

## Escalation to deep-research

After ultra-search, offer to escalate when:
- Findings are contradictory and need structured reconciliation
- The topic is decision-critical and confidence levels per claim are needed
- The user asks for a synthesized report, not just a source list

Say: "I've completed the coverage sweep. Want me to run this through deep-research for a structured synthesis with confidence levels?"
