---
name: gap-analysis
description: >
  Runs a structured gap analysis — current state vs. desired state, the gap, its
  root cause, and a prioritized plan to close it. Use when a user knows where they
  are and where they want to be and needs to map the distance and how to cross it
  (capabilities, process, performance, skills, market). Trigger on: "gap
  analysis", "current vs target state", "where are the gaps", "what's missing to
  reach", "close the gap". Archetype: Judgment Amplifier. Cross-references
  swot-analysis and business-consulting.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<current state + desired state / goal>"
auto-trigger:
  - gap analysis or current vs target state
  - where are the gaps / what's missing to reach a goal
  - mapping and closing the distance to a target
do-not-trigger:
  - a full consulting engagement (use business-consulting)
  - internal/external position scan (use swot-analysis)
  - competitor comparison (use competitive-brief)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Gap Analysis

Maps the distance between where a business is and where it wants to be — by
dimension — then explains the gap and how to close it. Honest about which gaps
matter and which are noise.

---

## Process

1. **Define desired state** — specific, measurable target ("85% on-time delivery", "$5M ARR", "feature parity with X"). A vague target makes a vague gap.
2. **Assess current state** — the same dimensions, measured, with evidence.
3. **Quantify the gap** — per dimension: current → target → size of gap.
4. **Root-cause each material gap** — why does it exist? (5 Whys / fishbone). Don't confuse symptom with cause.
5. **Prioritize** — by impact on the goal ÷ effort to close.
6. **Closure plan** — specific action, owner, sequence, and how you'll know it closed.

---

## Output Format

```markdown
# Gap Analysis — [domain] → [goal]

## Desired State
[the measurable target + by when]

## Gaps by Dimension
| Dimension | Current | Target | Gap | Root cause | Priority |
|---|---|---|---|---|---|
| [capability] | | | | | High |

## Closure Plan (prioritized)
| # | Gap | Action | Owner | Sequence | Done when |
|---|---|---|---|---|---|
| 1 | | | | | |

## What we're NOT closing (and why)
[gaps that don't move the goal — deliberately deprioritized]
```

Common dimensions: capability · process · performance/KPI · skills/people · technology · market position · compliance.

---

## Discipline

- **Measurable on both ends** — a gap between two vague states is unactionable.
- **Root cause, not symptom** — "low sales" isn't a cause; *why* is.
- **Prioritize ruthlessly** — list what you're deliberately not closing.
- **Evidence the current state** — don't assume where you are; measure it.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Wrap in a full consulting engagement | `business-consulting` |
| Position scan to inform the target | `swot-analysis` |
| Target is "beat competitor X" | `competitive-brief` |
| Client data needs profiling first | `profile-dataset` |

---

## Rules

- **Both states measurable** — no gap without numbers/criteria on each end.
- **Root-cause material gaps** — 5 Whys, not symptoms.
- **Impact ÷ effort** drives the order.
- **Name the non-goals** — what you're not closing and why.
- **Closure has a "done when"** — every action is verifiable.
