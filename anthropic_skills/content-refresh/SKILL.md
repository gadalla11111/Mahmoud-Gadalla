---
name: content-refresh
description: >
  Refreshes decaying articles to recover lost organic traffic. Finds pages whose
  traffic is sliding, diagnoses why (outdated info, slipped rankings, thin vs new
  competitors, stale dates, lost SERP features), and produces a prioritized refresh
  plan with before/after changes per page. Use when a user wants to win back
  traffic from existing content rather than write new posts. Trigger on: "refresh
  stale content", "recover lost traffic", "update old articles", "content decay",
  "why is this page dropping". Archetype: Judgment Amplifier. Cross-references
  claude-seo for AI-citation optimization and social-audit is unrelated (organic
  social).
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<URL or content set> [--audit | --plan]"
auto-trigger:
  - refresh stale content or recover lost traffic
  - update old articles / fix content decay
  - why is this page dropping in search
do-not-trigger:
  - writing brand-new content from scratch (use doc-coauthoring)
  - AI-answer-engine citation optimization only (use claude-seo)
  - social channel performance (use social-audit)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Content Refresh

Recovers organic traffic from content you already have. Decaying pages are usually
cheaper to fix than new ones are to rank — find the slide, diagnose it, refresh
with intent.

---

## Why Content Decays

| Cause | Signal |
|---|---|
| **Outdated info** | Year/stats/screenshots are old; "best X in 2023" |
| **Slipped rankings** | Position drifting down over months |
| **Outranked** | A newer, deeper competitor page now wins the query |
| **Stale dates** | No "last updated"; engines favor fresh |
| **Lost SERP features** | Dropped from featured snippet / People Also Ask |
| **Intent drift** | What searchers want for the query has changed |

---

## Process

1. **Find the decay** — pages with a downward traffic/position trend (use analytics/Search Console if connected; otherwise the user's export).
2. **Diagnose per page** — which cause(s) above; check the current top-ranking results for the target query to see what now wins.
3. **Prioritize** — refresh pages with the best *traffic-recovery ÷ effort*: high prior traffic, fixable cause, still-relevant topic.
4. **Plan the refresh** — specific before/after edits, not "improve the page".
5. **Re-publish signals** — update the date, re-promote, and (if structure changed) refresh internal links.

---

## Refresh Plan Output

```markdown
# Content Refresh — [site/section]

## Decaying pages (prioritized)
| Page | Traffic trend | Cause | Recovery potential | Effort |
|---|---|---|---|---|

## Per-page plan
### [URL]
- **Diagnosis**: [cause(s)]
- **Before → After**:
  - [outdated stat → current, cited]
  - [thin section → expanded to match what now ranks]
  - [missing → add FAQ / schema / comparison the SERP rewards]
- **Freshness**: update date, refresh internal links, re-promote
- **Expected**: [recover ~X% / regain snippet]
```

---

## Discipline

- Check the **current SERP** for each target query before planning — don't guess what now ranks; model it.
- Verify any stat you add or update with `fact-checker`; a refreshed page with a wrong number is worse than a stale one.
- Don't gut a page that still ranks — refresh surgically.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Optimize for AI answer engines (GEO) | `claude-seo` |
| Write a brand-new piece instead | `doc-coauthoring` |
| Stats need verifying | `fact-checker` |
| Deep competitive SERP research | `deep-research` |

---

## Rules

- **Diagnose before editing** — name the decay cause per page.
- **Model the current SERP** — refresh to beat what ranks *now*, not what used to.
- **Prioritize recovery ÷ effort** — fix the high-traffic, low-effort pages first.
- **Specific before/after** — never "improve the page".
- **Verify added stats** — and always update the freshness date.
