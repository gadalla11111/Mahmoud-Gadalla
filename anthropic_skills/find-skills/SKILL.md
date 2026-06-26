---
name: find-skills
description: >
  Discovers and installs skills. Use when a user wants a capability and isn't
  sure whether a skill for it already exists — searches this library first, then
  known external skill repos, and either routes to the existing skill or scaffolds
  a new one. Trigger on: "is there a skill for X", "find a skill that", "install a
  skill for", "what skill does Y", "do we have a skill to". Archetype: Interface
  Adapter. Differs from orchestrator (which routes among KNOWN skills for a task);
  find-skills DISCOVERS whether a skill exists at all and installs it.
allowed-tools: [Read, Glob, Grep, WebSearch, WebFetch, Bash, Write]
argument-hint: "<capability you want> [--search | --install <name>]"
auto-trigger:
  - "is there a skill for"
  - "find a skill that does"
  - "install a skill for"
  - "do we have a skill to"
  - discovering whether a capability already exists before building it
do-not-trigger:
  - routing among skills already known to apply (use orchestrator)
  - authoring a brand-new skill from a clear spec (use skill-creator)
  - using a skill the user already named
health:
  last_eval: 2026-06-26
  pass_rate: 0.9
  trigger_accuracy: 0.9

  open_issues:
    - discovery-vs-routing overlap with orchestrator on open-ended 'what should I do'
---

# Find Skills

Finds the skill you need — in this library or beyond — and installs it. The discovery layer in front of `orchestrator` (routes known skills) and `skill-creator` (builds new ones).

---

## Decision Flow

```
What capability do you want?
        │
        ▼
1. Search THIS library  ──found──►  route to it (hand to orchestrator)
        │ not found
        ▼
2. Search external skill repos ──found──►  install + adapt (see Install)
        │ not found
        ▼
3. No skill exists ──►  hand to skill-creator to build one
```

Never jump to building before searching — the cheapest skill is one that already exists.

---

## Step 1 — Search This Library

```
Grep the library for the capability:
  - rg -i "<keywords>" anthropic_skills/*/SKILL.md
  - check .memory/skills.md index (the composition graph)
  - check the orchestrator routing tables
```

Match on intent, not exact words — "make a video" should find `hyperframes` even if it doesn't say "video" in the name. Report the top 1–3 candidates with their trigger lines.

---

## Step 2 — Search External Repos

If nothing local fits, search known skill sources:

| Source | What it has |
|---|---|
| Official Anthropic skills | document, design, research, dev skills |
| Vendor repos (Sentry, Neon, Terraform, Stripe, Expo, shadcn) | tool-specific skills |
| openai/skills `.curated` | GitHub CI / workflow skills |
| skills.sh / agentskills.io | community skill directory |

Use WebSearch/WebFetch to confirm a candidate exists and read its `SKILL.md` before proposing it.

---

## Step 3 — Install

To install an external skill into this library:

1. Fetch its `SKILL.md` (and any bundled `reference/`, `scripts/`)
2. Place under `anthropic_skills/<name>/`
3. **Normalize to house format**: ensure `auto-trigger`/`do-not-trigger` are valid YAML (one phrase per item) and add a `health:` block
4. Preserve upstream `license:` line if present (marks it bundled)
5. Update the routing surfaces — `.memory/skills.md`, `.memory/stacks.md`, `orchestrator`, `CLAUDE.md` — so it's reachable
6. Verify the frontmatter parses as valid YAML before committing

```bash
python3 -c "import yaml,sys;yaml.safe_load(open('anthropic_skills/<name>/SKILL.md').read().split('---')[1]);print('valid')"
```

---

## Step 4 — Or Build New

If no skill exists anywhere, hand the capability to `skill-creator` with the discovery notes (what you searched, what was close-but-not-right). Don't reinvent — give skill-creator the gap analysis.

---

## Output Format

```markdown
## Skill Search: "<capability>"

### In this library
| Skill | Match | Trigger line |

### External candidates
| Skill | Source | URL | Fit |

### Recommendation
- [ROUTE to <existing>] / [INSTALL <external>] / [BUILD via skill-creator]
- Why: ...
```

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| A matching skill exists and the task is ready to run | `orchestrator` |
| No skill exists — build one | `skill-creator` |
| Installed skill needs trigger tuning | `skill-creator` (optimize description) |
| Verify an external skill's claims/provenance | `fact-checker` |

---

## Rules

- **Search before build** — local library, then external, then create. Never skip to creation.
- **Match on intent, not name** — the right skill may not contain the user's words.
- **Normalize on install** — valid YAML + health block + routing-surface updates, every time.
- **Hand gaps to skill-creator** — with discovery notes, not a cold start.
- **Don't duplicate** — if a skill is 80% right, route + suggest evolving it, don't clone it.
