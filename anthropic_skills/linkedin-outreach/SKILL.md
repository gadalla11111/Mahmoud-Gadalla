---
name: linkedin-outreach
description: >
  Plans and drafts LinkedIn outreach — connection requests, opening messages,
  and follow-up sequences — that get replies without being spammy. Builds an ICP,
  segments a prospect list, writes personalized first-touch and multi-step
  follow-ups, and tracks reply/positive-reply rates. Use when a user wants to run
  outbound on LinkedIn (sales, recruiting, partnerships). Trigger on: "LinkedIn
  outreach", "cold DM", "connection request message", "outreach sequence", "book
  meetings on LinkedIn", "automate LinkedIn DMs". Archetype: Workflow Automation.
  Distinct from linkedin-branding (inbound authority/content).
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<offer + target persona> [--sequence | --message]"
auto-trigger:
  - LinkedIn outreach, cold DM, or connection-request message
  - building an outreach sequence to book meetings on LinkedIn
  - personalizing outbound to a prospect list
do-not-trigger:
  - inbound authority/content strategy (use linkedin-branding)
  - paid LinkedIn ads (use media-buyer)
  - triaging an existing inbox (different tool)
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# LinkedIn Outreach

Plans outbound that earns replies: the right person, a relevant reason to talk,
and a short human sequence — not a spray of templated DMs. Outbound (this skill)
is distinct from inbound authority-building (`linkedin-branding`).

---

## Step 0 — ICP & Segments

Before any message, define **who** and **why now**:
- ICP: role, company stage/size, the trigger that makes them relevant *now*
- Segments: group the list so each gets a different angle (e.g. recent funding, hiring for X, posted about Y)

A generic list gets generic replies. Personalization beats volume.

---

## The Sequence (4 touches, value-first)

| Touch | Timing | Goal |
|---|---|---|
| **1 · Connect** | day 0 | Personalized request — a *specific* reason, no pitch |
| **2 · Open** | on accept | One line of relevance + a soft, low-friction question |
| **3 · Value** | +3 days | Give something useful (insight, resource) — still no hard ask |
| **4 · Ask** | +5 days | The clear, small ask (15 min? a resource?) — easy to say yes |

Stop on reply. Never send all four if they respond at touch 2.

---

## Message Rules

- **Personalize the first line** to something real on their profile/activity — never "I came across your profile".
- **One idea per message**, short (LinkedIn rewards brevity).
- **Soft asks early, clear ask late** — earn the reply before requesting time.
- **No fake familiarity, no flattery spam** — relevance, not charm.
- **Respect "no"** — one graceful follow-up max after a decline.

---

## Output Format

```markdown
# LinkedIn Outreach — [offer] → [persona]

## ICP & Trigger
[role · stage · why-now trigger]

## Sequence
| # | Touch | Timing | Message |
|---|---|---|---|
| 1 | Connect | day 0 | [≤300 chars, specific reason] |
| 2 | Open | on accept | [relevance + soft question] |
| 3 | Value | +3d | [useful give] |
| 4 | Ask | +5d | [small, clear ask] |

## Personalization tokens
[{{first_name}}, {{trigger}}, {{their_post}} — what to swap per prospect]

## Track
Reply rate · positive-reply rate · meetings booked
```

---

## Ethics & Compliance

- Personalize genuinely; don't mass-blast identical "personalized" messages.
- Respect LinkedIn's automation limits and people's time — outreach is permissioned conversation, not spam.
- Never fabricate a shared connection or a fake reason to connect.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Build inbound authority instead | `linkedin-branding` |
| The offer's positioning is unclear | `brand-framework` |
| Persuasion principles for the ask | `persuasion-psychology` |
| Strip AI tells from the messages | `humanizer` |

---

## Rules

- **ICP + trigger before messages** — relevance beats volume.
- **Value before the ask** — soft early, clear late.
- **First line is genuinely personal** — never a template opener.
- **Stop on reply** — don't run the whole sequence at someone engaging.
- **No fake familiarity** — real reason or no message.
