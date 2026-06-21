# ⚔️ Tokslayer

> **Stop dragging dead context through your conversation.**

You paste a README.

Claude reads:

* navigation
* badges
* legal boilerplate
* installation variants
* marketing copy
* repeated explanations

You wanted the product.

Claude got the whole website.

Tokslayer strips the noise, keeps the signal, and leaves a compact version in the conversation.

---

## The problem

Most people optimize what they type.

Almost nobody optimizes what they paste.

Yet developers constantly paste:

* GitHub READMEs
* Research papers
* API docs
* Jira tickets
* Confluence pages
* Slack threads
* PR descriptions
* Emails

These documents are full of text that helps humans navigate them but does nothing for the task you're trying to solve.

Examples:

```text
Skip to content
Repository navigation
Contributors
License
Star History
Sponsor
Related Projects
```

Useful on GitHub.

Useless when you're asking:

```text
Explain how this works.
```

---

## What Tokslayer does

When you paste content and give a command:

```text
[pasted content]

summarize
```

```text
[pasted content]

review
```

```text
[pasted content]

explain
```

Tokslayer:

1. Detects pasted content
2. Removes navigation and boilerplate
3. Removes redundant explanations
4. Removes filler language
5. Preserves technical details
6. Answers using the compact version

Example:

```text
ORIGINAL:
Skip to content...
Repository navigation...
License...
Sponsor...

OPTIMIZED:
Trooper: local-first LLM proxy.
Ollama default.
Escalate to Claude.
Preserves session context.
```

---

## What gets removed

* Navigation chrome
* Footers
* Share links
* Legal boilerplate
* Marketing copy
* Corporate filler
* Duplicate explanations
* Repeated sentences

Examples:

```text
"in order to"
→
"to"
```

```text
"is responsible for"
→
"handles"
```

```text
"it should be noted that"
→
[removed]
```

---

## What stays

* Code blocks
* Stack traces
* URLs
* File paths
* Numbers
* Error messages
* Technical terms
* Proper nouns
* Variable names

Meaning stays.

Noise goes.

---

## Why it matters

Without Tokslayer:

```text
Paste README
↓
README stays in conversation
↓
README influences every future turn
```

With Tokslayer:

```text
Paste README
↓
README compressed
↓
Conversation carries signal instead of noise
```

The longer the session runs, the more valuable that becomes.

---

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/shouvik12/tokslayer/main/install.sh | bash
```

Or:

```bash
mkdir -p ~/.claude/skills/tokslayer

curl -o ~/.claude/skills/tokslayer/SKILL.md \
  https://raw.githubusercontent.com/shouvik12/tokslayer/main/.claude/skills/tokslayer/SKILL.md
```

Restart Claude Code.

Done.

---

## How it works

No proxy.

No server.

No MCP.

No model fine-tuning.

Just a `SKILL.md`.

Claude detects pasted content, compresses it, and reasons over the compressed representation.

---

## Works with

* Claude Code
* Any agent that supports `SKILL.md`

---

## Roadmap

### Today

Compress pasted content into a denser representation.

### Next

Automatic subagent delegation.

```text
Large document
↓
Subagent
↓
Compression
↓
Compact result
↓
Main conversation
```

The raw document never enters the primary thread.

Only the signal does.

---

## Related

| Project   | Purpose                              |
| --------- | ------------------------------------ |
| trooper   | Route between local and cloud models |
| tokslayer | Compress clipboard context           |

Trooper keeps sessions alive.

Tokslayer keeps them lean.

---

## License

MIT
