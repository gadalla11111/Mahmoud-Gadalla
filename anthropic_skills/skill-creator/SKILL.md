---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy. Also trigger when a user wants to formalise a recurring workflow, port an external skill into the library, or asks "how do I make Claude always do X".
auto-trigger:
  - "create a new skill"
  - "add skill for X"
  - "I need a skill that does Y"
  - "how do I make Claude always do X"
  - "turn this into a skill"
  - formalising a recurring workflow into a reusable SKILL.md
  - porting an external skill into this library
  - "evolve/improve/update this skill"
do-not-trigger:
  - using an existing skill (just use the skill)
  - one-off tasks not worth formalising
  - asking what a skill does (just read the SKILL.md)

---

# Skill Creator

A skill for creating new skills and iteratively improving them — with archetype-aware authoring, adversarial evals, composition-graph awareness, and progressive maturity tiers.

---

## Maturity Tiers

Before writing anything, tell the user which tier to target. Most users need v1.

| Tier | What's included | When to target it |
|---|---|---|
| **v0** | SKILL.md only, 2 test cases, no assertions | Spike / proof of concept |
| **v1** | Bundled scripts (if repeated code detected), 5 test cases, objective assertions | Standard production skill |
| **v2** | References/ for domain knowledge, 10+ test cases, blind comparison, trigger optimization, health score | High-frequency or high-stakes skill |

The tier determines scope. Don't over-engineer a v0 or under-test a v2.

---

## Skill Archetypes

Immediately after capturing intent, classify the skill into one archetype. The archetype drives every downstream decision.

| Archetype | Traits | Authoring implication |
|---|---|---|
| **Workflow Automation** | Fixed steps, deterministic output | Bundle scripts; assertions are objective; thin "why" explanations |
| **Judgment Amplifier** | Fuzzy inputs, expert-level output | Deep "why" explanations; subjective eval; avoid rigid MUST rules |
| **Context Injector** | Loads domain knowledge into context | References/ heavy; SKILL.md stays thin and pointers-only |
| **Orchestrator** | Routes to other skills or spawns subagents | Trigger logic IS the skill; composition graph check is critical |
| **Interface Adapter** | Translates between formats or APIs | Examples are the core content; edge-case probing is essential |

One skill = one archetype. If it spans two, split it.

---

## Core Loop

At a high level:

1. Set tier + archetype → write draft → run test cases (with-skill + baseline in parallel)
2. While runs are in progress, draft assertions
3. Human reviews in eval viewer → read feedback
4. Run adversarial test round
5. Improve skill → repeat until satisfied
6. Composition graph check → update `.memory/stacks.md` if needed
7. Description optimization (v1+)
8. Package and present

Your job is to figure out where the user is in this loop and jump in. If they have a draft, go straight to evals. If they say "just vibe with me", do that.

---

## Communicating with the User

Pay attention to context cues. In the default case:
- "evaluation" and "benchmark" are OK
- "JSON" and "assertion" need explanation unless the user signals familiarity

It's fine to briefly define terms when in doubt.

---

## Step 1: Capture Intent

If the current conversation already contains a workflow the user wants to capture ("turn this into a skill"), extract answers from history first — tools used, sequence of steps, corrections made, input/output formats. Fill gaps with the user, then confirm before proceeding.

Questions to answer:
1. What should this skill enable Claude to do?
2. When should it trigger? (phrases, contexts, problem descriptions)
3. What's the expected output format?
4. **What archetype is this?** (classify immediately — see table above)
5. **What maturity tier?** (v0 / v1 / v2)
6. Should we set up test cases? Skills with verifiable outputs benefit from them; purely subjective skills often don't.

---

## Step 2: Interview and Research

Proactively ask about edge cases, input/output formats, example files, success criteria, and dependencies. Wait to write test prompts until this is ironed out.

Check available MCPs — if useful for research, use subagents in parallel.

**Composition graph check (do this now, not at the end):**
- Read `.memory/skills.md` and `.memory/stacks.md`
- Does this skill overlap with an existing skill? Resolve the boundary explicitly. Add `do-not-trigger` entries to BOTH skills.
- Does this skill naturally pair with another? Note the pairing for the stacks update later.
- Should this skill route to another as a subroutine? Document that in the description.

---

## Step 3: Write the SKILL.md

### Anatomy

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description, auto-trigger, do-not-trigger, health)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Domain docs loaded into context as needed
    └── assets/     - Templates, icons, fonts used in output
```

### Frontmatter fields

```yaml
---
name: skill-name
description: >
  What it does and when to use it. Be "pushy" — if the description
  matches, trigger. Include implicit-need phrasing, not just
  explicit-name phrasing.
