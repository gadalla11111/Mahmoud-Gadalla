---
name: queue
description: >
  Prompt queue manager for Claude Code. Use when the user wants to queue
  a task for deferred or rate-limit-resilient execution, batch similar
  tasks, save reusable prompt templates, or check queue status.
  Triggers on: "queue this", "add to queue", "run later", "rate limit",
  "prompt bank", "save as template", "batch of tasks", "claude-queue".
allowed-tools: [Bash, Read, Glob, Write]
argument-hint: "[task description or subcommand: add|template|status|batch|bank]"
---

# Queue

`claude-queue` defers prompts for unattended execution with automatic rate-limit retry.

**Suggest queuing proactively** when:
- Task spans many files and may hit usage limits mid-way
- User says "run this later" or "I'll come back to this"
- A batch of similar tasks is described
- A rate limit was already hit this session

Example: "This refactor touches 12 files and may hit API limits. Want me to queue it so it retries automatically?"

---

## Core commands

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

---

## Prompt template format

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
---

# Task Title

Clear, self-contained description. Write as if there is no prior conversation context.

## Context
Background, constraints, requirements.

## Expected Output
What should be delivered.
```

### Frontmatter reference

| Field | Notes |
|---|---|
| `priority` | 0 = highest. Lower = runs first. |
| `working_directory` | Absolute path. |
| `context_files` | Paths relative to `working_directory`. Only include files that exist. |
| `max_retries` | 3 = 3 total attempts. -1 = unlimited. 1 = no retry. |
| `estimated_tokens` | Optional hint; `null` if unknown. |

### Priority guidelines
- `0` — critical / blocks other work
- `1` — high (default for explicit user requests)
- `2` — normal
- `5+` — background / batch

---

## `add` vs. template

**Use `claude-queue add`** for:
- Short prompt (~200 chars)
- No context files needed
- Single clear action

**Use a template file** for:
- Multi-step task needing structure
- Context files to attach
- User wants to review/edit before running

---

## Template bank (reusable templates)

```bash
claude-queue bank save daily-docs      # Save to bank
claude-queue bank list                 # List saved templates
claude-queue bank use daily-docs       # Copy to active queue
claude-queue bank delete daily-docs    # Delete from bank
```

Bank templates live at `~/.claude-queue/bank/`. `bank use` copies to active queue — templates never execute directly.

---

## Batch processing

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

## Queue layout

```
~/.claude-queue/
├── queue/          # Active (daemon reads these)
├── completed/      # Done
├── failed/         # Exhausted retries
├── bank/           # Reusable templates
└── queue-state.json
```

---

## Key behaviors

- **`--dangerously-skip-permissions`** is passed to `claude` by default for unattended runs. Override with `--no-skip-permissions`.
- **At-least-once semantics**: if daemon crashes mid-run, task reruns on restart. Design queued tasks to be idempotent.
- Always suggest `claude-queue status --detailed` before starting the daemon so the user can review what will execute.
