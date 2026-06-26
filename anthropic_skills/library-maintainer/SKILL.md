---
name: library-maintainer
description: >
  Self-maintenance loop for the skill library. Runs the cycle:
  OVERVIEW → EVALUATE → EVOLVE → MERGE → AUTO-TRIGGER. Use to audit library
  health, run the mechanical auditor, fix the highest-priority drift, and keep
  the four routing surfaces in sync. Trigger on: "audit the library", "maintain
  the skills", "run the maintenance loop", "what skills need work", "library
  health". Archetype: Orchestrator. Drives misc/library_audit.py and routes
  fixes to skill-creator (evolve), find-skills (discover), and yeet (ship).
allowed-tools: [Bash, Read, Edit, Write, Glob, Grep, Task]
argument-hint: "[--audit | --evolve | --once | --report]"
auto-trigger:
  - "audit the library"
  - "maintain the skills"
  - "run the maintenance loop"
  - "what skills need work"
  - library health or drift check
do-not-trigger:
  - creating a single specific skill (use skill-creator)
  - routing one task (use orchestrator)
  - non-library codebase maintenance
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Library Maintainer

The skill library's self-maintenance loop. One cycle = overview the state,
evaluate for drift, evolve the highest-priority gap, ship it, and re-trigger
only if more work remains. Designed to run on a schedule or on demand.

---

## The Loop

```
        ┌──────────────────────────────────────────────┐
        ▼                                                │
1. OVERVIEW ──► 2. EVALUATE ──► 3. EVOLVE ──► 4. MERGE ──┘  (auto-trigger
   audit            findings        one fix      on green     if findings remain)
```

Each tick does **at most one focused evolution**, ships it, then decides whether
to re-arm. Small, reviewable PRs over big sweeps.

---

## Phase 1 — Overview (mechanical)

```bash
python misc/library_audit.py            # human report
python misc/library_audit.py --json     # machine report (exit 1 if drift)
```

The auditor reports totals and every drift class:
- `invalid-yaml` / `no-frontmatter` (🔴 high)
- `missing-health-block`, `missing-from-<surface>` (🟠 med)
- `eval-never-run`, `count-claim` mismatch (🟡 low)

Exit 0 = clean (end the loop). Exit 1 = work to do.

---

## Phase 2 — Evaluate (prioritize)

Order findings by severity, then by blast radius:

| Priority | Finding | Why |
|---|---|---|
| P0 | invalid-yaml / no-frontmatter | Skill may not load at all |
| P1 | missing-from-<surface> | Skill exists but is unreachable |
| P2 | missing-health-block | Untracked quality |
| P3 | eval-never-run | Unverified routing |
| P4 | count-claim mismatch | Cosmetic but signals desync |

Pick the **single highest-priority cluster** for this tick. For `eval-never-run`,
batch ~5–8 related skills into one adversarial eval round (see skill-creator).

---

## Phase 3 — Evolve (one focused fix)

Route the fix:

| Finding | Route to |
|---|---|
| invalid-yaml / missing-health | fix inline (this skill) |
| missing-from-surface | sync the routing surface(s) inline |
| eval-never-run | run adversarial eval (skill-creator method), write health numbers |
| capability gap (a real need with no skill) | `find-skills` → `skill-creator` |
| description/trigger collision | `skill-creator` (optimize description) |

**Rules while evolving** (learned this session):
- `auto-trigger`/`do-not-trigger`: one phrase per YAML item; never `- "a", "b"`
  and never a quoted phrase followed by bare words. Validate with PyYAML.
- Don't touch bundled upstream skills' content beyond frontmatter hygiene.
- Conflict resolution on `.memory/skills.md`, `.memory/stacks.md`, `CLAUDE.md`:
  keep our version (`git checkout --ours`), then re-apply the intended edit.
- Never bypass DiffGate ORANGE with `--no-verify` — remediate the content.

---

## Phase 4 — Merge (ship on green)

Hand to `yeet` (or the manual flow): branch off main, commit, push, open a draft
PR. Then gate on CI — Python lint 3.11/3.12, Secret scan, Code review gate,
Dependency review must all be green. If a webhook delivers a merge conflict,
rebase onto latest main, force-with-lease, re-check.

**Merge policy** — choose per the loop's authorization:
- **Supervised** (default): mark ready, surface green status, let a human merge.
- **Autonomous**: merge on all-green only for skill-markdown / config / docs
  changes that are DiffGate-clean. Never auto-merge code changes to
  `claude_agent_sdk/` or `misc/` logic without review.

---

## Phase 5 — Auto-Trigger (re-arm by need)

After merging, re-run Phase 1:
- **Still findings** → schedule the next tick (the loop continues).
- **Clean** → stop; report the green state.

This is the "according to need" part: the loop runs itself only while drift
exists, and goes quiet when the library is clean.

---

## Scheduling

- On demand: invoke this skill, or run `python misc/library_audit.py`.
- Recurring: arm via the harness loop (ScheduleWakeup / cron) with this skill's
  `--once` behavior — one cycle per fire, re-arm only while the auditor exits 1.
- Cadence: a long interval (daily/weekly) is right; library drift is slow.

---

## Output (per tick)

```markdown
## Maintenance Tick — [date]
**Overview**: N skills (X first-party / Y bundled); auditor exit [0/1]
**Top finding**: [P-level] [finding]
**Action**: [evolved what] → PR #NN
**CI**: [green/pending]
**Re-arm**: [yes — M findings remain / no — clean]
```

---

## Rules

- **One focused fix per tick** — small reviewable PRs, never a mega-sweep.
- **Severity order** — P0 load-breakers before P4 cosmetics.
- **Validate YAML every time** — the auditor is the gate, not vibes.
- **Sync all four surfaces** — orchestrator, CLAUDE.md, skills.md, stacks.md.
- **Stop when clean** — re-arm only while the auditor exits 1.
- **Never bypass DiffGate; never auto-merge code logic.**
