---
name: ministry-proposal
description: >
  Produces high-quality Arabic ministry proposals for MBK Education / جاهزون
  initiatives, aligned with the Egyptian ministry strategy (رؤية ٢٠٣٠ / SCU 2025 /
  START 2026 / برنامج فرصة) and formal فصحى writing register. Routes by brand:
  MERIDIAN (black-dominant, MY4 Education) or Jahizoon (navy-dominant, MBK Education).
  Use when drafting for وزارة التضامن الاجتماعي, وزارة التعليم العالي, or any
  Egyptian governmental body. Trigger phrases: "ministry proposal", "وزارة",
  "مقترح", "جاهزون", "MERIDIAN proposal".
  Mandatory gates: fact-checker before finalizing (every stat needs 3 sources);
  Nexford figures (78%/41%/51%) are single-sourced — flag and seek 2nd source.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep]
argument-hint: "<initiative-title> [--brand meridian|jahizoon] [--phase draft|review|finalize]"
auto-trigger:
  - Arabic ministry proposal or official document (وزارة)
  - MBK Education / Jahizoon / MERIDIAN brand content
  - Egyptian ministry-aligned programme narrative
  - proposal following the 15-slide Jahizoon schema
do-not-trigger:
  - generic Arabic writing
  - non-ministry English documents
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues:
    - "Nexford 78%/41%/51% figures are single-sourced — 2nd source not yet found"

---

# Ministry Proposal Skill

Produces proposals that match either MBK Education visual system and Egyptian governmental writing standards. Two brand variants; share the same Arabic register and strategy alignment rules.

---

## ⚠️ Source Warning — Read Before Producing Numbers

The following figures come from a **single source** (Nexford employer survey 2026):
- **78%** — employers can't find required skills
- **41%** — employers who call it a major hiring challenge
- **51%** — employers willing to fund training

These **must** be flagged `[مصدر إضافي مطلوب]` in any draft until a second independent source is confirmed. Do not finalize slides 04 or 11 without resolving this. Use `fact-checker` skill to search for corroborating employer surveys.

All other figures (CAPMAS 41.5%/6%, Consensus.app meta-analysis, MBK pilot numbers) have multiple sources and can be used without flags.

---

## Primary References

| File | Role |
|---|---|
| `MBK_Education_Brand_Guidelines.pdf` + `.pptx` | MERIDIAN design system — colours, typography, woven mark, icon rules |
| `MBK_Jahizoon_MoSS_AR_v2.pdf` / `.pptx` | **QA reference** — every layout decision and Arabic copy benchmarked here |
| `MBK_Education_Field_Ready_Ministry.pptx` | English parallel (same initiative, different audience) |
| `Generic_Issue.pptx` | Full 15-slide schema — authoritative slide structure |

**The MBK_Jahizoon_MoSS_AR_v2 PDF is the QA grid baseline.** When reviewing, compare slide-by-slide: gold placement, stat card layout, 3-party footer, co-branding positions, Arabic phrasing. Any deviation requires justification.

> All content produced by this skill must pass `anthropic_skills/fact-checker` before finalizing. Every statistic needs 3 independent sources.

---

## Visual System A — MERIDIAN (MY4 Education)

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
| Section label | Montserrat | SemiBold | 20 pt |
| Label / tracked | Montserrat | SemiBold | 10 pt |
| Body | Inter | Regular | 13 pt |
| Caption / source | Inter | Regular | 9 pt |

**Woven mark** — interlocking fine-line grid, gold on black, bleeds off one corner edge at ~25 % opacity. Appears on section dividers and cover; never on content slides.

**Icon style** — solid gold glyphs in rounded black square chips; one weight; no outlines.

---

## Visual System B — Jahizoon (MBK Education)

**Color palette**

| Role | Hex | Usage ratio |
|---|---|---|
| Navy | `#1C2B45` | ~65 % — slide background |
| White | `#FFFFFF` | ~25 % — body text and headings |
| Gold | `#C8A24C` | ~10 % — stat callouts, accent text, section labels |

**Typography**: Same Montserrat + Inter stack as MERIDIAN. Headings Montserrat Bold white; section labels Montserrat SemiBold gold small; body Inter white.

**Geometric accent**: Large dark circle (navy-on-navy, slightly lighter) bottom-left corner — structural, not content.

**Ministry co-branding**: Cover includes dashed placeholder box for وزارة التضامن الاجتماعي logo; MBK EDUCATION wordmark top-right. Final slide mirrors this layout.

