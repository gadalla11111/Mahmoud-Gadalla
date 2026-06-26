---
name: media-buyer
description: >
  Plans, launches, and optimizes paid media campaigns across Meta, Google, TikTok,
  YouTube, and programmatic. Use when a user needs a media plan, budget/bid
  strategy, audience targeting, creative specs, a launch QA checklist, KPI
  framework, optimization playbook, or a client performance report. Trigger on:
  "media plan", "paid media", "ad campaign", "media buying", "Meta/Google/TikTok
  ads", "budget allocation", "bidding strategy", "campaign optimization", "ROAS",
  "CPA". Archetype: Workflow Automation. Covers PAID media; for organic audits use
  social-audit and for organic content use social-content.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<campaign brief or objective> [--plan | --launch | --optimize | --report]"
auto-trigger:
  - media plan or paid media campaign
  - planning or optimizing ad campaigns (Meta / Google / TikTok / YouTube / programmatic)
  - budget allocation, bidding strategy, or audience targeting for paid ads
  - campaign launch QA, KPI framework, or paid-media client report
do-not-trigger:
  - organic social audit (use social-audit)
  - organic content creation — posts/reels (use social-content)
  - brand positioning strategy (use brand-framework)
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Media Buyer

Executes high-performance paid media end to end: plan → launch → optimize →
report. Bridges objective to channel mix to live optimization.

> Distilled from the Media Buyer Master Guide (Nayera Kamel, 2025). Platform
> mechanics drift — verify specs/limits against each platform's current docs
> before launch (WebSearch).

---

## Mode Selection

| Mode | Trigger | Output |
|---|---|---|
| `--plan` | "build a media plan" | Funnel-mapped channel + budget + KPI plan |
| `--launch` | "launch / QA this campaign" | Pre-launch QA checklist run |
| `--optimize` | "optimize / improve performance" | Daily/weekly action list + A/B tests |
| `--report` | "client report" | Story-led performance report |

---

## Planning (`--plan`)

8-step process: **Brief intake → Audience research → Channel selection →
Flighting → Budget allocation → KPI setting → Plan approval → Trafficking.**
Plan bottom-up — solid conversion paths before awareness spend.

**Funnel → channel mapping**

| Stage | Goal | Best channels | Budget % | Primary KPI |
|---|---|---|---|---|
| Awareness | Broad reach | YouTube pre-roll, Meta Reach, Display, TikTok TopView, OOH | 20–30% | Reach, CPM, VCR |
| Consideration | Mid-funnel engagement | Meta Traffic/Engagement, Google Search (generic), Native | 20–25% | Traffic, video views |
| Conversion | Warm intent | Google Search (brand/competitor), Meta Conversions, Retargeting | 35–45% | Leads, CPA, ROAS |
| Retention | Existing customers | Email, CRM retargeting, loyalty, push | 10–15% | ROAS, CVR |

---

## Platform Quick Reference

**Meta** — Campaign (objective, CBO budget) → Ad Set (audience, placement, bid, ABO budget) → Ad (creative, copy, CTA, UTMs).
- Advantage+ Audience for low-data prospecting; ≥50 conversions/week to exit learning
- 3–5 creatives/ad set; broad targeting + strong creative often beats tight segments
- Separate retargeting from prospecting; run CAPI alongside Pixel (iOS14+)
- Frequency cap 3–5×/7d on awareness

**Google** — Search (high intent), Performance Max (broad, data-hungry), Display (awareness/retarget), YouTube (awareness/consideration), Shopping (e-comm), Demand Gen (mid-funnel).
- Match types: Broad → Phrase → Exact; build negatives from day one
- Quality Score (1–10) drives Ad Rank/CPC; always add extensions (sitelinks, callouts, snippets)

---

## Bidding Guide

| Strategy | Platform | When |
|---|---|---|
| Lowest Cost (auto) | Meta, TikTok | Start — gather data |
| Cost Cap | Meta | Control avg CPA, keep volume |
| Bid Cap | Meta, TikTok | Hard CPA ceiling |
| Target CPA | Google | Hit a cost-per-acquisition |
| Target ROAS | Google, Meta | Revenue optimization (needs data) |
| Maximize Conversions | Google | Early phase, spend full budget |
| CPM / vCPM / CPV | Display / YouTube | Awareness / viewability / video |

Rule: start auto-bid, switch to cost-cap or target-CPA after **50+ conversions**.

---

