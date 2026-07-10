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
| Profile a dataset (shape, nulls, quality, follow-ups) | `anthropic_skills/profile-dataset` |
| People/HR analytics report (headcount, attrition, diversity, org-health) | `anthropic_skills/people-analytics` |
| Daily/weekly business pulse (cross-tool cash/sales/pipeline brief) | `anthropic_skills/business-pulse` |
| Strip AI writing tells / humanize a draft | `anthropic_skills/humanizer` |

### Research & Verification
| Task | Skill |
|---|---|
| Scientific database queries (AlphaFold, BLAST, DrugBank, PubMed, ClinVar, genomics, drug discovery) | `anthropic_skills/tooluniverse` |
| Treatment reasoning / clinical decision support / drug recommendations | `anthropic_skills/athena` |
| Biomedical knowledge graph queries (gene-drug-disease relationships, multi-hop) | `anthropic_skills/ark` |
| Computational biology / bioinformatics / cheminformatics / RNA-seq / molecular docking | `anthropic_skills/scientific-research` |
| AI/ML research / fine-tuning / RLHF / RAG / LLM serving / MLOps / ML paper | `anthropic_skills/ai-research` |
| Embedded vector DB / in-process vector search / hybrid retrieval / DiskANN / edge RAG | `anthropic_skills/zvec` |
| Evaluate LLM response quality / generate question-specific rubrics | `anthropic_skills/qworld` |
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
| Single-image infographic (stats/steps/comparison) | `anthropic_skills/infographic-maker` |
| Brand-consistent UI from DESIGN.md / open-design workflow | `anthropic_skills/open-design` |
| Design system generation (67 UI styles, 161 palettes, industry rules) | `anthropic_skills/ui-ux-pro-max` |
| Convert markdown/CSV/JSON to HTML / ship-ready HTML across 9 surfaces | `anthropic_skills/html-anything` |
| Architecture / C4 / UML / ERD / flowchart / ML pipeline diagram (draw.io) | `anthropic_skills/drawio` |
| Enterprise React UI components (Ant Design) | `anthropic_skills/frontend-design` |
| Enterprise React app scaffold (Ant Design Pro / Umi) | `anthropic_skills/frontend-design` |

