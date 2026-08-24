# Drive (drive.co.uk): Prospect Briefing

Prepared 24 August 2026 for the TenTerms PR and SEO pitch.
Research is desk-based: Ahrefs, live crawls of drive.co.uk and the redirected legacy domains, SerpApi live SERPs, Companies House and trade press. No GSC or analytics access.

---

## 1. Snapshot

| | |
|---|---|
| Brand | Drive |
| What they do | Consumer car marketplace: used car search, new car leasing offers, reviews, buying guides and finance comparison. They do not sell cars themselves; they pass enquiries to retailers |
| Operator | Volkswagen Financial Services (UK) Limited, trading as Drive. The complaints policy names VWFS UK as Drive's "principal firm", so Drive operates as an FCA appointed representative |
| Legal entities | VWFS (UK) Limited, no. 02835230, active, Brunswick Court, Milton Keynes. Legacy entity Mobility Trader UK Ltd (heycar UK), no. 12016686, **in liquidation** |
| Website | https://drive.co.uk |
| Launched | Week commencing 13 August 2026, roughly 11 days old at the time of writing |
| Built from | heycar UK + BuyaCar + Honest John, all three consolidated into one domain |
| Market | UK only |
| Key people | Dan James, Chief Transformation Officer, VWFS UK (the public voice of the launch). Mike Todd, CEO, VWFS UK |
| Source of lead | Agency-side prospecting; commercial priorities not shared |

**Scale of the site today:** 5,075 URLs in the sitemap. 2,669 make/model search pages, 1,754 location pages, 399 car reviews, 135 guides, 110 used-car filter pages, 7 static pages and exactly 1 leasing page.

---

## 2. Prospect scoring

Scored against the TenTerms qualifying pattern. Note that Drive breaks the usual ICP: this is a corporate division of a captive finance company, not an owner-managed SME.

| Dimension | Score | Visual |
|---|---|---|
| Search Opportunity | 10/10 | ██████████ |
| Ability to Pay | 10/10 | ██████████ |
| Lead Value | 9/10 | █████████░ |
| Strategic Value | 9/10 | █████████░ |
| Client-Side Capacity | 8/10 | ████████░░ |
| ICP Fit | 5/10 | █████░░░░░ |
| Decision Reachability | 3/10 | ███░░░░░░░ |

The commercial case is close to perfect and the qualifying case is not. A brand-new domain has just absorbed a 150,000-visits-a-month editorial asset through a botched redirect, it has 248 commercial keywords stranded on pages two and three, and its own structured data still tells Google it is a company in liquidation. The work is obvious, urgent and large. The problem is reach: this is a corporate marketing and transformation function inside a multi-billion-pound captive lender, almost certainly with an incumbent agency roster, an in-house team and a procurement process. Getting to Dan James or whoever owns Drive's P&L is the entire challenge, not building the case once there.

---

## 3. What Drive is, and how it makes money

Drive is a **lead generation and finance origination platform dressed as a marketplace.** The FAQ is unusually explicit about what it is not:

- It does not sell cars online. Buyers contact the retailer directly by message or phone.
- It does not buy cars or take part exchanges. Valuations are free, and sellers are referred to **Motorway**.
- It does not accept private seller listings. Only approved retailers can list.

So the revenue lines are:

1. **Finance and lease originations written by VWFS.** Drive is an appointed representative of VWFS UK, and finance complaints escalate to VWFS as principal.
2. **Retailer listing and lead fees** from Volkswagen Group and "aligned" retailers.
3. **Referral income**, at minimum from the Motorway part-exchange partnership.

The buried JavaScript configuration on the site confirms the funnel design. Live feature flags include `leadEnrichmentFinanceQuote`, `leadEnrichmentPartExchange`, `leadEnrichmentBookAppointment` and `leadFormReservationCta`, plus a "£99 hold" reservation flow. Every enquiry is being enriched with a finance quote, a part-exchange valuation and an appointment before it reaches the retailer.

---

## 4. Likely commercial goals, in priority order

This is the section you asked for. Drive has not published its objectives, so each of these is inferred from what the business is structurally built to do, and each carries the evidence that supports it.

### Priority 1: Grow VWFS finance and lease originations by owning the customer earlier

