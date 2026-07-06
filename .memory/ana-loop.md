# ANA Loop — Iteration Log

## Iteration 2 — 2026-07-04

**Extract:**
- mahmoud-gadalla: 103 skills (grew 76→103 across prior sessions)
- library-maintainer loop added (`misc/library_audit.py` + `anthropic_skills/library-maintainer/SKILL.md`)
- Adversarial eval infrastructure: 5 cases/skill, aggregate 96.7% (58/60)
- 32 older skills still have `pass_rate=null` (backlog for next iteration)
- gate-repl: stable — beliefgate 15/15 tests pass

**Apply:**
- `ANA_BLUEPRINT.md`: iteration counter, skill count, library-maintainer sub-loop documented
- `.github/workflows/ana-blueprint.yml`: added `library_audit.py` step in assess phase
- `.memory/ana-loop.md`: this file

**Assess:**
- gate-repl: 15/15 beliefgate tests (leak-proof invariant holds)
- library audit: to be confirmed by CI

**Merge to Evolve:**
- PRs: mahmoud-gadalla#59, gate-repl#2 (iteration 2)

## Iteration 3 — 2026-07-04

**Extract:**
- mims-harvard/ToolUniverse: 1,000+ scientific tools (AlphaFold, BLAST, DrugBank, PubMed, ClinVar, etc.)
- Unified `BaseTool` interface + MCP server (`tooluniverse-mcp`) + CLI (`tu`)
- 151 pre-built skills in ToolUniverse; 68 research workflows
- beliefgate integration pattern: gate before any scientific API call

**Apply:**
- `anthropic_skills/tooluniverse/SKILL.md`: skill wrapping ToolUniverse SDK
- `CLAUDE.md`: routing entry added under Research & Verification
- `ANA_BLUEPRINT.md`: Layer [0] Tool Layer added to pipeline diagram; ToolUniverse wired in
- `.memory/ana-loop.md`: this entry

**Assess:**
- Routing: tooluniverse skill reachable from CLAUDE.md
- Cross-reference: beliefgate ↔ tooluniverse integration pattern documented

**Merge to Evolve:**
- PR: mahmoud-gadalla#78 (iteration 3)

## Iteration 6 — 2026-07-06

**Extract:**
- Discovered via github.com/topics/claude-code-skills + awesome-agent-skills catalog
- VoltAgent/awesome-agent-skills: 1,000+ vendor skills (Microsoft Azure, Cloudflare, Netlify, HuggingFace, Figma, Sentry, Trail of Bits, Expo, fal.ai, Google Workspace, OpenAI, Kim Barrett, Apollo GraphQL, Binance, WordPress)
- sickn33/antigravity-awesome-skills: 1,901 skills (dev/frontend/security/testing/DevOps/data/agents/MCP)
- K-Dense-AI/scientific-agent-skills: 148 skills + 100+ scientific DBs (bioinformatics, cheminformatics, clinical, lab automation)
- Orchestra-Research/AI-Research-SKILLs: 98 skills, 23 categories (full AI research lifecycle)
- nexu-io/html-anything: 75 HTML skills × 9 surfaces
- deanpeters/Product-Manager-Skills: 26 PM skills (problem framing, stakeholder, PRD, AI product)
- Agents365-ai/drawio-skill: 7 diagram types, 4 export formats
- realkimbarrett: 12 direct response/advertising skills (Schwartz awareness, mechanism builder)
- parcadei/Continuous-Claude-v3: 109 skills + 32 agents + 30 hooks (compaction-proof multi-agent)

**Apply:**
- 6 new skills: `html-anything`, `drawio`, `scientific-research`, `ai-research`, `product-manager`, `ad-creative-expert`
- CLAUDE.md: +2 research routes, +2 design routes, +2 new sections (Product Management, Advertising & Direct Response)
- ANA_BLUEPRINT.md: iteration 6 marker
- Key external catalog: VoltAgent/awesome-agent-skills = official vendor skill registry

**Assess:**
- Skills: 117 → 123
- Research layer now: tooluniverse → athena → ark → scientific-research → ai-research (5-layer scientific stack)

**Merge to Evolve:**
- PR: mahmoud-gadalla#86 (iteration 6)

## Iteration 5 — 2026-07-06

**Extract:**
- 14 repos surveyed (design/frontend/backend focus)
- nexu-io/open-design: open-source Claude Design alternative — DESIGN.md brand schema, 100+ skills, 261 plugins, 150 design systems, MCP server (`od mcp install claude`)
- VoltAgent/awesome-design-md: 73+ brand DESIGN.md files (Linear, Stripe, Notion, Tesla, Apple…) — direct input to open-design
- nextlevelbuilder/ui-ux-pro-max-skill: AI design system generator — 67 UI styles, 161 color palettes, 57 font pairings, 161 industry reasoning rules
- gin-gonic/gin: Go HTTP framework (40x faster, zero-allocation router)
- Skipped: shadcn (have), mui (covered), clash-verge/rustdesk (unrelated), WebAssembly/java-patterns (reference only)

**Apply:**
- 3 new skills: `anthropic_skills/open-design`, `anthropic_skills/ui-ux-pro-max`, `anthropic_skills/gin`
- CLAUDE.md: +4 design routing entries, +1 Backend section (gin)
- ANA_BLUEPRINT.md: iteration 5 marker

**Assess:**
- Skills: 114 → 117
- open-design + awesome-design-md form composable brand system — documented in SKILL.md

**Merge to Evolve:**
- PR: mahmoud-gadalla#85 (iteration 5)

## Iteration 4 — 2026-07-06

**Extract:**
- 13 repos surveyed: mims-harvard (ATHENA, ARK/gates-buildathon, Qworld, MedLog), alirezarezvani/claude-skills (355 skills), coreyhaines31/marketingskills (45+ skills), ericosiu/ai-marketing-skills (Python pipelines), twentyhq/twenty (CRM), dubinc/dub (link attribution), mautic/mautic (marketing automation), matomo-org/matomo (analytics)
- ATHENA: 212 biomedical tools, AI treatment reasoning, 94.7% drug benchmark
- Qworld: recursive LLM eval framework — wired into library-maintainer eval protocol
- alirezarezvani/claude-skills: 355 SKILL.md skills; cross-referenced as external skill source

**Apply:**
- 6 new skills: `anthropic_skills/athena`, `anthropic_skills/ark`, `anthropic_skills/qworld`, `anthropic_skills/twenty`, `anthropic_skills/dub`, `anthropic_skills/mautic`
- CLAUDE.md: +3 research routing entries, +19 marketing routing entries (launch, ASO, CRO, onboarding, churn, programmatic-SEO, referrals, cold-email, pricing, revops, marketing-council, directory-submissions, schema, experiment-engine, mautic, dub, twenty, seo-audit, product-marketing)
- ANA_BLUEPRINT.md: iteration 4 marker, 12 new repos in external sources table
- `.memory/ana-loop.md`: this entry

**Assess:**
- Skills: 114 total (104 → 114, +10 net after routing additions)
- All new SKILL.md files follow health block convention
- CLAUDE.md routing surface expanded to cover scientific reasoning + treatment AI + 19 marketing task types

**Merge to Evolve:**
- PR: mahmoud-gadalla#84 (iteration 4)

## Iteration 1 — 2026-07-04

**Applied:** ANA_BLUEPRINT.md, beliefgate SKILL.md, ana-blueprint.yml CI workflows in both repos.
**Merged:** mahmoud-gadalla#58, gate-repl#1 — both squash-merged to main.
