# Web-Scraping & Content-Extraction Tooling — scan of 6 repos

**Date:** 2026-07-19
**Method:** one WebFetch per repo (public GitHub landing page + README). Star counts are **approximate** (read off the page, rounded). Capability notes reflect what each README claims.
**Lens:** these are all **scrape / crawl / extract** tools — evaluated for JS rendering, anti-bot/stealth, auth/login, LLM-markdown output, and MCP, then mapped to this repo's needs (`rulebook-ai`'s Playwright + search stack, the doc-heavy `qoder` plugins, and the open **Instagram-scraping** thread).
**See also:** `research/ai-agent-tooling-scan-2026-07.md` — its **Scrapling** pick is the same category and overlaps heavily with the LLM-scraper tier below.

---

## At a glance

| Repo | Sub-category | Stars≈ | Stack | License | JS render | Anti-bot | Auth/login | LLM-markdown | MCP | Fit |
|---|---|---|---|---|---|---|---|---|---|---|
| `unclecode/crawl4ai` | LLM scrape→markdown | 73k | Python (Playwright) | Apache-2.0 | ✅ | ✅ stealth+proxy | ✅ profiles | ✅ "fit" md | ✅ | ★★★ best overall fit |
| `firecrawl/firecrawl` | LLM scrape→markdown (API) | 153k | TS + Py | AGPL-3.0 (SDKs MIT) | ✅ | ✅ proxies | ⚠️ interactions | ✅ md/JSON | ✅ | ★★★ fastest to value |
| `browser-use/browser-use` | Agentic browser | 106k | Python (Playwright) | MIT | ✅ | via real browser | ✅ profiles/sessions | agent output | ✅ | ★★★ the auth/IG angle |
| `microsoft/markitdown` | File→markdown (not scraping) | 167k | Python | MIT | n/a | n/a | n/a | ✅ (files) | companion* | ★★☆ doc pipeline |
| `apify/crawlee` | Framework (JS-first) | 25k | Node/TS (+Py) | Apache-2.0 | ✅ PW/Puppeteer | ✅ fingerprints/TLS | manual | ✗ raw | ✗ | ★★☆ custom crawlers |
| `scrapy/scrapy` | Framework (classic) | 63k | Python | BSD-3 | ✗ (needs plugin) | manual | ✅ | ✗ raw | ✗ | ★☆☆ mature, heavy |

\* markitdown: the fetch didn't surface an MCP server; Microsoft publishes a companion `markitdown-mcp` package — verify coverage before relying on it.

---

## By sub-category

### 1. LLM scrape→markdown (the "paste a URL, get clean content" tier)

**`unclecode/crawl4ai` — 73k★, Python/Playwright, Apache-2.0.** OSS crawler purpose-built to turn sites into clean, "fit" markdown + JSON for LLM/RAG. Full JS execution, **undetected/stealth mode with proxy escalation**, **session/auth persistence via browser profiles**, Docker + FastAPI server, and an **MCP server** for direct Claude wiring.
→ *Fit:* **best overall adopt candidate for you.** Self-hostable, permissive license, Python (matches `rulebook-ai`), MCP-native (matches `ruflo`/`qoder`), and it covers the whole spectrum (stealth + auth + LLM output) in one library.

**`firecrawl/firecrawl` — 153k★, TS+Python, AGPL-3.0 (SDKs MIT).** The API-first version of the same idea: search + scrape + "agent" extraction, JS rendering, managed proxy rotation, markdown/JSON/screenshots, `firecrawl-mcp-server`, hosted cloud **or** self-host.
→ *Fit:* **fastest to value if you're OK with a hosted API** (or the AGPL self-host terms). Best-in-class managed scraping with an MCP server. The AGPL license matters only if you'd embed the self-hosted engine into something you distribute — as a service/API it's a non-issue.

*crawl4ai vs firecrawl:* same job, different posture — crawl4ai is the **library you run** (Apache, no strings), firecrawl is the **service you call** (managed, AGPL core). Both overlap with Scrapling from the prior scan; pick one of the three, not all.

### 2. Agentic browser (the tool that can actually log in)

