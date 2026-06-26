---
name: prove-claims
description: >
  Maps claims to evidence. Use when a change, release note, PR description,
  or document asserts something a reviewer must trust — and you need to
  show which evidence backs each claim. Catches overreaching claims
  (stated past their evidence) before they reach reviewers. Do not use
  to invent evidence that does not exist, or to treat green CI as proof
  of unrelated claims.
allowed-tools: [Read, Bash, Grep, Glob, Write]
argument-hint: "[claim source file or description]"
auto-trigger:
  - "substantiate this", "source this claim", "back this up with evidence"
  - single-claim verification needing sourced evidence
  - checking one specific assertion before using it
do-not-trigger:
  - multi-claim documents (use fact-checker)
  - creative writing

---

# Prove Claims

Evidence should answer named claims — not just create a vague sense that a change is fine. This skill turns each claim into a traceable proof.

---

## Claim types (keep these distinct)

| Type | Definition |
|---|---|
| Fact | Directly observable, verifiable by anyone |
| Assumption | Believed true but not checked |
| Unknown | Acknowledged gap — not yet investigated |
| Source claim | Something a cited source says |
| Local proof | Something you checked yourself (test, diff, log) |
| Decision authority | Who is entitled to decide (not evidence of correctness) |

---

## Process

1. **Extract claims** — pull every material assertion from the source (PR body, release note, doc section)
2. **Classify** — for each claim, identify which type(s) of support back it
3. **Choose verification type** — self-check / peer-check / concurrent verification / independent verification / test / eval
4. **Assign evidence status**: `pass` / `fail` / `gap` / `deferred` / `not applicable` / `planned`
5. **Trim overreaching claims** — narrow any claim until the evidence truly backs it
6. **Record gaps** — state how each gap affects the release or decision

---

## Output format

```markdown
## Claim-Evidence Map

| Claim | Support type | Verification | Evidence | Status | Notes |
|---|---|---|---|---|---|
| "Auth is secure" | local proof | test | `pytest tests/auth/` passes | pass | scope: unit only |
| "Zero regressions" | assumption | — | none | gap | CI doesn't cover e2e |
| "GDPR compliant" | source claim | peer-check | legal team review (see PR#123) | pass | |

## Gaps and release posture
- `gap`: "Zero regressions" — no e2e tests exist. Residual risk accepted by [owner].
- `fail` / unowned `gap` → escalate, do not ship.
```

---

## Rules

- **No claim reaches past its evidence** — if CI passed but the claim is about safety, say so explicitly
- **Green CI ≠ unrelated proof** — "tests pass" only proves what the tests check
- **Review counts as evidence only when its scope and result are written down**
- **`fail` or unowned `gap` → block** — do not carry into a release decision silently
- **Hidden gaps lead to worse decisions** — surface them, don't suppress them

---

## Common rationalizations to reject

- "CI passed, so all claims pass." — CI only proves what it checks.
- "A reviewer can read the code." — Review is evidence only when its scope and result are recorded.
- "The same agent checked itself." — Self-check, not independent verification.
- "We shouldn't mention gaps." — Hidden gaps produce worse release decisions.
