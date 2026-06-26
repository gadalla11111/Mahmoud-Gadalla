---
name: orchestrator
description: >
  Meta-skill that reads the incoming task, selects the right skill(s) from the
  83-skill library, resolves conflicts when multiple skills match, chains them in
  the correct order, and applies quality gates — all while minimising token spend.
  Use whenever a task could benefit from a structured skill but the user has not
  named one. Trigger on: "best way to", "help me with", "what skill should I use",
  "orchestrate", or any open-ended task where skill selection is non-obvious.
  Also trigger when the task clearly spans two or more domains (e.g. "research
  and write a doc", "scan then fix", "spec then implement"). Skip only when the
  user has already named a specific skill to invoke.
allowed-tools: [Read, Glob, Grep, Bash, Task]
argument-hint: "<task description>"
auto-trigger:
  - ambiguous request spanning multiple skill domains
  - user asks 'what should I do about X' without specifying approach
  - task requires sequencing two or more skills
  - unclear which single skill applies
  - open-ended ask with no explicit skill named
do-not-trigger:
  - tasks clearly handled by one specific skill the user named
  - one-off tasks with no library match
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Orchestrator

One entry point for the full 83-skill library. Classify the task → resolve conflicts → select the minimum viable chain → execute with quality gates → report.

---

## Step 1 — Classify

Read the task. Identify:
- **Primary intent** — what the user wants produced
- **Domain signals** — keywords, file types, mentioned tools, platforms
- **Secondary intents** — quality gates, verification, documentation side-effects
- **Constraints** — "quick", "just X", explicit token budget, deadline pressure

Then match to the routing tables below.

---

## Step 2 — Resolve Conflicts

When two or more skills match, apply these tiebreakers in order:

1. **Specificity wins.** A domain-specific skill beats a general one. `sentry-fix-issues` beats `debug` for a Sentry error. `neon-postgres` beats `debug` for a Postgres connection issue.
2. **The more constrained skill wins.** If `expo-building-native-ui` matches, don't also invoke `frontend-design` — Expo has stricter rules (no Tailwind/CSS).
3. **Archetype determines order.** Judgment Amplifier skills (`sparc`, `adr`, `deep-research`) run before Workflow Automation skills (`tdd`, `yeet`, `docx`).
4. **When still ambiguous, invoke `promptize/promptize` first.** A clarifying question costs XS; a wrong chain costs L.

---

## Routing Table — Single-Skill Intents

### Memory & Session

| Intent signal | Skill | Tier |
|---|---|---|
| "catch me up" / "where did I leave off" / resume session | `engram/briefing` | XS |
| "checkpoint" / "save context" / session end | `engram/working` | XS |
| "consolidate notes" / "organize knowledge" / stale notes | `engram/consolidate` | S |

### Code Quality & Development

| Intent signal | Skill | Tier |
|---|---|---|
| Non-trivial feature / refactor / bug fix / API or schema change | `ultracode` | M–L |
| Build with Claude API / Anthropic SDK / model selection / tool use / MCP client | `claude-api` | M |
| Complex feature, uncertain requirements, high rework-risk | `sparc` | M–L |
| "ADR" / architecture decision / new tech adoption / API design | `adr` | S |
| "write tests" / TDD / red-green-refactor / regression prevention | `tdd` | M |
| "debug" / traceback / "why is X broken" / production incident (no Sentry) | `debug` | S |
| "what does this change affect" / ripple effect / before merging | `change-impact` | S |
| Every non-trivial code edit/review/refactor (background always-on) | `karpathy-guidelines` | XS |
| "build MCP server" / "create MCP tool" / expose X as MCP | `mcp-builder` | L |
| "debug MCP" / "inspect MCP repo" / MCP tool not showing up | `mcp-inspector` | M |
| "test the UI" / Playwright / browser automation / E2E tests | `webapp-testing` | M |
| "fix CI" / failing GitHub Actions checks on a PR / red checks | `gh-fix-ci` | M |
| "address the comments" / reviewer feedback on open PR | `gh-address-comments` | S |
| "ship it" / "yeet" / commit + push + open PR in one flow | `yeet` | XS |

### Sentry Observability

| Intent signal | Skill | Tier |
|---|---|---|
| "fix this Sentry issue" / production error via Sentry | `sentry-fix-issues` | M |
| "create a Sentry alert" / notify on errors/regressions | `sentry-create-alert` | S |
| Monitor AI agents / token/latency for Anthropic/OpenAI/LangChain | `sentry-setup-ai-monitoring` | M |
| Seer bug-prediction PR review pre-merge | `sentry-pr-code-review` | S |
| Add Sentry SDK to Python app (Django/Flask/FastAPI) | `sentry-python-setup` | S |

### Neon Postgres

| Intent signal | Skill | Tier |
|---|---|---|
| Neon serverless Postgres setup / connections / branching / scale-to-zero | `neon-postgres` | M |
| High Neon bill / cut Postgres egress / `pg_stat_statements` | `neon-postgres-egress-optimizer` | M |

### Terraform

| Intent signal | Skill | Tier |
|---|---|---|
| Write/review Terraform HCL / HashiCorp conventions | `terraform-style-guide` | S |
| Write/run `.tftest.hcl` tests / mock providers / assertions | `terraform-test` | M |
| Terraform Stacks / multi-env/region infra / `.tfcomponent.hcl` | `terraform-stacks` | L |

### Security Analysis (Trail of Bits)

| Intent signal | Skill | Tier |
|---|---|---|
| "scan this codebase" / parallel Semgrep static analysis / SARIF | `trailofbits/semgrep` | M |
| "run CodeQL" / deep interprocedural taint / data-flow analysis | `trailofbits/codeql` | L |
| API misuse / footgun design review / dangerous defaults | `trailofbits/sharp-edges` | M |

### Document & Content

| Intent signal | Skill | Tier |
|---|---|---|
| ".docx" / "Word document" / formatted report/contract | `docx` | S |
| ".pdf" / "create PDF" / formatted document needing PDF | `pdf` | S |
| "presentation" / "slide deck" / ".pptx" / PowerPoint | `pptx` | M |
| ".xlsx" / "Excel" / "spreadsheet" / tabular/financial data | `xlsx` | S |
| Collaborative multi-turn document writing / "let's write this together" | `doc-coauthoring` | M |
| Team announcement / internal memo / all-hands / incident comms | `internal-comms` | S |
| "write a PRD" / product requirements / pre-engineering feature spec | `prd-generator` | M |
| "handoff notes" / "what did we accomplish" / context switch | `handoff` | S |
| "make this sound human" / strip AI writing tells / "reads like ChatGPT" | `humanizer` | S |
| University course / syllabus / learning outcomes / exam / rubric / grading | `curriculum-builder` | M |

### Research & Verification

| Intent signal | Skill | Tier |
|---|---|---|
| "fact check" / "verify claims" / "source this" / QA grid / doc with cited stats | `fact-checker` | S–M |
| Complex multi-step research / due diligence / literature review | `deep-research` | L |
| Exhaustive search / prior searches insufficient / competitive research | `ultra-search` | L |
| "latest news" / current events / time-sensitive information | `news-research` | M |
| "substantiate this" / single-claim verification / "evidence for" | `prove-claims` | S |
| GEO / "SEO for AI search" / get cited by ChatGPT/Perplexity/AI Overviews | `claude-seo` | M |

### Design & Frontend

| Intent signal | Skill | Tier |
|---|---|---|
| UI component / React/Vue/Svelte/HTML / dashboard / Tailwind/shadcn | `frontend-design` | M |
| Visual design / layout / typography / colour / "make this look good" / unsure which design skill | `design` (router) | M |
| Brand consistency / "is this on-brand" / Anthropic visual identity | `brand-guidelines` | S |
| Static art / poster / print / .pdf/.png artwork | `canvas-design` | M |
| Slide deck narrative + visual structure / "design my presentation" | `presentation-architect` | M |
| Write HTML and render it to MP4/GIF/WebM video | `hyperframes` | M |
| "create a theme" / colour palette / design tokens / component theming | `theme-factory` | M |
| "generative art" / p5.js / flow field / code-driven visual output | `algorithmic-art` | M |
| Self-contained HTML artifact / single-file interactive tool/demo | `web-artifacts-builder` | M |
| "GIF for Slack" / animated gif / short looping team communication | `slack-gif-creator` | S |
| Add/compose shadcn/ui components / projects with `components.json` / Tailwind v4 | `shadcn` | M |
| Integrate Stripe payments/billing/Connect / API selection / restricted keys | `stripe` | M |
| EAS Build/Submit / App Store/Play Store / TestFlight / EAS Update OTA | `expo/expo-deployment` | M |
| Expo Router screens / navigation / native tabs / RN app UI | `expo/expo-building-native-ui` | M |

**Expo conflict rule:** If both `frontend-design` and `expo-building-native-ui` match, `expo-building-native-ui` wins — Expo RN uses inline styles, not CSS/Tailwind.

### Orchestration & Meta

| Intent signal | Skill | Tier |
|---|---|---|
| Ambiguous multi-domain / task spans 2+ skills / unclear routing | `orchestrator` (self — recurse after classify) | XS |
| Task too large for single turn / parallelisable subtasks / multi-domain delegation | `nested-subagents` | M |
| "add to queue" / backlog management / multi-step incremental project | `queue` | S |
| "create a new skill" / "add skill for X" / formalise recurring workflow | `skill-creator` | M |
| "is there a skill for X" / find & install a skill / discover capability | `find-skills` | S |

### Workflow & Process

| Intent signal | Skill | Tier |
|---|---|---|
| Small targeted edit / "just change X" / strict scope boundaries | `lazy-cat/surgical` | XS |
| Before any non-trivial implementation / "is there a simpler way" | `lazy-cat/think-twice` | XS |
| Ambiguous/multi-interpretation request / missing context changes approach | `promptize/promptize` | XS |
| "estimate cost" / "how many tokens" / pre-flight model selection | `sipcode/estimate` | XS |
| "where did my tokens go" / post-session forensics | `sipcode/why` | XS |
| "compress this prompt" / "cut the tokens" / trim model-facing context | `caveman` | XS |
| Before/after savings comparison / "is sipcode helping" | `sipcode/impact` | XS |
| "run the benchmark" / verify sipcode savings claim | `sipcode/benchmark` | XS |
| "audit CLAUDE.md" / large/conflicting instructions / new project onboarding | `claude-md-audit` | S |
| "audit instruction placement" / CLAUDE.md vs hooks vs skills confusion | `steering-lint` | S |

### Domain-Specific

| Intent signal | Skill | Tier |
|---|---|---|
| Arabic ministry proposal / وزارة / MBK/Jahizoon/MERIDIAN brand | `ministry-proposal` | L |
| Draft/review contracts, NDAs, policies, ToS / legal risk redline | `legal-practice` | M |

### Marketing & Brand Strategy

| Intent signal | Skill | Tier |
|---|---|---|
| Brand strategy / positioning / brand pyramid / value proposition / rebrand | `brand-framework` | M |
| LinkedIn strategy / personal brand / thought leadership / content calendar | `linkedin-branding` | M |
| Social media audit / channel review / benchmark vs competitors | `social-audit` | M |
| Create social posts / reel scripts / captions / multi-platform content | `social-content` | M |

**Brand routing rule:** `brand-framework` = strategy/positioning (what the brand *means*); `brand-guidelines`/`applying-brand-guidelines` = applying an existing visual identity (what it *looks like*); `ministry-proposal` = the MERIDIAN/Jahizoon ministry brand specifically.

### Finance & Brand

| Intent signal | Skill | Tier |
|---|---|---|
| Financial statements / ratio analysis / P/E, ROE, EBITDA, liquidity/leverage | `analyzing-financial-statements` | M |
| DCF / Monte Carlo / M&A, LBO / scenario planning / WACC | `creating-financial-models` | M–L |
| Any Acme Corp document / "brand compliant" / brand consistency check | `applying-brand-guidelines` | S |

---

## Multi-Skill Chains

Consult `.memory/stacks.md` for the full domain stack guides. Common chains:

| Scenario | Chain | Notes |
|---|---|---|
| New feature from scratch | `lazy-cat/think-twice` → `sparc` → `tdd` → `yeet` | Think first; never skip Phase 0 |
| Security-sensitive feature | `lazy-cat/think-twice` → `sparc` → `trailofbits/sharp-edges` → `tdd` → `yeet` | API design reviewed before code |
| Static analysis scan | `trailofbits/semgrep` → `trailofbits/codeql` → `sentry-fix-issues` | Broad scan → deep taint → fix |
| API/interface misuse review | `trailofbits/sharp-edges` → `adr` → `ultracode` | Footgun review → decision → implementation |
| Architecture change | `lazy-cat/think-twice` → `adr` → `change-impact` → `adr` (review) | Think first, record decision, screen ripple |
| Research-backed document | `deep-research` → `prove-claims` → `prd-generator` or `docx` | Verify before writing |
| Ministry proposal | `deep-research` → `ministry-proposal` → `fact-checker` | fact-checker is mandatory gate |
| Security audit | `trailofbits/semgrep` → `trailofbits/codeql` → `debug` → `ultracode` | Full sweep before fixes |
| Vulnerability investigation | `trailofbits/semgrep` or `trailofbits/codeql` → `debug` → `change-impact` → `ultracode` → `tdd` | Trace → isolate → fix → test |
| Releasing work | `change-impact` → `prove-claims` → `handoff` | Gate before hand-off |
| Search → publish | `ultra-search` or `news-research` → `prove-claims` → output skill | Never publish unverified claims |
| MCP eval | `mcp-inspector` → `mcp-builder` (if safe) | Inspect before build |
| Session start | `engram/briefing` → task-appropriate skill | Orient first |
| Overlong session | `engram/working` → continue | Checkpoint before context fills |
| Vague ask | `promptize/promptize` → re-classify → route | Clarify before routing |
| Expo mobile feature | `lazy-cat/think-twice` → `expo-building-native-ui` → `tdd` → `expo/expo-deployment` | No CSS/Tailwind in RN |
| Terraform infrastructure | `terraform-style-guide` → `terraform-stacks` → `terraform-test` | Style first, then structure, then tests |
| Neon high bill | `neon-postgres-egress-optimizer` → `neon-postgres` (reconfigure) | Diagnose before reconfigure |
| shadcn UI build | `shadcn` → `frontend-design` → `webapp-testing` | Components → layout → E2E |
| Stripe integration | `stripe` → `tdd` → `sentry-setup-ai-monitoring` | Integration → tests → observability |

---

## Token Tiers

| Tier | Approximate cost | When to use |
|---|---|---|
| XS | < 2K tokens | Status, checkpoint, routing, surgical edits |
| S | 2–8K | Single well-scoped action |
| M | 8–30K | Multi-step skill with output |
| L | 30–100K | Deep research, large SPARC cycles, Terraform Stacks |
| XL | > 100K | Only if justified; flag to user first |

Before starting any M+ chain, estimate total tier and state it. If the chain reaches XL, propose a scoped alternative and ask for confirmation.

---

## Steps 3–6: Execute, Gate, Report

### Step 3 — Estimate and Confirm (M+ chains only)

State the plan before executing:
```
Plan: deep-research → prove-claims → prd-generator
Estimated tier: L (~40–60K tokens)
Proceed? (y / adjust scope / swap to lighter alternative)
```
Skip confirmation for XS and S — just run.

### Step 4 — Execute

Run each skill in order. Pass outputs forward explicitly:
- Provide the prior skill's output as context to the next skill
- Do not re-derive what was already established
- If a skill exposes a `health.open_issues` list, address those issues as part of execution

### Step 5 — Quality Gate

After each skill completes:

| Skill type | Gate |
|---|---|
| Research | Every claim has a source URL; no unsupported assertions |
| Code | Tests pass; `karpathy-guidelines` satisfied; no scope creep |
| Documents | All section headings filled; no `<!-- TODO -->` placeholders |
| SPARC | Every AC has a corresponding test; traceability matrix complete |
| ADR | Status is accurate; alternatives are recorded |
| Security scan | Zero-findings result investigated — never assumed clean |
| Ministry proposal | `fact-checker` run; Arabic فصحى register; visual system consistent |
| Handoff | Incoming owner can restate scope and stop conditions |

If a gate fails, fix the gap before reporting completion.

### Step 6 — Report

```markdown
## Orchestrator Summary
**Task**: {original task description}
**Skills used**: {ordered list}
**Token tier**: {XS/S/M/L/XL} — estimated {N}K tokens
**Conflicts resolved**: {if any — which skills competed and why this one won}
**Quality gates**: {passed / failed items}
**Output**: {summary of what was produced}
**Next step**: {what the user should do now, if anything}
```

---

## Rules

- **Never add skills the task does not require.** A one-step task does not need a chain.
- **Classify before acting.** Even for obvious tasks, state the selected skill first.
- **Specificity beats generality.** Platform-specific skills override general ones.
- **Confirm before L or XL chains.** The user's token budget is not yours to spend.
- **Pass outputs forward, not sideways.** Each skill receives the prior skill's output as explicit context.
- **Quality gates are not optional.** A chain that skips gates produces unverified output faster, not better output.
- **When in doubt, promptize first.** An ambiguous task routed to the wrong skill wastes more than a brief clarification round.
- **Consult `.memory/stacks.md` for complex domains.** It contains full stack guides for Security, Testing, Coding, Research, and 16 other domains.
