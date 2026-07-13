# Social Media Content Review — "Claude / AI for Marketing" swipe file

**Date:** 2026-07-13
**Method:** `anthropic_skills/social-audit` (audit rigor) framed as a **competitor / genre teardown** — because that's what the material turned out to be.
**For:** kuji.eg content strategy
**Status:** Substantially populated from supplied screenshots + uploaded videos. Items still behind login are marked **`UNSEEN`**.

---

## What this swipe file actually is

The original assumption ("audit kuji.eg's own posts") is **wrong** — confirmed by the content the user supplied. The n8nstack screenshot proved link #13 belongs to **n8nstack, not kuji.eg**, and the uploaded reels belong to **@RAYCFU** and an orange-branded MCP creator. The user also confirmed: **these are reference/inspiration, not their own content.**

So this is a **swipe file of other creators' content in one tight niche: "Claude & AI, made practical for marketers and developers."** The job is to reverse-engineer the genre so kuji.eg can produce it.

**The genre in one line:** dense, *educational* listicle content (carousels, silent caption-reels, single-image infographics) that teaches a Claude/AI workflow and converts via a **comment-to-DM lead magnet.**

---

## 1. Content Inventory (20 supplied assets, deduped)

Legend: ✅ seen (content captured) · 🟡 topic known from slug/title · ⬜ UNSEEN

| # | Source | Account | Format | Seen | Hook / Topic | CTA |
|---|---|---|---|---|---|---|
| 1 | IG profile | **kuji.eg** | Profile | ⬜ | subject account — vertical still unknown | — |
| 2 | IG reel `DZ2cxsiogmj` | ? | Reel | ⬜ | *(may = one of the uploaded reels)* | — |
| 3 | IG post `DadCbdQj1JV` | ? | Feed | ⬜ | — | — |
| 4 | IG post `DZO308SFYj1` | ? | Feed | ⬜ | — | — |
| 5 | Threads | **@arfaz6214** | Text | ⬜ | — | — |
| 6 | IG post `DZuHZfSDj2-` | ? | **Carousel ≥7** | ⬜ | *(may = "10 Skills" infographic set)* | — |
| 7 | IG reel `DYdRW7GJK3j` | ? | Reel | ⬜ | *(may = one of the uploaded reels)* | — |
| 8 | IG post `DapuR8sDN4E` | ? | Feed | ⬜ | — | — |
| 9 | LinkedIn | **manzar-khokhar** | Text | 🟡 | "Are you using **Claude for marketing**" | — |
| 10 | LinkedIn | **vicky-lalwani** | Text/video | 🟡 | CMO · marketing leadership · **Claude AI** | — |
| 11 | LinkedIn | **abdelghani-eissa** | Text | 🟡 | **Brand-management process** | — |
| 12 | Facebook | ? | Shared post | ⬜ | — | — |
| 13 | IG post `DZ6fVA4B_G1` | **n8nstack** | Single infographic | ✅ | "**What Happens When You Call Any LLM API** (~400ms)" | none (pure educational) |
| 14 | IG post `DafzlWHmES0` | ? | Feed | ⬜ | — | — |
| 15 | Upload (reel, 4 seg, silent) | **@RAYCFU** | Carousel-video | ✅ | "**These are the 8 Claude skills that actually matter**" | comment **"SKILLS"** → DM guide |
| 16 | Upload (reel, 57s, +audio) | orange creator | Reel | ✅ | "if you're using **claude code**… [MCP servers you're missing]" | comment **"MCP"** → DM |
| 17 | Upload (image ×2) | Claude-branded | Infographic | ✅ | "**10 Claude Skills for Marketing**" | — |
| 18 | Upload (image + text) | ? | Diagram | ✅ | "**Fable 5 Orchestrator** — cut Claude Code costs" | — |

> Likely overlaps: uploads #15/#16 probably **are** the content behind reel links #2/#7, and #17 may be carousel #6. Shortcodes don't encode content, so I can't hard-map them — confirm if it matters.

---

## 2. Confirmed content — what each seen asset does

### #13 — n8nstack · "What Happens When You Call Any LLM API" (single infographic)
- **Metrics (real):** 2.6K likes · 21 comments · **116 shares** · saved · Jun 23
- **Body:** system-diagram of the LLM request path (API gateway → tokenization → model routing → GPU inference → safety → streaming → logging/billing); payoff line *"95% of the wait isn't the API call — it's the model thinking."*
- **Pattern:** shares (116) ≫ comments (21) = **reference/save content**. People bookmark and share diagrams. No CTA — pure reach/authority play. This is the "make-it-make-sense" explainer archetype.

### #15 — @RAYCFU · "The 8 Claude skills that actually matter" (silent carousel-video)
- **Structure captured:** *For Design* → (1) Frontend Design ("still the best — escapes the generic AI look, uses real design systems"), (2) Canvas Design ("plain text → social graphics, posters, covers"). *For Developers Pt 1* → (3) Superpowers ("TDD, structured debugging, plan-to-execute"), (4) Remotion ("AI video generation in Claude"). *For Developers Pt 2* → (5) Context Optimization ("KV-cache tricks, lower token cost — install this first if you're hitting usage limits"). (+3 not captured.)
- **CTA (the engine):** *"I created a step-by-step guide with exact prompts… like this post and comment **'SKILLS'** and I'll send it to you."*
- **Pattern:** **comment-to-DM lead magnet** — engineered to farm comments (algorithm fuel) + build a DM list. Silent + fully captioned = optimized for feed autoplay.

