# fact-checker

Verify every factual claim in a document against 3 independent sources. The 3× rule is structural — not optional.

## Trigger

`/fact-checker [--strict] [file or pasted text]`

Use whenever a document contains statistics, dates, causal assertions, named studies, or institutional claims before it is finalised or published.

## Primary Reference

For MY4 Education / MoSS proposals: benchmark all Jahizoon-related statistics against **MBK_Jahizoon_MoSS_AR_v2.pdf** first. Claims that appear there are pre-verified; claims that differ must be sourced independently.

## Protocol

### Step 1 — Extract claims

Scan the document and list every verifiable claim:
- Numeric statistics (%, counts, rankings)
- Date assertions ("launched in 2023", "since 2019")
- Causal assertions ("leads to", "reduces X by Y%")
- Named studies, reports, surveys, or institutions
- Attributions ("Ministry of X states…", "According to Y…")

Output as a numbered claim list. Nothing else in this step.

### Step 2 — Source each claim × 3

For each claim, find **3 sources from different organisations**.

Disqualified source combinations:
- Two documents by the same author or institution (circular)
- A press release citing a report that cites the same press release
- Aggregator sites that trace back to a single primary

Required source format per claim:
```
S1: [Organisation] — [Document/URL/DOI] — [Exact quote or figure]
S2: [Organisation] — [Document/URL/DOI] — [Exact quote or figure]
S3: [Organisation] — [Document/URL/DOI] — [Exact quote or figure]
```

### Step 3 — QA grid

Output a markdown table:

| # | Claim (verbatim) | S1 | S2 | S3 | Verdict |
|---|---|---|---|---|---|
| 1 | "78% of graduates…" | ✓ Nexford 2024 | ✓ WEF 2023 | ✓ ILO 2024 | ✅ |
| 2 | "45% youth unemployment" | ✓ CAPMAS 2024 | ✓ World Bank 2024 | ⚠ IMF est. | ⚠️ |
| 3 | "6.3M youth NEET" | ✓ ILO 2023 | ✗ not found | ✗ not found | ❌ |

**Verdict key:**
- ✅ Confirmed by 3 independent sources
- ⚠️ Confirmed by 2; third is estimated, older than 2 years, or same-family org
- ❌ Fewer than 2 independent sources found
- 🔄 Claim needs reframing — true but misleading as stated

### Step 4 — Remediation list

For every row that is not ✅, output a specific fix:

```
Claim 2 (⚠️): Replace IMF estimate with a third survey-based source.
  → Try: OECD Employment Outlook 2024, or Egypt CAPMAS Labour Force Survey Q4 2024.

Claim 3 (❌): Remove or restate as "estimated X million" with source.
  → Current phrasing implies precision not supported by available data.
```

## --strict mode

Activate with `--strict`:
- ⚠️ is treated as ❌ (failure)
- Every source must include a URL or DOI — "widely reported" is not a source
- Any claim older than 3 years requires a note flagging potential staleness

## Pre-verified Jahizoon stats (MY4 / MoSS context)

The following figures appear in MBK_Jahizoon_MoSS_AR_v2.pdf and are baseline-verified. They still require independent corroboration before shipping in a ministry document.

| Stat | Figure | Status | Notes |
|---|---|---|---|
| Youth unemployment rate (Egypt) | ~30% | ✅ multi-source | CAPMAS + World Bank + ILO all aligned |
| Youth NEET population | 6–7M range | ✅ multi-source | ILO + CAPMAS convergent |
| Graduate employment gap (skills mismatch) | ~45% | ⚠️ needs 3rd source | CAPMAS + employer surveys; academic source needed |
| Nexford graduate employment rate | 78% | ⚠️ single-sourced | Nexford internal report only — needs independent survey |
| Nexford salary increase post-completion | 41% | ⚠️ single-sourced | Same Nexford report — flag explicitly in deck |
| Nexford promotion rate | 51% | ⚠️ single-sourced | Same Nexford report — flag explicitly in deck |
| AAST pilot completion rate | internal | 🔄 restate | Use "pilot cohort data" not a standalone stat |

**Action before finalising the MoSS proposal:** The three Nexford figures (78% / 41% / 51%) are currently single-sourced. Obtain one independent employer survey or labour market study that corroborates graduate outcomes at comparable online programmes before these ship in a ministry-facing document.

## Output contract

Always produce all four steps in order. Do not skip the QA grid even if most claims pass. The grid is the deliverable — the prose around it is secondary.
