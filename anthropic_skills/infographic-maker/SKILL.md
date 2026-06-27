---
name: infographic-maker
description: >
  Turns a small set of stats, steps, or comparisons into a single shareable
  infographic image. Picks a layout (stat stack, timeline, process, comparison,
  poster), confirms style and dimensions, writes a structured layout spec and
  palette, drafts the image prompt for the chosen generator, and renders the final
  image when an image model is available. Use when a user wants data turned into
  one graphic. Trigger on: "make an infographic", "turn data into one image",
  "visualize this comparison", "chart this process flow", "build a single-page
  graphic". Archetype: Workflow Automation. For motion use hyperframes; for a deck
  use presentation-architect.
allowed-tools: [Read, Write, WebSearch, WebFetch]
argument-hint: "<stats/steps/comparison> [--layout stat-stack|timeline|process|comparison|poster]"
auto-trigger:
  - make an infographic or single-page graphic
  - turn data into one image or visualize this comparison
  - chart this process flow as one shareable graphic
do-not-trigger:
  - animated/video output (use hyperframes)
  - multi-slide deck (use presentation-architect)
  - original fine-art poster with no data (use canvas-design)
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Infographic Maker

Turns a small set of numbers, steps, or comparisons into **one** shareable image.
Structure first, then style, then prompt, then render.

---

## Process

### 1. Pick the layout
| Layout | Best for |
|---|---|
| **Stat stack** | 3–6 headline numbers ("by the numbers") |
| **Timeline** | Progress / milestones over time |
| **Process** | A sequence of steps or a flow |
| **Comparison** | A vs B, before/after, us vs them |
| **Poster** | One big claim + supporting stats |

### 2. Confirm style + dimensions (one short menu)
Ask once: palette/mood (bold, minimal, corporate, playful), and output size
(square 1:1 for social, 9:16 story, 16:9 slide, portrait poster). Don't over-ask.

### 3. Write the layout spec + palette
Produce a structured spec the generator can follow — hierarchy, the hero number,
grouping, and a named palette with hex values. The biggest element is the single
most important number.

### 4. Draft the image prompt
Write the prompt for the chosen image generator, embedding the spec: layout,
exact figures (verbatim — never let the model invent numbers), palette, font mood,
dimensions, and a source line.

### 5. Render (when a model is available)
If an image MCP/tool is connected, render and deliver the file. If not, hand back
the finished prompt + spec so the user can render anywhere.

---

## Layout Spec Format

```markdown
# Infographic Spec — [title]

**Layout**: [stat-stack / timeline / process / comparison / poster]
**Dimensions**: [1:1 1080×1080 / 9:16 / 16:9 / poster]
**Palette**: [name] — primary #…, accent #…, text #…, bg #…
**Font mood**: [bold sans / editorial serif / mono accents]

## Content (verbatim — do not alter numbers)
- Hero: [the single biggest figure + label]
- Supporting: [2–5 stats/steps with labels]
- Source line: [attribution]

## Hierarchy
1. Hero number — largest
2. Supporting stats — grid
3. Source — small, bottom
```

---

## Data Integrity

- **Numbers are verbatim** — the figures in the image must exactly match the input; never let an image model round, invent, or "improve" them.
- Include a **source line** on every infographic.
- If a stat is unverified, flag it before rendering (offer `fact-checker`).

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| It should move (animation/video) | `hyperframes` |
| It's actually a multi-slide story | `presentation-architect` → `pptx` |
| Original artwork, not data | `canvas-design` |
| The numbers need verifying | `fact-checker` |
| It must follow a brand system | `brand-guidelines` / `brand-voice` |

---

## Rules

- **One image, one message** — if it needs multiple slides, it's not an infographic.
- **Structure before style** — layout + hierarchy before palette.
- **Hero number is biggest** — the eye lands on the most important figure first.
- **Numbers verbatim** — never let the generator alter a figure.
- **Always a source line.**
