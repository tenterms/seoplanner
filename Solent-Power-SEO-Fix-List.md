# Solent Power (solentpower.co.uk) — SEO Fix List for the Developer

*Prepared 13 Aug 2026. Sources: Ahrefs index data (crawl, backlinks, rankings), live Google SERP checks. Baseline: ~430 UK keywords, ~1.5–1.8k organic visits/mo, 647 live referring domains. Site is behind SiteGround bot protection, which blocks third-party fetches — see item 9.*

---

## 1. The 404s in the crawl report — 410 is fine, with these exceptions

Blanket answer: yes, dead URLs with no inbound links can be served as **410 Gone** — it's marginally cleaner than 404 and tells Google removal is deliberate. **But apply these exceptions first:**

### 1a. Do NOT 410 these — 301 them (they have live external backlinks pointing at them)

| Dead URL | Redirect to | Why |
|---|---|---|
| `/brand/teksan/` | `/generator-sales/teksan-generators/` | Teksan still has a live page under `/generator-sales/` — the old brand-archive URL has a dofollow backlink |
| `/electrical-services` | `/generator-service-maintenance/` | Dofollow backlink; nearest live equivalent service page |
| `/prevent-diesel-generator-failure/` | `/how-often-should-generators-be-serviced/` (or the closest live maintenance guide) | Dofollow backlink to the old blog post |

### 1b. Do NOT 410 these — they're symptoms of other bugs (fixes below)

| Dead URL | Real fix |
|---|---|
| `/uninterruptible-power-supply-servi%20es/` | UPS services slug with a **space typo** ("servi es"). Internal-link scan (13 Aug): **no live internal link points at it any more** — the sitewide nav link (499 dofollow) correctly targets `/uninterruptible-power-supply-services/`, so the broken href has already been fixed. Its high URL Rating is residual from when the broken link was live. Remaining action: **301 the typo URL** to `/uninterruptible-power-supply-services/` to reclaim that equity. |
| `/generator-accessories/page/3/` and `/page/4/` | Pagination stubs — the category shrank. Don't 410; make sure nothing (sitemap, internal links) still references trimmed pagination URLs. They can stay 404. |
| `/generators/doosan-generators/` | Decide: if Doosan is still sold, reinstate the page; if dropped, 410 is correct. Don't blanket-redirect a discontinued brand to the homepage. |

### 1c. Everything else in the report

