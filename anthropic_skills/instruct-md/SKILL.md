# Skill: instruct-md

**Trigger:** __instruct.md, per-folder context file, folder-scoped instructions, hierarchical project context, instruct md pattern, modular codebase context, folder-level AI instructions, progressive disclosure context.

---

## What this skill does

The `__instruct.md` per-folder pattern — compact, scoped context files that AI agents load progressively as they navigate a project. Each folder carries its own purpose, structure, and intent. Avoids the "read everything" problem by making context hierarchical and self-describing.

**Source:** DC Dmitry (Desktop Commander community) | MIT spirit

---

## The Pattern

Every folder the agent interacts with has an `__instruct.md` file describing:
1. **Purpose** — what this folder does and why it exists
2. **Contents** — key files and what they contain
3. **Relationships** — what this folder imports from / exports to
4. **Rules** — any special handling, constraints, or conventions

**Exception:** `__tests__` folders — no `__instruct.md` needed.

---

## File Structure

```markdown
# [FolderName] Instructions

## Purpose
[What this folder/module does — 1-3 sentences]

## Key Files
- `main.py` — entry point, [what it does]
- `config.yaml` — [what it configures]
- `utils/` — [what utilities are here]

## Relationships
- Imports from: `../auth/`, `../db/`
- Consumed by: `../api/routes/`

## Rules & Constraints
- [Any non-obvious rules specific to this folder]
- [Performance constraints, security requirements, etc.]

## Current State
- [What's done, what's in progress, what's next — keep it short]
```

---

## Creation Rules

1. **Create on first touch** — if `__instruct.md` doesn't exist when you enter a folder, create it
2. **Keep it compact** — 20-50 lines max; no padding, no history
3. **Reference, don't copy** — point to files by path + line range, never paste code
4. **Update after changes** — when you modify a folder, update its `__instruct.md`
5. **Delete stale content** — remove completed tasks, outdated descriptions
6. **Never duplicate** — if the root `__instruct.md` already covers it, reference that

---

## Evaluation Checklist (after create/update)

- [ ] Purpose is clear in ≤ 3 sentences
- [ ] All key files are listed with one-line descriptions
- [ ] Dependencies (in/out) are documented
- [ ] No stale or completed task references remain
- [ ] File is ≤ 50 lines
- [ ] No code pasted inline — only file references

---

## vs. CLAUDE.md / SKILL.md

| | `__instruct.md` | `CLAUDE.md` | `SKILL.md` |
|---|---|---|---|
| **Scope** | One folder | Whole project | One capability domain |
| **Updated by** | Agent during work | Human + agent | Agent/author once |
| **Purpose** | Structural context | Global rules | Reusable capability |
| **Read when** | Agent enters folder | Session start | Task matches trigger |

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/context-engineering
  - anthropic_skills/engram/working
archetype: context-pattern
```
