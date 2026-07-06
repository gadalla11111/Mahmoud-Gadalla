# Skill: twenty

**Trigger:** build or integrate a CRM, customer relationship management, self-hosted CRM, manage contacts/deals/pipelines, CRM data model design, "set up Twenty CRM".

---

## What this skill does

Guides setup, customization, and integration of Twenty — the #1 open-source CRM built on
React + NestJS + PostgreSQL + Redis. Supports cloud, self-hosted, and custom app development.

**Source:** `twentyhq/twenty`

---

## Core concepts

| Concept | Description |
|---|---|
| Objects | Custom data models (People, Companies, Deals, custom) |
| Views | Filtered/sorted table/kanban/timeline views of any object |
| Workflows | Automation rules triggered by object events |
| AI Agents | Built-in agents that act on CRM data |
| API | GraphQL + REST; TypeScript SDK |

---

## Quick setup (self-hosted)

```bash
git clone https://github.com/twentyhq/twenty
cd twenty
cp packages/twenty-server/.env.example packages/twenty-server/.env
# fill POSTGRES_URL, REDIS_URL, APP_SECRET
docker compose up -d
# → http://localhost:3000
```

---

## Integration patterns

```typescript
// Query contacts via GraphQL
const people = await client.query({
  query: GET_PEOPLE,
  variables: { filter: { company: { name: { eq: "Acme" } } } }
});

// Trigger workflow via API
await client.post('/api/workflows/trigger', {
  workflowId: 'deal-won',
  payload: { dealId, amount }
});
```

---

## When to use Twenty vs managed CRM

- Need full data ownership + GDPR compliance → Twenty self-hosted
- Need custom objects/fields beyond standard CRM → Twenty extensible data model
- Need managed/no-ops CRM → Salesforce, HubSpot

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/mautic
archetype: crm-integration
```
