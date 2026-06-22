---
name: tokslayer
version: "1.1.0"
description: "Compress pasted content into dense signal. Removes clipboard bloat from READMEs, papers, docs, tickets, emails, and web pages."
always: true
---

# Tokslayer

Turn pasted content into signal.

Most pasted content contains:

- navigation
- metadata
- boilerplate
- repeated explanations
- marketing copy
- filler language

Users want the content.

The conversation should keep the content, not the baggage.

## Pattern 1 — Pasted content + command

When a message contains a large pasted document followed by a task such as:

- summarize
- explain
- review
- analyze
- fix
- what does this mean

First create a compressed representation of the pasted content.

### Remove

- Navigation chrome
- Footers
- Headers
- Breadcrumbs
- Share links
- Metadata
- Legal boilerplate
- Marketing language
- Corporate filler
- Redundant explanations
- Repeated sentences

### Compress

Replace verbose wording with shorter wording only when meaning remains unchanged.

Examples:

- "in order to" → "to"
- "is responsible for" → "handles"
- "it should be noted that" → remove

If multiple sentences express the same idea, keep the strongest one.

### Preserve exactly

- Code blocks
- Stack traces
- URLs
- File paths
- Error messages
- Numbers
- Metrics
- Technical terms
- Variable names
- Proper nouns

### Compression Report

Before answering, show:

```
ORIGINAL: "<first 60 chars>..."
OPTIMIZED: "<first 60 chars>..."
ESTIMATED REDUCTION: ~X%
```

Use estimates only.
Never fabricate exact token counts.

### Response Behavior

Perform the requested task using the compressed representation.
Focus on signal.
Ignore removed boilerplate.

## Pattern 2 — Normal Conversation

Do not rewrite ordinary conversation.
Do not optimize short user messages.
Do not show compression reports for normal chat.
Only activate when substantial pasted content is detected.

## Hard Rules

- Preserve meaning exactly
- Preserve technical correctness
- Preserve source language
- Never modify code
- Never modify stack traces
- Never modify URLs or file paths
- Never invent facts
- Never invent savings
- If compression provides little value, leave content mostly unchanged

## Goal

Keep the signal.
Drop the baggage.
