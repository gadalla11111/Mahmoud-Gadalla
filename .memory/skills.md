# Skill Library — Knowledge Checkpoint
**Last updated**: 2026-06-26
**Source**: anthropic_skills/ + skills/custom_skills/ (main branch)

---

## Library Stats
- **Total skills**: 68 (61 in anthropic_skills/ + 4 sipcode sub-skills + 3 in skills/custom_skills/)
- **Newest**: Expo mobile (2: expo-deployment, expo-building-native-ui) under anthropic_skills/expo/ — from expo/skills
- **Prior**: stripe-best-practices under anthropic_skills/stripe/ — from stripe/ai; consults Stripe MCP planner when available
- **Prior**: shadcn (shadcn/ui component management) under anthropic_skills/shadcn/ — from shadcn-ui/ui
- **Prior**: Terraform IaC trio (style-guide, test, stacks) under anthropic_skills/terraform/ — from hashicorp/agent-skills
- **Prior**: Neon Postgres (2: neon-postgres, neon-postgres-egress-optimizer) under anthropic_skills/neon/
- **Prior**: Sentry observability suite (5) under anthropic_skills/sentry/ — requires Sentry MCP
- **Prior**: gh-fix-ci, gh-address-comments, yeet (GitHub CI trio, from openai/skills .curated, adapted for github MCP tools)
- **All skills have**: `auto-trigger` + `do-not-trigger` frontmatter
- **Auto-apply rule**: Skills trigger automatically by context — no explicit invocation needed

---

## Skill Index

### Memory & Session
| Skill | Path | Auto-triggers on |
|---|---|---|
| briefing | `engram/briefing` | "catch me up", returning after a break, start of ongoing project session |
| consolidate | `engram/consolidate` | "consolidate knowledge", stale/duplicated notes, pre-handoff cleanup |
| working | `engram/working` | "checkpoint", session end, mid-task pause, context switch |

### Code Quality & Development
| Skill | Path | Auto-triggers on |
|---|---|---|
| **ultracode** | `ultracode` | Any non-trivial feature, refactor, bug fix, API/schema/security change |
| claude-api | `claude-api` | Building with Claude/Anthropic SDK, model selection, tool use, MCP |
| sparc | `sparc` | Complex new feature, uncertain requirements, high rework-risk tasks |
| adr | `adr` | Significant architectural decision, new tech adoption, API/data model changes |
| tdd | `tdd` | Writing tests, "test first", red-green-refactor, regression prevention |
| debug | `debug` | Error/traceback investigation, "why is X broken", production incident |
| change-impact | `change-impact` | Before merging, "what does this break", shared module refactor |
| karpathy-guidelines | `karpathy-guidelines` | Every non-trivial code edit/review/refactor (always active on code) |
| mcp-builder | `mcp-builder` | "create MCP server", expose X as MCP tool |
| mcp-inspector | `mcp-inspector` | "debug MCP", MCP server not working, tool not showing up |
| webapp-testing | `webapp-testing` | Playwright/browser automation, "test the UI", E2E tests |
| gh-fix-ci | `gh-fix-ci` | "fix CI", failing GitHub Actions checks on a PR, autofix red checks |
| gh-address-comments | `gh-address-comments` | "address the comments", reviewer feedback on the open PR |
| yeet | `yeet` | "yeet", "ship it", commit + push + open a draft PR in one flow |
| sentry-fix-issues | `sentry/sentry-fix-issues` | "fix this Sentry issue", debug production error via Sentry MCP |
| sentry-create-alert | `sentry/sentry-create-alert` | "create a Sentry alert", notify on errors/regressions |
| sentry-setup-ai-monitoring | `sentry/sentry-setup-ai-monitoring` | monitor AI agents, token/latency for Anthropic/OpenAI/LangChain |
| sentry-pr-code-review | `sentry/sentry-pr-code-review` | Seer bug-prediction PR review pre-merge |
| sentry-python-setup | `sentry/sentry-python-setup` | add Sentry SDK to a Python app (Django/Flask/FastAPI) |
| neon-postgres | `neon/neon-postgres` | Neon serverless Postgres setup, connections, branching, scale-to-zero |
| neon-postgres-egress-optimizer | `neon/neon-postgres-egress-optimizer` | high Neon bill, cut Postgres egress via pg_stat_statements |
| terraform-style-guide | `terraform/terraform-style-guide` | write/review Terraform HCL per HashiCorp conventions |
| terraform-test | `terraform/terraform-test` | write/run `.tftest.hcl` tests, mock providers, assertions |
| terraform-stacks | `terraform/terraform-stacks` | Terraform Stacks, multi-env/region infra, `.tfcomponent.hcl`/`.tfdeploy.hcl` |

