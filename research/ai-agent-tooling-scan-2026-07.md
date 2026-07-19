# Repo Research Brief — 10 AI/agent/dev-tooling projects

**Date:** 2026-07-19
**Method:** one WebFetch per repo (public GitHub landing page + README). Star counts are **approximate** (read off the page, rounded). License/maturity noted where the page stated it.
**Lens:** what each project is + **how it maps to your repo** (`ruflo` harness, `qoder-plugins-publish`, `rulebook-ai`, `social_media_review`, and the deleted ANA-Blueprint skills idea).

---

## At a glance

| Repo | Category | Stars≈ | Stack | License | Maturity | Fit for you |
|---|---|---|---|---|---|---|
| `aaif-goose/goose` | AI agent harness | 51k | Rust + TS | Apache-2.0 | Very active; under Linux Foundation **AAIF** | ★★★ direct peer to `ruflo` |
| `bytedance/deer-flow` | Long-horizon multi-agent | 77k | Python (LangGraph) | MIT | v2.0 rewrite, Jun 2026 | ★★★ peer to `ruflo` **and** ANA-Blueprint (skills/memory/sub-agents) |
| `D4Vinci/Scrapling` | Adaptive web scraping | 70k | Python (Playwright) | BSD-3 | 92% cov, MCP server | ★★★ solves your **IG/anti-bot** wall; fits `rulebook-ai` + qoder Playwright |
| `decolua/9router` | LLM router / cost proxy | 22k | JS (Next) | MIT | 73 releases | ★★★ maps to `ruflo` 3-tier routing + the "cut Claude costs" theme |
| `infiniflow/ragflow` | RAG engine | 85k | Go + Python + TS | Apache-2.0 | Very mature | ★★☆ feeds `ruflo` rag-memory + doc-heavy qoder plugins |
| `johannesjo/parallel-code` | Parallel coding agents | 0.9k | TS (Electron/Solid) | MIT | Small but active | ★★☆ complements `ruflo` swarm (worktree-per-agent) |
| `JCodesMore/ai-website-cloner-template` | Claude-Code clone command | 29k | TS (Next/shadcn) | MIT | Viral template, 5 releases | ★★☆ command/skill-authoring pattern; design cloning |
| `dyad-sh/dyad` | Local AI app builder | 21k | TS (Electron/Next) | Apache-2.0 + FSL | 120 releases | ★☆☆ product tool, tangential to the harness |
| `pipecat-ai/pipecat` | Voice / multimodal AI | 14k | Python (WebRTC) | BSD-2 | 114 releases | ★☆☆ **net-new capability** (voice) — not in your stack today |
| `daytonaio/daytona` | Sandboxes for AI code | 72k | Multi-lang SDKs | (unconfirmed) | ⚠️ **NO LONGER MAINTAINED** (Jun 2026, core went private) | ★☆☆ concept useful; repo is a dead end |

---

## By category

### 1. Agent harnesses (direct peers to `ruflo`)

**`aaif-goose/goose` — 51k★, Rust+TS, Apache-2.0.** "Your native open-source AI agent — desktop, CLI, and API." 15+ LLM providers, 70+ MCP extensions, runs local across macOS/Linux/Windows. Now developed under the Linux Foundation's **Agentic AI Foundation (AAIF)** — not a fork, a standalone flagship.
→ *Fit:* the closest external analogue to what `ruflo` is (a harness around a model). Worth watching for MCP-extension patterns and its governance model. If you ever want `ruflo` to look credible next to a "reference" OSS agent, this is the benchmark.

**`bytedance/deer-flow` — 77k★, Python/LangGraph, MIT.** "Long-horizon SuperAgent harness that researches, codes, and creates." v2.0 is a ground-up rewrite: integrated sandboxes, persistent memory, **extensible skills**, sub-agent spawning, aggressive context summarization, multi-provider.
→ *Fit:* double relevance. (a) Conceptual peer to `ruflo`'s swarm/memory. (b) Its **skills + memory + sub-agent** model is the closest live implementation of your deleted **ANA-Blueprint** idea — if you revive extraction-to-skills, steal DeerFlow's skill schema rather than reinventing.

**`johannesjo/parallel-code` — 0.9k★, TS/Electron, MIT.** Runs Claude Code, Codex, and Gemini **side by side, each in its own git worktree**; side-by-side diff review, selective merge.
→ *Fit:* a lightweight, concrete take on `ruflo`'s parallel-swarm premise. The worktree-isolation pattern is exactly how agent parallelism is done safely (this very session's sub-agents use worktree isolation too). Good reference even if you don't adopt it.

### 2. Routing & cost control

**`decolua/9router` — 22k★, JS/Next, MIT.** Local router proxy connecting Claude Code / Codex / Cursor / Cline to **40+ providers** with three-tier fallback (premium → cheap → free), **RTK token compression (20–40% input savings)**, quota tracking, cross-API format translation.
→ *Fit:* maps straight onto `ruflo`'s **3-tier model routing (ADR-026/143)** and the "Fable 5 Orchestrator — cut Claude Code costs" note in your social-media swipe file (#18). If cost is a live concern, this is the most directly usable project in the batch.

