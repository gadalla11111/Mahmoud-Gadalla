---
name: mcp-builder
description: >
  Guide for creating high-quality MCP (Model Context Protocol) servers that
  enable LLMs to interact with external services through well-designed tools.
  Use when building MCP servers to integrate external APIs or services, whether
  in Python (FastMCP) or Node/TypeScript (MCP SDK). Trigger on: "create an MCP
  server", "build an MCP tool", "expose X as MCP", integrating a new service as
  a Claude tool, extending Claude's toolset. After building, invoke mcp-inspector
  to debug live. For high-stakes architecture decisions (stdio vs SSE, monolithic
  vs modular), invoke adr.
allowed-tools: [WebFetch, WebSearch, Read, Write, Bash]
argument-hint: "<service-name> [--lang python|typescript] [--transport stdio|sse]"
auto-trigger:
  - "create an MCP server", "build an MCP tool", "expose X as an MCP"
  - integrating a new service or API as an MCP tool
  - extending Claude's toolset with a custom server
do-not-trigger:
  - using an existing MCP tool
  - general API integration without MCP
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# MCP Server Development Guide

Build MCP servers that let LLMs accomplish real workflows — not just API wrappers.
Quality is measured by whether agents complete realistic tasks efficiently.

---

## Transport Selection (decide first)

| Transport | When to use | Invocation |
|---|---|---|
| **stdio** | Local tool, single user, spawned by Claude Desktop / CLI | `command + args` in config |
| **SSE (HTTP)** | Shared/hosted server, multiple concurrent users, remote API | `url` in config |
| **stdio default** | When in doubt — simpler, no auth surface, no port management | — |

Pick stdio unless the service must be shared or is already an HTTP endpoint. Log the decision in an ADR if the choice is non-obvious (`adr` skill).

---

## Phase 0 — Checklist Before Writing Code

- [ ] Transport decided (stdio / SSE)
- [ ] Language decided (Python / TypeScript)
- [ ] MCP spec fetched: `https://modelcontextprotocol.io/llms-full.txt`
- [ ] SDK README fetched (Python or TypeScript — see Phase 1)
- [ ] Target API fully read (auth, rate limits, pagination, error codes)
- [ ] Workflow map drawn: what real tasks will agents complete?
- [ ] Tool boundaries defined: consolidate where natural (e.g., `schedule_event` = check + create)

---

## Phase 1 — Research

### 1.1 Agent-Centric Design Principles

**Build for Workflows, Not Endpoints**
- Consolidate related calls: `schedule_event` checks availability and creates — one tool, not two
- Tools should complete a task unit, not expose an API surface
- Ask: "What would an agent need to do start-to-finish?"

**Optimize for Context Budget**
- Return high-signal summaries by default; offer `detail=full` for deep dives
- Use human-readable identifiers (names, not IDs) in responses
- Truncate large payloads at 25,000 chars with a `truncated: true` flag

**Actionable Errors**
- Every error message suggests a next step: "No results. Try `filter='active_only'` to narrow the search."
- Never return raw HTTP error codes without interpretation

**Discoverability**
- Group related tools with consistent prefixes: `calendar_create`, `calendar_list`, `calendar_delete`
- Tool names reflect how humans think, not how the API is organized

### 1.2 Load Documentation

```bash
# MCP specification (always)
WebFetch: https://modelcontextprotocol.io/llms-full.txt

# Python SDK
WebFetch: https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md
# → then read: ./reference/python_mcp_server.md

# TypeScript SDK
WebFetch: https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md
# → then read: ./reference/node_mcp_server.md
```

Read `./reference/mcp_best_practices.md` regardless of language.

### 1.3 Study the Target API

Read **all** available API docs:
- Auth (OAuth, API key, header format)
- Rate limits (per-minute, per-day, burst)
- Pagination (`cursor`, `offset`, `page_token` — which pattern?)
- Error codes and retry semantics
- Data models and field types

---

## Phase 2 — Implementation Plan

Write a plan with:

**Tool inventory** — ranked by agent value, with consolidation decisions noted
**Shared utilities** — API client, pagination helper, response formatter, error mapper
**Input/output contracts** — Pydantic (Python) or Zod (TypeScript) schemas per tool
**Character limit strategy** — how to truncate; what to omit first
**Error matrix** — each API error code → actionable error message

---

## Phase 3 — Implementation

### Language Setup

**Python (FastMCP)**
```
single .py file for simple servers
package layout for complex (tools/, utils/, models/)
Pydantic v2 with model_config
async/await for all I/O
@mcp.tool decorator with full docstring
```

**TypeScript**
```
package.json + tsconfig.json with strict: true
src/index.ts as entry
server.registerTool() with Zod .strict() schemas
explicit Promise<T> return types — no any
npm run build must pass clean
```

See language-specific guides: `./reference/python_mcp_server.md` / `./reference/node_mcp_server.md`

### Tool Implementation Pattern

For each tool:
1. **Schema** — Pydantic / Zod with constraints (min/max, regex, examples in field descriptions)
2. **Docstring** — one-line summary + purpose + params + return schema + usage examples + error handling
3. **Logic** — shared utilities, async I/O, multi-format response (JSON default, Markdown option)
4. **Annotations**:
   - `readOnlyHint: true` — no writes
   - `destructiveHint: false` — safe to call repeatedly
   - `idempotentHint: true` — same result on repeat
   - `openWorldHint: true` — hits external systems

### Code Quality Gates

- DRY: shared logic in utilities, not duplicated across tools
- Consistent: same operation type → same response shape
- Full type coverage
- Every external call has error handling
- Every tool has a comprehensive docstring

---

## Phase 4 — Testing Without Hanging

**MCP servers are long-running processes** — running directly hangs the shell.

Safe test approaches:

```bash
# Syntax check (Python)
python -m py_compile server.py

# Build check (TypeScript)
npm run build

# Process-safe manual test
tmux new-session -d -s mcp-test 'python server.py'
# then run evaluation harness in main shell

# Timeout test (quick smoke)
timeout 5s python server.py || true
```

**Recommended**: use the evaluation harness (Phase 5) — it manages the server process.

After building, invoke `mcp-inspector` skill to debug tools interactively before writing evaluations.

### Quality Checklist

Load the language-specific checklist:
- Python: "Quality Checklist" section in `./reference/python_mcp_server.md`
- TypeScript: "Quality Checklist" section in `./reference/node_mcp_server.md`

---

## Phase 5 — Evaluations

Load `./reference/evaluation.md` for full guide.

### Evaluation Requirements

10 questions minimum. Each must be:
- **Independent** — not relying on another question's state
- **Read-only** — no destructive ops
- **Multi-tool** — requires 2+ tool calls to answer
- **Realistic** — a real agent would face this
- **Verifiable** — single correct answer, string-comparable
- **Stable** — answer won't change as data changes

### Question Generation Process

1. List available tools
2. Explore data with READ-ONLY calls
3. Draft 10+ questions
4. Solve each yourself to verify the answer exists

### Output Format

```xml
<evaluation>
  <qa_pair>
    <question>...</question>
    <answer>...</answer>
  </qa_pair>
</evaluation>
```

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| stdio vs SSE is a close call | `adr` — record the trade-off |
| Server built, need live debugging | `mcp-inspector` |
| Security-sensitive tool (auth, credentials) | `trailofbits/sharp-edges` |
| Complex multi-service orchestration | `nested-subagents` |
| API docs are sparse or inconsistent | `ultra-search` |

---

## Reference Library

| File | Load when |
|---|---|
| `https://modelcontextprotocol.io/llms-full.txt` | Phase 1 — always |
| `./reference/mcp_best_practices.md` | Phase 1 — always |
| `./reference/python_mcp_server.md` | Phase 3 (Python) |
| `./reference/node_mcp_server.md` | Phase 3 (TypeScript) |
| `./reference/evaluation.md` | Phase 5 |
| Python SDK README (WebFetch) | Phase 1 (Python) |
| TypeScript SDK README (WebFetch) | Phase 1 (TypeScript) |