### Document & Content Generation
| Skill | Path | Auto-triggers on |
|---|---|---|
| docx | `docx` | ".docx", "Word document", formatted report/contract |
| pdf | `pdf` | ".pdf", "create PDF", formatted document needing PDF format |
| pptx | `pptx` | "presentation", "slide deck", ".pptx", PowerPoint/Keynote output |
| xlsx | `xlsx` | ".xlsx", "Excel", "spreadsheet", tabular data/financial model |
| doc-coauthoring | `doc-coauthoring` | Collaborative multi-turn document writing, "lets write this together" |
| internal-comms | `internal-comms` | Team announcement, internal memo, all-hands, incident comms |
| prd-generator | `prd-generator` | "write a PRD", product requirements, pre-engineering feature spec |
| handoff | `handoff` | Session end, "handoff notes", "what did we accomplish", context switch |

### Research & Verification
| Skill | Path | Auto-triggers on |
|---|---|---|
| **fact-checker** | `fact-checker` | Any doc with stats/cited claims, "verify", "fact check", before finalising proposals |
| deep-research | `deep-research` | Complex multi-step research, due-diligence, literature review |
| ultra-search | `ultra-search` | Exhaustive search needed, prior searches insufficient, competitive research |
| news-research | `news-research` | Current events, "latest news on", time-sensitive information |
| prove-claims | `prove-claims` | "substantiate this", single-claim verification, "source this" |

### Design & Frontend
| Skill | Path | Auto-triggers on |
|---|---|---|
| frontend-design | `frontend-design` | UI component, React/Vue/Svelte/HTML, dashboard, Tailwind/shadcn |
| design | `design` | Visual design task, layout/typography/colour decisions, "make this look good" |
| brand-guidelines | `brand-guidelines` | Brand consistency check, "is this on-brand", visual identity work |
| canvas-design | `canvas-design` | HTML canvas, Fabric.js/Konva, interactive drawing/whiteboard |
| theme-factory | `theme-factory` | "create a theme", colour palette, design tokens, component theming |
| algorithmic-art | `algorithmic-art` | "generative art", "p5.js", "flow field", code-driven visual output |
| web-artifacts-builder | `web-artifacts-builder` | Self-contained HTML artifact, single-file interactive tool/demo |
| slack-gif-creator | `slack-gif-creator` | "gif for Slack", animated gif, short looping team communication |
| shadcn | `shadcn` | add/compose shadcn/ui components, projects with components.json, Tailwind v4 |
| stripe-best-practices | `stripe` | integrate Stripe payments/billing/Connect, API selection, restricted keys |
| expo-deployment | `expo/expo-deployment` | EAS Build/Submit, App/Play Store, TestFlight, EAS Update OTA |
| expo-building-native-ui | `expo/expo-building-native-ui` | Expo Router screens, navigation, native tabs, RN app UI |

### Orchestration & Meta
| Skill | Path | Auto-triggers on |
|---|---|---|
| orchestrator | `orchestrator` | Ambiguous multi-domain request, task spans 2+ skills, unclear routing |
| nested-subagents | `nested-subagents` | Task too large for single turn, parallelisable subtasks, multi-domain delegation |
| queue | `queue` | "add to queue", backlog management, multi-step incremental project |
| skill-creator | `skill-creator` | "create a new skill", "add skill for X", formalise recurring workflow |

