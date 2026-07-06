# Skill: tooluniverse

**Trigger:** any task involving scientific databases, biomedical APIs, drug discovery,
genomics, protein structure, clinical trials, literature search, or "query [scientific
database]" — or whenever an agent step needs to call an external scientific tool/API.

---

## What this skill does

Routes scientific API calls through ToolUniverse — a unified SDK giving access to
1,000+ scientific tools (AlphaFold, BLAST, DrugBank, PubMed, ClinVar, ClinicalTrials,
UniProt, ChEMBL, and hundreds more) via a consistent `BaseTool` interface.

**Integration with beliefgate:** always gate before irreversible scientific API calls.
Derive `required` from the research task; parse `present` from structured API responses.

---

## Install

```bash
pip install tooluniverse
# or from source:
pip install -e /path/to/ToolUniverse
```

---

## Usage pattern

```python
from tooluniverse import ToolUniverse

tu = ToolUniverse()
tu.load_tools()

# discover tools
tools = tu.get_tools()                          # all 1000+
tool = tu.get_tool("AlphaFoldTool")             # by name

# call a tool
result = tool.run({"uniprot_id": "P69905"})    # structured response

# MCP server (exposes all tools to Claude)
# run: tooluniverse-mcp
```

---

## Key tool categories

| Category | Examples |
|---|---|
| Protein structure | AlphaFold, AlphaFill, Boltz, ESMFold |
| Drug/molecule | DrugBank, ChEMBL, BindingDB, ADMET-AI |
| Genomics/variant | ClinVar, dbSNP, BLAST, Ensembl, gnomAD |
| Disease | DisGeNET, OMIM, ClinicalTrials, OpenTargets |
| Literature | PubMed, bioRxiv, arXiv |
| Multi-omics | GTEx, ARCHS4, CELLxGENE, Allen Brain |

---

## beliefgate integration

```python
from beliefgate import check_set

def scientific_agent_step(task, context):
    required = extract_required_from_task(task)   # e.g. {"uniprot_id", "organism"}
    present  = set(context.keys())                 # from structured API response
    gate = check_set(required, present)
    if not gate.ok:
        return fetch_missing(gate.missing)
    return tu.get_tool(task.tool).run(context)
```

---

## CLI discovery

```bash
tu list                          # browse all tools
tu info AlphaFoldTool            # schema + description
tu run AlphaFoldTool --help      # parameters
```

---

## Anti-patterns

- Never let an LLM produce `present` from prose API descriptions
- Don't bypass the gate for "simple" lookups — partial data is the failure mode
- Don't call tools in parallel when downstream steps depend on upstream results

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/beliefgate
  - anthropic_skills/deep-research
archetype: tool-routing
```
