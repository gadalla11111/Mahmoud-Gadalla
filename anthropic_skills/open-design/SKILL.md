# Skill: open-design

**Trigger:** generate UI from brand design system, apply brand tokens to a prototype, "make it look like [brand]", DESIGN.md workflow, brand-consistent UI generation, design system enforcement across artifacts.

---

## What this skill does

Routes UI generation through Open Design — the open-source agent-native design tool that reads
a single `DESIGN.md` brand schema and generates brand-consistent web prototypes, dashboards,
decks, images, and video across 22+ coding agents including Claude Code.

**Source:** `nexu-io/open-design` | 100+ skills · 261 plugins · 150 pre-built design systems

---

## DESIGN.md — the brand schema

A 9-section Markdown file that controls all visual output:

```markdown
# DESIGN.md
## Color Palette
primary: #0F172A   accent: #6366F1   background: #FFFFFF

## Typography
heading: Inter 700   body: Inter 400   mono: JetBrains Mono

## Spacing
base: 4px   scale: 4/8/12/16/24/32/48/64

## Components
button: radius-md shadow-sm    card: border radius-lg

## Motion
duration: 200ms   easing: ease-out

## Voice and Tone
concise, direct, no jargon

## Brand Guidelines
...

## Anti-patterns
no drop shadows on text, no Comic Sans
```

Switch design systems instantly without regenerating — the entire output reshapes to the new tokens.

---

## Install (Claude Code MCP integration)

```bash
od mcp install claude
# → wires open-design MCP server into Claude Code
# → all design skills become available as tools
```

Or from source:
```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design && corepack enable && pnpm install
pnpm tools-dev run web
```

---

## Usage patterns

```bash
# CLI: generate a landing page in Stripe's design system
od apply saas-landing --design stripe --brief "SaaS pricing page, 3 tiers"

# CLI: pick from 73+ brand DESIGN.md files (awesome-design-md)
od plugin apply linear --brief "kanban dashboard"

# list available design systems
od plugin list --type design-system

# search skills by scenario
od plugin search "dashboard"
```

---

## Key skill modes

| Mode | Skills |
|---|---|
| Prototype | `web-prototype`, `saas-landing`, `dashboard`, `mobile-app`, `mobile-onboarding` |
| Deck | `guizang-ppt`, `html-ppt-*` (15 templates, 36 themes) |
| Media | `image` (93 prompt templates), `hyperframes` (HTML→MP4), `video` |
| Utility | `critique` (5-dimension self-eval), `tweaks` (parameter panels) |

---

## Brand DESIGN.md library (awesome-design-md)

73+ pre-built brand files for: Linear, Stripe, Notion, Figma, Vercel, Supabase, Sentry,
PostHog, Apple, Tesla, Spotify, Airbnb, Nike, BMW, Coinbase, and more.

```bash
# use a pre-built brand
od plugin apply stripe --brief "payment checkout flow"
```

---

## Anti-patterns

- Don't hardcode colors/fonts in generated HTML — always read from DESIGN.md
- Don't regenerate from scratch when switching brands — swap DESIGN.md, re-render
- Don't skip DESIGN.md for "quick" prototypes — consistency is the point

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/frontend-design
  - anthropic_skills/canvas-design
  - anthropic_skills/ui-ux-pro-max
archetype: design-system
```