**Why this is first.** VWFS makes its money on the credit agreement, not on the listing fee. A listing fee is worth tens of pounds. A four-year PCP on an £18,000 used car is worth thousands in interest income over its life. Historically VWFS met the customer at the very end of the journey, at the point the dealer arranged finance. Drive moves the first touch to the moment somebody types a model name into Google, months earlier.

**Evidence.**
- Drive is an FCA appointed representative of VWFS UK, not a neutral publisher.
- The homepage merchandises by **monthly payment**, not price. Its own internal links include `/cars/used?monthly-price__lte=150`, `£200` and `£300`.
- Product copy leads on "compare monthly costs" and "affordability", not on price or mileage.
- Every lead form carries a finance quote enrichment step.
- `/car-finance` is one of the few non-inventory pages that exists at all, with long-form PCP, HP and leasing explainers.

**What this means for a PR and SEO brief.** The money keyword set is not "used cars for sale". It is the finance and affordability layer: PCP, HP, car finance, £X a month, no deposit, bad credit, lease deals, business contract hire. Notably, Honest John already ranked at position 8 for "best pcp deals" and position 4 for "£99 a month car deals no deposit", and both of those pages have just been redirected into a homepage.

### Priority 2: Build a captive retail channel and cut the network's dependence on Auto Trader

**Why.** Auto Trader is effectively a tax on every UK dealer, and it takes 13.7 million organic visits a month in the UK against Drive's 5,088. VW Group retailers pay it to reach customers who then get financed by whoever the retailer chooses. A first-party VWFS-owned marketplace turns that cost centre into an owned channel and strengthens VWFS's hold on the retailer relationship.

**Evidence.** The trade press framing of the launch is explicit about giving Volkswagen Group and aligned retailers "another route to reach customers". Drive is the second platform VWFS UK has launched this year, after **Purchase Pro**, its wholesale platform for trade buyers. Together, wholesale plus retail plus finance is a closed loop.

**Caveat worth testing.** The homepage is heavily weighted to VW Group brands (Volkswagen, Audi, SEAT, Škoda, CUPRA are the default make filters and the featured reviews). If retailer supply is the goal, that tilt limits how broad the consumer proposition can credibly be.

### Priority 3: Support residual values and remarket the returning lease and PCP book

**Why.** Every PCP and lease VWFS writes creates a future used car it is exposed to. Residual value performance is one of the largest single swings in a captive lender's P&L. A retail marketplace plus a wholesale platform gives VWFS control over how ex-fleet and ex-PCP stock is disposed of and how visibly it is marketed.

**Evidence.** Purchase Pro on the wholesale side, Drive on the retail side, an inventory restricted to approved, warranty-backed vehicles "the majority less than eight years old", and heavy promotion of manufacturer approved-used programmes. Drive already ranks (badly, at positions 17 to 27) for "audi approved used", "vw approved used", "approved used bmw", "ford approved used" and "volvo selekt".

### Priority 4: Own the research and advice stage, and the first-party data that comes with it

**Why.** This is why VWFS bought and then absorbed editorial. Reviews and guides are how you reach a buyer six months before they are in market, and how you collect intent data.

**Evidence.** 399 car reviews and 135 guides migrated from Honest John, an `/authors` section preserving named journalists, and `/value-my-car` already ranking at position 8 for "free car valuation without email". Valuation tools are data capture instruments as much as consumer tools.

### Priority 5: Establish "Drive" as a UK consumer brand from a standing start

**Why.** They have thrown away three established brand names in one week. heycar had been building UK recognition since 2019. Honest John had 25 years of trust. Both are now gone, replaced by a generic English word that is heavily contested.

**Evidence, and this is stark.** A UK Google search for "drive.co.uk" returns a Knowledge Panel for **a driving school in Woolhampton, Reading**, an unclaimed listing pointing at carsandstuff.uk. Positions 2 to 10 are driving schools, a Reddit thread about a different company, a Trustpilot page for a different company, and **Drive Motor Retail**, a genuine 34-outlet UK dealer group. Drive has no LinkedIn company page (404). Its Instagram handle exists with zero posts and zero followers.

### Priority 6: Acquire part-exchange and sourcing volume

Lower priority because it is currently outsourced to Motorway rather than owned, but `/value-my-car` is already one of the site's two best-performing pages, and Drive ranks for "motorway car valuation" and "motorway car value". If sourcing ever comes in-house, this is where it starts.

