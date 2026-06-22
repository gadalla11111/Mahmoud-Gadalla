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
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep]
argument-hint: "<initiative-title> [--brand meridian|jahizoon] [--phase draft|review|finalize]"
---

# Ministry Proposal Skill

Produces proposals that match either MBK Education visual system and Egyptian governmental writing standards. Two brand variants; share the same Arabic register and strategy alignment rules.

---

## Visual System A — MERIDIAN (MY4 Education)

**Use for**: MY4 Education brand proposals

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

**Use for**: جاهزون initiative proposals to وزارة التضامن الاجتماعي

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

## Jahizoon 9-Slide Schema

```
01  Cover (غلاف)
    — Initiative title + "مبادرة وطنية" tagline
    — "من قاعة الدرس إلى سوق العمل: تدريب عملي..."
    — Ministry logo placeholder + MBK wordmark
    — "مقترح شراكة · مقدَّم إلى وزارة التضامن الاجتماعي"

02  من نحن — جهة شغّلت النموذج بالفعل
    — MBK Education description
    — Pilot proof (AAST warehouse exam)
    — 3 verified bullets

03  المشكلة والفرصة — الشهادة وحدها لا تصنع فرصة عمل
    — Bar chart: 41.5% (graduates) vs 6% (labour force)
    — 3 employer stats: 78% / 41% / 51%
    — Source caption

04  لماذا ينجح هذا النموذج — التدريب العملي يصنع التوظيف بشهادة الأدلة
    — 3 evidence cards: 8/10 / 63% / بقيادة الشركات
    — World Bank Egypt callout box

05  الحل · كيف يعمل — تدريب حقيقي، يُثبَت بالكاميرا
    — 3-step cards: 01 التحاق / 02 تدريب / 03 إثبات
    — 3-party footer: الوزارة / الشركات المضيفة / MBK

06  النتائج المباشرة · المرحلة التجريبية
    — 4 stat boxes: 1 جامعة / 3 كليات / 2 شركتان / 45 شابًا
    — Faculty list with icons (إدارة الأعمال / سلاسل الإمداد / القانون)
    — "شهر واحد من التدريب المنظَّم، يُختتم بامتحان عملي مُصوَّر"

07  خطة المراحل — من 45 شابًا إلى برنامج وطني
    — 3 timeline cards (right = active dark):
      0–6m  قصير المدى: 1 جامعة · 45 شابًا · نموذج مُثبت
      6–18m متوسط المدى: 4 جامعات · 500 شاب · بيانات توظيف
      18–36m طويل المدى: 15+ جامعة · 12+ محافظة · 3,000+ شاب سنويًا
    — Source footnote: 3.6M students, 73 universities

08  مؤشرات الأداء والأثر — أرقام نلتزم بها ونقيسها
    — 6-card KPI grid:
      ≥ 60%  نسبة الجاهزية للتوظيف خلال 6 أشهر
      ≥ 40%  تحويل التدريب إلى عرض عمل فعلي
      ≥ 90%  إتمام الشهادة المهارية
      3,000+ شاب يُدرَّب سنويًا عند التوسّع
      ≥ 85%  رضا جهات التشغيل عن الكوادر
      12+    محافظة يصلها البرنامج وطنيًا
    — Source: CAPMAS + Nexford + WBL reviews

09  التوافق مع الوزارة · الطلب
    — "امتداد طبيعي لبرنامج «فرصة»"
    — Italic gold tagline: «جاهزون» يخدم هدف الوزارة المعلن: الانتقال من الاتكالية إلى الاستقلال الاقتصادي
    — 3 alignment bullets with checkmarks
    — Ask box: "رعاية الوزارة وتمويلها للمرحلة التجريبية، والوصول إلى جامعة شريكة بثلاث كليات، عبر وحدات التضامن بالجامعات"
    — Co-branding footer (mirrors cover)
```

---

## Confirmed Statistics Reference

All figures for جاهزون proposals. Source every stat — do not paraphrase the source label.

| Stat | Figure | Source |
|---|---|---|
| Graduate unemployment | **41.5%** | CAPMAS، الربع الأول ٢٠٢٦ |
| Overall labour force unemployment | **6%** | CAPMAS، الربع الأول ٢٠٢٦ |
| Employers can't find required skills | **78%** | استطالع Nexford لأصحاب العمل في مصر، ٢٠٢٦ |
| Employers who call it a major hiring challenge | **41%** | استطالع Nexford، ٢٠٢٦ |
| Employers willing to fund training | **51%** | استطالع Nexford، ٢٠٢٦ |
| Employers offering jobs to interns post-training | **8 من 10** | مراجعات دولية للتعلّم المبني على العمل |
| Trainees with required behavioural skills | **63%** | مراجعات دولية |
| Students in higher education (current) | **3.6M** | المجلس الأعلى للجامعات / التعليم العالي |
| Universities nationwide | **73** | المجلس الأعلى للجامعات |
| Pilot cohort size | **45 شابًا** | — |

---

## Formal Arabic Writing Register (فصحى رسمية)

**Tashkeel** — selective, grammatically critical words only:
- Mark case endings where ambiguity exists: `طالبةً الرعايةَ الرسمية`
- Mark verb forms where misreading changes meaning: `يُثبَت`، `يُدرَّب`، `يُختتم`
- Never tashkeel entire paragraphs

