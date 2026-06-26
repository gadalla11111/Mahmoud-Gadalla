---
name: legal-practice
description: >
  Drafting and review support across legal practice areas — contracts, clauses,
  policies, demand letters, NDAs, and legal research summaries. Use when a user
  needs legal documents drafted, reviewed for risk, or explained. Trigger on:
  "draft a contract", "review this NDA", "redline this clause", "privacy policy",
  "terms of service", "legal risk in", "explain this clause". Archetype: Judgment
  Amplifier. NOT a substitute for a licensed attorney — flags where counsel is
  required. Cross-references fact-checker for citations and docx/pdf for delivery.
allowed-tools: [WebSearch, WebFetch, Read, Write, Edit]
argument-hint: "<document or clause> [--draft | --review | --explain]"
auto-trigger:
  - draft a contract or agreement
  - review this NDA or redline a clause
  - privacy policy or terms of service
  - "what's the legal risk in this"
  - explaining a contract clause in plain language
do-not-trigger:
  - final legal advice that requires a licensed attorney's sign-off
  - jurisdiction-specific litigation strategy
  - anything presented as a guaranteed legal outcome
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Legal Practice

Drafts, reviews, and explains legal documents — clause-precise, risk-flagged, plain-language. A drafting and review aid, **not** a licensed attorney.

---

## ⚠️ Mandatory Disclaimer (every output)

End every deliverable with:

> *This is drafting/review assistance, not legal advice. Have a licensed attorney in the relevant jurisdiction review before relying on it.*

Never assert a guaranteed legal outcome. When a question turns on jurisdiction-specific law or litigation strategy, say so and route to counsel.

---

## Mode Selection

| Mode | Trigger | Output |
|---|---|---|
| `--draft` | "draft a [contract/NDA/policy]" | Clean draft + assumptions + open items |
| `--review` | "review this", "redline" | Risk-flagged redline + issue list by severity |
| `--explain` | "what does this clause mean" | Plain-language explanation + what to watch |

---

## Practice Areas Covered

| Area | Typical documents |
|---|---|
| Commercial | MSAs, SOWs, NDAs, vendor/supplier agreements |
| Employment | offer letters, contractor agreements, IP assignment |
| Privacy & compliance | privacy policies, ToS, DPA, cookie notices (GDPR/CCPA) |
| Corporate | bylaws, board resolutions, cap-table side letters |
| IP | licensing, assignment, trademark/usage terms |
| Disputes (drafting only) | demand letters, cease-and-desist |

For anything outside drafting/review — court filings, regulatory submissions — flag for counsel.

---

## Review Output (`--review`)

Flag issues by severity, each tied to a clause:

```markdown
## Legal Review — [Document]

| # | Clause | Issue | Severity | Suggested fix |
|---|---|---|---|---|
| 1 | §4 Indemnification | Uncapped, one-sided | 🔴 High | Add mutual cap at fees paid |
| 2 | §7 Term | Auto-renews, no notice window | 🟠 Med | Add 30-day opt-out |

### Missing protections
- [ ] Limitation of liability
- [ ] Governing law / venue
- [ ] Confidentiality survival

### Requires attorney review
- [jurisdiction-specific items]
```

Severity: 🔴 High (material exposure) · 🟠 Med (unfavorable) · 🟡 Low (cleanup).

---

## Drafting Rules

- **Define terms once**, capitalize consistently, reference by defined term
- **Symmetry by default** — mutual obligations unless the brief says otherwise; flag one-sided terms
- **No blanks left silent** — every `[PLACEHOLDER]` listed in an "open items" section
- **Plain-language summary** atop every draft — what it does in 3 sentences
- **Cite live law where claimed** — verify statutes/regs via WebSearch + `fact-checker`; never assert a citation from memory

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Statute/regulation citations must be verified | `fact-checker` |
| Deliver as a formatted contract | `docx` / `pdf` |
| Brand-styled policy page | `applying-brand-guidelines` |
| Research a legal landscape deeply | `deep-research` |

---

## Rules

- **Not legal advice** — disclaimer on every output; route jurisdiction-specific calls to counsel.
- **Clause-precise** — reference sections, define terms once, no silent blanks.
- **Risk-flag by severity** — High/Med/Low, each tied to a clause.
- **Verify every legal citation** — no statutes/cases asserted from memory.
- **Symmetry unless told otherwise** — flag one-sided terms explicitly.