auto-trigger:
  - "user phrases that should trigger this"
do-not-trigger:
  - "adjacent cases that should NOT trigger this"
health:
  last_eval: YYYY-MM-DD
  pass_rate: null        # filled after first eval run
  trigger_accuracy: null # filled after description optimization
  open_issues: []
---
```

The `health` block starts null and gets filled in after evals. The `consolidate` engram skill uses it to surface degraded skills.

### Progressive Disclosure

Skills use a three-level loading system:
1. **Metadata** (name + description) — always in context (~100 words)
2. **SKILL.md body** — in context when triggered (<500 lines ideal)
3. **Bundled resources** — loaded as needed (unlimited)

Keep SKILL.md under 500 lines. If approaching the limit, add hierarchy with clear pointers to where to go next.

### Domain organization

When a skill supports multiple domains, organize by variant:
```
cloud-deploy/
├── SKILL.md (workflow + selection logic)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```
Claude reads only the relevant reference file.

### Writing principles

- **Explain the why.** LLMs are smart. When they understand *why* something matters, they go beyond rote compliance. If you're writing ALWAYS or NEVER in caps, that's a yellow flag — reframe as reasoning.
- **Keep it lean.** Remove things not pulling their weight. Read transcripts, not just outputs — if the skill wastes time on unproductive steps, cut those sections.
- **Generalize from examples.** The skill runs a million times across prompts you haven't seen. Don't overfit to the test cases. Try different metaphors if something is stubborn.
- **Archetype-appropriate style:** Workflow Automation → imperative + scripts. Judgment Amplifier → theory of mind + "why" explanations. Context Injector → references/ heavy. Interface Adapter → examples are the core.
- **Bundle repeated work.** If all test runs independently wrote the same helper script, that script belongs in `scripts/`.

### Description writing

The description is the primary triggering mechanism. Include both:
- **Explicit trigger** — user names the domain directly ("create a skill for X")
- **Implicit trigger** — user describes a problem without naming the solution ("how do I make Claude always remember to...")

Make it "pushy": instead of "How to build a dashboard", write "How to build a dashboard. Use whenever the user mentions data visualization, metrics display, or internal reporting — even if they don't say 'dashboard'."

### Principle of Least Surprise

Skills must not contain malware, exploit code, or content that compromises security. A skill's contents should not surprise the user in their intent if described. Don't create misleading skills or skills designed to facilitate unauthorized access. Roleplay/persona skills are fine.

---

## Step 4: Test Cases

After writing the draft, generate 2–3 (v0), 5 (v1), or 10+ (v2) realistic test prompts — the kind a real user would actually say. Share them with the user: "Here are the test cases I'd like to try. Do these look right, or want to add more?"

Save to `evals/evals.json`:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

See `references/schemas.md` for the full schema including the `assertions` field.

---

## Step 5: Run Tests (Continuous Sequence — Don't Stop Partway)

Do NOT use `/skill-test` or any other testing skill.

Put results in `<skill-name>-workspace/` as a sibling to the skill directory. Within the workspace, organize by `iteration-N/` then `eval-N/`. Create directories as you go.

### Spawn all runs in one turn (with-skill AND baseline)

For each test case, spawn two subagents simultaneously — one with the skill, one without. Don't run with-skill first and come back for baselines.

**With-skill run:**
```
Execute this task:
- Skill path: <path-to-skill>
- Task: <eval prompt>
- Input files: <eval files if any, or "none">
- Save outputs to: <workspace>/iteration-<N>/eval-<ID>/with_skill/outputs/
- Outputs to save: <what the user cares about>
```

**Baseline run:**
- New skill → no skill at all (same prompt, no skill path, save to `without_skill/outputs/`)
- Improving existing skill → snapshot first (`cp -r <skill-path> <workspace>/skill-snapshot/`), point baseline at snapshot, save to `old_skill/outputs/`

Write `eval_metadata.json` for each test case:
```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name-here",
  "prompt": "The user's task prompt",
  "assertions": []
}
```

### While runs are in progress: draft assertions

Good assertions are objectively verifiable and have descriptive names. Subjective skills → qualitative feedback, not forced assertions. Update `eval_metadata.json` and `evals/evals.json` once drafted. Explain to the user what they'll see in the viewer.

### As runs complete: capture timing data

Save immediately to `timing.json` in each run directory:
```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

This only comes through the task notification — capture it immediately.

### Grade, aggregate, launch viewer

1. **Grade** — spawn a grader subagent that reads `agents/grader.md`. Save `grading.json` per run. Use fields `text`, `passed`, `evidence` (exact names, viewer depends on them). For programmatically checkable assertions, write and run a script.

