# Golfweights brand pages — client handover

Everything needed to review, roll out and maintain the new brand collection pages. Three parts: **(1)** the metafield values per brand for sense-checking, **(2)** the checklist for adding new products, **(3)** how to switch the layout on across all brands.

All model lists below were generated from your live product tags and verified — every model line matches real products. Nothing here changes the live site until the "new cat" theme is published.

---

## 1 · Metafield values per brand

Each brand collection gets two metafield values now (Products → Collections → *brand* → Metafields). The Surfer-written copy (intros, FAQs) is a separate workstream and slots into further metafields later.

**Overview for sense-checking:**

| Brand page | Sections that will appear | Fit-finder clubs (model chips) | Weight range shown in hero |
|---|---|---|---|
| **TaylorMade** (`taylormade`) | Driver · Fairway · Hybrid · Putters · Kits · Wrenches | Driver (16) · Fairway (7) · Hybrid (4) · Putter (7) | 2g–38g |
| **Ping** (`ping`) | Driver · Fairway · Hybrid · Irons · Putters · Kits · Wrenches | Driver (6) · Fairway (6) · Hybrid (6) · Iron (1) · Putter (1) | 2g–39g |
| **Callaway** (`callaway`) | Driver · Fairway · Hybrid · Kits · Wrenches | Driver (11) · Fairway (11) · Hybrid (3) | 2g–23g |
| **Titleist** (`titleist`) | Driver · Fairway · Hybrid · Kits · Wrenches | Driver (9) · Fairway (6) · Hybrid (2) | 2g–25g |
| **Cobra** (`cobra`) | Driver · Fairway · Hybrid · Putters · Kits · Wrenches | Driver (7) · Fairway (6) · Hybrid (6) · Putter (1) | 3g–35g |
| **PXG** (`pxg`) | Driver · Fairway · Irons · Putters · Kits · Wrenches | Driver (3) · Fairway (3) · Iron (1) · Putter (3) | 2.5g–20g |
| **Scotty Cameron** (`scotty-cameron`) | Putters · Kits · Wrenches | Putter (10) | 5g–45g |
| **Odyssey** (`odyssey`) | Putters · Kits · Wrenches | Putter (7) | 4g–35g |
| **Srixon** (`srixon`) | Driver · Kits · Wrenches | Driver (3) | 4g–23g |
| **LAB** (`lab`) | Putters · Wrenches | Putter (3) | 2.5g–16g |
| **Toulon Design** (`toulondesign`) | Putters · Kits · Wrenches | Putter (2) | 5g–25g |
| **Mizuno** (`mizuno`) | Driver · Fairway · Wrenches | Driver (2) · Fairway (2) | 3g–20g |
| **Honma** (`honma`) | Driver · Fairway · Wrenches | Driver (3) · Fairway (3) | 5g–19g |

Sections not listed for a brand simply don't render there — no configuration needed. Wrenches appear on every page because universal wrenches fill in where a brand has no own-brand wrench.

### Values to paste per brand

For each brand below: **Models** goes into the `custom.models` metafield (format per line: `Chip label | product tag | club types`), **Weight range** into `custom.gram_range`.

#### TaylorMade (`/collections/taylormade`)

**Weight range:** `2g–38g`

**Models:**

```
Qi 35 | qi 35 | driver,fairway,hybrid
Qi 10 | qi 10 | driver,fairway,hybrid
Qi4D | qi4d | driver,fairway,hybrid
Stealth 2 | stealth 2 | driver,hybrid
Stealth | stealth | driver,fairway
SIM2 | sim 2 | driver
SIM Max | sim max | driver
Spider Tour | spider tour | putter
Spider X | spider x | putter
Spider EX | spider ex | putter
Spider GTX Max | spider gtx max | putter
Spider Mini & FCG | spider fcg | putter
TP Collection | tp collection | putter
Hydroblast & Truss | truss | putter
BRNR Mini | brnr | driver
M6 | m6 | driver
M5 | m5 | driver
M4 | m4 | driver,fairway
M3 | m3 | driver,fairway
M2 | m2 | driver
M1 | taylormade m1 | driver
R1-R11 Series | r9 | driver,fairway
R7 Quad | r7 quad | driver
```

