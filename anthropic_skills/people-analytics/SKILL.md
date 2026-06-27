---
name: people-analytics
description: >
  Generates a people-analytics report from HR data — summary, metrics, analysis,
  and recommendations. Modes: Headcount (snapshot by team/location/level/tenure),
  Attrition (voluntary vs involuntary, trends), Diversity (representation, pipeline,
  promotion, pay equity), Org health (span of control, layers, team sizes, flight
  risk). Use when a user has HR/HRIS data and wants a workforce report. Trigger on:
  "people analytics", "HR analytics", "headcount report", "attrition analysis",
  "workforce data", "team metrics", "eNPS". Archetype: Workflow Automation.
allowed-tools: [Bash, Read, Write, Glob]
argument-hint: "<HR dataset> [--headcount | --attrition | --diversity | --org-health]"
auto-trigger:
  - people analytics or HR analytics report
  - headcount, attrition, diversity, or org-health analysis
  - workforce data or team metrics review
do-not-trigger:
  - generic dataset profiling (use profile-dataset)
  - financial modelling (use creating-financial-models)
  - individual performance review of one employee
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# People Analytics

Turns HR/HRIS data into a workforce report: snapshot, the metrics that matter,
honest analysis, and recommendations leadership can act on.

---

## Mode Selection

| Mode | Focus | Core metrics |
|---|---|---|
| `--headcount` | Snapshot | Headcount by team/location/level/tenure; QoQ change |
| `--attrition` | Turnover | Voluntary vs involuntary; regretted vs not; trend |
| `--diversity` | Representation | Representation by level, hiring pipeline, promotion rate, pay equity |
| `--org-health` | Structure | Span of control, layers, team sizes, flight risk |

---

## Core Metrics & Benchmarks

| Metric | What it tells you | Watch when |
|---|---|---|
| **Headcount + QoQ** | Growth/contraction by unit | Sudden shifts unexplained by plan |
| **Attrition rate** | Turnover health | Rising trend; concentrated in one team/level |
| **Regretted attrition** | Losing the people you wanted to keep | High % of exits are high performers |
| **eNPS** | Engagement signal | Falling, or below ~+20 |
| **Span of control** | Manager load | <3 (over-layered) or >10 (stretched) |
| **Pay equity gap** | Fairness risk | Any unexplained gap by gender/ethnicity at same level |

Always show a metric **with its direction and context** (▲ 18 QoQ, ▲ 1.6%), not a bare number.

---

## Output Format

```markdown
# Workforce Snapshot — [Period]
[N employees · M departments · trailing N months] · [N to watch]

| HEADCOUNT | ATTRITION | eNPS |
| 248 ▲18 QoQ | 11.4% ▲1.6% | +42 ▲5 pts |

## Headcount by [dimension]
[ranked bars: unit → count]

## Analysis
- [what the numbers mean — trends, concentrations, surprises]
- [the 1–3 things "to watch"]

## Recommendations
1. [specific, owner-able action tied to a finding]

generated [date] · source: [HRIS export]
```

---

## Sensitivity Rules (mandatory)

People data is sensitive. Always:
- **Aggregate** — never expose individuals in a report; suppress cells below ~5 headcount
- **Pay equity** — present gaps as "unexplained gap after controlling for level/role", never raw averages alone
- **Flight risk / attrition** — describe at the group level; don't label named individuals
- **Diversity** — representation and process metrics, not protected-attribute targets that could imply quotas
- Flag where data is too thin to conclude rather than over-reading a small sample

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Raw HR file needs profiling first | `profile-dataset` |
| Turn the report into a deck | `presentation-architect` → `pptx` |
| Key numbers into one shareable image | `infographic-maker` |
| Compensation/financial modelling | `creating-financial-models` |

---

## Rules

- **Aggregate, never expose individuals** — suppress small cells.
- **Direction + context, not bare numbers** — every metric carries its trend.
- **Pay equity = controlled gap**, never raw averages alone.
- **Flag thin data** — don't over-read a small sample.
- **Recommendations are owner-able** — each ties to a finding and a next step.
