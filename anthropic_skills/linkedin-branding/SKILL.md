---
name: linkedin-branding
description: >
  Builds a LinkedIn personal-branding strategy and content system using the
  four-axis model (Profile Proof, Expertise Visibility, Structured Authenticity,
  Niche Engagement) and the 5-3-2 content ratio. Use when a user wants to grow
  authority on LinkedIn, plan a content calendar, rewrite their profile, or turn
  expertise into a posting cadence. Trigger on: "LinkedIn strategy", "personal
  brand", "LinkedIn content", "grow my LinkedIn", "thought leadership", "content
  calendar", "optimize my profile". Archetype: Workflow Automation.
  Cross-references brand-framework for positioning and social-audit for baseline metrics.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<name or niche> [--profile | --calendar | --post]"
auto-trigger:
  - "LinkedIn strategy"
  - "personal brand"
  - "thought leadership"
  - planning a LinkedIn content calendar or posting cadence
  - rewriting a LinkedIn profile headline/about for authority
do-not-trigger:
  - paid LinkedIn ad campaign setup (different discipline)
  - other platforms without a LinkedIn component (use social-audit)
  - corporate brand strategy with no individual (use brand-framework)
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []
---

# LinkedIn Personal Branding

Turns expertise into consistent authority signals through a four-axis strategy and a repeatable content system.

---

## Step 0 — Define the Authority Position

Before any post, fix the position. One sentence:

```
I help [audience] achieve [outcome] through [unique angle].
```

Everything downstream serves this. If a post doesn't reinforce it, it doesn't ship.

---

## The Four Axes (balance all — not just posting)

| Axis | What it is | Concrete move |
|---|---|---|
| **Profile Proof** | Visual + textual alignment | Headline states outcome, not job title; banner + photo on-brand; About opens with the audience's problem |
| **Expertise Visibility** | Original, useful insight | Each post teaches one thing the audience can use today |
| **Structured Authenticity** | Real human elements, on purpose | Planned personal stories that carry a lesson — not oversharing |
| **Niche Engagement** | Conversing in relevant feeds | Comment substantively on 5–10 niche posts/day; that's distribution, not filler |

A profile with great posts but no engagement stalls. Balance the four.

---

## Content System — the 5-3-2 Ratio

Per **10 posts**:

| Count | Type | Purpose | Example |
|---|---|---|---|
| **5** | Value | Educate | "How to…", frameworks, lessons learned |
| **3** | Authority | Prove | Case studies, results, client outcomes |
| **2** | Human | Connect | Journey, behind-the-scenes, a real failure |

Overall mix ~**80% educational / 20% promotional**. Selling more than 1-in-5 erodes trust.

---

## Format Priority (2026 engagement data)

| Format | Signal | Use for |
|---|---|---|
| **Native video** | 5× engagement of text; growing 2× fastest | Authority + human posts |
| **PDF carousel** | Highest dwell time | Value posts — 1 idea/slide, 8–12 slides max |
| **Text + image** | Reliable baseline | Quick insights, hot takes |
| **Text only** | Lowest reach | Replies, comments, micro-thoughts |

Hook in the first 2 lines (before "…see more"). One idea per post.

---

## Content Calendar Output

```markdown
# LinkedIn Calendar — [Name], [Month]

**Authority position**: [one sentence]

| Day | Type (V/A/H) | Format | Hook (first 2 lines) | Core idea | CTA |
|---|---|---|---|---|---|
| Mon | V | Carousel | | | |
| Wed | A | Video | | | |
| Fri | H | Text+img | | | |

**Engagement plan**: [niche accounts/hashtags to comment on daily]
**Weekly review metric**: [saves + shares + profile views — not raw reach]
```

---

## Profile Rewrite Module (`--profile`)

| Element | Rule |
|---|---|
| Headline | `[Outcome] for [audience]` — not "Senior X at Y" |
| About | Line 1 = audience's pain; then proof; then how to engage |
| Featured | Pin top Authority post or lead magnet |
| Banner | States the position visually |

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Underlying positioning is unclear | `brand-framework` |
| Need a baseline of current metrics across channels | `social-audit` |
| Carousel needs to look designed | `presentation-architect` |
| Claims/stats in a post need verification | `fact-checker` |

---

## Rules

- **Position first** — no content plan without a one-sentence authority position.
- **Balance four axes** — posting alone is one quarter of the system.
- **5-3-2, 80/20** — sell in at most 1 of every 5 posts.
- **One idea per post**, hook in the first two lines.
- **Measure quality** — saves/shares/profile views over impressions.
- **Engagement is distribution** — daily niche commenting is not optional.
