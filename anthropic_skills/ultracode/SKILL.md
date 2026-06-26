---
name: ultracode
description: >
  Maximum-quality coding mode. Stacks think-twice → SPARC → TDD → Karpathy
  guardrails → security review → change-impact → code-review into one unified
  pipeline. Apply automatically on any non-trivial feature, refactor, or bug fix
  where correctness and long-term maintainability matter. Trigger phrases:
  "ultracode", "maximum quality", "do this right", "production-ready", "no shortcuts".
  Also trigger proactively on: security-sensitive code, public API changes, schema
  migrations, shared module refactors, and performance-critical paths — even if the
  user doesn't ask for ultracode by name.
auto-trigger:
  - new feature implementation (more than ~20 lines of net-new logic)
  - architectural change or module restructuring
  - refactor of existing working code
  - bug fix in production or shared code
  - any task the user marks as important, critical, or production-bound
  - API design or public interface change
  - security-sensitive code paths
  - database migrations or schema changes
  - performance-critical code
  - integrating a new dependency or external service
do-not-trigger:
  - documentation-only changes
  - config value updates (env vars, JSON settings)
  - renaming a variable or file only
  - adding a log line
  - one-off scripts with no production impact
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob]
argument-hint: "<task-description> [--phase think|spec|build|review|ship]"
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Ultracode

Five-phase pipeline from raw request to production-ready code. Each phase gates the next. Apply to any task where correctness and maintainability matter.

---

## Pick Your Mode First

| Mode | When | Phases |
|---|---|---|
| **Full** | New feature, refactor, public API change, security-sensitive, schema migration | 0 → 1 → 2 → 3 → 4 |
| **Quick** | <20 line change, isolated bug fix, no shared dependencies touched | 0 → build → 3 → 4 (skip Phase 1) |
| **Hotfix** | Production incident, rollback-safe patch only | 0 → minimal change → 3 → 4 |

Never skip Phase 0 (Think) or Phase 3 (Review) regardless of mode.

---

## Phase 0 — Think (always first)

Before writing a single line, surface uncertainty. Read `lazy-cat/think-twice`.

- Restate the request in concrete, checkable terms.
- Identify the 2–3 simplest possible implementations.
- Pick the simplest one that fully satisfies the requirement — nothing more.
- State load-bearing assumptions. If any are uncertain, ask before proceeding.
- If a 10-line solution exists alongside a 100-line one, the 10-line one wins.
- **Security flag**: does this task touch auth, input handling, crypto, secrets, external API calls, or data at rest? If yes, `trailofbits/sharp-edges` runs in Phase 3.
- **Impact flag**: does this task touch a shared module, public API, or database schema? If yes, `change-impact` runs before Phase 4.

**Gate**: proceed only when success criteria are checkable and flags are noted.

---

## Phase 1 — Specify (SPARC Phase 1)

Read `sparc` → Phase 1 (Specification). Skip in Quick-mode.

- Requirements, acceptance criteria, edge cases, constraints.
- Write failing tests that encode the acceptance criteria (TDD Red phase).
- No implementation yet.
- For public APIs: document the interface contract explicitly (inputs, outputs, errors, side-effects).
- For schema migrations: document rollback plan and backward-compatibility window.

**Gate**: failing tests exist that will pass exactly when the spec is met.

---

## Phase 2 — Build (TDD Green + Karpathy)

Read `tdd` → Red → Green. Apply `karpathy-guidelines` throughout.

- Implement the minimum code to make the failing tests pass.
- Surgical changes only — touch nothing outside the task scope.
- No speculative abstractions, no extra config knobs, no future-proofing.
- After Green: Refactor phase — clean without changing behaviour; tests stay green.
- **New dependency added?** Verify it against actual docs/source before calling it. Never invent an API.

**Gate**: all tests pass; diff contains no line untraceable to the requirement.

---

## Phase 3 — Review (SPARC Phase 4 + code-review + security)

Read `sparc` → Phase 4 (Refinement).

### Core checklist

- [ ] Every changed line is traceable to the stated requirement
- [ ] No dead imports, unused variables, or orphaned helpers introduced
- [ ] Error handling exists only for conditions that can actually occur
- [ ] Test coverage ≥ 80% on new/changed code paths
- [ ] Performance: no O(n²) where O(n) suffices; no N+1 queries
- [ ] No `TODO` left uncommitted unless filed as a tracked issue

### Security checklist (run when security flag was set in Phase 0)

Invoke `trailofbits/sharp-edges` on the API/interface surface touched. Check:

- [ ] No secrets, tokens, or credentials embedded in code
- [ ] User input sanitised at all entry points
- [ ] SQL/command/template injection impossible by construction
- [ ] Auth checks present on every path that touches sensitive data
- [ ] Crypto: no homebrew algorithms; primitives are from well-known libraries
- [ ] Defaults are secure (timeouts set, verify=True, least-privilege)
- [ ] Algorithm/mode selection not delegated to the caller without validation

### Footgun check (always, even without security flag)

Does the changed interface invite misuse? If a developer could easily call this wrong and produce a silent failure or security issue, fix the design — not just the docs.

Fix all findings before proceeding to Phase 4.

**Gate**: all checklists clean; security findings resolved or explicitly deferred with justification.

---

## Phase 4 — Ship (SPARC Phase 5)

Read `sparc` → Phase 5 (Completion).

### Pre-ship: change impact (run when impact flag was set in Phase 0)

Invoke `change-impact` before committing. If any unexpected ripple is found, go back to Phase 3.

### Commit and PR

- Commit message: imperative mood, explains WHY not WHAT.
- PR description: what changed, why, how to test, which acceptance criteria it satisfies.
- No `TODO` left uncommitted unless tracked.
- Run the full test suite; confirm green.
- Use `yeet` for the commit + push + PR flow if available.

### CI gate

If CI fails after push: invoke `gh-fix-ci`. Do not mark the task complete until CI is green.

---

## Guardrails (always active)

| Rule | Detail |
|---|---|
| Simplicity | Minimum code that solves the stated problem |
| Surgical | Touch only what the task requires |
| No speculation | No features, abstractions, or error cases not in the requirement |
| Verify | Every claim about behaviour is backed by a passing test or observable output |
| No fabrication | Never invent a library, API, or behaviour not confirmed by docs or source |
| Security | Validate at boundaries; never embed secrets; sanitise user input |
| Honesty | If uncertain, say so — do not produce confident-sounding wrong code |
| Footgun-free | Interfaces must resist misuse — secure usage is the path of least resistance |

---

## Quick-mode (for genuinely small tasks)

For changes under ~20 lines where SPARC overhead is disproportionate:
1. Phase 0 (Think) — required, always
2. Write the change with TDD Red → Green
3. Phase 3 (Review + security checklist if flagged) — required, always
4. Phase 4 (Ship)

Never skip Phase 0 or Phase 3, even in Quick-mode.

---

## Skill integrations

| Situation | Invoke |
|---|---|
| Security flag raised in Phase 0 | `trailofbits/sharp-edges` in Phase 3 |
| Impact flag raised in Phase 0 | `change-impact` before Phase 4 |
| Static analysis needed | `trailofbits/semgrep` → `trailofbits/codeql` |
| CI fails after push | `gh-fix-ci` |
| PR has review comments | `gh-address-comments` |
| Commit + push + PR needed | `yeet` |
| ADR warranted (architecture decision) | `adr` during Phase 1 |
| TDD needs more depth | Read `tdd` skill fully |