**`browser-use/browser-use` — 106k★, Python/Playwright, MIT.** LLM-driven browser that clicks/types/fills/extracts like a human; renders JS natively, **navigates authenticated sites via saved profiles/sessions**, works with **Claude**/GPT/Gemini, and installs as an MCP skill. Ranks #1 on the Odysseys web-task leaderboard.
→ *Fit:* **the most relevant tool to the Instagram wall.** Unlike the scrape-to-markdown tier, an agent driving a *logged-in* browser is the realistic way past an authenticated gate.
→ ⚠️ **Honest caveat (same as before):** logging a bot into Instagram runs into ToS/anti-automation, 2FA/checkpoints, and flakiness. browser-use makes it *possible*, not *clean or durable* — for the one `Dac5qmEgdJx` post, screenshots are still the faster, lower-risk path. Reserve this for when you need repeatable authenticated extraction and accept the maintenance/policy cost.

### 3. General-purpose scraping frameworks (code-first, not LLM-specific)

**`apify/crawlee` — 25k★, Node/TS (also Python), Apache-2.0.** Mature framework unifying HTTP + headless (Playwright/Puppeteer) crawling, with strong **built-in anti-bot** (browser fingerprints, TLS replication, human-like headers), proxy rotation, persistent URL queues, and autoscaling.
→ *Fit:* reach for this when you're **building a real, large crawler** (TS-native — pairs with the `qoder` Playwright submitter). Its anti-bot fingerprinting is the strongest in this batch, but output is raw data, not LLM-markdown.

**`scrapy/scrapy` — 63k★, Python, BSD-3.** The long-established Python framework (Zyte-backed). Huge ecosystem, battle-tested at scale, but **no JS rendering by default** (needs `scrapy-playwright`) and no LLM-specific output.
→ *Fit:* only if you want the classic, plugin-rich framework for structured large-scale scraping. For LLM-ready content it's the heaviest path here — crawl4ai gets you there with far less assembly.

### 4. File→markdown conversion (a different job that completes the pipeline)

**`microsoft/markitdown` — 167k★, Python, MIT.** **Not a scraper.** Converts PDF/Word/PowerPoint/Excel/images (OCR)/audio (transcription)/HTML/CSV/JSON/EPub/YouTube into structure-preserving Markdown for LLMs; optional Azure Document Intelligence backend.
→ *Fit:* orthogonal and low-risk — it's the **"I already have the file, make it LLM-readable"** step. Complements **RAGFlow** (prior scan) and is a natural fit for the doc-heavy `qoder` plugins (contract-management, corporate-finance-tax, equity-research) where inputs arrive as Office/PDF, not URLs.

---

## Cross-cutting signals

- **Two axes decide everything here:** (a) *hosted API vs self-hosted library* — firecrawl on one end, crawl4ai/crawlee/scrapy on the other; (b) *LLM-markdown output vs raw framework* — crawl4ai/firecrawl vs crawlee/scrapy. Your stack (Python, MCP-heavy, Claude-centric) points to **self-hosted + LLM-markdown = crawl4ai**.
- **MCP is again the connective tissue.** crawl4ai, firecrawl, and browser-use all expose MCP, so they drop into `ruflo`/`qoder`/Claude Code with near-zero glue. crawlee and scrapy don't.
- **Scrape ≠ extract ≠ convert.** The clean pipeline is: *get it off the web* (crawl4ai/firecrawl, or browser-use behind a login) → *if it's a file, convert it* (markitdown) → *ground/retrieve* (RAGFlow, prior scan). These compose rather than compete.
- **This batch overlaps the last one.** Scrapling (prior) ≈ crawl4ai ≈ firecrawl on the anti-bot Python-scraping axis. Don't adopt all — one LLM-scraper + browser-use for auth covers the field.

## Recommendation (fit order for this repo)

1. **crawl4ai** — adopt as the default scrape→markdown engine: OSS, Python, MCP, stealth + auth, permissive. Highest-value, lowest-friction.
2. **browser-use** — add for **authenticated / agentic** tasks (the Instagram angle), accepting the ToS/reliability caveat.
3. **markitdown** — adopt for the **doc→markdown** step in `qoder`/RAG pipelines; orthogonal, near-zero risk.
4. **firecrawl** — pick over crawl4ai only if you'd rather call a managed API than run a library.
5. **crawlee / scrapy** — only for a large bespoke crawler; heavier and not LLM-shaped.

---

*Scope: reference research only — none of these repos are vendored, integrated, or built here. Companion to `research/ai-agent-tooling-scan-2026-07.md`. Open follow-ups: deep-dive any single tool, stand up a crawl4ai/browser-use MCP proof-of-concept, or (separately) resume the Instagram `Dac5qmEgdJx` teardown, which is still waiting on screenshots or caption text rather than any tool here.*
