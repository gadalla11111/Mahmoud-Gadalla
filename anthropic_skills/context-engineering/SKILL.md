# Skill: context-engineering

**Trigger:** context management for AI agents, context window optimization, intentional compaction, memory bank architecture, progressive context loading, research-plan-implement workflow, sub-agent context isolation, AI coding brownfield codebase, context utilization, modular skills architecture.

---

## What this skill does

Advanced context engineering for AI coding agents — structured workflows that keep context quality high across long sessions in large codebases. Synthesizes HumanLayer ace-fca patterns, Desktop Commander modular skills approach, and memory bank architecture.

**Sources:**
- `humanlayer/advanced-context-engineering-for-coding-agents` (ace-fca.md) | MIT
- Desktop Commander community (DC Eduards modular skills pattern)
- Memory bank pattern (Spectral / alex_here_now)

---

## Core Thesis

Context window quality is the only lever you control with stateless LLMs. "Frequent intentional compaction" — periodically distilling messy context into structured artifacts — is what separates productive AI coding from context soup.

**Target:** Keep context utilization at **40–60%** for production work. At 80%+ quality degrades sharply.

---

## The Three-Phase Workflow (ace-fca)

### 1. Research
- Use **fresh sub-agent context windows** to find/summarize code
- Sub-agents search → distill → return compact summaries to main agent
- Prevents search noise from polluting the implementation context
- Human review focus: research summaries (200 lines) not code (2,000 lines)

### 2. Plan
- Distill research into a structured implementation plan before writing code
- Plan is the highest-leverage human review point — a flawed plan cascades into thousands of bad lines
- Keep plan < 200 lines; reference file paths + line ranges, never paste code

### 3. Implement
- Agent implements against the plan with clean, focused context
- Periodic compaction: distill implementation progress into structured artifacts
- Reset context when approaching 60–70% utilization

---

## Memory Bank Architecture

**Hierarchical .md structure** (Spectral pattern + snarktank/ai-dev-tasks):

```
.memory-bank/
├── activeContext.md      # current focus, next step (keep short)
├── productContext.md     # what & why of the product
├── progress.md           # done / in-progress / blocked
├── projectbrief.md       # 600-line broad overview (AI rarely reads unless linking front↔back)
├── systemPatterns.md     # architectural decisions, patterns
└── techContext.md        # stack, dependencies, env setup
```

**Rules:**
- Each specialized file updated incrementally after every small feature
- Delete unnecessary content — keep files short and focused on next step
- Broad overview (projectbrief.md) read only when needed (cross-boundary linking)
- Update specialized file first, then compact into broad if needed

---

## Modular Skills Architecture (DC Eduards)

Per-folder context files instead of one monolithic system prompt:

```
project/
├── skills/
│   ├── main-skill.md          # entry point: what this is, how to use, how to improve
│   ├── bigquery/
│   │   ├── skill.md           # high-level intent
│   │   ├── first-setup.md
│   │   ├── connect.md
│   │   └── test-query-costs.md
│   └── auth/
│       ├── skill.md
│       └── oauth-flow.md
```

**Key principle:** Prefer referencing over rewriting.
- Reference files + line ranges instead of pasting code into markdown
- Reference existing docs, web pages, PDFs instead of duplicating them
- One source of truth per piece of information

---

## `__instruct.md` Per-Folder Pattern (DC Dmitry)

See `anthropic_skills/instruct-md/SKILL.md` for full details.

---

## Anti-Patterns to Avoid

- Pasting full file contents when a line reference suffices
- One monolithic 600-line system prompt read on every message
- No compaction: letting context grow until it hits the wall
- Memory bank files that grow unboundedly without trimming
- Reading entire codebase on every new chat (use hierarchical progressive loading instead)

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/engram/working
  - anthropic_skills/instruct-md
  - anthropic_skills/lazy-cat/think-twice
archetype: context-management
```
