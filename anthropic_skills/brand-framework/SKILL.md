---
name: brand-framework
description: >
  Builds a complete brand marketing strategy using the Brand Pyramid + 4C
  direction filter. Use when a user needs to define or audit a brand: positioning,
  value proposition, brand essence, personality, messaging matrix. Produces a
  structured, layered brand strategy ready for campaign activation. Trigger on:
  "brand strategy", "brand framework", "positioning statement", "brand pyramid",
  "define our brand", "brand essence", "value proposition", "rebrand".
  Archetype: Judgment Amplifier. Cross-references prd-generator for product scope,
  applying-brand-guidelines for compliance, and presentation-architect for decks.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<brand or product name> [--audit existing | --build new]"
auto-trigger:
  - "brand strategy"
  - "brand framework"
  - "brand pyramid"
  - "positioning"
  - defining or auditing a brand's identity, essence, or messaging
  - building a value proposition or competitive differentiation story
do-not-trigger:
  - applying an existing brand's visual rules to a document (use applying-brand-guidelines)
  - single tagline or copy edit with no strategy work
  - the MERIDIAN/Jahizoon ministry brand (use ministry-proposal)
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Brand Framework

Builds brand strategy bottom-up through the Brand Pyramid, grounded by the 4C filter, and exits with an activation-ready messaging matrix.

---

## Step 0 — Direction Filter (4C)

Before building the pyramid, ground the strategy. Answer each:

| C | Question |
|---|---|
| **Company** | What are we uniquely able to do? Mission, assets, constraints. |
| **Category** | What are the rules and conventions of our market? Who else plays? |
| **Consumer** | Who is the priority audience and what job are they hiring us for? |
| **Culture** | What shift in the wider world can we tap or lead? |

These four keep the pyramid honest under fast content cycles. Revisit if any layer below feels ungrounded.

---

## The Brand Pyramid (build bottom → top)

Each layer must follow from the one below. Never skip.

```
            ▲  5. ESSENCE
           ───  one core idea — 3 words max
          ─────  4. PERSONALITY
         ───────  human traits — "if the brand were a person…"
        ─────────  3. VALUES
       ───────────  principles that guide decisions
      ─────────────  2. EMOTIONAL BENEFITS
     ───────────────  how the customer feels
    ─────────────────  1. FUNCTIONAL BENEFITS
   ───────────────────  what the product literally does
```

| Layer | Build prompt | Test |
|---|---|---|
| 1 Functional | "What does it do, concretely?" | Verifiable, not aspirational |
| 2 Emotional | "How does that make them feel?" | Maps to a real human need |
| 3 Values | "What do we always/never do?" | Would survive a hard trade-off |
| 4 Personality | "Describe the brand as a person." | Distinct from 2 competitors |
| 5 Essence | "The one idea, in ≤3 words." | Can't be claimed by a rival |

**Rule**: emotional benefit must trace to a functional one; essence must compress the whole stack, not add a new claim.

---

## Activation Layer (the output that ships)

After the pyramid, produce the working artifacts:

### Positioning Statement
```
For [priority audience] who [need/job],
[brand] is the [category] that [single biggest benefit]
because [reason to believe].
Unlike [main alternative], we [key differentiator].
```

### Value Proposition
One sentence the customer would actually say. No jargon.

### Messaging Matrix

Map every pyramid layer to where it shows up:

| Pyramid layer | Headline message | Proof point | Channel/touchpoint |
|---|---|---|---|
| Essence | | | brand film, homepage hero |
| Personality | | | tone of voice, social |
| Values | | | about page, recruiting |
| Emotional | | | campaign concepts |
| Functional | | | product pages, spec sheets |

---

## Research Discipline

- Use WebSearch to pull category conventions and 2–3 competitor positionings before writing differentiation
- Cite competitor claims with a source URL — don't assert a rival's position from memory
- Flag any consumer insight that is assumed vs. evidenced

---

## Output Format

```markdown
# Brand Strategy: [Name]

## 4C Grounding
[one line each: Company / Category / Consumer / Culture]

## Brand Pyramid
| Layer | Statement |
|---|---|
[5 rows, functional → essence]

## Positioning Statement
[filled template]

## Value Proposition
[one sentence]

## Messaging Matrix
[table]

## Open Questions / Assumptions to Validate
[anything not yet evidenced]
```

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Product scope/feature definition needed first | `prd-generator` |
| Brand exists — apply its visual rules to a doc | `applying-brand-guidelines` |
| Turn strategy into a pitch deck | `presentation-architect` |
| Verify market-size or competitor claims | `fact-checker` |
| Deep competitor landscape required | `deep-research` |

---

## Rules

- **Build bottom-up** — never write essence before functional benefits exist.
- **One essence, ≤3 words** — if it needs a sentence, it's not essence yet.
- **Differentiation must be ownable** — if a competitor could say it too, it's table stakes, not positioning.
- **Every emotional claim traces to a functional truth.**
- **Ground in 4C** — a pyramid with no cultural or category grounding is a wish list.
