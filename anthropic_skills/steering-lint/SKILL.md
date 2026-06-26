---
name: steering-lint
description: >
  Audits Claude Code and coding-agent configurations to ensure instructions live
  in their correct "homes" — the right steering mechanism (CLAUDE.md, rules,
  skills, subagents, hooks, output styles) — based on load timing, context cost,
  authority, and compaction behavior. Read-only: reports misplaced instructions
  without editing. Use when onboarding a project, when CLAUDE.md feels bloated, or
  when automation/guardrails are written as prose instead of hooks.
allowed-tools: [Read, Glob, Grep, Bash]
argument-hint: "[paths to audit, or blank for project + user config]"
auto-trigger:
  - "audit instruction placement"
  - "is this in the right place"
  - CLAUDE.md vs hooks vs skills confusion
  - automation or prohibitions written as prose instead of hooks/permissions
  - long-session or prompt-injection robustness review of config
do-not-trigger:
  - auditing CLAUDE.md content quality only (use claude-md-audit)
  - editing configuration files (this skill is read-only)
  - general code review
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# steering-lint SKILL.md

This skill audits Claude Code and coding-agent configurations to ensure instructions live in their correct "homes" — the right steering mechanisms (CLAUDE.md, rules, skills, subagents, hooks, output styles) — based on load timing, context cost, authority, and compaction behavior.

## Core Purpose

The linter reads configurations and reports misplaced instructions without editing files. It surfaces problems that hide during normal use but emerge in long sessions, prompt injections, or context limits — such as always-loaded files carrying occasional procedures or narrow path-specific rules lacking scope declarations.

## Process (3-Step Checklist)

**1. Scope**: Decide which files to audit (project config, user-level, or explicit paths), then run the bundled scanner to inventory all memory files, rules, skills, subagents, and output styles.

**2. Classify**: Examine each surface and assign one status:
- **clean** — correctly placed
- **finding** — misplaced; record rule ID, title, location, instruction, why-axis, target home, and fix
- **cleared** — borderline but correctly placed; add a one-line note

**3. Report**: Assemble findings into JSON and render via `render_report.py` (or fall back to Markdown template). Do not edit any audited file.

## Key Rules (7 Total)

**High severity**: automation-as-prose (deterministic actions need hooks, not prose), prohibition-as-prose (guardrails require PreToolUse hooks or permissions), procedure-in-memory (runbooks belong in skills, not always-loaded files).

**Medium severity**: unscoped-narrow-rule (path-specific rules need `paths:` frontmatter), personal-pref-in-shared (personal taste belongs in user-level files), memory-bloat (keep root files lean), output-style-overreach (custom styles should preserve coding defaults or use append-system-prompt).

**Low severity**: skill-vs-subagent-mismatch (isolation determines the boundary — isolated side tasks become subagents, steerable procedures stay as skills).

## Output

A rendered HTML report listing findings in severity order with location, instruction excerpt, misplacement axis, recommended home, and concrete fix — plus a summary of scanned surfaces and clean surfaces. If Python is unavailable, output Markdown.
