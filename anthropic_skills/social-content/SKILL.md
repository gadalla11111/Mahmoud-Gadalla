---
name: social-content
description: >
  Multi-platform social content engine — turns one idea into platform-native
  posts, reels/short-video scripts, captions, and a posting calendar. Use when a
  user wants content created (not audited) for Instagram, TikTok, X, LinkedIn,
  YouTube Shorts, or Facebook. Trigger on: "write posts for", "make a reel
  script", "content for my socials", "caption for", "repurpose this for",
  "content calendar for posts". Archetype: Workflow Automation. Differs from
  social-audit (diagnoses existing presence) and linkedin-branding (LinkedIn-only
  authority system). Cross-references social-audit for what's working first.
allowed-tools: [WebSearch, WebFetch, Read, Write]
argument-hint: "<idea or asset> [--platforms ig,tiktok,x,li,yt] [--reel | --calendar]"
auto-trigger:
  - write posts for a social platform
  - make a reel script or short-video script
  - caption for a post
  - repurpose this for multiple platforms
  - building a multi-platform content calendar
do-not-trigger:
  - auditing existing social performance (use social-audit)
  - LinkedIn-only authority strategy (use linkedin-branding)
  - paid ad creative for a specific ad platform
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Social Content

One idea, every platform — natively. Produces posts, reel/short scripts, captions, and a calendar, each shaped to the platform's algorithm and audience.

---

## Step 0 — One Idea, Many Cuts

Start from a single core idea, then adapt per platform. Never cross-post the same asset verbatim — platform-native formats win (see `social-audit`).

| Platform | Native format | Hook window | Length |
|---|---|---|---|
| **TikTok / Reels / Shorts** | vertical video, sound-on | first 1–2 s | 15–45 s script |
| **Instagram feed** | carousel or single, save-worthy | first line + cover | 8–10 slide carousel |
| **X** | text-first, threadable | first 7 words | 1 hook + optional thread |
| **LinkedIn** | text + doc carousel | first 2 lines (before "…more") | one idea, professional |
| **YouTube Shorts** | vertical, retention-driven | first 3 s | 30–60 s script |
| **Facebook** | native video / link + context | first line | short, shareable |

---

## Output per Platform

### Short-video script (`--reel`)
```markdown
## [Platform] Reel — [Hook idea]
**Hook (0–2s)**: [pattern interrupt — visual + line]
**Beats**:
- 0–2s  [hook]
- 2–8s  [the one point]
- 8–20s [proof / demo]
- 20s+  [payoff + CTA]
**On-screen text**: [captions per beat]
**Caption**: [post copy + 3–5 niche hashtags]
**Sound**: [trending-sound suggestion or original]
```

### Feed post / carousel
```markdown
## [Platform] — [Idea]
**Cover / first line**: [stop-the-scroll]
**Slides / body**: [one idea per slide, 8–10 max]
**Caption**: [hook → value → CTA]
**Hashtags**: [3–5 niche > generic]
```

### Calendar (`--calendar`)
```markdown
| Day | Platform | Format | Hook | Core idea | CTA |
```

---

## Content Principles (2026)

- **Native format beats cross-post** — re-cut per platform, never paste the same file everywhere
- **Hook in the first beat** — 1–2s video, first line text; the algorithm decides fast
- **One idea per asset** — split multi-point ideas into multiple posts
- **Quality signals** — design for saves/shares/replies, not impressions
- **Sound-on by default** for short video; captions always (accessibility + silent viewing)
- **Niche over generic** hashtags and references

---

## Research Discipline

- Check current trending formats/sounds for the niche via WebSearch before scripting
- If claims/stats appear in content, verify with `fact-checker`
- Pull what already works for this account from a prior `social-audit` if available

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| What's already working on these channels | `social-audit` (run first) |
| LinkedIn authority system specifically | `linkedin-branding` |
| Underlying brand voice/positioning | `brand-framework` / `brand-guidelines` |
| Turn a script into actual video | `hyperframes` |
| Animated GIF for Slack/community | `slack-gif-creator` |

---

## Rules

- **Re-cut, never cross-post** — each platform gets a native version.
- **Hook first** — 1–2s for video, first line for text.
- **One idea per asset** — split, don't cram.
- **Design for saves/shares** — quality signals over raw reach.
- **Verify any stat** before it goes in a caption.
