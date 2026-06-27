---
name: communication-analysis
description: >
  Audits a piece or body of communication — exec message, campaign, internal memo,
  email, landing copy — for clarity, audience fit, channel fit, tone, and the gap
  between the intended message and the message actually received. Scores each on
  adherence and returns prioritized fixes. Use when a user wants to know whether
  their communication is landing and why. Trigger on: "communication analysis",
  "is this message clear", "audit our messaging", "does this land", "comms
  review", "intended vs received message". Archetype: Judgment Amplifier.
  Cross-references brand-voice for tone and persuasion-psychology for influence.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<message/copy + intended audience & goal>"
auto-trigger:
  - communication analysis or comms review
  - is this message clear / does this land
  - audit messaging for clarity, audience fit, or tone
  - intended vs received message gap
do-not-trigger:
  - writing brand voice guidelines (use brand-voice)
  - persuasion/conversion scoring (use persuasion-psychology)
  - removing AI tells from a draft (use humanizer)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Communication Analysis

Audits whether a message lands. The core question: is the message *received* the
same as the message *intended*? Most communication failures live in that gap.

---

## Step 0 — Establish Intent

Before judging, pin down: **who** is the audience, **what** should they think/feel/
do after, and **through what channel**. You can't audit "does it land" without a
target to land on.

---

## The Five Lenses

| Lens | Question | Failure mode |
|---|---|---|
| **Clarity** | Is the core message obvious in one read? | Buried lede, jargon, too many points |
| **Audience fit** | Does it speak to *this* reader's context and knowledge? | Insider language to outsiders, or vice versa |
| **Channel fit** | Right format for the medium? | A wall of text in Slack; a memo that should've been a meeting |
| **Tone** | On-voice and right for the moment? | Jokey in a crisis; stiff in a welcome |
| **Action** | Is the one next step unmistakable? | No CTA, or five competing ones |

Score each **on / watch / off**. The lowest one is usually the whole problem.

---

## Intended vs. Received

The diagnostic centerpiece. State both, side by side:

```
INTENDED: [what the sender wants understood]
RECEIVED: [what a reader in the target audience would actually take away]
GAP:      [the delta — and what causes it]
```

If a reasonable reader would miss the point, misread the tone, or not know what to
do — that's the finding, not "the writing is fine."

---

## Output Format

```markdown
# Communication Analysis — [piece]

## Intent
Audience: [...] · Goal (think/feel/do): [...] · Channel: [...]

## Lens Scores
| Lens | Score | Issue |
|---|---|---|
| Clarity | on/watch/off | |
| Audience fit | | |
| Channel fit | | |
| Tone | | |
| Action | | |

## Intended vs. Received
INTENDED: ...
RECEIVED: ...
GAP: ...

## Prioritized Fixes
1. [the fix that closes the biggest gap first]
```

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Define/repair the voice & tone | `brand-voice` |
| It's persuasion/conversion copy | `persuasion-psychology` |
| Internal-comms drafting | `internal-comms` |
| Strip AI tells from the rewrite | `humanizer` |

---

## Rules

- **Establish intent first** — no audience+goal, no audit.
- **Intended vs. received is the core** — name the gap, not just "it's fine".
- **Five lenses, scored** — clarity, audience, channel, tone, action.
- **Lowest lens leads** — fix the biggest gap first.
- **One unmistakable next step** — competing CTAs are a failure.