**Stat cards**: Gold percentage / number in a dark rounded card with white label below. 3-column grid on KPI slides.

---

## Shared Design Rules

| Do | Don't |
|---|---|
| Gold guides eye to ONE thing per slide | Let red flood more than one element |
| Generous margins (≥ 12 % of slide width) | Recolor the wordmark |
| Montserrat for display + Inter for body | Mix more than two type families |
| RTL layout — all text and numbering | Use gold text on white at small sizes |
| Navy or black backgrounds consistently | Switch background color mid-deck |

---

## Jahizoon Full Schema (15 slides — Generic_Issue version)

```
01  Cover (غلاف)
    — "MBK EDUCATION ✕ وزارة التضامن الاجتماعي" co-brand header
    — "مبادرة وطنية لتأهيل الشباب وتمكينه اقتصاديًا"
    — Display title: جاهزون (Montserrat ExtraBold, large)
    — "من قاعة الدرس إلى سوق العمل: تدريب عملي حقيقي داخل الشركات،
       يُختتم بامتحان مُصوّر يُثبت جاهزية الشاب للعمل."
    — "مقدَّم إلى وزارة التضامن الاجتماعي · مقترح شراكة"

02  خريطة العرض (Table of Contents)
    — 6 sections in 2 columns:
      ٠١ من نحن          ٠٤ المرحلة التجريبية والخطة
      ٠٢ المشكلة والفرصة  ٠٥ الأثر والفريق والإعلام
      ٠٣ الحل: كيف يعمل  ٠٦ التوافق مع الوزارة والطلب

03  من نحن — جهة شغّلت النموذج بالفعل
    — MBK Education description (founder: محمود جاد الله)
    — 3 verified proof bullets (AAST warehouse exam)
    — Gold italic: «جاهزون» هو هذا النموذج، موسَّعًا وطنيًا بالشراكة مع الوزارة
    — Photo placeholder: الامتحان العملي لإدارة المخازن
    ✓ Validation: founder name spelled correctly; AAST acronym expanded on first use

04  المشكلة والفرصة — الشهادة وحدها لا تصنع فرصة عمل
    — Research consensus callout: "إجماع بحثي مصري: 13 دراسة، 100% تؤكد
       وجود فجوة مهارات لدى الخريجين — في المهارات السلوكية والإدارية والتطبيقية"
      (Source: Consensus.app meta-analysis, N=13 Egyptian studies)
    — Bar chart: 41.5% (خريجو الجامعات) vs 6% (إجمالي القوى العاملة)
    — 3 employer stat cards: 78% / 41% / 51%
    — Source caption: CAPMAS الربع الأول ٢٠٢٦؛ استطلاع Nexford، ٢٠٢٦
    ⚠️  Validation gate: 78%/41%/51% must carry [مصدر إضافي مطلوب] until 2nd source confirmed

05  لماذا ينجح هذا النموذج — السبب معروف في مصر والحل هو نموذجنا
    — 3 cause → solution pairs (root-cause mapping):
      السبب: مناهج غير محدَّثة وبعيدة عن احتياجات سوق العمل
      ↓ ماذا يفعل «جاهزون»: منهج مبني على مهام واقعية داخل الشركة، يُصمَّم مع أصحاب العمل
      السبب: ضعف التنسيق بين الجامعة وأصحاب العمل
      ↓ ماذا يفعل «جاهزون»: شراكة تشغيل مباشرة مع شركات مضيفة طوال فترة التدريب
      السبب: غياب التدريب العملي والإرشاد المهني
      ↓ ماذا يفعل «جاهزون»: شهر تدريب ميداني تحت إشراف + امتحان مُصوَّر
    ✓ Validation: 3 pairs complete; each pair is parallel grammatically

06  الحل · كيف يعمل — تدريب حقيقي، يُثبَت بالكاميرا
    — 7 skills being built (listed as tags):
      التواصل · حل المشكلات · التخطيط · إدارة الوقت
      إدارة المشروعات · العمل الجماعي · التفكير النقدي
    — 3-step cards: 01 التحاق / 02 تدريب / 03 إثبات
    — 3-party footer: الوزارة (تُمكِّن وتموِّل وترعى) /
                      الشركات المضيفة (تُدرِّب عينيًا وتوظِّف) /
                      MBK (تُشغِّل وتنتج وتقيِّم)
    ✓ Validation: 3-party footer uses مضارع verbs in parallel; 7 skills listed

07  الامتحان المُصوَّر — قلب المبادرة
    — "ليس امتحانًا ورقيًا. الشاب يؤدّي مهامًا حقيقية أمام لجنة وكاميرا —
       فيتحوّل التدريب إلى دليل، والدليل إلى قصة."
    — Assessment framing: إثبات لا يُجامَل — أداء فعلي / تقييم من خبراء / شهادة يثق بها صاحب العمل
    — Media framing: حلقة ختامية مُصوَّرة تُبثّ تلفزيونيًا / رحلة تحوّل الشاب / يجذب الرعاة
    — Photo placeholder (pilot exam footage)
    ✓ Validation: both dimensions (assessment + media) present on same slide

08  النتائج المباشرة · المرحلة التجريبية
    — 4 stat boxes: 1 جامعة / 3 كليات / 2 شركتان مضيفتان / 45 شابًا في الدورة
    — Faculty cards with icons:
      إدارة الأعمال — الوظائف التجارية والتشغيلية
      سلاسل الإمداد — المخازن واللوجستيات والمشتريات
      التسويق — الحملات والمحتوى والمبيعات
    ✓ Validation: pilot numbers match Confirmed Statistics Reference table

09  الجدول الزمني للمرحلة التجريبية
    — 8-week pilot cycle (horizontal timeline):
      أسبوع ٠   التحضير والشراكات
      أسبوع ١–٢ الالتحاق والتأهيل
      أسبوع ٣–٥ التدريب الميداني
      أسبوع ٦   الامتحان المُصوَّر
      أسبوع ٧–٨ التقييم والنشر
    ✓ Validation: 5 phases cover 8 weeks exactly; labels are masdar form

10  خطة المراحل — من 45 شابًا إلى برنامج وطني
    — Growth: 45 (تجريبية) → ~500 (توسّع) → +3,000 (وطنية)
    — 3 timeline cards (قصير / متوسط / طويل المدى)
    — ~3.6M students / 73 universities footnote
    ✓ Validation: growth numbers consistent with slides 08 and 11; source footnote present

11  مؤشرات الأداء والأثر
    — 6-card KPI grid:
      ≥ 60%   نسبة الجاهزية للتوظيف خلال 6 أشهر
      ≥ 40%   تحويل التدريب إلى عرض عمل فعلي
      ≥ 90%   إتمام الشهادة المهارية
      3,000+  شاب يُدرَّب سنويًا
      ≥ 85%   رضا جهات التشغيل
      12+     محافظة
    ✓ Validation: KPI targets are aspirational but grounded; 41.5% baseline cited for context

12  الفريق والموارد
    — 3-layer structure: MBK / الشركاء / من الوزارة
    ✓ Validation: "من الوزارة" section is explicit ASK framing, not assumption

13  الخطة الإعلامية
    — 3 phases: إنتاج / بثّ / أثر
    ✓ Validation: START 2026 platform named explicitly in بثّ phase

14  الاتجاه قائم بالفعل
    — 3 existing programmes: برنامج فرصة / وحدات التضامن / قمة ستارت 2026
    ✓ Validation: «جاهزون» framed as completing, not replacing, ministry programmes

15  التوافق مع الوزارة · الطلب
    — Gold italic tagline + 3 alignment bullets + Ask box + co-branding footer
    — Closes: نتطلع إلى شرف تعاونكم
    ✓ Validation: ≥3 ministry strategies checked; Ask box states funding + university access explicitly
```

