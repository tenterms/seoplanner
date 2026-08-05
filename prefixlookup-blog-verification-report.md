# PrefixLookup.com blog — competitor & fact verification report

**All checks performed 2026-08-05** (live fetches with browser User-Agent, site sitemaps/metadata,
Ahrefs API, Wayback availability API, primary BCBS sources). Standard applied: a claim passes only
where the supporting page text could be quoted; otherwise it is marked **cannot verify**.

**Scope notes (limitations):**
- The 13 blog post drafts and `bluecard-factcheck.json` were **not present in this repository**, so
  verification ran against the claims as enumerated in the research brief. The corrected tables in
  Part 3 are master tables to be reconciled cell-by-cell against the actual drafts of posts 2, 4 and 10.
- Item 27 (British-spelling sweep across the 13 posts) **could not be performed** without the post text.
- **web.archive.org is blocked from this environment** (egress policy; CDX and snapshot fetches fail;
  the availability API worked intermittently). Where "material change history" depended on Wayback
  content-diffing it is marked cannot verify; in every important case the site's own sitemap/metadata
  provided equivalent or better evidence.

---

## Headline: claims that MUST be fixed before publication

| # | Claim as drafted | Problem | Fix |
|---|---|---|---|
| 1 | "Over 60 independent BCBS companies" | bcbs.com says **33**: "Our 33 BCBS companies serve more than 17 million unionized workers…" | "33 independent, locally operated BCBS companies (per bcbs.com, 2026)" |
| 2 | "Medical Billing Services Starting @ $2.49/claim" (attributed to competitors) | The only real figure is **Xceed's** popup: `Medical Billing Services Starting from 2.49%` — a **percentage of collections**, not a per-claim dollar price. No site checked shows "$2.49" or "/claim". | Quote Xceed's "Starting from 2.49%" exactly, attributed to Xceed only — or drop the line |
| 3 | "Only PrefixLookup returns the product type (PPO/HMO/EPO)" | **Two counter-examples**: Smart RCM's tool returns "Plan:" (Product Del Method — PPO/TRAD/EPO/…) for all 9,049 records; CareCentrix's xlsx has a Product Del Method column for 21,792 rows. (MyPayerDirectory also has a Plan Type column on 3 pages / 62 rows.) | Remove product type from the "only us" list |
| 4 | "Smart RCM Solutions does not show provider phone numbers" | Its instant tool returns **three** phone fields (Main, Pre-Cert, DME) per prefix; page title: "Instantly Find Payer, Plan Type & Phone Number" | Invert this cell |
| 5 | "MyPayerDirectory and Xceed show provider phone numbers" | MPD: phone column on 10 of 26 pages, populated in **101 of 20,213 rows (~0.5%)**. Xceed: **no phones in prefix tables at all** — phones live on a separate 64-row state directory page | "MPD: rarely populated (~0.5% of rows); Xceed: separate state phone page, not per-prefix" |
| 6 | Smart RCM has "partial" instant search | It is a **full client-side instant search with as-you-type autosuggest** (fetches a 4.78 MB JSON of 9,049 records; exact-prefix match). Limits: prefix-only matching, one page only; the 52 static range pages have no search | Call it a real instant lookup, note the limits accurately |
| 7 | "Some of the most commonly used tools haven't been touched since 2022" (plural) | Only **one** of the five fits: MyPayerDirectory. The other four all show 2026 activity | Make it singular and name MPD |
| 8 | "Most of these tools were built as marketing content for billing companies" | **2 of 5**: Xceed (Houston billing co.) and Smart RCM (billing co.). MPD = standalone ad-supported directory (pseudonymous "Payer Goddess"); RCM Guide = one-person info blog (AdSense, sells nothing); CareCentrix = home-care coordination company's provider resource | "Several are billing-company marketing pages" naming Xceed & Smart RCM; don't say "most" |
| 9 | "Filing limits range from 90 to 365 days" | Upper bound is **730 days / 24 months — BCBS of Alabama**: "Claims must be submitted and received by us within 24 months after the service takes place" (bcbsal.org) | "from 90 days (e.g. BCBS MA initial claims) to 24 months (BCBS AL)" |
| 10 | "Some plans route mental health claims to … Magellan" | **Outdated as of 1 Jan 2026**: BCBSTX ("Effective Jan. 1, 2026, BCBSTX rather than Magellan Healthcare will administer behavioral health"), Blue Shield of CA and Independence all ended Magellan administration; Magellan's own site confirms | Past tense for Magellan; keep Carelon (note its role is utilization management for Anthem plans — claims still go via Availity) |
| 11 | "Average hold time: 10-20 minutes" | **No published source exists.** Closest citable: CAQH Index 2024 — a phone inquiry consumes "25 minutes per inquiry" of staff time (not hold time) | Remove, or replace with the CAQH stat + citation |
| 12 | "Appeals and coverage questions often need to go to the home plan directly" (post 5) | BlueCard manuals say the opposite for appeals: "BlueCross BlueShield of South Carolina handles appeals for all claims. We will coordinate the appeal process with the member's Blue Plan, if needed." Highmark: "Provider appeals are handled through Highmark." Coverage/benefit determinations ARE made by the home plan — but reached via the local plan / prefix routers, not "directly" | "Appeals are filed with your local plan, which coordinates with the member's home plan; benefits, medical policy and prior auth are decided by the home plan" |
| 13 | "Each prefix is assigned to exactly one BCBS plan" | BCBS SC manual: "The prefix identifies the Blue Plan **or National Account**." FEP members have "R" + 8 digits, no 3-char prefix; some cards have no prefix; one company holds many prefixes | Soften: "each prefix maps to a single plan or national account for routing" + FEP exception |