### 3. Retrieval

**`infiniflow/ragflow` — 85k★ (biggest in the batch), Go+Python+TS, Apache-2.0.** Production RAG engine: deep document understanding, template-based chunking over PDFs/Word/images, **grounded citations** to cut hallucination, agent capabilities.
→ *Fit:* pairs with `ruflo`'s `ruflo-rag-memory` / `ruflo-knowledge-graph` plugins, and with the document-heavy **qoder** plugins (contract-management, corporate-finance-tax, equity-research all live or die on document grounding). Strong "adopt, don't rebuild" candidate.

### 4. Scraping & cloning

**`D4Vinci/Scrapling` — 70k★, Python/Playwright, BSD-3.** Adaptive scraping: HTTP + browser automation, **anti-bot bypass incl. Cloudflare Turnstile**, adaptive parsing that re-locates elements when a site's DOM changes, Scrapy-like Spider API, proxy rotation, **built-in MCP server**.
→ *Fit:* the most *immediately* useful to your open threads. It's the natural upgrade path for `rulebook-ai` (which already ships `playwright` + `duckduckgo-search`) and for the qoder Playwright submitter. **Caveat re: your Instagram task** — Scrapling beats generic anti-bot walls, but IG's *authenticated* login gate is a different problem; it wouldn't have magically unblocked that post without a logged-in session.

**`JCodesMore/ai-website-cloner-template` — 29k★, TS/Next/shadcn, MIT.** "Clone any website with one command." A Claude-Code `/clone-website` command that recons a URL, extracts the design system/assets, generates component specs, and rebuilds sections with **parallel agent builders** (Opus 4.8 recommended).
→ *Fit:* less about cloning, more a clean reference for **authoring a multi-phase Claude-Code slash-command/skill** — directly transferable to how you build `ruflo` plugins and qoder skills.

### 5. App builder & voice (adjacencies)

**`dyad-sh/dyad` — 21k★, TS/Electron, Apache-2.0 + FSL.** Local, private, open-source Lovable/v0-style app builder; bring-your-own API keys.
→ *Fit:* a product/end-user tool, only loosely related to your harness work. Interesting for its dual-license (`src/pro` under FSL) if you ever monetize.

**`pipecat-ai/pipecat` — 14k★, Python/WebRTC, BSD-2.** Real-time **voice & multimodal** conversational AI; composable pipeline, 50+ services, multi-agent handoff, client SDKs (JS/React/Swift/Kotlin).
→ *Fit:* the only **net-new capability** here — nothing in your repo does real-time voice. File under "expansion option," not "integrate now."

### 6. ⚠️ Dead end

**`daytonaio/daytona` — 72k★, sandboxes, <90ms starts, snapshots.** Great concept (secure elastic infra for AI-generated code), but the repo now says **"no longer maintained" (June 2026)** with core development moved to a private codebase.
→ *Fit:* the *idea* (snapshotable sandboxes for agent steps) matters to any harness, but don't build on this repo. If you need it live, look at maintained alternatives (e.g. E2B, Modal, or Daytona's hosted product).

---

## Cross-cutting signals

- **MCP is the connective tissue.** goose, Scrapling, and the router/cloner ecosystem all expose or consume MCP — the same standard `ruflo` and the qoder plugins are built around. Anything with an MCP server drops into your world with near-zero glue.
- **Claude-Code-native cluster.** parallel-code, 9router, ai-website-cloner, and dyad all target Claude Code directly — closest ecosystem fit, lowest integration cost.
- **Cost & context optimization is a recurring theme** (9router RTK compression, DeerFlow context summarization, `ruflo`'s token-optimizer, swipe-file #18). If you pick one thread to pull, this is the highest-leverage one.
- **Two projects mirror your deleted ANA-Blueprint** almost exactly: DeerFlow (skills + memory + sub-agents) and, structurally, the cloner's multi-phase command. If you revive extraction-to-skills, these are your reference implementations.

## If you extract these to skills next (priority order)

Ranked by relevance × how cleanly they'd become a reusable skill/plugin:

1. **Scrapling** — concrete, MCP-ready, solves a live need. Highest-value skill.
2. **9router** — routing/cost skill that plugs into `ruflo`'s tiering.
3. **RAGFlow** — retrieval skill for the doc-heavy qoder plugins.
4. **DeerFlow** — mine for the skill/memory *schema*, not as a skill itself.
5. **ai-website-cloner** — reference for authoring multi-phase commands.
6–10. goose / parallel-code / dyad / pipecat / daytona — watch/adjacency; daytona only as a concept.

---

*Scope: reference research only — none of these repos are vendored, integrated, or built here. Open follow-ups: deep-dive any single repo, or turn the top picks (Scrapling → 9router → RAGFlow → DeerFlow → ai-website-cloner) into skills. Note that building skills would re-introduce the `anthropic_skills/` structure removed in the `Finalize` commit (`29779d0b`) — confirm placement before doing so.*
