# Mahmoud-Gadalla

A staged collection of Claude agents, skills, and developer tools — ready to activate with an Anthropic API key.

## Quick Start

```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
uv sync --all-extras
```

See [AGENTS.md](AGENTS.md) for the full agent and skill lineup.

## Structure

| Directory | Contents |
|---|---|
| `claude_agent_sdk/` | Standalone Claude agents (research, SRE, chief of staff, vulnerability detection) |
| `managed_agents/` | Hosted stateful agents + 9 CMA tutorial notebooks |
| `anthropic_skills/` | 20+ drop-in skill folders (design, documents, dev, enterprise, memory) |
| `skills/` | Financial and brand skill modules from claude-cookbooks |
| `tool_use/` | Tool use notebooks (tool_choice, parallel tools, structured JSON, etc.) |
| `misc/` | Batch processing and outcome grader scripts |
| `tools/` | Developer tools (DiffGate code review, JetBrains plugin) |

## Agents

- **Research Agent** — web search + synthesis
- **Chief of Staff** — financial analysis, hiring decisions
- **Site Reliability Agent** — incident response
- **Vulnerability Detection** — security scanning
- **Data Analyst** — CSV → HTML report
- **Specialist Team Coordinator** — multi-agent sales proposal writer
- **Outcome Grader** — writer + independent verifier loop

## Skills

- **engram** — filesystem-backed memory (consolidate, briefing, working)
- **lazy-cat** — think-twice + surgical (eliminate waste before coding)
- **promptize** — confidence-gated intent builder
- **sipcode** — context health manager (token drift detection, cost estimation)
- **diffgate** — diff-aware three-tier code review gate

## Tools

- **DiffGate** — pre-commit security gate (secrets, SQL injection, XSS, destructive migrations)
- **Claude Code JetBrains Plugin** v0.1.14-beta

## Requirements

- Python 3.11+
- Node.js 18+
- `ANTHROPIC_API_KEY` with credits
