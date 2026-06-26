# My Claude Stack

A directory of the Mahmoud-Gadalla skill library, in the three-column "stack"
format (Plugins · Skills · MCP). Inspired by Charlie Hills' *My Claude Stack*.

**Library**: 81 skills (56 top-level + 25 nested) in `anthropic_skills/` · 3 in `skills/custom_skills/`
**Last updated**: 2026-06-26

---

## 🧩 SKILLS — what Claude knows how to do

Skills auto-trigger by context. Grouped by domain. ✅ = present in this repo.

### Code Quality & Development
| Skill | Does |
|---|---|
| `ultracode` | Multi-phase pipeline for any non-trivial feature/refactor/fix |
| `claude-api` | Build with the Claude/Anthropic SDK — models, tools, MCP |
| `sparc` | Structured feature dev for uncertain requirements |
| `adr` · `tdd` · `debug` · `change-impact` · `karpathy-guidelines` | Decisions, tests, debugging, impact analysis, code principles |
| `mcp-builder` · `mcp-inspector` | Build and debug MCP servers |
| `webapp-testing` | Playwright/browser E2E |
| `gh-fix-ci` · `gh-address-comments` · `yeet` | PR lifecycle: fix CI, address reviews, ship |

### Research & Verification
| Skill | Does |
|---|---|
| `deep-research` · `ultra-search` · `news-research` | Structured research, breadth sweep, current events |
| `fact-checker` · `prove-claims` | Triple-source verification · claim→evidence mapping |
| `claude-seo` ✨ | GEO — get content cited by AI answer engines |

### Document & Content
| Skill | Does |
|---|---|
| `docx` · `pdf` · `pptx` · `xlsx` | Office document generation |
| `doc-coauthoring` · `internal-comms` · `handoff` | Collaborative writing, comms, handoffs |
| `prd-generator` | Tiered product requirement docs |
| `curriculum-builder` | University courses, exams, rubrics, marking |
| `humanizer` ✨ | Strip AI writing tells from a draft |
| `caveman` ✨ | Cut model-facing token spend, meaning intact |

### Design & Frontend
| Skill | Does |
|---|---|
| `design` | Router for the whole design cluster |
| `frontend-design` · `shadcn` · `web-artifacts-builder` | Web UI, shadcn components, HTML artifacts |
| `canvas-design` · `algorithmic-art` | Static art (.pdf/.png) · generative p5.js art |
| `presentation-architect` · `theme-factory` · `brand-guidelines` | Deck design · theming · Anthropic identity |
| `hyperframes` ✨ | Write HTML, render to MP4/GIF/WebM |
| `slack-gif-creator` | Animated GIFs for Slack |

### Marketing & Brand Strategy
| Skill | Does |
|---|---|
| `brand-framework` | Brand Pyramid + 4C positioning |
| `linkedin-branding` | LinkedIn authority system (4-axis + 5-3-2) |
| `social-audit` | Six-section social audit + recommendations |

### Orchestration & Meta
| Skill | Does |
|---|---|
| `orchestrator` | Route a task across the library |
| `find-skills` ✨ | Discover & install a skill (local or external) |
| `skill-creator` | Author and evolve skills |
| `nested-subagents` · `queue` | Agent trees · deferred task queue |

### Workflow, Cost & Hygiene
| Skill | Does |
|---|---|
| `lazy-cat/think-twice` · `lazy-cat/surgical` · `promptize/promptize` | Think first, surgical edits, clarify intent |
| `sipcode/*` | Token economics: estimate, why, impact, benchmark |
| `claude-md-audit` · `steering-lint` | Config hygiene audits |

### Vendor / Tool Skills
`sentry/*` (5) · `neon/*` (2) · `terraform/*` (3) · `trailofbits/*` (3) · `stripe` · `expo/*` (2)

### Domain & Finance
`ministry-proposal` (Arabic ministry decks) · `skills/custom_skills/`: `analyzing-financial-statements`, `creating-financial-models`, `applying-brand-guidelines`

✨ = added 2026-06-26 (this batch: hyperframes, claude-seo, find-skills, humanizer, caveman)

---

## 🔌 PLUGINS — external tooling + native skill-equivalents

Tooling plugins install on your machine (see `stack/STACK_SETUP.md`). Skill-bundle
plugins are covered by native skills here — no plugin needed.

| Plugin | What it does | Coverage here |
|---|---|---|
| gstack | 23 dev tools, one install | ⬇ install via marketplace |
| superpowers | Dev methodology, 14 skills | ⬇ install via marketplace |
| codex-plugin-cc | OpenAI's official Codex plugin | ⬇ install via marketplace |
| financial-services | IB, PE, equity, wealth | ✅ `skills/custom_skills/` finance |
| claude-for-legal | Legal practice | ✅ `legal-practice` (native) |
| claude-skills | 263+ skills, every platform | ✅ discover via `find-skills` |
| marketingskills | 40 tools, growth ops | ✅ brand-framework + linkedin-branding + social-audit + social-content |
| social-media-skills | Posts, reels content OS | ✅ `social-content` + social-audit + linkedin-branding |

**Setup**: `stack/STACK_SETUP.md` · **MCP template**: `stack/mcp-servers.stack.json` · **Plugin config**: `stack/settings.plugins.template.json`

---

## 🛰️ MCP — connected servers (environment-provided)

MCP servers are provided by the runtime, not this repo. Availability varies by
session; recent sessions have surfaced (non-exhaustive):

| MCP | What it does |
|---|---|
| github | PRs, issues, CI, reviews, merges |
| Canva · Gamma · Adobe · Magnific | Design/creative generation |
| Ahrefs · Semrush · Motion · Polar · Supermetrics | SEO / marketing analytics |
| Shopify · Stripe (via skill) · Lovable · Replit | Commerce / app building |
| Granola · Gmail · Google Drive/Calendar · Zoom | Productivity |
| Asana · Buffer · Clay · Make · IFTTT | Workflow automation |

Reference-stack MCPs not present here: granola (✅ present), slack, notion, kondo,
zapier, higgsfield, perplexity, agent-browser — connect via the runtime if needed.

---

## How this maps to the reference stack

The reference "My Claude Stack" Skills column → this library:

| Reference skill | Here |
|---|---|
| frontend-design | ✅ `frontend-design` |
| skill-creator | ✅ `skill-creator` |
| mcp-builder | ✅ `mcp-builder` |
| hyperframes | ✅ `hyperframes` (built 2026-06-26) |
| claude-seo | ✅ `claude-seo` (built 2026-06-26) |
| find-skills | ✅ `find-skills` (built 2026-06-26) |
| humanizer | ✅ `humanizer` (built 2026-06-26) |
| caveman | ✅ `caveman` (built 2026-06-26) |

All 8 Skills-column entries now exist as first-party skills. Plugins and MCP
columns are external and provided outside this repo.
