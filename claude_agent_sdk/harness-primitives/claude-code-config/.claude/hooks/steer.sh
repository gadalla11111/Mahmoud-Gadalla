#!/usr/bin/env bash
# PreToolUse hook — surfaces STEER.md to the agent once and clears it.
set -euo pipefail

ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo .)
STEER="$ROOT/STEER.md"

if [[ -f "$STEER" ]]; then
  echo "=== OPERATOR STEERING NOTE ===" >&2
  cat "$STEER" >&2
  echo "=== END NOTE ===" >&2
  rm "$STEER"
fi