---

## Confirmed Statistics Reference

| Stat | Figure | Arabic source label | 2nd source? |
|---|---|---|---|
| Graduate unemployment | **41.5%** | CAPMAS، الربع الأول ٢٠٢٦ | ✓ CAPMAS official |
| Overall labour force unemployment | **6%** | CAPMAS، الربع الأول ٢٠٢٦ | ✓ CAPMAS official |
| Employers can't find required skills | **78%** | استطلاع Nexford، ٢٠٢٦ | ⚠️ single source |
| Employers who call it a major hiring challenge | **41%** | استطلاع Nexford، ٢٠٢٦ | ⚠️ single source |
| Employers willing to fund training | **51%** | استطلاع Nexford، ٢٠٢٦ | ⚠️ single source |
| Employers offering jobs to interns post-training | **8 من 10** | مراجعات دولية للتعلّم المبني على العمل | ✓ international literature |
| Trainees with required behavioural skills | **63%** | مراجعات دولية | ✓ international literature |
| Egyptian studies confirming skills mismatch | **13 من 13 (100%)** | Consensus.app meta-analysis, N=13 | ✓ peer-reviewed |
| Students in higher education | **~3.6M** | المجلس الأعلى للجامعات | ✓ official |
| Universities nationwide | **73** | المجلس الأعلى للجامعات | ✓ official |
| Pilot cohort size | **45 شابًا** | MBK Education تجربة AAST | ✓ internal data |

