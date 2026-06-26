---
name: adr
description: >
  Architecture Decision Records: create, review, verify, and index ADRs.
  Use when recording significant architectural decisions (new tech adoption,
  API design, data model changes, infrastructure choices). Routes by trigger
  phrase: "create adr", "review adr", "verify adrs", "index adrs".
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob]
argument-hint: "[create <title> | review [--branch BRANCH] | verify | index]"
auto-trigger:
  - significant architectural decision (new tech, API design, data model, infra choice)
  - user asks 'should we use X or Y' at an architectural level
  - "create adr"
  - "record decision"
  - "document why we chose"
do-not-trigger:
  - trivial implementation details
  - bug fixes
  - config-only changes

health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []
---

# Architecture Decision Records (ADR)

ADRs capture the why behind architectural choices. They are cheap to write and
expensive to skip — without them, the next engineer repeats your research or
reverses your decision unknowingly.

| Trigger | Action |
|---|---|
| "create adr <title>" | Create a new sequentially numbered ADR |
| "review adr" / "adr compliance" | Check code changes against accepted ADRs |
| "verify adrs" / "adr integrity" | Detect cycles, dangling refs, status mismatches |
| "index adrs" / "rebuild adr index" | Scan all ADRs and rebuild the reference index |

---

## create — New ADR

**When**: a significant architectural decision must be recorded.

**Steps**:
1. `Glob` for `docs/adr/ADR-*.md` and parse existing numbers to find the next sequential ID (ADR-001, ADR-002, …). Create `docs/adr/` if it does not exist.
2. Slugify the title argument: lowercase, hyphen-separated (e.g. "Use PostgreSQL" → `use-postgresql`).
3. `Write` the file at `docs/adr/ADR-NNN-<slug>.md` using this template:

```markdown
# ADR-NNN: <Title>

- **Status**: proposed
- **Date**: <YYYY-MM-DD>
- **Deciders**: <!-- names or team -->
- **Tags**: <!-- domain tags -->

## Context

<!-- What is the issue that motivates this decision? What forces are at play? -->

## Decision

<!-- What is the change being proposed and why? -->

## Consequences

### Positive
- 

### Negative
- 

### Neutral
- 

## Alternatives Considered

| Alternative | Reason rejected |
|---|---|
| | |

## References

- <!-- links to discussions, RFCs, related ADRs -->
```

4. Scan existing ADRs for related decisions and add references.
5. Report: file path created, next steps (fill in Context and Decision sections, change status to "accepted" when approved).

---

## review — Compliance Check

**When**: before merging a PR; after significant code changes; periodic audit.

**Steps**:
1. Run `git diff main...HEAD --name-only` (or `--branch` arg) to list changed files.
2. Run `git diff main...HEAD` to get full diff.
3. For each changed file:
   - `Grep` for ADR references (`ADR-\d+`) in the file
   - `Grep` `docs/adr/` for ADRs mentioning the changed file paths or modules
4. `Read` each relevant ADR. Focus on: **Decision** (what was decided), **Status** (only enforce `accepted`), **Consequences** (constraints).
5. Analyze each changed file against its ADRs:
   - Does the change contradict an accepted decision?
   - Does it use technology/pattern an ADR explicitly rejected?
   - Does it modify a module in a way the ADR's consequences warned against?
   - Does it reference a superseded ADR?
6. Report:

```markdown
## ADR Compliance Report

### Violations
- [ ] <file>:<line> — violates ADR-NNN: <reason>

### Warnings
- [!] <file> references superseded ADR-NNN (replaced by ADR-MMM)

### Compliant
- [x] <file> — consistent with ADR-NNN

### Unlinked Changes
- [?] <file> — no ADR coverage (consider creating one with `/adr create`)
```

7. For each violation: suggest whether to update the code or propose a new ADR to supersede.

---

## verify — Graph Integrity

**When**: after creating/modifying ADRs; in CI; before a release.

**Steps**:
1. `Glob` all `docs/adr/ADR-*.md` files.
2. For each ADR, extract: ID, status, supersedes/amends/related references.
3. Check for:
   - **Dangling refs** — a reference points to an ADR ID that does not exist on disk
   - **Supersede cycles** — ADR-A supersedes ADR-B and ADR-B supersedes ADR-A (or longer cycles)
   - **Status mismatches** — an ADR is the source of a `supersedes` edge but its own status is not `Superseded`
4. Report findings. Exit with a clear error message on cycles (always a data error).

```markdown
## ADR Integrity Report

### Cycles (CRITICAL — must fix)
- ADR-003 supersedes ADR-007 supersedes ADR-003 ← cycle

### Dangling References
- ADR-012 references ADR-099 (not found)

### Status Mismatches
- ADR-005 has a supersedes edge to ADR-008 but status is "accepted" (should be "Superseded")

### OK
- 14 ADRs, 6 edges — no issues
```

---

## index — Rebuild Reference Index

**When**: bootstrapping ADR tracking on an existing codebase; after bulk ADR import; when search is out of sync.

**Steps**:
1. `Glob` all `docs/adr/ADR-*.md` (and `docs/adrs/` as fallback).
2. For each ADR, parse:
   - ID and title (from `# ADR-NNN:` heading)
   - Status (from `**Status**:` line or YAML frontmatter)
   - Relationships: supersedes, amends, related, depends-on (scan body for ADR-\d+ refs)
3. Build an index table and a relationship graph edge list.
4. Write `docs/adr/INDEX.md`:

```markdown
# ADR Index

| ID | Title | Status | Supersedes | Amends |
|---|---|---|---|---|
| ADR-001 | Use PostgreSQL | accepted | — | — |
| ADR-007 | Switch to CockroachDB | accepted | ADR-001 | — |

## Relationship Graph
- ADR-007 supersedes ADR-001
- ADR-003 amends ADR-002
```

5. Report: total ADRs indexed, by-status breakdown, edge count, any integrity issues found (run verify logic inline).

---

## ADR lifecycle

```
proposed → accepted → superseded (by a later ADR)
         → rejected
         → deprecated
```

An ADR is immutable once accepted — record changes by creating a new ADR that supersedes it.

---

## Rules

- **One decision per ADR** — a record covering multiple unrelated choices is a sign the decision was not clear.
- **Rejected alternatives belong in the ADR** — if you don't write them down, the next engineer evaluates them again.
- **Status must be accurate** — an "accepted" ADR that has been implicitly reversed is worse than no ADR.
- **Never delete ADRs** — mark as superseded or deprecated; the history is the value.
