# DESIGN.md — Voltage (Bold High-Contrast / Streetwear)

> Brand-neutral design system, ready to clone per client. To brand it: replace the palette
> hex values and the fonts below, then the `:root` block in `templates.html` inherits them.

## Color Palette
- primary (ink):   `#0A0A0A`
- surface:         `#FFFFFF`
- muted:           `#7A7A7A`
- line/border:     `#111111`
- accent:          `#C6FF00`
- accent-2:        `#FF2D6E`
- soft-fill:       `#0A0A0A`

## Typography
- heading: `Archivo Black`  weight 900
- body:    `Inter`  weight 400–600
- case:    uppercase   ·   letter-spacing (headings): `-0.01em`

## Spacing
base: 4px · scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96

## Components
- button: radius `0px` · border `3px` · shadow `8px 8px 0 #0A0A0A`
- card:   radius `0px` · 1px line border · surface fill
- corners: `0px` throughout · borders `3px`

## Motion
duration: 200ms · easing: ease-out · hover: subtle lift / accent shift only

## Voice and Tone
Loud, blunt, high-energy. Short punches. ALL-CAPS headlines. Zero filler. Says it once, says it hard.

## Brand Guidelines
Accent is a spotlight, not a wash — one accent moment per view. Keep contrast high enough for
AA text. Headlines carry the idea; body copy supports. One idea per asset.

## Anti-patterns
No pastels. No rounded corners. No soft shadows. No timid type. Don't whisper — this system shouts.

## Post templates (see `templates.html`)
1. Carousel slide — 1080×1350 (4:5)
2. Infographic / explainer — 1080×1350 (4:5)
3. Quote / stat card — 1080×1080 (1:1)
4. Reel / story cover — 1080×1920 (9:16)