**Punctuation**

| Element | Rule |
|---|---|
| Em-dash `—` | Parenthetical precision; enclose in spaces: `— لكن من بوابة الشباب الجامعي —` |
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
المصدر: CAPMAS، الربع الأول ٢٠٢٦؛ استطالع Nexford لأصحاب العمل في مصر، ٢٠٢٦.
```

**Register markers**:
- Cover: `مقدَّم إلى وزارة التضامن الاجتماعي · مقترح شراكة`
- Narrative arc: `من الاتكالية إلى الاستقلال الاقتصادي`
- Final slide closing: `نتطلع إلى شرف تعاونكم`

**Parallel structure** — list items must share identical grammatical pattern (same verb form, same noun case). Example from actual slides:
```
التحاق — تدريب — إثبات  (masdar pattern)
تُمكِّن وتموِّل وترعى  (مضارع، subject: الوزارة)
تُدرِّب عينيًا وتوظِّف  (مضارع، subject: الشركات)
تُشغِّل وتنتج وتقيِّم  (مضارع، subject: MBK)
```

---

## Ministry Alignment Framework

Every proposal must include explicit ministry alignment. Use checkmarks (✓) in the alignment slide.

| Strategy | Alignment claim |
|---|---|
| رؤية مصر ٢٠٣٠ | إسهام موثَّق في التنمية البشرية وتشغيل الشباب |
| الإطار المرجعي للتعليم العالي SCU 2025 | ربط المناهج بسوق العمل |
| قمة START 2026 وزارة التضامن | منصات التدريب المهني |
| برنامج «فرصة» | امتداد طبيعي — الوصول عبر وحدات التضامن بالجامعات |
| وحدات التضامن الجامعية | 73 جامعة / أكثر من ٣.٦ مليون طالب — قاعدة المستفيدين المباشرين |

Narrative arc: **الاتكالية → الاستقلال الاقتصادي**. Every phase shows measurable movement on this axis.

---

## Phases

### Phase 1 — Draft

1. Confirm: initiative title (Arabic), ministry, lead contact (name / email / phone), date.
2. Confirm: core problem in one sentence, proposed solution, specific ask.
3. Choose brand variant (Jahizoon navy / MERIDIAN black).
4. Build content slide-by-slide using the Jahizoon 9-slide schema or MERIDIAN 12-slide schema.
5. For each content slide output:

```markdown
## Slide N — [Role] ([Arabic section label])
**Label (gold tracked)**: ...
**Headline (Montserrat Bold white)**: ...
**Body**: ...  (≤ 60 Arabic words)
**Stat callout**: [figure] — [source]
**Source caption**: المصدر: ...
```

**Gate**: every stat has a source; no claim precedes its evidence; gold accent on exactly one element per content slide.

---

### Phase 2 — Review

Check each slide:

| Check | Pass condition |
|---|---|
| Color discipline | Gold appears once per slide maximum |
| Evidence order | Statistic precedes claim on every data slide |
| Tashkeel | Applied only to ambiguous critical words |
| Ministry alignment | Final slide has explicit ✓ list for ≥ 3 strategies |
| Pilot numbers | 41.5% / 6% / 78% / 45 — all sourced |
| Word count | No content slide exceeds 80 Arabic words |
| Register | Arabic comma `،`; em-dash parentheticals where needed |
| Co-branding | Ministry logo placeholder on cover and final slide |

Output:

```markdown
## Review: [Initiative Title]

| Slide | Issue | Fix |
|---|---|---|
| 03 | Claim precedes stat | Move CAPMAS citation before implication |
| 09 | Missing برنامج فرصة alignment | Add ✓ row |

✓ Pass: [list clean slides]
```

---

### Phase 3 — Finalize

1. Apply all review fixes.
2. Verify cover includes: initiative title, tagline, ministry name, "مقترح شراكة", date.
3. Verify final slide closes with: `نتطلع إلى شرف تعاونكم` + contact block.
4. Output final slide-by-slide document, production-ready.
5. Produce designer handoff note:

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
```

---

## Quick-Start

If the user says "draft a ministry proposal for [X]", run Phase 1 immediately. Default to Jahizoon (navy) brand unless the user specifies MY4 / MERIDIAN. Default ministry: وزارة التضامن الاجتماعي.

---

## Rules

- **Evidence before claim** — every statistic must appear before any conclusion drawn from it. No exceptions.
- **One gold accent per slide** — if two elements compete for gold, the more impactful one wins; the other becomes white.
- **فصحى رسمية** — no colloquial (`عامية`) constructions, English loan words, or informal abbreviations in Arabic body copy.
- **Source every stat** — if a number appears without a citation, flag it `[مصدر مطلوب]` and do not finalize.
- **Ministry alignment is not optional** — every proposal must include the ✓ table in the final slide.
- **برنامج فرصة is the entry point** — always frame جاهزون as a natural extension of the ministry's existing فرصة programme.
- **RTL layout** — all spatial references in designer notes are RTL: "top-left" = Arabic start side.
- **Co-brand the cover** — ministry logo placeholder must appear alongside MBK wordmark on cover and final slide.
