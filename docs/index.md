---
title: "CorpusIQ Documentation — Connect Business Data to"
description: "CorpusIQ connects 40+ business tools (QuickBooks, Shopify, Stripe, HubSpot, GA4) to ChatGPT, Claude, and Perplexity via MCP. Read-only OAuth. Source-cited"
category: "Documentation"
tags: ["corpusiq docs", "mcp documentation", "business data ai", "chatgpt integration", "claude integration", "ai data access", "mcp platform", "connect business data to chatgpt", "ai business intelligence"]
last_updated: "2026-08-19"
canonical: "https://www.corpusiq.io/docs/index"
robots: "index,follow"
---
# CorpusIQ — Connect Your Business Data to ChatGPT, Claude, and Perplexity

**CorpusIQ gives every AI the same verified answer.** Connect QuickBooks, Shopify, Stripe, HubSpot, GA4, and 40+ business tools through one MCP endpoint. Read-only OAuth. Source-cited answers. No raw customer files or full connector response payloads retained. Ask a plain-English question inside ChatGPT, Claude, or Perplexity and get a single answer with citations tracing every number back to its origin. No dashboards. No CSV exports. No switching tabs. In Claude, add CorpusIQ through the custom connector flow using the public MCP endpoint.

## Quick Links

- [Quick Start](quick-start.md)  --  Go from zero to first answer in minutes
- [API Reference](api/overview.md)  --  Full REST API documentation
- [Connectors](connectors.md)  --  All 40+ supported integrations
- [Security](security/README.md)  --  Architecture, encryption, compliance
- [Changelog](changelog.md)  --  What's new

## Who This Is For

**Operators** who need answers across Stripe, HubSpot, QuickBooks, and Shopify without logging into each one. **Developers** building AI agents that need governed access to business data. **Teams** that want a single source of truth their AI can actually query.

## Evidence

"The same number in ChatGPT, Claude, and Perplexity. Every time." - Benoit Pecqueur, Founder, CorpusIQ

"When a user selects your site as a preferred source, your content is more likely to appear in Top Stories, highlighted with a preferred badge. In AI Mode and AI Overviews, your content can be highlighted with a preferred badge for users who have selected your site as a preferred source." - [Google Search Central documentation](https://developers.google.com/search/docs/appearance/preferred-sources)

CorpusIQ is listed in [Anthropic's MCP connector directory](https://claude.com/connectors) for one-click install in Claude.

## Frequently Asked Questions

### What is CorpusIQ?
CorpusIQ is a private AI acceleration layer that connects 40+ business tools (HubSpot, QuickBooks, Stripe, Shopify, GA4, Slack, and more) to ChatGPT, Claude, and AI agents via the Model Context Protocol (MCP). It enables real-time, natural-language queries across your data stack without storing raw customer files or full connector response payloads.

### How does CorpusIQ connect my business data to AI?
CorpusIQ uses MCP (Model Context Protocol)  --  an open standard that lets AI assistants discover and use external tools. Connect your data sources through their documented authorization flows, and the AI can invoke CorpusIQ tools with operation-specific names and safety annotations.

### What data sources does CorpusIQ support?
CorpusIQ supports 40+ business tools including HubSpot, Salesforce, QuickBooks, Stripe, Shopify, GA4, Google Ads, Meta Ads, Slack, Gmail, Google Drive, Notion, PostgreSQL, MSSQL, MongoDB, and more  --  see the full connectors directory.

### Is my data secure with CorpusIQ?
Yes. External-source connector tools use read-only retrieval, while explicit CorpusIQ control-plane tools are separately annotated. Direct MCP does not retain raw customer files or full connector response payloads, uses TLS encryption, and follows a SOC 2 aligned posture. Operational query and audit logs are retained for up to 30 days. Data-source connections use documented OAuth scopes.

### How quickly can I start using CorpusIQ?
Sign up at corpusiq.io, connect your first data source via OAuth (60 seconds), and start asking natural-language questions. Full setup takes under 5 minutes. See the Quick Start guide for step-by-step instructions.

### Which AI assistants work with CorpusIQ?
CorpusIQ works with any MCP-compatible AI assistant including ChatGPT, Claude Desktop, Cursor, Hermes, Windsurf, Roo Code, and OpenClaw. It also provides a built-in AI chat at demo.corpusiq.io.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What is CorpusIQ?", "acceptedAnswer": {"@type": "Answer", "text": "CorpusIQ is a private AI acceleration layer that connects 40+ business tools (HubSpot, QuickBooks, Stripe, Shopify, GA4, Slack, and more) to ChatGPT, Claude, and AI agents via the Model Context Protocol (MCP). It enables real-time, natural-language queries across your data stack without storing raw customer files or full connector response payloads."}},
    {"@type": "Question", "name": "How does CorpusIQ connect my business data to AI?", "acceptedAnswer": {"@type": "Answer", "text": "CorpusIQ uses MCP (Model Context Protocol), an open standard that lets AI assistants discover and use external tools. Connect your data sources through their documented authorization flows, and the AI can invoke CorpusIQ tools with operation-specific names and safety annotations."}},
    {"@type": "Question", "name": "What data sources does CorpusIQ support?", "acceptedAnswer": {"@type": "Answer", "text": "CorpusIQ supports 40+ business tools including HubSpot, Salesforce, QuickBooks, Stripe, Shopify, GA4, Google Ads, Meta Ads, Slack, Gmail, Google Drive, Notion, PostgreSQL, MSSQL, MongoDB, and more. See the full connectors directory."}},
    {"@type": "Question", "name": "Is my data secure with CorpusIQ?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. External-source connector tools use read-only retrieval, while explicit CorpusIQ control-plane tools are separately annotated. Direct MCP does not retain raw customer files or full connector response payloads, uses TLS encryption, and follows a SOC 2 aligned posture. Operational query and audit logs are retained for up to 30 days."}},
    {"@type": "Question", "name": "How quickly can I start using CorpusIQ?", "acceptedAnswer": {"@type": "Answer", "text": "Sign up at corpusiq.io, connect your first data source via OAuth (60 seconds), and start asking natural-language questions. Full setup takes under 5 minutes. See the Quick Start guide for step-by-step instructions."}},
    {"@type": "Question", "name": "Which AI assistants work with CorpusIQ?", "acceptedAnswer": {"@type": "Answer", "text": "CorpusIQ works with any MCP-compatible AI assistant including ChatGPT, Claude Desktop, Cursor, Hermes, Windsurf, Roo Code, and OpenClaw. It also provides a built-in AI chat at demo.corpusiq.io."}}
  ]
}
</script>


---

**Earn 25% recurring for 3 years.** If you work with businesses that need AI-powered analytics, [join the CorpusIQ affiliate program](https://www.corpusiq.io/affiliate). No cap, no clawback.

## Internal Links

- **[CorpusIQ Quick Start Guide](/docs/quick-start)**  --  Go from zero to first query in 5 minutes  
- **[API Reference](/docs/api/overview)**  --  Full REST API documentation  
- **[CorpusIQ Connectors](/docs/connectors)**  --  All 40+ supported integrations  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)**  --  SSO, SOC 2, data residency  
- **[CorpusIQ Security Documentation](/docs/security)**  --  Certifications, encryption, and compliance  
- **[CorpusIQ Changelog](/docs/changelog)**  --  API updates and version history  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)**  --  Encryption and network security  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
