---
name: ads-analysis
description: >
  Diagnoses an existing paid-ad account and explains where the spend is working,
  where it leaks, and what to change. Audits account structure, funnel metrics
  (CPM/CTR/CVR/CPA/ROAS), audience and placement performance, learning-phase and
  budget issues, then prioritizes fixes by recoverable spend. Use when a user has
  live ad data and wants a performance diagnosis (not a plan). Trigger on: "ads
  analysis", "why are my ads underperforming", "audit my ad account", "where is
  my ad spend leaking", "analyze ad performance", "ROAS dropping". Archetype:
  Judgment Amplifier. Diagnostic counterpart to media-buyer (which plans/launches).
allowed-tools: [WebSearch, WebFetch, Read, Write, Bash]
argument-hint: "<ad account export or metrics> [--platform meta|google|tiktok]"
auto-trigger:
  - ads analysis or audit my ad account
  - why are my ads underperforming or where is spend leaking
  - analyze ad performance when ROAS or CPA is dropping
do-not-trigger:
  - planning/launching a new campaign (use media-buyer)
  - analyzing the creative specifically (use creative-analysis)
  - organic social performance (use social-audit)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Ads Analysis

Diagnoses a live paid-ad account: where money works, where it leaks, what to fix
first. The diagnostic counterpart to `media-buyer` (which plans and launches).

---

## The Funnel Diagnosis

Read performance as a funnel — a problem at any stage masquerades as a problem below it:

| Stage | Metric | If weak here… |
|---|---|---|
| **Delivery** | CPM, frequency | Auction/audience too tight, or fatigue (rising freq) |
| **Hook** | CTR, thumb-stop | Creative or targeting mismatch → see `creative-analysis` |
| **Landing** | LP views ÷ clicks, bounce | Page speed/relevance, broken tracking |
| **Convert** | CVR | Offer, page, or audience-intent mismatch |
| **Efficiency** | CPA, ROAS | The sum — but always trace *which* stage caused it |

**Rule**: never "fix CPA" directly — find the stage that broke and fix *that*.

---

## Audit Checklist

**Account structure**
- Too many ad sets splitting conversions (below ~50/week → stuck in learning)?
- Retargeting mixed with prospecting in one ad set?
- Overlapping audiences cannibalizing the auction?

**Spend leaks**
- Spend on placements/audiences/keywords with no conversions
- Budget concentrated on a fatigued creative (rising freq, falling CTR)
- Search: missing negatives → spend on junk queries

**Tracking integrity**
- Pixel/CAPI firing? Conversions matching the platform vs. analytics?
- A measurement gap can fake a performance problem — verify first.

---

## Output Format

```markdown
# Ads Analysis — [account] · [period] · [spend]

## Headline
[the one-sentence diagnosis: which stage is broken and the recoverable spend]

## Funnel Read
| Stage | Metric | Value | Benchmark | Verdict |

## Spend Leaks (ranked by $ recoverable)
| # | Leak | Where | $ wasted / period | Fix |

## Structure & Tracking Issues
- [learning phase / overlap / tracking findings]

## Prioritized Fixes
1. [highest recoverable-spend fix first]
```

---

## Discipline

- **Trace, don't treat** — diagnose the broken funnel stage, not the symptom metric.
- **Verify tracking before concluding** — bad data fakes bad performance.
- **Quantify the leak** — rank fixes by recoverable spend, not gut feel.
- Pull live numbers from the export/connector; never invent benchmarks — source them.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Plan/launch the next campaign | `media-buyer` |
| The creative itself is the issue | `creative-analysis` |
| Raw export needs profiling | `profile-dataset` |
| Verify a benchmark | `fact-checker` |
| Live ad data via connector | Supermetrics / platform MCP |

---

## Rules

- **Funnel-first** — find the stage that broke; don't fix the summary metric.
- **Verify tracking** before any conclusion.
- **Rank by recoverable spend** — biggest leak first.
- **Source benchmarks** — no invented comparison numbers.
- **Diagnose, then hand planning to `media-buyer`.**
