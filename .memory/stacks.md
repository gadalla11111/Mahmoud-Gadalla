# Skill Stacks — Knowledge Checkpoint
**Last updated**: 2026-06-26 (rev 12) — all 51 skills now placed in at least one stack

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

## Agent Stacks

**Core (always)**
```
think-twice → sparc → claude-api → ultracode → tdd
```
- think-twice: confirm agent is needed vs single call or workflow

**Simple tool-use agent**
```
think-twice → claude-api → ultracode → tdd
```

**Complex multi-tool agent**
```
adr → sparc → claude-api → ultracode → tdd → change-impact
```

**Managed agent (Anthropic-hosted)**
```
adr → sparc → claude-api → ultracode → tdd → mcp-builder → mcp-inspector
```
- mcp-builder: expose tools as MCP for the managed agent to consume

**Nested / multi-agent systems**
```
adr → orchestrator → nested-subagents → claude-api → ultracode → tdd
```
- orchestrator: design the agent hierarchy first

**Debugging a broken agent**
```
debug → mcp-inspector → claude-api → ultracode (quick-mode)
```

**Cost-aware agent development**
```
sipcode/estimate → [build] → sipcode/why
```
- Agents compound token cost fast — estimate before building

**Shipping an agent**
```
ultracode → change-impact → tdd → handoff
```

**Key rules**
- Pass the "should I build an agent?" test: complexity + value + viability + cost of error
- `sparc` before any agent with >3 tools or open-ended loop logic
- `tdd` for every tool — tools are contracts
- `claude-api` always — don't guess SDK patterns for tool use or streaming
- `sipcode/estimate` before any L/XL agent chain — costs compound per loop iteration
- Managed agents need `mcp-builder` — tools must be MCP-exposed

---

## Security Stacks

**Core (always)**
```
think-twice → ultracode → tdd → change-impact
```
- ultracode Phase 0 (Think) mandatory — security tasks never skip threat modelling

**Vulnerability investigation**
```
debug → change-impact → ultracode (quick-mode) → tdd
```
- debug: root cause and exploit path first, fix second

**Security-sensitive new features**
```
adr → sparc → ultracode → tdd → change-impact
```
- adr: record auth model, data boundary, trust level decisions

**Dependency / supply chain review**
```
deep-research → prove-claims → change-impact
```
- deep-research: CVE lookup, dependency audit, upstream reputation

**Secret scanning / credential hygiene**
```
ultracode (quick-mode) → change-impact
```
- Remove secrets, rotate credentials, audit git history

**Security audit of existing code**
```
debug → change-impact → adr → ultracode → tdd
```

**API security (auth, rate limiting, input validation)**
```
adr → sparc → claude-api → ultracode → tdd
```

**Incident response**
```
debug → internal-comms → change-impact → ultracode (quick-mode) → handoff
```
- internal-comms: incident communication while fix is in progress

**Hard rules**
- Never skip Phase 0 (Think) on security tasks — ultracode enforces this
- `change-impact` before AND after any security fix — attack surface can shift
- `adr` for any decision that affects trust boundaries or data access
- No security fix ships without `tdd` — untested patches create new vulnerabilities
- Never commit `.env` or credentials — DiffGate blocks it but don't rely on it

---

## Testing Stacks

**Core (always)**
```
think-twice → tdd → ultracode (quick-mode) → change-impact
```

**New feature tests**
```
sparc → tdd → ultracode → change-impact
```
- sparc: spec the behaviour before writing tests

**Regression tests after a bug fix**
```
debug → tdd → ultracode (quick-mode)
```
- debug: reproduce the bug first, then write a test that pins it

**E2E / browser tests**
```
think-twice → webapp-testing → tdd
```
- webapp-testing: Playwright automation, UI flows, E2E scenarios

**API / tool contract tests**
```
tdd → claude-api → ultracode
```
- claude-api if testing Claude SDK integrations

**MCP tool tests**
```
mcp-inspector → tdd → webapp-testing
```
- mcp-inspector: understand the tool interface before writing tests

**Performance / load tests**
```
adr → tdd → change-impact
```
- adr: document the performance contract before testing against it

**Security tests**
```
debug → tdd → change-impact
```
- Test the exploit path first, then the fix, then the regression

**Test coverage audits**
```
change-impact → debug → tdd
```
- change-impact: find the uncovered surface

**Agent / loop tests**
```
tdd → claude-api → ultracode → change-impact
```
- Test each tool in isolation, then loop exit conditions

**Key rules**
- `tdd` always before `ultracode` — tests drive implementation, never the reverse
- `debug` before regression tests — reproduce first, then pin with a test
- `webapp-testing` for anything with a UI — Playwright over manual QA
- `change-impact` after any test suite change — tests are part of the API contract
- `mcp-inspector` before MCP tool tests — understand the schema before asserting

---

## Cost / Token Economics Stacks

**Full lifecycle**
```
sipcode/estimate → [run task] → sipcode/why → sipcode/impact → sipcode/benchmark
```

**Pre-flight cost prediction**
```
sipcode/estimate → [task]
```
- Predict cost across Opus / Sonnet / Haiku before committing

**Post-session forensics**
```
sipcode/why
```
- Forensic audit of where tokens actually went in one session

**Prove savings (A/B)**
```
sipcode/impact
```
- Before/after comparison on the user's own session data
- Honesty-gated: `delta: null` when comparison windows aren't comparable

**Verify the headline claim**
```
sipcode/benchmark
```
- Reproduce the headline savings number on demand

**Key rules**
- `impact` refuses to invent a savings number when windows are unfair — respect the integrity contract
- `benchmark` is the only one that *proves* the claim; `why` only diagnoses one session
- Never extrapolate single-session savings across many sessions
- Cross-reference: cost-hygiene shortcuts (`estimate → task → why`) live in Workflow + Orchestration stacks

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
| `sipcode/impact` + `sipcode/benchmark` | prove savings, then reproduce the claim |
| `engram/working` + `engram/briefing` | checkpoint on pause, briefing on return |
| `orchestrator` + `nested-subagents` | route then delegate |
| `think-twice` + `surgical` | think minimally, act minimally |
| `mcp-builder` + `mcp-inspector` | build then debug |
| `doc-coauthoring` + `handoff` | writing session needs checkpoint |
