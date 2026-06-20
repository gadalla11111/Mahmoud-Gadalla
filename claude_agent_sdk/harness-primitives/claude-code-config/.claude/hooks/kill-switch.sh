#!/usr/bin/env bash
# PreToolUse hook — halts all tool calls while AGENT_STOP exists at project root.
set -euo pipefail

ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo .)
if [[ -f "$ROOT/AGENT_STOP" ]]; then
  echo '{"decision":"block","reason":"AGENT_STOP file present. Remove it to resume."}' >&2
  exit 2
fi
