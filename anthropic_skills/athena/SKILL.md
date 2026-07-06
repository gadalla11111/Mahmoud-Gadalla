# Skill: athena

**Trigger:** treatment reasoning, clinical decision support, drug recommendations, multi-step biomedical analysis, evidence-based medicine queries, "what treatment for [condition]", drug-disease relationships.

---

## What this skill does

Routes clinical reasoning tasks through ATHENA-R1 — an AI agent with 212 biomedical tools
that performs multi-step treatment reasoning by retrieving evidence before answering.
Outperforms GPT-5 on drug reasoning: 94.7% vs 76.9% on treatment benchmarks.

**Pattern:** identify required evidence → query biomedical tools → incorporate findings → conclude.
Never answer from parametric knowledge alone; always ground in retrieved evidence.

**Integration with beliefgate:** gate before any treatment recommendation.
`required` = set of evidence types needed (drug efficacy, contraindications, guidelines).
`present` = evidence retrieved from biomedical APIs.

---

## Source

`mims-harvard/ATHENA` — ATHENA-R1 treatment reasoning agent.

---

## Usage pattern

```python
from tooluniverse import ToolUniverse
from beliefgate import check_set

tu = ToolUniverse()
tu.load_tools()

def treatment_reasoning_step(query, evidence_context):
    required = extract_evidence_requirements(query)
    # e.g. {"drug_efficacy", "contraindications", "clinical_guidelines"}
    present = set(evidence_context.keys())
    gate = check_set(required, present)
    if not gate.ok:
        # fetch from DrugBank, PubMed, ClinVar, OpenTargets as needed
        return fetch_biomedical_evidence(gate.missing, tu)
    return synthesize_treatment_recommendation(query, evidence_context)
```

---

## Key evidence sources (via ToolUniverse)

| Need | Tool |
|---|---|
| Drug mechanism/efficacy | DrugBank, ChEMBL |
| Clinical guidelines | PubMed, bioRxiv |
| Adverse effects | FDA Adverse Events, ClinVar |
| Disease-gene links | DisGeNET, OMIM, OpenTargets |
| Clinical trials | ClinicalTrials.gov |

---

## Anti-patterns

- Never produce a treatment recommendation without first gating on required evidence
- Don't use LLM parametric knowledge as the `present` set — only structured API responses
- Don't parallelize steps where downstream reasoning depends on upstream evidence

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/tooluniverse
  - anthropic_skills/beliefgate
archetype: scientific-reasoning
```
