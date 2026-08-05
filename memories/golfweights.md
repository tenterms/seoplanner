# Golfweights.co.uk — uniform enhanced brand-collection layout

**Client**: Golfweights.co.uk (golf club weights retailer, Shopify — Wetheme/Flow-based theme, NOT Dawn). Related to the earlier golf-weights de-cannibalisation project.

**Job**: A uniform, brand-agnostic enhanced layout for all brand collections (taylormade, ping, callaway, cobra, odyssey, titleist, scotty-cameron, …). Agreed structure per brand page:

- H1: `[brand] Golf Club Weights`
- H2: `All [brand] products` (2-row featured carousel)
- H2: `[brand] putter weights` · `[brand] driver weights` · `[brand] golf weight kits` · `[brand] club wrenches` (1-row carousels)
- Two text/image split blocks at the bottom (swing-weight guide + why-us)

## Where it landed (Aug 2026)

Work happens in a **draft theme called "new cat"** (theme id 196541677952). Two theme files, canonical copies in `golfweights/` in this repo:

- `sections/enhanced-collection.liquid` — the whole layout in one section, **brand-agnostic**:
  - `[brand]` token in any heading/description/link is replaced with `collection.title` at render time (URL-encoded in link overrides).
  - **Rollout control**: section setting `enabled_handles` (comma-separated collection handles, edited in the customiser — default `taylormade`). Replaced the earlier hardcoded handle check; the metafield + `collection.enhanced.json` route failed because Shopify only lists templates from the *published* theme in the collection's Theme-template dropdown.
  - **Auto show/hide**: each sub-carousel counts matching products (by product *type* equality OR *tag* contains, case-insensitive) and renders nothing when the brand has none. This is the per-brand show/hide mechanism — no per-brand config.
  - The shared collection header keeps `show_title`/`show_description` **true** in the template (non-enhanced collections need their H1); the enhanced section suppresses+removes the header title/description via scoped CSS+JS so enhanced pages keep a single H1.
  - Split-block images use core `image_url | image_tag` (not the theme's responsive-image snippet).
- `templates/collection.json` — default collection template with the enhanced section between header and grid, **all 6 blocks pre-configured in JSON** (4 sub-carousels + 2 splits) so no customiser block-clicking.

## Validated facts (don't re-derive)

- Product card snippet is `grid-view-item` — render directly for pixel-match cards.
- Store-wide product types: `Weights for Woods` (110), `Weights for Putters` (60), `Shaft Adapter` (37), `Wrench` (12), `Weights for Irons` (4). **Kits are NOT a type** — they're the tag `weight kit` (60 products, spans woods+putters).
- Per-brand coverage varies exactly as the show/hide design expects: Odyssey has no woods weights; Callaway/Titleist/Cobra have no wrenches; Mizuno/Honma/LAB have no kits. All brand collections ≤42 products, safely under Liquid's 50-product `collection.products` limit.
- Storefront filters: only `filter.p.product_type` and `filter.p.vendor` are enabled. **`?filter.` URLs canonicalise to the parent collection** (verified live) — safe for "view all" links.
- **Legacy tag URLs (`/collections/x/weight-kit`) self-canonicalise** — indexable duplicates, do NOT use. Kits "view all" instead links to `/collections/golf-club-weight-kits-1?filter.p.vendor=[brand]` (vendor = brand name, e.g. "TaylorMade").
- Header markup: title in `.collection-header__title > h1.collection-header__text-item`, description in `.collection-header__description`.
- Swing weight guide: `/pages/swing-weight-guide`. FAQs: `/pages/faqs`.
- Shopify gotchas hit: section schema `name`/preset max 25 chars; theme paths can't contain spaces; richtext settings in JSON templates must be `<p>…</p>`-wrapped.

## Open items

- Split blocks show grey placeholders until images are picked (customiser → Enhanced collection → block → Image).
- Rolling out to another brand = add its handle to `enabled_handles` in the customiser. Check the brand collection actually contains its wrench/kits products first (auto-hide covers gaps).
- `Weights for Irons` (4 products) and `Shaft Adapter` could become extra sub-carousel blocks later — same pattern.
- Wrench carousels often render 1 card in a 3-col row — expected.

Related: [[southern-ropes]] (separate client, same playbook).

## Client brand data sheet (Aug 2026 PDF) — target matrix

Client's per-brand category ticks (uniform layout = 7 auto-hiding carousels: driver, fairway, hybrid, irons, putters, kits, wrenches — wrenches/kits ticked for ALL brands):

| Brand | drv | fwy | hyb | irn | put | wr | kit |
|---|---|---|---|---|---|---|---|
| TaylorMade, Ping, PXG | Ping/PXG only have irons ✓; all three full woods+putters ✓ |
| Callaway, Titleist, Srixon, Mizuno, Honma | woods ✓, no putters/irons |
| Scotty Cameron, Odyssey, LAB, Toulon Design | putters only |
| Cobra | woods + putters, no irons |

Simulated against live data: **9/13 brands match exactly** with the wrench-collection fill. Wrench carousel pulls from `collections['golf-club-wrench']` (12 products: 5 Universal Wrench vendor + brand wrenches for TaylorMade/Scotty/Odyssey/Ping), brand's own vendor first then Universal fill — this is what makes "wrenches on every brand page" true.

**Client tagging gaps (carousels auto-appear when fixed in admin):**
- PXG: no woods product tagged `hybrid`
- Srixon: no `fairway` or `hybrid` tags
- Mizuno, Honma: no `hybrid` tags
- LAB, Mizuno, Honma: no kit products/`weight kit` tags (client ticked kits)

**LAB collection title is "Head Weights for Lab Putters"** — handled by the `brand_overrides` section setting (`lab:LAB`), which fixes the H1/headings without renaming the live collection.

**Open client question from the sheet**: "Fairway/Fairway Wood/Fairway Metal?" — we defaulted to "fairway wood weights" (dominant search phrasing); tag matching uses substring `fairway` so it works regardless.

Sub-carousel matching is **AND** semantics (type AND tag when both set), e.g. driver = `Weights for Woods` + tag `driver` (keeps driver-tagged shaft adapters out). New block settings: `source_collection` (alternate product pool) and `vendor_match` (brand-first + Universal fill).
