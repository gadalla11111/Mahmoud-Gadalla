---
name: news-research
description: >
  News-first research skill. Use when the user asks about current events,
  recent developments, or anything time-sensitive. Prioritizes primary
  sources and original reporting over aggregators, summaries, or
  AI-generated content. Always surfaces publication date, outlet, and
  author for every claim.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "[topic or question]"
---

# News Research

Research protocol for time-sensitive topics. Primary sources first, synthesis second.

---

## Source hierarchy (strict priority order)

1. **Original reporting** — bylined articles from established news outlets, published within the relevant time window
2. **Official statements** — press releases, government announcements, company blog posts, regulatory filings
3. **Expert commentary** — named experts in attributed quotes, academic preprints with methodology
4. **Secondary analysis** — aggregator summaries, newsletters, editorial opinion (clearly labeled as such)

Never cite AI-generated news summaries, anonymous posts, or unattributed social media as facts.

---

## Research process

### Step 1 — Establish time window
Before searching: what time range is relevant? (last 24h / week / month / year)
Use this to filter results and flag outdated sources.

### Step 2 — Primary search pass
Search for: `[topic] site:[major-news-outlet]` and `[topic] news [date-range]`
Target: original reporting, official statements.

### Step 3 — Source verification
For each key claim:
- Who reported it first?
- Has it been independently confirmed by a second outlet?
- Is the original source reachable (WebFetch the URL)?

### Step 4 — Synthesis
Combine verified findings. For contested or evolving stories, present multiple credible perspectives rather than flattening to a single narrative.

---

## Output format

```
## What we know (verified)
[Claim] — [Outlet], [Author], [Date], [URL]

## What is reported but unconfirmed
[Claim] — [Source type], [Date] — [why unconfirmed]

## What is contested
[Claim]: [Outlet A says X] vs [Outlet B says Y]

## Timeline
[Chronological list of key events with dates and sources]

## Source quality note
[Brief assessment of source landscape — e.g., "Only one outlet has reported this; no independent confirmation yet"]
```

---

## Rules

- Every factual claim gets a source citation (outlet + date + URL)
- Publication date must be explicitly stated — never omit it for time-sensitive topics
- If the most recent available information has a gap (e.g., "as of [date], no update found"), say so
- Distinguish "reported" from "confirmed" from "alleged"
- If WebSearch results are dominated by aggregators with no original reporting, say so and note the limitation