### Marketing & Brand Strategy
| Task | Skill |
|---|---|
| Brand strategy / positioning / brand pyramid / value proposition | `anthropic_skills/brand-framework` |
| LinkedIn / personal branding / content calendar / thought leadership | `anthropic_skills/linkedin-branding` |
| Social media audit / channel benchmark / recommendations | `anthropic_skills/social-audit` |
| Social content creation (posts, reels, captions, calendar) | `anthropic_skills/social-content` |
| Paid media buying (campaign plan, bidding, targeting, optimization) | `anthropic_skills/media-buyer` |
| Persuasion psychology (Cialdini audit, social proof, ethical copy) | `anthropic_skills/persuasion-psychology` |
| Brand voice & tone guidelines (verbal identity) | `anthropic_skills/brand-voice` |
| Competitive brief (rival positioning, messaging gaps) | `anthropic_skills/competitive-brief` |
| Blue Ocean strategy (canvas, ERRC, six paths) | `anthropic_skills/blue-ocean-strategy` |
| Brand-kit visual board (logo, palette, mockups image) | `anthropic_skills/brand-kit` |
| LinkedIn outreach sequences (cold DM, follow-ups) | `anthropic_skills/linkedin-outreach` |
| Content refresh (recover decaying organic traffic) | `anthropic_skills/content-refresh` |
| Free lead-gen tool planning (calculator, grader, quiz) | `anthropic_skills/free-marketing-tool` |
| Gap analysis (current vs target, root cause, closure plan) | `anthropic_skills/gap-analysis` |
| SWOT + TOWS analysis | `anthropic_skills/swot-analysis` |
| Paid-ad account diagnosis (spend leaks, funnel) | `anthropic_skills/ads-analysis` |
| Ad creative performance analysis (hook, fatigue, patterns) | `anthropic_skills/creative-analysis` |
| Communication/messaging analysis (intended vs received) | `anthropic_skills/communication-analysis` |
| Product launch planning / launch strategy | `anthropic_skills/marketing/launch` |
| Marketing automation (email drip, lead scoring, self-hosted) | `anthropic_skills/mautic` |
| Link shortening / click attribution / affiliate link tracking | `anthropic_skills/dub` |
| CRM setup / customization / self-hosted CRM (open-source) | `anthropic_skills/twenty` |
| SEO audit / site diagnosis | `anthropic_skills/marketing/seo-audit` |
| App Store Optimization (ASO) | `anthropic_skills/marketing/aso` |
| Conversion rate optimization (CRO) / landing page scoring | `anthropic_skills/marketing/cro` |
| Onboarding / user activation / time-to-value optimization | `anthropic_skills/marketing/onboarding` |
| Churn prevention / cancellation flows / payment recovery | `anthropic_skills/marketing/churn-prevention` |
| Product marketing / positioning document | `anthropic_skills/marketing/product-marketing` |
| Programmatic SEO / scaled content page generation | `anthropic_skills/marketing/programmatic-seo` |
| Referral / affiliate program design | `anthropic_skills/marketing/referrals` |
| Cold email sequences (B2B outreach) | `anthropic_skills/marketing/cold-email` |
| Pricing strategy / packaging / monetization | `anthropic_skills/marketing/pricing` |
| Revenue operations / lead lifecycle / marketing-to-sales handoff | `anthropic_skills/marketing/revops` |
| Marketing council (multi-expert advisory panel) | `anthropic_skills/marketing/marketing-council` |
| Directory submissions (startup/SaaS/AI directories) | `anthropic_skills/marketing/directory-submissions` |
| Schema markup / structured data | `anthropic_skills/marketing/schema` |
| Autonomous marketing experiments (run, measure, optimize) | `anthropic_skills/marketing/experiment-engine` |

### Product Management
| Task | Skill |
|---|---|
| Product strategy / problem framing / positioning / roadmap | `anthropic_skills/product-manager` |
| Stakeholder mapping / discovery interviews / PRD / user stories | `anthropic_skills/product-manager` |
| AI product design / agent orchestration / context engineering | `anthropic_skills/product-manager` |

### Advertising & Direct Response
| Task | Skill |
|---|---|
| Ad copywriting / Schwartz awareness / mechanism builder / headline matrix | `anthropic_skills/ad-creative-expert` |
| Scroll-stopping creative / objection crusher / full-funnel campaign | `anthropic_skills/ad-creative-expert` |

### Brand Building & Identity
| Task | Skill |
|---|---|
| Brand strategy / naming / story / manifesto / launch / rebrand / audit / measurement | `anthropic_skills/brand-building` |
| D2C strategy / B2B brand / influencer / UGC / packaging / email / Meta & Google ads | `anthropic_skills/brand-building` |
| Brand pillars / visual identity system / logo system / color / typography / motion | `anthropic_skills/brand-identity-pillars` |
| Sustainability brand pillars / ESG brand positioning / purpose-driven identity | `anthropic_skills/brand-identity-pillars` |
| Brand design language for 62 world-class brands (Nike, Stripe, Notion, Airbnb…) | `anthropic_skills/brand-identity-pillars` |

### Consumer Behaviour & Psychology
| Task | Skill |
|---|---|
| Consumer psychology / cognitive biases / behavioral economics / why people buy | `anthropic_skills/consumer-behaviour` |
| Pricing psychology / loss aversion / anchoring / BJ Fogg model / Jobs to Be Done | `anthropic_skills/consumer-behaviour` |
| UX psychology / 65 behavioral principles / decision architecture / persuasion design | `anthropic_skills/consumer-behaviour` |

### Data Management
| Task | Skill |
|---|---|
| Data governance / data catalog / metadata management / data dictionary | `anthropic_skills/data-management` |
| Data quality / data lineage / data contracts / data mesh / data observability | `anthropic_skills/data-management` |
| ETL pipeline design / dataset versioning / GDPR data compliance | `anthropic_skills/data-management` |

