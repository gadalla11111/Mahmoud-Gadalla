#!/usr/bin/env bash
# Stop hook — commits any uncommitted work when the session ends.
set -euo pipefail

cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)"

if ! git diff --quiet || ! git diff --cached --quiet; then
  git add -A
  git commit -m "wip: agent session checkpoint [auto]" || true
fi
