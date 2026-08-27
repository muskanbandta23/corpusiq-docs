# PROGRESS.md — corpusiq-docs build status

Current state and ongoing work for the public docs repository.

## File count (updated August 27, 2026)

- **Total Markdown files:** 1,986
- **Total HTML files:** 1,744 (MkDocs build output)
- **Hermes subdirectory:** 30 directories covering skills, MCP servers, setup guides, blueprints, ecosystem discovery, prompts, and more
- **Docs subdirectory:** 20 directories — SEO-optimized product pages, connector guides, troubleshooting, and comparison pages
- **Skills catalog:** 501 setup guides for Hermes skills
- **MCP servers:** 504 server listing markdown pages (+ HTML companions); 601 total .md under hermes/mcp/; 382 servers / 268 guides in the external catalog
- **SEO pages:** 126 programmatic landing pages targeting high-intent operator keywords

## Site architecture

- **Main docs:** `https://www.corpusiq.io/docs/` — MkDocs Material, served on corpusiq.io
- **Hermes knowledge base:** `https://corpusiq.github.io/corpusiq-docs/hermes/` — GitHub Pages
- **SEO pages:** 100+ programmatic pages targeting high-intent keywords (e.g., "connect Shopify to ChatGPT," "MCP for ecommerce")
- **Daily automation:** Ecosystem discovery cron, skills.sh marketplace monitoring, MCP.so/mcpservers.org scans

## Items punting / skipped

- **No separate FAQ.** Folded into `how-it-works/` and `troubleshooting/` — a formal FAQ page can be added if user questions warrant it.

## Current status — August 23, 2026

The repo is actively maintained with daily automated updates:

- **Ecosystem discovery:** Nightly GitHub scan finds new Hermes-related repos.
- **MCP server scans:** MCP.so + mcpservers.org scanned daily. 536 servers listed with integration guides.
- **Skills.sh marketplace:** Daily scan for new Hermes skills. 501 setup guides published.
- **SEO pages:** 126 programmatic landing pages targeting operator search intent.
- **Content ops:** Automated internal linking, meta descriptions, OG tags, and sitemap generation.
- **Broken link repair:** Proactive weekly audit.

## Ongoing doc gaps