410 away — **and also remove any internal links that still point at them** (that's the part that actually matters to Google; the status code is secondary). After the change, check GSC → Pages → "Not found (404)" in ~4 weeks to confirm the list is shrinking.

---

## 2. Kill the redirects-to-homepage (Google treats them as soft 404s)

At least two old URLs 301 to the homepage:

- `/electronic-repairs` → `/`
- `/is-using-a-generator-cheaper-than-the-electric-company/` → `/`

Redirecting a dead page to the homepage passes nothing — Google classifies it as a soft 404. Either point each at a genuinely relevant page, or let them 410. Please also export the full redirect map and check for other homepage catch-alls.

## 3. Duplicate page: two live Battery Energy Storage pages

- `/battery-energy-storage-systems/` (title: "Battery Energy Storage System | Our Services…")
- `/battery-energy-storage-solutions-bess/` (title: "Battery Energy Storage Solutions (BESS)…")

Same intent, two URLs — this splits the ranking signal for a strategically important term. Keep **one** (the `-systems` URL has the higher authority), merge the content, 301 the other into it.

## 4. Finish the UPS subcategory migration

The UPS subcategory tree moved from `/ups/*` to `/uninterruptible-power-supplies/*` around 11 July 2026 (the new URLs each receive ~277 internal links). Three loose ends:

- Confirm `/ups/rack-mount/`, `/ups/tower/`, `/ups/three-phase/`, `/ups/single-phase/`, `/ups/modular/` each 301 to their new `/uninterruptible-power-supplies/…` equivalent in one hop.
- `/ups/configurable-output/` missed the migration — still **live** with the default archive title "Configurable Output UPS Archives | Solent Power", competing with the new `/uninterruptible-power-supplies/configurable-output/`. 301 it to the new URL.
- 12 internal links still point at the old `/uninterruptible-power-supply/` redirect — update those hrefs to the live destination.

## 5. Product catalogue hygiene (WooCommerce artifacts)

- Duplicated-product leftovers in live slugs: `…hsf-65…-copy/` and `…hsf-80…-copy-2/`. Worse, the 80kVA one has the **wrong title** ("Himoinsa HSF-80 T5 | 65 Diesel Generator" — says 65, is 80). Fix the titles now; don't change the slugs of ranking pages just for cosmetics (URL changes cost more than they gain).
- Typo'd titles: "1000 kVAGenerator - Baudouin…" (missing space), and the `/generator-sales/` category title contains a broken character: "Generator Sales ¬ Diesel Generators for Sale".

## 6. Redirect chain on the http + non-www variant

`http://solentpower.co.uk/` → `https://solentpower.co.uk/` → `https://www.solentpower.co.uk/` (two hops). Make every host/protocol variant 301 **directly** to `https://www.` in one hop. Minor, but free to fix in the server config.

## 7. Brand pages live under three URL patterns

- `/brand/{cat, himoinsa, pramac, solent-power}/` (taxonomy archives)
- `/generators/{baudouin, cummins, perkins, yanmar}-generators/` (curated pages)
- `/generator-sales/{hyundai, teksan}-generators/`

No brand is currently duplicated across patterns (Teksan was, and the leftover is the 404 in item 1a), so **do not move existing URLs** — but pick ONE pattern for all future brand pages, and be aware this inconsistency is how orphaned 404s like Teksan happen. The curated `/generators/x-generators/` pages are the strongest performers; prefer that pattern.

## 8. `scorecard.solentpower.co.uk`

This subdomain is reachable and has been crawled by third-party bots. If it's an internal tool, add `noindex` and/or block it in robots — verify it isn't in Google's index.

## 9. Bot protection (SiteGround sgcaptcha) — verify crawler access

The site serves a captcha challenge (HTTP 202) to non-browser requests. Google's own indexing currently looks healthy, but Ahrefs' crawler is being blocked on a number of pages, which means: (a) SEO tools under-report the site, and (b) if the firewall rules ever tighten, Googlebot could be caught. Ask SiteGround to whitelist verified search-engine and mainstream SEO crawlers, and check GSC → Settings → Crawl stats for any spike in "server connectivity" / challenge responses.

## 10. Sitemap check (couldn't verify externally — captcha)

Please confirm: the XML sitemap contains **only 200-status canonical URLs** — none of the 404/410 URLs from the report, no trimmed pagination, no redirected URLs. Stale sitemaps keep dead URLs in the recrawl queue indefinitely.

---

# Beyond the dev fixes — what's actually holding rankings back

These are for Joe/content rather than the developer, but they came out of the same audit:

**A. Over half the organic traffic is the Power Cut Checker hub, not the shop.** The `/power-cut-checker/*` pages earn ~850+ of ~1,540 monthly visits (NIE Northern Ireland alone is #1 on the site). That's a great asset — but those pages should be working harder as the top of the funnel: add prominent, descriptive-anchor links from every checker page down to `/generator-sales/standby-generators/`, `/generators/residential-generators/` and `/uninterruptible-power-supplies/` ("keep the power on next time — standby generators from £X").

**B. Cannibalisation on the installation cluster.** For "standby generator installation" **four different Solent URLs** appear on one SERP (best is a blog guide at #8, with `/generator-installation/` also competing). Same for "generator fuel" / "fuel generator" — **five URLs** each. One page must own each intent: make `/generator-installation/` the sole commercial target (retitle the guide to the informational phrasing and link it to the service page with exact anchor), and consolidate the fuel content similarly.

**C. Product vs category on size terms.** "30kva generator" ranks via a product page (#7) while the `/generators/30kva/` category sits unused — the category should own the generic size term; the product should target its model ("CPS AP30S"). Conversely "250kva generator" ranks #1 via the Pramac product — leave that one alone (don't break a #1), just make sure the category links to it prominently.

**D. kW vs kVA parallel series.** ~39 near-identical size category pages exist in both units, with almost interchangeable titles. They genuinely differ (searchers use both), so keep both — but disambiguate titles/intros and cross-link each kW page to its kVA twin (100kW ↔ 125kVA etc.) so Google doesn't pick one arbitrarily.

**E. Titles don't merchandise.** Category titles are the bare pattern "150kVA Diesel Generators For Sale in the UK | Solent Power". Add the things a buyer chooses on: price-from, UK stock, delivery, brands held ("150kVA Diesel Generators | UK Stock, From £X | CAT, Himoinsa, Pramac"). This is the cheapest CTR win on pages already ranking 2–7.

**F. Traffic trend context.** Organic traffic has drifted from ~3.1k/mo (Aug 2024) to ~1.5–1.8k now, with a sharper dip in June 2026 that's partially recovered. Nothing in the technical picture suggests a penalty — the pattern reads as gradual erosion plus algorithm-update turbulence. The fixes above (plus consolidation) are the right response; avoid any URL restructuring while it re-stabilises.

---

*Rule of thumb for all of the above: fix titles, links, content and status codes freely — but do not rename or move URLs that currently rank. Every URL change resets Google's evaluation of that page.*