---

## Part 1 — the five named competitors

### 1. MyPayerDirectory (mypayerdirectory.com) — checked 2026-08-05

Structure: hub `/bcbs-prefix-list/` (H1 "Insurance Plan Identifier List") → 26 static letter pages,
TablePress tables paginated at 100 rows. 20,213 rows / **18,795 unique prefixes** counted (no number
stated on site). Columns vary by page; all have Prefix + Plan Name.

| Q | Verdict | Evidence |
|---|---|---|
| 1 Plan name | **Yes** | `<th class="column-2">Plan Name</th>`; e.g. `XOF | BCBS of Illinois` |
| 2 State | **No** dedicated field | No State column on any of 26 pages; state only inside plan names |
| 3 Payer ID | **No** | No such column on any page |
| 4 Claims address | **No** | None; `/bcbs-contact-info/` page is phones only |
| 5 Phone | **Rarely** | Phone column on 10/26 pages; populated in 101 of 20,213 rows (~0.5%). E.g. `XCD | Anthem BCBS of Connecticut | 855-854-1438`; XOF's phone cell empty |
| 6 Filing limit | **No** | None |
| 7 Product type | **Marginal** | "Plan Type" column on 3 pages (V/X/Y), 62 rows populated (e.g. "Health Exchange - Pathway Individual (HMO)") |
| 8 Extras | Precert Phone column (T/W/Z pages); Notes column (J page, "HIX - on exchange") |
| 9 Finding a prefix | Static letter pages; DataTables config implies a per-table filter box (inferred from config, not visually confirmed); no instant tool; no download |
| 10 Coverage | ~18,795 unique prefixes (measured); no number stated |
| 11 Mobile | Responsive markup present (viewport meta + responsive.css) |
| 12 Login/payment | None; optional MailChimp signup only |
| 13 Last updated | **No visible date.** Hidden `<time class="date updated" datetime="2020-07-27">` on prefix pages; hub 2020-08-30 |
| 14 Freshness | Footer "2021 © My Payer Directory"; newest posts 2020; WordPress 5.7.15; post sitemap lastmod 2021-03-14; privacy policy touched 2026-04 but is unedited WP boilerplate ("Suggested text: …") |
| 15 Archive/material change | Wayback CDX blocked from env. **Site's own page-sitemap.xml is decisive: every `/bcbs-prefix-list/` page lastmod 2022-03-05 (hub 16:54:50-06:00), contact pages 2022-03-08.** Only /privacy-policy/ modified since (2026-04-20) |
| 16 Data source | None stated |
| 17 Error reporting | **None for prefix pages** — no contact page (404s), no mailto anywhere; blog posts have comment forms |
| 18 Ads | Yes — **Monumetric** (fastly.mmt.delivery script + 3 `$MMT.tags` slots), not AdSense |
| 19 Sells billing services | **No** — zero service/pricing content |
| 20 Ownership | Standalone ad-supported directory; the directory IS the site. Byline pseudonym "Payer Goddess"; domain registered 2009-01-09 (GoDaddy, registrant redacted). Notable: Aug 2021 page "The BCBS Prefix List is no longer available" — "The BCBS Association has requested that the prefix list on this website be immediately removed" — list later reinstated under "Insurance Plan Identifier" labels with the Mar 2022 timestamps |
| 21 $2.49 | **Not found** — zero matches for $2.49 / per claim / /claim |

