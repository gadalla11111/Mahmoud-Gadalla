---
name: design
description: >
  Unified design routing skill. Answers "how should this look?" at every layer —
  from Anthropic brand compliance to generative art to web UI to slide themes.
  Invoke this skill whenever a visual design question arises; it routes to the
  right sub-skill based on the output medium and creative latitude requested.
  Single entry point for the whole design cluster: canvas-design, frontend-design,
  theme-factory, brand-guidelines, presentation-architect, web-artifacts-builder,
  algorithmic-art, shadcn. Routes — does not duplicate their content.
auto-trigger:
  - visual design task without a specific named tool or medium
  - layout, typography, colour, or composition decisions
  - "design this"
  - "make this look good"
  - "visual hierarchy"
  - "which design skill"
do-not-trigger:
  - code-only tasks
  - purely textual content generation
  - when the medium is already obvious (invoke the specific sub-skill directly)
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Design — Unified Routing Skill

One entry point for all visual design decisions. Read the request, identify the medium and latitude, then follow the matching path below.

---

## Routing table

| Medium / output | Creative latitude | Path |
|---|---|---|
| Static art — poster, print, PDF/PNG | High (original artwork) | → **canvas-design** |
| Generative/algorithmic art — p5.js, flow fields, particles | High (computational) | → **algorithmic-art** |
| Web UI — page, component, app interface | High (distinctive POV) | → **frontend-design** |
| Complex standalone HTML artifact — state, routing, shadcn | Medium (functional) | → **web-artifacts-builder** |
| shadcn/ui components in a components.json project | Low–medium | → **shadcn** |
| Slides / deck — narrative + visual structure | Medium (research-backed) | → **presentation-architect** |
| Slides/docs/reports — apply a preset/custom theme | Low–medium | → **theme-factory** |
| Any artifact that must carry Anthropic branding | Any | → **brand-guidelines** (layer last) |
| Brand strategy / positioning (not visuals) | — | → **brand-framework** (strategy, not look) |

If the request spans multiple rows (e.g., "an Anthropic-branded web page"), run the medium path first, then layer brand-guidelines on top. For a deck: **presentation-architect** sets the spine, **theme-factory** or **brand-guidelines** styles it, **pptx** produces the file.

---

## Disambiguation — the easy-to-confuse pairs

| If the user says… | They mean | Route to |
|---|---|---|
| "canvas" + poster/print/.png | Static art | **canvas-design** |
| "canvas" + drawing tool / whiteboard / Fabric.js | Interactive web canvas | **frontend-design** / **web-artifacts-builder** |
| "art from code" / generative | p5.js computational art | **algorithmic-art** |
| "design a deck/slides" | Narrative + layout | **presentation-architect** |
| "theme my slides" | Apply palette/fonts | **theme-factory** |
| "make it on-brand" | Anthropic identity | **brand-guidelines** |
| "build our brand" | Positioning strategy | **brand-framework** (not a visual skill) |

When still ambiguous, ask one question: **"What's the final output — a static image, a web interface, a slide deck, or a styled document?"** Then route.

---

## canvas-design path

Use when the user asks for a poster, piece of art, design, or other static visual (PDF or PNG output).

**Two-step process**:

### Step 1 — Design Philosophy (.md file)
Create a VISUAL PHILOSOPHY — an aesthetic movement, not a layout template. Name it (1–2 words: "Brutalist Joy", "Chromatic Silence"). Write 4–6 paragraphs covering: space and form, color and material, scale and rhythm, composition and balance, visual hierarchy.

Critical guidelines:
- Each aspect once — no repetition.
- Emphasize craftsmanship repeatedly: "meticulously crafted", "painstaking attention", "master-level execution".
- Leave interpretive room for the canvas step.
- Output as a `.md` file.

### Step 2 — Canvas creation (.pdf or .png)
Identify the subtle conceptual thread from the original request (think jazz musician quoting another song — only those who know will catch it, everyone appreciates the music). Then express the philosophy visually:

- 90% visual design, 10% essential text.
- Repeating patterns, perfect shapes, dense accumulation of marks.
- Sparse clinical typography — search `./canvas-fonts` directory for fonts; use different fonts, make typography part of the art itself.
- All elements within canvas boundaries, nothing overlapping, breathing room throughout.
- After first pass: refine without adding new graphics — make what exists more cohesive, crisper, more of a piece. Remove rather than add.

