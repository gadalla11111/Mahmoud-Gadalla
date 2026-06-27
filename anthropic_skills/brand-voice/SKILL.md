---
name: brand-voice
description: >
  Generates brand voice-and-tone guidelines — the verbal identity of a brand.
  Produces a "We Are / We Are Not" trait grid, the voice-vs-tone distinction,
  do/don't examples, and a confidence read on current voice alignment. Use when a
  user wants to define how a brand sounds in writing, audit copy against a voice,
  or onboard writers. Trigger on: "brand voice", "voice and tone", "how should we
  sound", "tone of voice guidelines", "verbal identity", "writing guidelines".
  Archetype: Judgment Amplifier. Verbal counterpart to brand-framework (strategy)
  and brand-guidelines (visual identity).
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<brand or sample copy> [--build | --audit]"
auto-trigger:
  - brand voice or voice-and-tone guidelines
  - how should we sound, verbal identity, or writing guidelines
  - auditing copy against a defined brand voice
do-not-trigger:
  - brand positioning/strategy (use brand-framework)
  - visual identity — colours/typography (use brand-guidelines)
  - persuasion/conversion copy audit (use persuasion-psychology)
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Brand Voice

Defines how a brand *sounds* — its verbal identity. Voice is constant; tone flexes
by context. This is the words layer, distinct from positioning (brand-framework)
and visuals (brand-guidelines).

---

## Voice vs Tone

- **Voice** — constant. The brand's enduring personality in words (e.g. *confident, approachable, precise*).
- **Tone** — flexes by context. The same voice adjusts: warmer in onboarding, sober in an incident notice, lighter on social.

A guideline defines voice once, then shows how tone shifts across 3–4 contexts.

---

## The "We Are / We Are Not" Grid

The core artifact. Each trait is paired with its **failure mode** — the adjacent
vice it must not tip into:

| We Are | We Are Not |
|---|---|
| Confident | Arrogant |
| Approachable | Sloppy |
| Precise | Jargon-heavy |

Pick 3–5 traits. The "We Are Not" column is what makes the guideline usable —
it draws the line writers actually need.

---

## Build Mode (`--build`)

1. **Derive traits from positioning** — pull voice from `brand-framework` personality if it exists; otherwise interview for it.
2. **Write the grid** — 3–5 We Are / We Are Not pairs.
3. **Open questions** — surface the deliberate choices ("humor level?", "first person plural or singular?", "contractions?").
4. **Do/Don't examples** — for each trait, one rewrite showing the same sentence on-voice vs off-voice.
5. **Tone map** — how the voice flexes across onboarding / error states / marketing / support.

```markdown
# [Brand] Voice & Tone

## Voice (constant)
[one sentence]

## We Are / We Are Not
| We Are | We Are Not |
|---|---|
[3–5 rows]

## Voice vs Tone
Voice: [constant traits] · Tone: flexes by context

## Tone by Context
| Context | Shift |
|---|---|
| Onboarding | warmer, encouraging |
| Errors | calm, specific, no blame |
| Marketing | confident, punchy |
| Support | patient, plain |

## Do / Don't
| Trait | Do | Don't |
|---|---|---|

## Open Questions
- [humor level? contractions? person? emoji?]
```

---

## Audit Mode (`--audit`)

Read sample copy against the grid. Give a **confidence read** — a rough %
alignment — and mark each passage on-voice or off-voice with the trait it breaks.

```markdown
## Voice Audit — [sample]
**Confidence: ~86% aligned**
| Passage | On/Off | Trait broken | Fix |
```

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Voice should follow from positioning | `brand-framework` |
| Visual identity (colour/type) | `brand-guidelines` |
| Persuasion/conversion copy | `persuasion-psychology` |
| Apply voice while removing AI tells | `humanizer` |

---

## Rules

- **Voice constant, tone flexes** — define voice once, map tone to contexts.
- **Every trait has a "We Are Not"** — the failure mode is what makes it usable.
- **Show, don't tell** — each trait gets a do/don't rewrite, not just an adjective.
- **Surface the open choices** — humor, person, contractions are deliberate, not default.
- **Audit gives a confidence read**, passage by passage.
