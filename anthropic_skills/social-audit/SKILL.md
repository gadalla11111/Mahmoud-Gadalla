---
name: social-audit
description: >
  Audits social media presence across platforms and produces a prioritized
  recommendations report. Use when a user wants to evaluate their social
  channels, benchmark against competitors, or get a data-backed action list.
  Six-section structure: profile inventory, metrics by platform, audience
  insights, top/low performers, competitive benchmark, prioritized actions.
  Trigger on: "audit my social", "social media audit", "review my channels",
  "social media report", "how are my pages doing", "benchmark against competitors".
  Archetype: Judgment Amplifier. Cross-references linkedin-branding for LinkedIn
  deep-dives and brand-framework when positioning gaps surface.
allowed-tools: [WebSearch, WebFetch, Read, Write, Bash]
argument-hint: "<brand/handle> [--platforms ig,fb,x,li,tiktok] [--competitors @a,@b]"
auto-trigger:
  - "social media audit", "audit my social", "review my channels"
  - benchmarking social channels against competitors
  - producing a prioritized social recommendations report
do-not-trigger:
  - building a content calendar from scratch (use linkedin-branding or brand-framework)
  - one-off post performance question
  - paid-ad-only performance review
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Social Media Audit

Evaluates social presence and exits with a prioritized, owned action list — not just a data dump.

---

## The Six-Section Structure

Every audit produces these six, in order:

1. **Profile Inventory** — every handle, URL, follower count, last-active date, bio consistency
2. **Key Metrics by Platform** — the right metric per platform (see benchmarks)
3. **Audience Insights** — who's actually engaging vs. who you're targeting
4. **Top & Low Performers** — best/worst content, with the pattern behind each
5. **Competitive Benchmark** — follower trend + engagement vs. 2–3 named rivals
6. **Prioritized Action List** — ranked fixes, each with an owner and expected impact

---

## Platform-Specific Metrics (use the right one)

Engagement rate is not comparable across platforms. Audit each on what its algorithm rewards:

| Platform | Primary metric | 2026 benchmark | Why |
|---|---|---|---|
| **Instagram** | Engagement rate/post; reach by format; DM shares | ~0.48% | Shares/saves drive distribution |
| **Facebook** | Referral traffic; paid CPM/CTR/CPL; native-video organic reach | ~0.15% | Organic engagement is low — measure traffic |
| **X** | Reach per post; text-vs-link impression rate | ~0.12% | Use reach, not engagement (too low to read) |
| **LinkedIn** | Saves, shares, profile views, dwell | — | Authority signals over raw reach |
| **TikTok** | Watch-through rate; shares; sound adoption | — | Completion beats follower count |

**Universal rule**: saves + shares + replies signal algorithm-worthy content far more reliably than impressions or follower counts.

---

## Audit Cadence (recommend to the user)

| Frequency | Reviews | Metrics |
|---|---|---|
| **Monthly** | Operational | Engagement rate/channel, reach, posting frequency, MoM change |
| **Quarterly** | Strategic | Social referral traffic, conversion rate, follower trend vs. competitors |

---

## Content Performance Diagnosis

For top and low performers, identify the *pattern*, not just the post:

- Format: did native vertical video / carousel beat cross-posted statics? (it should)
- Hook: first 3 seconds / first 2 lines
- Cadence: consistency vs. sporadic
- Topic-audience fit: did it serve the priority audience?

Flag cross-posted static content as a likely drag — platform-native formats win in 2026.

---

## Output Format

```markdown
# Social Media Audit — [Brand], [Date]

## 1. Profile Inventory
| Platform | Handle | Followers | Last active | Bio consistent? |

## 2. Metrics by Platform
| Platform | Primary metric | Value | Benchmark | Verdict |

## 3. Audience Insights
[targeted vs. actual engaged audience — gaps]

## 4. Top & Low Performers
| Post | Platform | Metric | Pattern behind it |

## 5. Competitive Benchmark
| Competitor | Followers | Eng. rate | Trend vs. us |

## 6. Prioritized Action List
| # | Action | Platform | Owner | Expected impact | Effort |
|---|---|---|---|---|---|
| 1 | | | | High | Low |
```

Order the action list by **impact ÷ effort** — quick high-impact wins first.

---

## Research Discipline

- Pull competitor public metrics via WebSearch/WebFetch — cite the source and access date
- Flag any metric estimated vs. measured
- Note where platform API data would sharpen the audit if available

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| LinkedIn needs a full content system | `linkedin-branding` |
| Audit reveals a positioning/identity gap | `brand-framework` |
| Recommendations become a client deck | `presentation-architect` |
| Competitor claims need verification | `fact-checker` |

---

## Rules

- **Six sections, in order** — an audit without a prioritized action list is just analytics.
- **Right metric per platform** — never compare IG engagement to X engagement directly.
- **Quality signals over reach** — rank saves/shares/replies above impressions.
- **Every action has an owner and an impact estimate** — recommendations without ownership don't ship.
- **Cite competitor data** — no benchmark numbers from memory.