### Workflow & Process
| Skill | Path | Auto-triggers on |
|---|---|---|
| lazy-cat/surgical | `lazy-cat/surgical` | Small targeted edit, "just change X", strict scope boundaries |
| lazy-cat/think-twice | `lazy-cat/think-twice` | Before any non-trivial implementation, "is there a simpler way" |
| promptize/promptize | `promptize/promptize` | Ambiguous/multi-interpretation request, missing context changes approach |
| sipcode | `sipcode` | "how much will this cost", token estimate, before L/XL task chains |
| sipcode/estimate | `sipcode/estimate` | Pre-flight cost prediction — "estimate the cost", model selection question |
| sipcode/why | `sipcode/why` | Post-session forensics — "where did my tokens go", "why was that so expensive" |
| sipcode/impact | `sipcode/impact` | Before/after A/B savings comparison — "is sipcode saving me tokens" |
| sipcode/benchmark | `sipcode/benchmark` | Reproducibility proof — "run the benchmark", verify headline savings claim |
| claude-md-audit | `claude-md-audit` | "audit CLAUDE.md", large/conflicting instructions, new project onboarding |
| steering-lint | `steering-lint` | "audit instruction placement", CLAUDE.md/rules/hooks may be misplaced |

### Domain-Specific
| Skill | Path | Auto-triggers on |
|---|---|---|
| **ministry-proposal** | `ministry-proposal` | Arabic ministry doc (وزارة), MBK/Jahizoon/MERIDIAN brand, 15-slide schema |

### Finance & Brand (skills/custom_skills/)
| Skill | Path | Auto-triggers on |
|---|---|---|
| analyzing-financial-statements | `skills/custom_skills/analyzing-financial-statements` | Financial statement data, ratio requests (P/E, ROE, EBITDA, liquidity/leverage) |
| creating-financial-models | `skills/custom_skills/creating-financial-models` | DCF, Monte Carlo, M&A/LBO, scenario planning, WACC, enterprise value |
| applying-brand-guidelines | `skills/custom_skills/applying-brand-guidelines` | Any Acme Corp document, "brand compliant", brand consistency check |

---

## Key Facts

### ministry-proposal
- Two visual systems: MERIDIAN (`#0E0E0E` black dominant) · Jahizoon (`#1C2B45` navy dominant)
- Primary QA baseline: `MBK_Jahizoon_MoSS_AR_v2.pdf`
- 15-slide schema from `Generic_Issue.pptx`
- `fact-checker` is mandatory pre-finalization gate
- Arabic فصحى register required

### fact-checker
- 3× rule: every claim needs 3 independent sources from different organisations
- Pre-verified Jahizoon stats: 41.5% graduate unemployment (CAPMAS Q1 2026), ~7× labour average
- ⚠️ Nexford figures (78%/41%/51%) are single-sourced — need 2nd source before publishing
- Verdicts: ✅ VERIFIED · ⚠️ PARTIAL · ❌ UNVERIFIED · 🔄 CORRECTED

### ultracode
- 5-phase pipeline: Think → Specify → Build → Review → Ship
- Quick-mode for <20 line changes: Think + TDD + self-review checklist (skip full SPARC)
- Never skips Phase 0 (Think) or Phase 3 (Review)

### steering-lint
- 7 rules: 3 high (automation-as-prose, prohibition-as-prose, procedure-in-memory)
- 3 medium (unscoped-narrow-rule, personal-pref-in-shared, memory-bloat, output-style-overreach)
- 1 low (skill-vs-subagent-mismatch)
- Outputs HTML report via `scripts/render_report.py`

---

## Recent Session Work (2026-06-26)
- Built `ministry-proposal`, `fact-checker`, `steering-lint`, `ultracode` skills
- Added `auto-trigger` / `do-not-trigger` to all 44 skills
- Fixed flake8 F824 in `claude_agent_sdk/utils/agent_visualizer.py`
- All merged to main via PR #4, PR #6, PR #7
