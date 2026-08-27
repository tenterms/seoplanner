# The Massive Movie Calendar

A film for every one of the 366 days of the year. The rule: the film must either be
*about* that date, or its story must demonstrably take place on it.

**Live tool:** https://claude.ai/code/artifact/c6abda6f-7d1f-482a-9bec-579dc95115c2

## Files

| File | What it is |
|---|---|
| `massive-movie-calendar.html` | The interactive tool. Self-contained, no build step, no external JS. |
| `data/calendar.json` | The dataset — 366 records, the source of truth. |
| `data/calendar.csv` | Same data, flat, for spreadsheets. |
| `data/{jan…dec}.json`, `data/fills*.json` | Working files the merged set was built from. Kept for auditability. |
| `build.py` | Regenerates the HTML from `data/calendar.json`. Run `python3 build.py`. |

## Record shape

```json
{
  "date": "08-22",
  "title": "Dog Day Afternoon",
  "year": 1975,
  "tier": "A",
  "why": "Sonny Wortzik's fourteen-hour bank siege in Gravesend, Brooklyn, 22 August 1972...",
  "alt": "Michael Collins — killed at Béal na Bláth, 22 August 1922; Richard III — Bosworth Field..."
}
```

`wildcard: true` appears on the handful of entries chosen for an anniversary rather than a setting.

## Confidence tiers

Every entry is graded, and the grade is shown in the tool. This is the honest part.

- **A — Exact (252 days).** The date is stated on screen (a title card, a diary entry, an essay
  heading, a police report) or the film is structurally built around the real event of that day.
  *The Breakfast Club* dates Brian's essay Saturday, March 24, 1984. *Goodfellas* captions
  Sunday, May 11th, 1980. *Sully* is 15 January 2009 from end to end.
- **B — Strong (62 days).** Solid internal or documentary evidence, but you need the history to
  see it. *The Sound of Music* on 12 March for the Anschluss; *Ferris Bueller* on 5 June 1985,
  which is fan-derived from the Cubs fixture and the attendance records.
- **C — Thematic (52 days).** An anniversary, a birth, a premiere or a feast day. Flagged as such
  rather than dressed up. These are the days where nothing better exists — 10 January, 22 March,
  27 March and 22 December are the weakest in the set.

## Where this is thin, and what would fix it

1. **The C tier is the work list.** 52 days are carried by an anniversary rather than a setting.
   Every one of them is a candidate for replacement if a better-evidenced film turns up.
2. **The original crowdsourcing is unread.** The 2019 r/movies thread this project came from is
   behind Reddit's bot protection from this environment (403 on the JSON endpoint, old.reddit,
   and every mirror tried). Reading it from a browser session would likely upgrade a dozen C-tier
   days in an afternoon — it is the single highest-value next step.
3. **Cross-check sources exist but are also blocked here.** Ivan Walters' book *A Year of Movies:
   365 Films to Watch on the Date They Happened*, Letterboxd's *Dating the Movies* monthly lists
   (`letterboxd.com/crew/list/dating-the-movies-{month}/`) and IMDb list `ls530968289` all cover
   the same ground and would confirm or contradict the picks here.
4. **Floating holidays are handled as fixed dates.** Thanksgiving sits on 25 November because that
   is the real date of *The Last Waltz* and the *Rocky II* rematch, not because Thanksgiving is
   always the 25th. Easter is not represented at all.
5. **Days with several legitimate claimants** are resolved in the `why` field and the loser is
   listed in `alt`. 15 August carries Belfast, Woodstock, VJ Day and Indian independence;
   14 February carries the massacre, *Sleepless in Seattle* and *Raging Bull*. A future version
   could let the reader pick which strand they want.
6. **Two entries use the same film** — *Back to the Future*, on 26 October 1985 and 12 November
   1955, because the film stamps both dates on screen. Everything else is unique.

## If this becomes a public tool

The dataset is the moat, not the code. Worth considering:

- A URL per day (`/august-22/`) so each date can rank on its own — that is 366 indexable pages off
  one dataset, and "what movie is set on [date]" is a real long-tail query family.
- Poster art and streaming availability per entry would turn it from a reference into a destination.
- A submission form. The Reddit thread proved people enjoy arguing about this; the arguments are
  free content and free corrections.
