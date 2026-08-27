import json
cal = json.load(open('data/calendar.json'))
DATA = json.dumps(cal, ensure_ascii=False, separators=(',',':'))

HEAD = r'''<title>The Massive Movie Calendar</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@500;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{
  --ground:#E6E5DF; --sheet:#F4F3EE; --tile:#FBFAF6; --edge:#CFCDC4;
  --ink:#15181E; --ink-2:#3C424B; --mute:#70757E;
  --amber:#B9762A; --amber-soft:#E9A03C; --ticket:#B8362A;
  --shadow:0 1px 0 rgba(21,24,30,.06), 0 8px 22px -14px rgba(21,24,30,.35);
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --ground:#0E1116; --sheet:#151A21; --tile:#1B212A; --edge:#2C343F;
  --ink:#E9E7DE; --ink-2:#BFC3C9; --mute:#878E98;
  --amber:#E9A03C; --amber-soft:#F0B863; --ticket:#E0574A;
  --shadow:0 1px 0 rgba(0,0,0,.4), 0 10px 26px -16px rgba(0,0,0,.9);
}}
:root[data-theme="dark"]{
  --ground:#0E1116; --sheet:#151A21; --tile:#1B212A; --edge:#2C343F;
  --ink:#E9E7DE; --ink-2:#BFC3C9; --mute:#878E98;
  --amber:#E9A03C; --amber-soft:#F0B863; --ticket:#E0574A;
  --shadow:0 1px 0 rgba(0,0,0,.4), 0 10px 26px -16px rgba(0,0,0,.9);
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font-family:"Newsreader",Georgia,serif;font-size:16px;line-height:1.55;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 90px}
h1,h2,h3,.sign{font-family:"Big Shoulders Display","Arial Narrow",sans-serif;font-weight:800;
  letter-spacing:.01em;text-transform:uppercase;text-wrap:balance;margin:0}
.mono{font-family:"IBM Plex Mono",ui-monospace,monospace;font-variant-numeric:tabular-nums}

/* ---- masthead ---- */
header.mast{border-bottom:2px solid var(--ink);margin-bottom:26px;padding:34px 0 16px}
.kicker{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.22em;
  text-transform:uppercase;color:var(--mute);display:flex;gap:14px;flex-wrap:wrap;align-items:baseline}
.kicker b{color:var(--amber);font-weight:600}
h1{font-size:clamp(46px,10.5vw,116px);line-height:.84;margin:14px 0 12px}
h1 em{font-style:normal;color:var(--amber);display:block}
.standfirst{max-width:60ch;color:var(--ink-2);font-size:17px;margin:0 0 4px}

/* ---- today card ---- */
.today{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:0;
  background:var(--sheet);border:1px solid var(--edge);border-top:3px solid var(--amber);
  box-shadow:var(--shadow);margin:26px 0 40px}
@media(max-width:720px){.today{grid-template-columns:1fr}}
.today .datebox{padding:26px 26px 22px;border-right:1px solid var(--edge);display:flex;
  flex-direction:column;justify-content:space-between;gap:18px}
@media(max-width:720px){.today .datebox{border-right:0;border-bottom:1px solid var(--edge)}}
.datebox .dnum{font-family:"Big Shoulders Display",sans-serif;font-weight:800;
  font-size:clamp(70px,15vw,132px);line-height:.78;letter-spacing:-.01em}
.datebox .dmon{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--mute)}
.today .filmbox{padding:26px}
.nowshow{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--amber);margin-bottom:10px}
.today h2{font-size:clamp(30px,5.2vw,52px);line-height:.92}
.today .yr{color:var(--mute);font-weight:500}
.today p{margin:12px 0 0;color:var(--ink-2);max-width:62ch}
.altline{margin-top:14px;padding-top:12px;border-top:1px dotted var(--edge);
  font-size:14px;color:var(--mute)}
.altline span{font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.18em;
  text-transform:uppercase;display:block;margin-bottom:4px}

/* ---- controls ---- */
.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;
  position:sticky;top:0;z-index:20;padding:12px 0;background:var(--ground);
  border-bottom:1px solid var(--edge);margin-bottom:24px}
input[type=search]{font-family:"IBM Plex Mono",monospace;font-size:13px;padding:9px 12px;
  background:var(--tile);color:var(--ink);border:1px solid var(--edge);border-radius:2px;
  min-width:230px;flex:1 1 230px}
input[type=search]:focus-visible,button:focus-visible,.day:focus-visible{outline:2px solid var(--amber);outline-offset:2px}
button{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.12em;
  text-transform:uppercase;padding:9px 12px;background:var(--tile);color:var(--ink-2);
  border:1px solid var(--edge);border-radius:2px;cursor:pointer}
button:hover{color:var(--ink);border-color:var(--ink-2)}
button[aria-pressed="true"]{background:var(--ink);color:var(--ground);border-color:var(--ink)}
.count{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--mute);margin-left:auto}

/* ---- year grid ---- */
.month{margin-bottom:34px}
.mhead{display:flex;align-items:baseline;gap:12px;border-bottom:1px solid var(--ink);
  padding-bottom:5px;margin-bottom:12px}
.mhead h3{font-size:26px;line-height:1}
.mhead .mn{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.2em;
  color:var(--mute);margin-left:auto}
.days{display:grid;grid-template-columns:repeat(auto-fill,minmax(148px,1fr));gap:7px}
.day{position:relative;text-align:left;display:block;padding:8px 9px 9px;min-height:78px;
  background:var(--tile);border:1px solid var(--edge);border-radius:2px;cursor:pointer;
  transition:transform .12s ease,border-color .12s ease,background .12s ease}
.day:hover{transform:translateY(-2px);border-color:var(--ink-2);background:var(--sheet)}
.day .n{font-family:"IBM Plex Mono",monospace;font-size:10.5px;color:var(--mute);
  display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}
.day .t{font-family:"Big Shoulders Display",sans-serif;font-weight:700;font-size:16.5px;
  line-height:.98;text-transform:uppercase;color:var(--ink);
  overflow-wrap:break-word;hyphens:auto;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.day .y{font-family:"IBM Plex Mono",monospace;font-size:10px;color:var(--mute);margin-top:3px}
.pip{width:6px;height:6px;border-radius:50%;display:inline-block}
.k-dated .pip{background:var(--amber)}
.k-about .pip{background:transparent;box-shadow:inset 0 0 0 1.5px var(--amber)}
.k-holiday .pip{background:var(--ticket)}
.f-spine .pip{background:transparent;box-shadow:inset 0 0 0 1.5px var(--mute)}
.is-open{border-style:dashed;background:transparent}
.is-open .t{color:var(--mute);font-weight:500}
.is-open .pip{display:none}
.t-A .pip{background:var(--amber)}
.t-B .pip{background:transparent;box-shadow:inset 0 0 0 1.5px var(--amber)}
.t-C .pip{background:transparent;box-shadow:inset 0 0 0 1.5px var(--mute)}
.day.is-today{border-color:var(--ticket);box-shadow:inset 0 0 0 1px var(--ticket)}
.day.is-today .n::after{content:"TODAY";color:var(--ticket);font-size:9px;letter-spacing:.14em}
.day.dim{opacity:.22;pointer-events:none}
.day.hit{border-color:var(--amber);box-shadow:inset 0 0 0 1px var(--amber)}

/* ---- modal ---- */
dialog{border:none;padding:0;background:transparent;max-width:min(680px,94vw);width:100%}
dialog::backdrop{background:rgba(8,10,14,.62);backdrop-filter:blur(2px)}
.card{background:var(--sheet);border:1px solid var(--edge);border-top:3px solid var(--amber);
  box-shadow:var(--shadow);color:var(--ink)}
.card .top{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;
  padding:20px 22px 0}
.card .dt{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--amber)}
.card h2{font-size:clamp(26px,5vw,42px);line-height:.94;padding:8px 22px 0}
.card h2 .yr{color:var(--mute);font-weight:500}
.card .body{padding:14px 22px 22px}
.card p{margin:0;color:var(--ink-2)}
.tag{font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.14em;
  text-transform:uppercase;padding:4px 7px;border:1px solid var(--edge);border-radius:2px;
  color:var(--mute);white-space:nowrap}
.tag.t-A{color:var(--amber);border-color:var(--amber)}
.navrow{display:flex;gap:8px;padding:0 22px 20px}
.closeX{border:none;background:none;font-size:20px;line-height:1;padding:2px 6px;color:var(--mute)}
footer{border-top:2px solid var(--ink);margin-top:40px;padding-top:18px;color:var(--mute);font-size:14px}
footer h3{font-size:18px;margin-bottom:8px;color:var(--ink)}
footer ul{margin:0;padding-left:18px}
footer li{margin-bottom:5px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>'''

