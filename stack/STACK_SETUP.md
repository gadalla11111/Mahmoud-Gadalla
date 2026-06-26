# Stack Setup — Plugins & MCP (Claude Code CLI / desktop)

How to connect the **Plugins** and **MCP** columns from *My Claude Stack* on your
own machine. The **Skills** column is already native in `anthropic_skills/` and
needs no setup. This guide targets the **Claude Code CLI / desktop app**.

> Every URL, package name, and slug in the template files is a **placeholder**
> marked `REPLACE_…` / `_status: verify`. Confirm each against the vendor's current
> docs before connecting — they change, and I won't guess credentials or endpoints.

---

## 1. MCP servers

The 8 MCP servers from the image. Template: [`mcp-servers.stack.json`](./mcp-servers.stack.json).

### Why this isn't the live `.mcp.json`
The repo's `.mcp.json` runs this project's own servers (`umbriel`, `diffgate`,
`memex`). Adding unconfigured external servers there would make every session try
(and fail) to connect to Slack/Notion/etc. So the stack servers live in a separate
template you merge locally.

### Add them (two ways)

**A. CLI (recommended)** — one command per server:
```bash
# stdio (local process)
claude mcp add perplexity -- npx -y <perplexity-mcp-package>
# remote (hosted URL)
claude mcp add --transport http notion https://<notion-mcp-endpoint>
```
Remote servers prompt you to connect your account the first time — confirm once.

**B. Merge the JSON** — copy the entries you want from `mcp-servers.stack.json`
into your project `.mcp.json` under `mcpServers`, then replace every `REPLACE_…`.

### Per-server notes
| Server | Transport | What to verify | Auth |
|---|---|---|---|
| granola | stdio | package name (already connected in some envs) | account |
| slack | http | hosted MCP endpoint URL | sign-in |
| notion | http | hosted MCP endpoint URL | sign-in |
| kondo | stdio/http | package or endpoint | LinkedIn auth |
| zapier | http | your personal Zapier MCP URL (generate in Zapier) | per-URL |
| higgsfield | stdio | package + `HIGGSFIELD_API_KEY` | API key |
| perplexity | stdio | package + `PERPLEXITY_API_KEY` | API key |
| agent-browser | stdio | package + local browser binary | none |

Put API keys in your shell env (`export PERPLEXITY_API_KEY=…`), never inline in JSON.

---

## 2. Plugins

The Plugins column splits into **tooling plugins** (install) and **skill bundles**
(already native here).

### Tooling plugins — install via marketplace
```bash
# add the marketplace, then install
/plugin marketplace add OWNER/REPO        # the plugin's marketplace repo
/plugin install gstack@<marketplace>
/plugin install superpowers@<marketplace>
/plugin install codex-plugin-cc@<marketplace>
```
Or browse interactively with `/plugin`. The equivalent committed-settings shape is
in [`settings.plugins.template.json`](./settings.plugins.template.json) (merge into
`.claude/settings.json`, **not** `settings.local.json`).

### Skill bundles — already native, no plugin needed
| Reference plugin | Native here |
|---|---|
| marketingskills | `brand-framework` · `linkedin-branding` · `social-audit` · `social-content` |
| social-media-skills | `social-content` · `social-audit` · `linkedin-branding` |
| financial-services | `skills/custom_skills/analyzing-financial-statements` · `creating-financial-models` |
| claude-for-legal | `anthropic_skills/legal-practice` |
| claude-skills (263+) | discover + install on demand via `anthropic_skills/find-skills` |

---

## 3. Verify

```bash
claude mcp list          # shows configured servers + connection status
/plugin                  # shows installed plugins
```

A server showing "failed" usually means a wrong package/URL or missing env var —
re-check the per-server row above.

---

## What works where

| Surface | MCP | Plugins | Skills |
|---|---|---|---|
| **CLI / desktop** (your target) | ✅ full, after auth | ✅ | ✅ |
| Claude Code on the web | ⚠️ needs a network policy allowing each service | ⚠️ varies | ✅ |
| This sandboxed session | ❌ can't complete external sign-in | ❌ | ✅ |

The Skills column is the part that works everywhere — which is why it was built
natively into the repo first.
