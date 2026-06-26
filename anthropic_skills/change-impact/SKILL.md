---
name: change-impact
description: >
  Ripple-effect screen for controlled changes. Use when a change touches
  more than one kind of artifact, a running system, a schema, or an API
  other code depends on. Finds what a change leaves stale across docs,
  tests, skills, commands, templates, prompts, and runtime contracts —
  before those surfaces surprise you. Returns per-item actions (update /
  leave / defer / block), not a vague "looks fine".
allowed-tools: [Read, Glob, Grep, Bash, Write]
argument-hint: "[change description or diff path]"
auto-trigger:
  - before merging or shipping a change
  - "what does this break", "what depends on X", "impact of removing Y"
  - refactoring a shared module or public API
  - any change touching more than 3 files
do-not-trigger:
  - greenfield code with no existing dependents

---

# Change Impact

An impact screen answers: when a controlled item changes, what else does that change leave out of date? You look downstream for ripple effects before they hit.

---

## Artifact families to screen

For each family, decide one action: **update** / **leave as-is** / **defer** / **block**.

| Family | What to check |
|---|---|
| Documentation | README, CLAUDE.md, API docs, architecture docs referencing changed items |
| Tests | Unit, integration, e2e tests covering changed behavior |
| Skills | SKILL.md files referencing changed workflows, paths, or APIs |
| Commands / slash-commands | Any command that wraps or describes changed behavior |
| Templates | Prompt templates, issue templates, PR templates with stale references |
| Checkers / validators | Scripts or CI steps that validate the changed surface |
| Prompts | System prompts or few-shot examples referencing changed behavior |
| Release artifacts | Changelogs, release notes, version pins |
| Saved versions | Pinned configs, lockfiles, cached artifacts |
| Source-lineage notes | Attribution or provenance references to changed items |

---

## Runtime blast radius (check when touching live systems)

When the change affects a running system, stored data, or an API:

- **Schema migration**: what consumes this schema? what breaks on old shape?
- **API contract**: what downstream services depend on the changed interface?
- **Backward compatibility**: can old clients still function? for how long?
- **Rollback-of-state**: if we revert, what data is stranded or incompatible?

---

## Process

1. Name the change: file(s), behavior(s), interface(s) affected
2. For each artifact family above: does the change leave it stale?
3. For each stale surface: assign one action (update / leave / defer / block) with an owner and re-check trigger
4. For live systems: run the runtime blast-radius check
5. Carry any block-level items into the release posture

---

## Output

```markdown
## Change Impact Screen
**Change**: [description]

| Artifact | Stale? | Action | Owner | Re-check trigger |
|---|---|---|---|---|
| CLAUDE.md line 34 | Yes — references deleted file | update | [name] | before merge |
| tests/auth/ | No | leave as-is | — | — |
| CHANGELOG.md | Yes — unreferenced | update | [name] | before release |
| API v1 consumers | Unknown | defer | [name] | post-deploy monitoring |

## Runtime blast radius
[schema / API / backward-compat / rollback findings, or "not applicable"]

## Blockers
[Items with `block` action — carry into release posture]
```

---

## Rules

- **No stale surface silently accepted** — every stale item gets an action and an owner
- **Deferred items get triggers** — a defer without a named re-check trigger is a hidden gap
- **Small changes can break public claims** — do not skip documentation because the diff looks small
- **Checker updates can't wait** — if docs claim a behavior, drift in the validator matters now

---

## Common rationalizations to reject

- "The diff is small." Small changes can break docs, tests, or public claims.
- "The README can lag." Public docs are controlled surfaces that carry trust.
- "The near miss is fixed." The control that let it happen may still be stale.
