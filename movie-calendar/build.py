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

/* ---- key ---- */
.key{background:var(--sheet);border:1px solid var(--edge);box-shadow:var(--shadow);
  padding:20px 22px 16px;margin:0 0 28px}
.key h2{font-size:22px;margin-bottom:12px}
.key .krow{display:grid;grid-template-columns:110px 1fr;gap:10px;align-items:baseline;
  padding:7px 0;border-top:1px dotted var(--edge)}
.key .krow:first-of-type{border-top:none}
.key .krow p{margin:0;color:var(--ink-2);font-size:15px}
.key .krow p b{color:var(--ink)}
.key .kex{color:var(--mute);font-size:13.5px}
.key .knote{margin:12px 0 0;padding-top:10px;border-top:1px solid var(--edge);
  color:var(--mute);font-size:13.5px}
@media(max-width:560px){.key .krow{grid-template-columns:1fr;gap:2px}}

/* ---- grade badges ---- */
.gb{font-family:"IBM Plex Mono",monospace;font-size:9px;letter-spacing:.1em;font-weight:600;
  padding:1px 4px;border-radius:2px;border:1px solid var(--edge);color:var(--mute);line-height:1.5}
.gb-P1{background:var(--amber);border-color:var(--amber);color:var(--ground)}
.gb-P2{border-color:var(--amber);color:var(--amber)}
.gb-P3{border-color:var(--mute);color:var(--ink-2)}
.gb-P4{border-style:dashed;border-color:var(--mute);color:var(--mute)}
.gb-P5{border-style:dashed;border-color:var(--ticket);color:var(--ticket)}

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
.g-P4 .t,.g-P5 .t{font-weight:500}
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
.gradeline{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--mute);
  padding:6px 22px 0;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.navrow{display:flex;gap:8px;padding:0 22px 20px}
