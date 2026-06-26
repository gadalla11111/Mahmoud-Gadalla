---
name: design
description: >
  Unified design routing skill. Answers "how should this look?" at every layer —
  from Anthropic brand compliance to generative art to web UI to slide themes.
  Invoke this skill whenever a visual design question arises; it routes to the
  right sub-skill based on the output medium and creative latitude requested.
auto-trigger:
  - visual design task without a specific named tool
  - layout, typography, colour, or composition decisions
  - "design this page", "make this look good", "visual hierarchy"
do-not-trigger:
  - code-only tasks
  - purely textual content generation

---

# Design — Unified Routing Skill

One entry point for all visual design decisions. Read the request, identify the medium and latitude, then follow the matching path below.

---

## Routing table

| Medium | Creative latitude | Path |
|---|---|---|
| Static art — poster, print, PDF/PNG canvas | High (original artwork) | → **canvas-design** |
| Web UI — page, component, app interface | High (distinctive point of view) | → **frontend-design** |
| Slides, docs, reports, HTML pages | Low–medium (apply a preset or custom theme) | → **theme-factory** |
| Any artifact that must carry Anthropic branding | Any | → **brand-guidelines** (apply after the medium path) |

If the request spans multiple rows (e.g., "an Anthropic-branded web page"), run the medium path first, then layer brand-guidelines on top.

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
