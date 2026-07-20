# AGENTS.md — crawl4ai-mcp-poc

## What this is
A proof-of-concept MCP (Model Context Protocol) server that wraps [Crawl4AI](https://github.com/unclecode/crawl4ai) for AI-accessible web scraping. Uses stdio transport.

## Stack
- **Python** / **FastMCP**
- Stdio-based MCP server

## Build / Test
```bash
# Install dependencies
uv sync

# Run the MCP server
python -m crawl4ai_mcp_poc
```

## Conventions
- Follow existing Python style (PEP 8)
- MCP tool definitions should have clear descriptions and input schemas
- Keep the server lightweight — no unnecessary dependencies

## AI Assistant Notes
- This is a PoC — focus on functionality over production hardening
- Test MCP tool calls end-to-end before proposing changes
- Do not add web UI or HTTP transport without discussion
