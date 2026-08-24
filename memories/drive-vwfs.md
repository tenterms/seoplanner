# Project memory: Drive (drive.co.uk), Volkswagen Financial Services UK

**Type:** Prospect research for a TenTerms PR + SEO pitch (not yet a client). Researched 2026-08-24.
**Deliverable:** `Drive_Prospect_Briefing.md` (this repo).

## Who they are
- **Drive** = VWFS UK's consumer car marketplace, launched **w/c 13 Aug 2026**. Consolidation of **heycar UK + BuyaCar + Honest John** into one domain.
- Operator: **Volkswagen Financial Services (UK) Limited**, co. 02835230, Milton Keynes, active. Drive is an **FCA appointed representative**; VWFS UK is named as its "principal firm" on /complaints.
- Legacy entity **Mobility Trader UK Ltd** (heycar UK), co. 12016686, **in liquidation**, accounts overdue since Dec 2025.
- Public voice: **Dan James, Chief Transformation Officer, VWFS UK**. CEO: Mike Todd. No Drive-specific marketing lead findable. **Intermediary risk high.**
- Sister platform: **Purchase Pro** (VWFS wholesale/trade), launched earlier in 2026.

## Business model (from /faq, verified)
Lead-gen + finance origination, NOT a retailer. Does not sell cars online, does not buy cars or take part-ex (refers to **Motorway**), no private listings. Revenue = VWFS finance/lease originations + retailer listing/lead fees + referral. Lead forms carry finance-quote, part-ex and appointment enrichment flags; £99 reservation hold.

## Commercial goals, prioritised (the core verdict, don't re-derive)
1. **VWFS finance & lease originations** — the P&L driver. Homepage merchandises by monthly payment (`?monthly-price__lte=150/200/300`), not price.
2. **Captive retailer channel to reduce Auto Trader dependence** for VW Group + aligned retailers.
3. **Residual value support / remarketing** the returning lease & PCP book (Drive retail + Purchase Pro wholesale = closed loop).
4. **Own the research stage + first-party data** (why they bought/absorbed Honest John editorial; /value-my-car).
5. **Build "Drive" as a brand from zero.**
6. Part-ex/sourcing volume (currently outsourced to Motorway).
NOT goals: direct online sales, private classifieds, and (currently) indexed new-car search.

## Killer findings (all verified live, 2026-08-24)
- **Honest John blanket 301.** EVERY honestjohn.co.uk URL 301s to `https://drive.co.uk/?from=hj` — incl. /real-mpg/, /carbycar/, /askhj/, /forum/, /new-car-deals/, and classics. & kit. subdomains. Only vans. gets a category target. heycar got proper 1:1 mapping; BuyaCar got model→category. **HJ = 152,361 visits/mo, DR 68, 6,286 ref domains, ~$50k/mo traffic value.** Decay not yet in Ahrefs as of 24 Aug — the pitch window.
- **Real MPG does not exist on Drive.** /real-mpg = 404, nothing in sitemap. Trade press said it moved; it hasn't.
- **Schema says the site is heycar.** JSON-LD `brand: "Mobility Trader UK Limited"` (in liquidation), `alternateName: heycar/heycar uk`, `sameAs` = heycar socials, address = heycar's Lacon House, primaryImage = `/img/heycar-logo-square.jpg` (still resolves). /value-my-car meta desc still says "from heycar". German heycar-DE finance strings still in payload.
- **Brand SERP lost.** UK search "drive.co.uk" → Knowledge Panel for **a driving school in Woolhampton**. Positions 2-10 are other Drives incl. Drive Motor Retail (real 34-outlet dealer group). **No LinkedIn company page (404). Instagram @drive.co.uk = 0 posts, 0 followers.**
- **Soft 404s:** `/guides/{anything}` returns HTTP 200, blank `<title> | Drive</title>`, 196 words boilerplate.
- **robots.txt vs sitemap conflict:** `Disallow: /cars/new` blocks 503 new-car URLs that ARE in the sitemap. Also `Disallow: /*?*` yet `?from=buyacar` / `?from=heycar-uk` URLs are indexed and outranking clean URLs.
- **Case-variant duplicates ranking:** `/Cars` is the ranking URL for "audi q7" (41k) and "toyota hilux" (27k). Also `/Guides`, `/Car`.
- **1,754 thin location pages** (`/cars/used/abbots-langley` claims "6,517 cars in Abbots Langley" from a national feed).
- **Leasing = 1 sitemap URL** (`/cars/lease-deals`); `/leasing` has no H1. Huge gap for a leasing company.
- No /about, no newsroom, no retailer page.

## Numbers
- drive.co.uk: DR 59, 1,094 GB keywords, 5,088 visits/mo, ~$1,855/mo value, 1,350 live ref domains (579→1,383 in Aug from launch PR).
- Sitemap 5,075 URLs: 2,669 model (2,166 used + 503 new), 1,754 location, 399 reviews, 135 guides, 110 facets, 7 static, 1 leasing.
- **Near-miss inventory: 248 keywords at vol ≥1,000 sitting at positions 11-30 = 2,793,000 combined monthly searches.** e.g. peugeot 3008 (103k, p25), ford kuga (80k, p21), byd seal (114k, p12), vw tiguan (68k, p16).
- Competitors: autotrader 13.66M/mo DR82; carwow 1.75M DR74; theaa 3.76M; cazoo 889k; parkers 601k; cinch 596k; whatcar 686k; motorpoint 602k.

## Pitch strategy verdict
Outside the normal TenTerms ICP (corporate division of a captive lender, not a £500k-£20m SME). **Do not pitch a generic retainer.** Lead with a dated migration-audit document ("what the Honest John migration is about to cost Drive"), sell a paid migration-recovery + brand-entity sprint scoped in weeks. PR angles that stand alone: brand entity establishment, Honest John goodwill management (visible backlash on PistonHeads / motoring press), and data-led PR off Real MPG + valuation + finance data.

**Artifact URLs:** briefing (presentation cut) https://claude.ai/code/artifact/61004e43-0758-4ddb-bb6e-bba83ef975dd · full text https://claude.ai/code/artifact/d5091795-24b6-457a-a0d8-bebf03879aaf
