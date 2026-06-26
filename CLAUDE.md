# Claude Code Instructions — Mahmoud-Gadalla

## Project Layout

- `claude_agent_sdk/` — standalone Python agents (research, SRE, chief of staff, vulnerability detection, session browser)
- `managed_agents/` — Claude Managed Agents notebooks and integrations (Slack, Sentry, Linear)
- `anthropic_skills/` — drop-in skill folders; each has a `SKILL.md`
- `skills/` — cookbooks skill modules (financial, brand)
- `tool_use/` — tool use pattern notebooks
- `misc/` — runnable scripts (batch_processing.py, outcome_grader.py)
- `tools/` — developer tooling (diffgate submodule, JetBrains plugin)

## Skill Routing

Skills are applied **automatically** based on task context — no explicit invocation needed. When a task matches a skill's domain, load and follow it.

### Memory & Session
| Task | Skill |
|---|---|
| Consolidate/audit knowledge directories | `anthropic_skills/engram/consolidate` |
| Session briefing / catch me up | `anthropic_skills/engram/briefing` |
| Checkpoint working memory | `anthropic_skills/engram/working` |

### Code Quality & Development
| Task | Skill |
|---|---|
| Any non-trivial feature, refactor, bug fix, API/schema change, or security-sensitive task | `anthropic_skills/ultracode` |
| Build apps with Claude API / SDK | `anthropic_skills/claude-api` |
| Structured feature development (SPARC) | `anthropic_skills/sparc` |
| Architecture Decision Records | `anthropic_skills/adr` |
| Test-driven development | `anthropic_skills/tdd` |
| Debugging | `anthropic_skills/debug` |
| Assess impact of a change | `anthropic_skills/change-impact` |
| Karpathy-style coding principles | `anthropic_skills/karpathy-guidelines` |
| MCP server creation | `anthropic_skills/mcp-builder` |
| Inspect/debug MCP servers | `anthropic_skills/mcp-inspector` |
| Web app test automation | `anthropic_skills/webapp-testing` |
| Fix failing GitHub Actions CI on a PR | `anthropic_skills/gh-fix-ci` |
| Address PR review comments | `anthropic_skills/gh-address-comments` |
| Commit, push & open a PR in one flow | `anthropic_skills/yeet` |
| Find & fix production issues from Sentry | `anthropic_skills/sentry/sentry-fix-issues` |
| Create Sentry alerts | `anthropic_skills/sentry/sentry-create-alert` |
| Instrument AI/LLM agent monitoring | `anthropic_skills/sentry/sentry-setup-ai-monitoring` |
| Sentry Seer bug-prediction PR review | `anthropic_skills/sentry/sentry-pr-code-review` |
| Set up Sentry SDK in Python | `anthropic_skills/sentry/sentry-python-setup` |
| Neon serverless Postgres setup/branching | `anthropic_skills/neon/neon-postgres` |
| Diagnose & cut Postgres egress costs | `anthropic_skills/neon/neon-postgres-egress-optimizer` |
| Write Terraform HCL (style conventions) | `anthropic_skills/terraform/terraform-style-guide` |
| Write/run Terraform tests (.tftest.hcl) | `anthropic_skills/terraform/terraform-test` |
| Terraform Stacks (multi-env/region infra) | `anthropic_skills/terraform/terraform-stacks` |
| Stripe payments/billing integration | `anthropic_skills/stripe` |
| Build/ship Expo apps (EAS Build, stores) | `anthropic_skills/expo/expo-deployment` |
| Expo Router app UI (screens, navigation) | `anthropic_skills/expo/expo-building-native-ui` |
| Static analysis scan (Semgrep) | `anthropic_skills/trailofbits/semgrep` |
| Deep taint analysis (CodeQL) | `anthropic_skills/trailofbits/codeql` |
| API misuse / footgun design review | `anthropic_skills/trailofbits/sharp-edges` |

### Document & Content Generation
| Task | Skill |
|---|---|
| Word documents | `anthropic_skills/docx` |
| PDF documents | `anthropic_skills/pdf` |
| PowerPoint | `anthropic_skills/pptx` |
| Excel | `anthropic_skills/xlsx` |
| Collaborative document writing | `anthropic_skills/doc-coauthoring` |
| Internal communications | `anthropic_skills/internal-comms` |
| Product requirement docs | `anthropic_skills/prd-generator` |
| Session/work handoff notes | `anthropic_skills/handoff` |
| University curriculum / syllabus / exam / rubric / grading | `anthropic_skills/curriculum-builder` |
| Strip AI writing tells / humanize a draft | `anthropic_skills/humanizer` |

### Research & Verification
| Task | Skill |
|---|---|
| Triple-source fact verification / QA grid | `anthropic_skills/fact-checker` |
| Deep multi-step research | `anthropic_skills/deep-research` |
| Exhaustive multi-source search | `anthropic_skills/ultra-search` |
| News & current events research | `anthropic_skills/news-research` |
| Substantiate claims | `anthropic_skills/prove-claims` |
| GEO / SEO for AI answer engines | `anthropic_skills/claude-seo` |

