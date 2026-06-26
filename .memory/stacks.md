# Skill Stacks — Knowledge Checkpoint
**Last updated**: 2026-06-26 (rev 3)

---

## Coding Stacks

**Core (always)**
```
think-twice → ultracode → karpathy-guidelines → tdd
```

**New features**
```
think-twice → sparc → ultracode → tdd → change-impact
```

**Bug fixes**
```
debug → ultracode (quick-mode) → tdd
```

**Architecture decisions**
```
adr → sparc → ultracode
```

**Shipping**
```
ultracode → change-impact → handoff
```

**API/SDK work**
```
claude-api → ultracode → tdd
```

**MCP servers**
```
mcp-builder → ultracode → mcp-inspector
```

**Quick edits (trivial, <20 lines)**
```
think-twice + surgical
```

---

## Design Stacks

**Core (always)**
```
think-twice → design → brand-guidelines
```

**Frontend/UI**
```
think-twice → frontend-design → brand-guidelines → webapp-testing
```

**Design systems**
```
theme-factory → brand-guidelines → frontend-design
```

**Presentations/documents**
```
design → pptx / docx / pdf → fact-checker
```

**Arabic ministry proposals**
```
ministry-proposal → design → fact-checker
```

**Generative/canvas**
```
algorithmic-art → canvas-design → web-artifacts-builder
```

**Slack assets**
```
design → slack-gif-creator
```

**Quick visual tweak**
```
surgical + brand-guidelines
```

---

## Research Stacks

**Core (always)**
```
deep-research → fact-checker → prove-claims
```

**Current events / time-sensitive**
```
news-research → fact-checker → prove-claims
```

**Exhaustive competitive research**
```
ultra-search → deep-research → fact-checker
```

**Proposals and documents**
```
deep-research → fact-checker → pptx / docx / pdf
```

**Arabic ministry proposals**
```
deep-research → fact-checker → ministry-proposal
```
- fact-checker is a hard gate — proposal cannot be finalized without it
- Pre-verified: 41.5% graduate unemployment (CAPMAS Q1 2026)
- ⚠️ Nexford figures (78%/41%/51%) single-sourced — need 2nd source before publishing

**PRDs and product specs**
```
deep-research → prove-claims → prd-generator
```

**Cost-sensitive research sessions**
```
sipcode/estimate → deep-research → sipcode/why
```

**Quick single claim**
```
prove-claims
```

---

## Document Stacks

**Core (always)**
```
think-twice → [format skill] → fact-checker
```
- fact-checker is mandatory if the doc contains any stats or claims

**By output format**

| Output | Skill |
|---|---|
| Word (.docx) | `docx` |
| PDF | `pdf` |
| PowerPoint (.pptx) | `pptx` |
| Excel (.xlsx) | `xlsx` |

**Collaborative writing**
```
doc-coauthoring → fact-checker → handoff
```

**Product specs / PRDs**
```
deep-research → prove-claims → prd-generator → docx / pdf
```

**Internal communications**
```
internal-comms → fact-checker
```

**Arabic ministry proposals**
```
deep-research → fact-checker → ministry-proposal → pptx
```
- fact-checker is a hard gate — cannot finalize without it

**Data-heavy documents**
```
xlsx → fact-checker → pdf / docx
```
- Build data model in Excel first, export narrative around verified numbers

**Branded documents**
```
[format skill] → brand-guidelines → fact-checker
```

**Session handoff notes**
```
handoff → docx / pdf
```

**Quick single doc (no claims)**
```
surgical + [format skill]
```

---

## Orchestration Stacks

**Core (always)**
```
promptize → orchestrator → nested-subagents
```

**Large ambiguous tasks**
```
promptize → orchestrator → nested-subagents → handoff
```

**Queue / backlog management**
```
queue → orchestrator
```

**Cost-aware orchestration**
```
sipcode/estimate → orchestrator → nested-subagents → sipcode/why
```
- Estimate before spinning up agent trees — costs compound fast

**Creating new workflows**
```
skill-creator → orchestrator
```
- skill-creator formalises recurring workflow; orchestrator routes it automatically next time

**Session management**
```
engram/briefing → orchestrator → engram/working
```

**ADR-driven orchestration**
```
adr → orchestrator → nested-subagents → change-impact
```

**Key rules**
- `orchestrator` before any request spanning 2+ skill domains
- `nested-subagents` only when subtasks are genuinely parallelisable
- `promptize` whenever intent is ambiguous — wrong routing wastes the whole chain
- `sipcode/estimate` before any L/XL agent tree

---

## Cross-Domain Complementary Pairs

| Pair | Why |
|---|---|
| `ultracode` + `karpathy-guidelines` | ultracode calls karpathy internally (Phase 2) |
| `ultracode` + `tdd` | ultracode Phase 2 requires tests |
| `ministry-proposal` + `fact-checker` | fact-checker is a mandatory pre-finalization gate |
| `deep-research` + `fact-checker` | find → verify |
| `fact-checker` + `prove-claims` | verify → substantiate |
| `frontend-design` + `brand-guidelines` | UI must be brand-checked |
| `design` + `theme-factory` | visual design feeds design tokens |
| `prd-generator` + `sparc` | PRD feeds SPARC spec phase |
| `sipcode/estimate` + `sipcode/why` | pre-flight then post-session forensics |
| `engram/working` + `engram/briefing` | checkpoint on pause, briefing on return |
| `orchestrator` + `nested-subagents` | route then delegate |
| `think-twice` + `surgical` | think minimally, act minimally |
| `mcp-builder` + `mcp-inspector` | build then debug |
| `doc-coauthoring` + `handoff` | writing session needs checkpoint |
