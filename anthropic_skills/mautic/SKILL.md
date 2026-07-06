# Skill: mautic

**Trigger:** marketing automation, email drip campaigns, lead nurturing, lead scoring, campaign builder, "automate my marketing emails", open-source HubSpot alternative, self-hosted marketing automation.

---

## What this skill does

Guides setup and use of Mautic — the open-source marketing automation platform.
Email campaigns, landing pages, lead scoring, CRM sync, multi-channel automation.

**Source:** `mautic/mautic`

---

## Core capabilities

| Feature | Description |
|---|---|
| Email campaigns | Drip sequences, broadcasts, A/B testing |
| Landing pages | Built-in page builder with form capture |
| Lead scoring | Rule-based scoring on behavior + attributes |
| Segments | Dynamic contact lists based on filters |
| Campaigns | Visual drag-and-drop campaign builder |
| Integrations | CRM sync (Salesforce, Twenty), webhooks, plugins |
| API | REST API for contacts, campaigns, events |

---

## Quick setup

```bash
# Docker
docker run -d \
  -e MAUTIC_DB_HOST=db \
  -e MAUTIC_DB_USER=mautic \
  -e MAUTIC_DB_PASSWORD=secret \
  -p 8080:80 \
  mautic/mautic:latest
```

---

## Campaign automation pattern

```php
// Via Mautic REST API — add contact + trigger campaign
POST /api/contacts/new
{ "email": "user@example.com", "firstname": "John" }

POST /api/campaigns/{id}/contact/{contactId}/add
```

---

## When to use vs Mailchimp/ActiveCampaign

- Full data ownership + EU data residency required → Mautic self-hosted
- Heavy customization (custom scoring rules, webhooks) → Mautic
- Need managed/no-ops email automation → ActiveCampaign, Mailchimp

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/twenty
archetype: marketing-automation
```
