# Skill: scientific-research

**Trigger:** bioinformatics analysis, RNA-seq, single-cell, cheminformatics, molecular docking, drug discovery pipeline, clinical variant interpretation, pharmacogenomics, scientific data visualization, lab automation, materials science, proteomics, neuroscience data analysis.

---

## What this skill does

Routes scientific computing tasks through K-Dense-AI's scientific agent skill library —
148 skills covering biology, chemistry, medicine, and data science, backed by 100+
scientific databases and Python package integrations.

**Source:** `K-Dense-AI/scientific-agent-skills` | 148 skills | MIT licensed

**Complements:** `anthropic_skills/tooluniverse` (API lookups) + `anthropic_skills/athena` (clinical reasoning)

---

## 148 Skills by Category

| Category | Skills | Key Capabilities |
|---|---|---|
| **Bioinformatics & Genomics** | 23 | RNA-seq, single-cell (Scanpy), sequence processing, phylogenetics |
| **Scientific Communication** | 26 | Literature review, peer review, LaTeX, presentation tools |
| **Data Analysis & Visualization** | 21 | Statistical analysis, network viz, geospatial, Matplotlib/Seaborn |
| **Machine Learning** | 14 | Deep learning, Bayesian methods, graph neural networks, time series |
| **Cheminformatics & Drug Discovery** | 10 | RDKit, molecular docking, virtual screening, MD simulation |
| **Post-Training (ML)** | 8 | Fine-tuning, LoRA, RLHF, distillation |
| **Clinical & Precision Medicine** | 8 | Variant interpretation, pharmacogenomics, clinical trials |
| **Materials Science & Physics** | 7 | Crystal structures, quantum computing, astronomical data |
| **Platform Integrations** | 9 | Benchling, DNAnexus, LatchBio, OMERO, Protocols.io |
| **Lab Automation** | 6 | Liquid handling, LIMS, cloud lab platforms |

---

## Routing decision

| Task | Skill |
|---|---|
| Database lookup (protein, drug, gene) | `tooluniverse` |
| Treatment recommendation | `athena` |
| Biomedical knowledge graph | `ark` |
| Computational analysis (RNA-seq, docking, ML) | `scientific-research` (this skill) |
| Literature synthesis | `deep-research` |

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/tooluniverse
  - anthropic_skills/athena
  - anthropic_skills/ark
archetype: scientific-computing
```
