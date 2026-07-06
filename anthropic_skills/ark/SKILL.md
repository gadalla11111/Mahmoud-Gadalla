# Skill: ark

**Trigger:** biomedical knowledge graph queries, "find relationships between [gene/drug/disease]", graph-based biological network analysis, multi-hop biomedical reasoning, knowledge graph exploration.

---

## What this skill does

Routes biomedical knowledge graph queries through ARK (Agent Relay for Knowledge graphs) —
a CLI-based agent that discovers knowledge graphs and answers natural language questions
about complex biological relationships.

Pre-loaded biomedical graphs: protein-protein interactions, drug-disease associations,
gene-phenotype networks. Custom graphs accepted as Parquet + config file.

**Source:** `mims-harvard/gates-buildathon`

---

## Usage pattern

```bash
# launch ARK with a biomedical question
ark --graph protein_interactions "What proteins interact with BRCA1?"
ark --graph drug_disease "Which drugs target the pathway for Type 2 Diabetes?"

# add a custom knowledge graph
# 1. provide data.parquet with edges (source, target, relation, weight)
# 2. provide config.yaml with graph metadata
ark --graph ./my_graph "Query in natural language"
```

---

## When to use ARK vs ToolUniverse

| Task | Use |
|---|---|
| Lookup single entity (protein structure, drug info) | ToolUniverse |
| Multi-hop relationship queries across a graph | ARK |
| "What connects A to B through C?" | ARK |
| "Get the AlphaFold structure for P69905" | ToolUniverse |

---

## beliefgate integration

Gate on graph availability before querying:

```python
gate = check_set({"graph_loaded", "query_parsed"}, present)
if not gate.ok:
    return load_graph(gate.missing)
```

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/tooluniverse
  - anthropic_skills/beliefgate
  - anthropic_skills/athena
archetype: knowledge-graph
```