*Verified chips (product counts): driver: Qi 35(2), Qi 10(2), Qi4D(2), Stealth 2(2), Stealth(1), SIM2(1), SIM Max(1), BRNR Mini(1), M6(1), M5(1), M4(1), M3(1), M2(2), M1(1), R1-R11 Series(1), R7 Quad(2) — fairway: Qi 35(2), Qi 10(2), Qi4D(2), Stealth(1), M4(1), M3(1), R1-R11 Series(1) — hybrid: Qi 35(2), Qi 10(2), Qi4D(2), Stealth 2(2) — putter: Spider Tour(3), Spider X(1), Spider EX(1), Spider GTX Max(1), Spider Mini & FCG(2), TP Collection(4), Hydroblast & Truss(2)*

#### Ping (`/collections/ping`)

**Weight range:** `2g–39g`

**Models:**

```
G440 | g440 | driver,fairway,hybrid
G430 | g430 | driver,fairway,hybrid
G425 | g425 max | driver,fairway,hybrid
G410 | g410 | driver,fairway,hybrid
G400 | g400 | driver,fairway,hybrid
G30 | g30 sf tec | driver,fairway,hybrid
i-Series Irons | i59 | iron
Vault 2.0 Putters | piper | putter
```

*Verified chips (product counts): driver: G440(2), G430(2), G425(2), G410(1), G400(1), G30(1) — fairway: G440(2), G430(2), G425(2), G410(1), G400(1), G30(1) — hybrid: G440(2), G430(2), G425(2), G410(1), G400(1), G30(1) — iron: i-Series Irons(1) — putter: Vault 2.0 Putters(1)*

#### Callaway (`/collections/callaway`)

**Weight range:** `2g–23g`

**Models:**

```
Elyte | elyte | driver,fairway,hybrid
Ai Smoke | ai smoke | driver,fairway
Paradym | paradym | driver,fairway,hybrid
Quantum | quantum max | driver,fairway,hybrid
Rogue | rogue | driver,fairway
Rogue ST | rogue st max d | driver,fairway
Epic Speed | epic speed | driver,fairway
Epic Max | epic max | driver,fairway
Epic Flash | epic flash | driver,fairway
Mavrik | mavrik | driver,fairway
Big Bertha | big bertha | driver,fairway
Apex Hybrids | apex | hybrid
XR16 & Great Big Bertha | great big bertha | driver,fairway
```

*Verified chips (product counts): driver: Elyte(2), Paradym(2), Quantum(2), Rogue(2), Rogue ST(1), Epic Speed(2), Epic Max(3), Epic Flash(2), Mavrik(2), Big Bertha(3), XR16 & Great Big Bertha(2) — fairway: Elyte(1), Ai Smoke(1), Paradym(2), Rogue(1), Rogue ST(1), Epic Speed(1), Epic Max(1), Epic Flash(1), Mavrik(2), Big Bertha(3), XR16 & Great Big Bertha(1) — hybrid: Elyte(1), Quantum(1), Apex Hybrids(1)*

#### Titleist (`/collections/titleist`)

**Weight range:** `2g–25g`

**Models:**

```
GT Series | gt2 | driver,fairway,hybrid
GT3 | gt3 | driver,fairway,hybrid
TSR | tsr2 | driver,fairway
TSi | tsi2 | driver,fairway
TSi3 | tsi3 | driver
TS2 & TS4 | ts2 | driver,fairway
TS3 | ts3 | driver
TS1 | ts1 | driver
GTS | gts | driver,fairway
```