- **Skills sweep ✅ (Aug 27, 2026):** 15-query skills.sh tiered sweep (604 unique skills, 0 failures). 70 NEW flags all below the 100-install bar (max 54). Two PARTIAL ≥100 candidates re-verified: `mercury-ui-skills` (ihlamury/design-skills, 199 — README still Claude Code/Cursor/Copilot only; rejection holds) and `pp-mercury` (mvanhorn/printing-press-library, 124 — **rejection overturned**: the publisher README now documents first-class Hermes install paths (`hermes skills install mvanhorn/printing-press-library/cli-skills/pp-mercury`); mechanism is an agent-agnostic Go CLI, install path verified live with `npx skills add --list`). Added discrete setup guide `pp-mercury-setup.md` (🟡 Beta — Trust Hub Pass / Socket Warn / Snyk Fail, stated honestly; `workflow payment-plan` read-only approval workflow is the standout feature) + catalog index entry. Corrected the stale `printing-press-library-setup.md` cluster guide — it misdescribed the repo as a Python document-template library; the repo is actually the 472-CLI Printing Press catalog — and added its previously missing catalog index entry (501 setup guides). Mac Mini reachable this run.
- **Skills sweep ✅ (Aug 26, 2026):** 15-query skills.sh tiered sweep (605 unique skills, 0 failures). 89 NEW flags all below the 100-install bar (max 89), 113 PARTIAL. Both PARTIAL ≥100 candidates re-verified as standing rejections: `skill-composer-studio` (onewave-ai/claude-skills, 264 — Claude Code chain composer), `azure-chaos-studio` (microsoftdocs/agent-skills, 118 — Azure platform). New find: `calesthio/generative-media-skills` (137⭐ MIT, 153 skills, 2.1K indexed installs) — full media production brain with explicit HERMES.md support, direct fit for the UGC video pipeline (elevenlabs-tts, openai-gpt-image, hyperframes-video-composition, heygen-avatar-video, media-qc-delivery). Install path verified live (`npx skills add ... --list` → 151 packages; 2 YAML-parse skips documented). Added cluster setup guide `generative-media-skills-setup.md` + catalog index entry (500 setup guides; reconciled the marketplace stat line 493 → 500). Parked: oakoss/agent-skills (89), thatrebeccarae/claude-marketing (83), kyleamathews/field-lab (31), seven Hermes-named 1–8-install skills (watchlist). PII scan clean. Pushed to main, changed pages verified HTTP 200.
- **Maintenance ✅ (Aug 26, 2026, afternoon):** Catalogued 3dlogo MCP (chatmcp/mcpso issue #3779, first post-midday issue) — 3D logos and coins, remote Streamable HTTP, OAuth 2.1 PKCE + free public tier; endpoint verified live (INIT 200 serverInfo 3dlogo v1.0.0, main endpoint HTTP 401 auth gate). External catalog: 381 → 382 servers, 267 → 268 guides. New sweep report sweep-aug26-2026-afternoon.md. Fixed 98 files with malformed frontmatter (`last_updated: 2026-08-23"` missing opening quote — dates were unquoted while the closing quote remained). Bumped 3 stale last_updated dates in docs/ (chatgpt-integration, enterprise-ai-data-access, mcp-vs-data-warehouse — cutoff Aug 19). Normalized 1 connector-count straggler (docs/what-is-an-mcp-server.md "over 30" → "over 40"). Internal links: 0 broken (3 false positives = Slack mrkdwn `[text](url)` examples). PII scan clean. PROGRESS.md stats refreshed (1,976 MD, 504 server pages, 601 hermes/mcp .md). Deployed to Vercel, changed pages verified HTTP 200.
- **Maintenance ✅ (Aug 25, 2026):** Sanitized internal IP (192.168.x.x) from 2 sweep pages (sweep-august24-2026-evening, sweep-august25-2026-morning → "internal worker node"). Refreshed all 3 sitemaps (hermes-sitemap.xml 193 URLs + sitemap-index.xml 2 + sitemap.xml 323 → 2026-08-25). Connector count: 0 stragglers (canonical 40+ per corpusiq.io). Stale dates: 0 files. Internal links: 0 broken. Frontmatter: all 3,456 valid. External spot-check all 200. Deploy shipped 18 pending MCP server pages from Aug 24-25 sweeps (previously 404 on production) — all verified HTTP 200. PROGRESS.md stats refreshed (1,958 MD, 503 MCP servers, 585 hermes/mcp .md). Pushed to main (1c8931a0), deployed to Vercel, changed pages verified HTTP 200.
- **Skills sweep ✅ (Aug 24, 2026, evening):** 48-query skills.sh API sweep (686 unique skills, 0 failures), plus hot-leaderboard and watchlist re-verification. API surface fully known at 2K threshold. New find: `coreyhaines31/makerskills` (23 skills, 4.7K publisher installs vs 480 API sum, 681⭐, active same day) — cohesive personal-operator suite (second-brain, company-brain, deep-research, decide, CFO skills) with zero tree hits. Added cluster setup guide `makerskills-setup.md` + catalog index entry (498 setup guides; catches up 4 uncounted Aug 24 morning guides). Parked below bar: serkan-ozal/browser-devtools-skills (496), secondsky/claude-skills (359, claude-skills repo, rejected), davidlee/doctrine spec-tech (89, watchlist). Mac Mini offline; sweep ran from Spark clone.
- **Maintenance ✅ (Aug 24, 2026):** Normalized 3 root-level connector-count stragglers (37+ → 40+: connectors.md, chatgpt-integration.md, changelog.md; served docs/ copies already at 40+). Stale dates: 0 files. Internal links: 0 broken. Frontmatter: all valid. PII scan clean. Genericized 3 historical identifiers in PROGRESS.md sanitization notes. External spot-check all 200. Pushed to main (b851fe9a), deployed to Vercel, changed pages verified HTTP 200.
- **Maintenance ✅ (Aug 23, 2026):** Refreshed 100 stale `last_updated` dates in docs/ (SEO pages + API + security + comparison pages stuck on 2026-08-06 through 2026-08-15). Refreshed docs/hermes-sitemap.xml (193 URLs) + docs/sitemap-index.xml lastmod → 2026-08-23. Internal links: 0 broken (1 false positive: `[text](url)` inside a Slack mrkdwn code example). Connector count: all pages consistent at 40+. PII scan clean. PROGRESS.md stats refreshed (1,903 MD, 536 MCP servers). Pushed to main, deployed, changed pages verified HTTP 200.
- **Skills sweep ✅ (Aug 21, 2026, evening):** 15-query skills.sh sweep (607 unique skills). 94 NEW flags all below the 100-install bar (max 89) — parked. Verified rejections: `skill-composer-studio` (onewave-ai/claude-skills, 259 — Claude Code only), `mercury-ui-skills` (ihlamury/design-skills, 195 — Claude/Cursor/Copilot), `azure-chaos-studio` + `azure-lab-services` (microsoftdocs/agent-skills, 115/108 — Azure platform), `pp-mercury` (mvanhorn/printing-press-library, 123 — OpenClaw banking CLI). High-value gap found: `sickn33/agentic-awesome-skills` (45K⭐, 2,025 skills) — 37 generic engineering playbooks at 100 to 13,215 installs were flagged "covered" on Aug 14 but had zero tree hits. Added cluster setup guide `agentic-awesome-skills-setup.md` + catalog index entry (493 setup guides).
- **Maintenance ✅ (Aug 21, 2026):** Skills sweep found 1 high-value gap: `design-review` (nexu-io/open-design, 2,369 installs, 90K⭐) — added catalog setup guide + index entry (492 setup guides). MCP sweeps current through issue #3679 (309 servers, 195 guides). Internal links: 0 broken. No stale last_updated dates in docs/. Frontmatter validated. Pushed to main, new page verified HTTP 200.
- **Maintenance ✅ (Aug 20, 2026):** Normalized 5 connector-count stragglers (36+ → 40+) across docs/architecture/README.md, odoo-mcp.md (x2), datamcp-mcp, and refreshed stale ecosystem stats (36+ pages → 1,700+, 326+ repos → 450+, 133+ skills → 490+). Refreshed PROGRESS.md stats (1,852 MD files, 491 skills, 488 MCP servers, 126 SEO pages). Internal links: 0 broken. Frontmatter: all valid. Deployed to Vercel, changed pages verified HTTP 200.
- **Maintenance ✅ (Aug 19, 2026):** Refreshed 21 stale `last_updated` dates (18 docs/*.md SEO pages stuck on 2026-06-16 + docs/index.md, hermes/index.md, hermes/README.md). Repointed 19 dead `skills.sh/aradotso/*` links to live GitHub repos (aradotso profile 404s on skills.sh) across 17 catalog/marketplace files. Fixed vibgrate trust link (`/mcp-trust` → `/trust`, was 404). Refreshed hermes-sitemap.xml (193 URLs) + sitemap-index.xml lastmod → 2026-08-19. Internal links: 0 broken. Deployed to Vercel, all changed pages HTTP 200.
- **Maintenance ✅ (Aug 17, 2026):** Fixed 2 broken internal links in skills catalog (chrome-devtools + oh-my-hermes setup guides → /hermes/best-practices/security/). Refreshed all 3 sitemaps (sitemap.xml 323 URLs + hermes-sitemap.xml 193 URLs + sitemap-index.xml) from 2026-08-10/2026-06-17 → 2026-08-17. Refreshed PROGRESS.md stats (1,742 MD files, 473 skills, 423 MCP servers).
- **Stale .html duplicates ✅ (Aug 15, 2026):** Removed 202 stale static .html files in hermes/ (22.8 MB) superseded by .md builds. They were copied into the site output as orphan pages with broken relative links (../../../quick-start.html → 404) and duplicate content. All had .md twins; none referenced in nav, sitemap, or .md content.
- **Sanitization ✅ (Aug 15, 2026):** Removed 5 internal-info instances: internal hostname + sweep ops note (new-aug15-2026 sweep page), personal name (etincel-mcp page), internal inbox handles (busymail-mcp page), demo email value → hello@example.com (chrome-devtools setup), "on an internal worker" sweep note (new-aug12-2026-evening page).
- **Maintenance ✅ (Aug 16, 2026):** 103 user-facing files normalized 37+ → 40+ connectors (zero stragglers). Refreshed 2 stale dates (mcp-vs-data-warehouse, enterprise-ai-data-access). Removed internal outreach tracker (hermes/data/directory_submissions.json) + unreferenced demo asset; restored demo.mp4 (still linked from 2 pages). Sanitized historical PROGRESS.md identifiers. Internal links: 0 broken.
- **Root-level .html legacy files (119, ~12 MB):** Still in repo root but auto-excluded from MkDocs build (404 in production). Dead weight only; candidate for a future dedicated sweep.
- **Connector count consistency ✅ (Aug 10, 2026):** Website updated to "40+ connected business tools." Normalized README.md (6 instances) from 37+ → 40+ to match corpusiq.io. Remaining 37+ instances in older published-content/ and hermes/launch/ files are technically still true (40 > 37) but flagged for next sweep.
- **Screenshots:** Quickstart screenshots pending — low priority, no user complaints.
- **DOC-GAP connectors:** 7 connectors (amazon_seller, gohighlevel, google_workspace, gunbroker, mongodb, postgres, postscript) in the connector registry need verified vendor setup steps — tracked in connector registry, not docs repo.
- **Sitemap dates ✅ (Aug 14, 2026):** Updated hermes-sitemap.xml (193 URLs) + sitemap-index.xml from 2026-06-17 to 2026-08-14.
- **Stale dates ✅ (Aug 14, 2026):** 43 top-level docs/ SEO pages refreshed from 2026-07 → 2026-08-14.
- **Sanitization ✅ (Aug 14, 2026):** Removed invented example private IPs from hermes-plugins-42evey-setup.md (not in upstream repo) → replaced with agent-a.local/agent-b.local. A third-party meshtastic example private IP was verified as upstream content, kept.

---

*Last updated: August 25, 2026. This repo is updated daily via automated crons. Canonical connector count: 40+ per corpusiq.io.*
---
