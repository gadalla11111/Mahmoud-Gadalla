---
name: free-marketing-tool
description: >
  Plans a free lead-generating marketing tool — calculators, graders, ROI
  estimators, quizzes, generators — that attracts the right audience and captures
  leads. Defines the audience and the "aha" the tool delivers, picks a tool type,
  specs inputs/outputs/logic, plans the lead-capture and follow-up, and projects
  reach. Use when a user wants a free interactive tool as a growth/lead-gen
  channel. Trigger on: "free tool idea", "lead-gen tool", "build a calculator",
  "ROI calculator", "interactive lead magnet", "grader tool". Archetype: Workflow
  Automation. Hand the build to frontend-design / web-artifacts-builder.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<product + audience>"
auto-trigger:
  - free tool idea or lead-gen tool
  - build a calculator / ROI estimator / grader as a lead magnet
  - interactive free tool as a growth channel
do-not-trigger:
  - paid acquisition (use media-buyer)
  - the actual UI build with no strategy (use frontend-design)
  - a static content piece (use doc-coauthoring)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Free Marketing Tool

Plans a free interactive tool as a lead-generation channel — the kind people use,
share, and trade their email for. Strategy and spec here; the build goes to
`frontend-design` / `web-artifacts-builder`.

---

## Why Free Tools Work

A useful free tool earns attention, links, and leads on its own — it delivers a
real "aha" in seconds, and the user happily gives an email for the full result.
The bar: it must be **genuinely useful even before** the email gate.

---

## Process

1. **Audience + aha** — who is this for, and what one valuable answer does it give them instantly? ("Your projected ROI is 3.4×.")
2. **Pick the tool type** — match the aha to a format:

| Type | Delivers | Example |
|---|---|---|
| **Calculator / ROI** | A number that matters | "$172k projected annual gain" |
| **Grader / scorecard** | A score + what to fix | "Your page scores 78/100" |
| **Estimator** | A range / forecast | pricing, savings, time |
| **Quiz / diagnostic** | A category + next step | "You're a Type B operator" |
| **Generator** | A usable artifact | headline, plan, template |

3. **Spec inputs → logic → output** — the few inputs needed, the transparent logic, the headline result + supporting detail.
4. **Lead capture** — show enough value *before* the gate to earn the email; gate the full report / saved result / extras.
5. **Follow-up** — what the email sequence does with the lead (tie to the product).
6. **Reach** — how it gets distributed (SEO, social, embeds, partners).

---

## Spec Output

```markdown
# Free Tool — [name]

## Audience & Aha
[who] · instant value: "[the headline result]"

## Type
[calculator / grader / estimator / quiz / generator]

## Inputs → Logic → Output
- Inputs: [3–5 fields]
- Logic: [the transparent formula/rules]
- Output: [hero result] + [supporting breakdown]

## Lead Capture
- Free before gate: [the visible aha]
- Gated: [full report / save / benchmark] → email
- Follow-up: [sequence → product]

## Distribution
[SEO target query · social · embeddable · partner]

## Build handoff
→ frontend-design / web-artifacts-builder with this spec
```

---

## Discipline

- **Value before the gate** — if the tool is useless until you give an email, it fails.
- **Transparent logic** — show how the number is computed; trust drives shares.
- **Real numbers** — if the calculator uses benchmarks, source them (`fact-checker`); don't invent multipliers.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Build the actual tool UI | `frontend-design` / `web-artifacts-builder` |
| Persuasion on the landing/gate | `persuasion-psychology` |
| Verify benchmark numbers | `fact-checker` |
| Drive paid traffic to it | `media-buyer` |
| SEO the tool's landing page | `claude-seo` / `content-refresh` |

---

## Rules

- **Aha in seconds** — one valuable answer, instantly.
- **Value before the email gate** — earn the lead.
- **Transparent logic, real benchmarks** — trust is the growth engine.
- **One clear hero result** — not a wall of numbers.
- **Plan the follow-up** — a lead with no sequence is a wasted email.
