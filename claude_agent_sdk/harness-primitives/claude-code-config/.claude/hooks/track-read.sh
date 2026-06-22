#!/usr/bin/env bash
# PreToolUse hook — records evidence reads so verify-gate.sh can enforce them.
# Fires before every Read tool call; appends the path to .evidence-reads.
set -euo pipefail

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name // ""')
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')

EVIDENCE_PATTERNS=(
  "screenshots/"
  "test-results.json"
  "*.log"
  "*.png"
)

if [[ "$TOOL" == "Read" ]]; then
  for pat in "${EVIDENCE_PATTERNS[@]}"; do
    if [[ "$FILE" == $pat ]]; then
      echo "$FILE" >> ".claude/.evidence-reads"
      break
    fi
  done
fi
