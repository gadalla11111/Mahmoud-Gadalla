---
name: profile-dataset
description: >
  Profiles a new table or file — shape, nulls, distributions, data-quality flags,
  and follow-up analyses worth running. Use when a user points at a dataset
  (CSV/Parquet/SQL table/DataFrame) and wants to understand it before analysis.
  Resolves the source, classifies every column, pulls counts/distincts/null rates/
  distributions, flags placeholders/skew/duplicates/stale data, surfaces keys and
  correlations, and recommends 3–5 specific next explorations. Trigger on:
  "profile this dataset", "explore this data", "summarize data quality", "describe
  dataset shape", "find patterns in data". Archetype: Judgment Amplifier.
allowed-tools: [Bash, Read, Write, Glob, Grep]
argument-hint: "<path or table name>"
auto-trigger:
  - profile or explore a new dataset, table, or file
  - summarize data quality or describe dataset shape
  - understanding columns, nulls, distributions before analysis
  - "find patterns in data"
do-not-trigger:
  - building a financial model (use creating-financial-models)
  - a specific known query with no profiling need
  - HR/people analytics specifically (use people-analytics)
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Profile Dataset

Profiles an unfamiliar table or file so you know its shape, quality, and the
analyses worth running next — before you commit to a direction.

---

## Process

### 1. Resolve & classify
- Resolve the source (CSV, Parquet, SQL table, DataFrame). Note row count, column count, size.
- Classify every column: identifier · categorical · numeric · datetime · boolean · free-text.

### 2. Per-column stats
For each column pull: count, distinct count, null rate, and a value distribution
(top values for categoricals; min/median/max/quartiles for numerics; range for dates).

### 3. Quality flags
- **Placeholders**: "N/A", "unknown", "0000", empty strings masquerading as values
- **Skew**: one value dominating a categorical; long-tailed numerics
- **Duplicates**: duplicate rows; duplicate keys on the candidate grain
- **Stale data**: max date far in the past; no recent rows

### 4. Structure
- Identify the **grain** (the column(s) that make a row unique)
- Surface likely **foreign keys**, hierarchies, and **correlated columns**

### 5. Recommend next steps
End with **3–5 specific** follow-up explorations grounded in what you found —
not generic advice ("look at the data") but pointed ("phone is 22.6% null — check
whether nulls cluster in a region or signup channel").

---

## Output Format

```markdown
# Profile — [dataset] · [N rows] · [M cols]

## Shape
rows: N · cols: M · grain: [key] · missing overall: X% · dup keys: N · numeric cols: K

## Columns
| Column | Type | Null % | Distinct | Note |
|---|---|---|---|---|
[one row per column, sorted by null % desc]

## Quality Flags
- [placeholder / skew / duplicate / stale findings, each with the column + number]

## Structure
- Grain: [key]
- Likely FKs / hierarchies: ...
- Correlated columns: ...

## Recommended Explorations (3–5)
1. [specific, grounded in a finding above]
```

---

## Tooling

Prefer whatever the environment has: `duckdb` (`summarize(read_parquet(...))`),
pandas (`df.describe(include='all')`, `df.isna().mean()`), or SQL `GROUP BY`
profiling. State which engine and query you used so the profile is reproducible.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| It's HR/workforce data | `people-analytics` |
| Financial-statement data | `analyzing-financial-statements` |
| Turn the profile into a deck | `presentation-architect` |
| Turn key numbers into one image | `infographic-maker` |

---

## Rules

- **Classify before counting** — type drives which stats matter.
- **Flag, don't fix** — surface quality issues; don't silently clean.
- **State the grain** — a profile without the unique key is incomplete.
- **Recommend specifics** — every follow-up ties to a finding, never generic.
- **Reproducible** — name the engine and the query used.
