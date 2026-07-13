# Social Media Content Review — kuji.eg swipe file

**Date:** 2026-07-13
**Method:** `anthropic_skills/social-audit` (six-section structure)
**Status:** ⚠️ Partial — see *Access limitation* below. Sections marked **`NEEDS INPUT`** require the actual caption/creative, which is behind a login wall and cannot be fetched automatically.

---

## Access limitation (read first)

Every link supplied is on a login-walled platform. None of the automated paths could read post content:

| Path tried | Result |
|---|---|
| `WebFetch` (Instagram profile + LinkedIn post) | **403 Forbidden** — auth required |
| Ahrefs social-media connector | **Insufficient plan** |
| LunarCrush social search | **Subscription required** |

So the real captions, creative, transcripts, and metrics are **not machine-readable here**. What *is* reliable is URL-decodable metadata: platform, post format (reel vs. carousel vs. single), carousel depth, and — for LinkedIn — the topic embedded in the slug. This review is built on that, with explicit slots to complete once you paste the content.

**Important attribution caveat:** an Instagram shortcode (`/p/…`, `/reel/…`) does **not** encode the author. I cannot confirm which of the `/p/` and `/reel/` links belong to **kuji.eg** vs. other accounts you're collecting as inspiration. Handles are marked *unconfirmed*.

---

## 1. Content Inventory (from URL metadata)

| # | Platform | Account (confirmed?) | Format (decoded) | Topic signal | Notes |
|---|---|---|---|---|---|
| 1 | Instagram | **kuji.eg** (confirmed) | Profile | — | The subject account. Bio/vertical **`NEEDS INPUT`** |
| 2 | Instagram | *unconfirmed* | **Reel** (vertical video) | — | `DZ2cxsiogmj` |
| 3 | Instagram | *unconfirmed* | Feed post (photo/carousel/video) | — | `DadCbdQj1JV` |
| 4 | Instagram | *unconfirmed* | Feed post | — | `DZO308SFYj1` |
| 5 | **Threads** | **@arfaz6214** (confirmed, ≠ kuji) | Text/Threads post | — | Different author — thought-leadership reference? |
| 6 | Instagram | *unconfirmed* | **Carousel ≥ 7 slides** | — | `?img_index=7` → deep carousel. Save-driven format |
| 7 | Instagram | *unconfirmed* | **Reel** (vertical video) | — | `DYdRW7GJK3j` |
| 8 | Instagram | *unconfirmed* | Feed post | — | `DapuR8sDN4E` |
| 9 | **LinkedIn** | **manzar-khokhar** | Text post | **"Are you using Claude for marketing"** | AI-for-marketing POV |
| 10 | **LinkedIn** | **vicky-lalwani** | Text/video post | **CMO · marketing leadership · Claude AI** | AI-for-marketing POV |
| 11 | **LinkedIn** | **abdelghani-eissa** | Text post | **Brand management process** | Brand-ops POV |
| 12 | **Facebook** | *unconfirmed* | Shared post | — | Opaque share ID `1EhHmk7woN` |
| 13 | Instagram | *unconfirmed* | Feed post | — | `DZ6fVA4B_G1` |
| 14 | Instagram | *unconfirmed* | Feed post | — | `DafzlWHmES0` |

**What the mix already tells us (defensible, no content needed):**
- The Instagram set spans **all three feed formats** — reels (×2+), single/mixed feed posts (×6), and at least one **deep 7+ slide carousel**. That format spread is healthy: reels for reach, carousels for saves, singles for cadence.
- The **LinkedIn + Threads cluster is a distinct theme** from the Instagram brand content: it's **"AI/Claude for marketing" thought leadership** (posts 9–11 all point there via their slugs). This looks less like *kuji.eg's own content* and more like **reference material on how to run AI-assisted marketing / brand ops**.
- Read together, this swipe file looks like two piles: **(A) Instagram brand-content inspiration**, and **(B) a POV library on using AI in the marketing workflow.**

---

## 2. Metrics by Platform  —  `NEEDS INPUT`