### #16 — orange creator · "5 MCP servers for Claude Code" (57s reel, has audio)
- **Structure captured:** #1 Perplexity MCP · #2 Playwright MCP ("control tabs, buttons for you") · #3–#4 (agent/website/AI-image examples incl. Machina Sports) · #5 Chrome MCP → "install [MCP hub]" → **"Comment 'MCP' for free."**
- **Pattern:** identical comment-to-DM mechanic; numbered-countdown format; strong negative-hook ("Stop using Claude Code as a fancy chatbot").
- ⚠️ Audio VO not transcribed (no offline STT available; captions carry the full script). Adobe cloud transcription available on request.

### #17 — "10 Claude Skills for Marketing" (Claude-branded infographic)
- **List:** Campaign audit · Landing-page audit · A/B-test analyzer · Competitor teardown · UTM generator · Email sequence · Content repurposer · ICP builder · Ad-copy matrix · Creative brief. (Maps almost 1:1 to this repo's `anthropic_skills/*` marketing skills.)
- **Pattern:** clean numbered list + emoji + one-line "paste X, get Y" benefit each. Highly save-able reference card.

### #18 — "Fable 5 Orchestrator" (diagram + caption)
- **Content:** cost-cutting setup — Fable 5 orchestrates, delegates deep reasoning to Opus and mechanical work to Sonnet via two subagents + a CLAUDE.md.
- ⚠️ **Verify before reuse:** the caption states specific Claude model prices ("$10/$50 per M tokens, 2× Opus, 3–5× Sonnet"). Do **not** reprint these as fact without checking against `anthropic_skills/claude-api` — model pricing claims age fast and are easy to get wrong.

---

## 3. Cross-cutting genre patterns (the replicable playbook)

1. **One workflow per post.** Every winner teaches a single, concrete AI workflow — not "AI is amazing," but "here are the 8 skills / 5 MCP servers / what an API call does."
2. **Two content jobs, two formats:**
   - **Reach/authority** → dense *single-image or carousel infographics*, no CTA (n8nstack, "10 Skills"). Optimized for **saves + shares**.
   - **List-building** → *silent captioned reels* ending in **comment-to-DM** (@RAYCFU, MCP reel). Optimized for **comments**.
3. **Comment-to-DM is the growth engine.** "Comment 'SKILLS'/'MCP' and I'll send it" manufactures comment volume (ranking signal) and a DM funnel. This is the single most copyable mechanic here.
4. **Negative / curiosity hooks.** "Stop using Claude Code as a fancy chatbot", "the skills that *actually* matter", "what *really* happens when…".
5. **Silent-first video.** Reels are fully burned-in captioned and readable with sound off.
6. **Named specifics over vague tips.** Perplexity, Playwright, Chrome MCP, Remotion, KV-cache — concrete named tools/skills, never "productivity hacks."

---

## 4. Metrics · Audience · Benchmark — `NEEDS INPUT`

Only #13's metrics are known (2.6K/21/116). Per the audit method, rank **saves + shares + comments** over likes/reach. To complete: native insights for the other seen posts, kuji.eg's positioning/target audience, and 2–3 competitor handles (n8nstack and @RAYCFU are natural benchmarks — both operate this exact genre).

---

## 5. Prioritized Action List for kuji.eg

Ordered by impact ÷ effort.

| # | Action | Format | Expected impact | Effort |
|---|---|---|---|---|
| 1 | **Adopt the comment-to-DM lead magnet** — pick one flagship guide (e.g. "10 Claude Skills for Marketing"), post a captioned reel ending in "comment 'X' and I'll send it" | Reel | High (comments + DM list) | Low |
| 2 | **Build a save-bait infographic series** in the n8nstack/"10 Skills" mold — one AI workflow per graphic, diagram-led, no CTA | Single/carousel | High (reach via shares) | Med |
| 3 | **Run the two-format cadence:** 1 authority infographic (saves) + 1 lead-magnet reel (comments) per week | Both | High | Med |
| 4 | **Steal the hook formulas** — negative ("Stop using…"), authority-filter ("the ones that *actually* matter"), curiosity ("what really happens…") | All | Med | Low |
| 5 | **Caption everything, silent-first** — full burned-in text, sound optional | Reels | Med | Low |
| 6 | **Fact-check any Claude pricing/model claims** against `claude-api` before publishing (see #18) | All | Med (credibility) | Low |
| 7 | Benchmark n8nstack + @RAYCFU on follower/engagement trend to set targets | — | Med | Med |

---

## 6. Still missing (to fully close the audit)

- **kuji.eg's own positioning + vertical** — still unknown; needed for §4 and to tailor the playbook.
- **UNSEEN links** #2,3,4,5,7,8,12,14 — captions/screenshots would confirm the likely overlap with uploads and complete the inventory.
- **LinkedIn #9–11** bodies — topics known, full text would sharpen the "Claude-for-marketing POV" angle.
- **MCP-reel VO** — on request via Adobe cloud transcription.

---

## Appendix — assets set aside

The batch also included GitHub links to red-team / adversary-emulation frameworks (atomic-red-team, CALDERA, Infection Monkey, Red-Teaming-Toolkit, prelude). These are legitimate published security-testing tools but are **out of scope** for a social-content review and carried no instruction, so they are not analyzed here. Flag if they were meant for a separate task.
