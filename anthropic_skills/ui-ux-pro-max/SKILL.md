# Skill: ui-ux-pro-max

**Trigger:** design system generation, UI style selection, "what UI style fits my product", color palette for [industry], font pairing, enterprise UI design, "generate a design system", professional UI for [use case].

---

## What this skill does

AI-powered design system generator with 67 UI styles, 161 color palettes, 57 font pairings,
and 161 industry-specific reasoning rules. Analyzes project requirements and generates a
complete, tailored design system — patterns, styles, colors, typography, anti-patterns.

**Source:** `nextlevelbuilder/ui-ux-pro-max-skill`

---

## Design System Generator

```
INPUT: product description + target industry + tech stack
  ↓
ANALYZE: industry reasoning rules (161 rules across 8 sectors)
  ↓
SELECT: UI style + color palette + font pairing
  ↓
OUTPUT: complete design system with anti-patterns
```

---

## 67 UI Styles (selection)

| Style | Best for |
|---|---|
| Glassmorphism | SaaS dashboards, dark-mode apps |
| Claymorphism | Consumer apps, playful products |
| Minimalism | Editorial, content, docs |
| Brutalism | Creative agencies, art platforms |
| Neumorphism | IoT interfaces, control panels |
| Bento Grid | Link-in-bio, portfolio, dashboards |
| AI-Native UI | AI tools, chat interfaces |
| Enterprise Flat | B2B SaaS, internal tools |

---

## Industry reasoning rules (161 rules, 8 sectors)

- **Tech & AI** — high contrast, data-dense, monospace accents
- **Finance** — trust signals, muted palette, grid precision
- **Healthcare** — accessibility-first, WCAG AA minimum, calming tones
- **E-commerce** — urgency cues, product-forward, CTA hierarchy
- **Services** — relationship-oriented, photo-led, warm tones
- **Creative** — bold typography, asymmetric layouts, expressive color
- **Lifestyle** — aspirational imagery, serif headings, generous whitespace
- **Emerging tech** — futuristic, dark-first, neon accents

---

## Multi-stack support

React · Vue · Angular · Laravel · iOS · Android · 10+ other frameworks.
Outputs framework-specific component patterns alongside design tokens.

---

## Usage

```
Given: "B2B SaaS analytics platform for enterprise finance teams"
→ Style: Enterprise Flat + Data-dense Grid
→ Palette: #0F172A / #3B82F6 / #F8FAFC (trust + precision)
→ Fonts: Inter 700 headings / Inter 400 body
→ Anti-patterns: no gradients, no decorative icons, no rounded >8px
→ Components: compact tables, badge statuses, sidebar nav
```

---

## Integration with open-design

Use ui-ux-pro-max to SELECT the design system, then encode it into a `DESIGN.md` for
open-design to enforce across all generated artifacts.

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/open-design
  - anthropic_skills/frontend-design
  - anthropic_skills/theme-factory
archetype: design-system
```
