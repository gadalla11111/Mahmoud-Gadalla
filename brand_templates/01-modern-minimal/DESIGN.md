# DESIGN.md — Clarity (Modern Minimal / Tech-SaaS)

> Brand-neutral design system, ready to clone per client. To brand it: replace the palette
> hex values and the fonts below, then the `:root` block in `templates.html` inherits them.

## Color Palette
- primary (ink):   `#0B0F14`
- surface:         `#FFFFFF`
- muted:           `#6B7280`
- line/border:     `#E6E8EB`
- accent:          `#4F46E5`
- accent-2:        `#06B6D4`
- soft-fill:       `#F4F6F8`

## Typography
- heading: `Inter`  weight 800
- body:    `Inter`  weight 400–600
- case:    none   ·   letter-spacing (headings): `-0.02em`

## Spacing
base: 4px · scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96

## Components
- button: radius `16px` · border `1px` · shadow `0 10px 30px rgba(11,15,20,.08)`
- card:   radius `16px` · 1px line border · surface fill
- corners: `16px` throughout · borders `1px`

## Motion
duration: 200ms · easing: ease-out · hover: subtle lift / accent shift only

## Voice and Tone
Concise, direct, confident. No jargon, no hype. Let whitespace carry the message.

## Brand Guidelines
Accent is a spotlight, not a wash — one accent moment per view. Keep contrast high enough for
AA text. Headlines carry the idea; body copy supports. One idea per asset.

## Anti-patterns
No drop shadows on text. No gradients on body copy. No more than one accent per view. Never crowd the canvas.

## Post templates (see `templates.html`)
1. Carousel slide — 1080×1350 (4:5)
2. Infographic / explainer — 1080×1350 (4:5)
3. Quote / stat card — 1080×1080 (1:1)
4. Reel / story cover — 1080×1920 (9:16)
