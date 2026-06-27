---
name: competitive-brief
description: >
  Researches one or more competitors and ships a positioning brief — messaging
  gaps, threats, and clear opportunities. Captures the competitor list and your
  context, scans homepage/pricing/blog/jobs/press, pulls third-party signals
  (G2, analysts, reviews), maps positioning/content cadence/audience overlap, and
  returns a structured brief with strengths, gaps, and angles. Trigger on: "build
  a competitive brief", "compare to competitors", "find positioning gaps", "map
  messaging vs rivals", "scout rival pricing". Archetype: Judgment Amplifier.
  Cross-references deep-research for depth and brand-framework for your positioning.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<your brand + competitors> [--quick | --deep]"
auto-trigger:
  - build a competitive brief or compare to competitors
  - find positioning gaps or map messaging vs rivals
  - scout rival pricing, content cadence, or audience overlap
do-not-trigger:
  - your own brand positioning with no competitor (use brand-framework)
  - a full multi-source research report (use deep-research)
  - social-channel benchmark only (use social-audit)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Competitive Brief

Researches competitors and ships a positioning brief leadership can act on:
where rivals are strong, where they're exposed, and the angle you should own.

---

## Process

1. **Capture** — your brand + context, the competitor list (2–4), and focus areas (positioning / pricing / content / product).
2. **Scan each competitor** — homepage, pricing page, blog, jobs board (signals hiring intent), recent press (last 90 days).
3. **Third-party signals** — G2/Capterra reviews, analyst mentions, review-site sentiment. Cite each source.
4. **Map** — positioning, content cadence, primary audience, pricing posture, recent moves, share of voice.
5. **Synthesize** — the single biggest opportunity and the single biggest threat.

---

## Output Format

```markdown
# Competitive Brief — [category] · [N competitors]

| Brief dimension | You ([brand]) | [Competitor A] (leader) | [Competitor B] (upstart) |
|---|---|---|---|
| Core message | | | |
| Primary audience | | | |
| Pricing posture | | | |
| Content cadence | | | |
| Recent move (90d) | | | |
| Share of voice | | | |

> **BIGGEST OPPORTUNITY** — [the gap no competitor owns + how to claim it, with urgency]
> **BIGGEST THREAT** — [the move that closes your differentiation + the timeline]

## Angles to test
- [2–3 specific positioning/messaging plays grounded in the gaps above]
```

---

## Research Discipline

- Cite every competitor claim with a source URL + access date; never assert a rival's pricing/position from memory.
- Separate **observed** (on their site) from **inferred** (read between the lines) — label inferences.
- Flag where data is thin rather than over-reading a single signal.
- For deep multi-source diligence, escalate to `deep-research`.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Deeper multi-source investigation | `deep-research` |
| Your own positioning needs defining | `brand-framework` |
| Find uncontested space, not just compare | `blue-ocean-strategy` |
| Verify a competitor stat/claim | `fact-checker` |
| Turn the brief into a deck | `presentation-architect` |

---

## Rules

- **Cite every rival claim** — no competitor facts from memory.
- **Label observed vs inferred** — don't pass speculation as fact.
- **One biggest opportunity, one biggest threat** — force the prioritization.
- **Angles must be ownable** — tie each to a real gap, with urgency.
- **Flag thin data** — don't over-read a single signal.
