# Golfweights.co.uk — TaylorMade enhanced collection layout

**Client**: Golfweights.co.uk (golf club weights retailer, Shopify — Wetheme/Flow-based theme, NOT Dawn). Related to the earlier golf-weights de-cannibalisation project.

**Job**: Rebuild `/collections/taylormade` as a merchandised category page — H1 + 2-row featured carousel + three H2 sub-carousels (putter weights, driver weights, wrenches) + two text/image split blocks — without touching the live theme.

## Where it landed (Aug 2026)

Work happens in a **draft theme called "new cat"** (theme id 196541677952). Two theme files, canonical copies in `golfweights/` in this repo:

- `sections/enhanced-collection.liquid` — the whole layout in one section. Gated by a **hardcoded handle check** (`collection.handle == 'taylormade'`), not a metafield and not a `collection.enhanced.json` template. That route failed repeatedly: Shopify only lists templates from the *published* theme in the collection's Theme-template dropdown, so a draft-theme template can't be assigned. Handle-check + editing the default `templates/collection.json` sidesteps it entirely and previews fine via the draft-theme Preview URL.
- `templates/collection.json` — default collection template with the enhanced section inserted between header and grid, **all 5 blocks pre-configured in the JSON** (so no customiser block-clicking), and header `show_title`/`show_description` false (kills the duplicate hero text).

## Validated facts (don't re-derive)

- Product card snippet is `grid-view-item` — render it directly for pixel-match cards.
- TaylorMade collection: 42 products. Product types: `Weights for Woods` (27), `Weights for Putters` (11), `Shaft Adapter` (3), `Wrench` (1). Filter values in the template match these exactly.
- Storefront filtering exposes `filter.p.product_type` and `filter.p.vendor`; **filtered URLs already canonicalise to the parent collection** (verified live) — so sub-carousel "view all" links use `?filter.p.product_type=…` with zero cannibalisation risk. No subcollections needed.
- Swing weight guide lives at `/pages/swing-weight-guide` (split-block CTA target).
- Shopify section schema `name` and preset names max 25 chars (FileSaveError otherwise); theme file paths can't contain spaces.
- Richtext settings in JSON templates must be wrapped in `<p>…</p>` or the save fails.

## Gotchas / open items

- Split blocks show placeholder grey boxes until Joe picks images (customiser → Enhanced collection → block → Image). Canonical liquid uses core `image_url | image_tag` for robustness.
- `Shaft Adapter` (3 products) could be a 4th sub-carousel if the client wants it.
- Rollout to more brands = duplicate the handle check (`or collection.handle == '…'`) or revisit the metafield approach *after* the theme is published.
- Wrench carousel renders 1 card in a 3-col row (only 1 wrench product) — fine, wide-card look.

Related: [[southern-ropes]] (separate client, same playbook).
