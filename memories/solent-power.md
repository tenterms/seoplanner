# Project memory: Solent Power (solentpower.co.uk)

**Client:** Solent Power, Rowlands Castle, Hampshire (£2–2.5m rev → £3m target). Power continuity specialist: large generators (800kVA+ = best-fit deal signal), servicing/maintenance retainers (£3k/mo), UPS (new push), HTM 06-01 healthcare compliance. Buyers: M&E, electrical consultants, FM, site teams at hospitals, data centres, universities, pharma/manufacturing. South England focus, whole-UK for big projects. 2–3 SQL/week.
**Deliverable:** `Solent-Power-SEO-Plan-Content-Research.xlsx` (this repo, 2026-07-29). 155 GB keywords + 40 US sample, 11 clusters, 523-URL per-page checklist.

## Site facts
- WordPress/Woo on SiteGround. **SiteGround sgcaptcha bot wall challenges ALL scripted GETs (even Chromium via the agent proxy failed with ERR_CONNECTION_RESET)** — crawl via Ahrefs crawled-pages + GSC Pages + Wayback CDX instead; HEAD sometimes works. Spot-check live HTML from an office machine.
- ~523 clean non-powercut URLs: 291 products, 95 articles, 19 kVA + 21 kW size pages, 23 categories, brand pages under **3 patterns** (/brand/ taxonomy, /brands/, /generator-sales/{x}-generators/), 9 locations, UPS under **2 patterns** (/ups/*, /uninterruptible-power-supplies/*) + blog.
- **Power-cut checker = ~90% of clicks** (11.7k vs 1.1k commercial per 90d GSC). Verdict: protect + leverage (regional pages link to /emergency-generator-hire/ + sectors); never in the commercial keyword plan. It's the authority/AI-association engine.
- staging2 subdomain live but noindexed (x-robots) — recommend password. Filter-param URLs crawlable but not indexed (SERPAPI verified). No penalty signature; Ahrefs traffic is a plateau at ~1.5–2.5k/mo since 2024.

## The diagnosis (client's hypothesis CONFIRMED, with precision)
Nearly every commercial term in the niche is **KD 0–3** — the problem is structural, not competitive:
- **Servicing (the money cluster): 60,559 impressions / 27 clicks / pos 27–44** — intent split across /generator-service-maintenance/, how-often blog (wins 'servicing and maintenance' pos 1), /knowledge-base/ (wins 'diesel generator maintenance'), /locations/surrey/ (wins 'generator service'), /hampshire-generators/ (wins 'repair near me').
- **UPS: 6,489 impr / 3 clicks**, best URL is a blog at pos 26–40; modular ups has 469 impr pos 22 with NO page.
- Products outrank their own size categories (30/45/60/80/250/300kVA — validated by serp-overview: size *category* pages win those SERPs).
- 39 of top 250 organic keywords have ≥2 Solent URLs ranking (Ahrefs serp_target_positions_count).

## Validated verdicts (don't re-litigate)
- **service = servicing = maintenance = contracts = company → ONE page** (/generator-service-maintenance/); combined service-page type wins the SERP (Yorpower, P&I, Pleavin).
- **Repair is a SEPARATE intent** (breakdown-now, TP 200) → NEW /generator-repair/.
- **kVA vs kW → FULL MERGE, client-agreed (rev 2026-07-29):** one kVA-only series; every kW page 301s to the kVA page ≥ its converted rating (**kW ÷ 0.8, rounded UP — 200kW→250kVA, 100kW→150kVA; NEVER same-number**, 200kVA=160kW). kW equivalent goes into the kVA title + an H2 conversion note BEFORE redirects fire. Defensibility evidence: their own Pramac GSW250P "200kW 250kVA" product ranks in both families from one URL. Known trade: kW series = 266 clicks/90d (60% from sub-ICP 10–20kW), expect dip + recovery at KD 0. (Earlier SERP check showed twins *could* coexist at ≥50kW — merge chosen anyway for structural simplicity; don't reopen.)
- **Small-size pruning = OPEN CLIENT DECISION:** proposed floor 50kVA. Sub-50kVA estate (10/20/25/30/40kVA categories + 10–30kW feeders + ~68 products) earns ~600 clicks/90d — over half of commercial clicks, none of it ICP. Prune = 301 into /diesel-generators/, visible traffic drop, positioning gain. Softer option: keep live, demote from nav/link spine. Client must confirm the smallest unit they'll sell/service before the batch ships.
- **Bare 'ups power supply'/'uninterruptible power supply' = retail SERP** (RS/Amazon/Currys) → don't fight. **'industrial ups' = manufacturer-spec SERP** (Socomec — a stocked brand — ranks) → winnable with spec pages.
- **Bare 'generator hire' (2,200) = HSS/Speedy-owned** → don't fight; win emergency (£9 CPC!), kVA-qualified, industrial, Hampshire/Southampton/Portsmouth.
- **'emergency generator hire' SERP = dedicated service pages** → NEW page justified.
- **'800 kva generator' SERP stale/weak** → open for ICP ladder; ADD kVA pages: 70, 90, 110, 350, 900, 1250, 1500, 2000, 2500 (600/700/800 already exist).
- 'commercial generator' → industrial-generators page owns industrial+commercial (already ranks pos 3 for it); hospital page retargets healthcare only.
- HTM 06-01: 150/mo, £4.50 CPC, KD 0 → guide + /sectors/healthcare/. Fuel polishing: 300/mo KD 0, no page → fuel-services child.
- Info assets that are the link engine: transfer-switch install guide (10k impr pos 9), oil guide (25k impr), sizing guide (merge the duplicate), kVA-vs-kW chart (pos 34, rebuild).

## Priorities shipped in plan
P1: servicing-page rebuild + intent consolidation · homepage repositioning (continuity specialist, not 'Generator Sales') · installation retarget. P2: UPS spine build-out (hub + industrial/modular/phase spec pages + maintenance/installation/battery services) · /emergency-generator-hire/ · location-page retarget. P3: kVA cleanup (categories own sizes, products→model terms, twin folds, ICP size additions) · info link engine. P4: brand consolidation to /brands/ · sector pages · checker leverage links. Golden rule throughout: consolidations = one clean 301, then freeze the graph a quarter; measure via GSC at wk 6–8 (success = one URL per cluster, servicing CTR >1%).

Related: [[southern-ropes]] (same playbook; generator-retailer signal-splitting pattern echoed here).
