# Claude Code Ecosystem — scan of 10 repos

**Date:** 2026-07-19
**Method:** one WebFetch per repo (public GitHub landing page + README).
**⚠ Star counts are approximate and shaky** — WebFetch misreads them. Treat every number below as "order of magnitude," and note `affaan-m/everything-claude-code`'s reported ~212k is almost certainly a misread (that would be a top-20 repo on all of GitHub) — flagged as **unverified**.
**Lens:** these are all **Claude Code ecosystem** resources (awesome-lists, guides, component toolkits, the official repo). Evaluated for *what they contain* (subagents / skills / commands / hooks / MCP / CLAUDE.md patterns) and how they feed **`ruflo`** (a Claude Code meta-harness with agents/plugins/skills), the **`qoder`** plugins (SKILL.md skills), and this repo's own CLAUDE.md work.
**See also:** the two companion scans — `research/ai-agent-tooling-scan-2026-07.md` and `research/web-scraping-tooling-scan-2026-07.md`.

---

## At a glance

| Repo | Type | Stars≈ | Contains | Fit |
|---|---|---|---|---|
| `anthropics/claude-code` | Official repo | ~138k | Issues/docs/plugins/devcontainers; **core CLI closed-source** (npm/brew) | ★★★ ground truth for features/formats |
| `shareAI-lab/learn-claude-code` | Learning (build-a-harness) | ~71k | 20-chapter "build a nano Claude-Code harness from 0→1"; EN/JP/CN | ★★★ the conceptual manual for what `ruflo` *is* |
| `hesreallyhim/awesome-claude-code` | Awesome-list (index) | ~50k | 20+ categories: skills, MCP, plugins, hooks, guides | ★★★ the master discovery index |
| `VoltAgent/awesome-claude-code-subagents` | Subagent collection | ~24k | **154+ subagents**, 10 categories, markdown+frontmatter | ★★★ mine for `ruflo` agent defs |
| `davila7/claude-code-templates` | CLI installer + templates | ~30k | CLI + web browser (aitmpl.com), 100+ components, analytics | ★★☆ fastest way to pull components |
| `travisvn/awesome-claude-skills` | Skills awesome-list | ~14k | Curated Skills (SKILL.md), official + community | ★★☆ maps to `qoder` SKILL.md |
| `affaan-m/everything-claude-code` | Component mega-kit | **unverified** | 67 agents, 278 skills, hooks, rules, MCP; multi-harness | ★★☆ big but overlaps; verify stats |
| `rohitg00/awesome-claude-code-toolkit` | Toolkit / list | ~2.4k | 135 agents / 35 skills / 42 commands / plugins / hooks | ★★☆ another mega-index; heavy overlap |
| `FlorianBruniaux/claude-code-ultimate-guide` | Guide + templates | ~5.5k | 24k-line guide, 275 templates, quiz, **MCP CVE tracking** | ★★☆ CLAUDE.md + security patterns |
| `gsd-build/get-shit-done` | Workflow framework | ~65k(?) | Meta-prompting / spec-driven dev system — **ARCHIVED Jun 2026** | ★☆☆ moved to `gsd-core`; look there |

---

## By type

### Official (the source of truth)

**`anthropics/claude-code` — official repo, core CLI closed-source.** Public issue tracker, docs, plugins, devcontainers, examples; the CLI itself ships via npm/brew/installers. Everything the rest of this list orbits.
→ *Fit:* track it for **format/feature changes** (skills, plugins, hooks, subagents) that `ruflo` and the `qoder` plugins are built on. When a format shifts here, your downstream conventions follow.

### Learning / "how the harness works"

**`shareAI-lab/learn-claude-code` — "Bash is all you need", 20-chapter build-a-harness tutorial (EN/JP/CN).** Teaches *harness engineering* — building the tools/memory/permissions/coordination around a model — one mechanism per chapter, from tool dispatch to multi-agent + MCP.
→ *Fit:* **the single most relevant repo here.** Its thesis ("agency comes from the model; the harness is everything else") is *literally `ruflo`'s* own framing ("Agent = Model + Harness"). Read it as the conceptual manual for what `ruflo` is doing, and the CN content fits your bilingual work.

**`FlorianBruniaux/claude-code-ultimate-guide` — 24k-line guide + 275 templates + a 374-question quiz.** Architecture-first: agents, skills, hooks, CLAUDE.md best practices, TDD/SDD/BDD, and a **security angle (28 CVEs tracked, MCP vetting)**.
→ *Fit:* reference for **CLAUDE.md patterns** (directly relevant to the CLAUDE.md you maintain here) and for **MCP security** before wiring new servers into `ruflo`/`qoder`.

