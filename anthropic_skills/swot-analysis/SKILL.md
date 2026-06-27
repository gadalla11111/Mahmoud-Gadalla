---
name: swot-analysis
description: >
  Runs a SWOT analysis and converts it into strategy with a TOWS matrix.
  Separates internal (Strengths, Weaknesses) from external (Opportunities,
  Threats), forces evidence behind each item, then pairs quadrants into concrete
  strategies (SO/ST/WO/WT) so the output is actions, not a static four-box.
  Use when a user wants a structured position read that leads to moves. Trigger
  on: "SWOT", "strengths and weaknesses", "opportunities and threats", "SWOT
  analysis", "position analysis". Archetype: Judgment Amplifier.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<company/product/initiative>"
auto-trigger:
  - SWOT or SWOT analysis
  - strengths and weaknesses, opportunities and threats
  - structured position read that should lead to strategy
do-not-trigger:
  - current-vs-target state mapping (use gap-analysis)
  - head-to-head competitor brief (use competitive-brief)
  - a full engagement (use business-consulting)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# SWOT Analysis

A SWOT that doesn't stop at four boxes. Internal vs. external, evidence behind
every item, then a **TOWS** step that turns the quadrants into real strategies.

---

## 1. SWOT — Internal vs. External

| | Helpful | Harmful |
|---|---|---|
| **Internal** (you control) | **Strengths** | **Weaknesses** |
| **External** (you don't) | **Opportunities** | **Threats** |

Rules that keep it honest:
- **Internal ≠ external.** "Rising demand" is an Opportunity, not a Strength. A common error is filing market trends as strengths.
- **Evidence each item.** "Strong brand" → with what proof (NPS, share, recall)? A SWOT of opinions is a vibe, not analysis.
- **Specific, not generic.** "Good team" is filler; "the only vendor with SOC2 + sub-50ms latency" is a strength.
- **3–6 per quadrant.** A list of 15 isn't prioritized.

---

## 2. TOWS — Turn It Into Strategy

The step most SWOTs skip. Pair quadrants to generate moves:

| | Opportunities | Threats |
|---|---|---|
| **Strengths** | **SO** — use strengths to seize opportunities (attack) | **ST** — use strengths to defend against threats |
| **Weaknesses** | **WO** — fix weaknesses to capture opportunities | **WT** — minimize weaknesses + avoid threats (survive) |

Each cell yields 1–2 concrete strategies. SO plays are usually where to lean.

---

## Output Format

```markdown
# SWOT + TOWS — [subject]

## SWOT (evidenced)
**Strengths**     | **Weaknesses**
- [item] — proof  | - [item] — proof
**Opportunities** | **Threats**
- [item] — source | - [item] — source

## TOWS Strategies
- **SO (attack)**: [strength × opportunity → move]
- **ST (defend)**: [strength × threat → move]
- **WO (improve)**: [fix weakness → capture opportunity]
- **WT (survive)**: [reduce weakness + dodge threat]

## Priority moves
[the 2–3 strategies to act on first, with why]
```

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Then map current → target | `gap-analysis` |
| Rival-specific position | `competitive-brief` |
| Find uncontested space | `blue-ocean-strategy` |
| Inside a full engagement | `business-consulting` |
| Verify a market claim | `fact-checker` |

---

## Rules

- **Internal vs. external, correctly sorted** — trends are O/T, never S/W.
- **Evidence every item** — no opinion-only SWOTs.
- **Specific beats generic** — "good team" is filler.
- **Always do TOWS** — a SWOT without strategies is half-finished.
- **Prioritize** — 3–6 per quadrant; name the first moves.