### Fact-Checker Gate

Before finalizing any proposal:
1. Invoke `anthropic_skills/fact-checker` on all stats in the "⚠️ single source" rows
2. If 2nd source found: update table, remove flag, update source caption on slide
3. If 2nd source not found: keep `[مصدر إضافي مطلوب]` flag visible in the output; do not finalize slide 04

---

## Academic Evidence Layer

Consensus.app meta-analysis (N=13 Egyptian studies) — peer-reviewed backing for problem slide:

- **Consensus**: 100% of 13 Egyptian studies confirm graduate skills mismatch
- **Root causes**: outdated curricula / weak university-employer coordination / limited practical exposure
- **Sectors**: Agriculture, Communication, Hospitality, Architecture, Computer Engineering
- **Missing skills**: leadership, planning, communication, problem-solving, time management, teamwork, critical thinking

**Citation format** (footnotes only — not body text):
```
(Ghimire et al., 2022; Ahmed, 2020; Nassef, 2016)
```

Key papers:
- Ghimire et al., 2022 — employer vs. student self-rating gap (Agriculture)
- Nassef, 2016 — system barriers in Egyptian HE (Computer Engineering)
- Ahmed, 2026 — SSRN: "Employment Gap in Egypt: Hidden Causes and Necessary Solutions"
- Bassyouny, 2024 — stagnant programs, communication sector

---

## Formal Arabic Writing Register (فصحى رسمية)

**Tashkeel** — selective, grammatically critical words only:
- Mark case endings where ambiguity exists: `طالبةً الرعايةَ الرسمية`
- Mark verb forms where misreading changes meaning: `يُثبَت`، `يُدرَّب`، `يُختتم`
- Never tashkeel entire paragraphs

**Punctuation**

| Element | Rule |
|---|---|
| Em-dash `—` | Parenthetical precision; enclose in spaces |
| ◈ | Bullet character for unordered lists (not •, -, *) |
| Superscript | Footnote reference inline: `41.5%¹` |
| Comma | Arabic comma `،` not Latin `,` in Arabic runs |

**Evidence-before-claim rule** — inviolable:
```
[Statistic] [Source] — then — [Implication/claim]
```
Example: `41.5% من خريجي الجامعات عاطلون عن العمل — CAPMAS الربع الأول ٢٠٢٦ — وهذا يعني أن الشهادة وحدها لا تصنع فرصة عمل.`

Attribution format (caption line, Inter 9pt):
```
المصدر: CAPMAS، الربع الأول ٢٠٢٦؛ استطلاع Nexford لأصحاب العمل في مصر، ٢٠٢٦.
```

**Register markers**:
- Cover: `مقدَّم إلى وزارة التضامن الاجتماعي · مقترح شراكة`
- Narrative arc: `من الاتكالية إلى الاستقلال الاقتصادي`
- Final slide closing: `نتطلع إلى شرف تعاونكم`

**Parallel structure** — list items must share identical grammatical pattern:
```
التحاق — تدريب — إثبات          (masdar pattern)
تُمكِّن وتموِّل وترعى           (مضارع، subject: الوزارة)
تُدرِّب عينيًا وتوظِّف          (مضارع، subject: الشركات)
تُشغِّل وتنتج وتقيِّم           (مضارع، subject: MBK)
```

**Arabic typography rules**:
- Numbers in Arabic text use Eastern Arabic numerals (٠١٢٣٤٥٦٧٨٩) for slide labels and ordinals
- Western numerals (0123456789) for percentages and statistics (41.5%, 78%)
- Mixed use on same slide: statistics in Western, ordinal labels in Eastern

---

## Ministry Alignment Framework

| Strategy | Alignment claim |
|---|---|
| رؤية مصر ٢٠٣٠ | إسهام موثَّق في التنمية البشرية وتشغيل الشباب |
| SCU 2025 | ربط المناهج بسوق العمل |
| قمة START 2026 | منصات التدريب المهني |
| برنامج «فرصة» | امتداد طبيعي — الوصول عبر وحدات التضامن بالجامعات |
| وحدات التضامن الجامعية | 73 جامعة / أكثر من ٣.٦ مليون طالب |

