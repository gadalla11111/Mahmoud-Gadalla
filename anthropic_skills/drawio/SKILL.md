# Skill: drawio

**Trigger:** create a diagram, architecture diagram, flowchart, UML, C4 model, ER diagram, ML pipeline diagram, "visualize this system", "draw a diagram of", Mermaid diagram, draw.io.

---

## What this skill does

Converts natural language descriptions into professional draw.io diagrams with self-correction
and iterative refinement. Exports as PNG, SVG, PDF, or JPG.

**Source:** `Agents365-ai/drawio-skill`

---

## 7 Diagram Types

| Type | Use |
|---|---|
| **Architecture** | Microservices, cloud deployments, system topology |
| **C4 Model** | Multi-page system hierarchy (Context → Container → Component → Code) |
| **ML/Deep Learning** | Neural network graphs with tensor shape annotations |
| **Flowchart** | Processes, decision trees, state machines |
| **UML** | Class diagrams, sequence diagrams |
| **ERD** | Entity-relationship, database schema |
| **Mermaid** | Mindmaps, Gantt charts, timelines, git graphs |

---

## Workflow

```
describe system in natural language
  ↓
dependency check + layout planning
  ↓
generate .drawio XML
  ↓
export draft PNG → self-check (up to 2 auto-fix rounds)
  ↓
user review → refinement loop (up to 5 rounds)
  ↓
final export: PNG / SVG / PDF / JPG
```

---

## Special capabilities

- **Codebase visualization** — auto-diagrams Python/JS/Go/Rust codebases
- **IaC diagrams** — Terraform/Kubernetes/Docker → architecture diagram
- **SQL schemas** — database tables → ERD with official cloud provider icons
- **Mermaid → draw.io** — convert Mermaid source to editable draw.io format

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/mcp-builder
archetype: diagramming
```