2. **Aggregate** — run:
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```
   Produces `benchmark.json` and `benchmark.md`. Put with_skill before baseline counterpart.

3. **Analyst pass** — read `agents/analyzer.md`. Surface non-discriminating assertions, high-variance evals, time/token tradeoffs.

4. **Launch viewer:**
   ```bash
   nohup python <skill-creator-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   VIEWER_PID=$!
   ```
   For iteration 2+, add `--previous-workspace <workspace>/iteration-<N-1>`.

   **Headless/Cowork:** use `--static <output_path>` to write standalone HTML. Feedback downloads as `feedback.json` when user clicks "Submit All Reviews".

   **⚠ GENERATE THE EVAL VIEWER BEFORE evaluating inputs yourself.** Get outputs in front of the human ASAP.

5. Tell the user: "I've opened the results in your browser. 'Outputs' lets you click through each test case and leave feedback, 'Benchmark' shows the quantitative comparison. Come back when done."

### Read feedback

When done, read `feedback.json`:
```json
{
  "reviews": [
    {"run_id": "eval-0-with_skill", "feedback": "chart is missing axis labels", "timestamp": "..."},
    {"run_id": "eval-1-with_skill", "feedback": "", "timestamp": "..."}
  ],
  "status": "complete"
}
```

Empty feedback = fine. Focus improvements on cases with complaints. Kill viewer: `kill $VIEWER_PID 2>/dev/null`

---

## Step 6: Adversarial Test Round (v1+ only)

After the first human review, run a second batch targeting failure modes — not happy paths.

Generate 3–5 adversarial prompts per category relevant to the archetype:

| Category | What to probe |
|---|---|
| **Ambiguous input** | Incomplete context, missing required info, vague phrasing |
| **Skill boundary overlap** | A prompt where this skill and an adjacent skill both match — who wins? |
| **Wrong-domain adjacent** | Same keywords but clearly needs something else (tests do-not-trigger) |
| **Regression** | Re-run all previously-passing evals — confirm nothing broke |
| **Edge case injection** | Empty input, max-length input, malformed input, unusual format |

Add adversarial results to a new `iteration-N-adversarial/` directory. Run through the same grade → aggregate → viewer pipeline. Failing adversarial evals are high-priority fixes.

---

## Step 7: Improve the Skill

1. **Generalize from feedback.** The skill runs across prompts you haven't seen. Avoid overfit, oppressive MUSTs, or fiddly fixes. Try different metaphors for stubborn issues.

2. **Keep it lean.** Read the full run transcripts — if the skill makes the model waste time, cut those sections.

3. **Explain the why.** Transmit understanding, not just rules.

4. **Bundle repeated work.** If all test runs wrote the same helper, it belongs in `scripts/`.

5. **Update `health` block** in frontmatter: set `last_eval`, `pass_rate`, `open_issues`.

### Iteration loop

After improving:
1. Apply improvements to SKILL.md
2. Rerun all test cases into `iteration-<N+1>/`, including baseline
3. Launch viewer with `--previous-workspace`
4. Wait for human review
5. Repeat until: user is happy, feedback is all empty, or no meaningful progress

---

## Step 8: Composition Graph Update

Before description optimization, check cross-skill impact:

1. Read `.memory/stacks.md` — does this skill belong in an existing stack? Add it.
2. Read `.memory/skills.md` — does this skill create a new pairing with an existing skill? Document it.
3. If any skill boundary overlaps were found in adversarial testing, update `do-not-trigger` in BOTH skills.
4. If this skill is an Orchestrator archetype, trace the full routing graph and document it in stacks.md.

Commit the updated stacks/skills files alongside the skill itself.

---

## Step 9: Description Optimization (v1+)

### Generate trigger eval queries

Create 20 eval queries — mix of should-trigger and should-not-trigger. Save as JSON:
```json
[
  {"query": "the user prompt", "should_trigger": true},
  {"query": "another prompt", "should_trigger": false}
]
```

Queries must be concrete and realistic — file paths, personal context, column names, company names. Include typos, casual speech, abbreviations. Focus on edge cases, not clear-cuts.

**Should-trigger (8–10):** different phrasings of the same intent — formal, casual, implicit-need, uncommon use cases, cases where this skill competes with another but should win.

**Should-not-trigger (8–10):** near-misses — same keywords but different domain, ambiguous phrasing where naive match would fire but shouldn't, adjacent tasks where another skill wins.

Bad: `"Format this data"` — too easy, tests nothing.
Good: `"ok my boss sent me this xlsx (Q4 sales final FINAL v2.xlsx) and wants a profit margin column. Revenue is col C, costs are col D i think"`

### Generate dual-variant descriptions

For richer optimization, generate **two candidate descriptions** before running the optimizer:
- **Explicit variant** — matches when user names the domain directly
- **Implicit variant** — matches when user describes the problem without naming the solution

Add both as candidates in the eval set so the optimizer can compare.

### Review with user

1. Read `assets/eval_review.html`
2. Replace `__EVAL_DATA_PLACEHOLDER__`, `__SKILL_NAME_PLACEHOLDER__`, `__SKILL_DESCRIPTION_PLACEHOLDER__`
3. Write to `/tmp/eval_review_<skill-name>.html` and open it
4. User edits queries, toggles should-trigger, clicks "Export Eval Set"
5. Check `~/Downloads/` for most recent `eval_set.json`

### Run optimization loop

```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-powering-this-session> \
  --max-iterations 5 \
  --verbose
