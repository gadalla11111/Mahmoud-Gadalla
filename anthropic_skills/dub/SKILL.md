# Skill: dub

**Trigger:** link shortening, link tracking, click attribution, affiliate link management, UTM parameters, conversion tracking, "track my links", link analytics, referral attribution.

---

## What this skill does

Integrates Dub — the open-source link attribution platform (100M+ clicks/month).
Creates short links, tracks conversions, manages affiliate programs.

**Source:** `dubinc/dub`

---

## Core capabilities

- Short link creation with custom slugs and domains
- Click tracking with full attribution (country, device, referrer, UTM)
- Conversion events (signup, purchase) tied back to link clicks
- Affiliate program management with commission tracking
- Analytics API for reporting

---

## Quick integration

```typescript
import { Dub } from "dub";

const dub = new Dub({ token: process.env.DUB_API_KEY });

// Create a tracked link
const link = await dub.links.create({
  url: "https://yoursite.com/pricing",
  domain: "go.yoursite.com",
  key: "pricing-q4",
  utm_source: "email",
  utm_campaign: "q4-launch"
});
// → { shortLink: "https://go.yoursite.com/pricing-q4" }

// Track a conversion event
await dub.track.lead({
  clickId: req.cookies['dub_id'],  // auto-set by Dub script
  eventName: "Signup",
  customerId: user.id
});
```

---

## Self-hosted setup

```bash
git clone https://github.com/dubinc/dub
cd dub
cp .env.example .env  # fill DATABASE_URL, NEXTAUTH_SECRET, etc.
pnpm install && pnpm build
pnpm start
```

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references: []
archetype: link-attribution
```
