# Brief: write Surfer-optimised copy for all Golfweights brand pages

You are writing the on-page copy for 13 brand collection pages on golfweights.co.uk (UK golf club weights retailer, Shopify). The page template is already built; your job is to produce the text that fills its fixed copy slots, optimised in Surfer, one page per brand. Use the Surfer MCP tools (create a content editor per page, pull its terms/NLP guidelines, draft against them, check the content score).

## The brands and which sections each page has

Every page has the same skeleton; sections only appear where the brand has matching products. Write copy ONLY for the sections listed per brand:

| Brand (collection handle) | driver | fairway | hybrid | irons | putters | kits | wrenches |
|---|---|---|---|---|---|---|---|
| TaylorMade (taylormade) | Y | Y | Y | — | Y | Y | Y |
| Callaway (callaway) | Y | Y | Y | — | — | Y | Y |
| Titleist (titleist) | Y | Y | Y | — | — | Y | Y |
| Ping (ping) | Y | Y | Y | Y | Y | Y | Y |
| Scotty Cameron (scotty-cameron) | — | — | — | — | Y | Y | Y |
| Odyssey (odyssey) | — | — | — | — | Y | Y | Y |
| Cobra (cobra) | Y | Y | Y | — | Y | Y | Y |
| PXG (pxg) | Y | Y | Y* | Y | Y | Y | Y |
| Srixon (srixon) | Y | Y* | Y* | — | — | Y | Y |
| LAB — write as "LAB", not the collection title (lab) | — | — | — | — | Y | Y* | Y |
| Toulon Design (toulondesign) | — | — | — | — | Y | Y | Y |
| Mizuno (mizuno) | Y | Y | Y* | — | — | Y* | Y |
| Honma (honma) | Y | Y | Y* | — | — | Y* | Y |

`*` = section pending a product-tagging fix on the client side — write the copy anyway so it's ready.

## Surfer setup per page

- Primary keyword: `[brand] golf club weights` (e.g. "taylormade golf club weights"). Location: United Kingdom, desktop.
- Add secondary keywords matching the sections the brand has: `[brand] driver weights`, `[brand] fairway wood weights`, `[brand] hybrid weights`, `[brand] iron weights`, `[brand] putter weights`, `[brand] golf weight kits`, `[brand] wrench`.
- Configure the outline to mirror the fixed heading structure below so scoring aligns, then work the Surfer term/NLP suggestions into the body slots and FAQ answers. Do not stuff — every sentence must read like a specialist retailer wrote it.

## Fixed heading structure (do not change; already in the template)

- H1: `[Brand] Golf Club Weights`
- H2: `All [Brand] products`
- H2: `Shop by model`
- H2 per category: `[Brand] driver weights` · `[Brand] fairway wood weights` · `[Brand] hybrid weights` · `[Brand] iron weights` · `[Brand] putter weights`
- H2: `[Brand] golf weight kits` (dark feature band)
- H2: `[Brand] club wrenches`
- H2 ×2: the two bottom text boxes (see global slots — headings ARE editable and are a good place for heading keywords)
- H2: `[Brand] golf club weights — FAQs`, with each FAQ question as an H3 (questions are editable — use them for heading-keyword coverage Surfer wants)

## Copy slots and length limits

### Per-brand slots (deliver one set per brand; these are pasted into Shopify collection metafields)

| Slot (metafield key) | Sits under | Length | What it should say |
|---|---|---|---|
| `intro` | the H1 | 40–60 words, 1–2 short paragraphs | The page's thesis: largest UK range of aftermarket head weights for [brand] clubs, name 3–4 flagship model families, gram range, UK stock/same-day dispatch. Primary keyword in the first sentence. |
| `featured_intro` | H2 All [Brand] products | 15–30 words, 1–2 sentences | What the range covers as a whole. |
| `models_intro` | H2 Shop by model | 10–20 words, 1 sentence | Invite users to jump to their model's weights. |
| `driver_intro` | H2 [Brand] driver weights | 15–35 words | Effect of driver head weights (launch, spin, shot shape) + name the brand's driver families. |
| `fairway_intro` | H2 [Brand] fairway wood weights | 15–35 words | Same pattern for fairway woods. |
| `hybrid_intro` | H2 [Brand] hybrid weights | 15–35 words | Same pattern for hybrids/rescues. |
| `irons_intro` (Ping, PXG only) | H2 [Brand] iron weights | 15–35 words | Consistent swing weight through the set. |
| `putter_intro` | H2 [Brand] putter weights | 15–35 words | Feel/balance/stability + the brand's putter families. |
| `wrench_intro` | H2 [Brand] club wrenches | 15–30 words | You need a torque wrench; brand + universal options stocked. |
| `faqs` | H2 FAQ section | 4–6 Q&As; questions 5–10 words (H3), answers 30–60 words | Prioritise question-format keywords from Surfer/PAA. Always cover: fitment ("which weights fit my [brand] driver/putter?"), gram choice, wrench requirement, genuine-vs-aftermarket, delivery. Format as H3 + paragraph(s). One internal link per answer max (swing weight guide `/pages/swing-weight-guide`, delivery `/pages/delivery-returns`). |

Notes:
- Rendered line width is ~68 characters; section intros should be at most ~2 rendered lines. Respect the word counts.
- British English. No em-dash-heavy AI cadence; write like a knowledgeable club fitter.
- Never invent product claims (no "official", "licensed", "OEM parts"). These are aftermarket weights engineered to fit — say exactly that when relevant.
- Model names per brand: read them from the collection's products (titles) before writing so the families named are real (e.g. TaylorMade: Qi 35, Qi 10, Stealth 2, Spider Tour, TP Collection; Ping: G430, G425, PLD…). Do not guess model names.

### Global slots (write ONCE, using the literal token `[brand]` where the brand name belongs — the template substitutes it per page)

| Slot | Format | Length | Notes |
|---|---|---|---|
| Kit band H2 + body | H2 + paragraph + CTA label | H2 5–8 words containing "[brand] golf weight kits"; body 30–50 words | The "one box, every gram" pitch: test weights until the setup feels right; case + wrench included where true. |
| Bottom text box 1 (swing weight guide) | H2 + paragraph + CTA label | H2 5–9 words — put a heading keyword here (e.g. "Dial in your [brand] swing weight"); body 35–55 words | Explains swing weight and points to the guide. |
| Bottom text box 2 (trust/why us) | H2 + paragraph + CTA label | H2 5–9 words; body 35–55 words | UK stock, fast dispatch, engineered to match OEM spec, thousands of golfers. |
| How-it-works steps ×3 | step title 3–5 words + 15–25 word body each | — | Pick your model → choose your grams → one turn of the wrench. |
| Default FAQs ×5 | as per-brand FAQs | — | Generic versions with [brand] tokens, used until a brand's own `faqs` metafield is written. |

## Deliverable format

One markdown file per brand named `[handle]-copy.md`, each slot clearly labelled with its metafield key and the copy ready to paste (FAQs as `<h3>Question</h3><p>Answer</p>` blocks). Plus one `global-copy.md` for the global slots. Finish each brand by reporting its Surfer content score and the top unused terms you consciously left out (with one-line reasons).

## Order of work

TaylorMade first (it's the pilot page), then Ping, Callaway, Titleist, Cobra, Scotty Cameron, Odyssey, then the rest. If Surfer quota or time is a concern, stop after any brand — each file is independently useful.
