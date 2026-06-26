# Skill Stacks — Knowledge Checkpoint
**Last updated**: 2026-06-26 (rev 8)

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

## Workflow Stacks

**Core (always)**
```
think-twice → surgical
```

**Session start**
```
engram/briefing → orchestrator
```

**Session end / context switch**
```
engram/working → handoff
```

**Ambiguous requests**
```
promptize → think-twice → [right skill]
```

**Recurring tasks**
```
think-twice → skill-creator → orchestrator
```
- skill-creator formalises the workflow so it auto-triggers next time

**Cost hygiene**
```
sipcode/estimate → [task] → sipcode/why
```

**Instruction / config quality**
```
steering-lint → claude-md-audit
```
- steering-lint: check CLAUDE.md vs hooks vs skills placement (7 rules)
- claude-md-audit: audit quality, conflicts, bloat

**Knowledge hygiene**
```
engram/consolidate → engram/working
```
- consolidate before handoff to deduplicate and prune stale memory

**Queue-driven workflows**
```
queue → orchestrator → engram/working
```
- checkpoint after each queue item completes

**Key rules**
- `think-twice` + `surgical` is the default for any workflow step — do less, not more
- `promptize` before acting on any request that could be interpreted multiple ways
- `engram/working` at every natural pause — memory is cheap, context loss is not
- `steering-lint` whenever CLAUDE.md feels bloated or contradictory

---

## Finance Stacks

**Core (always)**
```
think-twice → analyzing-financial-statements → fact-checker
```

**Financial modelling**
```
think-twice → creating-financial-models → fact-checker
```

**Full investment analysis**
```
deep-research → analyzing-financial-statements → creating-financial-models → fact-checker
```

**Financial reports / deliverables**
```
analyzing-financial-statements → fact-checker → xlsx → pdf / docx
```

**Financial models as deliverables**
```
creating-financial-models → fact-checker → xlsx
```

**Presentations with financial data**
```
analyzing-financial-statements → fact-checker → pptx
```
- Never put unverified figures in a slide deck

**Due diligence**
```
deep-research → ultra-search → analyzing-financial-statements → creating-financial-models → fact-checker
```

**Scenario / sensitivity analysis**
```
creating-financial-models → fact-checker → xlsx → doc-coauthoring
```

**Branded financial deliverables (Acme Corp)**
```
[finance skill] → fact-checker → applying-brand-guidelines → xlsx / pdf / docx
```

**Key rules**
- `fact-checker` always gates financial output — numbers without sources don't ship
- `analyzing-financial-statements` before `creating-financial-models` — understand history before projecting
- `deep-research` before analysis on any unfamiliar company or sector
- `xlsx` is the canonical output for financial models

---

## Ministry Proposal Stacks

**Core (always)**
```
deep-research → fact-checker → ministry-proposal → pptx
```
- fact-checker is a hard gate — no slide gets a stat without 3 independent sources

**Full proposal from scratch**
```
deep-research → ultra-search → fact-checker → ministry-proposal → design → pptx
```
- design applies visual system after content is locked

**Verifying existing claims**
```
fact-checker → prove-claims → ministry-proposal
```
- Run before finalizing any slide that cites figures

**Data-backed slides**
```
analyzing-financial-statements → fact-checker → ministry-proposal → pptx
```

**Arabic language quality**
```
ministry-proposal → fact-checker → internal-comms
```
- internal-comms: review tone and register for formal Arabic فصحى

**Branded output**
```
ministry-proposal → applying-brand-guidelines → pptx
```
- MERIDIAN: `#0E0E0E` black dominant (MY4 Education)
- Jahizoon: `#1C2B45` navy dominant (MBK Education)

**Handoff between sessions**
```
engram/briefing → ministry-proposal → fact-checker → engram/working
```

**Hard rules**
- `fact-checker` is non-negotiable — proposals cannot be finalized without it
- Pre-verified: 41.5% graduate unemployment (CAPMAS Q1 2026) — safe to use
- ⚠️ Nexford figures (78%/41%/51%) — single-sourced, need 2nd source before any slide
- `deep-research` before `ministry-proposal` — never draft slides on unverified material
- Visual system must match the client: MERIDIAN ≠ Jahizoon

---

## Brand Stacks

**Core (always)**
```
think-twice → applying-brand-guidelines → fact-checker
```
- Confirm which brand system applies before touching anything

**Brand compliance on documents**
```
[format skill] → applying-brand-guidelines → fact-checker
```
- Apply brand after content is written, verify before delivery

**UI/frontend brand consistency**
```
frontend-design → brand-guidelines → applying-brand-guidelines
```
- brand-guidelines: general principles during build
- applying-brand-guidelines: Acme Corp–specific compliance check after build

**Design systems**
```
theme-factory → applying-brand-guidelines → brand-guidelines
```

**Branded financial deliverables**
```
[finance skill] → fact-checker → applying-brand-guidelines → xlsx / pdf / docx
```
- Numbers verified first, brand applied last

**Branded ministry proposals**
```
ministry-proposal → applying-brand-guidelines → pptx
```
- MERIDIAN: `#0E0E0E` black dominant (MY4 Education)
- Jahizoon: `#1C2B45` navy dominant (MBK Education)

**New brand assets**
```
design → theme-factory → applying-brand-guidelines
```

**Internal branded communications**
```
internal-comms → applying-brand-guidelines → fact-checker
```

**Branded presentations**
```
design → pptx → applying-brand-guidelines → fact-checker
```

**Key rules**
- `applying-brand-guidelines` triggers on any Acme Corp document — no exceptions
- Always confirm which brand system applies before designing (Acme ≠ MERIDIAN ≠ Jahizoon)
- Brand check comes after content is locked, before delivery
- `fact-checker` always follows brand check if the doc has any cited claims

---

## MCP Stacks

**Core (always)**
```
think-twice → mcp-builder → ultracode → mcp-inspector
```

**New MCP server from scratch**
```
adr → sparc → mcp-builder → ultracode → tdd → mcp-inspector
```

**Debugging a broken MCP server**
```
debug → mcp-inspector → ultracode (quick-mode)
```

**MCP servers using Claude API**
```
claude-api → mcp-builder → ultracode → tdd → mcp-inspector
```

**Exposing existing codebase as MCP**
```
change-impact → adr → mcp-builder → ultracode → mcp-inspector
```
- change-impact: assess what exposing as MCP breaks or touches

**Testing MCP tool behaviour**
```
mcp-inspector → webapp-testing → tdd
```

**Shipping an MCP server**
```
ultracode → change-impact → mcp-inspector → handoff
```

**Key rules**
- `mcp-inspector` is always the last step before declaring an MCP server done
- `adr` before any MCP server that exposes shared infrastructure
- `tdd` for every tool — tool schemas are contracts, test them like APIs
- `claude-api` if Claude is the MCP client — don't guess SDK patterns

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
