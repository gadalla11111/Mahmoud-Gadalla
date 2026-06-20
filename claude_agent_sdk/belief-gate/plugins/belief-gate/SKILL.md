---
name: belief-gate
description: >
  Verify context completeness by execution, not judgment. Use this skill when a task
  requires all items from an enumerable set (quarters, IDs, invoice keys, named columns)
  before computing an answer. The gate runs deterministic set-difference — it never
  false-completes. Invoke when you see "sum over all X", "aggregate Y for periods Z",
  or any task where a missing item would silently corrupt the result.
allowed-tools:
  - Bash
  - Read
  - Write
---

# belief-gate skill

When a task requires complete data from a known set, verify before computing.

## The pattern

```python
from beliefgate import check_set

required = <derive from task — ids, quarters, keys>
present  = <parse from structured source — never ask the model>

res = check_set(required=required, present=present)
if res.ok:
    answer = compute(...)
else:
    print(f"Cannot compute: missing {res.missing}. Fetch and retry.")
```

## Rules
- `required` comes from the task (the question, the spec). Never from the data.
- `present` comes from a parser, DB query, or API. Never from an LLM reading prose.
- On INCOMPLETE: report `res.missing` exactly. Never fill gaps with estimates.
- On UNDECIDABLE: do not proceed. Ask the user how to resolve coverage.

## When to use this skill
- Multi-period aggregation ("sum revenue for Q1–Q4 2023")
- ID-range completeness ("did I get all accounts 200–250?")
- Before any write, payment, or irreversible action that depends on complete data

## When NOT to use it
- Open QA where relevance isn't enumerable
- Tasks so small that completeness is obvious
- Semantic / subjective properties (tone, intent, meaning)
