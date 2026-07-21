# DESIGN.md — Maison (Editorial Luxury / Premium)

> Brand-neutral design system, ready to clone per client. To brand it: replace the palette
> hex values and the fonts below, then the `:root` block in `templates.html` inherits them.

## Color Palette
- primary (ink):   `#14110F`
- surface:         `#F7F3EC`
- muted:           `#8A8175`
- line/border:     `#DBD3C6`
- accent:          `#B08D4C`
- accent-2:        `#14110F`
- soft-fill:       `#EFE9DE`

## Typography
- heading: `Playfair Display`  weight 600
- body:    `Inter`  weight 400–600
- case:    none   ·   letter-spacing (headings): `0em`

## Spacing
base: 4px · scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96

## Components
- button: radius `3px` · border `1px` · shadow `none`
- card:   radius `3px` · 1px line border · surface fill
- corners: `3px` throughout · borders `1px`

## Motion
duration: 200ms · easing: ease-out · hover: subtle lift / accent shift only

## Voice and Tone
Refined, understated, assured. Speaks softly. Chooses fewer words, each one deliberate.

## Brand Guidelines
Accent is a spotlight, not a wash — one accent moment per view. Keep contrast high enough for
AA text. Headlines carry the idea; body copy supports. One idea per asset.

## Anti-patterns
No neon. No heavy shadows. No rounded pill buttons. No exclamation marks. Avoid clutter — negative space is luxury.

## Post templates (see `templates.html`)
1. Carousel slide — 1080×1350 (4:5)
2. Infographic / explainer — 1080×1350 (4:5)
3. Quote / stat card — 1080×1080 (1:1)
4. Reel / story cover — 1080×1920 (9:16)