### Presentation Design & Aesthetics
| Task | Skill |
|---|---|
| Slide deck design / narrative spine / visual hierarchy / data slide / pitch deck polish | `anthropic_skills/presentation-design` |
| Cinematic web presentation / script → 16:9 slides → screen-recordable video | `anthropic_skills/presentation-design` |
| Four-axis aesthetic brief / slide aesthetics / executive deck / presentation template | `anthropic_skills/presentation-design` |

### Fashion Intelligence
| Task | Skill |
|---|---|
| Personal styling / outfit recommendations / wardrobe management / capsule wardrobe | `anthropic_skills/fashion-intelligence` |
| Fashion history / fashion economics / luxury goods economics / trend analysis | `anthropic_skills/fashion-intelligence` |
| Fast fashion vs. slow fashion / resale market / fashion sustainability / colour analysis | `anthropic_skills/fashion-intelligence` |

### Orchestration & Meta
| Task | Skill |
|---|---|
| Route any task to the right skill | `anthropic_skills/orchestrator` |
| Deep delegation via agent tree | `anthropic_skills/nested-subagents` |
| Task queue management | `anthropic_skills/queue` |
| Create a new skill | `anthropic_skills/skill-creator` |
| Audit & maintain the skill library (loop) | `anthropic_skills/library-maintainer` |
| Find & install a skill (discover capability) | `anthropic_skills/find-skills` |
| Structured business consulting (issue tree, hypothesis, recommend) | `anthropic_skills/business-consulting` |

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
| Context window optimization / intentional compaction / memory bank architecture | `anthropic_skills/context-engineering` |
| Per-folder __instruct.md context files / modular project context | `anthropic_skills/instruct-md` |

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

### Backend & Infrastructure
| Task | Skill |
|---|---|
| Go HTTP API / REST / microservice (Gin framework) | `anthropic_skills/gin` |

## MCP Servers

This repo has no `.mcp.json` yet — no project-scoped MCP servers are shared with contributors.

- Add one for the whole team: `claude mcp add --scope project --transport http <name> <url>` writes to `.mcp.json` in the repo root; commit it so it's shared.
- Add one for yourself only: omit `--scope project` (defaults to `local`, stored in `~/.claude.json`).
- For MCP server creation, use `anthropic_skills/mcp-builder`; to inspect/debug an existing server, use `anthropic_skills/mcp-inspector`.
- Never commit tokens/secrets into `.mcp.json` — use the `env` field with a placeholder and document the required var, or pass `--header "Authorization: Bearer <token>"` at `local`/`user` scope instead.

## Models

- Sonnet: `claude-sonnet-4-6`
- Haiku: `claude-haiku-4-5`
- Opus: `claude-opus-4-6`

## Code Style

- Python: follow existing patterns, no unnecessary abstractions
- No comments unless the WHY is non-obvious
- Never commit `.env` files

## Communication Guidelines

### Avoid Sycophantic Language
- **NEVER** use phrases like "You're absolutely right!", "You're absolutely correct!", "Excellent point!", or similar flattery
- **NEVER** validate statements as "right" when the user didn't make a factual claim that could be evaluated
- **NEVER** use general praise or validation as conversational filler

### Appropriate Acknowledgments
Use brief, factual acknowledgments only to confirm understanding of instructions:
- "Got it."
- "Ok, that makes sense."
- "I understand."
- "I see the issue."

These should only be used when:
1. You genuinely understand the instruction and its reasoning
2. The acknowledgment adds clarity about what you'll do next
3. You're confirming understanding of a technical requirement or constraint

### Examples

**❌ Inappropriate (Sycophantic)**
> User: "Yes please." → Assistant: "You're absolutely right! That's a great decision."

**✅ Appropriate (Brief Acknowledgment)**
> User: "Yes please." → Assistant: "Got it." [proceeds with the requested action]

**✅ Also Appropriate (No Acknowledgment)**
> [proceeds directly with the requested action]

Source: `anthropics/claude-code#3382`

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
