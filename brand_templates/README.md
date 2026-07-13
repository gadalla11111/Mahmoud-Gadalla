# Brand Templates Kit

Brand-neutral, aesthetically-tuned design systems + ready-to-use social post templates.
Staged so that when a client lands, you clone a folder, recolor once, and ship the same day.

## What's inside

Four aesthetic directions, each a self-contained folder:

| Folder | System | Best for |
|---|---|---|
| `01-modern-minimal/` | **Clarity** | AI / tech / B2B / SaaS |
| `02-editorial-luxury/` | **Maison** | Fashion, luxury, premium (e.g. Men's Club) |
| `03-warm-playful/` | **Sunny** | F&B, wellness, D2C, lifestyle (e.g. Merakii) |
| `04-bold-streetwear/` | **Voltage** | Youth, sport, streetwear (e.g. NEXUS) |

Each folder has:
- **`DESIGN.md`** — the 9-section design-system schema (palette, type, spacing, components,
  motion, voice, anti-patterns). This is the file an AI agent reads (`open-design` skill) to
  generate on-brand UI. Same format as [awesome-design-md](https://github.com/VoltAgent/awesome-design-md).
- **`preview.html`** — a visual showcase of the system (swatches, type scale, buttons, cards).
- **`templates.html`** — four ready-to-use post formats on one page, each at native export size:
  1. **Carousel slide** — 1080×1350 (numbered-list "swipe" format)
  2. **Infographic / explainer** — 1080×1350 (save-bait: stats + steps)
  3. **Quote / stat card** — 1080×1080 (shareable)
  4. **Reel / story cover** — 1080×1920 (scroll-stopping hook)

The post formats mirror what performs in the AI/marketing niche (see the content review in
`social_media_review/`): educational, one-idea-per-asset, save/share-driven.

## How to brand one (≈5 minutes)

1. Pick the folder whose aesthetic fits the client.
2. In `DESIGN.md`, replace the palette hexes + font names with the client's.
3. In `templates.html` (and `preview.html`), edit the `:root { … }` block at the top —
   same variable names. Everything re-skins automatically; **never hardcode colors in the markup.**
4. Swap `@yourbrand`, copy, numbers, and the reel hook.
5. Open the HTML in a browser and screenshot each `.canvas` at native size to export
   (or print-to-PDF). These also import cleanly into Adobe Express / can seed a Canva brand kit.

## Regenerate

All files are generated from `build_templates.py` (kept in the session scratchpad). Re-run it
after editing the token dictionary to rebuild every file consistently.

## Fonts

Files use robust system-font stacks so they render offline. Each has a commented
`@import` line near the top — uncomment it to pull the intended premium web font when online.
