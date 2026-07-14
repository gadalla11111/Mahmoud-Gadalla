# Plugin Index

_Generated 2026-07-14 from ~/.qoderwork/plugins/_

**Total: 16 plugins**

| Plugin | Display | Version | Author | Description |
|---|---|---|---|---|
| `ali1688-seller-assistant` | 1688 Seller Assistant | 1.0.0 | Mahmoud Gadalla | One-stop support for 1688 merchants, from shop diagnosis to product operations, helping sellers read data clearly, optimize listings, and boost conversion. |
| `alibabacloud-core` | Alibaba Cloud Core | 1.0.20 | Mahmoud Gadalla | Core Alibaba Cloud plugin for OpenAPI SDK code generation through a constrained MCP server. |
| `alibabacloud-spec-ops` | Alibaba Cloud AI Spec Ops | 0.1.4 | Mahmoud Gadalla | Alibaba Cloud AI Ops Plugin - Infrastructure operations workflow with intelligent planning, validation, and execution powered by MCP tooling. |
| `consulting-delivery` | Consulting Delivery | 1.1.1 | Mahmoud Gadalla | Full-cycle management consulting toolkit covering seven core scenarios: desk research, interview notes, framework design, report writing, benchmarking, weekly status reports, and e |
| `contract-management` | Contract Management | 1.1.1 | Mahmoud Gadalla | Full-lifecycle contract management: review contract risks (red/yellow/green grading), draft contract first drafts (Word output), redline comparison of two contract versions, rapid  |
| `corporate-finance-tax` | Corporate Finance & Tax | 1.1.1 | Mahmoud Gadalla | Corporate finance and tax management toolkit covering financial analysis, journal entries, budget analysis, VAT management, annual CIT settlement, internal audit, financial stateme |
| `corporate-legal` | Corporate Legal | 1.1.2 | Mahmoud Gadalla | Comprehensive corporate legal assistant: draft legal documents (demand letters, complaints, defense statements, legal opinions), generate corporate resolutions and articles of asso |
| `equity-research` | Equity Research | 1.1.2 | Mahmoud Gadalla | End-to-end equity research toolkit for sell-side and buy-side analysts, covering deep-dive reports, industry research, annual report analysis, earnings reviews, field research note |
| `investment-banking` | Investment Banking | 1.1.2 | Mahmoud Gadalla | AI-powered investment banking assistant covering six core workflows: IPO prospectus drafting, M&A advisory reports, bond offering memoranda, regulatory response to exchange inquiri |
| `marketing` | Marketing | 1.1.1 | Mahmoud Gadalla | Full-spectrum marketing toolkit covering copywriting, ad compliance, competitive tracking, campaign planning, social media trends, SEO optimization, marketing performance analysis, |
| `pe-vc-investment` | Private Equity | 1.1.2 | Mahmoud Gadalla | End-to-end PE/VC toolkit covering deal screening, due diligence checklists, term sheet review, investment committee memos, return modeling, and exit analysis. Built for investment  |
| `product-design` | Product Design | 0.5.10 | Mahmoud Gadalla | A full-process toolkit for designers, covering eleven core scenarios: problem definition, user research, information architecture, interaction flows, visual standards, marketing as |
| `product-management` | Product Management | 1.1.1 | Mahmoud Gadalla | An end-to-end product management toolkit covering eight core workflows: PRD writing, user story breakdown, competitive analysis, requirement prioritization, user feedback analysis, |
| `qoder-for-cn-litigation` | 中国民商事诉讼工具箱 | 1.0.0 | Mahmoud Gadalla | Full-lifecycle Chinese civil & commercial litigation toolkit for legal counsel and attorneys. 20 skills across four layers: routing (hub + onboarding interview + quick-config edito |
| `wealth-management` | Wealth Management | 1.1.2 | Mahmoud Gadalla | Full-spectrum wealth management toolkit covering market snapshots, asset allocation, fund analysis, client reporting, financial planning, and tax planning. Built for relationship m |
| `yqx-tech-service-suite` | 科技服务助手 | 1.1.0 | Mahmoud Gadalla | A full-chain technology service toolkit bridging demand and supply in a closed loop. The demand side covers tech demand mining, results search & matching, value assessment, deal pl |

## Per-plugin layout

```
<plugin>/
  .qoder-plugin/plugin.json    # Plugin manifest
  .mcp.json                    # Connector / MCP server config
  CONNECTORS.md                # Connector documentation
  README.md / README_EN.md     # User-facing docs (CN + EN)
  assets/icon.svg              # Plugin icon
  skills/<skill-name>/SKILL.md # Individual skills
```