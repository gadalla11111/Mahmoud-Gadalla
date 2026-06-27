---
name: brand-kit
description: >
  Generates a premium brand-kit overview board — logo, mockups, color, typography,
  and atmosphere — as one cinematic deck-style image. Picks a mode (dark developer,
  dark operator, calm system, security, editorial compliance, luxury beauty, voice
  AI, cultural experimental), then produces a structured board spec and the image
  prompt. Use when a user wants a visual brand-identity board, not written voice
  guidelines. Trigger on: "design a brand kit", "brand mood board", "create logo
  and palette", "build visual identity board", "brand overview board". Archetype:
  Workflow Automation. For verbal identity use brand-voice; for strategy use
  brand-framework; for a single data graphic use infographic-maker.
allowed-tools: [Read, Write, WebSearch, WebFetch]
argument-hint: "<brand name + vibe> [--mode dark-dev|calm-system|luxury|...]"
auto-trigger:
  - design a brand kit or brand mood board
  - create logo and palette / build a visual identity board
  - premium brand overview board as one image
do-not-trigger:
  - verbal voice & tone guidelines (use brand-voice)
  - brand positioning/strategy (use brand-framework)
  - a single data infographic (use infographic-maker)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Brand Kit

Produces a premium brand-kit overview **board** — the visual identity at a glance
(logo, construction, color, type, mockups, atmosphere) in one cinematic, deck-style
image. The visual counterpart to `brand-voice` (words) and `brand-framework`
(strategy).

---

## 1. Pick a Mode

Each mode is a coherent visual world — colors, textures, and energy:

| Mode | Feel |
|---|---|
| **Dark developer** | terminals, monospace, builder energy |
| **Dark operator** | card systems, glowing chips, tactical flow |
| **Calm system** | deep green, misty landscapes, quiet SaaS |
| **Security** | shields, radar, controlled gradients |
| **Editorial compliance** | ivory, seals, refined paper |
| **Luxury beauty** | serif monogram, embossing, soft shadow |
| **Voice AI** | indigo, waveforms, mic motifs |
| **Cultural experimental** | halftone, CRT, bold poster |

Match the mode to the brand's category and audience; confirm before generating.

---

## 2. Board Spec (9 panels)

A brand-kit board reads as a numbered grid:

```
01 Logo            02 Logo construction   03 Digital application
04 Tagline         05 Color system        06 Typography
07 Physical app.   08 Atmosphere          09 System details
```

For each panel, specify: content, and how it expresses the mode.

---

## 3. Spec + Prompt Output

```markdown
# Brand Kit Board — [Brand]

**Mode**: [chosen mode]
**Palette**: [4 swatches with hex + names — e.g. Charcoal #0D0D0F, Ivory #F5F1E8, Cyan #00E5FF, Coral #FF6B6B]
**Type**: [display face + mono/body face — e.g. Satoshi display, IBM Plex Mono]
**Logo direction**: [monogram / wordmark / mark + construction grid]

## Panels
01 Logo — [...]      02 Construction — [...]   03 Digital — [...]
04 Tagline — "[...]" 05 Color — [swatches]     06 Type — [specimen]
07 Physical — [...]  08 Atmosphere — [...]      09 Details — [...]

## Image Prompt
[full prompt for the image generator: deck-style 9-panel brand board, mode,
palette hex, type, logo, mockups, cinematic lighting, dimensions, footer
"[BRAND] · BRAND KIT · v1.0"]
```

---

## 4. Render

If an image tool/MCP is connected, render and deliver. Otherwise hand back the
spec + prompt so the user can generate anywhere.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Verbal voice & tone | `brand-voice` |
| Underlying positioning | `brand-framework` |
| Anthropic-specific brand application | `brand-guidelines` |
| A single data infographic | `infographic-maker` |
| Original fine-art piece | `canvas-design` |

---

## Rules

- **Mode first** — one coherent visual world drives every panel.
- **Hex + named palette** — never vague color words alone.
- **9-panel board** — logo through system details, deck-style.
- **Confirm the mode** before generating; it's the biggest lever.
- **Spec + prompt always** — deliverable works even with no image model connected.
