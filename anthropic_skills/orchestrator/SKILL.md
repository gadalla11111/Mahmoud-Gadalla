---
name: orchestrator
description: >
  Meta-skill that reads the incoming task, selects the right skill(s) from the
  library, chains them in the correct order, and applies quality gates — all
  while minimizing token spend. Use whenever a task could benefit from a
  structured skill but the user has not named one. Trigger phrases: "best way
  to", "help me with", "what skill should I use", "orchestrate", or any open-
  ended task where skill selection is non-obvious. Skip when the user has
  already named a specific skill to invoke.
allowed-tools: [Read, Glob, Grep, Bash, Task]
argument-hint: "<task description>"
---

# Orchestrator

One entry point for the full skill library. Classify the task, select the
minimum viable skill chain, execute with quality gates, and report token cost.

---

## Classification → Skill routing table

Read the task. Match the primary intent to a row. If multiple rows match,
check the **chain** column — that is the ordered execution plan.

### Single-skill intents

| Intent signal | Skill | Token tier |
|---|---|---|
| "catch me up" / "where did I leave off" / resume session | `engram/briefing` | XS |
| "checkpoint" / "save context" | `engram/working` | XS |
| "consolidate notes" / "organize knowledge" | `engram/consolidate` | S |
| "estimate cost" / "how many tokens" | `sipcode/estimate` | XS |
| "token spend audit" / "why so many tokens" | `sipcode/why` | XS |
| "token impact" / "did sipcode help" | `sipcode/impact` | XS |
| "clarify this ask" / "sharpen the prompt" | `promptize/promptize` | XS |
| "think before coding" / "is there a simpler way" | `lazy-cat/think-twice` | XS |
| "surgical edit" / "only change X" | `lazy-cat/surgical` | XS |
| "debug" / "diagnose" / "why is this failing" | `debug` | S |
| "write tests" / "TDD" / "red-green-refactor" | `tdd` | M |
| "SPARC" / "structured feature" / "spec then implement" | `sparc` | M–L |
| "ADR" / "architecture decision" | `adr` | S |
| "nested agents" / "deep delegation" / "subagent tree" | `nested-subagents` | M |
| "queue task" / "batch prompt" | `queue` | S |
| "build MCP server" | `mcp-builder` | L |
| "inspect MCP repo" / "is this MCP safe" | `mcp-inspector` | M |
| "CLAUDE.md accurate?" / "check docs for staleness" | `claude-md-audit` | S |
| "what does this change affect" / "ripple effect" | `change-impact` | S |
| "prove these claims" / "evidence for" | `prove-claims` | S |
| "fact check" / "verify claims" / "source this" / "triple check" / "QA grid" | `fact-checker` | S–M |
| "hand off work" / "transfer to another agent" | `handoff` | S |
| "create a PRD" / "product requirements" | `prd-generator` | M |
| "deep research" / "comprehensive research" | `deep-research` | L |
| "ultra search" / "max coverage search" | `ultra-search` | L |
| "news" / "primary source" / "what is being reported" | `news-research` | M |
| "create skill" / "new skill" / "improve skill" | `skill-creator` | M |
| "brand guidelines" | `brand-guidelines` | S |
| "design" / "UI" / "frontend" | `design` (routes internally) | M |
| "web app" / "React" / "Vue" / "HTML artifact" | `frontend-design` | M |
| "canvas" / "static art" / "illustration" | `canvas-design` | M |
| "slides" / "PowerPoint" / "presentation" | `pptx` | M |
| "Word document" / ".docx" | `docx` | S |
| "PDF" | `pdf` | S |
| "Excel" / "spreadsheet" | `xlsx` | S |
| "test web app" / "browser automation" | `webapp-testing` | M |
| "Slack" / "internal comms post" | `internal-comms` | S |
| "GIF for Slack" | `slack-gif-creator` | S |
| "co-author doc" | `doc-coauthoring` | S |

### Multi-skill chains (ordered)