### Curated indexes (browse, don't clone)

**`hesreallyhim/awesome-claude-code` — the canonical index, 20+ categories.** Skills, MCP servers, plugins, hooks, observability, multi-agent patterns, progressive learning paths.
→ *Fit:* **bookmark as the master index.** Start here to discover anything Claude-Code, then go to the specific repo.

**`VoltAgent/awesome-claude-code-subagents` — 154+ subagents across 10 domains.** Each is a markdown file with frontmatter (name, description, tools, model routing) + a system prompt.
→ *Fit:* a direct **mine for `ruflo` agent definitions** — the frontmatter+prompt shape matches Claude Code's subagent format `ruflo` already uses. Lift/adapt rather than author from scratch.

**`travisvn/awesome-claude-skills` — curated Skills (SKILL.md), official + community.** Documents the SKILL.md frontmatter + progressive-disclosure format; nascent (Skills launched late 2025).
→ *Fit:* maps onto the **`qoder` plugins' `skills/<name>/SKILL.md`** shape — a source of skill patterns and a reference for the official skill format.

### Component toolkits / installers

**`davila7/claude-code-templates` — a CLI installer + web browser (aitmpl.com), 100+ components.** Installs agents/commands/MCPs/settings/hooks/skills; adds analytics, a conversation monitor, health checks.
→ *Fit:* the **practical "pull components into a project fast"** tool — useful for bootstrapping, and the analytics/monitor angle rhymes with `ruflo`'s `cognitum-analytics`.

**`affaan-m/everything-claude-code` — a component mega-kit (67 agents, 278 skills, hooks, rules, MCP), multi-harness (Claude Code/Cursor/Codex).** ⚠ Reported stars are **implausible — verify before citing.**
**`rohitg00/awesome-claude-code-toolkit` — 135 agents / 35 skills / 42 commands / 176+ plugins / hooks / rules / MCP configs, 10 agent categories.**
→ *Fit (both):* large ready-made component collections that overlap heavily with each other **and** with the VoltAgent/skills lists above. Useful as bulk sources, but **don't adopt more than one** — the redundancy is high and provenance/licensing varies.

### Workflow framework

**`gsd-build/get-shit-done` — meta-prompting / spec-driven-dev system for Claude Code. ARCHIVED (Jun 2026).** Active development moved to the Open GSD repo (`gsd-core`).
→ *Fit:* if spec-driven workflows interest you, evaluate **`gsd-core`**, not this archived tree. The SDD approach is complementary to `ruflo`'s SPARC methodology.

---

## Cross-cutting signals

- **Massive overlap.** At least four of these (VoltAgent, everything-claude-code, the toolkit, templates) re-aggregate the *same* agents/skills/commands/hooks. Pick **one index** (hesreallyhim) + **one component source** — cloning several just duplicates files.
- **Two mineable component types for you:** *subagents* (markdown + frontmatter → `ruflo` agents) and *skills* (SKILL.md → `qoder` plugins). Everything else (hooks, commands, MCP configs) is secondary.
- **The harness framing is shared.** `learn-claude-code` and `ruflo` independently land on "Agent = Model + Harness." That alignment makes learn-claude-code the best conceptual companion to `ruflo` in this batch.
- **Freshness varies:** `awesome-claude-skills` is nascent (Skills only launched late 2025); **GSD is archived** (→ gsd-core); the rest are actively maintained.
- **Trust the official repo over the lists** for formats — `anthropics/claude-code` is ground truth; the community kits lag and drift.

## Recommendation (what to actually do)

1. **`hesreallyhim/awesome-claude-code`** — bookmark as your master index; browse, don't clone.
2. **`shareAI-lab/learn-claude-code`** — read it; it's the conceptual manual for `ruflo`-style harness engineering (and it's translated).
3. **`VoltAgent/.../subagents` + `travisvn/awesome-claude-skills`** — mine for `ruflo` agent defs and `qoder`-adjacent SKILL.md patterns.
4. **`davila7/claude-code-templates`** — the installer to pull components fast when bootstrapping.
5. **`anthropics/claude-code`** — watch for official format/feature changes your stack depends on.
6. **`ultimate-guide`** — CLAUDE.md + MCP-security reference.
7. everything-claude-code / toolkit / GSD — bulk collections (verify stats / dedupe) and an archived framework (use gsd-core).

---

*Scope: reference research only — none of these repos are vendored, integrated, or built here. Third of three companion scans in `research/`. Open follow-ups: deep-dive any single repo, or actually mine one (e.g. adapt N subagents into `ruflo` agent definitions, or catalog SKILL.md patterns for the qoder plugins).*