**Claim verdicts:**
- **"Hasn't been updated since March 2022" — CONFIRMED** for the prefix/contact content (own sitemap:
  2022-03-05/08; visible dates 2020). Caveat if claiming "site untouched": trivial privacy-policy edit
  Apr 2026. Cite the sitemap.
- **"Most well-known" — superlative cannot be verified**, but defensible if reworded: Ahrefs
  (2026-08-05) est. **24,415 monthly organic visits — 5× the next competitor** (RCM Guide 4,685;
  help.carecentrix.com 2,534; Smart RCM 1,494; Xceed 514, mostly India); 711 referring domains; oldest
  site in the niche (2009, prefix posts since 2012); BCBSA itself demanded its list's removal in 2021.
  No forum/third-party "best known" citation found. Recommend: "the highest-traffic and longest-running
  of the third-party prefix sites (Ahrefs, Aug 2026)".

### 2. RCM Guide (rcmguide.com) — checked 2026-08-05

Structure: hub `/bcbs-prefix-list/` → 52 range pages (26 alpha × 676 rows + 26 alphanumeric × 208 rows
≈ 22,984 rows incl. unallocated; no number stated). Table = exactly 3 columns:
`"BCBS Prefix List 2024 - Alpha" | "State Lookup" | "BCBS Company"` (e.g. `LAD | Oregon/Idaho/Utah/Washington | Regence Blue-Cross Blue-Shield`; unassigned rows "Unallocated/Not Assigned").

| Q | Verdict | Evidence |
|---|---|---|
| 1 Plan name | **Partial** — BCBS licensee/company name, not product name |
| 2 State | **Yes** — dedicated "State Lookup" column |
| 3 Payer ID / 4 Address / 6 Filing / 7 Product type | **No** to all — zero matches in tables (payer IDs/TFL exist only as separate articles) |
| 5 Phone | **No** — blog's claim RCM Guide lacks phones is **correct**; phones are separate articles |
| 8 Extras | Enumerates unallocated prefixes; FEP "R + number" note |
| 9 Finding a prefix | Static range pages; TablePress/DataTables per-page filter box, 100 rows/page; no global lookup; no download |
| 11 Mobile | Responsive + AMP variant |
| 12 Login/payment | None |
| 13 Last updated | **No visible date** (visible byline "February 24, 2021"). Hidden `article:modified_time` = **2026-01-24** on the range pages (three pages sampled, all 2026-01-24) → "January 2026" is defensible **as metadata**, not as an on-page statement. Hub's modified stamp = 2026-08-05 |
| 14 Freshness contradictions | Titles say "2026" but table headers still say "**2024**"; footer © 2026; newest blog posts July 2024 |
| 15 Archive | CDX blocked; availability API: archived, closest hub snapshot 2026-04-18. Material-change history cannot verify |
| 16 Data source | None stated |
| 17 Error reporting | Contact form **broken** (renders literal `[wpforms id="84"]`); email admin@rcmguide.com |
| 18 Ads | Heavy AdSense (ca-pub-3631846639440701; 25 units on one prefix page) |
| 19/20 | **Not a billing company** — one-person WordPress info blog ("Channagangaiah, Founder", started Aug 2019; "the information we provide … is free to use"); prefix list is its flagship content |
| 21 $2.49 | **Not found** (zero matches) |

