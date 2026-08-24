# Project memory: Idea Reality (ideareality.design)

**Client:** Idea Reality — product design consultancy, Hampshire (Southampton area). Historically served solo inventors; repositioning to B2B.
**New target (2026-08):** UK consumer product brands, existing product range, 10–250 staff, no large internal industrial design/NPD department.
**Deliverable:** `IdeaReality-B2B-Content-Strategy-Site-Review.xlsx` (this repo, 2026-08-24). 12 tabs, 79 GB keywords + 30 US sample.
**Related:** the "product design consultancy head-term collapse" in the CLAUDE.md pattern library is this client.

## Site facts
- 236 sitemap URLs. ~95 of them are a full Spanish `/es/` mirror (incl. the inventor blog and Shark Tank/Dragons Den tools).
- **hreflang is CORRECTLY implemented** here — reciprocal en/es/x-default, self-referencing canonical on /es/. Unusual; do not re-diagnose it as broken. It's a commercial decision (noindex or commit), not a technical fault.
- Homepage redirects clean: http, www → https non-www, single 301s.
- **`/services/product-design/` still 301s to the homepage** (verified 2026-08-24, unfixed). Its five children are live and in the sitemap. This is the dead head-term URL.
- `/services/` is a raw WP archive: title "Services Archive - Idea Reality", H1 "Services".
- Homepage H1 and hero are already half-B2B ("helps businesses and start ups"); the **meta description is inventor-coded** ("take your idea out of the paper").
- Only 11 GB keywords ≥10/mo. Ranking assets: `/services/prototyping/` **#1 for "prototyping services" (300/mo)**, `/services/product-design/cad-product-design/` #3 for "cad product design" (200/mo), `/tools/product-design-process/` #8, `/tools/get-your-product-on-dragons-den/` #9, `/blog/pet-product-safety-regulations-in-the-uk/` #5.
- Organic competitor set = LinkedIn, Companies House, catipilla.com (own client), golfbays, jacksonsart. **Zero product design consultancies** — Google does not classify them in this market.

## Validated verdicts (don't re-litigate)
- **"product design services" = "product design consultancy" = "product design company"** → ONE page. SERP is consultancy root domains + single service pages (4D Products, Duku, LUMA, NPD Studio, D2M, Cambridge DT, Alloy, Therefore, Crux). Both page types win, so reinstating the hub is safe.
- **"industrial design consultancy" (GB) = BRAND SERP** — IDC Ltd (idc.uk.com, DR92) owns 7/10 incl. Companies House + LinkedIn + careers page. KD 0 is an artefact. **Do not build this page.** Use "industrial design services" (150/mo KD1). US verdict is the opposite (clean, KD 0) — per-country validation matters.
- **"consumer product design" → SECTOR pages win** (frog, oxfordproductdesign, acornpd, smallfry, sparkinnovations). Their `/design-sectors/consumer-product-design/` is already the right page type — promote, don't rebuild.
- **NPI is the winnable B2B territory**: whole cluster KD 0–1 (~600/mo). "new product introduction" 200/mo KD0.
- **Biggest informational gap = DFM** (~700/mo cluster, they own none).
- **Easiest single win = "injection moulding tooling"** 150/mo KD 0, commercial intent.

## Traps (hard-won)
- **Bare "npd" = narcissistic personality disorder** (7,800/mo). Always the full phrase "new product development". Plus a 550/mo NPD *jobs* cluster (npd manager/technologist) — that's the job title of the buyer, but searchers want jobs.
- **Bare "npi" = US National Provider Identifier** (1,500/mo), plus NPI pension (Phoenix Life), narcissism inventory, Nottingham Prognostic Index. Only qualified forms are safe.
- **"product design" is being colonised by software/UX** (~1,500/mo of digital/SaaS/MVP variants; Toptal + Parallel rank in the GB "product design services" SERP). Every title must disambiguate: industrial / physical / consumer product.
- **"line extension" = London Underground** (Bakerloo 1,500/mo etc.). Only "product range/line extension" is safe.
- Also strip: web design *for* manufacturers, product design *recruitment*, food/FMCG NPD (~600/mo, different discipline — client decision pending), manufacturing insurance/ERP/OEE, "prototype" → Poppy Playtime.

## Key honesty point
Low-volume, high-value market. Whole UK commercial universe ≈2,500–3,000/mo; **D2M's best UK page earns ~77 visits/mo**. Content here is qualification/credibility/AI-citation, not traffic. Revenue is in ~10 commercial terms.
- **D2M (design2market.co.uk) is the model competitor** — `/academy/` hub; their top page is a "top UK product design companies" listicle. That format is proven here.

## Priorities shipped in plan
P1: reinstate /services/product-design/ · homepage meta rewrite · /services/ title+H1 · pull /tools/ from nav · build /tooling/, /new-product-introduction/, /outsourced-product-development/ · promote consumer sector page · DFM + NPD pillars · cost page · UK companies listicle.
Open client questions: Spanish tree (noindex or commit)? Food & drink NPD in scope? Do inventor enquiries still pay the bills (governs how aggressive the /tools/ demotion can be)?

Related: [[southern-ropes]]
