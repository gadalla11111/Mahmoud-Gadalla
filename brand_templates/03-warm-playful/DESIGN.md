# DESIGN.md — Sunny (Warm & Playful / Lifestyle)

> Brand-neutral design system, ready to clone per client. To brand it: replace the palette
> hex values and the fonts below, then the `:root` block in `templates.html` inherits them.

## Color Palette
- primary (ink):   `#3B2E2A`
- surface:         `#FFF7EF`
- muted:           `#9B8A80`
- line/border:     `#F0E2D4`
- accent:          `#E8674C`
- accent-2:        `#F4B740`
- soft-fill:       `#FFEEDD`

## Typography
- heading: `Quicksand`  weight 700
- body:    `Nunito`  weight 400–600
- case:    none   ·   letter-spacing (headings): `0em`

## Spacing
base: 4px · scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96

## Components
- button: radius `28px` · border `2px` · shadow `0 12px 28px rgba(232,103,76,.18)`
- card:   radius `28px` · 1px line border · surface fill
- corners: `28px` throughout · borders `2px`

## Motion
duration: 200ms · easing: ease-out · hover: subtle lift / accent shift only

## Voice and Tone
Warm, upbeat, human. Talks like a friend who's genuinely excited. Emoji welcome, in moderation.

## Brand Guidelines
Accent is a spotlight, not a wash — one accent moment per view. Keep contrast high enough for
AA text. Headlines carry the idea; body copy supports. One idea per asset.

## Anti-patterns
No cold greys as primary. No sharp corners. No corporate stiffness. Don't overload — keep it light and breezy.

## Post templates (see `templates.html`)
1. Carousel slide — 1080×1350 (4:5)
2. Infographic / explainer — 1080×1350 (4:5)
3. Quote / stat card — 1080×1080 (1:1)
4. Reel / story cover — 1080×1920 (9:16)
