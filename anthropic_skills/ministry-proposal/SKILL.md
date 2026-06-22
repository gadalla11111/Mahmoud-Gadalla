---
name: ministry-proposal
description: >
  Produces high-quality Arabic ministry proposals aligned with the MY4 Education /
  MERIDIAN brand system, Egyptian ministry strategy (رؤية ٢٠٣٠ / SCU 2025 /
  START 2026), and formal فصحى writing register. Use when drafting a proposal for
  وزارة التضامن الاجتماعي, وزارة التعليم العالي, or any Egyptian governmental body.
  Trigger phrases: "ministry proposal", "وزارة", "مقترح", "MERIDIAN proposal".
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep]
argument-hint: "<initiative-title> [--ministry <ministry-name>] [--phase draft|review|finalize]"
---

# Ministry Proposal Skill

Produces proposals that match the MY4 Education MERIDIAN visual system and formal Egyptian governmental writing standards.

---

## System Reference

### MERIDIAN Brand System

**Color palette**

| Role | Hex | Usage ratio |
|---|---|---|
| Black | `#0E0E0E` | 64 % — layout carrier, slide background |
| White | `#FFFFFF` | 20 % — body text on black, breathing space |
| Gold | `#C8A24C` | 11 % — ONE accent per slide; never flood |
| Red | `#A4232A` | 5 % — critical callout only; never decorative |

**Typography**

| Scale | Font | Weight | Size |
|---|---|---|---|
| Display | Montserrat | Black / ExtraBold | 44 pt |
| Headline | Montserrat | Bold | 34 pt |
| Section | Montserrat | SemiBold | 20 pt |
| Label | Montserrat | SemiBold | 10 pt, tracked |
| Body | Inter | Regular | 13 pt |
| Caption / source | Inter | Regular | 9 pt |

**Woven mark** — interlocking fine-line grid, gold on black, bleed off one corner edge at ~25 % opacity. Appears as watermark on section dividers and cover; never full-bleed on content slides.

**Icon style** — solid gold glyphs in rounded black square chips; one weight; no outlines.

**Do / Don't**

| Do | Don't |
|---|---|
| Black carries layout | Let red flood more than one element |
| Gold guides eye to ONE thing | Recolor the wordmark |
| Generous margins (≥ 12 % of slide width) | Use gold text on white at small sizes |
| Montserrat for display + Inter for body | Mix more than two type families |
| Woven mark at corner, not center | Crowd content — white space is structural |

---

### Twelve-Slide Section Schema

```
01  Cover
02  Table of Contents
── Section divider 01 ──  الإشكالية
03  Statistics / Problem Data
── Section divider 02 ──  الحل
04  Solution Mechanics
05  Proof / Pilot Evidence
── Section divider 03 ──  خطة المراحل
06  Phases Timeline
── Section divider 04 ──  الطلب من الوزارة
07  KPIs + Ministry Alignment
08  Contact / Thank You
```

**Section dividers**: full-bleed black; large gold numeral (44 pt Montserrat Black) top-left; Arabic section title centered; woven mark bleeds from bottom-right corner.

**Content slide anatomy**:
- Top bar: gold label (10 pt Montserrat SemiBold, tracked) flush right
- Body: Inter 13 pt white on black
- Callout stat: Montserrat ExtraBold 44–64 pt gold, followed by Inter 13 pt explanation below
- Source caption: Inter 9 pt, `المصدر: <body>، <date>` format, flush bottom-left

---

### Formal Arabic Writing Register (فصحى رسمية)

**Tashkeel** — selective, grammatically critical words only:
- Mark case endings where ambiguity exists: `طالبةً الرعايةَ الرسمية`
- Mark verb forms where misreading changes meaning: `يُفنِّدها`
- Never tashkeel entire paragraphs

**Punctuation**

| Element | Rule |
|---|---|
| Em-dash `—` | Parenthetical precision; enclose in spaces: `— لم يُفنِّدها دراسة واحدة —` |
| ◈ | Bullet character for all lists (not •, -, *) |
| Superscript | Footnote reference inline: `6.3%¹` |
| Comma | Arabic comma `،` not Latin `,` in Arabic runs |

**Evidence-before-claim rule** — inviolable:
```
[Statistic] [Source citation] — then — [Implication/claim]
```
Never state a claim then support it. The data speaks first.

Attribution format:
```
المصدر: CAPMAS، الربع الرابع ٢٠٢٥
```

**Parallel structure** — list items must share identical grammatical pattern (same verb form, same noun case).

**Register markers** — use these constructions:
- `تتشرف [org] بتقديم...` (cover opening)
- `انطلاقاً من...` (contextual grounding)
- `إيماناً بأن...` (principled rationale)
- `نتطلع إلى شرف تعاونكم` (closing request)

