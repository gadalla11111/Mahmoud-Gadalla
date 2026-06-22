---
name: fact-checker
description: >
  Triple-source fact verification for every claim in a document, slide deck, or
  proposal. No claim — major or minor — is accepted on fewer than 3 independent
  sources. Returns a structured QA grid: claim × source-1 × source-2 × source-3 ×
  verdict. Use before finalizing any ministry proposal, research document, or
  published content. Trigger phrases: "fact check", "verify claims", "source this",
  "triple check", "QA grid".
allowed-tools: [Read, WebSearch, WebFetch, Grep, Glob]
argument-hint: "<document-path or inline text> [--strict] [--lang ar|en]"
---

# Fact Checker

Every claim gets three independent sources or it does not pass. No exceptions.

---

## What counts as a claim

Any statement that could be false if a source disappeared:

- Statistics and percentages (`41.5% of graduates are unemployed`)
- Named studies or institutions (`CAPMAS Q1 2026`)
- Dates and timelines (`قمة ستارت 2026`)
- Causal assertions (`work-based learning reduces unemployment`)
- Comparative claims (`7× more likely than the labour force average`)
- Programme descriptions (`برنامج فرصة targets economic independence`)
- Pilot results (`45 students, 1 university, 3 faculties`)

Opinions, rhetorical framing, and design instructions are **not** claims — skip them.

---

## The 3× Rule

| Source tier | Counts as independent? |
|---|---|
| Primary data (government statistics, official reports) | Yes |
| Peer-reviewed academic paper | Yes |
| Reputable news outlet with named reporter and date | Yes |
| Organisation's own published report (annual report, white paper) | Yes |
| Another slide or document from the same author | **No** |
| Paraphrase of a source already cited | **No** |
| "Common knowledge" or unattributed claim | **No** |

A claim passes only when **3 sources from different organisations** independently support it.

---

## Process

### Step 1 — Extract claims

Read the document. List every verifiable claim in order, numbered sequentially.

```
C-01: 41.5% of Egyptian university graduates are unemployed (Q1 2026)
C-02: Graduate unemployment is ~7× the national labour force average
C-03: 78% of Egyptian employers cannot find candidates with required skills
...
```

### Step 2 — Search for sources (3 per claim)

For each claim, run independent searches. Search strategy:

1. **Primary search**: look for the original data source cited in the document (e.g., CAPMAS bulletin)
2. **Secondary search**: look for a second organisation reporting the same figure
3. **Tertiary search**: look for a peer-reviewed paper or authoritative report corroborating the claim

Prefer sources in the same language as the claim. For Arabic-language proposals, accept Arabic and English sources.

### Step 3 — Score each claim

| Verdict | Condition |
|---|---|
| ✅ VERIFIED | 3 independent sources agree on the figure/fact |
| ⚠️ PARTIAL | 2 sources agree; third not found or slightly different |
| ❌ UNVERIFIED | Fewer than 2 confirming sources found |
| 🔄 CORRECTED | Sources found but figure differs — provide corrected value |
| ➖ NOT A CLAIM | Rhetorical / design / framing — skipped |

### Step 4 — Output the QA grid

```markdown
## Fact-Check QA Grid — [Document Title]
**Date checked**: [YYYY-MM-DD]
**Claims extracted**: N
**Verified**: N  **Partial**: N  **Unverified**: N  **Corrected**: N

| # | Claim | Source 1 | Source 2 | Source 3 | Verdict |
|---|---|---|---|---|---|
| C-01 | 41.5% graduate unemployment, Q1 2026 | CAPMAS Labour Force Survey Q1 2026 | World Bank Egypt data 2026 | Ahmed, M. (2026) SSRN:5887743 | ✅ VERIFIED |
| C-02 | ~7× labour force average | Derived: 41.5÷6 = 6.9× — CAPMAS Q1 2026 | ILO Egypt Country Brief 2026 | — | ⚠️ PARTIAL |
| C-03 | 78% employers can't find skills | Nexford Employer Survey Egypt 2026 | — | — | ❌ UNVERIFIED |
```

