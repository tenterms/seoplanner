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
| The film takes place on the date | 87 |
| The date is the film's spine | 177 |
| **Open — nothing qualifies** | **102** |

Held honestly, the year does not fill. That is the finding, not a failure of searching.

Three classes of pick were removed to get here:

1. **Anniversaries (60 days).** Conan Doyle's birthday, Mozart's, the night *Metropolis*
   premiered. A film about a man is not set on the day he was born.
2. **Lives with the date inside them (44 days).** *Bohemian Rhapsody* has twenty minutes of
   Live Aid inside fifteen years. *Malcolm X*, *Milk* and *Selena* simply end on their date.
   Plucking a biography's climax picks a spoiler, not a setting.
3. **Records of an occasion (2 days).** *A Queen Is Crowned* and *Grenfell* — a newsreel and a
   memorial artwork. Worthy; not movies set on a date.

Every open day carries the best pitch that was rejected for it, in the `candidate` field, so
the argument starts from something rather than nothing.

## Where the remaining weakness is

- **The 177 spine days are the soft middle.** Each is defensible, but a film that runs three
  hours around a date is doing less work than one that runs ninety minutes *on* it. Replacing
  spine days with day days is the main upgrade path.
- **Copy still spoils in places.** The rewrite favours setups over climaxes, but any entry
  whose date is a real event carries the ending in the history. Flagging spoiler-bearing
  entries would let readers opt out.
- **Floating holidays are absent by design** — Easter, Thanksgiving and Mother's Day have no
  fixed date, so *The Last Waltz* sits on 25 November because that is the real date of the
  concert, not because Thanksgiving lives there.
- **Two entries share a film** — *Back to the Future*, on 26 October 1985 and 12 November 1955,
  because it stamps both on screen.

## Sources

Built from film knowledge, then corrected against the 2019 r/movies thread that started the
project and Letterboxd's *Dating the Movies: January* list. Both supplied picks now in the
set: *Psycho* (11 December), *The Wicker Man* (May Day), *Before Sunrise* (Bloomsday),
*Gone Girl* (5 July), *Akira* (16 July), *The Texas Chain Saw Massacre* (18 August),
*Friday the 13th* (13 June), *Rosemary's Baby* (25 June), *The Crow* (Devil's Night),
*Cloverfield* (22 May), *An Affair to Remember* (1 July), *The Time Machine* (5 January).

Ivan Walters' book *A Year of Movies: 365 Films to Watch on the Date They Happened* covers the
same ground and has not been consulted — it is the obvious next cross-check.
