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
auto-trigger:
  - Arabic ministry proposal or official document (وزارة)
  - MBK Education / Jahizoon / MERIDIAN brand content
  - Egyptian ministry-aligned programme narrative
  - proposal following the 15-slide Jahizoon schema
do-not-trigger:
  - generic Arabic writing
  - non-ministry English documents

---

# Ministry Proposal Skill

Produces proposals that match either MBK Education visual system and Egyptian governmental writing standards. Two brand variants; share the same Arabic register and strategy alignment rules.

## Primary References (canonical — use these, not generic templates)

| File | Role |
|---|---|
| `MBK_Education_Brand_Guidelines.pdf` + `.pptx` | MERIDIAN design system — colours, typography, woven mark, icon rules |
| `MBK_Jahizoon_MoSS_AR_v2.pdf` / `.pptx` | **QA reference** — every layout decision and Arabic copy pattern is benchmarked against this file |
| `MBK_Education_Field_Ready_Ministry.pptx` | English-language parallel (same initiative, different audience) |
| `Generic_Issue.pptx` | Full 15-slide expanded version — authoritative slide schema |

**The MBK_Jahizoon_MoSS_AR_v2 PDF is the QA grid baseline.** When reviewing output, compare slide-by-slide against it: gold placement, stat card layout, 3-party footer, co-branding positions, Arabic phrasing. Any deviation from that reference requires explicit justification.

> All content produced by this skill must pass `anthropic_skills/fact-checker` before finalizing. Every statistic needs 3 independent sources.

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

04  المشكلة والفرصة — الشهادة وحدها لا تصنع فرصة عمل
    — Research consensus callout: "إجماع بحثي مصري: 13 دراسة، 100% تؤكد
       وجود فجوة مهارات لدى الخريجين — في المهارات السلوكية والإدارية والتطبيقية"
      (Source: Consensus.app meta-analysis, N=13 Egyptian studies)
    — Bar chart: 41.5% (خريجو الجامعات) vs 6% (إجمالي القوى العاملة)
    — 3 employer stat cards: 78% / 41% / 51%
    — Source caption: CAPMAS الربع الأول ٢٠٢٦؛ استطلاع Nexford، ٢٠٢٦

05  لماذا ينجح هذا النموذج — السبب معروف في مصر والحل هو نموذجنا
    — 3 cause → solution pairs (root-cause mapping):
      السبب: مناهج غير محدَّثة وبعيدة عن احتياجات سوق العمل
      ↓ ماذا يفعل «جاهزون»: منهج مبني على مهام واقعية داخل الشركة، يُصمَّم مع أصحاب العمل
      السبب: ضعف التنسيق بين الجامعة وأصحاب العمل
      ↓ ماذا يفعل «جاهزون»: شراكة تشغيل مباشرة مع شركات مضيفة طوال فترة التدريب
      السبب: غياب التدريب العملي والإرشاد المهني
      ↓ ماذا يفعل «جاهزون»: شهر تدريب ميداني تحت إشراف + امتحان مُصوَّر

06  الحل · كيف يعمل — تدريب حقيقي، يُثبَت بالكاميرا
    — 7 skills being built (listed as tags):
      التواصل · حل المشكلات · التخطيط · إدارة الوقت
      إدارة المشروعات · العمل الجماعي · التفكير النقدي
    — 3-step cards: 01 التحاق / 02 تدريب / 03 إثبات
    — 3-party footer: الوزارة (تُمكِّن وتموِّل وترعى) /
                      الشركات المضيفة (تُدرِّب عينيًا وتوظِّف) /
                      MBK (تُشغِّل وتنتج وتقيِّم)

07  الامتحان المُصوَّر — قلب المبادرة
    — Concept framing:
      "ليس امتحانًا ورقيًا. الشاب يؤدّي مهامًا حقيقية أمام لجنة وكاميرا —
       فيتحوّل التدريب إلى دليل، والدليل إلى قصة."
    — As assessment: إثبات لا يُجامَل — أداء فعلي / تقييم من خبراء / شهادة يثق بها صاحب العمل
    — As media: حلقة ختامية مُصوَّرة تُبثّ تلفزيونيًا / رحلة تحوّل الشاب / يجذب الرعاة
    — Photo placeholder (pilot exam footage)