*Verified chips (product counts): driver: GT Series(2), GT3(2), TSR(2), TSi(1), TSi3(1), TS2 & TS4(1), TS3(1), TS1(1), GTS(2) — fairway: GT Series(2), GT3(3), TSR(2), TSi(1), TS2 & TS4(1), GTS(2) — hybrid: GT Series(1), GT3(2)*

#### Cobra (`/collections/cobra`)

**Weight range:** `3g–35g`

**Models:**

```
DS Adapt | ds adapt | driver,fairway,hybrid
Darkspeed | darkspeed | driver,fairway,hybrid
Aerojet | aerojet | driver,fairway,hybrid
LTDx | ltdx | driver,fairway,hybrid
Radspeed | radspeed | driver,fairway,hybrid
Speedzone | king sz speedzone | driver,fairway,hybrid
OPTM | optm | driver,fairway,hybrid
King Vintage & 3D | vintage | putter
```

*Verified chips (product counts): driver: DS Adapt(2), Darkspeed(2), Aerojet(2), LTDx(2), Radspeed(2), Speedzone(1), OPTM(2) — fairway: DS Adapt(3), Aerojet(1), LTDx(1), Radspeed(1), Speedzone(1), OPTM(2) — hybrid: DS Adapt(1), Aerojet(1), LTDx(1), Radspeed(1), Speedzone(1), OPTM(2) — putter: King Vintage & 3D(2)*

#### PXG (`/collections/pxg`)

**Weight range:** `2.5g–20g`

**Models:**

```
Black Ops | black ops | driver,fairway
0811 Gen4-6 | gen5 | driver,fairway
0211 | 0211 | driver,fairway
0311 Irons | 0311 t | iron
Battle Ready | battle ready | putter
Blackjack | blackjack | putter
Gunboat | gunboat | putter
```

*Verified chips (product counts): driver: Black Ops(2), 0811 Gen4-6(2), 0211(2) — fairway: Black Ops(2), 0811 Gen4-6(2), 0211(2) — iron: 0311 Irons(1) — putter: Battle Ready(2), Blackjack(2), Gunboat(2)*

#### Scotty Cameron (`/collections/scotty-cameron`)

**Weight range:** `5g–45g`

**Models:**

```
Newport | newport series | putter
Phantom X | phantom x | putter
Futura | futura series | putter
Golo | golo series | putter
Select | select | putter
Special Select | special select | putter
Studio Select | studio select | putter
California | california series | putter
Concept X | concept x | putter
Del Mar | del mar | putter
```

*Verified chips (product counts): putter: Newport(26), Phantom X(26), Futura(26), Golo(26), Select(16), Special Select(15), Studio Select(17), California(26), Concept X(14), Del Mar(15)*

#### Odyssey (`/collections/odyssey`)

**Weight range:** `4g–35g`

**Models:**

```
Ai One | ai one | putter
Square 2 Square | square 2 square | putter
Tri-Hot | tri hot | putter
Jailbird | jailbird | putter
2-Ball Ten | 2- ball ten | putter
Seven | seven | putter
Toulon Ai | toulon | putter
```

*Verified chips (product counts): putter: Ai One(5), Square 2 Square(3), Tri-Hot(3), Jailbird(3), 2-Ball Ten(4), Seven(5), Toulon Ai(1)*

#### Srixon (`/collections/srixon`)

**Weight range:** `4g–23g`

**Models:**

```
ZXi | zxi | driver,fairway,hybrid
ZX5 & ZX7 | zx5 | driver,fairway,hybrid
MKI & MKII | mki | driver,fairway,hybrid
```

*Verified chips (product counts): driver: ZXi(2), ZX5 & ZX7(2), MKI & MKII(3)*

#### LAB (`/collections/lab`)

**Weight range:** `2.5g–16g`

**Models:**

```
DF Series | df2 | putter
Mezz | mezz.1 | putter
OZ | oz.1 | putter
```

*Verified chips (product counts): putter: DF Series(1), Mezz(1), OZ(1)*

#### Toulon Design (`/collections/toulondesign`)

**Weight range:** `5g–25g`

**Models:**

