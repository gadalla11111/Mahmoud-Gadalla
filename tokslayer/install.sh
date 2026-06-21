#!/usr/bin/env bash
set -e

SKILL_DIR="$HOME/.claude/skills/tokslayer"
SKILL_URL="https://raw.githubusercontent.com/shouvik12/tokslayer/main/.claude/skills/tokslayer/SKILL.md"

echo "⚔️  tokslayer — slaying tokens before they reach Claude"
echo ""

mkdir -p "$SKILL_DIR"

if command -v curl &>/dev/null; then
    curl -fsSL "$SKILL_URL" -o "$SKILL_DIR/SKILL.md"
elif command -v wget &>/dev/null; then
    wget -q "$SKILL_URL" -O "$SKILL_DIR/SKILL.md"
else
    echo "Error: curl or wget required"
    exit 1
fi

echo "✅ Installed to $SKILL_DIR/SKILL.md"
echo ""
echo "Restart Claude Code. Tokslayer activates automatically."
echo ""
echo "Your clipboard was leaking tokens. Not anymore. ⚔️"
