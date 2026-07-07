# Skill: brand-identity-pillars

**Trigger:** brand pillars, brand identity system, logo system design, brand color system, brand typography, brand imagery direction, visual identity brief, brand design language, brand for sustainability, ESG brand positioning, purpose-driven brand, brand values framework, brand pillar architecture, triple bottom line brand.

---

## What this skill does

Visual identity + brand pillar architecture with a sustainability lens — logo systems, color, typography, imagery, motion principles, and purpose-driven pillar frameworks. Draws on rampstackco brand-identity (five-element identity system), zephyrwang6/brand-design-md (62 world-class brand design languages), and sustainability branding conventions.

**Sources:**
- `rampstackco/claude-skills` — brand-identity skill | MIT
- `zephyrwang6/brand-design-md` — 62 brand design systems | MIT

---

## Five-Element Identity System (rampstackco)

### 1. Logo System
- Marks: primary logo, wordmark, symbol, lockups, monogram, favicon
- Critical rule: legible at 16px (favicon test) — if it falls apart, redesign
- Context matrix: print, digital, embroidery, emboss, dark/light backgrounds

### 2. Color System
- Roles: primary, secondary, neutral, semantic (success/warning/error/info), accent
- Document: hex, RGB, CMYK, Pantone, WCAG contrast ratios, usage rules
- Dark mode variants, print-safe swatches

### 3. Typography
- Display + body typeface pair; type scale (5–8 steps)
- Web licensing confirmation; system font fallbacks
- Hierarchy rules: heading levels, caption, label, UI text

### 4. Imagery & Iconography
- Photography direction: subject, lighting, composition, color grading, banned tropes
- Illustration style: stroke weight, fill approach, metaphor palette
- Icon conventions: size grid, corner radius, optical alignment

### 5. Motion
- Easing curves, duration scales, choreography for digital and video
- Entrance, exit, micro-interaction patterns

---

## Brand Pillar Architecture

A pillar is a belief the brand will defend publicly and consistently.

### Pillar Framework (3–5 pillars)
| Pillar | Definition | Proof point | Expression |
|---|---|---|---|
| [Name] | What we believe | How we demonstrate it | How it shows in product/content |

### Sustainability Pillar Layer
For purpose-driven or ESG-positioned brands:
- **Environmental** — carbon commitments, materials, circularity, supply chain
- **Social** — labour standards, community impact, diversity in supply chain
- **Governance** — transparency, B-Corp/GRI/SASB reporting alignment
- **Communication** — greenwashing guard: claims must be specific, measurable, verified
- **Visual coding** — palette, material photography, packaging language that signals sustainability authentically

### Pillar ↔ Identity Coherence Test
Every identity element should reinforce at least one pillar. Inconsistency between pillars and visual identity is the most common brand failure.

---

## Brand Design Languages (zephyrwang6/brand-design-md)

Access exact design values for 62 world-class brands on demand:
```bash
npx getdesign@latest add <slug>   # e.g. nike, stripe, notion, airbnb
```
- Request: "Build in Nike style" → exact letter-spacing, weights, grid
- Mix: "Notion warm colors + Linear minimal layout"
- Output: HTML, React, Vue, or Tailwind

**Covered sectors:** Tech/AI (Apple, Claude, Figma, Vercel, Stripe, Linear), Infrastructure (IBM, HashiCorp), Fintech (Coinbase, Wise), Consumer (Nike, Tesla, Spotify, Airbnb, Uber)

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/brand-building
  - anthropic_skills/brand-guidelines
  - anthropic_skills/open-design
archetype: brand-identity-sustainability
```