### Design & Frontend
| Task | Skill |
|---|---|
| Frontend/UI artifacts | `anthropic_skills/frontend-design` |
| General design workflows | `anthropic_skills/design` |
| Brand guidelines | `anthropic_skills/brand-guidelines` |
| Canvas-based design | `anthropic_skills/canvas-design` |
| Theme generation | `anthropic_skills/theme-factory` |
| Generative/algorithmic art | `anthropic_skills/algorithmic-art` |
| Web artifact construction | `anthropic_skills/web-artifacts-builder` |
| Animated GIFs for Slack | `anthropic_skills/slack-gif-creator` |
| shadcn/ui components (components.json projects) | `anthropic_skills/shadcn` |
| Presentation design (narrative spine, data storytelling, visual hierarchy) | `anthropic_skills/presentation-architect` |
| HTML-to-video rendering (MP4/GIF/WebM from markup) | `anthropic_skills/hyperframes` |

### Marketing & Brand Strategy
| Task | Skill |
|---|---|
| Brand strategy / positioning / brand pyramid / value proposition | `anthropic_skills/brand-framework` |
| LinkedIn / personal branding / content calendar / thought leadership | `anthropic_skills/linkedin-branding` |
| Social media audit / channel benchmark / recommendations | `anthropic_skills/social-audit` |
| Social content creation (posts, reels, captions, calendar) | `anthropic_skills/social-content` |

### Orchestration & Meta
| Task | Skill |
|---|---|
| Route any task to the right skill | `anthropic_skills/orchestrator` |
| Deep delegation via agent tree | `anthropic_skills/nested-subagents` |
| Task queue management | `anthropic_skills/queue` |
| Create a new skill | `anthropic_skills/skill-creator` |
| Audit & maintain the skill library (loop) | `anthropic_skills/library-maintainer` |
| Find & install a skill (discover capability) | `anthropic_skills/find-skills` |

### Workflow & Process
| Task | Skill |
|---|---|
| Think before coding (find shortcuts) | `anthropic_skills/lazy-cat/think-twice` |
| Surgical edits (write only what's asked) | `anthropic_skills/lazy-cat/surgical` |
| Clarify intent before agent acts | `anthropic_skills/promptize/promptize` |
| Estimate task cost | `anthropic_skills/sipcode/estimate` |
| Audit session token spend | `anthropic_skills/sipcode/why` |
| Compress model-facing prompt/context tokens | `anthropic_skills/caveman` |
| Audit CLAUDE.md quality | `anthropic_skills/claude-md-audit` |
| Audit instruction placement (CLAUDE.md vs hooks vs skills) | `anthropic_skills/steering-lint` |

### Domain-Specific
| Task | Skill |
|---|---|
| Arabic ministry proposal (MERIDIAN/MBK brand) | `anthropic_skills/ministry-proposal` |
| Legal drafting/review (contracts, NDAs, policies, ToS) | `anthropic_skills/legal-practice` |

### Finance & Brand (skills/custom_skills/)
| Task | Skill |
|---|---|
| Financial ratio analysis (ROE, P/E, liquidity, leverage) | `skills/custom_skills/analyzing-financial-statements` |
| Financial modelling (DCF, Monte Carlo, M&A, LBO, scenarios) | `skills/custom_skills/creating-financial-models` |
| Acme Corporation brand compliance on any document | `skills/custom_skills/applying-brand-guidelines` |

## Environment

```bash
cp .env.example .env   # add ANTHROPIC_API_KEY
uv sync --all-extras   # install Python deps
```

## Models

- Sonnet: `claude-sonnet-4-6`
- Haiku: `claude-haiku-4-5`
- Opus: `claude-opus-4-6`

## Code Style

- Python: follow existing patterns, no unnecessary abstractions
- No comments unless the WHY is non-obvious
- Never commit `.env` files

<!-- sipcode:start v=2 -->
<!-- sipcode:block name="output-compression" mode="default" -->
## Sipcode Output Compression

mode: default — optimizes for: diff edits, no ceremony

the rules below apply to your responses in this project. follow them.
they exist so the user pays for code, not for ceremony.
### rules (default mode)

1. **diff-only edits.** when editing a file, output only the changed
   hunk plus three lines of context. never paste the full file back
   when three lines changed. this is the single biggest win.
2. **no preamble.** skip "i'll help with that", "sure", "here's what
   i did". lead with the work. the user can see what you did.
3. **no post-amble.** don't summarize what was just shown unless the
   user explicitly asks for a summary.
4. **code over prose.** when the answer is code, the code is the
   answer. any explanation goes after the code block, not before.
5. **bullets over paragraphs** for any list of options, steps, or
   trade-offs. saves tokens versus flowing prose.
6. **one canonical example, not three.** show one good example. skip
   the exhaustive variants — the user will ask if they want more.
7. **no filler verbs.** drop "let me", "i'll go ahead and", "i'm
   going to". just do the thing.

(installed by sipcode. switch modes with `npx sipcode rules --mode <m>`.
uninstall with `npx sipcode rules --uninstall`.)
<!-- /sipcode:block -->

<!-- sipcode:end -->
