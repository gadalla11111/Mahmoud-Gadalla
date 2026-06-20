#!/usr/bin/env bash
# PreToolUse hook — blocks writes to test-results.json unless evidence was read first.
set -euo pipefail

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name // ""')
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // ""')
RESULTS_FILE="test-results.json"

if [[ "$TOOL" =~ ^(Write|Edit|Bash)$ ]] && [[ "$FILE" == *"$RESULTS_FILE"* ]]; then
  EVIDENCE_COUNT=$(wc -l < ".claude/.evidence-reads" 2>/dev/null || echo 0)
  if [[ "$EVIDENCE_COUNT" -lt 1 ]]; then
    echo '{"decision":"block","reason":"No evidence read before marking test-results.json. Open a screenshot or log first."}' >&2
    exit 2
  fi
  # Reset after gate passes so next feature starts clean.
  > ".claude/.evidence-reads"
fi
