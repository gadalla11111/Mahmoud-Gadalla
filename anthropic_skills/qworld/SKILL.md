# Skill: qworld

**Trigger:** evaluate LLM response quality, generate evaluation criteria, assess answer completeness, "how good is this response", question-specific rubric generation, LLM benchmarking.

---

## What this skill does

Generates question-specific evaluation criteria using recursive expansion trees (Qworld method
from `mims-harvard/Qworld`). Decomposes a question into scenarios → perspectives → fine-grained
criteria, enabling contextual evaluation that adapts per question rather than fixed rubrics.

Achieved 89% coverage of expert criteria on HealthBench. Reveals capability gaps in frontier
LLMs across equity, error handling, and interdisciplinary reasoning.

**Primary use in this repo:** skill evaluation in the library-maintainer loop. Replace static
adversarial cases with Qworld-generated criteria for richer, question-adaptive eval.

---

## Eval protocol (replaces static 5-case adversarial eval)

```
1. DECOMPOSE: given a skill's trigger, expand into scenarios × perspectives × criteria
2. GENERATE: create test cases covering each leaf criterion
3. SCORE: run skill response through each criterion (pass/fail)
4. REPORT: coverage% against expert criteria set
```

```python
def qworld_eval(skill_trigger: str, skill_response: str) -> dict:
    # Step 1: decompose trigger into evaluation tree
    tree = expand_question_tree(skill_trigger)
    # Step 2: extract leaf criteria
    criteria = extract_leaf_criteria(tree)
    # Step 3: score response against each criterion
    scores = {c: evaluate_criterion(skill_response, c) for c in criteria}
    return {
        "coverage": sum(scores.values()) / len(scores),
        "criteria": scores,
        "missing": [c for c, v in scores.items() if not v]
    }
```

---

## Integration with library-maintainer loop

In `misc/library_audit.py`, when `pass_rate=null`:
- Use Qworld to generate eval criteria from skill trigger
- Run 5 Qworld-generated cases (replaces manual adversarial cases)
- Set `pass_rate` from Qworld coverage score

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/library-maintainer
  - anthropic_skills/beliefgate
archetype: evaluation
```
