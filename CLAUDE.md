# Claude Code Instructions — Mahmoud-Gadalla

## Project Layout

- `claude_agent_sdk/` — standalone Python agents (research, SRE, chief of staff, vulnerability detection, session browser)
- `managed_agents/` — Claude Managed Agents notebooks and integrations (Slack, Sentry, Linear)
- `anthropic_skills/` — drop-in skill folders; each has a `SKILL.md`
- `skills/` — cookbooks skill modules (financial, brand)
- `tool_use/` — tool use pattern notebooks
- `misc/` — runnable scripts (batch_processing.py, outcome_grader.py)
- `tools/` — developer tooling (diffgate submodule, JetBrains plugin)

## Skill Routing

| Task | Skill |
|---|---|
| Consolidate/audit knowledge directories | `anthropic_skills/engram/consolidate` |
| Session briefing / catch me up | `anthropic_skills/engram/briefing` |
| Checkpoint working memory | `anthropic_skills/engram/working` |
| Think before coding (find shortcuts) | `anthropic_skills/lazy-cat/think-twice` |
| Surgical edits (write only what's asked) | `anthropic_skills/lazy-cat/surgical` |
| Clarify intent before agent acts | `anthropic_skills/promptize/promptize` |
| Estimate task cost | `anthropic_skills/sipcode/estimate` |
| Audit session token spend | `anthropic_skills/sipcode/why` |
| Frontend/UI artifacts | `anthropic_skills/frontend-design` |
| Word documents | `anthropic_skills/docx` |
| PDF documents | `anthropic_skills/pdf` |
| PowerPoint | `anthropic_skills/pptx` |
| Excel | `anthropic_skills/xlsx` |
| MCP server creation | `anthropic_skills/mcp-builder` |
| Brand guidelines | `anthropic_skills/brand-guidelines` |
| Route any task to the right skill | `anthropic_skills/orchestrator` |
| Structured feature development (SPARC) | `anthropic_skills/sparc` |
| Architecture Decision Records | `anthropic_skills/adr` |
| Deep delegation via agent tree | `anthropic_skills/nested-subagents` |
| Arabic ministry proposal (MERIDIAN brand) | `anthropic_skills/ministry-proposal` |
| Triple-source fact verification / QA grid | `anthropic_skills/fact-checker` |

## Environment

```bash
cp .env.example .env   # add ANTHROPIC_API_KEY
uv sync --all-extras   # install Python deps
```

## Models

- Sonnet: `claude-sonnet-4-6`
- Haiku: `claude-haiku-4-5`
- Opus: `claude-opus-4-6`

## Code Style

- Python: follow existing patterns, no unnecessary abstractions
- No comments unless the WHY is non-obvious
- Never commit `.env` files

<!-- sipcode:start v=2 -->
<!-- sipcode:block name="output-compression" mode="default" -->
## Sipcode Output Compression

mode: default — optimizes for: diff edits, no ceremony

the rules below apply to your responses in this project. follow them.
they exist so the user pays for code, not for ceremony.
### rules (default mode)

1. **diff-only edits.** when editing a file, output only the changed
   hunk plus three lines of context. never paste the full file back
   when three lines changed. this is the single biggest win.
2. **no preamble.** skip "i'll help with that", "sure", "here's what
   i did". lead with the work. the user can see what you did.
3. **no post-amble.** don't summarize what was just shown unless the
   user explicitly asks for a summary.
4. **code over prose.** when the answer is code, the code is the
   answer. any explanation goes after the code block, not before.
5. **bullets over paragraphs** for any list of options, steps, or
   trade-offs. saves tokens versus flowing prose.
6. **one canonical example, not three.** show one good example. skip
   the exhaustive variants — the user will ask if they want more.
7. **no filler verbs.** drop "let me", "i'll go ahead and", "i'm
   going to". just do the thing.

(installed by sipcode. switch modes with `npx sipcode rules --mode <m>`.
uninstall with `npx sipcode rules --uninstall`.)
<!-- /sipcode:block -->

<!-- sipcode:end -->