### 3. Smart RCM Solutions (smartrcmsolutions.com) — checked 2026-08-05

**Two separate systems**: (A) instant JS tool at `/bcbs-prefix-lookup-tool/` searching
`/bcbs-data.json` (4.78 MB, **exactly 9,049 records**); (B) 52 static range pages (different, larger
dataset; ~15–17k rows; no search). Tool result card: Prefix, **Plan** (product type), **Payer** (home
plan name), **Main Phone, Pre-Cert phone, DME phone**. Static table columns:
`BCBS Prefix | State | Company Name | Types Of Health Plan`.

| Q | Verdict | Evidence |
|---|---|---|
| 1 Plan name | **Yes** (both systems) — e.g. "Anthem Blue Cross - California" |
| 2 State | **Yes in static tables** (e.g. `SAA | South Dakota/Iowa | Wellmark…`); not a tool field |
| 3 Payer ID | **No** — despite marketing copy claiming "payer ID verification", no payer-ID field exists in JSON, tool output or tables |
| 4 Claims address / 6 Filing limit | **No** to both |
| 5 Phone | **YES — blog claim refuted.** Tool returns Main + Pre-Cert + DME phones (e.g. "(800).677.6669"); title "Instantly Find Payer, Plan Type & Phone Number". (Static tables: no phones) |
| 7 Product type | **YES — blog's uniqueness claim refuted.** "Product Del Method": PPO 8,002 / TRAD 769 / MED ADV / MEDIGAP / POS / EPO…; tables' "Types Of Health Plan" |
| 8 Extras | Pre-Cert + DME phones; JSON carries employer group ("Account Name") + Comments (not displayed) |
| 9 Search ("partial"?) | **Genuine instant search**: fetches full JSON client-side, exact-prefix match + as-you-type autosuggest (top 10). Limits: prefix-only, one page; range pages have no search. "Partial" only defensible as "only part of the content is searchable" |
| 10 Coverage | 9,049 (tool, measured) — no number stated on site |
| 11 Mobile | Responsive (OceanWP) |
| 12 Login/payment | None (JSON itself is public) |
| 13 Last updated ("April 2026"?) | **Partial.** No visible date. Tool page dateModified **2026-04-17**; hub **2026-06-06**; sitemap lastmods up to 2026-06-06. Blog active to 2026-07-30. "April 2026" understates freshness |
| 15 Archive | Blocked / 429; cannot verify |
| 16 Data source | None stated; disclaimer disclaims accuracy ("Use the content at your own risk"). **Provenance note:** the JSON's keys are verbatim the CareCentrix spreadsheet's column headers ("Out of State Blues Plan - Home Plan Name", "Pre-Cert (Now has Med-Surg Numbers)", "Column I Custom Column (Yellow if populated Free Text)") — the tool's dataset appears to be a converted, uncredited subset (9,049 of 21,792 rows) of the CareCentrix file. Editorially useful; phrase as "appears derived from" if published |
| 17 Error reporting | Open comments on prefix posts + contact form + Info@smartrcmsolutions.com + phone |
| 18 Ads | AdSense Auto ads sitewide (ca-pub-8708030479421437) |
| 19/20 | **Billing company content-marketing — confirmed** ("end-to-end billing services"; ~20 specialties; 53 of 78 sitemap posts are prefix pages; About names "Tim Woods — CEO & Founder"; registered-agent address in Sheridan, WY) |
| 21 $2.49 | **Not found** (only phone-digit matches and the substring "Pro**per claim** routing") |