Output: single `.pdf` or `.png` plus the philosophy `.md`.

---

## frontend-design path

Use when building new UI or reshaping an existing interface (web page, component, app).

**Process — two passes**:

### Pass 1 — Design plan
Before writing code, produce a compact token system:
- **Color**: 4–6 named hex values
- **Type**: display face (used with restraint) + body face + utility face if needed; state the pairing rationale
- **Layout**: one-sentence prose + ASCII wireframe for the concept
- **Signature**: the single unique element this page will be remembered by

Name the subject, its audience, and the page's single job if the brief doesn't.

### Self-critique before Pass 2
Check: does any part of the plan read like the generic default for any similar page? Three common defaults to avoid unless the brief explicitly calls for them:
1. Warm cream background (~#F4F1EA) + high-contrast serif + terracotta accent
2. Near-black background + single acid-green or vermilion accent
3. Broadsheet hairline-rule dense-column layout

If a plan element is a default, revise it and state what changed and why. Then build.

### Building guidelines
- Hero is a thesis — open with the most characteristic thing in the subject's world.
- Typography carries personality — pair deliberately, set a clear type scale.
- Structure encodes meaning — numbered markers only if content is actually sequential.
- Motion deliberately — one orchestrated moment lands harder than scattered effects.
- Spend boldness in one place (the signature element); keep everything else quiet.
- Responsive to mobile, visible keyboard focus, `prefers-reduced-motion` respected.
- Watch CSS selector specificity — `.section` + `.cta` padding/margin conflicts are common.

**Writing in design**: words are design material. Active voice. Name things by what users control. Errors explain what went wrong and how to fix it. Empty states are invitations to act.

---

## theme-factory path

Use when styling an existing artifact (slides, docs, reports, HTML pages) with a preset or custom palette.

### With existing themes
1. Show `theme-showcase.pdf` for the user to browse (do not modify it).
2. Ask which theme to apply.
3. Wait for explicit confirmation.
4. Read the theme file from `themes/` directory and apply colors + fonts consistently.

**Available themes** (defined in `themes/`):
Ocean Depths · Sunset Boulevard · Forest Canopy · Modern Minimalist · Golden Hour · Arctic Frost · Desert Rose · Tech Innovation · Botanical Garden · Midnight Galaxy

### Custom theme
When no preset fits: ask for a brief description, generate a named theme (hex palette + font pairing), show it for review, then apply.

---

## brand-guidelines layer

Apply after any medium path when the output must carry Anthropic's visual identity.

**Colors**:
- Dark: `#141413` — primary text / dark backgrounds
- Light: `#faf9f5` — light backgrounds / text on dark
- Mid Gray: `#b0aea5` — secondary elements
- Light Gray: `#e8e6dc` — subtle backgrounds
- Orange: `#d97757` — primary accent
- Blue: `#6a9bcc` — secondary accent
- Green: `#788c5d` — tertiary accent

**Typography**:
- Headings (24pt+): Poppins (Arial fallback)
- Body: Lora (Georgia fallback)
- Non-text shapes cycle through orange → blue → green accents

Apply via `python-pptx`'s `RGBColor` for slides, or inline CSS / Tailwind custom tokens for web. Preserve text hierarchy; smart color selection based on background lightness.

---

## Other cluster paths (hand off — don't reimplement)

| Path | Use when | Follow |
|---|---|---|
| **presentation-architect** | Deck needs a narrative spine + visual hierarchy | Title-test spine → data storytelling → then theme-factory/brand-guidelines → pptx |
| **algorithmic-art** | Computational/generative art via p5.js | Seeded randomness + parameter exploration |
| **web-artifacts-builder** | Elaborate single-file HTML artifact (state/routing/shadcn) | Not for simple JSX — that's frontend-design |
| **shadcn** | Project already uses components.json | Component-level work within an existing system |

These are full skills — route to them, don't duplicate their guidance here. This router only carries canvas-design / frontend-design / theme-factory / brand-guidelines inline because they share the medium-then-brand layering flow.
