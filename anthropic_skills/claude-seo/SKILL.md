---
name: claude-seo
description: >
  Generative Engine Optimization (GEO) — optimize content to be cited by AI
  answer engines (Claude, ChatGPT, Perplexity, Google AI Overviews), not just
  ranked by classic search. Use when a user wants content that AI search surfaces
  and quotes: structuring for extractability, citation-worthiness, and entity
  clarity. Trigger on: "SEO for AI", "GEO", "rank in AI search", "get cited by
  ChatGPT/Perplexity", "AI Overviews optimization", "answer-engine optimization".
  Archetype: Judgment Amplifier. Cross-references deep-research for SERP/answer
  analysis and fact-checker for citation integrity.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<topic, URL, or draft> [--audit | --optimize | --brief]"
auto-trigger:
  - "SEO for AI search"
  - GEO or generative engine optimization
  - get cited by ChatGPT, Perplexity, or AI Overviews
  - making content extractable and quotable by answer engines
do-not-trigger:
  - classic keyword-density / backlink SEO only (different discipline)
  - paid search / SEM campaign setup
  - social media reach (use social-audit)
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Claude SEO — Generative Engine Optimization

Optimizes content so AI answer engines **cite and quote** it. Classic SEO targets a ranked link; GEO targets being the sentence the model repeats.

---

## What AI engines reward (different from classic SEO)

| Classic SEO | GEO (answer engines) |
|---|---|
| Keyword density | Direct, extractable answers |
| Backlinks | Citation-worthiness + source authority |
| Title/meta tuning | Clear entity definitions, structured facts |
| Ranking position | Being *quoted* in the generated answer |
| Page-level | Passage-level (a single quotable chunk) |

The unit of optimization is the **passage**, not the page. Answer engines lift self-contained chunks.

---

## Mode Selection

| Mode | Trigger | Output |
|---|---|---|
| `--audit` | "how does my content do in AI search" | Gap report vs. GEO best practice |
| `--optimize` | "make this citable" | Rewritten content, passage-structured |
| `--brief` | "what should I write to rank" | GEO content brief before drafting |

---

## The GEO Checklist (apply to every page)

1. **Lead with the answer.** First sentence of each section answers the implied question directly — no warm-up. Engines lift the first clear claim.
2. **Self-contained passages.** Each heading's first paragraph must make sense quoted alone, with the entity named (not "it"/"this").
3. **Explicit entities + definitions.** Define the subject in one crisp sentence early ("X is a …"). Engines match entities, not keywords.
4. **Structured facts.** Tables, ordered steps, and stat callouts are extracted preferentially over prose.
5. **Citations and sources.** Link primary sources; engines trust (and re-cite) content that itself cites authority. Tier sources (see `deep-research`).
6. **Question-shaped headings.** Headings that mirror real queries ("How does X work?") map to how engines retrieve.
7. **Freshness signals.** Dateline + "last updated"; AI Overviews favor recent, dated content.
8. **Statistics and quotables.** Original data and crisp one-liners get quoted far more than generic claims.

---

## Audit Output (`--audit`)

```markdown
# GEO Audit — [URL/Title]

## Extractability
| Section | Answers-first? | Self-contained? | Entity named? | Fix |

## Structure
- Tables/lists present where facts belong? [y/n]
- Question-shaped headings? [y/n]

## Authority & Citations
- Primary sources linked? [count]
- Original data/stats present? [count]

## Freshness
- Dated / last-updated? [y/n]

## Prioritized Fixes (impact ÷ effort)
| # | Fix | Why it matters for AI citation | Effort |
```

---

## Research Discipline

- Use WebSearch to see what answer engines currently surface for the target query — model the passages they're lifting
- Verify every statistic with `fact-checker` before it ships; a wrong stat that gets cited is a liability
- Flag claims that are assumed vs. evidenced

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Need the competitive answer-engine landscape | `deep-research` |
| Stats must be citation-solid | `fact-checker` |
| Output is a full content piece | `doc-coauthoring` |
| Broader channel/social performance | `social-audit` |

---

## Rules

- **Answer first, every section** — engines lift the first clear claim.
- **Optimize passages, not pages** — each chunk must stand alone, entity named.
- **Cite to be cited** — content that references authority gets re-cited.
- **Structured facts win** — tables/steps/stats are extracted over prose.
- **Every stat verified** — a cited wrong number is worse than no number.
