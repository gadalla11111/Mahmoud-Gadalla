# Skill: html-anything

**Trigger:** convert markdown/CSV/JSON to HTML, generate ship-ready HTML artifacts, HTML prototype from description, social cards, office documents, VFX/motion frames, deck slides as HTML.

---

## What this skill does

Agent-era HTML editor — converts any input format into ship-ready HTML across 9 surfaces.
Detects active coding agents automatically, streams generation with sandboxed preview.

**Source:** `nexu-io/html-anything` | 75 skills × 9 surfaces

---

## 9 Surfaces × 75 Skills

| Surface | Skills (count) | Examples |
|---|---|---|
| **Prototype** | 21 | web, saas-landing, waitlist, pricing, dashboard, docs, blog, mobile-app, onboarding, editorial |
| **Deck** | 20 | swiss-international, guizang-editorial, magazine-web, pitch, product-launch, blueprint, course-module |
| **Frame/VFX/Mockup** | 12 | liquid-hero, data-chart, glitch-title, hyperframes, sprite-animation, 3d-mockup, logo-outro |
| **Social** | 8 | x-card, spotify, reddit, carousel, xiaohongshu, dashboard, matrix |
| **Office/Doc** | 14 | pm-spec, okrs, meeting-notes, kanban, runbook, finance-report, invoice, live-dashboard |

---

## Usage

```bash
# CLI
html-anything prototype web --brief "SaaS pricing page, 3 tiers, dark mode"
html-anything deck pitch --brief "Seed round deck, 10 slides, AI startup"
html-anything social x-card --brief "Thread announcement, bold typography"

# In agent: describe the surface + brief
# → streams HTML into sandboxed iframe
# → one-click export: WeChat / X / Zhihu / standalone file
```

---

## When to use vs open-design

| Need | Use |
|---|---|
| Brand-consistent output (DESIGN.md) | `open-design` |
| Rapid HTML from any input format | `html-anything` |
| Social card / office doc / motion frame | `html-anything` |
| Design system enforcement | `open-design` |

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/open-design
  - anthropic_skills/frontend-design
  - anthropic_skills/hyperframes
archetype: html-generation
```