### Step 5 — Remediation list

For every ⚠️, ❌, or 🔄 row, produce a remediation action:

```markdown
## Remediation Required

**C-02 ⚠️ PARTIAL**
- Found 2 sources. Missing: independent third source for the 7× multiplier.
- Action: Replace "نحو سبع مرات" with "أكثر من ست مرات" (CAPMAS-derived) until a third source is found,
  OR add footnote: "نسبة مشتقة من بيانات CAPMAS، الربع الأول ٢٠٢٦."

**C-03 ❌ UNVERIFIED**
- Only the Nexford survey found. No independent corroboration.
- Action: Either remove the 78% figure, mark [مصدر مطلوب], or locate the original Nexford report
  and a second employer survey to cross-check.
```

---

## Reference: Verified Jahizoon Statistics

These have been pre-verified across multiple sources and may be used without re-checking:

| Claim | Verified figure | Sources (3) |
|---|---|---|
| Egyptian graduate unemployment rate | **41.5%** | CAPMAS Q1 2026 · World Bank Egypt · Ahmed 2026 (SSRN) |
| Overall labour force unemployment | **6%** | CAPMAS Q1 2026 · ILO Egypt · CAPMAS Annual 2025 |
| Graduate unemployment multiple vs. workforce | **~7×** (41.5÷6 = 6.9) | Derived from CAPMAS figures — cite as "نحو سبع مرات" |
| Employers can't find required skills | **78%** | Nexford Egypt Survey 2026 — **needs 2nd source before publishing** |
| Employers calling it a major challenge | **41%** | Nexford Egypt Survey 2026 — **needs 2nd source** |
| Employers willing to fund training | **51%** | Nexford Egypt Survey 2026 — **needs 2nd source** |
| Employers offering jobs to interns post-training | **8 of 10** | WBL International Reviews · British Council · ILO WBL Report |
| Trainees with required behavioural skills | **63%** | WBL International Reviews · García-Álvarez et al. 2022 · Succi & Canovi 2020 |
| Egyptian studies confirming skills mismatch | **13/13 (100%)** | Consensus.app N=13 · Ghimire et al. 2022 · Ahmed 2020 · Nassef 2016 |
| Students in higher education (Egypt) | **~3.6M** | SCU / Ministry of Higher Education · CAPMAS · World Bank |
| Universities nationwide (Egypt) | **73** | SCU official list · Ministry of Higher Education · UNESCO Egypt profile |

**Note on Nexford figures (78% / 41% / 51%)**: Currently single-sourced. Before using in a final published proposal, locate the full Nexford report URL and one independent employer survey (e.g., ManpowerGroup Egypt, AmCham Egypt employer survey) to reach 3× verification.

---

## Strict Mode (`--strict`)

When `--strict` is passed:
- ⚠️ PARTIAL claims are treated as failures (same remediation requirement as ❌)
- Every source must include a URL or DOI — no "general knowledge" attributions
- Derived figures (like the 7× multiplier) must be shown as explicit calculations, not stated as facts

---

## Arabic-Language Mode (`--lang ar`)

When checking Arabic proposals:
- Arabic-language government sources (CAPMAS Arabic bulletins) count as independent from their English equivalents
- Arabic academic journals count as independent sources
- Ministry official statements in Arabic count if dated and attributed to a named official

---

## Rules

- **3 sources or it doesn't ship** — a claim with 2 sources is ⚠️, not ✅. Do not present partial as verified.
- **No circular sourcing** — if Source B cites Source A, they are not independent.
- **Corrected figures take precedence** — if sources give a different number than the document, the document is wrong. State the correct figure explicitly.
- **Flag single-source stats visibly** — if a stat only has one source (like the Nexford figures), mark it in the QA grid and in the remediation list. Never silently pass it.
- **Date your check** — sources age. A verified figure from 2024 may be outdated by 2026 data. Always record the check date and the source date.
- **Do not fabricate sources** — if a third source cannot be found, the verdict is ⚠️ or ❌. Never invent a citation to reach 3×.
