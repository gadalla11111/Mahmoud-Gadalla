# Skill: data-management

**Trigger:** data governance, data catalog, data quality, metadata management, data pipeline, ETL design, data lineage, master data management, data dictionary, data lake architecture, data observability, GDPR data compliance, data mesh, data contract, dataset versioning.

---

## What this skill does

End-to-end data management — governance, cataloging, quality, pipelines, and compliance. Draws on alirezarezvani/claude-skills data patterns, HuggingFace dataset standards, and OpenMetadata catalog conventions.

**Sources:**
- `alirezarezvani/claude-skills` — data & compliance skills | MIT
- `huggingface/hugging-face-datasets` — dataset configs and SQL querying | Apache 2.0
- OpenMetadata — open platform for data context and business semantics

---

## Coverage by Domain

### Data Governance
- Policy design: ownership, stewardship, classification (public / internal / confidential / restricted)
- Regulatory compliance: GDPR, CCPA, HIPAA, EU AI Act, DPDP Act
- Data access controls, entitlement reviews, audit trails

### Data Catalog & Metadata
- Business glossary construction (terms, definitions, owners)
- Technical metadata: schema, lineage, column-level profiling
- OpenMetadata-style asset tagging and discovery

### Data Quality
- Quality dimensions: completeness, accuracy, consistency, timeliness, uniqueness
- Profiling: null rates, distribution checks, schema drift detection
- Anomaly monitoring rules and SLA-breach alerting

### Pipeline & ETL Design
- Source → transform → load patterns (batch, micro-batch, streaming)
- Data contract design: schema versioning, breaking-change protocol
- HuggingFace datasets: config YAML, splits, SQL querying via DuckDB

### Data Architecture
- Data lake vs. warehouse vs. lakehouse trade-offs
- Data mesh: domain ownership, federated governance, product thinking for data
- Data observability: freshness, volume, schema, distribution pillars

### Data Dictionary & Documentation
- Column-level descriptions, example values, business context
- Lineage diagrams (source → transformation → consumer)

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/scientific-research
  - anthropic_skills/ai-research
archetype: data-governance
```
