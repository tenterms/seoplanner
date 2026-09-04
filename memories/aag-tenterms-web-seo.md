# Project memory: AAG IT Services × TenTerms – web design / website management / SEO pages (aag-it.com)

**Client:** AAG IT Services (aag-it.com), Chesterfield/Sheffield MSP, long-standing TenTerms SEO client (DR 74, ~3.9k organic visits/mo GB, 211 keywords; #1 "outsourced it support", #1 "it support for law firms", #3 "it support sheffield", #2 "it support chesterfield"). Partnership: AAG will resell TenTerms web design, website management (hosting + updates) and SEO (incl. AI SEO) via new pages on aag-it.com.
**Deliverable:** `AAG-TenTerms-Web-SEO-Keyword-Universe.xlsx` (this repo, 2026-09-04). 1142 cleaned GB keywords (P1 106 · P2 ~310 · P3 ~200 · Reference ~90 · Don't-fight ~400), 10 tabs (Read Me · Recommendations · Page Naming Spec · Keyword Universe · Clusters · SERP Validation · Location Matrix · Sector Matrix · Competitors · Page Plan & Linking).

## Site facts
- URL patterns: `/it-support-{city}/` (24 locations incl. Sheffield, Chesterfield, Derby, Doncaster, Mansfield, Barnsley, Wakefield, Huddersfield, Leeds, Nottingham, Hull, York, Bradford, Lincoln, Grimsby, Loughborough, Stoke, Burton, London, Mayfair, Manchester, Birmingham, Leicester), sub-service pages `/it-support-{city}/cyber-security-services-{city}/`, `/services/{service}/`, `/sectors/{sector}/` (law firms, solicitors, barristers, accountants, charities, financial services, hedge funds, hospitality, logistics, manufacturing, business/small business).
- AAG ranks for zero SEO/web-design terms today → no cannibalisation risk; GBP is an IT category (won't enter SEO local packs).
- tenterms.com: DR low, services = AI Search Optimisation ("AI SEO Agency"), Homepage Plus, Link Magnets, Website Quick Wins, Website Strategy, SEO Agency Southampton.

## Validated verdicts (don't re-litigate)
- **Sheffield SEO = ONE page** (`/seo-sheffield/`, H1 "SEO Agency in Sheffield"): agency/bare/company/services variants share top-10 URLs (calmdigital, jdrgroup, wildcat, seoworks, nettl, clutch). Cluster ≈5.5k/mo, KD 0–2, DR-14 site ranks #7–9.
- **Chesterfield SEO = separate page** (`/seo-chesterfield/`, H1 "Chesterfield SEO Company"); "company" is the winning modifier in towns, "agency" in cities. Derbyshire folded in (shared seo-copilot/peakdistrictseo). uclimb DR 8 at #2.
- **Web design Sheffield = ONE page** for web design / website design / web development / agency variants (6+ shared URLs). KD 34, portfolio-led SERP – slowest of the P1 set. `/web-design-sheffield/`.
- **Web design Chesterfield** `/web-design-chesterfield/` KD 4; Derbyshire folded in; Derby city is its own SERP (P2).
- **Website management = national page** `/services/website-management/` ("website management services" 700 KD 0, "website management" 800 KD 2). **Maintenance is a separate intent** (1 shared URL) and bigger (~5k/mo) → P2 page `/services/website-maintenance/`.
- **AI SEO**: agency + services = one page (found, mrs.digital, sinedigital shared); GEO/AEO = distinct SERP → section first. ~7.5k/mo, KD 3–5, DR-25 at #2. P2 national page; must agree term ownership with tenterms.com/service/ai-search-optimisation/.
- **Sectors worth pages (P2):** SEO for Law Firms & Solicitors (~5k, KD 0–16, conscious.co.uk DR 55), Charity Website Design (KD 4–9), SEO for Accountants (KD 1–2), Small Business Website Design/SEO. P3: financial services, manufacturing (guide-led SERP), hospitality. **Not:** SEO for IT companies (conflict), logistics (50/mo).
- **Don't fight:** London/Manchester/Birmingham/Leicester SEO & web design; national generic "seo agency/services", "web design agency"; "web design yorkshire" (TP 10, directory SERP).
- Local-page naming rule from data: cities → "SEO Agency [City]"; towns → "[Town] SEO Company"/"SEO [Town]". Web design local pages only where KD < 35.

## Environment notes
- Ahrefs Keywords Explorer `difficulty` and `parent_topic` select columns returned "internal server error" all session (matching-terms + overview); KD sourced from Site Explorer competitor pulls instead. Both aag-it.com and tenterms.com are behind a SiteGround captcha (WebFetch/curl/headless all blocked); web.archive.org blocked by egress policy. LibreOffice recalc hangs in this sandbox → workbook uses build-time values, not formulas.
- ~45k Ahrefs units used.

Related: [[southern-ropes]] (same playbook).
