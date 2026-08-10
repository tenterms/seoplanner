---
name: competitor-landscape
description: Generate a SERP-first Competitor Landscape table for a keyword + client domain. Use whenever the user asks for a competitor landscape, competitor report, or "who ranks for X" analysis — e.g. `/competitor-landscape "IT Support Sheffield" aag-it.com`. Fetches live Google rankings (SerpAPI), filters out directories/junk, enriches real businesses with Ahrefs metrics, and returns a completed table with the client's row highlighted.
argument-hint: "<keyword>" <client-domain> [criteria...]
---

# Competitor Landscape Generator (SERP-first)

Port of the Google Apps Script "SERP-FIRST COMPETITOR LANDSCAPE GENERATOR". The SERP is
the source of truth for who competes and at what rank; Ahrefs supplies the strength
metrics; Claude itself does the business-vs-junk classification (replacing Perplexity).

## Inputs

Parse from the arguments (ask only if the keyword or client domain is missing):

- **keyword** — the search term, e.g. `IT Support Sheffield`.
- **client domain** — root domain, e.g. `aag-it.com`. Normalize (strip protocol/`www.`/paths).
- **criteria** (optional) — extra include/exclude guidance, e.g. "exclude national MSPs".
- **country** — default **UK** (`google.co.uk`, `gl=uk`, Ahrefs country `gb`). Honour an
  explicit override (US → `google.com`, `gl=us`, `us`).

Target: **~20 real businesses** in the final table (plus the client's row, always).

## Step 1 — Fetch the SERP (source of truth)

Use `mcp__serpapi__search` with the **`google`** engine (not `google_light` — you need
the local pack):

```json
{"params": {"engine": "google", "q": "<keyword>", "google_domain": "google.co.uk",
            "gl": "uk", "hl": "en", "num": 100}, "mode": "compact"}
```

- Ask for `num: 100` in one call. If Google returns fewer than ~30 organic results,
  paginate with `start: 10/20/...`, `num: 10` (the Apps Script approach) until you have
  30+ or pages come back empty.
- **Local pack** (`local_results.places`): capture on the first page only. Entries with a
  `website` are competitors too — record them with their pack position and mark source
  `local_pack`. Entries without a website are noted but can't be enriched.
- **Organic** (`organic_results`): record `position`, `link`, `title`, `snippet`.

Normalize every URL to a root domain: strip protocol, `www.`, and path; keep multi-part
TLDs intact (`foo.co.uk`, `bar.org.uk` → three labels, not two). Dedupe by root domain,
keeping the **best (lowest) organic position**.

## Step 2 — Classify: real business vs junk

Classify every deduped domain yourself using the title/snippet (WebFetch a homepage only
when genuinely ambiguous). Keep **commercial companies that actually sell the service in
the keyword** (B2B or B2C, local or national). Exclude:

- **Directories/aggregators**: Yell, Cylex, Checkatrade, Bark, Trustpilot, Clutch,
  TechBehemoths, FreeIndex, Yelp, Thomson Local, "top 10 X in Y" listicle sites.
- **Job boards/recruiters**: Indeed, Reed, Totaljobs, CV-Library, agency vacancy pages.
- **Government/education**: `.gov.uk`, `.ac.uk`, councils, universities, colleges.
- **Charities/community groups**, news/blog/press sites, forums (Reddit, Quora),
  course/training providers, Wikipedia, social platforms.
- Apply any user-supplied **criteria** on top.

Be inclusive about commercial businesses, strict about non-commercial. Keep the top ~20
businesses by SERP rank. Record the exclusions (domain + one-word reason) — they go in a
collapsed footnote, not the table.

**Client row**: if the client domain appeared in the SERP, use its real rank. If not,
its rank is "Not in top N" (N = organic results fetched) — still include the row and
still enrich it.

## Step 3 — Enrich with Ahrefs (one batch call)

Single `mcp__Ahrefs__batch-analysis` call for all kept domains + the client
(≤100 targets). Each target: `{"url": "<root domain>", "mode": "subdomains",
"protocol": "both"}` — **`mode` must be `subdomains`** for domains. Set
`country` to `gb` (or the override) so organic metrics are market-specific, and
`volume_mode: "average"`.

```
select: ["url", "domain_rating", "org_traffic", "org_keywords",
         "org_keywords_1_3", "org_keywords_4_10", "refdomains", "backlinks"]
```

Derive **Top 10** = `org_keywords_1_3` + `org_keywords_4_10`; **Top 3** =
`org_keywords_1_3`. (This matches the old report's Ahrefs-CSV columns, with DR added.)

*Optional — Indexed Pages*: the old report's `site:domain` count via SerpAPI. Skip by
default (one API call per domain, flaky counts); add only if the user asks.

## Step 4 — Deliver the table

Output a markdown table in chat, sorted by Current Rank ascending (client row **bold**,
"Not in top N" rows last, sorted by Organic Traffic desc):

| # | Company | Root Domain | Current Rank | DR | Organic Traffic (GB) | Kw Top 100 | Top 10 | Top 3 | Ref. Domains | Backlinks | Notes |

- **Company**: real trading name from the SERP title (not a prettified domain).
- **Notes**: source (`local pack`), specialisation, or anything from the criteria.
- Follow the table with 3–5 bullet takeaways: where the client sits, who the strongest
  competitors are (rank × authority), and any gap worth flagging (e.g. client outranked
  by lower-DR sites → on-page problem; client absent → different analysis needed).
- Name exclusions briefly at the end ("Filtered out: yell.com (directory), …").

**Excel export**: only if the user asks (or asked for multiple keywords) — use the
`xlsx` skill, one tab per keyword, same columns, header fill + freeze panes +
auto-filter per the CLAUDE.md build notes, saved to the working directory.

## Gotchas

- SerpAPI sometimes returns no `local_results` — fine, proceed with organic only.
- Ahrefs `org_traffic` with `country: gb` can be 0 for real but tiny local firms —
  report 0, don't drop the row.
- Same brand on two domains (`.com` + `.co.uk`): keep the one that ranked; note the twin.
- Multiple URLs from one domain in the SERP is a cannibalisation signal for that
  competitor — worth a note, and dedupe to best rank as usual.