Narrative arc: **الاتكالية → الاستقلال الاقتصادي**. Every phase shows measurable movement on this axis.

---

## Phase 1 — Draft

1. Confirm: initiative title (Arabic), ministry, lead contact, date.
2. Confirm: core problem in one sentence, proposed solution, specific ask.
3. Choose brand variant (Jahizoon navy / MERIDIAN black). Default: Jahizoon.
4. Build content slide-by-slide using the 15-slide schema above.
5. For each slide output:

```markdown
## Slide N — [Role] ([Arabic section label])
**Label (gold tracked)**: ...
**Headline (Montserrat Bold white)**: ...
**Body**: ...  (≤ 60 Arabic words)
**Stat callout**: [figure] — [source]  ⚠️ [مصدر إضافي مطلوب] if single-sourced
**Source caption**: المصدر: ...
**Validation**: [per-slide check from schema above]
```

**Gate**: every stat has a source; no claim precedes its evidence; gold accent on exactly one element.

---

## Phase 2 — Review

Check each slide against this grid:

| Check | Pass condition |
|---|---|
| Color discipline | Gold appears once per slide maximum |
| Evidence order | Statistic precedes claim on every data slide |
| Tashkeel | Applied only to ambiguous critical words |
| Ministry alignment | Final slide has ✓ list for ≥ 3 strategies |
| Pilot numbers | 41.5% / 6% / 45 — all sourced; 78%/41%/51% flagged if 2nd source absent |
| Word count | No content slide exceeds 80 Arabic words |
| Register | Arabic comma `،`; em-dash parentheticals where needed |
| Co-branding | Ministry logo placeholder on cover and final slide |
| Typography | Eastern numerals for labels; Western for statistics |
| Parallel structure | Verb form or noun case consistent within each list |
| Per-slide validation | Each slide's ✓/⚠️ check from schema resolved |

Output:

```markdown
## Review: [Initiative Title]

| Slide | Issue | Fix |
|---|---|---|
| 04 | 78% lacks 2nd source | Add [مصدر إضافي مطلوب] flag; invoke fact-checker |
| 09 | Missing برنامج فرصة alignment | Add ✓ row |

✓ Pass: [list clean slides]
```

---

## Phase 3 — Finalize

1. Invoke `fact-checker` on all ⚠️ flagged statistics — do not skip.
2. Apply all review fixes.
3. Verify cover includes: initiative title, tagline, ministry name, "مقترح شراكة", date.
4. Verify final slide closes with: `نتطلع إلى شرف تعاونكم` + contact block.
5. Output final slide-by-slide document, production-ready.
6. Produce designer handoff note:

```markdown
## Designer Handoff — [Initiative Title]

**Brand variant**: Jahizoon (navy) / MERIDIAN (black)
**Background**: #1C2B45 (Jahizoon) or #0E0E0E (MERIDIAN)
**Gold accent**: #C8A24C — maximum ONE accent element per content slide
**Font stack**: Montserrat (headings) + Inter (body)
**Geometric accent**: Large dark circle bottom-left (Jahizoon only)
**Co-branding**: Ministry logo placeholder top-center + MBK wordmark top-right (cover + final slide)
**Layout direction**: RTL — all text, numbering, icon placement
**Slide count**: [N]
**Delivery format**: PPTX with embedded fonts
**Open flags**: [list any remaining ⚠️ items for designer awareness]
```

---

## Quick-Start

If the user says "draft a ministry proposal for [X]", run Phase 1 immediately. Default: Jahizoon (navy) brand, وزارة التضامن الاجتماعي.

---

## Rules

- **Evidence before claim** — every statistic must appear before any conclusion. No exceptions.
- **One gold accent per slide** — if two elements compete, the more impactful wins; the other becomes white.
- **فصحى رسمية** — no colloquial, English loan words, or informal abbreviations in Arabic body copy.
- **Source every stat** — unsourced numbers get `[مصدر مطلوب]` and block finalization.
- **Single-source warning** — Nexford 78%/41%/51% carry `[مصدر إضافي مطلوب]` until a 2nd source is confirmed.
- **Ministry alignment is mandatory** — every proposal must include the ✓ table in the final slide.
- **برنامج فرصة is the entry point** — always frame جاهزون as a natural extension of the ministry's existing فرصة programme.
- **RTL layout** — all spatial references in designer notes are RTL: "top-left" = Arabic start side.
- **Co-brand the cover** — ministry logo placeholder must appear on cover and final slide.
- **Fact-checker gate** — invoke before finalizing; never bypass.