```
Toulon 2025 Collection | formula series | putter
Toulon 2022 Series | toulon 22 | putter
```

*Verified chips (product counts): putter: Toulon 2025 Collection(2), Toulon 2022 Series(1)*

#### Mizuno (`/collections/mizuno`)

**Weight range:** `3g–20g`

**Models:**

```
ST-X & ST-Z | st-x | driver,fairway,hybrid
ST-G | st-g 220 | driver,fairway,hybrid
```

*Verified chips (product counts): driver: ST-X & ST-Z(1), ST-G(1) — fairway: ST-X & ST-Z(1), ST-G(1)*

#### Honma (`/collections/honma`)

**Weight range:** `5g–19g`

**Models:**

```
TR20 | tr20 460cc | driver,fairway,hybrid
TW757 | tw757 | driver,fairway,hybrid
T World GS | t world gs | driver,fairway,hybrid
```

*Verified chips (product counts): driver: TR20(1), TW757(1), T World GS(1) — fairway: TR20(1), TW757(1), T World GS(1)*

---

## 2 · Adding a new product — checklist

The page builds itself from three product fields. Get these right and the product appears everywhere automatically — no page edits.

1. **Product type** (exact spelling): `Weights for Woods`, `Weights for Putters`, `Weights for Irons`, `Wrench` or `Shaft Adapter`. This decides which category section the product belongs to.
2. **Club tags** — for `Weights for Woods` products only, tag every club it fits: `driver`, `fairway wood`, `hybrid`. This is what puts it under the right club button in the fit finder and in the right carousels. *A woods product with no club tags is invisible to the finder.*
3. **Model tag** — add the exact tag from the brand's Models list above (e.g. `qi 35`, `g430`, `phantom x`). This puts it under the right model chip and in the Shop-by-model rail. Spelling must match the list exactly.
4. **Kit tag** — if it's a weight kit, tag it `weight kit` (this keeps it in the kits band and the kits collection).
5. **Vendor** = the brand name as it appears on the collection (e.g. `TaylorMade`). This orders brand wrenches ahead of universal ones and powers the kits link.
6. **Add it to the brand's collection** as you do today.

**When a new model family launches** (e.g. a Qi 40 next season): tag the new products with a consistent model tag, then add one line to that collection's Models metafield — `Qi 40 | qi 40 | driver,fairway,hybrid`. The chip, the rail card and the counts appear immediately.

**Currently missing tags** (products invisible to the finder until fixed):

- TaylorMade: "Sim Driver" and "Sim Max-D Driver" have no `driver` tag
- Callaway: "Paradym Ai Smoke Max D…" has no tags at all; the two "Apex Utility Wood" products and "Paradym X Triple Diamond Hybrid" have no club tags
- PXG: "Gen 8 Irons" weights have no tags
- Hybrid/fairway tags to add so those sections appear: PXG (`hybrid`), Srixon (`fairway wood`, `hybrid`), Mizuno (`hybrid`), Honma (`hybrid`)

---

## 3 · Rolling out to all brands

Yes — one hit is safe, because the layout adapts per brand automatically: sections, club buttons and chips only render where that brand has matching products (Scotty Cameron correctly shows a putter-only page with no configuration). And nothing is live until the theme is published.

1. In the **"new cat"** theme customiser, open any brand collection page, click **Enhanced collection** in the sidebar, and set **Enabled collection handles** to:

```
taylormade, ping, callaway, titleist, cobra, pxg, scotty-cameron, odyssey, srixon, lab, toulondesign, mizuno, honma
```

2. Paste each brand's **Models** and **Weight range** values from section 1 into its collection metafields.
3. Review each page on the theme preview (the overview table above says what to expect on each).
4. When happy: publish the "new cat" theme. Rollback is instant — republish the old theme.

Optional per-brand polish, any time after launch: a hero image (`custom.hero_image` metafield, 2400×1200px), and the Surfer-optimised intros and FAQs into the remaining metafields.
