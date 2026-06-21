---
name: ultra-search
description: >
  Maximum-coverage search skill. Automatically combines multiple search
  tools in parallel — broad context, deep extraction, direct URL retrieval,
  interactive verification — without requiring the user to name which tool
  to use. Use when a simple WebSearch isn't enough and the user needs
  comprehensive, source-documented results on a specific topic or question.
allowed-tools: [WebSearch, WebFetch, Bash, Read, Write]
---

# Ultra Search

Maximizes search coverage by automatically routing queries across all available tools. Activates without explicit prompting whenever the task is multi-faceted or a single search pass is clearly insufficient.

---

## Core workflow

### 1. Decompose (before searching)
Break the query into core components:
- Identify key concepts and relationships
- Determine which search passes will cover which aspects
- Plan parallel vs. sequential tool use

### 2. Primary research (parallel when possible)
- **WebSearch / Brave**: broad context, `max_results` set high
- **Tavily / WebFetch**: deeper insights, specialized queries, content extraction
- Document every query string for reproducibility

### 3. Content retrieval (for known sources)
- **WebFetch direct URL**: when a specific source is identified in Step 2
- Retrieve full page content, not just snippets

### 4. Synthesis
- Combine findings across all passes
- De-duplicate, cross-reference, flag contradictions
- Present in structured format with source citations

---

## Tool usage rules

| Tool | When |
|---|---|
| WebSearch (Brave) | Initial broad pass, general context, pagination with offset |
| WebFetch (Tavily) | Deeper analysis, academic/technical, content extraction |
| WebFetch direct | When URL is already known from a prior pass |
| Bash `curl` | Fallback when MCP tools unavailable |

**Always use multiple tools.** A single-tool result is a draft, not a finished search.

---

## Source documentation (mandatory)

Every result must include:
- Full URL
- Title
- Access timestamp (use today's date if real-time unavailable)
- Tool used to retrieve it

Quote only what is directly retrievable. Flag inferred or synthesized content.

---

## Output format

```
## Summary
[1–2 sentences: what was found and with what confidence]

## Findings
[Structured by topic, not by tool]

## Sources
| # | Title | URL | Tool |
|---|---|---|---|
```

---

## Auto-trigger signals

Apply this skill automatically (without the user naming it) when:
- Query spans multiple sub-questions
- Topic is fast-moving (news, releases, security advisories)
- User asks for "thorough", "comprehensive", "everything about"
- First search pass returns low-signal results