| Scenario | Chain | Notes |
|---|---|---|
| New feature from scratch | `sparc` (spec) → `tdd` → `sparc` (refine/complete) | SPARC gates, TDD fills coverage |
| Research-backed document | `deep-research` → `prove-claims` → `prd-generator` or `docx` | Verify before writing |
| Architecture change | `lazy-cat/think-twice` → `adr` (create) → `change-impact` → `adr` (review) | Think first, record decision, screen ripple |
| Security-sensitive feature | `sparc` (spec) → `tdd` → `prove-claims` | Claims must be backed before shipping |
| Releasing work | `prove-claims` → `change-impact` → `handoff` | Gate before hand-off |
| Search → publish | `ultra-search` or `news-research` → `prove-claims` → output skill | Never publish unverified claims |
| MCP eval | `mcp-inspector` → `mcp-builder` (if safe) | Inspect before build |
| Session start | `engram/briefing` → task-appropriate skill | Orient first |
| Overlong session | `engram/working` → continue | Checkpoint before context fills |
| Vague ask | `promptize/promptize` → route again after approval | Clarify before routing |

---

## Token tiers

| Tier | Approximate cost | When to use |
|---|---|---|
| XS | < 2 K tokens | Status, checkpoint, routing queries |
| S | 2–8 K | Single well-scoped action |
| M | 8–30 K | Multi-step skill with output |
| L | 30–100 K | Deep research, large SPARC cycles |
| XL | > 100 K | Only if justified; flag to user |

Before starting a chain, estimate total tier and state it. If the chain would
reach XL, propose a scoped alternative and ask the user to confirm.

---

## Process

### Step 1 — Classify

Read the task description. Identify:
- **Primary intent** (what the user wants produced)
- **Secondary intents** (quality gates, verification, documentation)
- **Constraints** (token budget, deadline, "just a quick X")

### Step 2 — Select

Match to the routing table above. If no single row matches, check the chain
table. If still ambiguous, invoke `promptize/promptize` to sharpen the ask
before proceeding.

### Step 3 — Estimate and confirm (for M+ chains)

State the plan before executing:
```
Plan: deep-research → prove-claims → prd-generator
Estimated tier: L (~40–60 K tokens)
Proceed? (y / adjust scope / swap to lighter alternative)
```
Skip this confirmation for XS and S tiers — just run.

### Step 4 — Execute

Run each skill in order. Pass outputs forward explicitly:
- Provide the prior skill's output as context to the next skill's prompt
- Do not re-derive what was already established

### Step 5 — Quality gate

After each skill completes, apply the relevant gate:

| Skill type | Gate |
|---|---|
| Research | Every claim has a source URL; no unsupported assertions |
| Code | Tests pass; karpathy-guidelines satisfied (no scope creep) |
| Documents | All section headings filled; no `<!-- TODO -->` placeholders |
| SPARC | Every AC has a corresponding test; traceability matrix complete |
| ADR | Status is accurate; alternatives are recorded |
| Handoff | Incoming owner can restate scope and stop conditions |

If a gate fails, fix the gap before reporting completion — do not surface a
partial result without flagging what is missing.

### Step 6 — Report

```markdown
## Orchestrator Summary
**Task**: {original task description}
**Skills used**: {list}
**Token tier**: {XS/S/M/L/XL} — estimated {N}K tokens
**Quality gates**: {passed / failed items}
**Output**: {summary of what was produced}
**Next step**: {what the user should do now, if anything}
```

---

## Rules

- **Never add skills that the task does not require.** A one-step task does
  not need a chain. Unnecessary skill invocations waste tokens.
- **Classify before acting.** Even for obvious tasks, state the selected skill
  before running it.
- **Confirm before L or XL chains.** The user's token budget is not yours to
  spend without notice.
- **Pass outputs forward, not sideways.** Each skill in a chain receives the
  prior skill's output as explicit context — do not start fresh.
- **Quality gates are not optional.** A chain that skips gates produces
  unverified output faster, not better output.
- **When in doubt, promptize first.** An ambiguous task routed to the wrong
  skill wastes more tokens than a brief clarification round.