08  النتائج المباشرة · المرحلة التجريبية
    — 4 stat boxes: 1 جامعة / 3 كليات / 2 شركتان مضيفتان / 45 شابًا في الدورة
    — Faculty cards with icons:
      إدارة الأعمال — الوظائف التجارية والتشغيلية
      سلاسل الإمداد — المخازن واللوجستيات والمشتريات
      التسويق — الحملات والمحتوى والمبيعات
    — "شهر واحد من التدريب المنظَّم، يُختتم بامتحان عملي مُصوَّر وأول دفعة قابلة للقياس"

09  الجدول الزمني للمرحلة التجريبية
    — 8-week pilot cycle (horizontal timeline):
      أسبوع ٠   التحضير والشراكات: توقيع الاتفاقات، اختيار الكليات والشركات
      أسبوع ١–٢ الالتحاق والتأهيل: انضمام الشباب للشركات، بدء التهيئة المهنية
      أسبوع ٣–٥ التدريب الميداني: مهام واقعية داخل الشركة تحت إشراف ومتابعة
      أسبوع ٦   الامتحان المُصوَّر: أداء فعلي أمام لجنة وكاميرا — قلب المبادرة
      أسبوع ٧–٨ التقييم والنشر: منح الشهادات، قياس النتائج، بثّ الحلقة الختامية

10  خطة المراحل — من 45 شابًا إلى برنامج وطني
    — Growth chart: 45 (تجريبية) → ~500 (توسّع) → +3,000 (وطنية)
    — 3 timeline cards:
      قصير المدى  0–6m:   1 جامعة · 3 كليات · شركتان · 45 شابًا / النتيجة: نموذج مُثبت وقابل للتكرار
      متوسط المدى 6–18m:  4 جامعات · حتى 10 شركات · ~500 شاب / النتيجة: بيانات توظيف مقاسة + سلسلة محتوى
      طويل المدى  18–36m: 15+ جامعة · 12+ محافظة · 3,000+ سنويًا / النتيجة: برنامج وطني مدمج مع منظومة الوزارة
    — Source footnote: ~3.6 مليون طالب في التعليم العالي و73 جامعة

11  مؤشرات الأداء والأثر — أرقام نلتزم بها ونقيسها
    — 6-card KPI grid:
      ≥ 60%   نسبة الجاهزية للتوظيف خلال 6 أشهر (مقابل 41.5% بطالة اليوم)
      ≥ 40%   تحويل التدريب إلى عرض عمل فعلي (عبر شبكة الشركات المضيفة)
      ≥ 90%   إتمام الشهادة المهارية (لكل مشارك في الدورة)
      3,000+  شاب يُدرَّب سنويًا عند التوسّع (بنهاية المرحلة الثالثة)
      ≥ 85%   رضا جهات التشغيل عن الكوادر (قياس بعد كل دورة)
      12+     محافظة يصلها البرنامج وطنيًا (تغطية جغرافية متدرجة)
    — Source: CAPMAS + Nexford + مراجعات دولية للتعلّم المبني على العمل

12  الفريق والموارد — من يُنفّذ، وبأي موارد
    — 3-layer resource structure:
      الموارد البشرية: فريق MBK يصمّم المنهج، يدير التقييم، وينتج التغطية الإعلامية داخليًا
      الشركاء: الشركات المضيفة والكليات — بيئة عمل حقيقية ومُرشدون، تربط التدريب باحتياج التوظيف
      من الوزارة: رعاية ووصول وتمويل تشغيلي — الرعاية الرسمية + جامعة شريكة + تمويل المرحلة التجريبية

13  الخطة الإعلامية — من امتحان مُصوَّر إلى قصة وطنية
    — 3 media phases:
      ٠١ إنتاج: حلقات وقصص نجاح — توثيق رحلة كل دفعة من متدرّب إلى جاهز
      ٠٢ بثّ: تلفزيون + منصات تواصل + منصة «ستارت» الرقمية
      ٠٣ أثر: وعي عام → يجذب رعاة جُددًا → يموّل التوسّع
    — Cadence note: "حلقة ختامية مُصوَّرة مع كل دورة — محتوى متجدّد يرافق نمو البرنامج"

