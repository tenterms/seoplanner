# Research channels — what works from an agent environment, and what doesn't

Findings from the deep-research rounds, so future passes don't rediscover them.

## Channels that work

1. **IMSDb screenplay grep (primary source).** `curl` fetches full scripts (no bot wall);
   grep for `Month DD` patterns. Found A Few Good Men's "August 6th" (×8) and Dragon
   Tattoo's "September 21st, 1966" in dialogue. **Warning: title pages carry script DRAFT
   dates** — The Game's "October 19, 1995", Heathers' "November 17, 1987" and Superbad's
   "July 20, 2006" are all registration dates, not settings. Always read the context lines.
   Coverage is patchy (~1,200 scripts; many classics missing).
2. **Wikipedia holiday-film lists** (`List of films set around May Day`, `…New Year`) —
   fetchable, curated, and they cite the in-film evidence.
3. **Published reference books as PDFs.** Walters' *A Year of Movies* yielded 14 adoptions
   plus timestamps. Books beat the open web: someone already did the frame-checking.
4. **Targeted WebSearch verification** of one named claim ("film X date Y") — high accuracy.
   Open-ended searches ("movie set on January 3") are useless noise.
5. **The 1001-list sweep pattern**: take any canon list, judge from film knowledge, verify
   the risky ones. Yield ~1 adoption per 90 titles, but the alternates enrich everything.

## Channels that are blocked from here (need a human browser)

- **Letterboxd** *Dating the Movies* monthly lists (403) — ~350 curated dated picks.
- **Reddit** threads (403 on every route and mirror).
- **@DatesInMovies / CineCalendar on X** — a purpose-built date-per-day account; tweets
  don't reach the search index reliably. An hour of scrolling it would be worth more than
  any automated pass. Their pinned archive, if one exists, is the single best target.
- **ResetEra** thread on the Choekaas 366-scene YouTube video (403), and the video itself.

## Channels not yet tried

- **OpenSubtitles corpus grep** — subtitle files are the film's actual spoken text; an API
  key would allow searching "January 14" across ~million subtitle files. The single most
  scalable idea if the calendar goes public.
- **Frame-checking via the Choekaas video** (a clip for all 366 days, with visible dates).
- **Crowdsourcing on the tool itself** — the original Reddit thread proved people love this
  argument; 100 open days with named rejected pitches is bait, deliberately.