No metrics are retrievable. Paste per-post numbers (or export from each platform's native insights) and I'll score against the right benchmark per platform — engagement rate is **not** comparable across platforms:

| Platform | Primary metric to pull | 2026 benchmark | Why |
|---|---|---|---|
| Instagram | Eng. rate/post; **reach by format**; **saves + DM shares** | ~0.48% | Shares/saves drive distribution |
| Facebook | Referral traffic; native-video organic reach | ~0.15% | Organic engagement is low — measure traffic |
| LinkedIn | **Saves, shares, profile views, dwell** | — | Authority signals over raw reach |
| Threads | Replies + reshares | — | Conversation velocity is the signal |

> Rule from the audit method: rank **saves + shares + replies** above impressions/followers — they predict algorithmic distribution far better.

**To complete:** for each numbered link above, give me `format → reach → likes → comments → saves → shares` (whatever you have).

---

## 3. Audience Insights  —  `NEEDS INPUT`

Needs: kuji.eg's **target** audience (who you want) vs. **actual engaged** audience (IG insights: top locations, age, gender, active hours). The gap between the two is the finding. Provide the vertical/positioning of kuji.eg — currently unknown — so this can be assessed.

---

## 4. Top & Low Performers  —  partial

Cannot rank without metrics (§2). What can be said now is **format-pattern** guidance to apply once ranked:

- **Native vertical video (reels 2, 7)** should out-reach static feed posts — if they don't, the hook (first 1–2s) is the likely culprit.
- **The 7+ slide carousel (6)** is the natural **save magnet** — check its saves-per-reach; if high, that topic/format is your replicable winner.
- Flag any **cross-posted static** (same file pushed to IG + FB + LinkedIn) as a probable drag — platform-native formats win in 2026.

**To complete:** once §2 is filled, I'll populate:

| Post | Platform | Metric | Pattern behind it |
|---|---|---|---|
| _top_ | | | |
| _low_ | | | |

---

## 5. Competitive Benchmark  —  `NEEDS INPUT`

Name 2–3 competitors of kuji.eg (ideally Egyptian / same vertical) and I'll pull public follower + engagement trends (with sources + access dates). No benchmark numbers from memory — the method forbids it.

---

## 6. Prioritized Action List (provisional)

Ordered by **impact ÷ effort**. Items 1–3 are executable now from the inventory; 4–6 unlock once you paste content/metrics.

| # | Action | Platform | Owner | Expected impact | Effort |
|---|---|---|---|---|---|
| 1 | **Confirm account attribution** — tag each `/p/` & `/reel/` link as *kuji.eg's own* vs. *inspiration*. Splits the file into "audit my content" vs. "study competitors" | All IG | You | High (unblocks everything) | Low |
| 2 | **Lock the two-pile purpose** — decide if pile B (LinkedIn "Claude for marketing") is a *workflow* reference (how you'll produce content) or *content* to emulate | LinkedIn/Threads | You | Med | Low |
| 3 | **Double down on carousels + reels** — the mix already shows a deep carousel and reels; formalize a weekly cadence: 1 reel (reach) + 1 carousel (saves) + singles for consistency | Instagram | Content | High | Med |
| 4 | **Score every post on saves/shares**, not likes — rebuild §2 table, then promote the top save-driver's topic into a series | Instagram | Analyst | High | Low* |
| 5 | **Kill cross-posts** — audit for the same file appearing on IG+FB+LI; re-cut per platform | All | Content | Med | Med |
| 6 | **Benchmark 2–3 named rivals** on follower trend + engagement to set realistic targets | All | Analyst | Med | Med |

\* low effort *after* metrics are supplied.

---

## How to finish this review

Paste any of the following and I'll complete the matching section in place:

1. **Captions / transcripts** for each numbered link (or screenshots) → completes §1 topics, §4 patterns.
2. **Native insights** per post (reach, saves, shares, comments) → completes §2, §4.
3. **kuji.eg positioning** — what it sells, target customer, current bio → completes §3.
4. **2–3 competitor handles** → completes §5.
5. **Attribution** — which links are kuji.eg's own → resolves Action #1.

The fastest unlock is a screenshot of each post's caption + the insights panel; from there this becomes a fully populated, data-backed audit rather than a metadata skeleton.