### What are almost certainly *not* goals

- **Direct online car sales.** Explicitly ruled out in the FAQ.
- **Private classifieds.** Explicitly ruled out.
- **New car sales, for now.** Despite "new cars" appearing in the navigation and 503 new-car URLs sitting in the sitemap, `robots.txt` actively blocks `/cars/new` from every crawler. Either new cars is a deliberately un-indexed lead channel, or this is a mistake. Worth asking.

---

## 5. Who's who

| Role | Person | Notes |
|---|---|---|
| Public voice of Drive | **Dan James**, Chief Transformation Officer, VWFS UK | Quoted in every launch story. Frames Drive as "an important milestone in our digital transformation" |
| Ultimate decision maker | **Mike Todd**, CEO, VWFS UK | Unlikely to be reachable directly |
| Adjacent | Mark Pain, product and change delivery director; Katie Warrington, Head of Product | Product side rather than marketing |

**Intermediary risk: high.** There is no visible marketing director or head of brand for Drive specifically, and no LinkedIn company page to trace hires from. A pitch is likely to enter through a marketing manager or an agency procurement route, not through a P&L owner. The single most valuable thing to establish on a first call is who owns Drive's commercial targets and who signs an agency contract.

**Capacity is not a concern.** Unlike a typical SME prospect, there is a product team, a content team with named authors, and an engineering function shipping releases (the site reports build v0.233.2).

---

## 6. Financial picture and affordability

**Volkswagen Financial Services (UK) Limited**, no. 02835230, incorporated 1993, active. Registered at Brunswick Court, Milton Keynes. SIC 64999 financial intermediation and 77110 leasing of cars. Last accounts to 31 December 2024; next due 30 September 2026.

VWFS UK is one of the largest motor finance providers in the country and a subsidiary of Volkswagen Financial Services AG. Affordability is not a question. A £1,500 to £4,500 monthly retainer is immaterial at this scale, which cuts both ways: budget will not be the objection, but neither will the standard TenTerms retainer look meaningful enough to command senior attention. Any pitch needs to be sized and framed as a programme, not a retainer.

**The one financial flag worth knowing.** The legacy entity **Mobility Trader UK Ltd** (heycar UK, no. 12016686) is **in liquidation**, with accounts overdue since 31 December 2025. This matters commercially because of what is described in section 7.

---

## 7. Search and AI visibility snapshot

Spot check from public data, not a rank-tracked audit with GSC access.

### Where Drive stands today

| Metric | drive.co.uk | honestjohn.co.uk (the asset absorbed) |
|---|---|---|
| Domain Rating | 59 | 68 |
| Live referring domains | 1,350 | 6,286 |
| Organic keywords (GB) | 1,094 | tens of thousands |
| Est. monthly organic visits (GB) | 5,088 | 152,361 |
| Est. monthly traffic value | ~$1,855 | ~$49,970 |

Referring domains to drive.co.uk jumped from 579 in July to 1,383 in August, so the launch PR did land links. The site is nonetheless carrying roughly one fifth of the authority of the brand it replaced.

### The competitive set

| Competitor | UK monthly organic traffic | DR | Shared keywords |
|---|---|---|---|
| autotrader.co.uk | 13,657,667 | 82 | 858 |
| carwow.co.uk | 1,754,969 | 74 | 765 |
| theaa.com | 3,764,431 | 82 | 571 |
| arnoldclark.com | 1,286,703 | 68 | 404 |
| cazoo.co.uk | 888,864 | 68 | 518 |
| whatcar.com | 686,349 | 74 | 477 |
| motorpoint.co.uk | 601,651 | 57 | 428 |
| parkers.co.uk | 600,795 | 69 | 692 |
| cinch.co.uk | 595,984 | 60 | 528 |

Drive is competing simultaneously against classifieds (Auto Trader, Motors), retail disruptors (Cinch, Cazoo, Motorpoint), publishers (Parkers, What Car?, Auto Express) and its own retailer network's own websites (Arnold Clark, Lookers, Evans Halshaw). Honest John used to give it a credible foothold in the publisher category. That foothold is currently being dismantled.

### What a buyer actually sees

A UK buyer searching "used cars for sale" sees Auto Trader, Motors, Cazoo, AutoUncle, Carwow, AvailableCar, Group 1, Lookers, Motorpoint and the AA, plus a local map pack of physical dealers and four AI-generated related questions including "What is the best site for second-hand cars?". Drive appears nowhere on page one, and does not appear in the AI answer surfaces.

