---
name: business-consulting
description: >
  Runs a structured management-consulting engagement on a business problem.
  Frames the problem as an issue tree (MECE), forms hypotheses, gathers evidence,
  routes to the right analysis (gap, SWOT, competitor, ads, creative,
  communication, financial), and synthesizes recommendations with the Pyramid
  Principle. Use when a user has a fuzzy business problem and wants structure and
  a recommendation, not just an answer. Trigger on: "business consulting", "help
  me think through", "strategy problem", "structure this problem", "what should we
  do about", "consulting analysis". Archetype: Orchestrator. Routes the analysis
  sub-skills below.
allowed-tools: [WebSearch, WebFetch, Read, Write, Task]
argument-hint: "<business problem or decision>"
auto-trigger:
  - business consulting or a strategy problem
  - help me think through a fuzzy business decision
  - structure a problem and recommend an action
  - a question spanning multiple business analyses
do-not-trigger:
  - a single specific analysis the user named (use that skill directly)
  - financial modelling only (use creating-financial-models)
  - implementation/coding work
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Business Consulting

Structures a fuzzy business problem the way a strategy consultant would: frame it,
hypothesize, gather, analyze, synthesize, recommend. The umbrella that routes to
the focused analysis skills.

---

## The Engagement Flow

```
1. FRAME  → 2. HYPOTHESIZE → 3. GATHER → 4. ANALYZE → 5. SYNTHESIZE → 6. RECOMMEND
   (issue tree)  (what's true?)   (evidence)  (route)      (pyramid)      (so-what)
```

---

## 1. Frame — Issue Tree (MECE)

Break the problem into sub-questions that are **Mutually Exclusive, Collectively
Exhaustive**. Start from the core question and branch until each leaf is answerable.

```
Should we enter market X?
├── Is the market attractive?     (size, growth, margins)
├── Can we win?                   (right to play, differentiation)
└── Is it worth it?               (return vs. cost & risk)
```

No overlaps, no gaps. The tree *is* the workplan.

---

## 2. Hypothesize

State the likely answer up front as a testable hypothesis ("We should enter,
because X"). Consulting is hypothesis-driven — you test to confirm/refute, not
boil the ocean. Note what evidence would change your mind.

---

## 3. Gather

For each leaf of the tree, get the evidence. Cite sources; flag assumptions.
Use `deep-research`/`ultra-search` for external data, `profile-dataset` for the
client's own data.

---

## 4. Analyze — Route to the Right Tool

| Sub-question | Route to |
|---|---|
| Where are we vs. where we want to be? | `gap-analysis` |
| Internal strengths/weaknesses + external forces? | `swot-analysis` |
| How do we stack up against rivals? | `competitive-brief` |
| Is the paid-ad spend working? | `ads-analysis` |
| Which creative wins and why? | `creative-analysis` |
| Is our messaging landing? | `communication-analysis` |
| Numbers / ratios / forecast? | `analyzing-financial-statements` / `creating-financial-models` |

---

## 5. Synthesize — Pyramid Principle

Lead with the **answer**, then group supporting arguments, then the data under
each. The reader gets the recommendation in the first line and the logic beneath it.

```
RECOMMENDATION (the so-what)
├── Reason 1  → [evidence]
├── Reason 2  → [evidence]
└── Reason 3  → [evidence]
```

---

## 6. Recommend

```markdown
# [Problem] — Recommendation

## Bottom line
[the answer, in one sentence — what to do and why]

## Why (pyramid)
1. [reason] — [evidence]
2. [reason] — [evidence]
3. [reason] — [evidence]

## Risks & mitigations
[top 2–3]

## Next steps
[owner-able actions, sequenced]
```

---

## Rules

- **MECE or it's not framed** — no overlapping or missing branches.
- **Hypothesis-driven** — test a stated answer; don't boil the ocean.
- **Answer first** — Pyramid Principle: the so-what leads.
- **Route, don't reinvent** — hand each sub-question to its analysis skill.
- **Every claim sourced** — flag assumptions; recommendations are owner-able.
