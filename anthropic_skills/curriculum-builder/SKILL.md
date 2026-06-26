---
name: curriculum-builder
description: >
  Designs university-level marketing/business curricula, generates assessments,
  and builds grading rubrics using Backward Design (Wiggins & McTighe) and
  Bloom's Taxonomy. Use when a user is a professor/instructor building a course,
  writing a syllabus, generating exams or quizzes, or marking student work.
  Trigger on: "design a course", "build a syllabus", "learning outcomes",
  "write an exam", "generate test questions", "create a rubric", "grade this",
  "mark this assignment", "curriculum". Archetype: Workflow Automation.
  Cross-references prd-generator for scoping and pdf/docx for deliverable output.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<course or topic> [--syllabus | --exam | --rubric | --mark]"
auto-trigger:
  - "design a course", "build a syllabus", "learning outcomes", "curriculum"
  - generating exam/quiz questions for a course
  - creating a grading rubric or marking student work
do-not-trigger:
  - K-12 lesson plans without higher-ed outcomes (adapt manually)
  - corporate training decks (use presentation-architect)
  - single factual question with no pedagogical framing
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Curriculum Builder

Designs courses, assessments, and rubrics that are internally aligned — outcomes drive assessment drive instruction. Built on Backward Design + Bloom's Taxonomy.

---

## Mode Selection

| Mode | Trigger | Output |
|---|---|---|
| `--syllabus` | "design a course", "build a syllabus" | Outcomes + assessment plan + schedule |
| `--exam` | "write an exam", "generate questions" | Items mapped to outcomes + Bloom levels |
| `--rubric` | "create a rubric" | One-page criterion × level grid |
| `--mark` | "grade this", "mark this work" | Scored result against a rubric + feedback |

---

## Backward Design — the spine of every course

Always design in this order. Never start from content.

```
1. DESIRED RESULTS   → what should students be able to DO by the end?
        ↓
2. ACCEPTABLE EVIDENCE → how will we know? (assessments, performance tasks)
        ↓
3. LEARNING PLAN     → instruction/activities that build toward the evidence
```

Content selection is the *last* step, not the first.

---

## Bloom's Taxonomy — write measurable outcomes

State every learning outcome with an action verb at the target cognitive level:

| Level | Verbs | Marketing/business example |
|---|---|---|
| **Remember** | define, list, recall | List the 4Ps of the marketing mix |
| **Understand** | explain, summarize, classify | Explain how positioning differs from segmentation |
| **Apply** | apply, calculate, demonstrate | Apply CLV formula to a SaaS scenario |
| **Analyze** | compare, differentiate, attribute | Analyze why a campaign underperformed |
| **Evaluate** | critique, justify, defend | Evaluate two go-to-market strategies and recommend one |
| **Create** | design, construct, formulate | Design a full brand pyramid for a startup |

**Rule**: a marketing/business course should weight toward Apply→Create. Avoid an exam that is 90% Remember.

Outcomes appear in: syllabus, assignment briefs, rubrics, and lesson intros — keep wording identical across all four.

---

## Syllabus Output (`--syllabus`)

```markdown
# [Course Title] — Syllabus

## Course Learning Outcomes
By the end, students will be able to:
1. [verb + content + Bloom level]
[3–6 outcomes, weighted toward higher order]

## Assessment Plan (evidence for each outcome)
| Outcome | Assessment | Type | Weight | Bloom level |

## Weekly Schedule
| Week | Topic | Outcome served | Activity | Prep |

## Grading Policy
[breakdown + rubric pointers]
```

---

## Exam Generation (`--exam`)

For each item:
1. Tag the **outcome** it measures and the **Bloom level**
2. Match item type to the cognitive target:
   - Remember/Understand → MCQ, short answer
   - Apply/Analyze → scenario/case problem
   - Evaluate/Create → essay, project brief
3. Build an **answer key** + per-item rationale

```markdown
## Exam — [Course], [Term]

| # | Question | Type | Outcome | Bloom | Points | Answer |
```

Balance: state the Bloom distribution (e.g., 20% recall / 50% apply-analyze / 30% evaluate-create) and check it matches the syllabus weighting.

---

## Rubric Design (`--rubric`)

Best practices baked in:
- **One page** — criteria as rows, performance levels as columns
- Consistent wording across levels; clear, concrete descriptors
- Each criterion ties to a learning outcome
- Pilot on sample work before live use

```markdown
## Rubric — [Assignment]

| Criterion (→ outcome) | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|---|---|---|---|---|
```

---

## Marking (`--mark`)

When grading student work against a rubric:
1. Score **one question/criterion across all students** before moving on — not one student fully at a time (consistency)
2. Keep responses **anonymous** and grade in **random order** (bias control)
3. Separate **mechanics** (grammar) from the **measured outcome** unless writing is the outcome
4. Give feedback tied to the rubric level, with one concrete improvement per criterion

```markdown
## Marked: [Student/ID] — [Assignment]
| Criterion | Level | Points | Feedback |
**Total**: X / Y
**Top priority improvement**: [one thing]
```

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Course needs a scoped "product" definition | `prd-generator` |
| Deliver syllabus/exam as a polished doc | `docx` / `pdf` |
| Slide deck for lectures | `presentation-architect` |
| Verify a cited statistic or study | `fact-checker` |

---

## Rules

- **Backward design always** — outcomes → evidence → instruction → content. Never content-first.
- **Every outcome has a Bloom verb** and is measurable.
- **Weight toward higher order** for marketing/business — Apply through Create.
- **Alignment is mandatory** — each assessment item and rubric criterion maps to an outcome.
- **Mark by criterion, anonymized, randomized** — consistency and bias control are not optional.
- **Identical outcome wording** across syllabus, briefs, rubrics, and lessons.