A UK buyer searching the brand itself, "drive.co.uk", sees Drive rank first organically but sees a **Knowledge Panel for a driving school in Woolhampton** occupying the right-hand entity slot, and seven of the ten organic results belonging to other companies called Drive.

### AI and entity visibility: the finding that matters most

Drive's own structured data, served on every page, currently tells Google and every AI crawler this:

```json
"about": {
  "@type": "Organization",
  "foundingDate": "2019",
  "brand": "Mobility Trader UK Limited",
  "alternateName": ["heycar", "heycar uk", "heycar used cars"],
  "sameAs": ["facebook.com/heycar.uk", "instagram.com/heycaruk",
             "linkedin.com/company/heycar", "twitter.com/heycar_uk"],
  "address": { "streetAddress": "Theobalds Rd, Lacon House", "postalCode": "WC1X 8NL" }
}
```

The declared brand owner is a company in liquidation. The declared alternate names are heycar. The declared social profiles are heycar's. The declared address is heycar's old office. The page's declared primary image is still `/img/heycar-logo-square.jpg`, and it still resolves. The `/value-my-car` meta description, on a page ranking at position 8, still reads "free car valuation without email **from heycar**". German-language finance strings from the heycar DE codebase ("Finanzierung mit Schlussrate", "PrivatLeasing", "km/Jahr Laufleistung") are still shipping in the page payload.

For a business trying to establish a brand entity and get named in AI answers, this is the highest-value, lowest-effort fix on the site.

---

## 8. The migration problem, and why timing makes this urgent

This is the strongest single reason to pitch Drive this month rather than next quarter.

Honest John was redirected in the week of 13 August 2026. The three legacy domains were handled very differently:

| Legacy domain | Redirect behaviour | Verdict |
|---|---|---|
| heycar.co.uk | `/volkswagen/golf` → `/cars/volkswagen/golf/review` | Properly mapped, page to page |
| buyacar.co.uk | `/cars/ford/focus` → `/cars/used` | Partially mapped, model to category |
| **honestjohn.co.uk** | **every URL → `https://drive.co.uk/?from=hj`** | **Blanket 301 to the homepage** |

Every Honest John URL tested returns a 301 to the homepage. `/carbycar/`, `/real-mpg/`, `/askhj/`, `/forum/`, `/new-car-deals/`, `/used-prices/`, `/news/`, and the subdomains `classics.honestjohn.co.uk` and `kit.honestjohn.co.uk` all land on the same page. Only `vans.honestjohn.co.uk` gets a category-level target.

Google treats a bulk redirect to an irrelevant page as a soft 404 and drops the redirected URL's rankings rather than transferring them. The pages being thrown away include:

| Page | Est. monthly visits | Rank |
|---|---|---|
| honestjohn.co.uk homepage | 12,460 | 1 for "honest john" |
| /advice/owning-advice/wet-belt/ | 3,602 | 2 for "wet belt" |
| /askhj/answer/42957/ (real mpg) | 2,327 | 2 for "real mpg" |
| /real-mpg/ | 1,847 | 135 keywords |
| /guides/suv/best-small-suv/ | 1,102 | 5 |
| classics.honestjohn.co.uk (two pages) | 2,059 | 6 and 7 for "classic cars for sale" |
| /new-car-deals/pcp-car-deals/ | 569 | 8 for "best pcp deals" |

**Real MPG, the proprietary crowd-sourced fuel economy dataset that was Honest John's single most defensible asset, does not exist on Drive.** `drive.co.uk/real-mpg` returns 404. There is no `real-mpg` section anywhere in the sitemap. The only related URL is one guide, `/guides/best-cars-for-real-mpg`. The trade press reported that the data had moved. As far as Google is concerned, it has not. The same is true of the Ask HJ archive, the forum and the classics marketplace.

Ahrefs still shows honestjohn.co.uk at 152,361 monthly visits for August because the redirect is 11 days old and the index has not caught up. **The decay has not happened yet. It is about to.** That is the window.

### Additional technical faults found in a 30-minute crawl

