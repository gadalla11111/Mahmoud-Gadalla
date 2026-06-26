---
name: nested-subagents
description: >
  Spawn a tree of sub-agents where each child can itself spawn children, up to
  5 levels deep. Solves two problems: (1) context management — each node gets a
  fresh context window so deep work does not exhaust the root's budget; (2)
  parallelism — independent subtasks run simultaneously when spawned in the same
  turn. Use when a problem decomposes into nested layers (research → expand →
  verify → synthesize), when a single context window cannot hold all intermediate
  state, or when subtasks genuinely benefit from specialised agent types. Trigger
  on: "spawn agents", "delegate to subagents", "parallel research", "multi-domain",
  "too large for one agent". Skip when flat fan-out (parallel Task calls in one
  message) is enough — prefer simplicity.
allowed-tools: [Task, TodoWrite, Read, Grep, Glob, Bash]
argument-hint: "<problem-statement>"
auto-trigger:
  - task too large or broad for a single agent turn
  - parallelisable subtasks that can run independently
  - "spawn agents for"
  - "delegate to subagents"
  - "parallel research"
  - multi-domain task requiring specialised agents per domain
  - context window would overflow with all intermediate state
do-not-trigger:
  - simple single-step tasks
  - sequential tasks with no parallelism and no context overflow
  - when flat fan-out (parallel Task calls) in one message is sufficient
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Nested Sub-Agents

Delegate deep work through a tree of agents, each with its own clean context window. The motivation is **context management + parallelism**: leaves report compact summaries upward so the root never accumulates every intermediate artifact, and independent branches run simultaneously.

---

## Choose Your Spawn Pattern First

Pick the pattern that matches the problem structure. Only go deeper when the pattern genuinely requires it.

| Pattern | Structure | When to use |
|---|---|---|
| **Fan-out (flat)** | Root → N leaves in parallel | Independent subtasks, no nesting needed. Use plain `Task` calls in one message — no subagent skill needed. |
| **Pipeline** | Root → A → B → C (sequential) | Each stage's output is the next stage's input. Depth 1 per stage. |
| **Map-Reduce** | Root → N mappers → 1 reducer | Parallel data gathering, single synthesis. Depth 2. |
| **Tree** | Root → coordinators → workers → leaves | Multi-domain, multi-layer decomposition. Depth 3–4. |
| **Scatter-Gather** | Root → domain agents → verifiers → synthesizer | Research + verification per domain. Depth 3. |

Default to the **shallowest pattern** that keeps each node's context clean. Depth adds latency — every extra level is a round trip.

---

## Depth Budget

| Source | Limit |
|---|---|
| Anthropic API | 5 levels |
| Recommended default | 4 levels (one guard band) |
| Research/doc tasks | 3 levels is almost always enough |
| Code tasks | 2 levels usually sufficient |

---

## Agent Type Selection

Match the `subagent_type` to what the node needs to do:

| Node role | Recommended `subagent_type` | Notes |
|---|---|---|
| Coordinator / orchestrator | `general-purpose` | Needs Task tool to spawn children |
| Code writer / fixer | `general-purpose` | Needs Edit, Write, Bash |
| Researcher / reader | `Explore` | Read-only, fast, no side effects |
| Code reviewer | `code-reviewer` | Focused on diff analysis |
| Verifier / fact-checker | `general-purpose` | Needs WebSearch or Grep |
| Leaf worker (no spawning) | Any — omit Task from tools | Explicitly disable spawning |

If the subagent_type list doesn't include a specialist, `general-purpose` with a tightly scoped prompt is always safe.

---

## Process

### Step 1 — Decompose Before Spawning

Never spawn without a written tree plan. Use `TodoWrite` to lay out the full spawn tree before any `Task` call:

```
root-coordinator
├── domain-A-agent (depth 1) — parallel
│   ├── fetcher-A1 (depth 2)
│   └── fetcher-A2 (depth 2)
├── domain-B-agent (depth 1) — parallel
│   └── verifier-B (depth 2)
└── synthesis-agent (depth 1) — waits for domain agents
```

Show the tree to the user and get confirmation for depth 3+ work. For depth 1–2 fan-out, just proceed.

### Step 2 — Spawn Parallel Branches in One Message

**Critical**: spawn all independent branches in the same response. Don't spawn A, wait for A, then spawn B. Parallel branches spawned in one message run concurrently.

```python
# Spawn all depth-1 nodes in one turn
Task({
    "subagent_type": "Explore",
    "name": "research-domain-A",
    "description": "Research <domain A>",
    "prompt": """
<sub-task for domain A>

You are a leaf researcher. Do NOT spawn children.
Return a structured summary ≤ 300 tokens.
Current depth: 1 of 4. Spawning: DISABLED.
"""
})

Task({
    "subagent_type": "Explore", 
    "name": "research-domain-B",
    "description": "Research <domain B>",
    "prompt": """
<sub-task for domain B>

You are a leaf researcher. Do NOT spawn children.
Return a structured summary ≤ 300 tokens.
Current depth: 1 of 4. Spawning: DISABLED.
"""
})
```

