---
name: tdd
description: >
  Test-Driven Development skill. Enforces the Red-Green-Refactor cycle,
  AAA test structure, and FIRST principles. Use when the user is writing
  tests or implementing features and wants TDD discipline applied.
  Never mention "TDD" in code, comments, commits, or PRs — the process
  is invisible; only the code speaks.
auto-trigger:
  - writing tests or implementing features with test-first discipline
  - "test first"
  - "red green refactor"
  - "write a failing test"
  - any new function or module where correctness is critical
  - bug fix where a regression test should prevent recurrence
do-not-trigger:
  - exploratory / throwaway scripts
  - docs-only changes

health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []
---

# TDD

## Output style

Never explicitly mention TDD in code, comments, commits, PRs, or issues. Write natural, descriptive code. The development process is invisible; only the result is shown.

---

## The cycle: Red → Green → Refactor

### Red phase — one failing test

- Write ONE test that describes the desired behavior.
- The test must fail for the **right reason** — not a syntax error or missing import.
- One test at a time. No exceptions except:
  - Browser-level / expensive-setup tests (e.g., Storybook `*.stories.tsx`): group multiple assertions in one block only when adding to an existing interaction flow. New interactions still get new tests.
  - Initial test file setup or extracting shared test utilities.
- For DOM tests: use `data-testid` attributes, not CSS classes, tag names, or text content.
- No hard-coded timeouts (`sleep()`, `timeout: 5000`). Use `waitFor`, `findBy*`, or event-based sync; defer to global test config for timeout values.

### Green phase — minimal code

- Implement only what's needed to pass the current failing test.
- No anticipatory coding, no extra features, no extra methods.
- Address the specific failure message, nothing more.

### Refactor phase — improve, don't add

- Only when all relevant tests are green (run them first, show proof).
- Applies to both implementation and test code.
- Allowed: types, interfaces, constants replacing magic values, helpers, abstractions, clean-up.
- Not allowed: new behavior, new logic, new methods not covered by passing tests.

---

## Incremental development

Each step addresses ONE specific issue:

| Test failure | Correct response |
|---|---|
| "X is not defined" | Create empty stub/class only |
| "X is not a function" | Add method stub only |
| Assertion failure | Implement minimal logic only |

---

## Optional: Spike phase (exceptional only)

Before Red, a Spike may be used when it is impossible to define a meaningful failing test due to technical uncertainty.

- Goal: exploration and learning only.
- All spike code is **disposable** — never merge or reuse directly.
- Once the problem space is understood, discard everything and start from Red.

---

## Core violations to block

| Violation | Signal |
|---|---|
| Multiple test addition | >1 new test in a single step |
| Over-implementation | Code that goes beyond the current failing test's message |
| Premature implementation | Implementation added before a test exists and fails |
| Refactoring with failing tests | Refactor attempted without a green run |

---

## Test structure — AAA pattern

Every test:
- **Arrange**: Set up minimal test data and preconditions.
- **Act**: Execute the single action being tested.
- **Assert**: Verify the expected outcome with specific, behavior-focused assertions.

---

## Test quality — FIRST principles

| Principle | What to verify |
|---|---|
| **Fast** | No I/O, no network calls, no `sleep()`/`setTimeout` delays |
| **Independent** | No shared mutable state, no execution-order dependencies |
| **Repeatable** | No `Date.now()`, no unseeded `Math.random()`, no external service dependencies |
| **Self-validating** | Meaningful assertions — no manual verification needed |
| **Timely** | Test written before the code it validates |

---

## Anti-patterns to detect

| Anti-pattern | Detection signal |
|---|---|
| **The Liar** | `expect(true).toBe(true)`, empty bodies, zero assertions |
| **Excessive Setup** | >20 lines of arrange, >5 mocks, deep nested object construction |
| **The One** | >5 assertions testing unrelated behaviors in one test |
| **The Peeping Tom** | Testing private methods or internal state; tests that break on any refactor |
| **The Slow Poke** | Real DB/network calls, file I/O, hard-coded timeouts |

---

## Hints when stuck

- Test output shows "no tests run" on a new failing test → likely a missing import or constructor; create a simple stub first.
- Cannot write a meaningful failing test → consider a Spike, but validate that uncertainty is genuine before using it.
- Green phase feels like it needs more code → it doesn't; trust the next Red to drive the next increment.
