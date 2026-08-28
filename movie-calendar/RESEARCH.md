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
- **@DatesInMovies / CineCalendar on X** — PARTIALLY CRACKED. The raw timeline is behind
  X's login wall, every Nitter mirror is dead, and web.archive.org is blocked by the egress
  proxy — but Google indexes a few hundred of the account's tweet pages with full text, and
  SerpApi reaches that index. Month-by-month OR-queries over the open days recovered ~60
  usable tweets in one session: six became primaries (Taxi Driver's dated diary, The Karate
  Kid's tournament banner, Turning Red's concert tickets, Idiocracy, Days of Thunder, The
  Fugitive) and ~35 enriched notes. Yield caveat: the account mostly logs PROP dates
  (birthdates on driving licences, newspaper inserts) — evidence-grade for "the date is in
  the film", rarely for "the film happens on the date". And it makes errors: its Trading
  Places date falls on a Sunday when the markets were shut. The un-indexed remainder of the
  timeline still needs a logged-in human scroll.
- **ResetEra** thread on the Choekaas 366-scene YouTube video (403), and the video itself.

## Handoff requests (user offered)

- **Letterboxd page sources**: save the twelve `letterboxd.com/crew/list/dating-the-movies-
  {month}/detail/` pages (the /detail/ view carries the curator's per-film date notes) as
  HTML and drop them in like the Walters PDF. The notes fields are what matter.
- **Choekaas video**: the *description* likely lists all 366 films with dates — worth more
  than the transcript, since the video is a montage of film audio. Copy the description text
  and any pinned comment; a transcript of on-screen date cards would be the bonus.

## Channels not yet tried

- **OpenSubtitles corpus grep** — subtitle files are the film's actual spoken text; an API
  key would allow searching "January 14" across ~million subtitle files. The single most
  scalable idea if the calendar goes public.
- ~~Frame-checking via the Choekaas video~~ — DONE: the project's own 366-film list arrived
  as a PDF (now `data/choekaas-movie-calendar.json`), with its sources — which include the
  original Carphone Warehouse calendar via the Wayback Machine, closing the circle on this
  project's own origin. Three adoptions (Twelve Monkeys, Reversal of Fortune, Silver Linings
  Playbook), ~25 note enrichments, and two caught errors: its Reversal of Fortune date
  confuses Sunny's two comas, and its The Fog filing (9 Dec) contradicts the film's own
  dialogue (21 April).
- **Crowdsourcing on the tool itself** — the original Reddit thread proved people love this
  argument; 100 open days with named rejected pitches is bait, deliberately.
