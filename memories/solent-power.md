# Project memory: Solent Power (solentpower.co.uk)

**Client:** Generator sales/hire/servicing, Hampshire (Solent). WooCommerce on SiteGround.
**Deliverable:** `Solent-Power-SEO-Fix-List.md` (this repo, 2026-08-13) — developer fix list, not a full keyword universe.
**Baseline (Aug 2026):** ~432 GB keywords, ~1.5–1.8k organic visits/mo, DR-level 647 live refdomains. Traffic drifted down from ~3.1k/mo Aug 2024; sharper June 2026 dip, partially recovered. No penalty signals.

## Site facts
- **SiteGround sgcaptcha blocks all non-browser fetches** (202 + IP-bound JS challenge; egress IP rotation makes it unbeatable from CCR). Google indexes fine; Ahrefs partially blocked (11 pages 202). Use Ahrefs crawled-pages + SERPAPI for structure, not live crawls.
- ~250 known URLs: 79 products (`/product/diesel-generators/…`), 39 kW/kVA size categories under `/generators/`, brand pages in THREE patterns (`/brand/`, `/generators/x-generators/`, `/generator-sales/x-generators/`), `/power-cut-checker/*` info hub, `scorecard.` subdomain.
- **Power-cut-checker hub = 55%+ of all organic traffic** (NIE Northern Ireland page is the site's #1 page). Commercial pages rank well (#1–3 on many kW/kVA terms) but earn little each.

## Validated verdicts (don't re-litigate)
- 404s → 410 OK **except**: `/brand/teksan/`, `/electrical-services`, `/prevent-diesel-generator-failure/` (have backlinks → 301 targets in fix list); `/uninterruptible-power-supply-servi%20es/` typo'd slug — broken href ALREADY FIXED (verified 13 Aug: zero live internal links to it; nav's 499 links target the correct URL), UR 8.1 is residual → just 301 it to `/uninterruptible-power-supply-services/`.
- UPS tree migrated `/ups/*` → `/uninterruptible-power-supplies/*` ~11 Jul 2026; `/ups/configurable-output/` missed the migration (live, "Archives" title); 12 internal links still hit old `/uninterruptible-power-supply/` redirect.
- Soft-404 pattern: old posts 301'd to homepage (`/electronic-repairs`, `/is-using-a-generator-cheaper…`).
- BESS duplicated: `/battery-energy-storage-systems/` + `/battery-energy-storage-solutions-bess/` → keep `-systems`, 301 the other.
- `/ups/*` tree half-consolidated; `/ups/configurable-output/` left live with "Archives" title.
- Cannibalisation confirmed via serp_target_positions_count: "standby generator installation" ×4 URLs, "generator fuel"/"fuel generator" ×5. "30kva generator" product-beats-category; "250kva generator" product ranks #1 — leave it.
- kW vs kVA parallel series: keep both, disambiguate + cross-link (same as generator-retailer precedent).
- Product artifacts: `-copy`/`-copy-2` slugs, HSF-80 titled "65", "kVAGenerator" typo, "¬" in generator-sales title.

## Open items
- User's original 404 report attachment was lost in session resets — fix list covers Ahrefs-known 404s + the blanket 410 rule; cross-check against their report if it resurfaces.
- Sitemap contents unverifiable externally (captcha) — dev asked to confirm no dead/redirected URLs in it.
