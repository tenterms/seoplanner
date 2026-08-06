# prefixlookup.com — Full Website Health Check

**Date:** 6 August 2026
**Scope:** Technical SEO forensics (redirects, canonicals, robots, sitemap, indexation), authority & backlink profile (Ahrefs), live SERP/indexation checks (Google via SERPAPI), page-template audit.
**Site:** BCBS alpha-prefix lookup tool for US medical billers. Next.js on Vercel. US market.

---

## Verdict in one paragraph

The site is **technically well-built but organically invisible, and two things are actively hurting it**: the robots.txt sitemap directive points at a parked domain the site doesn't control, and the backlink profile is ~100% purchased/spam links (DR 0 despite 417 referring domains). The underlying engineering is sound — clean redirect graph, correct canonicals, proper 404s, fast responses — and the competitive SERP is weak (stale 2020-era blog lists), so this is recoverable. The domain is ~4 months old with essentially zero genuine authority; the priority is to fix the two self-inflicted wounds, get the full page inventory into sitemaps, and start earning real links.

---

## Scorecard

| Area | Status |
|---|---|
| HTTPS / redirect graph | ✅ Healthy |
| Canonicals & indexation controls | ✅ Healthy |
| 404 handling | ✅ Healthy (assigned-vs-unassigned prefix behaviour to verify) |
| robots.txt | 🔴 **Critical bug** — sitemap points at a parked third-party domain |
| XML sitemap coverage | 🟠 Major gap — 181 of ~17k+ live prefix pages listed |
| Page templates (titles/meta/H1) | ✅ Healthy |
| Structured data | 🟠 Missing entirely |
| Page weight / rendering | 🟠 Homepage HTML is 4.4 MB (full database embedded) |
| Backlink profile | 🔴 **Toxic** — spam/purchased links, DR 0 |
| Organic visibility | 🔴 1 ranking keyword, 0 estimated traffic |
| Competitive opportunity | ✅ Genuinely winnable SERP |

---

## Critical issues

### 1. robots.txt sends Google's sitemap discovery to a parked domain you don't control

`https://prefixlookup.com/robots.txt` currently reads:

```
User-Agent: *
Allow: /

Sitemap: https://bcbsprefixlookup.com/sitemap.xml
```

`bcbsprefixlookup.com` is a **parked junk domain** (its robots.txt disallows parking-page scripts like `/cpx.php`; its homepage title is just the domain name; Ahrefs shows DR 0, rank ~271M, no legacy authority). The site's real sitemap at `https://prefixlookup.com/sitemap.xml` works fine (200, valid XML) but is never referenced.

**Fix (one line):** change the directive to `Sitemap: https://prefixlookup.com/sitemap.xml`, and submit the sitemap directly in Google Search Console as well. This looks like a leftover from an earlier naming/branding of the project.

### 2. The backlink profile is almost entirely spam / purchased links — and it isn't working

Ahrefs: **607 live backlinks from 417 referring domains, yet Domain Rating = 0** (Ahrefs rank ~99.5M). The top "referring domains" by DR tell the story:

- `fiverr-quality-seo-at-affordable-rates.site` (DR 68)
- `seogrow.agency`, `rankgrowth.agency`, `seonix.agency`, `rankio.agency`
- `buyseobacklinks.shop`, `pbnseolinks.shop`, `authoritybacklinks.shop`, `linkrankpro.shop`, `rankxlinks.shop`, …

These are link-seller / PBN network domains with artificially inflated DR. Whether these were bought (e.g. a Fiverr gig) or are spam-network noise, they contribute **zero authority** — DR 0 with 417 refdomains is the proof — and a profile that is 100% this pattern is a risk with no upside.

