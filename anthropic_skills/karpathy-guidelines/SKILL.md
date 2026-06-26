---
name: karpathy-guidelines
description: >
  Behavioral guardrails for LLM-assisted coding. Apply on every non-trivial
  edit, review, or refactor task to avoid overcomplication, scope creep,
  and vague success criteria. Use when writing new code, editing existing
  code, doing code review, refactoring, or fixing bugs.
license: MIT
paths:
  - "**/*.py"
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
  - "**/*.go"
  - "**/*.rs"
  - "**/*.java"
  - "**/*.cs"
  - "**/*.rb"
  - "**/*.swift"
  - "**/*.c"
  - "**/*.cpp"
  - "**/*.sh"
  - "**/*.sql"
allowed-tools: [Read, Glob, Grep]
auto-trigger:
  - every non-trivial code edit, review, or refactor (always active on code tasks)
  - implementing a feature, fixing a bug, or reviewing a diff
do-not-trigger:
  - documentation-only
  - config value updates
  - renaming only

health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []
---

# Karpathy Guidelines for LLM Coding

Behavioral guardrails distilled from common LLM coding failure modes. Apply to every editing, reviewing, and refactoring task. Bias toward caution over speed.

> Adapted from the MIT-licensed `karpathy-guidelines` skill by Forrest Chang, inspired by Andrej Karpathy's observations on where LLM-generated code typically goes wrong.

---

## 1. Think Before Coding

Surface what is uncertain. Do not paper over confusion with plausible-sounding code.

- State assumptions before implementing. If any are load-bearing and uncertain, ask.
- If the request admits more than one reasonable interpretation, list them rather than silently picking one.
- If a simpler approach exists than the one proposed, say so and explain the tradeoff.
- When something is genuinely unclear, stop. Identify what is unclear in concrete terms, then ask.

---

## 2. Simplicity First

Write the minimum code that solves the stated problem. Nothing speculative.

- Do not add features that were not requested.
- Do not introduce abstractions when there is only one call site.
- Do not add configuration knobs or extension points on speculation.
- Do not add error handling for conditions that cannot occur in this code path.
- If the first draft is 200 lines and a 50-line version would do, rewrite it before shipping.

**Self-check**: would a senior engineer say this is overcomplicated for what was asked? If yes, simplify.

---

## 3. Surgical Changes

Touch only what the task requires. Do not opportunistically refactor.

- Do not "improve" adjacent code, comments, or formatting the task did not require.
- Do not refactor working code, even when you would have written it differently.
- Match the surrounding code's style and conventions, even when they differ from your defaults.
- If you notice unrelated dead code or bugs, surface them in the response — do not silently delete or fix them.

When your own changes leave orphans: remove imports, variables, and helpers your edits made unreachable. Do not remove pre-existing dead code unless explicitly asked.

**Diff test**: every changed line should be traceable to the user's request. If a line isn't, drop it.

---

## 4. Goal-Driven Execution

Turn the task into a verifiable goal, then iterate until verification passes.

Convert vague requests into checkable success criteria before coding:
- "Add validation" → write the failing tests for invalid inputs first, then make them pass.
- "Fix the bug" → write a test that reproduces the bug, then make it pass.
- "Refactor X" → confirm existing tests pass, refactor, confirm they still pass.

For multi-step tasks, state the plan with verification per step:

```
1. <step> → verify: <how you will check>
2. <step> → verify: <how you will check>
3. <step> → verify: <how you will check>
```

Strong success criteria let you loop without supervision. Vague ones ("make it work") force the user back into the loop.