.closeX{border:none;background:none;font-size:20px;line-height:1;padding:2px 6px;color:var(--mute)}
footer{border-top:2px solid var(--ink);margin-top:40px;padding-top:18px;color:var(--mute);font-size:14px}
footer h3{font-size:18px;margin-bottom:8px;color:var(--ink)}
footer ul{margin:0;padding-left:18px}
footer li{margin-bottom:7px}
footer .gb{font-size:10px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>'''

BODY = r'''
<div class="wrap">
<header class="mast">
  <div class="kicker"><span>A film for every day of the year</span><span>&middot;</span><b>All 366 days</b><span>&middot;</span><span>Every pick graded for how honestly it earns its date</span></div>
  <h1>The Massive<br>Movie <em>Calendar</em></h1>
  <p class="standfirst">A film for every day of the year, chosen by one rule: the film has to <em>happen</em> on the date. Sometimes the film says the date out loud. Sometimes it appears on a title card, a diary page, a newspaper, or a gravestone. And sometimes the whole film simply takes place on that one day.</p>
  <p class="standfirst" style="margin-top:10px">Not every date has a film that truly lives on it, so every pick carries a grade for how honestly it earns its day. P1 is the real thing; P5 is an admitted stretch. Click any day to see the film, the evidence, and the other films with a claim on the date.</p>
</header>

<section class="today" id="todayCard" aria-label="Today's film"></section>

<section class="key" aria-label="How to read the grades">
  <h2>How to read the grades</h2>
  <div class="krow"><span class="gb gb-P1">P1 PURE</span><p><b>The whole film takes place on this date, and the date is in the film.</b> <span class="kex">Groundhog Day is 2 February, over and over. Halloween is Haddonfield on 31 October. <span id="c1"></span> days.</span></p></div>
  <div class="krow"><span class="gb gb-P2">P2 ANCHORED</span><p><b>The date is in the film, and the film is built around that day.</b> <span class="kex">The Karate Kid trains for the tournament whose date hangs on the arena banner. <span id="c2"></span> days.</span></p></div>
  <div class="krow"><span class="gb gb-P3">P3 UNSPOKEN</span><p><b>The film takes place on this day, but never says the date.</b> It comes from history or from fans' research. <span class="kex">Dog Day Afternoon is one Brooklyn afternoon, 22 August 1972; the newspapers dated it, the film never does. <span id="c3"></span> days.</span></p></div>
  <div class="krow"><span class="gb gb-P4">P4 GLIMPSED</span><p><b>The date appears in the film, but the film doesn't stay on that day.</b> A caption, a prop, a line of dialogue. <span class="kex">Zodiac captions one 1969 attack to the day, then spans two decades. <span id="c4"></span> days.</span></p></div>
  <div class="krow"><span class="gb gb-P5">P5 BORROWED</span><p><b>The date isn't in the film at all.</b> It comes from a novel, a fan calendar, or a tradition. An honest stretch, marked in red. <span class="kex">Hot Fuzz on St George's Day. <span id="c5"></span> days.</span></p></div>
  <p class="knote">Two smaller markers. <b>Ends here</b> means the film finishes on its date, so reading the entry is mildly spoilery. <b>Loop / real time / one take</b> marks films whose very form ties them to a single day: a time loop, a real-time story, or one unbroken take.</p>
</section>

<div class="controls">
  <input type="search" id="q" placeholder="Search a film, a date, an event&hellip;" aria-label="Search the calendar">
  <button id="g1" data-g="P1" aria-pressed="false" title="The whole film takes place on this date, and the date is in the film">P1 Pure</button>
  <button id="g2" data-g="P2" aria-pressed="false" title="The date is in the film, and the film is built around that day">P2 Anchored</button>
  <button id="g3" data-g="P3" aria-pressed="false" title="The film takes place on this day, but never says the date">P3 Unspoken</button>
  <button id="g4" data-g="P4" aria-pressed="false" title="The date appears in the film, but the film doesn't stay on that day">P4 Glimpsed</button>
  <button id="g5" data-g="P5" aria-pressed="false" title="The date isn't in the film; it comes from a novel, a fan calendar, or a tradition">P5 Borrowed</button>
  <button id="fform" aria-pressed="false" title="Time loops, real-time films and single-take films: forms that tie a film to a single day">Loop / real time / one take</button>
  <button id="rand">Random day</button>
  <span class="count" id="count"></span>
</div>

<main id="year"></main>

<footer>
  <h3>House rules</h3>
  <p style="max-width:66ch;margin:0 0 14px">The grades do the honesty; these rules did the choosing. They are the difference between this calendar and a list of release dates.</p>
  <ul>
    <li><b>An anniversary is not a setting.</b> A film about Mozart is not set on the day Mozart was born. Dozens of tempting picks fell to this rule alone.</li>
    <li><b>A life is not a day.</b> Biopics love to end on a famous date, but a film that spends two hours getting somewhere is not set there. When a biopic's date survives here, it survives at a lower grade, and the entry says why.</li>
    <li><b>Watch the film, not the poster.</b> Every date was checked against what is actually on screen where possible. Scripts and props hold surprises: The Game's screenplay carries an October date that turns out to be the draft's registration stamp, and Forrest Gump's gravestone contradicts its own dialogue.</li>
    <li><b>One film, one day.</b> The only exceptions are Back to the Future and Cloverfield, which each stamp two different dates on screen and so hold two days each.</li>
    <li><b>Every day lists its rivals.</b> Open any entry and you'll find the other films with a claim on that date, including the rejected ones and the reasons. If you can beat a P4 or a P5 with something purer, the argument is ready for you.</li>
  </ul>
  <p style="max-width:66ch;margin:14px 0 0">Sources, gratefully argued with: the r/movies thread that started this idea; the <em>Dating the Movies</em> lists on Letterboxd; Ivan Walters's book <em>A Year of Movies: 365 Films to Watch on the Date They Happened</em> (2016); Choekaas's 366-film video calendar; and the @DatesInMovies account. Each of them got at least one date wrong, which is why no date here rests on any single source's word.</p>
</footer>
</div>

<dialog id="dlg"><div class="card">
  <div class="top"><span class="dt" id="dDate"></span>
    <span style="display:flex;gap:8px;align-items:center"><span class="gb" id="dGrade"></span>
    <button class="closeX" id="dClose" aria-label="Close">&times;</button></span></div>
  <h2 id="dTitle"></h2>
  <div class="gradeline" id="dGradeLine"></div>
  <div class="body"><p id="dWhy"></p>
    <div class="altline" id="dAltWrap"><span>Other films with a claim on this date</span><span id="dAlt"></span></div>
  </div>
  <div class="navrow"><button id="dPrev">&larr; Previous day</button><button id="dNext">Next day &rarr;</button></div>
</div></dialog>

<script>
const CAL = __DATA__;
const MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"];
const GRADE = {P1:"Pure", P2:"Anchored", P3:"Unspoken", P4:"Glimpsed", P5:"Borrowed"};
const GDESC = {
  P1:"Pure: the whole film takes place on this date, and the date is in the film.",
  P2:"Anchored: the date is in the film, and the film is built around that day.",
  P3:"Unspoken: the film takes place on this day, but never says the date. It comes from history or from fans' research.",
  P4:"Glimpsed: the date appears in the film, in a caption, a prop or a line, but the film doesn't stay on that day.",
  P5:"Borrowed: the date isn't in the film. It comes from a novel, a fan calendar, or a tradition."};
const FORM = {loop:"Time loop", realtime:"Real time", onetake:"One take"};
const byDate = Object.fromEntries(CAL.map(e => [e.date, e]));
const pad = n => String(n).padStart(2,"0");
const now = new Date();
const todayKey = pad(now.getMonth()+1) + "-" + pad(now.getDate());
const longDate = k => { const [m,d] = k.split("-"); return Number(d) + " " + MONTHS[Number(m)-1]; };
const esc = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
for (const g of ["P1","P2","P3","P4","P5"]) {
  const n = CAL.filter(e => e.grade === g).length;
  const c = document.getElementById("c"+g[1]); if (c) c.textContent = n;
  const f = document.getElementById("f"+g[1]); if (f) f.textContent = n;
}

/* ---------- year grid ---------- */
const year = document.getElementById("year");
let html = "";
for (let m = 1; m <= 12; m++) {
  html += '<section class="month"><div class="mhead"><h3>'+MONTHS[m-1]+
          '</h3><span class="mn" data-mn="'+m+'"></span></div><div class="days">';
  for (const e of CAL.filter(x => x.date.startsWith(pad(m)))) {
    const d = Number(e.date.slice(3));
    html += '<button class="day g-'+e.grade+(e.date===todayKey?" is-today":"")+'" data-k="'+e.date+
            '"><span class="n"><span>'+MONTHS[m-1].slice(0,3).toUpperCase()+" "+d+
            '</span><span class="gb gb-'+e.grade+'">'+e.grade+'</span></span><span class="t">'+
            esc(e.title)+'</span><span class="y">'+e.year+'</span></button>';
  }
  html += "</div></section>";
}
year.innerHTML = html;

/* ---------- today ---------- */
const t = byDate[todayKey];
document.getElementById("todayCard").innerHTML =
  '<div class="datebox"><div><div class="dmon">'+MONTHS[Number(todayKey.slice(0,2))-1]+
  '</div><div class="dnum">'+Number(todayKey.slice(3))+'</div></div>'+
  '<div class="dmon"><span class="gb gb-'+t.grade+'">'+t.grade+' '+GRADE[t.grade].toUpperCase()+'</span>'+
  (t.form ? ' &middot; ' + FORM[t.form] : '') + (t.ending ? ' &middot; ends here' : '')+'</div></div>'+
  '<div class="filmbox"><div class="nowshow">Today&rsquo;s film</div>'+
  '<h2>'+esc(t.title)+' <span class="yr">'+t.year+'</span></h2><p>'+esc(t.why)+'</p>'+
  (t.alt ? '<div class="altline"><span>Other films with a claim on this date</span>'+esc(t.alt)+'</div>' : '')+
  '</div>';

/* ---------- modal ---------- */
const dlg = document.getElementById("dlg");
let current = todayKey;
function open(k){
  const e = byDate[k]; if(!e) return; current = k;
  document.getElementById("dDate").textContent = longDate(k);
  const gtag = document.getElementById("dGrade");
  gtag.textContent = e.grade + " " + GRADE[e.grade].toUpperCase();
  gtag.className = "gb gb-" + e.grade;
  document.getElementById("dTitle").innerHTML = esc(e.title)+' <span class="yr">'+e.year+'</span>';
  document.getElementById("dGradeLine").textContent = GDESC[e.grade] +
    (e.form ? " · " + FORM[e.form] : "") + (e.ending ? " · ends here" : "");
  document.getElementById("dWhy").textContent = e.why;
  const wrap = document.getElementById("dAltWrap");
  wrap.style.display = e.alt ? "" : "none";
  document.getElementById("dAlt").textContent = e.alt || "";
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
const gradeBtns = [...document.querySelectorAll("[data-g]")];
const formBtn = document.getElementById("fform");
let formOnly = false;
const active = new Set();
function apply(){
  const term = q.value.trim().toLowerCase();
  const perMonth = {};
  let shown = 0;
  for (const el of year.querySelectorAll(".day")) {
    const e = byDate[el.dataset.k];
    const gradeOK = (active.size === 0 || active.has(e.grade)) && (!formOnly || !!e.form);
    const hay = (e.title+" "+e.year+" "+e.grade+" "+e.why+" "+(e.alt||"")+" "+longDate(e.date)).toLowerCase();
    const ok = gradeOK && (!term || hay.includes(term));
    el.classList.toggle("dim", !ok);
    el.classList.toggle("hit", ok && !!term);
    if (ok) { shown++; const m = Number(e.date.slice(0,2)); perMonth[m] = (perMonth[m]||0)+1; }
  }
  for (const el of year.querySelectorAll("[data-mn]")) el.textContent = (perMonth[el.dataset.mn]||0) + " shown";
  countEl.textContent = shown + " of 366 days";
}
q.addEventListener("input", apply);
for (const b of gradeBtns) b.onclick = () => {
  const g = b.dataset.g;
  active.has(g) ? active.delete(g) : active.add(g);
  b.setAttribute("aria-pressed", active.has(g)); apply();
};
formBtn.onclick = () => { formOnly = !formOnly; formBtn.setAttribute("aria-pressed", formOnly); apply(); };
document.getElementById("rand").onclick = () => open(CAL[Math.floor(Math.random()*CAL.length)].date);
apply();
</script>'''

open('massive-movie-calendar.html','w').write(HEAD + BODY.replace('__DATA__', DATA))
print('written')
