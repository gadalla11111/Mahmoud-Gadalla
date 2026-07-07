# Skill: presentation-design

**Trigger:** presentation design, slide deck aesthetics, visual storytelling, pitch deck layout, data slide design, slide hierarchy, narrative spine for slides, cinematic presentation, web presentation, slide animation, deck polish, presentation aesthetics, slide template, executive deck.

---

## What this skill does

Presentation design system — narrative architecture, visual hierarchy, data storytelling, and aesthetic polish. Synthesizes rampstackco creative-direction, ConardLi garden-skills web-video-presentation, and VoltAgent pptx-generator patterns.

**Sources:**
- `rampstackco/claude-skills` — creative-direction skill (four-axis aesthetic briefs) | MIT
- `ConardLi/garden-skills` — web-video-presentation (script → 16:9 web slides → screen-recordable video) | MIT
- `VoltAgent/awesome-agent-skills` — pptx-generator (MiniMax-AI) | MIT

---

## Framework

### 1. Narrative Architecture (before slides)
- Story spine: problem → stakes → insight → solution → proof → call to action
- Audience calibration: executive summary vs. deep-dive vs. investor mode
- Slide count discipline: one idea per slide, 10/20/30 rule baseline

### 2. Four-Axis Aesthetic Brief (rampstackco creative-direction)
Define the deck's visual character across four axes before any design:
- **Formal ↔ Playful** — tone and geometry
- **Dense ↔ Airy** — information density and whitespace
- **Classic ↔ Contemporary** — typeface and color era
- **Corporate ↔ Editorial** — layout and imagery style

### 3. Visual Hierarchy
- Grid: 12-column base, safe zones, bleed areas
- Type scale: headline (40–60pt) → subhead (24–32pt) → body (16–18pt) → caption (12pt)
- Color: 1 dominant, 1 accent, 1 neutral; semantic use (alert = red, success = green)
- Contrast: WCAG AA minimum on all text; test on projector white

### 4. Data Slide Design
- Chart selection: comparison → bar; trend → line; composition → stacked/pie; distribution → histogram
- Annotation-first: highlight the insight, not the data
- Reduce non-data ink; label directly (no legends where possible)

### 5. Slide Types & Templates
- Title slide, section divider, "big number" stat slide, quote pull, two-column compare, timeline, team grid, appendix

### 6. Web/Cinematic Presentation (ConardLi)
- Script → click-driven 16:9 HTML slides
- Screen-recordable as MP4 video
- Embedded animations, transitions, code highlights

### 7. PPTX Generation (VoltAgent/MiniMax-AI)
- Generate and edit `.pptx` files programmatically
- Apply themes, master slides, custom layouts

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/presentation-architect
  - anthropic_skills/pptx
  - anthropic_skills/brand-identity-pillars
archetype: presentation-design
```
