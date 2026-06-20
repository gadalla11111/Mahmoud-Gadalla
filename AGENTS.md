# Agent Lineup

All agents are staged and ready. Set `ANTHROPIC_API_KEY` in a `.env` file (copy `.env.example`) to activate any of them.

## Quick Start

```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
uv sync --all-extras
```

---

## Claude Agent SDK (`/claude_agent_sdk/`)

Standalone Python agents built on the Claude Agent SDK.

| Agent | Entry Point | What It Does |
|---|---|---|
| Research Agent | `claude_agent_sdk/research_agent/agent.py` | Web search + synthesis on any topic |
| Chief of Staff | `claude_agent_sdk/chief_of_staff_agent/agent.py` | Multi-task delegation, scheduling, financial analysis |
| Observability Agent | `claude_agent_sdk/observability_agent/` | Monitors logs and traces |
| Site Reliability Agent | `claude_agent_sdk/site_reliability_agent/` | SRE incident response |
| Vulnerability Detection | `claude_agent_sdk/vulnerability_detection_agent/` | Security scanning of codebases |
| Session Browser | `claude_agent_sdk/session_browser_demo/` | Browser automation |

### Run an agent

```bash
uv run python claude_agent_sdk/research_agent/agent.py
```

---

## Claude Managed Agents (`/managed_agents/`)

Hosted stateful agents — define once, run in persistent sessions.

### Applied

| Agent | Notebook | What It Does |
|---|---|---|
| Data Analyst | `managed_agents/data_analyst_agent.ipynb` | CSV → narrative HTML report |
| Slack Data Bot | `managed_agents/slack_data_bot.ipynb` | Slack bot wrapping data analyst |
| SRE Incident Responder | `managed_agents/sre_incident_responder.ipynb` | Alert → investigate → PR → human approval |

### Guided Tutorials (in order)

| Notebook | Teaches |
|---|---|
| `CMA_iterate_fix_failing_tests.ipynb` | Core loop: agent / environment / session, file mounts |
| `CMA_orchestrate_issue_to_pr.ipynb` | Issue → fix → PR → CI → merge |
| `CMA_explore_unfamiliar_codebase.ipynb` | Codebase grounding |
| `CMA_gate_human_in_the_loop.ipynb` | Human approval gates |
| `CMA_prompt_versioning_and_rollback.ipynb` | Prompt versioning & rollback |
| `CMA_operate_in_production.ipynb` | MCP toolsets, vaults, webhooks |
| `CMA_remember_user_preferences.ipynb` | Memory stores across sessions |
| `CMA_coordinate_specialist_team.ipynb` | Multi-agent specialist teams |
| `CMA_verify_with_outcome_grader.ipynb` | Grade-and-revise loops |

### Integrations (need extra credentials in `.env`)

| Integration | Location | Needs |
|---|---|---|
| Slack | `managed_agents/slack/` | `SLACK_BOT_TOKEN`, `SLACK_SIGNING_SECRET` |
| Sentry | `managed_agents/sentry/` | `SENTRY_DSN` |
| Linear | `managed_agents/linear/` | `LINEAR_API_KEY` |

---

## Skills (`/skills/`)

Reusable skill modules that agents can call.

```
skills/
  custom_skills/    # Drop-in skill definitions
  notebooks/        # Skill usage examples
  sample_data/      # Test data
```

---

## Models in Use

- **Sonnet:** `claude-sonnet-4-6`
- **Haiku:** `claude-haiku-4-5`
- **Opus:** `claude-opus-4-6`
