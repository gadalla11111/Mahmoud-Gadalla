# Skill Stacks — Knowledge Checkpoint
**Last updated**: 2026-06-26

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