### Step 3 — Root Coordinator Pattern (for deep trees)

When you need a coordinator to manage depth-2+ children:

```python
Task({
    "subagent_type": "general-purpose",
    "name": "root-coordinator",
    "description": "Decompose and delegate <problem>",
    "prompt": """
<problem statement>

You are the root coordinator. Your job:
1. Decompose the problem into N independent sub-tasks.
2. Spawn one child agent per sub-task using Task — spawn ALL in one message (parallel).
3. Each child must return a summary ≤ 300 tokens.
4. Synthesize child summaries into a final report.

Current depth: 1 of 4 maximum.
Children you spawn will be at depth 2 — they may spawn depth-3 children.
Depth-3 children must NOT spawn further.

Return the synthesized report when all children complete.
"""
})
```

### Step 4 — Depth Tracking (mandatory)

Pass current depth in every child prompt. A node at the depth cap does the work itself or returns an "exceeded depth" signal — never spawns.

```python
# Inside a coordinator at depth 2, spawning depth-3 leaves:
Task({
    "subagent_type": "general-purpose",
    "name": "leaf-worker",
    "prompt": """
<sub-task description>

Current depth: 3 of 4. You are a LEAF. Do NOT spawn children.
Return a structured summary ≤ 200 tokens.
"""
})
```

### Step 5 — Compact Upward Reporting

Each node returns a structured summary, never its full work product:

```markdown
## Summary: {node-name}
- Completed: {what was done — 1 sentence}
- Key findings: {bullet list, ≤ 5 items}
- Artifacts: {file paths or inline snippets if small}
- Open issues: {anything the parent needs to decide}
```

Parents synthesize child summaries. They never need to read child raw output. This is what keeps the root's context clean.

### Step 6 — Error Containment

A failing child should not crash the whole tree. Each coordinator must handle child failure explicitly:

```
If child returns an error or "exceeded depth" signal:
1. Log the failure in Open Issues
2. Attempt the subtask inline (at current depth) if small enough
3. Otherwise mark as unresolved and continue with remaining children
4. Surface all unresolved items in the final report's Gaps section
```

Never let a single leaf failure block the synthesis step.

---

## Output Format

Root coordinator final report:

```markdown
# Task Complete: {problem-statement}

## Findings
{synthesized from all child summaries — not transcribed verbatim}

## Artifacts
{list of files, data, or outputs produced}

## Gaps / Open Issues
{anything that could not be resolved within the tree}

## Tree Stats
- Pattern used: {fan-out / pipeline / map-reduce / tree / scatter-gather}
- Depth used: {N} of {cap} levels
- Agents spawned: {N}
- Failed nodes: {N} (see Gaps)
```

---

## Common Recipes

### Research + Synthesize (Map-Reduce, depth 2)

```
root → [source-A-fetcher, source-B-fetcher, source-C-fetcher] → synthesis
```
Spawn all fetchers in one message. Wait for all. Synthesize inline at root.

### Multi-Domain Feature (Tree, depth 3)

```
root
├── spec-writer (reads requirements, produces AC)
├── implementer (reads AC, writes code)
│   └── tdd-runner (runs tests, reports failures)
└── reviewer (reads diff, applies checklist)
```
Spec and review can't run until implementer finishes — use sequential coordination at root.

### Security Scan (Pipeline, depth 2)

```
root → semgrep-runner → codeql-runner → findings-synthesizer
```
Each stage's output is the next stage's input. Sequential pipeline at depth 1 each.

### Competitive Research (Scatter-Gather, depth 3)

```
root
├── competitor-A-agent → verifier-A
├── competitor-B-agent → verifier-B
└── competitor-C-agent → verifier-C
→ synthesis (after all gather)
```
Scatter phase parallel; gather phase sequential.

---

## Rules

- **Decompose first, spawn second** — never spawn without a written tree plan.
- **Parallel branches in one message** — don't serialize what can run concurrently.
- **Pass depth budget explicitly** — every child prompt must know its current depth and cap.
- **Leaves return ≤ 300-token summaries** — parents synthesize, not transcribe.
- **No spawning at the depth cap** — work inline or return an "exceeded depth" signal.
- **Contain failures** — a failing child goes to Gaps; it doesn't abort the tree.
- **Prefer shallower trees** — depth adds latency; flat fan-out is almost always faster for ≤6 independent tasks.
- **Disable spawning explicitly** — tell leaf nodes "Do NOT spawn children" in the prompt; don't rely on tool restrictions alone.