14  الاتجاه قائم بالفعل — الوزارة تتحرك في هذا الاتجاه ونحن نُكمله
    — Framing: "«جاهزون» يضيف الطبقة الناقصة: التدريب الميداني داخل الشركات والإثبات العملي المُصوَّر"
    — 3 existing ministry programmes:
      ١ برنامج «فرصة» — الانتقال من الاتكالية إلى الاستقلال الاقتصادي للشباب والنساء وذوي الإعاقة
      ٢ وحدات التضامن الاجتماعي بالجامعات — تأهيل الطلاب مهنيًا وعمليًا ودمجهم بسوق العمل
      ٣ قمة «ستارت 2026» ومنصتها الرقمية — منصة تعمل على مدار العام للتدريب والتأهيل وربط الفرص

15  التوافق مع الوزارة · الطلب — امتداد طبيعي لمنظومة الوزارة
    — Gold italic tagline: «جاهزون» يخدم هدف الوزارة المعلن: الانتقال من الاتكالية إلى الاستقلال
       الاقتصادي — من بوابة الشباب الجامعي
    — 3 alignment bullets with checkmarks:
      تمكين اقتصادي قابل للقياس
      متوافق مع رؤية مصر 2030
      يندمج مع «ستارت» ووحدات التضامن — يبني على منظومة قائمة، ولا يبدأ من الصفر
    — Ask box: "رعاية الوزارة وتمويلها للمرحلة التجريبية، والوصول إلى جامعة شريكة بثلاث كليات،
       عبر وحدات التضامن بالجامعات"
    — Co-branding footer (mirrors cover)
```

---

## Confirmed Statistics Reference

All figures for جاهزون proposals. Source every stat exactly as shown — do not paraphrase.

| Stat | Figure | Arabic source label |
|---|---|---|
| Graduate unemployment | **41.5%** | CAPMAS، الربع الأول ٢٠٢٦ |
| Overall labour force unemployment | **6%** | CAPMAS، الربع الأول ٢٠٢٦ |
| Employers can't find required skills | **78%** | استطلاع Nexford لأصحاب العمل في مصر، ٢٠٢٦ |
| Employers who call it a major hiring challenge | **41%** | استطلاع Nexford، ٢٠٢٦ |
| Employers willing to fund training | **51%** | استطلاع Nexford، ٢٠٢٦ |
| Employers offering jobs to interns post-training | **8 من 10** | مراجعات دولية للتعلّم المبني على العمل |
| Trainees with required behavioural skills | **63%** | مراجعات دولية |
| Egyptian studies confirming skills mismatch | **13 من 13 (100%)** | Consensus.app meta-analysis, N=13 |
| Students in higher education (current) | **~3.6M** | المجلس الأعلى للجامعات / التعليم العالي |
| Universities nationwide | **73** | المجلس الأعلى للجامعات |
| Pilot cohort size | **45 شابًا** | MBK Education تجربة AAST |

## Academic Evidence Layer

The Consensus.app meta-analysis (N=13 Egyptian studies) provides peer-reviewed backing for the problem slide. Key findings for use in proposals or research notes:

- **Consensus**: 100% of 13 Egyptian studies confirm graduate skills mismatch (Ahmed 2020; Nassef 2016; Abdou & Mostafa 2017; Ghimire et al. 2022; Ahmed 2026)
- **Root causes** (from peer review): outdated curricula / weak university-employer coordination / limited practical exposure
- **Sectors documented**: Agriculture, Communication, Hospitality, Architecture, Computer Engineering
- **Most cited missing skills**: leadership, planning, communication, problem-solving, time management, project management, critical thinking, teamwork
- **Key citations for proposal footnotes**:
  - Ghimire et al., 2022 — employer ratings vs. student self-ratings gap (Agriculture)
  - Nassef, 2016 — system-level barriers in Egyptian HE (Computer Engineering)
  - Ahmed, 2026 — SSRN: "Employment Gap in Egypt: Hidden Causes and Necessary Solutions"
  - Bassyouny, 2024 — stagnant programs, communication sector

When asked to add academic depth to a proposal, cite these as: `(Ghimire et al., 2022; Ahmed, 2020; Nassef, 2016)` in footnotes — do not embed full citations in body text.

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
