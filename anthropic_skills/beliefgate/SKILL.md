# Skill: beliefgate

**Trigger:** any task involving "verify completeness", "check all required", "gate before
action", or whenever you are about to compute/answer using data that might be incomplete.

---

## What this skill does

Runs `beliefgate.check_set` to verify that every item the task requires is actually present
in the context — before any expensive or irreversible step. Never false-completes. Returns
the exact missing set on failure so the agent knows precisely what to fetch.

**The one rule:** feed `present` from a parser/DB/API. Derive `required` from the task.
Never let an LLM produce `present` by reading prose.

---

## Install

```bash
# from mahmoud-gadalla root
pip install -e gate-repl/dist/beliefgate
# or if gate-repl is a sibling dir:
pip install -e ../gate-repl/dist/beliefgate
```

Zero runtime dependencies.

---

## Usage pattern

```python
from beliefgate import check_set, Verdict

# 1. REQUIRED — parse from the task / question
required = extract_required_from_task(task)   # e.g. {"2021", "2022", "2023"}

# 2. PRESENT — from a STRUCTURED source (DB, file, API — never LLM prose)
present = parse_present_from_source(source)   # e.g. {"2021", "2023"}

# 3. GATE
res = check_set(required=required, present=present)

if res.ok:
    # proceed — coverage is proven
    answer = compute(...)
else:
    # abstain — exact gap known
    print(f"Missing: {res.missing}")   # e.g. {"2022"}
    # fetch missing items, or refuse
```

---

## Verdict reference

| `res.verdict` | Meaning | Action |
|---|---|---|
| `COMPLETE` | All required items present | Proceed |
| `INCOMPLETE` | `res.missing` lists the gap | Fetch gap or refuse |
| `UNDECIDABLE` | Can't determine from available data | Abstain or escalate |

---

## Predicate coverage (when required isn't a fixed list)

```python
from beliefgate import CoverageClaim, CoverageKind, SourceFacts, verify_coverage

facts = SourceFacts(
    present_count=len(rows),
    keys=[r.id for r in rows],
    sorted_desc=False,
    boundary_crossed=False,
    predicate_evaluable=True,
)
claim = CoverageClaim(CoverageKind.FULL_COUNT, total=source_claimed_total)
res = verify_coverage(claim, facts)
```

Only `FULL_COUNT` and `CONTIGUOUS_IDS` are deletion-proof. `SORTED_TO_THRESHOLD` is not —
the lib refuses to certify it.

---

## Fixation guard

On novel-structure tasks in multi-step chains, place the gate at step 1 (the fixation
point). One gate there rescues the entire chain. Don't add CoT everywhere — only where
the fast path is unreliable. (See `gate-repl/INCUBATION_FIXATION.md` §3 Exp. 7.)

---

## Anti-patterns

- ❌ LLM produces `present` by reading prose → measured failure mode
- ❌ `required` derived from the data instead of the task
- ❌ Filling gaps with zero/average/interpolation on INCOMPLETE
- ❌ Using it for relevance, tone, or subjective properties — no deterministic anchor
