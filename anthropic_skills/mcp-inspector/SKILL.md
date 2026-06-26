---
name: mcp-inspector
description: >
  MCP server security evaluator. Use when the user provides a GitHub URL
  to an MCP server repository and wants to know if it's safe to install.
  Produces a structured Security_Assessment.md with confidence-graded
  findings, not hedged generalities. Requires: mcp__github__* tools or
  WebFetch for code retrieval, WebSearch for community validation.
allowed-tools: [WebSearch, WebFetch, Read, Write, Bash]
argument-hint: "[GitHub URL of MCP server repository]"
auto-trigger:
  - "debug MCP", "MCP server not working", "tool not showing up"
  - diagnosing MCP connection or schema issues
  - testing an MCP server's responses
do-not-trigger:
  - building a new MCP server (use mcp-builder)
  - general debugging

---

# MCP Inspector

Security evaluator for MCP server repositories. Produces definitive, evidence-grounded assessments — not "moderate concerns" but specific CVE-class findings with line references.

---

## Input

GitHub URL of the MCP server repository. Parse to extract `{owner}` and `{repo_name}`.

---

## Evaluation sequence

Execute in order. After each step, append findings to `Security_Assessment.md`.

### 1. Repository metadata
Via `mcp__github__*` tools or WebFetch of the GitHub API:
- Stars, forks, open issues, last commit date, license
- Number of contributors, commit frequency
- Dependency manifest (package.json / pyproject.toml / Cargo.toml)

### 2. Purpose analysis
- Read README.md fully
- What does this server do? What tools does it expose?
- What permissions / network access / filesystem access does it require?
- Is the scope appropriate for the stated purpose?

### 3. Alternatives analysis
- WebSearch: "smithery.ai {repo_name}", "glama.ai {repo_name}", "mcp.so {repo_name}"
- Are there official or better-maintained alternatives for the same purpose?
- If yes: name them and note the comparison

### 4. Code review (systematic)
For each main source file:
- **Input validation**: are all tool parameters validated before use?
- **Shell injection**: any `exec`, `spawn`, `subprocess.run` with unsanitized input?
- **Credential handling**: API keys in code? Logged? Stored insecurely?
- **Data exfiltration**: does the server phone home? Log prompts/responses?
- **Scope creep**: does the code do more than the README claims?
- **Dependency audit**: any known-vulnerable packages? (`npm audit` / `pip-audit` patterns)

Cite specific file + line number for every finding.

### 5. Community validation
WebSearch queries (document each result):
- `reddit {owner} {repo_name} MCP`
- `{owner} {repo_name} security vulnerability`
- `site:smithery.ai {repo_name}`

### 6. Risk scoring

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| Code quality | | |
| Security practices | | |
| Maintenance activity | | |
| Community trust | | |
| Scope appropriateness | | |

**Overall**: Low / Medium / High / Critical risk

---

## Assessment document

Write to `Security_Assessment.md`:

```markdown
# Security Assessment: [repo name]
**URL**: [GitHub URL]
**Date**: [today]
**Evaluator**: MCP Inspector skill

## Verdict
**SAFE TO INSTALL / USE WITH CAUTION / DO NOT INSTALL**
[One paragraph justification]

## Risk Score
[Table from Step 6]

## Findings

### Critical (install-blocking)
- [Finding] — [file:line] — [impact]

### High
- ...

### Medium
- ...

### Low / Informational
- ...

## Alternatives
[If any found in Step 3]

## Evidence trail
| Step | Query / File | Finding |
|---|---|---|
```

---

## Rules

- **No hedging**: say "this server logs all tool inputs to stdout" not "there may be logging concerns"
- **Evidence required**: every finding must cite file + line or a search result URL
- **Definitive verdict**: always conclude with SAFE / USE WITH CAUTION / DO NOT INSTALL
- **Scope honesty**: if code access was limited, note what couldn't be reviewed and why
