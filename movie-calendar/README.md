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
| The film takes place on the date | 94 |
| The date is the film's spine | 198 |
| **Open — nothing qualifies** | **74** |

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

## The destination test

The question that decides every spine day: **where does the film think it's going?** If the
answer is the date — *Oppenheimer* to Trinity, *Apollo 13* to splashdown, *Argo* to the
airport, *Thirteen Days* through its thirteen — the film stays. If the date is just where a
story about something else stops, it goes.

That test removed, this round: *Goodfellas* (a caption and twenty-five great minutes, at the
end of twenty-five years), *The Social Network* (a timestamped first act, then seven years of
depositions), *Zodiac* (the most precise date captions in cinema, spread across two decades),
*Darkest Hour* (checked against its own script it runs 9 May–4 June 1940 and was never a
10 May film), *At Eternity's Gate*, *The Cranes Are Flying*, *Rosemary's Baby* (a nine-month
film whose date never reaches the screen), and — the audit's best catch — *Gallipoli*, which
everyone remembers as an Anzac Day film although the charge at the Nek was **7 August 1915**;
it is now an alternate on the date it actually depicts, and 25 April is honestly open.

Promotions from the same pass, each verified:

- **14 February — Picnic at Hanging Rock.** The opening card: "On Saturday 14th February 1900
  a party of schoolgirls from Appleyard College picnicked at Hanging Rock…"
- **21 April — The Fog.** "One hundred years ago, on the 21st of April…" — Antonio Bay's
  centennial day, witching hour to fog-out.
- **30 December — Strange Days.** The penultimate day of 1999; the film is this day and the next.
- **31 December — The Phantom Carriage.** The last sinner to die before midnight drives Death's
  carriage; the whole film sits inside the year's final hour. *When Harry Met Sally* moves to
  the alternates, where the ends-at-the-party films live.
- **6 June — The Longest Day.** The title is the claim; *Saving Private Ryan* runs a week past
  the 6th and steps down to alternate.
- **15 March — Julius Caesar (1953).** "The ides of March are come." The date is dialogue.
- **23 February — Twin Peaks: Fire Walk with Me.** Laura's last week, dated by series canon
  worked backwards from the pilot — flagged as fan arithmetic, like Ferris Bueller's 5 June.

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

## The Walters cross-check

Ivan Walters' *A Year of Movies: 365 Films to Watch on the Date They Happened* (Rowman &
Littlefield, 2016) was read in full and parsed into `data/walters-year-of-movies.json` —
all 365 picks, alternates, and his killer feature: a **"Date Revealed in Film"** timestamp
for every entry where the date appears on screen.

His rule is looser than ours — one scene on the date qualifies — so most of his picks are
what we'd grade scene-level. But the timestamps are primary-source evidence, and fourteen of
his picks pass our destination test. All fourteen adopted, with his timestamps in the copy:

The Great Raid (29 Jan) · Charlie and the Chocolate Factory (1 Feb — the tour is dated on
screen at 31:13 and then fills two-thirds of the runtime) · Love Affair (8 Feb) · The Song of
Bernadette (11 Feb) · **Planet of the Apes (27 Mar — Taylor's hibernation log reads "Earth
date March 27, 2673", making this the calendar's only twenty-seventh-century entry)** ·
A Passage to India (3 Apr) · A Matter of Life and Death (3 May) · In the Heat of the Night
(13 Sep — the murder night is dated on screen at 14:09) · The Greatest Game Ever Played
(19 Sep) · Air Force One (23 Sep) · Frequency (15 Oct) · Henry V '44 (24 Oct — Olivier gets
the eve of Agincourt, Branagh keeps the day) · Battleground (22 Dec — the "NUTS!" day) ·
Lethal Weapon (23 Dec, handing off to Die Hard on the 24th).

His remaining picks are quoted in the open days' candidate notes, including his own reader's-
note confession that *Excalibur* was the one film he "forced" into a date. His Blade Runner
filing (8 January, against the film's own "November 2019" card) is flagged as disputed.

## The world-cinema pass

The calendar was anglophone-skewed, so the full 1001 Movies list was swept with the same rules.
The headline negative finding: world cinema's masterpieces are overwhelmingly calendar-free —
Ozu, Bresson, Tarkovsky, Kiarostami, Wong (mostly), Bergman (mostly) never date a frame.
But thirteen date-anchored exceptions came through, and several fixed the weakest squares:

- **6 Jan — The Dead** (Epiphany night, one evening; Spotlight steps down to alternate)
- **3 Feb — Serpico** (opens inside the ambulance, 3 February 1971)
- **20 Mar — The White Balloon** (the last ninety minutes before Nowruz, near real time)
- **25 Apr — 1900** (the Liberation Day frame — the square Gallipoli falsely occupied)
- **8 May — Ashes and Diamonds** (VE Day 1945 in one Polish town, one day and night)
- **12 Jun — Bus 174** (the Rio hijacking of 12 June 2000, live footage of one afternoon)
- **27 Jun — The Battleship Potemkin** (the mutiny, 27 June 1905 new style)
- **25 Jul — The Conformist** (present tense: the night Mussolini falls)
- **10 Aug — The Night of the Shooting Stars** (San Lorenzo night, in the title)
- **21 Sep — Grave of the Fireflies** ("September 21, 1945. That was the night I died.")
- **7 Oct — Son of Saul** (a day and a half, ending in the Sonderkommando revolt)
- **10 Oct — Tokyo Olympiad** (the ceremony that became a national holiday)
- **16 Nov — Children of Men** (the newscast is dated 16 November 2027 — verified)

Plus some thirty world-cinema alternates: Chungking Express's 1 May pineapple tins, Z on
22 May, Some Like It Hot fleeing the Valentine's massacre, Le Samouraï's captioned 4 April
alibi, the Umbrellas of Cherbourg Esso-station Christmas Eve, Mishima's 25 November present
tense, the Marriage of Maria Braun ending on the Miracle of Bern, and The Big Lebowski's
Ralphs check post-dated 11 September 1991.

## The deep-research round

`RESEARCH.md` now documents which channels work from an agent environment and which
need a human browser. The screenplay-grep channel (IMSDb, fetchable by curl) produced
primary-source dialogue evidence; the Walters alternates and Wikipedia holiday lists
produced the rest. Seven adoptions: Black Sunday (shot at the real Super Bowl X, 18 Jan
1976), The Buccaneer (restored after a wrongful deletion), Good Night and Good Luck
(the 9 March 1954 broadcast), K-PAX ("July 27, at 5:51 a.m."), The Damned United
(Clough's 44 days end 12 Sept 1974), Knowing (a film that is a countdown to its own
date, 19 Oct 2009), The Caine Mutiny (the charge sheet recites 18 December 1944).
One demotion the rules demanded: The China Syndrome's claim was a release-date
coincidence with Three Mile Island, not a setting — the square is open and says so.

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
