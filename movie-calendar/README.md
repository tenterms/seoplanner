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
  "kind": "about", "focus": "day",
  "why": "Sonny Wortzik's fourteen-hour bank siege in Gravesend, Brooklyn, 22 August 1972...",
  "alt": "Michael Collins — killed at Béal na Bláth, 22 August 1922; Richard III — Bosworth Field..."
}
```

Open days carry `open: true`, no title, and a `candidate` string holding the rejected pitch.

## The rule

A film earns a date three ways. Genre is irrelevant — a war film that happens on one day
counts exactly as much as a comedy that does.

- **On screen** — the date is stated in the film. *The Breakfast Club* heads Brian's essay
  Saturday, March 24, 1984. *Psycho* opens on FRIDAY, DECEMBER THE ELEVENTH. *Akira*'s first
  card is 16 July 1988. *The Texas Chain Saw Massacre* reads its date out like a bulletin.
- **The film is that day** — the whole picture takes place on it: *Dog Day Afternoon*,
  *Groundhog Day*, *Zulu*, *Peterloo*, *United 93*.
- **Holiday** — a fixed calendar date: Bonfire Night, Bloomsday, May Day, Christmas Eve.

Each entry is also marked by **focus**: `day` (the film takes place on the date) or `spine`
(a longer film built around it — *Oppenheimer*, *Apollo 13*, *Zero Dark Thirty*). The tool's
*Whole film is that day* filter shows only the first kind.

## What the rule costs

| | days |
|---|---|
| The film takes place on the date | 91 |
| The date is the film's spine | 163 |
| **Open — nothing qualifies** | **112** |

Held honestly, the year does not fill, and each round of scrutiny makes it fill less. That is
the finding, not a failure of searching.

Four classes of pick have been removed:

1. **Anniversaries (60 days).** Conan Doyle's birthday, Mozart's, the night *Metropolis*
   premiered. A film about a man is not set on the day he was born.
2. **Lives with the date inside them (44 days).** *Bohemian Rhapsody* has twenty minutes of
   Live Aid inside fifteen years. Plucking a biography's climax picks a spoiler, not a setting.
3. **Films that only end on the date (13 days).** *La Bamba*, *Mata Hari*, *The Red Baron*,
   *Cool Runnings*, *The Assassination of Jesse James* — the date is where the story stops.
4. **Records of an occasion (2 days).** *A Queen Is Crowned* and *Grenfell*.

Four entries survive with an `ending: true` flag and are labelled **ends here** in the tool —
*Goodfellas* among them. Its date is captioned and it spends twenty-five minutes inside that
day, but the day is still where Henry Hill's story stops. Marked rather than hidden, so the
judgement is visible.

## Where the remaining weakness is

- **The 166 spine days are the soft middle** and the main upgrade path. A film running three
  hours around a date is doing less work than one running ninety minutes on it.
- **Open days are growing, not shrinking.** Every audit finds more picks that do not hold. Plan
  for the number to rise before it falls.
- **Floating holidays are absent by design** — Easter, Thanksgiving and Mother's Day have no
  fixed date.
- **Two entries share a film** — *Back to the Future*, on 26 October 1985 and 12 November 1955,
  because it stamps both on screen.

## Form as evidence

Some films cannot be anywhere but their own day, because the form forbids it. A time loop, a
real-time film or a single unbroken take is self-evidencing in a way no plot summary is. Eleven
entries carry a `form` field (`loop`, `realtime`, `onetake`) and the tool filters on it.

| date | film | form |
|---|---|---|
| 2 February | Groundhog Day | loop |
| 12 February | Before I Fall | loop |
| 6 April | 1917 | one take |
| 21 June | Cléo from 5 to 7 | real time |
| 22 July | Utøya: July 22 | one take, real time |
| 18 September | Happy Death Day | loop |
| 9 November | Palm Springs | loop |
| 15 January · 22 August · 11 September · 11 October | Sully, Dog Day Afternoon, United 93, Saturday Night | real time |

**One-take does not imply datable.** *Rope*, *Victoria*, *Locke*, *Birdman*, *Timecode*,
*The Guilty* and *Boiling Point* are all continuous or real-time and none names a date, so none
can be placed. The same is true of most single-day films: *Clerks*, *Friday*, *Do the Right
Thing*, *Falling Down*, *Training Day*, *Collateral*, *After Hours* and *12 Angry Men* are all
one day and all undatable. The form narrows the field; it does not fill the calendar.

## Best remaining seams

- **More loops.** *The Map of Tiny Perfect Things*, *Naked*, *ARQ*, *Boss Level* and *12:01*
  are loops whose dates were not verifiable here. Each would be a top-grade entry if one exists.
- **Fixed-date folk horror**, which gave up *Saint* (5 December) and *The Wicker Man* (May Day).
- **Holiday horror** clusters heavily on dates already filled, but the long tail is unexplored.

Community sources remain unreachable from this environment: Reddit, Letterboxd list pages and
ResetEra all return 403. Letterboxd's *Dating the Movies* monthly lists carry a curator's note
giving the exact date for each film — roughly 350 human-verified picks. Opening those twelve
pages in a browser and pasting the notes is still the single highest-value hour anyone could
spend on this dataset.

## Sources

Built from film knowledge, then corrected against the 2019 r/movies thread that started the
project and Letterboxd's *Dating the Movies: January* list. Both supplied picks now in the
set: *Psycho* (11 December), *The Wicker Man* (May Day), *Before Sunrise* (Bloomsday),
*Gone Girl* (5 July), *Akira* (16 July), *The Texas Chain Saw Massacre* (18 August),
*Friday the 13th* (13 June), *Rosemary's Baby* (25 June), *The Crow* (Devil's Night),
*Cloverfield* (22 May), *An Affair to Remember* (1 July), *The Time Machine* (5 January).

Ivan Walters' book *A Year of Movies: 365 Films to Watch on the Date They Happened* covers the
same ground and has not been consulted — it is the obvious next cross-check.