---

### Ministry Alignment Framework

Every ask must map to ≥ 1 national strategy. Include explicit checkmark table in KPIs slide.

| Strategy | Alignment claim |
|---|---|
| رؤية مصر ٢٠٣٠ | خريج اقتصاد المعرفة — knowledge-economy graduate pipeline |
| الإطار المرجعي للتعليم العالي SCU 2025 | ربط المناهج بسوق العمل — curriculum-market linkage |
| قمة START 2026 وزارة التضامن | منصات التدريب المهني — vocational training platforms |
| وحدات التضامن الجامعية | 43 جامعة / أكثر من ٢٥٠ ألف طالب — direct beneficiary base |

Narrative arc: **اتكالية → استقلال** (dependency → independence). Every phase should show measurable progression on this axis.

---

## Phases

### Phase 1 — Draft

**Steps**:
1. Confirm initiative title (Arabic), ministry name, lead contact, and date.
2. Ask: What is the core problem in one sentence? What is the proposed solution? What is the specific ask (funding / MOU / data access)?
3. Build the 8-slide content plan using the schema above. For each content slide, list:
   - Headline (Montserrat 34 pt)
   - One gold callout stat with source
   - Body paragraph (≤ 60 words in Arabic)
4. Write all Arabic copy following the فصحى register rules.
5. Output a slide-by-slide content document in this format:

```markdown
## Slide N — [Role]
**Label (gold, tracked)**: ...
**Headline**: ...
**Body**: ...
**Stat callout**: [number] — [source in Arabic]
**Source caption**: المصدر: ...
```

**Gate before proceeding**: every stat has a source; no claim precedes its evidence; gold accent assigned to exactly one element per content slide.

---

### Phase 2 — Review

**Steps**:
1. Read the draft output.
2. Check each slide against:

| Check | Pass condition |
|---|---|
| Color discipline | Gold appears once per slide maximum |
| Evidence order | Statistic precedes claim on every data slide |
| Tashkeel | Applied only to ambiguous critical words |
| Ministry alignment | KPIs slide has explicit ✓ table for all 4 strategies |
| Section dividers | Appear before each of the 4 major sections |
| Word count | No content slide exceeds 80 Arabic words |
| Register | Arabic comma `،`; em-dash parentheticals; ◈ bullets |

3. Output a review table:

```markdown
## Review: [Initiative Title]

| Slide | Issue | Fix required |
|---|---|---|
| 03 | Claim precedes stat | Move CAPMAS citation before implication |
| 07 | Missing START 2026 alignment | Add ✓ row to alignment table |
```

4. List zero-issue slides as "✓ Pass".

---

### Phase 3 — Finalize

**Steps**:
1. Apply all review fixes.
2. Verify:
   - Cover has: initiative title, ministry name, date, contact (name / email / phone)
   - TOC lists all 4 Arabic section titles with gold numbering
   - Contact slide closes with: `نتطلع إلى شرف تعاونكم`
3. Output final slide-by-slide document, production-ready for layout.
4. Produce a brief handoff note for the designer:

```markdown
## Designer Handoff — [Initiative Title]

**Brand system**: MERIDIAN — see brand guidelines PDF
**Font stack**: Montserrat (headlines) + Inter (body)
**Background**: #0E0E0E on all slides
**Gold accent**: #C8A24C — maximum ONE accent element per content slide
**Woven mark**: bottom-right corner bleed on cover + all 4 dividers, 25% opacity
**Layout direction**: RTL — all text, numbering, icon placement
**Slide count**: [N]
**Delivery format**: PPTX with embedded fonts
```

---

## Quick-Start (single-command path)

If the user says "draft a ministry proposal for [X]", run Phase 1 immediately without asking for phase selection. Use any detail available in the current conversation as input. If ministry name is absent, default to وزارة التضامن الاجتماعي.

---

## Rules

- **Evidence before claim** — every statistic must appear before any conclusion drawn from it. No exceptions.
- **One gold accent per slide** — if two elements compete for gold, the more impactful one wins; the other becomes white.
- **فصحى رسمية** — never use colloquial (`عامية`) constructions, English loan words, or informal abbreviations in the Arabic body copy.
- **Source every stat** — if a number appears without a citation, flag it as `[مصدر مطلوب]` and do not finalize the slide.
- **Ministry alignment is not optional** — every proposal must include the four-strategy ✓ table in the KPIs slide.
- **Section dividers gate sections** — never jump from one major section to another without a divider slide.
- **RTL layout** — all spatial references (left, right, corner) refer to RTL reading direction: "top-left" means the Arabic start side.
