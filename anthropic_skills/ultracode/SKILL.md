---
name: ultracode
description: >
  Maximum-quality coding mode. Stacks think-twice → SPARC → TDD → Karpathy
  guardrails → code-review → debug into one unified pipeline. Apply automatically
  on any non-trivial feature, refactor, or bug fix where correctness and
  long-term maintainability matter. Trigger phrases: "ultracode", "maximum
  quality", "do this right", "production-ready", "no shortcuts".
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob]
argument-hint: "<task-description> [--phase think|spec|build|review|ship]"
---

# Ultracode

Five-phase pipeline from raw request to production-ready code. Each phase gates
the next. Apply to any task where correctness and maintainability matter.

---

## Phase 0 — Think (always first)

Before writing a single line, surface uncertainty. Read `lazy-cat/think-twice`.

- Restate the request in concrete, checkable terms.
- Identify the 2-3 simplest possible implementations.
- Pick the simplest one that fully satisfies the requirement — nothing more.
- State load-bearing assumptions. If any are uncertain, ask before proceeding.
- If a 10-line solution exists alongside a 100-line one, the 10-line one wins.

**Gate**: proceed only when success criteria are checkable.

---

## Phase 1 — Specify (SPARC Phase 1)

Read `sparc` → Phase 1 (Specification).

- Requirements, acceptance criteria, edge cases, constraints.
- Write failing tests that encode the acceptance criteria (TDD Red phase).
- No implementation yet.

**Gate**: failing tests exist that will pass exactly when the spec is met.

---

## Phase 2 — Build (TDD Green + Karpathy)

Read `tdd` → Red → Green. Apply `karpathy-guidelines` throughout.

- Implement the minimum code to make the failing tests pass.
- Surgical changes only — touch nothing outside the task scope.
- No speculative abstractions, no extra config knobs, no future-proofing.
- After Green: Refactor phase — clean without changing behaviour; tests stay green.

**Gate**: all tests pass; diff contains no line untraceable to the requirement.

---

## Phase 3 — Review (SPARC Phase 4 + code-review)

Read `sparc` → Phase 4 (Refinement).

Self-review checklist before shipping:
- [ ] Every changed line is traceable to the stated requirement
- [ ] No dead imports, unused variables, or orphaned helpers introduced
- [ ] Error handling exists only for conditions that can actually occur
- [ ] Test coverage ≥ 80% on new/changed code paths
- [ ] No security regressions (injection, XSS, secrets in code)
- [ ] Performance: no O(n²) where O(n) suffices; no N+1 queries

Fix all findings before proceeding.

**Gate**: checklist is clean.

---

## Phase 4 — Ship (SPARC Phase 5)

Read `sparc` → Phase 5 (Completion).

- Commit message: imperative mood, explains WHY not WHAT.
- PR description: what changed, why, how to test.
- No `TODO` left uncommitted unless filed as an issue.
- Run the full test suite; confirm green.

---

## Guardrails (always active)

These apply across all phases regardless of which phase is currently active:

| Rule | Detail |
|---|---|
| Simplicity | Minimum code that solves the stated problem |
| Surgical | Touch only what the task requires |
| No speculation | No features, abstractions, or error cases not in the requirement |
| Verify | Every claim about behaviour is backed by a passing test or observable output |
| No fabrication | Never invent a library, API, or behaviour not confirmed by docs or source |
| Security | Validate at boundaries; never embed secrets; sanitise user input |
| Honesty | If uncertain, say so — do not produce confident-sounding wrong code |

---

## Quick-mode (for genuinely small tasks)

For changes under ~20 lines where SPARC overhead is disproportionate:
1. Think (Phase 0) — required, always
2. Write the change with TDD Red → Green
3. Self-review checklist (Phase 3) — required, always
4. Ship

Never skip Phase 0 or Phase 3, even on trivial tasks.