## Audience Targeting

Types: demographic · interest · behavioral · keyword · contextual · custom (CRM/visitors) · lookalike/similar · retargeting · life events · geofencing.

- Layer: start broad, add interest/behavioral layers for efficiency
- Exclude converters from prospecting
- Retargeting windows: 7d hot / 30d warm / 90d cool
- Lookalike: 1–3% quality, 5–10% scale — test both
- Use audience-overlap tools to avoid cannibalization

---

## Creative (the #1 performance variable)

**Specs by placement**

| Placement | Ratio | Dimensions | Video |
|---|---|---|---|
| Meta Feed | 1:1 or 4:5 | 1080×1080 / 1080×1350 | 15–30s, <20% text |
| Meta Stories/Reels | 9:16 | 1080×1920 | 7–15s |
| YouTube pre-roll | 16:9 | 1920×1080 | 15–30s, hook in 5s |
| TikTok in-feed | 9:16 | 1080×1920 | 9–15s, native feel |

**AIDA framework**: Attention (0–2s, stop the scroll) → Interest (2–5s, the hook) → Desire (5–15s, benefit/proof) → Action (clear CTA). A/B test ONE variable at a time.

---

## Launch QA (`--launch`)

Run before go-live:
- **Tracking**: Pixel/CAPI firing on key events; GTM tested; conversions verified; UTMs on all URLs; test lead/purchase event
- **Setup**: right objective; budget level (CBO vs ABO) confirmed; bid strategy aligned; dates set; dayparting if relevant
- **Audience**: defined + confirmed at ad-set level; exclusions added; retargeting ≥1,000; lookalike source ≥1,000 matched
- **Creative**: client/legal approved; specs correct; copy proofed; ≥3 variants/ad set; landing page loads
- **Post-launch 24–48h**: spend pacing; no disapprovals; conversions recording; CPM/CTR/frequency sane; flag anomalies

---

## KPIs by Objective

| Objective | Primary KPIs |
|---|---|
| Awareness | Reach, Impressions, CPM, VCR, Brand Lift |
| Traffic | Clicks, CTR, CPC, LP views, Bounce |
| Engagement | Eng. rate, shares, saves, 3s/10s views |
| Leads | Lead volume, CPL, lead quality, form-fill rate |
| Conversions | Conversions, CPA, CVR, ROAS |
| App installs | Installs, CPI, D7 retention, in-app events |
| E-commerce | Revenue, ROAS, AOV, cart abandonment |

**Attribution**: align window to sales cycle — short purchase = 7d-click; considered (cars, real estate) = 28d-click. DDA when volume allows.

---

## Optimization Playbook (`--optimize`)

**Daily**: spend pacing · CPM trend (spike = competition/fatigue) · CTR (decline = creative fatigue → refresh) · conversion volume · pause creatives <0.5% CTR after 3 days · budget-depletion risk.

**Weekly**: rotate creative (pause bottom-20%, scale top-20%) · demographic breakdown check · placement analysis · search-term review (add converters as exact, junk as negatives) · bid adjustments · landing-page test if CVR drops · reallocate budget to winners.

**A/B tests**: one variable, 7–14 days, then pause loser / scale winner.

---

## Reporting (`--report`)

Structure: Executive summary (did we hit KPIs?) → Performance snapshot (vs target) → Channel breakdown → Creative performance → Audience insights → Optimizations made → Recommendations.

Cadence: daily (internal, pacing) · weekly (AM+client, trends) · monthly (client+mgmt, ROI) · campaign-end (all, lessons).

**Never present raw data — lead with the story**: "2.3× ROAS, driven by Reels outperforming Feed by 40%."

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Organic channel health, not paid | `social-audit` |
| Create the ad creative/scripts | `social-content` → `hyperframes` (render) |
| Underlying brand positioning | `brand-framework` |
| Build the client report deck | `presentation-architect` → `pptx` |
| Verify a market/benchmark stat | `fact-checker` |
| Pull live platform spec/limit | WebSearch |

---

## Rules

- **Plan bottom-up** — conversion paths before awareness spend.
- **Creative is #1** — targeting/bidding can't save bad creative.
- **50+ conversions before tightening bids** — don't starve the learning phase.
- **QA tracking before launch** — no UTMs / no Pixel = blind campaign.
- **One A/B variable at a time.**
- **Report the story, not the data dump.**
- **Verify platform specs live** — they drift; never launch on memorized limits.