1. **Soft 404s at scale.** `/guides/anything-at-all` returns HTTP 200 with a blank `<title> | Drive</title>` and 196 words of boilerplate. Every dead Honest John guide URL Google retries will get a 200 instead of a 404.
2. **robots.txt contradicts the sitemap.** `Disallow: /cars/new` blocks 503 new-car URLs that are submitted in `sitemap-search-model-pages.xml`.
3. **Parameter URLs are indexed and competing.** `robots.txt` says `Disallow: /*?*`, yet `?from=buyacar` and `?from=heycar-uk` versions of model pages are ranking, in some cases instead of the clean URL (`/cars/used/dacia/jogger?from=buyacar`, `/cars/used/suzuki/vitara?from=buyacar`).
4. **Case-variant duplicates are ranking.** `/Cars`, `/Guides` and `/Car` all rank as separate pages. `/Cars` is the ranking URL for "audi q7" (41,000 searches) and "toyota hilux" (27,000).
5. **1,754 location pages with no local content.** `/cars/used/abbots-langley` advertises "6,517 cars for sale in Abbots Langley" from a national feed. These are thin doorway pages at scale and a Helpful Content risk.
6. **Leasing is one page.** For a leasing company, `/cars/lease-deals` is the only leasing URL in the sitemap, and `/leasing` has no H1 at all.
7. **No corporate surface.** No `/about`, no newsroom, no retailer-facing page. There is nowhere for earned coverage to point and nothing establishing who Drive is.
8. **Title bug.** `/guides` renders "Car Buying Guides | Trusted & Expert Car Buying Advice | Drive  | Drive".

---

## 9. Size of the prize

### The near-miss inventory

Drive currently ranks in positions **11 to 30** for **248 keywords with 1,000 or more UK searches a month**, representing **2,793,000 combined monthly searches**. These are page two and page three positions on terms like "peugeot 3008" (103,000), "ford kuga" (80,000), "vw tiguan" (68,000), "byd seal" (114,000, position 12) and "vauxhall corsa" (50,000).

| Scenario | Assumption | Additional monthly organic visits |
|---|---|---|
| Conservative | one quarter of the set reaches positions 8 to 10, at 2% CTR | ~14,000 |
| Realistic | half the set reaches positions 4 to 7, at 6% CTR | ~84,000 |
| Stretch | the set averages positions 3 to 5, at 12% CTR | ~335,000 |

These are model-name head terms contested by Auto Trader and the manufacturers, so the conservative figure is the honest one to lead with. The point is not the exact number: it is that the inventory already exists and is one page away.

### Recovering what is being lost

Separately, correctly remapping the Honest John estate is a recovery play worth up to **152,000 monthly visits**, valued by Ahrefs at roughly **$50,000 a month**, or about **£450,000 a year** in equivalent paid media. Some of that is unrecoverable (the forum, arguably the classifieds). A realistic recovery target on the reviews, guides, advice and Real MPG content is a meaningful fraction of it, and every week of delay reduces it.

### Translating to Drive's revenue

Drive has not published lead economics, so this is an illustrative chain with stated assumptions, to be replaced by their own figures at discovery:

- 84,000 additional monthly sessions (the realistic case above)
- at a 1.5% enquiry rate, a conservative marketplace figure: **1,260 leads a month**
- at a 10% lead-to-sale conversion through the retailer: **126 incremental units a month**
- at 60% finance penetration: **~76 incremental VWFS finance agreements a month**, roughly 900 a year

Even at a modest few hundred pounds of net lifetime margin per agreement, that is a seven-figure annual contribution, before any listing or referral revenue. The three assumptions in that chain are exactly the three numbers to ask for on the first call.

---

## 10. TenTerms fit and suggested entry point

**Honest assessment.** Drive sits well outside the standard TenTerms ICP. This is not a £500k to £20m owner-managed SME; it is a division of a captive lender inside the Volkswagen Group. Expect an incumbent agency, an in-house SEO or performance team, and procurement. A cold pitch for a £3,000 a month retainer will not fit how they buy.

**What does fit, and what to lead with.**