**Fix:** stop any paid link acquisition immediately. A disavow file is optional (Google claims to ignore these, and the site has no manual action visible from outside — check GSC's Manual Actions report to confirm), but the real fix is that the site currently has **no genuine links at all**. Realistic targets for real links in this niche: medical-billing and RCM communities (r/CodingandBilling, AAPC forums), billing-software resource pages, RCM company blogs (the current SERP leaders — rcmguide.com, mypayerdirectory.com — got their rankings this way), and "free tool" roundups for practice managers.

### 3. Organic visibility is effectively zero — but the target SERP is weak

- Ahrefs: **1 ranking keyword** — `bcbs alpha prefix lookup` (450/mo US), homepage at **position 29**. Estimated organic traffic: 0.
- Traffic history: the domain first registers in Ahrefs around **April 2026** — this is a brand-new site, not a site that lost rankings. Nothing was "broken"; it simply hasn't earned anything yet.
- Google **has** indexed the site (confirmed live via `site:prefixlookup.com`), including `/prefix/{code}` pages, and is already surfacing them for the exact query pattern the site is built for.

The live top-10 for "bcbs prefix lookup": mypayerdirectory.com (a 2020 blog post), bcbs.com (official), healthquestbilling.com, a CareCentrix .xlsx file, bcbstx.com, rcmguide.com (2021), azblue.com, a Premera PDF, smartrcmsolutions.com. Apart from the official BCBS properties, **the competition is stale blog-format lists and literal spreadsheets/PDFs** — a fast, structured lookup tool with per-prefix pages is a better result. This is winnable with authority.

---

## Major issues

### 4. The sitemap lists 181 prefix pages; thousands more are live

Sitemap inventory (254 URLs total): 181 `/prefix/` pages, 65 `/plans/` pages, 2 `/blog/`, 6 static (home, about, contact, pricing, privacy, 1 guide).

But the site serves a live page for apparently **every** three-letter prefix — spot-checked `/prefix/aaa`, `/prefix/zzz`, `/prefix/qqq`, `/prefix/ubz`, all 200 with real plan data. That's an inventory of up to ~17,500 pages, of which the sitemap exposes ~1%. Google is finding some prefix pages anyway (they appear in `site:` results, including ones like UBZ that may or may not be in the sitemap), but discovery is being left to internal links and luck.

**Fix:** generate a sitemap index with chunked sitemaps (≤50k URLs each, so 1–2 chunks) covering **every prefix page with real data**. These pages are the long-tail money — every "bcbs prefix XYZ" search is a biller with a claim in hand.

**Also verify:** whether *unassigned* prefix combinations render a 200 page with placeholder/guessed data. Every combination tested returned 200 with plan data; if genuinely unassigned codes also return 200, those should 404 (or noindex) to avoid a soft-404 / low-quality-bulk problem at 17k-page scale.

### 5. Homepage HTML is 4.4 MB — the entire database is embedded in the page

The homepage delivers **4,370,235 bytes of HTML** (~275 KB compressed on the wire, which hides the problem). The bulk is a single Next.js RSC flight payload (`self.__next_f.push(...)`) containing what appears to be the full prefix dataset. Consequences:

- Every crawl of the homepage costs Google a 4.4 MB parse; Googlebot's HTML processing has practical size limits and this wastes them.
- Real users on mid-range mobiles pay the hydration cost in main-thread time (INP risk) even though TTFB is fast.
- It re-fragments crawl efficiency across the whole site since the homepage is the most-crawled URL.

**Fix:** serve the search box backed by an API/server action instead of shipping the dataset inline. The prefix data already lives on the individual `/prefix/` pages where it belongs. Target: homepage HTML under ~100 KB uncompressed.

### 6. No structured data anywhere

No JSON-LD on the homepage, plan pages, or prefix pages. Cheap wins for a data site:

- `BreadcrumbList` (breadcrumbs already exist visually on prefix pages: Home › Plan › Prefix).
- `Organization` + `WebSite` (with `SearchAction` for the lookup box) on the homepage.
- `FAQPage` on the guide/informational pages (e.g. timely-filing-limits guide).
- Consider `Dataset` markup for the prefix directory.

---

## What's healthy (verified — leave alone)

- **Redirect graph is clean**: `http://` → 308 → `https://`; `www` → 301 → apex (verified on deep URLs too, e.g. `/prefix/anb`); trailing slash → 308 → non-slash. Single hops, no chains. HSTS enabled.
- **Canonicals are correct and self-referencing** on every template checked (home, plans, prefix), all pointing at the apex non-slash URL. The handful of `www.` URLs currently in Google's index are lag, not a config fault — canonicals will consolidate them; no action needed beyond time.
- **404 handling is real**: garbage paths and fake plan slugs return proper 404s (no soft-404 pattern at the routing level).
- **Templates are well-formed**: descriptive unique titles (`UBZ BCBS Prefix | Anthem Blue Cross and Blue Shield of Indiana (Indiana) | BCBS Prefix Lookup`), meta descriptions with the billing specifics (payer ID, phone), single H1, sensible breadcrumb trail. Prefix pages carry ~500 words of genuinely structured, useful data (provider phone, payer ID, claims address, timely filing) — thin by wordcount but legitimately data-complete, which is correct for this page type.
- **Performance at the transport level**: fast TTFB (0.3–0.6s), compression on, Vercel CDN caching. Plan pages ~30 KB, prefix pages ~6 KB compressed. Only the homepage is the outlier (issue 5).
- **No hreflang complexity** (single-market US site) and no locale-variant mess.
- **The core query is already within reach**: position 29 for the head term on a 4-month-old, DR 0 domain, with already-indexed long-tail pages, is actually a promising baseline.

---

## Priority action list

| # | Action | Effort | Impact |
|---|---|---|---|
| 1 | Fix robots.txt sitemap line to `https://prefixlookup.com/sitemap.xml`; submit in GSC | 5 min | High |
| 2 | ~~Expand sitemap to all real prefix pages~~ **Superseded — see Addendum.** Sitemap should contain only *verified-data* pages | Small | High |
| 3 | Stop buying links; check GSC Manual Actions; optionally disavow the spam networks | Small | Risk removal |
| 4 | Start earning genuine links (RCM/billing communities, resource pages, tool roundups) | Ongoing | **The** ranking lever |
| 5 | Strip the embedded dataset from the homepage HTML (API-backed search) | Medium | Medium-High |
| 6 | Verify unassigned prefixes 404/noindex rather than rendering data | Small | Medium |
| 7 | Add JSON-LD (BreadcrumbList, WebSite+SearchAction, Organization, FAQPage) | Small | Medium |
| 8 | Keep URLs exactly as they are — no slug changes, no restructures | — | Protective |

**Measurement:** re-check in 6–8 weeks — GSC index coverage of `/prefix/` pages, position for "bcbs alpha prefix lookup" / "bcbs prefix lookup", and referring-domain growth (genuine domains only).

---

## Addendum — root-cause diagnosis (added after owner context)

Owner context received after the initial audit: the spam links were **not** purchased (only one deliberate link, from successknocks — the rest is automated spam); Google indexed ~22,000 pages at launch and has since **algorithmically deindexed the site to roughly the homepage** (no manual actions); the site performs well on Bing (~5.6k visits via Bing/Teams shares); launch-era programmatic pages were near-identical and have since been improved.

Additional verification (2026-08-06):

- `site:prefixlookup.com` (100 results requested) returns **7 URLs** — the homepage plus 6 `/prefix/` stragglers. The mass-deindexing is confirmed.
- **Every three-letter combination returns a confident, fully-detailed assignment**: `/prefix/zzz` → "Anthem Blue Cross (California), phone (855) 871-4899"; `/prefix/jjj` → Anthem Ohio; `/prefix/xqz` → Wellmark SD/Iowa; `/prefix/qqq` → BCBS Minnesota, payer ID CBMN1. (`/prefix/xxx` is special-cased to a generic page — still HTTP 200.) No public source has verified assignments for all 17,576 combinations; the generator is assigning a plan to everything.
- The current live sitemap still contains **181 `/prefix/` URLs** — the intended removal of programmatic pages from the sitemap has not (fully) shipped.

**Diagnosis:** this is a site-level algorithmic quality suppression, not a mystery penalty. The launch pattern — a days-old, zero-authority domain publishing ~22k near-identical programmatic pages of **YMYL data** (payer phone numbers, payer IDs, claims mailing addresses that billers act on), with no cited sources, no verifiable entity behind the site, and confident answers for combinations that cannot all be verified — matches Google's scaled-content-abuse / auto-generated-content classification exactly. That classification is enforced algorithmically (no manual action appears), applies **site-wide** (which is why even the homepage barely ranks and why a new blog will inherit the suppression), and post-dating improvements to page uniqueness doesn't clear it — the fabricated-coverage footprint is still live. Bing runs no equivalent site-level suppression, and much of the Bing/Teams traffic is genuinely earned distribution — evidence the tool is useful; Google's objection is trust/provenance, not usefulness.

The automated link spam (link-seller networks scraping and blasting new domains to advertise their services) is almost certainly incidental noise, not the cause — but with zero genuine links, the profile is 100% spam, so there is no counterweight.

**Revised recovery plan (supersedes actions 2 and 6 above):**

1. **Split the inventory into "verified" and "unverifiable" and stop publishing the latter as fact.** Keep prefix pages only where the assignment is genuinely sourced; give them per-row provenance ("source / last verified" dates). For everything else, serve an honest "no verified assignment for XYZ — here's how to identify the plan from the member ID card / BlueCard routing" page (noindexed) or a 404. This is the single change that matters; nothing else works while ~17k confident-but-unverifiable YMYL pages remain live.
2. **Prune to a defensible core**: verified prefixes + the 65 plan pages + guides + blog. A smaller site Google can trust beats a complete-looking one it can't.
3. **Add entity and provenance signals**: named who-runs-this, methodology/data-sources page, last-verified dates, real contact details.
4. **Confirm the diagnosis in GSC**: the Page indexing report buckets tell the story — "Crawled – currently not indexed" at scale = quality assessment; "Duplicate, Google chose different canonical" = template collapse; "Soft 404" = the everything-resolves-200 pattern. URL-inspect a handful of improved pages and check the Google-selected canonical.
5. **Convert the real users into links**: the billing companies sharing the tool on Teams are the genuine-link source most sites never have. Ask.
6. **Expect months, not weeks**: site-level reassessment after cleanup typically needs sustained crawling of the cleaned state and often a core-update cycle. Keep URLs frozen throughout; Bing traffic continues meanwhile.

---

## Data appendix

**Ahrefs (2026-08-06, mode=subdomains):**
- Domain Rating 0.0, Ahrefs rank 99,506,069
- Backlinks: 607 live (621 all-time) from 417 live referring domains (429 all-time)
- Organic keywords: 1 (`bcbs alpha prefix lookup`, US, 450/mo, position 29, URL = homepage)
- Organic traffic estimate: 0/mo; history shows the domain appearing ~April 2026
- `bcbsprefixlookup.com` (robots.txt target): DR 0.0, rank 271,040,756 — parked

**Live checks (2026-08-06):**
- `site:prefixlookup.com` — indexed; both apex and (lagging) www deep URLs present
- Top-10 for "bcbs prefix lookup": mypayerdirectory.com, bcbs.com, healthquestbilling.com, carecentrix .xlsx, bcbstx.com, rcmguide.com, azblue.com, premera PDF, smartrcmsolutions.com
- Sitemap: 254 URLs (181 prefix / 65 plans / 2 blog / 6 static), valid XML
- Homepage: 200, HTML 4,370,235 bytes raw / ~275 KB compressed
- Redirects: http→https 308, www→apex 301 (incl. deep paths), trailing-slash 308; all single-hop
- 404s: correct on unknown paths; all tested 3-letter `/prefix/` combos return 200 with data