```

Use the model ID from your system prompt — triggering test must match what the user actually experiences. Periodically tail the output to give the user updates.

The loop: 60% train / 40% held-out test → evaluate current description (3 runs per query) → Claude proposes improvements → re-evaluate → repeat up to 5×. Returns `best_description` selected by test score (not train score — avoids overfitting).

### Apply the result

Take `best_description` from JSON output and update SKILL.md frontmatter. Show before/after and report scores. Update `health.trigger_accuracy` in the frontmatter.

### How triggering works

Skills appear in `available_skills` with name + description. Claude only consults skills for tasks it can't easily handle alone — simple one-step queries won't trigger even if the description matches. Eval queries should be substantive enough that Claude would actually benefit from the skill.

---

## Step 10: Package and Present

Check whether `present_files` tool is available. If so:

```bash
python -m scripts.package_skill <path/to/skill-folder>
```

Direct the user to the resulting `.skill` file path.

---

## Advanced: Blind Comparison

For rigorous A/B comparison between two skill versions (e.g., "is the new version actually better?"), read `agents/comparator.md` and `agents/analyzer.md`. An independent agent judges quality without knowing which output came from which version. Optional — human review loop is usually sufficient.

---

## Platform-Specific Notes

### Claude.ai (no subagents, no browser)

- **Test cases:** Read the skill's SKILL.md, then follow its instructions yourself. One at a time. Skip baseline runs.
- **Reviewing results:** Skip browser viewer. Show prompt + output inline. Ask for feedback in conversation.
- **Benchmarking:** Skip — baseline comparisons aren't meaningful without subagents.
- **Description optimization:** Requires `claude -p` CLI — skip on Claude.ai.
- **Blind comparison:** Requires subagents — skip.
- **Packaging:** Works anywhere with Python and a filesystem.

### Cowork (subagents yes, no browser)

- Main workflow (parallel spawning, baselines, grading) all works.
- If severe timeout issues, run test prompts in series rather than parallel.
- Use `--static <output_path>` for eval viewer — no display available.
- Feedback downloads as `feedback.json` — read from there (may need to request access).
- Description optimization (`run_loop.py`) works fine — uses `claude -p`, not browser.
- **⚠ GENERATE THE EVAL VIEWER before evaluating inputs yourself.** Put outputs in front of the human ASAP. Add this explicitly to your TodoList: "Create evals JSON and run `eval-viewer/generate_review.py` so human can review test cases."

### Updating an existing skill

- **Preserve the original name.** Keep directory name and `name` frontmatter unchanged.
- **Copy to writable location.** Installed path may be read-only — copy to `/tmp/skill-name/`, edit there, package from the copy.
- **Stage in `/tmp/` first** if packaging manually — direct writes may fail.

---

## Reference Files

```
agents/grader.md     — How to evaluate assertions against outputs
agents/comparator.md — How to do blind A/B comparison between two outputs
agents/analyzer.md   — How to analyze why one version beat another
references/schemas.md — JSON structures for evals.json, grading.json, benchmark.json
```

---

## Core Loop (Summary)

```
tier + archetype → composition graph check → draft SKILL.md
→ test cases (with-skill + baseline in parallel)
→ [while running] draft assertions
→ grade → aggregate → eval viewer → human review
→ adversarial test round
→ improve skill → update health block
→ repeat until satisfied
→ composition graph update → stacks.md update
→ description optimization (dual-variant)
→ package and present
```

Add these to your TodoList before starting:
- [ ] Classify archetype and tier
- [ ] Composition graph check (before writing)
- [ ] Create evals JSON and run `eval-viewer/generate_review.py` so human can review test cases
- [ ] Run adversarial test round after first human review
- [ ] Update health block in frontmatter
- [ ] Update `.memory/stacks.md` if new pairing found
- [ ] Description optimization (v1+)

Good luck!