BODY = r'''
<div class="wrap">
<header class="mast">
  <div class="kicker"><span>A perpetual programme</span><span>&middot;</span><b id="kCount"></b><span>&middot;</span><span>Any genre. The date has to be in the film.</span></div>
  <h1>The Massive<br>Movie <em>Calendar</em></h1>
  <p class="standfirst">One film per day, under one rule: the film has to <em>happen</em> on the date. Said out loud, stamped on a title card, written in a diary &mdash; or simply the day the whole picture takes place. Genre is irrelevant. An anniversary is not a setting, and a life with the date somewhere inside it is not either.</p>
  <p class="standfirst" style="margin-top:10px">Held to that, the year does not fill. <b id="sCount"></b> days have a film that takes place entirely on them; another <b id="pCount"></b> have one built around that day as its spine. <b id="oCount"></b> days are open, and each carries the best pitch I could find and reject, so you have something to argue with.</p>
</header>

<section class="today" id="todayCard" aria-label="Today's film"></section>

<div class="controls">
  <input type="search" id="q" placeholder="Search a film, a date, an event&hellip;" aria-label="Search the calendar">
  <button id="fdated" aria-pressed="false" title="The date is spoken or shown on screen">On screen</button>
  <button id="fabout" aria-pressed="false" title="The whole film is that single day">One-day film</button>
  <button id="fholiday" aria-pressed="false" title="A fixed-date holiday">Holiday</button>
  <button id="fopen" aria-pressed="false" title="Days with no qualifying film">Open days</button>
  <button id="strict" aria-pressed="false" title="Only films that take place entirely on the date — hides longer films built around it">Whole film is that day</button>
  <button id="fform" aria-pressed="false" title="Time loops, real-time films and single-take films — the forms that guarantee a film happens on its date">Loop / real time / one take</button>
  <button id="rand">Random day</button>
  <span class="count" id="count"></span>
</div>

<main id="year"></main>

<footer>
  <h3>The rule, and what it costs</h3>
  <p style="max-width:66ch;margin:0 0 14px">A film earns a date three ways. <b>On screen</b> &mdash; the date is stated: Brian's essay is headed Saturday, March 24, 1984; Psycho opens on FRIDAY, DECEMBER THE ELEVENTH; Akira's first card is 16 July 1988. <b>The film is that day</b> &mdash; the whole picture takes place on it: Dog Day Afternoon, Groundhog Day, Zulu, Peterloo. <b>Holiday</b> &mdash; a fixed date: Bonfire Night, Bloomsday, May Day, Christmas Eve.</p>
  <ul>
    <li><b>Genre is not a filter.</b> A war film that happens on one day is exactly as valid as a comedy that does. What matters is whether the day holds the film.</li>
    <li><b>An anniversary is not a setting.</b> Sixty picks came out on this alone &mdash; Conan Doyle's birthday, Mozart's, the night Metropolis premiered. A film about a man is not set on the day he was born.</li>
    <li><b>A life is not a day.</b> Bohemian Rhapsody has twenty minutes of Live Aid inside fifteen years; Malcolm X, Milk and Selena all simply end on their date. Plucking the climax out of a biography picks a spoiler, not a setting. Twenty-six of those are now open days.</li>
    <li><b>Form is the strongest evidence there is.</b> A time loop, a real-time film or a single unbroken take cannot be anywhere but its own day. <em>Cleo from 5 to 7</em> spends ninety minutes of 21 June 1961 in real time; <em>1917</em> opens on its date and never cuts away; <em>Utoya: July 22</em> runs one 72-minute take, the exact length of the attack. Eleven days are held by films like these &mdash; filter for them with <em>Loop / real time / one take</em>. One-take films are not automatically eligible: <em>Rope</em>, <em>Victoria</em>, <em>Locke</em> and <em>Birdman</em> never name a date, so they cannot be placed.</li>
    <li><b>Ending-anchored days are marked "ends here".</b> Goodfellas caption its date and spend real screen time inside it &mdash; but the day is where the story stops, which makes the pick a spoiler as much as a setting. Four survive on that basis and say so. Thirteen more that only ended on their date, from La Bamba to Mata Hari, were removed this round.</li>
    <li><b>Spine days are marked, not hidden.</b> Oppenheimer, Apollo 13 and Zero Dark Thirty run longer than their date but are built around it &mdash; the day is the spine. Press <em>Whole film is that day</em> to see only the strictest set.</li>
    <li><b>A record of an occasion is not a movie.</b> A Queen Is Crowned and Grenfell are both out.</li>
    <li><b>Open days carry their best rejected pitch</b>, so the argument starts from something rather than nothing.</li>
  </ul>
</footer>
</div>

<dialog id="dlg"><div class="card">
  <div class="top"><span class="dt" id="dDate"></span>
    <span style="display:flex;gap:8px;align-items:center"><span class="tag" id="dTier"></span>
    <button class="closeX" id="dClose" aria-label="Close">&times;</button></span></div>
  <h2 id="dTitle"></h2>
  <div class="body"><p id="dWhy"></p>
    <div class="altline" id="dAltWrap"><span>Also on this date</span><span id="dAlt"></span></div>
  </div>
  <div class="navrow"><button id="dPrev">&larr; Previous day</button><button id="dNext">Next day &rarr;</button></div>
</div></dialog>

<script>
const CAL = __DATA__;
const MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"];
const KIND = {dated:"Date on screen", about:"The film is that day", holiday:"Holiday"};
const FORM = {loop:"Time loop", realtime:"Real time", onetake:"One take"};
const byDate = Object.fromEntries(CAL.map(e => [e.date, e]));
const pad = n => String(n).padStart(2,"0");
const now = new Date();
const todayKey = pad(now.getMonth()+1) + "-" + pad(now.getDate());
const longDate = k => { const [m,d] = k.split("-"); return Number(d) + " " + MONTHS[Number(m)-1]; };
const esc = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
const nDay = CAL.filter(e => !e.open && e.focus === "day").length;
const nSpine = CAL.filter(e => !e.open && e.focus === "spine").length;
const nOpen = CAL.filter(e => e.open).length;
document.getElementById("kCount").textContent = (nDay+nSpine) + " days filled, " + nOpen + " open";
document.getElementById("sCount").textContent = nDay;
document.getElementById("pCount").textContent = nSpine;
document.getElementById("oCount").textContent = nOpen;

/* ---------- year grid ---------- */
const year = document.getElementById("year");
let html = "";
for (let m = 1; m <= 12; m++) {
  html += '<section class="month"><div class="mhead"><h3>'+MONTHS[m-1]+
          '</h3><span class="mn" data-mn="'+m+'"></span></div><div class="days">';
  for (const e of CAL.filter(x => x.date.startsWith(pad(m)))) {
    const d = Number(e.date.slice(3));
    const cls = e.open ? "is-open" : ("k-"+e.kind+" f-"+e.focus);
    html += '<button class="day '+cls+(e.date===todayKey?" is-today":"")+'" data-k="'+e.date+
            '"><span class="n"><span>'+MONTHS[m-1].slice(0,3).toUpperCase()+" "+d+
            '</span><span class="pip"></span></span><span class="t">'+
            (e.open ? "Open" : esc(e.title))+'</span><span class="y">'+
            (e.open ? "no qualifying film" : e.year)+'</span></button>';
  }
  html += "</div></section>";
}
year.innerHTML = html;

/* ---------- today ---------- */
const t = byDate[todayKey];
document.getElementById("todayCard").innerHTML =
  '<div class="datebox"><div><div class="dmon">'+MONTHS[Number(todayKey.slice(0,2))-1]+
  '</div><div class="dnum">'+Number(todayKey.slice(3))+'</div></div>'+
  '<div class="dmon">'+(t.open ? "Open date" : KIND[t.kind] + (t.form ? " &mdash; " + FORM[t.form] : "") + (t.ending ? " &mdash; ends here" : ""))+'</div></div>'+
  '<div class="filmbox"><div class="nowshow">'+(t.open?"Nothing qualifies today":"Now showing &mdash; today’s film")+'</div>'+
  (t.open ? '<h2>This date is open</h2><p>'+esc(t.why)+'</p><div class="altline"><span>Best pitch, rejected</span>'+esc(t.candidate||"")+'</div>'
          : '<h2>'+esc(t.title)+' <span class="yr">'+t.year+'</span></h2><p>'+esc(t.why)+'</p>'+
            (t.alt ? '<div class="altline"><span>Also claimed for this date</span>'+esc(t.alt)+'</div>' : ''))+
  '</div>';

/* ---------- modal ---------- */
const dlg = document.getElementById("dlg");
let current = todayKey;
function open(k){
  const e = byDate[k]; if(!e) return; current = k;
  document.getElementById("dDate").textContent = longDate(k);
  const tag = document.getElementById("dTier");
  tag.textContent = e.open ? "Open" : KIND[e.kind] + (e.focus === "spine" ? " · spine" : "") + (e.ending ? " · ends here" : "") + (e.form ? " · " + FORM[e.form] : "");
  tag.className = "tag" + (e.open || e.focus === "spine" ? "" : " t-A");
  document.getElementById("dTitle").innerHTML = e.open ? "This date is open"
      : esc(e.title)+' <span class="yr">'+e.year+'</span>';
  document.getElementById("dWhy").textContent = e.why;
  const wrap = document.getElementById("dAltWrap");
  const label = e.open ? "Best pitch, rejected" : "Also claimed for this date";
  const body = e.open ? (e.candidate||"") : (e.alt||"");
  wrap.style.display = body ? "" : "none";
  wrap.querySelector("span").textContent = label;
  document.getElementById("dAlt").textContent = body;
  if (!dlg.open) dlg.showModal();
}
function step(n){
  const keys = CAL.map(e => e.date);
  open(keys[(keys.indexOf(current) + n + keys.length) % keys.length]);
}
year.addEventListener("click", ev => { const b = ev.target.closest(".day"); if (b) open(b.dataset.k); });
document.getElementById("dClose").onclick = () => dlg.close();
document.getElementById("dPrev").onclick = () => step(-1);
document.getElementById("dNext").onclick = () => step(1);
dlg.addEventListener("click", ev => { if (ev.target === dlg) dlg.close(); });
document.addEventListener("keydown", ev => {
  if (!dlg.open) return;
  if (ev.key === "ArrowRight") { ev.preventDefault(); step(1); }
  if (ev.key === "ArrowLeft")  { ev.preventDefault(); step(-1); }
});

/* ---------- filters ---------- */
const q = document.getElementById("q"), countEl = document.getElementById("count");
const kindBtns = {dated:document.getElementById("fdated"), about:document.getElementById("fabout"),
                  holiday:document.getElementById("fholiday"), open:document.getElementById("fopen")};
const strictBtn = document.getElementById("strict");
const formBtn = document.getElementById("fform");
let formOnly = false;
const active = new Set();
let dayOnly = false;
function apply(){
  const term = q.value.trim().toLowerCase();
  const perMonth = {};
  let shown = 0;
  for (const el of year.querySelectorAll(".day")) {
    const e = byDate[el.dataset.k];
    const bucket = e.open ? "open" : e.kind;
    const histOK = !dayOnly || e.open || e.focus === "day";
    const kindOK = (active.size === 0 || active.has(bucket)) && (!formOnly || !!e.form);
    const hay = ((e.title||"Open")+" "+(e.year||"")+" "+e.why+" "+(e.alt||e.candidate||"")+" "+longDate(e.date)).toLowerCase();
    const ok = histOK && kindOK && (!term || hay.includes(term));
    el.classList.toggle("dim", !ok);
    el.classList.toggle("hit", ok && !!term);
    if (ok) { shown++; const m = Number(e.date.slice(0,2)); perMonth[m] = (perMonth[m]||0)+1; }
  }
  for (const el of year.querySelectorAll("[data-mn]")) el.textContent = (perMonth[el.dataset.mn]||0) + " shown";
  countEl.textContent = shown + " of 366 days";
}
q.addEventListener("input", apply);
for (const [k,b] of Object.entries(kindBtns)) b.onclick = () => {
  active.has(k) ? active.delete(k) : active.add(k);
  b.setAttribute("aria-pressed", active.has(k)); apply();
};
strictBtn.onclick = () => { dayOnly = !dayOnly; strictBtn.setAttribute("aria-pressed", dayOnly); apply(); };
formBtn.onclick = () => { formOnly = !formOnly; formBtn.setAttribute("aria-pressed", formOnly); apply(); };
document.getElementById("rand").onclick = () => open(CAL[Math.floor(Math.random()*CAL.length)].date);
apply();
</script>'''

open('massive-movie-calendar.html','w').write(HEAD + BODY.replace('__DATA__', DATA))
print('written')
