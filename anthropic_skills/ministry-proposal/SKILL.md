# ministry-proposal

Orchestrator for MY4 Education ministry-facing proposal decks. Coordinates research, fact-checking, brand compliance, and PPTX/PDF output against a declared baseline reference.

## Trigger

`/ministry-proposal [--draft | --final] [proposal-docx]`

## Primary Reference

**MBK_Jahizoon_MoSS_AR_v2.pdf** is the QA baseline for all layout, content, and stat decisions. Every slide in the output deck is benchmarked slide-by-slide against this document before handoff.

- Layout: match section flow and information hierarchy from the reference
- Stats: all figures cross-checked via `/fact-checker` before inclusion
- Arabic RTL: use Gamma export (`exportAs: "pptx"`) — never python-pptx text insertion into LTR frames
- Brand: MY4 Education brand system (Black `#0E0E0E` · Gold `#C8A24C` · White `#FFFFFF` · Red `#A4232A`; Montserrat + Inter)

## Orchestration sequence

```
1. /fact-checker --strict [proposal-docx]
   → Gate: no ❌ rows allowed in final mode. ⚠️ rows must be disclosed in deck footnotes.

2. Brand alignment check
   → Verify against MY4_Education_Brand_Guidelines.pdf:
      - Colors: #0E0E0E / #C8A24C / #FFFFFF / #A4232A
      - Fonts: Montserrat (display) + Inter (body)
      - Woven mark: gold on black, corner-anchored
      - Logo lockup on cover

3. Gamma generation (if rebuilding deck)
   → Theme: aurum (closest available to brand palette)
   → exportAs: "pptx"
   → textOptions: { language: "ar" }
   → imageOptions: { source: "noImages" }
   → Download via browser — assets.api.gamma.app is blocked in remote Claude Code environments

4. Slide-by-slide QA vs MBK_Jahizoon_MoSS_AR_v2.pdf
   → Section order, stat placement, CTA structure
   → Flag any divergence before handoff

5. Output checklist
   [ ] All ❌ claims removed or restated
   [ ] All ⚠️ claims footnoted with caveat
   [ ] Brand colors / fonts / woven mark confirmed
   [ ] Arabic renders correctly (not garbled LTR frames)
   [ ] Ministry ask is explicit: 3-part (endorsement / pilot sites / co-funding)
   [ ] Contact slide includes correct details
```

## Slide structure (10 slides)

| # | Arabic title | Content |
|---|---|---|
| 1 | Cover | MY4 Education + وزارة التضامن الاجتماعي + date |
| 2 | الملخص التنفيذي | 3-line executive summary |
| 3 | المشكلة | Stats: unemployment, NEET, skills gap |
| 4 | النموذج الثلاثي | 3-step solution model |
| 5 | إثبات النجاح | AAST pilot results |
| 6 | خارطة الطريق | 3-phase roadmap (6 / 12 / 24 months) |
| 7 | مؤشرات الأداء | KPI table |
| 8 | التوافق مع الوزارة | Alignment with MoSS strategic pillars |
| 9 | المطلوب من الوزارة | 3-part ask |
| 10 | Contact | Closing + contact details |

## Known constraints

- **Gamma PPTX download**: `assets.api.gamma.app` is blocked in Claude Code remote environments. Always instruct the user to download via browser.
- **Nexford stats**: 78% employment / 41% salary increase / 51% promotion — single-sourced. Run `/fact-checker --strict` and footnote these until a second independent source is obtained.
- **Dependency review CI**: GitHub Dependency Graph must be enabled in repo Settings → Security & analysis. This is a repo config issue, not a code fix.
