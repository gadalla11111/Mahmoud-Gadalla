---
name: creative-analysis
description: >
  Analyzes ad and marketing creative performance to explain which creatives win,
  why, and what to test next. Reads hook rate, hold/retention, thumb-stop, CTR,
  and conversion per creative; detects fatigue; extracts the winning patterns
  (hook type, format, message, length); and recommends the next creative tests.
  Use when a user has creative-level performance data and wants to understand the
  creative, not the account. Trigger on: "creative analysis", "which ad creative
  works", "hook rate", "creative fatigue", "why is this ad winning", "what to test
  next". Archetype: Judgment Amplifier. Pairs with ads-analysis and social-content.
allowed-tools: [WebSearch, WebFetch, Read, Write, Bash]
argument-hint: "<creative-level performance data>"
auto-trigger:
  - creative analysis or which ad creative works
  - hook rate, hold rate, thumb-stop, or creative fatigue
  - why an ad is winning and what creative to test next
do-not-trigger:
  - account structure/spend diagnosis (use ads-analysis)
  - creating new content (use social-content)
  - organic channel audit (use social-audit)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Creative Analysis

Explains the creative, not the account: which ads win, the *pattern* behind the
winners, where fatigue is setting in, and what to test next. Creative is the #1
performance lever, so this is where most lift hides.

---

## The Creative Funnel (per asset)

| Metric | What it measures | Reads as |
|---|---|---|
| **Hook / thumb-stop rate** | 3s views ÷ impressions | Does the first 2s stop the scroll? |
| **Hold / retention** | 15s+ or completion ÷ 3s views | Does it keep them after the hook? |
| **CTR** | clicks ÷ impressions | Does it earn the click? |
| **CVR per creative** | conversions ÷ clicks | Does the promise match the landing? |

A great hook with poor hold = strong open, weak payoff. Trace the drop-off.

---

## Pattern Extraction (the real output)

Don't just rank ads — find *why* the winners win, so it's repeatable:

- **Hook type** — question, bold claim, pattern interrupt, demo, UGC, problem-first
- **Format** — UGC vs. polished, static vs. video, talking-head vs. screen-capture
- **Message** — which value prop / angle each winner leads with
- **Length & pacing** — where attention drops
- **Opening frame** — the literal first 1–2 seconds

Group winners and losers; the difference between the clusters is the insight.

---

## Fatigue Detection

A creative is fatiguing when, over time: frequency rises **and** CTR/hook rate
falls **and** CPA climbs — same asset, declining returns. Flag it, rotate it,
and brief a fresh variant on the winning pattern (not a random new idea).

---

## Output Format

```markdown
# Creative Analysis — [account/campaign] · [N creatives]

## Winners & Losers
| Creative | Hook | Hold | CTR | CVR | Verdict |

## Winning Pattern
- Hook type that wins: [...]
- Format that wins: [...]
- Message/angle that wins: [...]
- (with the evidence: winners share X, losers share Y)

## Fatigue Watch
| Creative | Freq↑ | CTR↓ | CPA↑ | Action (rotate/refresh) |

## Next Tests (one variable each)
1. [test the winning hook in a new format]
2. [test a new angle against the control]
```

---

## Discipline

- **Pattern over ranking** — "video #4 won" is useless; *why* it won is the asset.
- **One variable per test** — so the next read is clean.
- **Fatigue = trend, not snapshot** — freq↑ + CTR↓ + CPA↑ together.
- **Brief from the pattern** — new creatives extend what works, not random shots.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Account structure/spend, not creative | `ads-analysis` |
| Produce the next creative/scripts | `social-content` |
| Render an HTML/motion concept | `hyperframes` |
| Live creative metrics (Meta) | Motion / platform MCP |

---

## Rules

- **Extract the pattern** — repeatable why, not a leaderboard.
- **One variable per test.**
- **Fatigue is a trend** of freq↑/CTR↓/CPA↑ on one asset.
- **Next creatives extend the winner** — brief from evidence.
- **Trace hook → hold → click → convert** to find the drop-off.
