# Claude Code Ecosystem — mined component catalog

**Date:** 2026-07-19
**Companion to:** `research/claude-code-ecosystem-scan-2026-07.md` (the survey). This doc is the **extraction**: the concrete components these 10 repos expose, consolidated + deduplicated, with a **lift list** for `ruflo` (agents) and the `qoder` plugins (skills).
**Depth & honesty:** compiled from the repos' **README/index level** (categories, counts, headline component names) — not a file-by-file clone of every agent/skill. Numbers are the repos' own claims; treat as indicative. Reliable star counts were **not obtainable** this run (`api.github.com` is proxy-blocked; the scoped GitHub tools only cover this repo), so this catalog leans on *what* each repo contains, not popularity.

---

## 1. Component tally (what each repo actually ships)

| Repo | Agents | Skills | Commands | Hooks | MCP configs | Other |
|---|---|---|---|---|---|---|
| `everything-claude-code` | 67 | 278 | `/plan`, `/code-review`, `/build-fix` (+legacy) | SessionStart/End, pre/post-edit, memory | GitHub, Supabase, Vercel, Context7 | language rules (TS/Py/Go/Swift/PHP/Java); CLAUDE.md examples (SaaS/Go/Django/Laravel/Rust) |
| `awesome-claude-code-subagents` (VoltAgent) | **154+** (10 categories) | — | — | — | — | markdown agent defs w/ frontmatter (name/description/tools/model) |
| `awesome-claude-code-toolkit` (rohitg00) | 135 (10 categories) | 35 (+SkillKit marketplace) | 42 | 20 | 14 | 176+ plugins, 15 rules, 7 templates |
| `claude-code-templates` (davila7) | ✓ | ✓ | ✓ | ✓ | ✓ | 100+ installable components via CLI + web (aitmpl.com); analytics/monitor |
| `awesome-claude-skills` (travisvn) | — | official + community | — | — | — | documents SKILL.md frontmatter + progressive disclosure |
| `awesome-claude-code` (hesreallyhim) | index | index | index | index | index | the 20+-category master index |
| `claude-code-ultimate-guide` | patterns | patterns | patterns | patterns | **28-CVE MCP vetting DB** | 275 templates, 48 diagrams, 374-q quiz |
| `learn-claude-code` (shareAI-lab) | — | — | — | — | — | 20-chapter "build a harness from 0→1" (EN/JP/CN) |
| `anthropics/claude-code` | official format | official format | official format | official format | official format | **source of truth**; core CLI closed-source |
| `get-shit-done` | — | — | — | — | — | SDD/meta-prompting framework — **ARCHIVED** (→ `gsd-core`) |

*Heavy overlap:* the four component collections (everything-claude-code / VoltAgent / toolkit / templates) re-aggregate largely the **same** agents/skills. Pull from **one**, not four.

---

## 2. Subagents → `ruflo` agent definitions

Both VoltAgent (154+) and the toolkit (135) organize agents into the **same 10 categories** — a de-facto taxonomy worth aligning `ruflo`'s agents to:

1. Core Development · 2. Language Specialists · 3. Infrastructure · 4. Quality & Security · 5. Data & AI · 6. Developer Experience · 7. Specialized Domains · 8. Business & Product · 9. Meta & Orchestration · 10. Research & Analysis

**Format match:** each subagent is a markdown file with frontmatter (`name`, `description`, `tools`, model routing) + a system prompt — the **same shape `ruflo`'s Claude Code plugins already use**, so adaptation is copy-and-retune, not rewrite.

**Lift list (highest-value agents to adapt into `ruflo` first):**
- `code-reviewer`, `security-reviewer` — map onto `ruflo-security-audit` / review flows.
- `planner` / architecture agents — feed `ruflo`'s anti-drift planning swarm.
- Language specialists (TS/Py/Go/Rust/…) — `ruflo` is TS + Rust + Python; these slot straight in.
- Meta & Orchestration agents — closest to `ruflo`'s swarm-coordination role; compare against its 60+ existing agents to fill gaps, not duplicate.

**Source of record:** `VoltAgent/awesome-claude-code-subagents` (vendor-neutral, markdown, installable) is the cleanest single source; `everything-claude-code` is a fallback (verify its stats/licensing).

---

## 3. Skills → the `qoder` plugins (SKILL.md)

`awesome-claude-skills` documents the **official SKILL.md format** (`name`/`description` frontmatter + progressive disclosure + optional `scripts/`/`references/`) — **exactly the `skills/<name>/SKILL.md` shape the qoder plugins use.** Official skill families worth mirroring:

- **Document** — `docx`, `pdf`, `pptx`, `xlsx`. **Direct fit** for the doc-heavy qoder plugins (contract-management, corporate-finance-tax, equity-research, investment-banking) whose inputs/outputs are Office/PDF.
- **Design & Creative** — `algorithmic-art`, `canvas-design` → the `product-design` / `marketing` qoder plugins.
- **Development** — `frontend-design`, `web-artifacts-builder`, `mcp-builder` → general tooling (you already used `mcp-builder` to build the crawl4ai PoC).
- **Communication** — `brand-guidelines`, `internal-comms` → `marketing` / `consulting-delivery`.

**Lift action:** for each doc-heavy qoder plugin, cross-check its skills against the official `docx`/`pdf`/`xlsx` skills — adopt their progressive-disclosure structure and any scripts, keeping the plugin's Chinese-first content.

---

## 4. Commands / hooks / MCP (secondary but useful)

- **Slash commands:** `/plan`, `/code-review`, `/build-fix` recur — reference implementations for `ruflo`'s command surface.
- **Hooks:** the common pattern is **SessionStart/SessionEnd + pre/post-edit + memory persistence** — mirrors `ruflo`'s hooks/`.harness` and the (removed) ANA-Blueprint memory idea. Good template for session-scoped memory.
- **MCP configs:** GitHub, Supabase, Vercel, **Context7** recur as the "default" server set. Context7 (docs retrieval) is the notable add for a coding harness.
- **Security:** the ultimate-guide's **28-CVE MCP vetting database** is the one genuinely differentiated asset here — consult it before wiring any new MCP server into `ruflo`/`qoder`.

---

## 5. Cautions

- **Dedup hard.** Adopting multiple mega-collections just copies the same files under different licenses. One agent source + one skills source is enough.
- **Provenance / licensing varies** (Apache-2.0 on some, unstated on others; community-aggregated). Check each component's origin before vendoring into `ruflo`/`qoder`.
- **`ruflo` is upstream-tracking.** Per its CLAUDE.md, local additions can be overwritten on the next bulk re-sync — if you adapt agents into `ruflo/`, make that explicit in the commit and expect to re-apply, or keep adapted agents in a separate first-party location.
- **GSD is archived** — take patterns from `gsd-core`, not the frozen tree.

## 6. Concrete next actions (pick one)

1. **Adapt a starter set of ~10 subagents** from VoltAgent into first-party `ruflo` agent definitions (code-reviewer, security-reviewer, planner, + language specialists), matching `ruflo`'s existing agent frontmatter.
2. **Skill audit:** map each doc-heavy qoder plugin's skills against the official `docx`/`pdf`/`xlsx` skills and note gaps.
3. **MCP shortlist:** adopt Context7 + the ultimate-guide's CVE-vetting checklist as the default "safe MCP" set for the repo.

---

*Scope: reference research only — none of these repos or components are vendored or integrated here yet. Extraction companion to the ecosystem survey. The "next actions" above are the point where mining turns into actual first-party artifacts — say which and I'll build it.*
