---
name: nested-subagents
description: >
  Spawn a tree of sub-agents where each child can itself spawn children, up to
  5 levels deep. For context management, not parallelism — each level gets a
  fresh context window so deep work does not exhaust the top-level agent's
  context budget. Use when a problem decomposes into nested layers (research →
  expand → verify → synthesize) or when a single context window cannot hold
  all intermediate state. Skip when flat fan-out (parallel Task calls in one
  message) is enough.
allowed-tools: [Task, TodoWrite, Read, Grep, Glob, Bash]
argument-hint: "<problem-statement>"
auto-trigger:
  - task too large or broad for a single agent turn
  - parallelisable subtasks that can run independently
  - "spawn agents for", "delegate to subagents", "parallel research"
  - multi-domain task requiring specialised agents per domain
do-not-trigger:
  - simple single-step tasks
  - sequential tasks with no parallelism

---

# Nested Sub-Agents

Delegate deep work through a tree of agents, each with its own clean context window.
The motivation is **context management**, not parallelism: leaves report compact
summaries back up the tree so the root never accumulates every intermediate artifact.

---

## When to use

- The problem decomposes into nested layers where each layer's output is the input
  for the next (e.g. research → expand findings → verify claims → synthesize report).
- A single agent's context window would not hold all intermediate state.
- The leaves of the tree need different `subagent_type`s (e.g. `pii-detector` at
  one leaf, `tester` at another) with specialized prompts.

**Skip** when flat fan-out suffices — spawning parallel `Task` calls in a single
message is simpler, faster, and adequate when there is no nesting dependency.

---

## Depth budget

| Source | Limit |
|---|---|
| Anthropic API | 5 levels |
| Recommended default | 4 levels (one guard band) |

Each additional level adds round-trip latency. Default to the minimum depth that
keeps each node's context clean.

---

## Process

### Step 1 — Decompose before spawning

Before any `Task` call, use `TodoWrite` to lay out the full spawn tree:

```
root-coordinator
├── research-agent (depth 1)
│   ├── source-a-fetcher (depth 2)
│   └── source-b-fetcher (depth 2)
├── synthesis-agent (depth 1)
│   └── verifier (depth 2)
└── writer-agent (depth 1)
```

Show the user the tree and get confirmation before spawning deep work.

### Step 2 — Spawn the root coordinator

```python
Task({
    "subagent_type": "general-purpose",
    "name": "root-coordinator",
    "description": "Decompose and delegate <problem>",
    "prompt": """
<problem statement>

You are the root coordinator. Your job:
1. Decompose the problem into N sub-tasks.
2. Spawn one child agent per sub-task using Task (you may spawn children,
   who may in turn spawn children — max depth from this node: 3).
3. Each child must return a summary ≤ 200 tokens.
4. Synthesize child summaries into a final report.

Current depth: 1 of 5 maximum.
"""
})
```

### Step 3 — Children spawn children

Any agent that has `Task` in its tool list can spawn the next level. Agents
without `Task` are leaves — they do the work and return a compact summary.

**Depth tracking**: pass the current depth in every child prompt and decrement
the remaining budget. A node at depth 4 must not spawn children.

```python
# Inside a coordinator prompt at depth 2:
Task({
    "subagent_type": "general-purpose",
    "name": "leaf-worker",
    "description": "Execute specific sub-task",
    "prompt": """
<sub-task description>

Return a structured summary ≤ 200 tokens. Do NOT spawn children (you are at
depth 3 of 5 — spawning is disabled at this level for this task).
"""
})
```

### Step 4 — Compact upward reporting

Each node returns a structured summary, not a full transcript:

```markdown
## Summary: {node-name}
- Completed: {what was done}
- Key findings: {bullet list, ≤ 5 items}
- Artifacts produced: {file paths or inline snippets}
- Open issues: {anything the parent needs to decide}
```

The parent synthesizes child summaries; it never needs to read child raw output.

---

## Output format

Root coordinator final report:

```markdown
# Task Complete: {problem-statement}

## Findings
{synthesized from all child summaries}

## Artifacts
{list of files, data, or outputs produced by the tree}

## Gaps / Open Issues
{anything that could not be resolved within the tree}

## Tree Summary
- Depth used: {N} levels
- Agents spawned: {N}
- Total nodes: {N}
```

---

## Rules

- **Decompose first, spawn second** — never spawn without a written tree plan.
- **Pass depth budget explicitly** — every child prompt must know its current depth.
- **Leaves return ≤ 200-token summaries** — parents synthesize, not transcribe.
- **No spawning at the depth cap** — a node at depth 5 (or at your configured cap) must do the work itself or return an "exceeded depth" signal.
- **Depth adds latency** — prefer shallower trees; only go deeper when context genuinely overflows.
