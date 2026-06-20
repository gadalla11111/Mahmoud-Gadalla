# Claude Code JetBrains Plugin — v0.1.14-beta

## Install

1. Open your JetBrains IDE (IntelliJ IDEA, PyCharm, WebStorm, etc.)
2. Go to **Settings → Plugins → ⚙️ gear icon → Install Plugin from Disk...**
3. Select `claude-code-jetbrains-plugin-0.1.14-beta.zip` from this folder
4. Click **OK** and restart the IDE

## What it includes

| JAR | Purpose |
|---|---|
| `claude-code-jetbrains-plugin-0.1.14-beta.jar` | Main plugin |
| `kotlin-sdk-jvm-0.4.0.jar` | Anthropic Kotlin SDK |
| `ktor-*` jars | HTTP/WebSocket client (SSE streaming) |
| `kotlinx-coroutines-*` | Async runtime |
| `jansi` | Terminal color support |

## Requirements

- JetBrains IDE 2023.1 or later
- Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
- `ANTHROPIC_API_KEY` set in your environment
