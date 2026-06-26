---
name: caveman
description: >
  Aggressive token reducer. Rewrites prompts, context, and documents into the
  fewest tokens that still carry the full instruction — caveman-terse, meaning
  intact. Use when a user wants to cut token spend on a prompt, system message,
  or pasted context before sending it to a model. Trigger on: "cut the tokens",
  "compress this prompt", "make this shorter for the model", "too many tokens",
  "trim the context". Archetype: Workflow Automation. Complements sipcode
  (which measures/estimates spend); caveman actively compresses the input.
allowed-tools: [Read, Write, Edit]
argument-hint: "<prompt/context/text to compress> [--aggressive | --safe]"
auto-trigger:
  - "cut the tokens"
  - "compress this prompt"
  - "too many tokens"
  - "trim the context for the model"
  - reducing input size before sending to an LLM
do-not-trigger:
  - user-facing prose that must stay readable (use humanizer/doc skills)
  - measuring or estimating token cost (use sipcode)
  - removing information rather than encoding it more tightly
health:
  last_eval: 2026-06-26
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []
---

# Caveman

Few words. Same meaning. Fewer tokens. Compresses model-facing text without losing instruction fidelity.

---

## When this is safe (and when it isn't)

| Compress | Leave alone |
|---|---|
| Prompts, system messages, instructions | Legal/contract language |
| Pasted reference context | Code (whitespace is semantic) |
| Verbose specs and requirements | User-facing prose meant to be read |
| Repeated boilerplate | Anything where exact wording is the point |

Caveman is for **model-facing** text. The model doesn't need your manners; the reader does. Never run this on prose a human will read — that's `humanizer`'s job, opposite goal.

---

## Compression Techniques (ordered by safety)

1. **Cut courtesy + filler.** "Could you please go ahead and…" → "". Models don't need politeness.
2. **Drop redundant framing.** "I want you to act as an expert who…" → state the task; the model infers role from the task.
3. **Collapse repetition.** Said once is enough — delete restatements and summaries.
4. **Telegraphic syntax.** Drop articles/auxiliaries where unambiguous: "the function should return a list" → "return list".
5. **Symbolize structure.** Prose lists → bullets; relationships → arrows (`→`); conditions → `if/then`.
6. **Deduplicate context.** Repeated entities → define once, reference short.
7. **Strip examples to one.** Three illustrative examples → one canonical, unless variety is the point.

Apply 1–4 by default (`--safe`); add 5–7 for `--aggressive`.

---

## The Fidelity Rule

Compression must be **lossless on instruction**. After compressing, verify:
- Every constraint in the original is still present
- Every named entity / file / value survives exactly
- No requirement got merged away or softened
- Negations preserved ("do NOT" must never vanish)

If a technique risks dropping a constraint, don't apply it. Terse ≠ incomplete.

---

## Output

Return the compressed text plus a one-line **savings estimate** (rough token delta) and a **fidelity note** confirming all constraints/entities/negations survived. Offer to hand the estimate to `sipcode` for an exact count.

```markdown
## Compressed (≈ -62% tokens)
<terse text>

Fidelity: all 7 constraints, 3 file paths, 2 negations preserved.
```

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Exact token count / cost estimate | `sipcode/estimate` |
| Where tokens went post-session | `sipcode/why` |
| Opposite goal — make prose human-readable | `humanizer` |
| Compressing a whole repo's context | `nested-subagents` (map-reduce summaries) |

---

## Rules

- **Model-facing only** — never compress text a human will read.
- **Lossless on instruction** — every constraint, entity, value, and negation survives.
- **Politeness is free to cut** — models don't need "please" or role-play framing.
- **Structure beats prose** — bullets, arrows, if/then carry more per token.
- **Verify negations** — a dropped "NOT" inverts the instruction; check every one.
