---
title: "Agentic Atlas MCP - Field-Tested Agent-System Design Patterns"
description: "Read-only MCP consultation surface for field-tested agent-system design patterns. Eight keyless tools for orientation, card and section reads, relationship traversal, provenance, glossary terms and publication decisions, live-probed at agentic-atlas.dev/mcp with revision-coherence markers that refuse stale reads."
category: AI Agents
stars: n/a (new listing)
added: 2026-08-24
source: "mcp.so feed + live endpoint probe (8 tools verified)"
relevance: ★★
tags: [agents, design-patterns, architecture, knowledge, agent-engineering, read-only, remote-mcp]
---

# Agentic Atlas MCP

**Public, read-only consultation surface for field-tested agent-system design patterns** - a hosted knowledge corpus that both people and agents can read. Eight keyless tools map ordinary design vocabulary to canonical patterns, read the corpus at card, section, or full-node depth, and traverse relationships, provenance, glossary terms and publication decisions. Live-probed stateless endpoint at `https://agentic-atlas.dev/mcp/` (server v3.4.7, protocol 2025-06-18), no account and no credentials.

```
Server type: Remote (Streamable HTTP, hosted, stateless)
Auth: None
Endpoint: https://agentic-atlas.dev/mcp/
Tools: 8 (live-probed; server v3.4.7, protocol 2025-06-18)
Pricing: free
Category: AI & Agents
Built by: Avery Jones (github.com/aj604/agentic-atlas-plugin)
```

## Why This Matters for Operators

Agent systems fail in predictable ways - unbounded context, unclear ownership of decisions, drift between what was designed and what was shipped. Agentic Atlas is the reference layer for those failures: patterns that have been field-tested, with provenance for every claim and publication decisions kept visible. **The corpus is versioned: every payload carries a coherence marker, and a tool call that carries a stale marker is refused with `revision_changed` instead of silently answering from a different release** - the same read-your-writes discipline operators want in their own systems.

For a team building or buying agent infrastructure, this is a cheap, keyless way to have an agent consult established design practice before it invents one.

## Tools & Capabilities

8 read-only tools confirmed by live probe:

| Tool | Purpose |
|---|---|
| atlas_orient | Entry point: map ordinary design vocabulary (e.g. "context window budget") to canonical node identities; paged results with kind/status filters |
| atlas_cards | Read 1-4 canonical ids as ordered cards: identity, one-line hook, sealed decision-bearing claims with source addresses |
| atlas_read | Exact section wording or a complete multi-section node |
| atlas_links | Traverse relationships between nodes |
| atlas_provenance | Expanded provenance for a card's claims |
| atlas_navigate | Walk the canonical tree or the publisher-curated tour |
| atlas_define | Glossary term lookup |
| atlas_decisions | Publication decisions for a node |

Calls are idempotent and read-only (annotated `readOnlyHint`), and results carry `scope` metadata (total/returned/truncated) with cursor pagination. An empty result is a successful empty payload, not an error.

## Installation

```bash
claude mcp add agentic-atlas --transport http https://agentic-atlas.dev/mcp/
```

No local installation, no account, no credentials. Works with Claude Code, Cursor, VS Code, Codex and any MCP-compatible client.

## Configuration

```json
{
  "mcpServers": {
    "agentic-atlas": {
      "type": "http",
      "url": "https://agentic-atlas.dev/mcp/"
    }
  }
}
```

The server is stateless: initialize returned no session ID and tools/list succeeds without one (MCP '26-style stateless transport). No API key of any kind.

## Business Relevance

- **Operators building agent systems** get a consultation surface for design decisions - when to add memory, how to structure approval gates, which patterns have held up in the field.
- **Architects reviewing agent stacks** get provenance for every recommendation, so a design choice can be traced to its published evidence.
- **Teams onboarding agents** get a stable glossary and canonical naming layer that a new agent can read on first contact.

## Integration with CorpusIQ

CorpusIQ is the business-data layer (QuickBooks, Stripe, HubSpot, GA4 and 40+ more connectors); Agentic Atlas is the design-practice layer. A Hermes agent composing a workflow can consult Agentic Atlas for the pattern (how should approval gates and read-only contracts be structured?) and then execute against CorpusIQ for the data (what do the numbers say?). Design wisdom from Agentic Atlas, business truth from CorpusIQ.

## Limitations

- Brand new listing (submitted Aug 24, 2026) - no long-term track record yet.
- Read-only consultation surface: it provides design guidance, not transactional APIs or execution.
- Single-source corpus: patterns reflect the publisher's curation and field testing, not an open contribution pool.
- No authentication means no personalization - every caller reads the same public release.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - curated third-party MCP servers for operators
- [MCP Integration Guide](/hermes/mcp/) - connecting MCP servers to Hermes Agent
- [Truth Bear GAUGE MCP](/hermes/mcp/servers/external/truth-bear-gauge/) - verifiable government data with the same proof-first discipline
