---
name: persuasion-psychology
description: >
  Audits and applies Cialdini's seven persuasion principles to product copy,
  landing pages, onboarding, and pricing flows. Scores each persuasive element
  0–10 on adherence, applies reciprocity/commitment/social-proof/authority
  triggers, stress-tests liking/scarcity/unity for ethics, combines principles
  into layered messaging, and flags fake scarcity, fabricated proof, and other
  dark patterns. Trigger on: "add social proof", "write persuasive copy", "boost
  landing trust", "craft scarcity message", "rate persuasion", "persuasion audit".
  Archetype: Judgment Amplifier. Cross-references brand-framework for positioning.
allowed-tools: [WebSearch, WebFetch, Read, Write, Edit]
argument-hint: "<copy/page to audit or brief to write> [--audit | --apply]"
auto-trigger:
  - persuasion audit or rate copy on persuasion
  - add social proof or write persuasive copy
  - applying Cialdini principles to landing/pricing/onboarding copy
  - flagging dark patterns (fake scarcity, fabricated proof)
do-not-trigger:
  - brand positioning strategy (use brand-framework)
  - generic copyediting with no persuasion goal
  - paid-ad campaign setup (use media-buyer)
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Persuasion Psychology

Audits and applies Cialdini's seven principles of influence to product copy —
ethically. Persuasion that relies on deception destroys trust the moment it's
noticed, so dark patterns are flagged, not deployed.

---

## The Seven Principles

| Principle | What it does | Honest application |
|---|---|---|
| **Reciprocity** | Give value before the ask | Free trial / useful content up front, then the offer |
| **Commitment & Consistency** | Small yes → larger yes | Micro-question opens the flow (foot-in-the-door) |
| **Social Proof** | Others did it → it's safe | Real, specific counts ("4,217 teams"), named logos, reviews |
| **Authority** | Credible source → trust | Real credentials ("built by ex-Stripe engineers"), certifications, badges |
| **Liking** | We say yes to those we like | Shared values, relatable voice, genuine warmth |
| **Scarcity** | Limited → valuable | *Real* limits only (true seat caps, real deadlines) |
| **Unity** | Shared identity → influence | "For founders, by founders" when actually true |

---

## Audit Mode (`--audit`)

Score each persuasive element **0–10** on adherence, then triage:

```markdown
# Persuasion Audit — [Page] · 7 principles

[N critical] · [N watch] · [N ok]

CRITICAL  [Element] — [why it fails / is a dark pattern]
          [consequence] · [score]/10
WATCH     [Element] — [weak but salvageable]
          [fix direction] · [score]/10
OK        [Element] — [working]
          [why it's credible] · [score]/10

REACH 10/10 → FIX FIRST
[the single highest-leverage change]

Framework: Cialdini's principles of influence · Assessment
```

Triage bands: **Critical** (dark pattern / trust-destroying), **Watch** (vague or
buried), **OK** (credible, working). Lead with the fix that moves a low score to 10.

---

## Dark-Pattern Flags (never deploy, always flag)

- **Fake scarcity** — "Only 3 left" that resets every visit
- **Fabricated proof** — invented testimonials, fake counts, borrowed logos
- **Confirmshaming** — guilt-tripping the decline option
- **Forced continuity** — hidden auto-renewal
- **Vague proof** — "thousands of teams" when a real number exists and is stronger

Rule: if a tactic only works while the user doesn't notice it, it's a dark pattern.
Replace it with the honest, usually-stronger version (a real "4,217" beats a vague "thousands").

---

## Apply Mode (`--apply`)

When writing or revising:
1. Pick the 2–3 principles that fit the funnel stage (reciprocity + social proof for top; scarcity + authority near the ask)
2. Layer them — one element can carry two principles (a named case study = social proof + authority)
3. Ground every claim in something true; flag anything that would need a fact you don't have
4. Place value before the ask (reciprocity) and reserve scarcity for real limits

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Underlying positioning is unclear | `brand-framework` |
| Voice/tone of the copy | `brand-voice` |
| Stats/claims need verification | `fact-checker` |
| Paid-ad creative specifically | `media-buyer` |
| Strip AI tells from the final copy | `humanizer` |

---

## Rules

- **Ethics first** — flag dark patterns; never deploy deception.
- **Real beats vague** — a specific true number outperforms a fuzzy claim.
- **Value before the ask** — reciprocity opens, scarcity closes (only if real).
- **Score 0–10, fix the lowest-leverage-to-10 first.**
- **Every claim grounded** — unverifiable proof gets flagged, not written.
