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
  <div class="kicker"><span>A perpetual programme</span><span>&middot;</span><b>366 days, 366 films</b><span>&middot;</span><span>Every one set on its date</span></div>
  <h1>The Massive<br>Movie <em>Calendar</em></h1>
  <p class="standfirst">One film for every day of the year &mdash; each one either <em>about</em> that date or with its story demonstrably taking place on it. Dog Day Afternoon on 22 August. Bloomsday on the 16th of June. Judgment Day on 29 August 1997. Pick a day.</p>
</header>

<section class="today" id="todayCard" aria-label="Today's film"></section>

<div class="controls">
  <input type="search" id="q" placeholder="Search a film, a date, an event&hellip;" aria-label="Search the calendar">
  <button id="fA" aria-pressed="false" title="The date is stated on screen, or the film depicts that day's real event">Exact</button>
  <button id="fB" aria-pressed="false" title="Strong internal or historical evidence">Strong</button>
  <button id="fC" aria-pressed="false" title="Anniversary or thematic pick">Thematic</button>
  <button id="rand">Random day</button>
  <button id="jumpToday">Today</button>
  <span class="count" id="count"></span>
</div>

<main id="year"></main>

<footer>
  <h3>How the picks were made</h3>
  <ul>
    <li><b>Exact</b> &mdash; the date appears on screen (a title card, a diary, an essay heading) or the film is built around the real event of that day. 252 of the 366.</li>
    <li><b>Strong</b> &mdash; solid internal or documentary evidence, but you have to know the history to spot it. 62 days.</li>
    <li><b>Thematic</b> &mdash; an anniversary, a birth, a premiere or a feast day. Flagged honestly rather than dressed up as something firmer. 52 days.</li>
    <li>Alternates are listed on every card. Several days have three or four legitimate claimants &mdash; 15 August alone carries Belfast, Woodstock, VJ Day and Indian independence.</li>
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
const TIERNAME = {A:"Exact",B:"Strong",C:"Thematic"};
const byDate = Object.fromEntries(CAL.map(e => [e.date, e]));
const pad = n => String(n).padStart(2,"0");
const now = new Date();
const todayKey = pad(now.getMonth()+1) + "-" + pad(now.getDate());
const longDate = k => { const [m,d] = k.split("-"); return Number(d) + " " + MONTHS[Number(m)-1]; };

/* ---------- year grid ---------- */
const year = document.getElementById("year");
let html = "";
for (let m = 1; m <= 12; m++) {
  const entries = CAL.filter(e => e.date.startsWith(pad(m)));
  html += '<section class="month" id="m'+m+'"><div class="mhead"><h3>'+MONTHS[m-1]+
          '</h3><span class="mn">'+entries.length+' days</span></div><div class="days">';
  for (const e of entries) {
    const d = Number(e.date.slice(3));
    html += '<button class="day t-'+e.tier+(e.date===todayKey?" is-today":"")+'" data-k="'+e.date+
            '"><span class="n"><span>'+MONTHS[m-1].slice(0,3).toUpperCase()+" "+d+
            '</span><span class="pip"></span></span><span class="t">'+esc(e.title)+
            '</span><span class="y">'+e.year+'</span></button>';
  }
  html += "</div></section>";
}
year.innerHTML = html;
function esc(s){ return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

/* ---------- today ---------- */
const t = byDate[todayKey] || byDate["01-01"];
document.getElementById("todayCard").innerHTML =
  '<div class="datebox"><div><div class="dmon">'+MONTHS[Number(todayKey.slice(0,2))-1]+
  '</div><div class="dnum">'+Number(todayKey.slice(3))+'</div></div>'+
  '<div class="dmon">Confidence &mdash; '+TIERNAME[t.tier]+'</div></div>'+
  '<div class="filmbox"><div class="nowshow">Now showing &mdash; today’s film</div>'+
  '<h2>'+esc(t.title)+' <span class="yr">'+t.year+'</span></h2><p>'+esc(t.why)+'</p>'+
  (t.alt ? '<div class="altline"><span>Also on this date</span>'+esc(t.alt)+'</div>' : '')+'</div>';

/* ---------- modal ---------- */
const dlg = document.getElementById("dlg");
let current = todayKey;
function open(k){
  const e = byDate[k]; if(!e) return; current = k;
  document.getElementById("dDate").textContent = longDate(k);
  document.getElementById("dTier").textContent = TIERNAME[e.tier];
  document.getElementById("dTier").className = "tag t-"+e.tier;
  document.getElementById("dTitle").innerHTML = esc(e.title)+' <span class="yr">'+e.year+'</span>';
  document.getElementById("dWhy").textContent = e.why;
  document.getElementById("dAltWrap").style.display = e.alt ? "" : "none";
  document.getElementById("dAlt").textContent = e.alt || "";
  if (!dlg.open) dlg.showModal();
}
function step(n){
  const keys = CAL.map(e => e.date);
  const i = keys.indexOf(current);
  open(keys[(i + n + keys.length) % keys.length]);
}
year.addEventListener("click", ev => {
  const b = ev.target.closest(".day"); if (b) open(b.dataset.k);
});
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
const tierBtns = {A:document.getElementById("fA"), B:document.getElementById("fB"), C:document.getElementById("fC")};
const active = new Set();
function apply(){
  const term = q.value.trim().toLowerCase();
  let shown = 0;
  for (const el of year.querySelectorAll(".day")) {
    const e = byDate[el.dataset.k];
    const tierOK = active.size === 0 || active.has(e.tier);
    const hay = (e.title+" "+e.year+" "+e.why+" "+(e.alt||"")+" "+longDate(e.date)+" "+e.date).toLowerCase();
    const textOK = !term || hay.includes(term);
    const ok = tierOK && textOK;
    el.classList.toggle("dim", !ok);
    el.classList.toggle("hit", ok && !!term);
    if (ok) shown++;
  }
  countEl.textContent = shown === 366 ? "366 days" : shown + " of 366 days";
}
q.addEventListener("input", apply);
for (const [k,b] of Object.entries(tierBtns)) b.onclick = () => {
  active.has(k) ? active.delete(k) : active.add(k);
  b.setAttribute("aria-pressed", active.has(k));
  apply();
};
document.getElementById("rand").onclick = () => open(CAL[Math.floor(Math.random()*CAL.length)].date);
document.getElementById("jumpToday").onclick = () => {
  const el = year.querySelector('[data-k="'+todayKey+'"]');
  if (el) { el.scrollIntoView({behavior:"smooth", block:"center"}); el.focus(); }
};
apply();
</script>'''

open('massive-movie-calendar.html','w').write(HEAD + BODY.replace('__DATA__', DATA))
print('written', len(HEAD+BODY)+len(DATA), 'bytes')
