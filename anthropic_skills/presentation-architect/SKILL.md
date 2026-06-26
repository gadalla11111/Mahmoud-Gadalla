---
name: presentation-architect
description: >
  Designs, restructures, and visually polishes presentations using research-backed
  principles: title-only narrative test, data storytelling over raw tables, visual
  hierarchy, and accessibility by default. Use when a user wants to build a deck
  from scratch, restructure an existing one, or upgrade slides aesthetically with
  a strong information spine. Trigger on: "build a presentation", "design slides",
  "fix my deck", "restructure this presentation", "make these slides better",
  "pitch deck", "slide design", "data storytelling". Archetype: Workflow Automation.
  Cross-references pptx for production, brand-framework for on-brand decks, and
  deep-research when slides need researched substance.
allowed-tools: [WebSearch, WebFetch, Read, Write, Bash]
argument-hint: "<topic or existing deck> [--build | --restructure | --polish]"
auto-trigger:
  - "build a presentation"
  - "design slides"
  - "pitch deck"
  - "slide design"
  - restructuring or visually upgrading an existing deck
  - turning research/data into a narrative slide sequence
do-not-trigger:
  - producing the final PPTX binary only (use pptx after this skill)
  - a single chart with no deck context
  - written report with no slides (use a doc skill)
health:
  last_eval: 2026-06-26
  pass_rate: 0.9
  trigger_accuracy: 0.9

  open_issues:
    - polish-vs-theme boundary — 'theme my slides' can match --polish or theme-factory
---

# Presentation Architect

Builds decks where structure carries the story and design serves clarity. Information spine first, aesthetics second — both research-backed.

---

## Mode Selection

| Mode | Trigger | Focus |
|---|---|---|
| `--build` | "build a presentation" | Spine → slides → visuals, from scratch |
| `--restructure` | "fix/restructure my deck" | Re-sequence for narrative; cut/merge slides |
| `--polish` | "make these better" | Visual hierarchy + accessibility, content intact |

---

## The Four Principles (apply to every slide)

| Principle | Means |
|---|---|
| **Clarity over decoration** | If an element doesn't aid understanding, remove it |
| **Story over slide count** | A tight 12-slide arc beats 40 dense slides |
| **Consistency over improvisation** | One type/color/spacing system, applied everywhere |
| **Accessibility by default** | High contrast, readable type, inclusive language |

---

## Step 1 — Build the Spine (the title test)

Before designing anything, write **only the slide titles** as full sentences. Read them top to bottom.

> **The title test**: if someone reads only the titles, they must understand the entire story.

If the title-only read has gaps or jumps, fix the *structure* before touching visuals. Titles are assertions ("Q3 churn rose 4pts in enterprise"), not topics ("Churn").

---

## Step 2 — Data Storytelling (not data dumping)

Transform raw numbers into narrative-driven visuals:

| Don't | Do |
|---|---|
| Paste a 12-column table | Show the one number that matters, big |
| "Here's all the data" | "Here's the insight; here's the proof" |
| Three competing charts/slide | One chart, one takeaway, stated in the title |

For each data slide: **what's highlighted, what's minimized, how attention is guided.** Sophistication sits in the structure, not the decoration.

---

## Step 3 — Visual Hierarchy System

| Tool | Rule |
|---|---|
| **Scale** | Largest element = the point. Supporting text small and calm. |
| **Type** | 2–3 styles max; vary weight/size, not families |
| **Color** | Neutral base + 1–2 accents; use color shift to highlight the key data point |
| **Space** | Generous margins; one idea per slide; let it breathe |
| **Contrast** | High-contrast text/background; pass WCAG AA |

90% of processed information is visual — let hierarchy do the explaining.

---

## Step 4 — Research Layer (when substance matters)

For high-stakes/expert decks:
- Use WebSearch/WebFetch to source every claim; cite on-slide or in an appendix
- Flag assumed vs. evidenced figures
- For deep substantiation, hand off to `deep-research` before designing

Never fill a slide with confident numbers you can't source.

---

## Output Format

```markdown
# Deck Plan: [Title]

## Narrative Spine (title test)
1. [assertion title]
2. [assertion title]
... [read these alone — do they tell the story?]

## Slide-by-Slide
### Slide N — [Title assertion]
- **Takeaway**: one sentence
- **Visual**: [chart type / image / layout]
- **Highlight**: what the eye lands on first
- **Data/source**: [figure — source URL]
- **Speaker note**: [what you say, not what's on screen]

## Design System
- Type: [2–3 styles]
- Color: [base + accents, hex]
- Layout grid: [margins, columns]
- Accessibility: [contrast check, alt text plan]
```

---

## Restructure Mode Checklist (`--restructure`)

- Run the title test on the existing deck — mark where the story breaks
- Merge slides that share one takeaway; cut slides with none
- Re-order to: context → tension → insight → proof → ask
- Reduce every slide to one idea

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Produce the final editable .pptx | `pptx` |
| Deck must follow a brand system | `brand-framework` / `applying-brand-guidelines` |
| Slides need researched substance | `deep-research` |
| Financial/market figures need checking | `fact-checker` |
| Ministry (Arabic/MERIDIAN/Jahizoon) deck | `ministry-proposal` |

---

## Rules

- **Spine before slides** — pass the title test before any visual work.
- **Titles are assertions**, not topics.
- **One idea per slide**, one takeaway per data visual.
- **Story over slide count** — cut anything without a takeaway.
- **2–3 type styles, 1–2 accent colors** — consistency over improvisation.
- **Accessibility by default** — high contrast, readable, inclusive.
- **Source every number** — no unverifiable figures on a slide.