### 4. Xceed Billing Solutions (xceedbillingsolutions.com) — checked 2026-08-05

Structure: hub `/bcbs-prefixes-list/` → 52 static range pages. Alpha table:
`Alpha Prefix | BCBS Home Plan Name | BCBS Home Plan Website`; alphanumeric adds a State column.
~19–20k rows sampled incl. "Prefix Not in Use" entries; no count stated ("we have listed down the
complete BCBS alpha prefix list"). Note: **bcbsprefix.com is a 301 alias** of Xceed's prefix hub.

| Q | Verdict | Evidence |
|---|---|---|
| 1 Plan name | **Yes** (`AAA | BCBS of Alabama | https://www.bcbsal.org/…`) |
| 2 State | **Alphanumeric pages only**; alpha pages have no State column |
| 3 Payer ID | **No** (separate cross-linked /payer-id-list-lookup/ page) |
| 4 Address / 6 Filing / 7 Product type | **No** to all |
| 5 Phone | **No — blog claim refuted as stated.** Prefix rows never return a phone; a separate page /bcbs-provider-phone-number/ is a 64-row state table ("BCBS of Alabama … | 800-760-6852") |
| 8 Extras | Home-plan website URL per prefix; retired prefixes flagged ("ARI | Prefix Not in Use") |
| 9 Search | Static range pages; DataTables per-page search box (single page only, pageLength 1000); no global lookup; no download |
| 11 Mobile | Responsive (viewport + TablePress responsive CSS) |
| 12 Login/payment | None (dismissible lead-capture popup only) |
| 13 Last updated ("January 2026"?) | **CONFIRMED — visibly.** `<time class="updated" datetime="2026-01-07T09:51:59+00:00">January 7, 2026</time>` on AAA–AZZ; three other pages same date; titles "(Updated 2026)". (Self-reported; archive could not corroborate) |
| 14 Freshness | Footer © 2026; hub body still says "directory of 2025" |
| 16 Data source | None stated (self-attestation only) |
| 17 Error reporting | Open comment forms on prefix pages + Tidio chat + email + 2 phones + contact form |
| 18 Ads | Heavy AdSense on prefix content (28–32 units/page; none on homepage) |
| 19/20 | **Billing company — confirmed** ("Medical Billing Services Company Houston Texas"; full RCM + specialty pages; prefix list is lead-gen side content) |
| 21 $2.49 | **The source of the garbled quote.** Exact HTML: `<h3 class="hustle-title">Medical Billing Services Starting from  2.49%</h3>` (homepage popup; the only 2.49 on the site; no "$", no "/claim"). Percentage of collections |

### 5. CareCentrix (help.carecentrix.com) — checked 2026-08-05

| Q | Verdict | Evidence |
|---|---|---|
| Exists / downloadable | **CONFIRMED** — https://help.carecentrix.com/ProviderResources/BCBS_Pre-Fix_Identification_Tool.xlsx, HTTP 200, 1.6 MB, no login (site root 403s to browsing but the file serves anonymously) |
| Excel? | **CONFIRMED** — genuine .xlsx (lookup form sheet + data sheet) |
| Contents | **21,792 prefix rows.** Columns: Prefix, Account Name (employer group), Home Plan Name, **Product Del Method** (PPO 17,349 / TRAD 2,042 / TBD 1,453 / MED ADV 309 / HMO / EPO / POS…), Main Provider Services Phone, 2 × Pre-Cert phones, Comments. **Plan name ✓, phones ✓, product type ✓; state only inside plan name; payer ID ✗, claims address ✗, filing limit ✗** |
| Last updated | **HTTP Last-Modified: Thu, 02 Jul 2026** (internal metadata 2026-07-02; in-file date 2026-06-26, "EDRC Aproved # 948" [sic]) — **actively maintained; cannot be framed as stale** |
| Business | Home-based care coordination / home benefit management company ("CareCentrix simplifies care coordination and home benefit management…"). **Not** a billing-services vendor; the tool is a free provider resource. Official description (BlueCard QRG): "This tool identifies BCBS plans using the 3-character prefix as well as the home plan, group name, product type and phone numbers…" |

### Other significant tools the comparison omits (checked 2026-08-05)

1. **medicalbillingrcm.com** — the biggest omission. Hub /alpha-prefix-list-bcbs/ + 52 range pages
   (AAA–ZZZ + alphanumeric); **prefix + plan name only**; dated "updated August 5, 2026" (hub);
   AdSense; billing-education site. Strong search visibility ("BCBS prefix list 2026" ~position 2).
2. **rcm.tools/tool/bcbs-prefix-lookup** — ranked #1 for "blue cross prefix lookup tool"; the only
   other instant-search app, but **currently broken** (homepage stuck "Loading prefixes…"; every
   result route probed returned 404). Carries an accuracy disclaimer.
3. **healthquestbilling.com/bcbs-prefix-lookup/** — static hub + 52 range pages, no search, no date;
   billing-company content marketing.
4. **Official plan resources** (partial scope, outrank third parties on head terms): Premera PDF
   "Three Character Prefixes, Last updated: 08/01/2026"; AZBlue Excel prefix lists (eff. 1/1/26 &
   7/1/26, own prefixes only); BCBSTX BlueCard explainer.
5. Dead: billingexecutive.com (DNS fail/502), bcbsprefixlookup.com (parked/for sale).

**Uniqueness check across the wider field:** no additional tool returns payer IDs, claims addresses
or filing limits. The payer-ID and claims-address uniqueness claims survive everywhere; the
**product-type and phone claims do not** (Smart RCM tool, CareCentrix file).

---

## Part 1C — specific claim verdicts

| Claim | Verdict |
|---|---|
| "MyPayerDirectory … hasn't been updated since March 2022" | **CONFIRMED** (own sitemap: all prefix pages lastmod 2022-03-05, contact 2022-03-08; visible dates 2020; only a boilerplate privacy page touched Apr 2026) |
| "MyPayerDirectory is the most well-known" | **Cannot verify the superlative.** Supportable reworded: highest organic traffic of the five (Ahrefs 2026-08-05: ~24.4k visits/mo, 5× next) and oldest (2009; BCBSA takedown demand 2021) |
| RCM Guide last updated "January 2026" | **Partially confirmed** — `article:modified_time` 2026-01-24 on prefix pages (metadata only; no visible date; table headers still say "2024") |
| Smart RCM last updated "April 2026" | **Partially confirmed / understated** — tool page 2026-04-17, but prefix pages modified to 2026-06-06 and site active July 2026 |
| Xceed last updated "January 2026" | **CONFIRMED** — visible "January 7, 2026" updated stamp |
| "None of the other major prefix tools include payer IDs or claims addresses" | **CONFIRMED** for those two fields, across all five + the wider field (caveat: Smart RCM *advertises* "payer ID verification" but does not deliver it). If the sentence bundles filing limits: also confirmed. If it bundles product type or phones: **refuted** |
| "Most of these tools were built as marketing content for billing companies" | **REFUTED as "most"** — 2 of 5 (Xceed, Smart RCM). MPD = standalone directory; RCM Guide = personal blog; CareCentrix = care-coordination provider resource |
| "Some of the most commonly used tools … haven't been touched since 2022" | **Only MyPayerDirectory.** Make it singular and specific |
| Smart RCM has "partial" instant search | **Inaccurate** — full instant search w/ autosuggest (exact-prefix-only, single page) |
| MPD & Xceed show phones; RCM Guide & Smart RCM don't | **Mostly refuted**: MPD ~0.5% of rows only; Xceed none in prefix results (separate page); RCM Guide correct (none); Smart RCM **does** (tool, 3 phone fields) |
| CareCentrix is a downloadable Excel file | **CONFIRMED**, still available, no login, updated 2026-07-02 |

---

## Part 2 — industry-fact verdicts (items 22–30)

| # | Claim | Verdict | Evidence / fix |
|---|---|---|---|
| 22 | "Over 60 independent BCBS companies" | **REFUTED** | bcbs.com/about-us/blue-cross-blue-shield-system: "Our 33 BCBS companies…". Count is a moving target (39→36→35→34→33) — date it. Fix: 33 (2026) |
| 23 | Alphanumeric prefixes since 2018, letter space running out | **CONFIRMED** | Premera FAQ 045078 (2.28.2018): "Effective April 15, 2018, all BCBS plans and providers must be able to accept alpahnumeric [sic] prefixes… will use these prefixes for new plans. Existing BCBS plans won't change existing alpha prefixes." Reason: "limited number of combinations and a growing number of plans." Add the exact date; note existing prefixes unchanged |
| 24 | "Each prefix assigned to exactly one BCBS plan" | **Partly confirmed — caveat needed** | BCBS SC manual: "The prefix identifies the Blue Plan **or National Account**…" FEP = "R" + 8 digits (no prefix — Blue Cross of Idaho PAP 102, Highmark manual); some cards have no prefix; one company holds many prefixes |
| 25 | "Average hold time: 10-20 minutes" | **CANNOT VERIFY — unsourced** | No published source found. Citable alternative: CAQH Index 2024 — phone inquiry = "25 minutes per inquiry" of staff time. Remove or substitute |
| 26 | "Filing limits 90–365 days" | **REFUTED (upper bound)** | **730 days = BCBS of Alabama**: "Claims must be submitted and received by us within 24 months after the service takes place" (bcbsal.org). Floor 90 days confirmed: BCBS MA Timely Filing Guidelines ("90 days from the date of service"). Mid: BCBSIL 180, BCBSTX PPO 365 |
| 27 | British spellings across 13 posts | **Cannot check** | Post drafts not in this repository. Known flag: "prior authorisation" in post 6. Run a sweep for -ise/-isation, "colour", "whilst", "cheque", "centre", "programme", "authorised", "organisation" once drafts are available |
| 28 | Carelon / Magellan behavioral carve-outs | **Carelon confirmed; Magellan outdated** | Carelon Behavioral Health (Elevance) current for Anthem plans (role = utilization management; claims via Availity — "routes claims to Carelon" overstates). Magellan ended for BCBSTX, Blue Shield of CA, Independence effective **1 Jan 2026** (BCBSTX provider news; magellanprovider.com). Fix to past tense / "check the ID card" |
| 29 | HMO referrals / EPO in-network | **CONFIRMED** as generalisations | healthcare.gov glossary quotes captured. Add "(emergencies excepted)" to the EPO sentence |
| 30 | "Appeals and coverage questions often need to go to the home plan directly" (post 5) | **Partly refuted** | BCBS SC §5.8: local plan "handles appeals for all claims" and coordinates with the home plan; Highmark same. Home plan does decide benefits/medical policy/prior auth — via prefix routers/EPA/800-676-BLUE, not direct contact. Rewrite the sentence |

---

## Part 3 — corrected master comparison table

The drafts of posts 2, 4 and 10 were not in this repository; the table below is the verified master
to reconcile each post's table against. Every cell is evidenced above; nothing here is asserted
beyond what was checked on 2026-08-05.

| Feature | PrefixLookup* | MyPayerDirectory | RCM Guide | Smart RCM Solutions | Xceed Billing | CareCentrix (xlsx) |
|---|---|---|---|---|---|---|
| Plan name | ✓ | ✓ | ✓ (company name) | ✓ | ✓ | ✓ |
| State / service area | ✓ | ✗ (in name only) | ✓ | ✓ tables / ✗ tool | ✓ alphanumeric pages only | ✗ (in name only) |
| Electronic payer ID | ✓ | ✗ | ✗ | ✗ (despite marketing) | ✗ (separate page) | ✗ |
| Claims mailing address | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Provider phone | ✓ | ~0.5% of rows | ✗ | **✓ (tool: main + pre-cert + DME)** | ✗ (separate state page) | ✓ (3 phone columns) |
| Timely filing limit | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Product type (PPO/HMO/EPO) | ✓ | 62 rows only | ✗ | **✓** | ✗ | **✓** |
| Lookup format | instant | static letter pages | static + per-table filter | **instant tool** (exact prefix + autosuggest) + static pages | static + per-table filter | Excel download |
| Approx. coverage (measured) | 65 billing entities† | ~18,795 prefixes | ~22,984 rows incl. unallocated | 9,049 (tool) | ~19–20k rows incl. not-in-use | 21,792 rows |
| Last content update (evidence) | — | **Mar 2022** (own sitemap) | 24 Jan 2026 (page metadata) | 17 Apr–6 Jun 2026 (metadata) | 7 Jan 2026 (visible stamp) | **2 Jul 2026** (HTTP header) |
| Login/payment required | — | ✗ | ✗ | ✗ | ✗ | ✗ |
| Mobile-responsive markup | — | ✓ | ✓ (+AMP) | ✓ | ✓ | n/a (file) |
| Display ads | — | Monumetric | AdSense | AdSense | AdSense | none |
| Sells billing services | — | ✗ | ✗ | ✓ | ✓ | ✗ (care coordination co.) |
| Data source stated | — | ✗ | ✗ | ✗ (disclaims accuracy) | ✗ | own provider resource |
| Error-report channel | — | none | email only (form broken) | comments + form + email | comments + chat + email + phone | n/a |

\* PrefixLookup's own column asserted per the brief; verify against the live product before publishing.
† The brief notes PrefixLookup's database holds 65 billing entities — not directly comparable with
per-prefix row counts; don't juxtapose the numbers without saying so.

### Safe replacement sentences for the risky claims

- Uniqueness: "**None of the other prefix tools we checked returns an electronic payer ID, a claims
  mailing address, or a timely filing limit** (verified against MyPayerDirectory, RCM Guide, Smart RCM
  Solutions, Xceed Billing and the CareCentrix spreadsheet, August 2026)." — do **not** include product
  type or phone numbers in that sentence.
- Staleness: "**MyPayerDirectory — the highest-traffic third-party prefix site — hasn't updated its
  prefix pages since March 2022** (per its own sitemap); the other tools we checked all show 2026
  updates."
- Billing-company framing: "**Two of the five** (Xceed Billing Solutions and Smart RCM Solutions) are
  billing companies whose prefix lists double as lead-generation content; the others are an
  ad-supported directory, an information blog, and a care-coordination company's provider resource."
- Pricing: quote Xceed exactly — "Medical Billing Services Starting from 2.49%" — or omit.

---

## Ahrefs authority/traffic snapshot (2026-08-05, mode=subdomains)

| Domain | DR | Est. organic traffic/mo | Keywords | Ref. domains | Top country |
|---|---|---|---|---|---|
| mypayerdirectory.com | 2.4 | 24,415 | 516 | 711 | US |
| rcmguide.com | 4.0 | 4,685 | 633 | 720 | US |
| help.carecentrix.com | 48.0 | 2,534 | 248 | 65 | US |
| smartrcmsolutions.com | 0.0 | 1,494 | 255 | 394 | US |
| xceedbillingsolutions.com | 51.0 | 514 | 137 | 577 | **India** |
| prefixlookup.com | 0.0 | 0 | 2 | 410 | US |