1. **Lead with the migration audit, not with services.** The evidence in sections 7 and 8 is specific, verifiable in minutes and time-critical. A short, dated document titled something like "What the Honest John migration is about to cost Drive" is a far stronger opening than a credentials deck. It demonstrates capability rather than claiming it.
2. **Sell a paid migration recovery and brand entity sprint first**, scoped in weeks, not a retainer. Redirect remapping, Real MPG reinstatement, schema and entity correction, soft 404 fix, parameter and case-variant cleanup. This is a defined project with a measurable before and after, which is how corporates buy from new suppliers.
3. **The PR angle is genuinely strong and separable.** Three things need earned media that only PR can deliver:
   - **Brand entity establishment.** Drive needs consistent third-party citations, its own social profiles, a claimed Google entity, and a corrected `sameAs` graph before it can win its own brand SERP back from a Woolhampton driving school.
   - **Goodwill management.** Honest John's closure has produced visible negative sentiment on PistonHeads and in the motoring press ("25 years of advice you could actually trust"). Drive has inherited a bereaved audience. Handled well, that is a reputation asset. Ignored, it is a slow-burning brand problem.
   - **Data-led PR.** Drive is sitting on Real MPG, valuation data and VWFS finance data. That is a ready-made engine for the kind of data stories that earn national motoring coverage and the referring domains the domain badly needs (1,350 against Auto Trader's authority).
4. **Do not pitch a generic retainer.** If a retainer follows, it should follow a delivered project.

---

## 11. Discovery questions

1. Who owns Drive's commercial targets, and who would sign off an agency engagement? (Tests decision authority. This is the highest-value question on the call.)
2. What does success look like in the first twelve months: finance originations written through Drive, retailer lead volume, or brand awareness? The answer completely changes the SEO and PR priority order.
3. Was the Honest John redirect strategy a deliberate decision or a technical shortcut, and who owns the redirect map now? (Tests whether the finding in section 8 is news to them, and how defensively it will land.)
4. What happened to Real MPG? The trade press reported the data moved; we cannot find it on the site. Is it coming back, and on what URL?
5. Why is `/cars/new` blocked in robots.txt when 503 new-car URLs are in the sitemap? Is new car search a deliberately un-indexed lead channel?
6. What is a qualified enquiry worth to Drive, and what proportion converts to a funded VWFS agreement? (Replaces our estimates in section 9 with their numbers.)
7. Who is handling SEO and PR now, in-house or agency, and what is already committed for the next two quarters?
8. Is the ambition a whole-market marketplace or a Volkswagen Group retail channel? The current homepage says the latter; the positioning says the former.

---

## 12. Risks and open items

- **Decision reachability is the deal risk, not the commercial case.** Everything else here is strong. Assume several conversations before reaching a budget holder.
- **Incumbent agency is very likely** and unknown. Not established by desk research.
- **The migration may already be under review internally.** VWFS has a product and engineering function; they may well have spotted it. Our advantage is speed and specificity, not exclusivity.
- **Tone matters.** Section 8 amounts to telling a prospect that their brand-new flagship platform has a serious defect. Framed as an opportunity with a closing window it lands well; framed as criticism of their launch it does not.
- **Traffic decay is not yet visible in the data.** If we present this after the collapse shows up in Ahrefs, we are one of many. If we present it now, we are the only ones who saw it coming. That is a real but short-lived edge.
- **We have no GSC or analytics access**, so all traffic figures are Ahrefs estimates and all revenue figures are illustrative.
- **Scale mismatch.** TenTerms may not be credible as the sole supplier at this scale. A defined specialist project is the credible ask.

---

## 13. Sources

- drive.co.uk: live crawl of homepage, `/faq`, `/complaints`, `/cookies`, `/car-finance`, `/leasing`, `/value-my-car`, `/guides`, sample location, model and review templates; `robots.txt`; all seven sitemap files (5,075 URLs); on-page JSON-LD structured data; HTTP response headers
- honestjohn.co.uk, buyacar.co.uk, heycar.co.uk and the classics/vans/kit subdomains: live redirect testing with status codes and Location headers
- Ahrefs Site Explorer: metrics, metrics history, top pages, organic keywords, organic competitors, backlinks stats, referring domains history, domain rating, for drive.co.uk, honestjohn.co.uk and heycar.co.uk
- SerpApi live Google UK results for "used cars for sale" and "drive.co.uk"
- Companies House: VOLKSWAGEN FINANCIAL SERVICES (UK) LIMITED (02835230); MOBILITY TRADER UK LTD (12016686)
- Trade press: AM-online, Motor Trade News, Car Dealer Magazine, Fleet Europe, Asset Finance Connect
