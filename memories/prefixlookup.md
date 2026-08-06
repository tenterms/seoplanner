# prefixlookup.com — website health check (Aug 2026)

**Client/site:** prefixlookup.com — BCBS alpha-prefix lookup tool for US medical billers. Next.js on Vercel, US-only market. Brand new domain (Ahrefs first sees it ~April 2026).

**Deliverable:** `Prefixlookup-Website-Health-Check.md` (repo root, branch `claude/prefixlookup-health-check-99c7v9`).

## Core verdicts (don't re-litigate)

- **Technically sound**: clean redirect graph (http→308→https, www→301→apex incl. deep URLs, trailing-slash→308, all single-hop), correct self-canonicals on all templates, real 404s, HSTS, fast TTFB, good unique titles/meta. Leave URLs alone.
- **Critical bug**: robots.txt `Sitemap:` points at `bcbsprefixlookup.com` — a **parked third-party junk domain** (DR 0, no legacy value; likely leftover from earlier project naming). One-line fix.
- **Backlink profile is toxic**: 607 links / 417 refdomains, DR 0. Refdomains are link-seller/PBN spam (`buyseobacklinks.shop`, `fiverr-quality-seo-at-affordable-rates.site`, `*.agency` network). Purchased links doing nothing. Site has zero genuine links.
- **Visibility ≈ zero**: 1 organic keyword (`bcbs alpha prefix lookup`, 450/mo US, pos 29, homepage). Indexed fine (site: confirmed, incl. /prefix/ pages; www duplicates in index are lag only).
- **Sitemap gap**: 254 URLs listed (181 /prefix/, 65 /plans/, 2 /blog/, 6 static) but *every* 3-letter /prefix/ combo returns 200 with data (~17.5k pages live). Needs full chunked sitemaps + verify unassigned prefixes 404 (soft-404 risk at scale).
- **Homepage = 4.4 MB HTML** (full prefix DB embedded in one Next.js RSC flight payload; ~275 KB compressed). Should be API-backed search, <100 KB target.
- **No structured data at all** — BreadcrumbList / WebSite+SearchAction / FAQPage are cheap wins.
- **SERP is winnable**: top-10 for "bcbs prefix lookup" is stale 2020-era blog lists (mypayerdirectory, rcmguide, healthquestbilling), raw .xlsx/PDF files, plus official bcbs.com/azblue/bcbstx. A structured lookup tool beats these on merit; missing ingredient is genuine authority (RCM/billing communities, resource pages).

## Follow-up plan
Re-check 6–8 weeks after fixes: GSC index coverage of /prefix/, head-term positions, genuine refdomain growth. Ahrefs spend for this check: ~600 units.
