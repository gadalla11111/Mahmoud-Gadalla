# ANA Blueprint — Autonomous Networked Agent

**Loop:** Extract → Apply → Assess → Merge to Evolve → Auto Trigger

This document is the unified doctrine binding `mahmoud-gadalla` (agents, skills, tools)
and `gate-repl` (belief-gate: completeness verification by execution) into one
self-evolving system.

**Iteration:** 6 — 2026-07-06 | Skills: 123 | External tools: ToolUniverse (1,000+) · ATHENA (212) · ARK · scientific-research (148) · ai-research (98) · open-design (100+ skills, 150 systems)

---

## The Core Principle (from gate-repl/UNIFICATION.md)

> A derived view is trustworthy only if it carries an arrow back to the source that
> produced it. Most LLM systems break precisely because the LLM erases the arrow.

The fix — in every layer — is the same shape:
**replace compression/judgment with structured declaration + deterministic checking.**

```
SOURCE  (DB, API, document, prior turns)
  │
  ▼
[0] TOOL LAYER     ← ToolUniverse: 1,000+ scientific APIs (AlphaFold, BLAST, DrugBank…)
  │
  ▼
[1] EXTRACTION     ← deterministic (parser, DB query, API — never LLM prose)
  │
  ▼
[2] VERIFICATION   ← belief-gate: required − present; never false-completes
  │
  ▼
[3] MEMORY         ← modality tag + provenance + invalidation (engram)
  │
  ▼
ACTION
```

---

## The Loop

### 1. Extract
Pull key patterns from every repo and session:
- gate-repl: `check_set`, `verify_coverage`, `run_with_repair`, incubation study results
- mahmoud-gadalla: agent patterns (skills, managed agents, tool use)
- Cross-session: engram memory (`.memory/`) snapshots

### 2. Apply
Wire belief-gate into agent actions:
- Use `beliefgate` skill (see `anthropic_skills/beliefgate/`) before any irreversible agent step
- Gate placement rule: **verify-on-novelty**, not deliberate-everywhere
- Feed `present` from structured sources; derive `required` from the task

### 3. Assess
Run deterministic benchmarks:
```bash
# gate-repl: completeness verification
python -m pytest gate-repl/dist/beliefgate/tests/ -q

# mahmoud-gadalla: skill library audit (drift detection)
pip install pyyaml -q && python misc/library_audit.py

# smoke tests
uv run python -m pytest misc/ -q 2>/dev/null || true
```
Verdict: COMPLETE (all required items verified) / INCOMPLETE (gap listed) / UNDECIDABLE.

### Library-Maintainer Loop (sub-loop)

Runs inside Step 3 when `library_audit.py` reports drift (exit 1):
```
OVERVIEW → EVALUATE → EVOLVE → MERGE → RE-ARM (only while drift exists)
```
- Drift classes: invalid YAML, missing health block, uneval'd skills (`pass_rate=null`), count mismatch, missing from routing surfaces
- Eval protocol: 5 adversarial cases/skill across ambiguous/boundary/wrong-domain/regression/edge
- Merge policy: supervised for logic changes; mechanical fixes (YAML, count) may auto-merge

### 4. Merge to Evolve
- Merge `claude/ana-blueprint-wkp95w` → `main` when assessment passes
- Tag the merge with the loop iteration number
- Update `.memory/` with what changed and why

### 5. Auto Trigger
GitHub Action (`ana-blueprint.yml`) fires on:
- Every push to `claude/ana-blueprint-wkp95w`
- Weekly schedule (Sunday 00:00 UTC) — the standing "evolve" cycle
- Manual dispatch

---

## Belief-Gate Integration for Agents

Install the skill from `anthropic_skills/beliefgate/SKILL.md`.

**Pattern for any agent action:**
```python
from beliefgate import check_set

def agent_step(task, context):
    required = derive_required(task)      # from the task statement
    present  = parse_present(context)     # from a parser/DB/API — never LLM prose
    gate = check_set(required, present)
    if not gate.ok:
        return request_missing(gate.missing)   # exact gap; never guess
    return take_action(task, context)
```

**Rule:** the gate only makes the recoverable error (refusing a valid action).
Taking action on incomplete data is often unrecoverable.

---

## Fixation Guard (from gate-repl/INCUBATION_FIXATION.md)

Novel structure triggers template-capture on fast LLM paths (System-1 trap).
CoT eliminates it universally (0/80 trap rate). One gate at the fixation point
rescues 100% of recursive chains (vs 62% without).

**Architectural rule:** place a gate at the first novel-structure step in any
multi-stage chain. Don't deliberate everywhere — deliberate where the fast path
is unreliable.

---

## Repos

| Repo | Role |
|---|---|
| `gadalla11111/mahmoud-gadalla` | Agent ecosystem: skills, managed agents, tools |
| `gadalla11111/gate-repl` | Completeness verification library + research |
| `mims-harvard/ToolUniverse` | Scientific tool layer: 1,000+ APIs via unified SDK + MCP server |
| `mims-harvard/ATHENA` | Treatment reasoning agent: 212 biomedical tools, 94.7% drug benchmark |
| `mims-harvard/gates-buildathon` | ARK: biomedical knowledge graph agent (natural language → graph queries) |
| `mims-harvard/Qworld` | LLM eval via recursive question expansion; 89% expert criteria coverage |
| `mims-harvard/MedLog` | Medical AI logging protocol: provenance + bias detection (9-field standard) |
| `alirezarezvani/claude-skills` | 355 SKILL.md skills: engineering, C-suite, research, compliance, marketing |
| `coreyhaines31/marketingskills` | 45+ marketing skills: CRO, SEO, email, launch, referrals, analytics |
| `ericosiu/ai-marketing-skills` | Python marketing pipelines: Growth Engine, Sales Pipeline, Content Ops |
| `twentyhq/twenty` | Open-source CRM (React/NestJS/PostgreSQL); self-hosted, extensible |
| `dubinc/dub` | Open-source link attribution: shortlinks, click tracking, affiliate mgmt |
| `mautic/mautic` | Open-source marketing automation: email, lead scoring, campaign builder |
| `matomo-org/matomo` | Open-source web analytics: self-hosted Google Analytics alternative |

**Branch:** `claude/ana-blueprint-wkp95w` in both gadalla11111 repos.

## ToolUniverse Integration

Install the skill from `anthropic_skills/tooluniverse/SKILL.md`.

**Pattern — scientific agent step with gate:**
```python
from tooluniverse import ToolUniverse
from beliefgate import check_set

tu = ToolUniverse()
tu.load_tools()

def scientific_step(task, context):
    required = extract_required(task)           # e.g. {"uniprot_id"}
    present  = set(context.keys())              # from structured source
    gate = check_set(required, present)
    if not gate.ok:
        return fetch_missing(gate.missing)
    return tu.get_tool(task.tool).run(context)
```

**MCP server:** run `tooluniverse-mcp` to expose all 1,000+ tools to Claude directly.
