---
name: humanizer
description: >
  Strips AI writing tells from text — the hedges, scaffolding, and stock phrasing
  that mark a draft as machine-written — without changing meaning. Use when a user
  wants copy that reads like a person wrote it: removing "it's important to note",
  "in today's fast-paced world", em-dash overuse, tricolons, and forced symmetry.
  Trigger on: "make this sound human", "strip AI tells", "de-AI this", "less
  robotic", "it reads like ChatGPT". Archetype: Workflow Automation.
  Cross-references doc-coauthoring for longer-form rewriting.
allowed-tools: [Read, Write, Edit]
argument-hint: "<text or file to humanize>"
auto-trigger:
  - "make this sound human"
  - "strip the AI tells"
  - de-AI this or less robotic
  - "it reads like ChatGPT/AI"
  - removing machine-writing patterns from a draft
do-not-trigger:
  - generating new content from scratch (use doc-coauthoring)
  - translation between languages
  - factual editing or fact-checking (use fact-checker)
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Humanizer

Removes the fingerprints of machine writing. Same meaning, same facts — fewer tells.

---

## The Tell Inventory (hunt and remove)

| Tell | Example | Fix |
|---|---|---|
| **Throat-clearing** | "It's important to note that…", "It's worth mentioning…" | Delete; state the thing |
| **Stock openers** | "In today's fast-paced world…", "In the realm of…" | Open on the specific subject |
| **Hedge stacks** | "may potentially possibly…" | Pick one modal or none |
| **Forced tricolons** | "fast, reliable, and scalable" everywhere | Vary list length; sometimes two, sometimes four |
| **Em-dash overuse** | three em-dashes per paragraph | Mix in periods, commas, parens |
| **Symmetry tic** | "Not just X, but Y" / "It's not about A, it's about B" repeated | Use once at most; break the rhythm |
| **Empty intensifiers** | "truly", "really", "very", "incredibly" | Cut; let the noun carry it |
| **Summary restatement** | "In conclusion, as we've seen…" | End on a real point, not a recap |
| **Hyper-balanced sentences** | every sentence the same length/shape | Vary cadence — short. Then a longer one that breathes. |
| **Corporate abstractions** | "leverage synergies to drive value" | Concrete verbs and nouns |

---

## Process

1. **Read for rhythm first.** AI text is suspiciously even. Mark where every sentence is the same length — that monotony is the biggest tell.
2. **Strike the throat-clearing** — openers and "note that" framings go first; they're pure scaffolding.
3. **Break the symmetry** — find the repeated "not just X but Y" / tricolon patterns and vary them.
4. **Cut intensifiers and hedges** — they signal a model padding for confidence.
5. **Re-vary cadence** — deliberately alternate short and long sentences. A fragment is allowed. So is a run-on, occasionally.
6. **Keep meaning and facts identical** — this is style surgery, not a rewrite. Never invent or drop information.

---

## What NOT to do

- Don't inject slang or fake casualness to "sound human" — that's a different artificial.
- Don't change the argument, facts, or structure.
- Don't strip domain terms that belong (precision ≠ AI tell).
- Don't add errors to seem human — humans write cleanly too.

---

## Output

Return the humanized text. If asked, append a short **change log**: which tells were removed and how many (e.g., "removed 6 throat-clearing openers, broke 4 forced tricolons, varied cadence in 3 paragraphs").

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Rewriting longer-form collaboratively | `doc-coauthoring` |
| Output must match a brand voice | `brand-guidelines` / `applying-brand-guidelines` |
| Facts need checking after editing | `fact-checker` |

---

## Rules

- **Meaning is invariant** — strip style, never facts or argument.
- **Vary cadence on purpose** — monotone sentence length is the #1 tell.
- **Throat-clearing dies first** — "it's important to note" adds nothing.
- **Break the symmetry tic** — "not just X but Y" once, then never again.
- **Don't fake casual** — removing tells ≠ adding slang.
