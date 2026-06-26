---
name: queue
description: >
  Prompt queue manager for Claude Code. Use when the user wants to queue
  a task for deferred or rate-limit-resilient execution, batch similar
  tasks, save reusable prompt templates, or check queue status.
  Triggers on: "queue this", "add to queue", "run later", "rate limit",
  "prompt bank", "save as template", "batch of tasks", "claude-queue".
  Proactively suggest queuing when a task spans many files, may hit limits,
  or the user says "I'll come back to this". Supports dependency chains,
  stale task detection, and cross-session state via engram.
allowed-tools: [Bash, Read, Glob, Write]
argument-hint: "[task description or subcommand: add|template|status|batch|bank|deps|stale]"
auto-trigger:
  - managing a backlog of tasks across a session
  - "add to queue"
  - "whats next"
  - "task list"
  - "backlog"
  - multi-step project where tasks arrive incrementally
  - rate limit already hit this session
do-not-trigger:
  - single-task sessions
  - one-shot requests
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Queue

`claude-queue` defers prompts for unattended execution with automatic rate-limit retry.

---

## Proactive Suggestion Rule

Suggest queuing without being asked when:
- Task touches more than 5 files (may hit usage limits mid-way)
- User says "run this later" or "I'll come back to this"
- A batch of similar tasks is described
- A rate limit was already hit this session
- A task has a prerequisite that isn't complete yet

Example prompt: "This refactor touches 12 files and may hit API limits. Want me to queue it so it retries automatically?"

---

## Core Commands

```bash
# Quick add (short prompt, no context files)
claude-queue add "Fix the auth bug" --priority 1 --working-dir /path/to/project

# Template file (complex prompt with context)
claude-queue template task-name --priority 2

# Check queue
claude-queue status --detailed
claude-queue list --status queued

# Start daemon (runs prompts, auto-retries on rate limit)
claude-queue start

# Cancel
claude-queue cancel <prompt-id>
```

Always suggest `claude-queue status --detailed` before starting the daemon so the user can review what will execute.

---

## Prompt Template Format

Template files live at `~/.claude-queue/queue/task-name.md`:

```markdown
---
priority: 1
working_directory: /absolute/path/to/project
context_files:
  - src/relevant-file.py
  - tests/test_relevant.py
max_retries: 3
estimated_tokens: null
depends_on: []          # list of task-names that must complete first
timeout_minutes: null   # null = no timeout; set for long-running tasks
---

# Task Title

Clear, self-contained description. Write as if there is no prior conversation context.

## Context
Background, constraints, requirements.

## Expected Output
What should be delivered.
```

### Frontmatter Reference

| Field | Notes |
|---|---|
| `priority` | 0 = highest. Lower = runs first. |
| `working_directory` | Absolute path. |
| `context_files` | Paths relative to `working_directory`. Only include files that exist. |
| `max_retries` | 3 = 3 total attempts. -1 = unlimited. 1 = no retry. |
| `estimated_tokens` | Optional hint; `null` if unknown. |
| `depends_on` | List of task-names. Daemon skips this task until all dependencies complete. |
| `timeout_minutes` | Max wall-clock time before marking as failed. `null` = unlimited. |

### Priority Guidelines

| Priority | Use for |
|---|---|
| `0` | Critical — blocks other work |
| `1` | High — explicit user request |
| `2` | Normal — general tasks |
| `5+` | Background / batch |

**Priority escalation**: if a task sits in queue for more than 24 hours without running, auto-suggest bumping its priority.

---

## `add` vs. Template

**Use `claude-queue add`** for:
- Short prompt (~200 chars)
- No context files needed
- Single clear action
- No dependencies

**Use a template file** for:
- Multi-step task needing structure
- Context files to attach
- Dependency on another task
- User wants to review/edit before running

---

## Dependency Graph

Tasks can declare prerequisites. The daemon respects order automatically.

```markdown
# Template: task-b.md
---
depends_on:
  - task-a    # task-b waits until task-a is in completed/
---
```

Check dependency status:
```bash
claude-queue deps task-b      # shows what task-b is waiting on
claude-queue deps --graph     # ASCII tree of all dependencies
```

Dependency rules:
- Circular dependencies are rejected at add time
- A task with a failed dependency is marked `blocked` (not auto-failed)
- Manual resolution: `claude-queue unblock task-b --override` after fixing the dependency

---

## Stale Task Detection

Tasks that haven't moved in an unusually long time are flagged:

```bash
claude-queue stale           # list tasks with no status change > 2h
claude-queue stale --purge   # remove stale tasks after user confirmation
```

A task is stale if:
- Status is `queued` for more than 2 hours with daemon running
- Status is `running` for more than `timeout_minutes` (if set)
- Status is `failed` and `max_retries` was reached days ago

Suggest stale purge at session start if the queue has been idle.

---

## Template Bank (Reusable Templates)

```bash
claude-queue bank save daily-docs      # Save to bank
claude-queue bank list                 # List saved templates
claude-queue bank use daily-docs       # Copy to active queue
claude-queue bank delete daily-docs    # Delete from bank
```

Bank templates live at `~/.claude-queue/bank/`. `bank use` copies to active queue — templates never execute directly.

---

## Batch Processing

```bash
claude-queue batch generate my-template --data entries.csv
claude-queue batch generate my-template --data entries.csv --dry-run
claude-queue batch variables my-template    # list {{placeholders}}
claude-queue batch validate my-template --data entries.csv
```

Use `{{variable}}` placeholders matching CSV column names:

```markdown
Refactor `{{filename}}` at `{{filepath}}`:
- Replace old_api() with new_api()
- Preserve existing tests
```

---

## Cross-Session Persistence (Engram Integration)

Queue state can be checkpointed so it survives session restarts:

```bash
claude-queue checkpoint    # write current queue state to engram working memory
claude-queue restore       # load last checkpoint into queue
```

When to checkpoint:
- Before ending a long session with tasks still queued
- After adding a complex dependency graph
- Any time `engram/working` skill would checkpoint working memory

The checkpoint writes to `~/.claude-queue/queue-state.json` AND the engram working memory directory for cross-tool visibility.

---

## Queue Layout

```
~/.claude-queue/
├── queue/          # Active (daemon reads these)
├── completed/      # Done
├── failed/         # Exhausted retries
├── bank/           # Reusable templates
└── queue-state.json
```

---

## Key Behaviors

- **`--dangerously-skip-permissions`** is passed to `claude` by default for unattended runs. Override with `--no-skip-permissions`.
- **At-least-once semantics**: if daemon crashes mid-run, task reruns on restart. Design queued tasks to be idempotent.
- **Dependency graph**: `depends_on` ensures correct execution order across sessions.
- **Stale detection**: `claude-queue stale` surfaces tasks that are stuck without needing manual inspection.
- **Engram checkpoint**: queue state persists across sessions when checkpointed.
