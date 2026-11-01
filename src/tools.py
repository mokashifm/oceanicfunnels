"""Free tools: Speed to Lead Test."""
import json
from html import escape as E

TOOL_CSS = r"""
.st-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:28px;align-items:start}
.st-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:28px}
.st-card h2{font-size:22px;letter-spacing:-.02em;margin-bottom:6px}
.st-card .hint{font-size:14px;color:var(--muted);margin-bottom:18px}
.st-q{margin-top:20px}
.st-q label.t{display:block;font-family:var(--display);font-weight:600;font-size:15px;color:var(--ink);margin-bottom:8px}
.st-q small{display:block;font-size:13px;color:var(--muted);margin-top:6px}
.st-in{width:100%;box-sizing:border-box;font:inherit;font-size:16px;padding:12px 14px;border:1px solid var(--line);border-radius:8px;background:#fff;color:var(--ink)}
.st-in:focus{outline:2px solid var(--aqua);outline-offset:1px;border-color:var(--aqua-d)}
.st-two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.st-range{display:flex;align-items:center;gap:14px}
.st-range input{flex:1;accent-color:var(--aqua-d)}
.st-range output{font-family:var(--display);font-weight:700;min-width:48px;text-align:right;color:var(--ink)}
.st-checks{display:grid;gap:10px;margin-top:4px}
.st-checks label{display:flex;gap:12px;align-items:flex-start;font-size:15px;line-height:1.45;color:var(--text);padding:12px 14px;border:1px solid var(--line);border-radius:8px;cursor:pointer}
.st-checks label:hover{border-color:var(--aqua-d)}
.st-checks input{margin-top:3px;accent-color:var(--aqua-d);width:18px;height:18px;flex:none}
.st-res{position:sticky;top:20px;background:var(--ink);color:#fff;border-color:var(--ink)}
.st-res h2{color:#fff}
.st-score{display:flex;align-items:center;gap:20px;margin-top:14px}
.st-ring{--p:0;width:118px;height:118px;border-radius:50%;flex:none;display:grid;place-items:center;background:conic-gradient(var(--aqua) calc(var(--p)*1%),rgba(255,255,255,.12) 0)}
.st-ring span{width:92px;height:92px;border-radius:50%;background:var(--ink);display:grid;place-items:center;font-family:var(--display);font-size:36px;font-weight:700;letter-spacing:-.04em}
.st-grade{font-family:var(--display);font-size:20px;font-weight:700;color:var(--aqua)}
.st-gtxt{font-size:15px;line-height:1.5;color:#C9D6D4;margin-top:6px}
.st-nums{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:22px}
.st-nums div{background:rgba(255,255,255,.06);border-radius:10px;padding:14px}
.st-nums b{display:block;font-family:var(--display);font-size:26px;letter-spacing:-.03em;color:#fff}
.st-nums small{font-size:13px;color:#C9D6D4;line-height:1.4;display:block;margin-top:4px}
.st-fix{margin-top:22px}
.st-fix h3{font-size:15px;color:#fff;font-family:var(--display);margin-bottom:8px}
.st-fix ol{padding-left:20px;display:grid;gap:8px;font-size:14.5px;line-height:1.5;color:#E3ECEA}
.st-fix a{color:var(--aqua)}
.st-res .nf-btn{margin-top:22px;width:100%;justify-content:center;box-sizing:border-box;text-align:center}
.st-note{font-size:12.5px;color:#9DB0AD;margin-top:14px;line-height:1.5}
@media (max-width:900px){.st-grid{grid-template-columns:1fr}.st-res{position:static}}
@media (max-width:520px){.st-card{padding:20px}.st-two{grid-template-columns:1fr}.st-score{gap:14px}}
"""

CHECKS = [
    ("auto", "Every new lead gets an automatic text or email within a minute", "/guides/speed-to-lead/", "Send an instant text and email with a booking link the moment a lead arrives."),
    ("hours", "Leads that arrive at night and on weekends get a reply straight away", "/guides/ai-chat-agent-for-business/", "Use an AI agent to answer and book leads outside business hours."),
    ("route", "Each lead is assigned to a person automatically", "/guides/online-booking-calendars/", "Route leads automatically (round robin or by service) so every lead has an owner."),
    ("form", "Our forms ask for 5 fields or fewer", "/guides/speed-to-lead/", "Cut your forms to name, phone, email and one or two qualifying questions."),
    ("calls", "Missed calls get an automatic text back", "/guides/missed-call-text-back/", "Turn on missed call text back so phone leads get a reply in seconds."),
    ("alerts", "My team gets a phone alert for every new lead", "/guides/speed-to-lead/", "Send push or SMS alerts with a tap-to-call link to whoever owns the lead."),
    ("measure", "We check our response times at least once a week", "/guides/marketing-reporting-dashboards/", "Review response times weekly, by person and by lead source."),
]
BANDS = [("40", "Under 1 minute"), ("32", "1 to 5 minutes"), ("18", "5 to 30 minutes"), ("10", "30 to 60 minutes"),
         ("4", "1 to 24 hours"), ("0", "More than a day, or I'm not sure")]

FAQS = [
    ("What is a speed to lead test?", "A speed to lead test checks how fast your business replies to new leads and what slows you down. This free test scores your response time and seven speed to lead practices out of 100, and shows how many leads and how much revenue wait longer than five minutes."),
    ("How is the score calculated?", "Up to 40 points come from your typical first response time, from 40 for under a minute down to 0 for more than a day. The other 60 points are split equally across seven practices: instant automatic replies, after-hours replies, automatic lead routing, short forms, missed call text back, phone alerts and weekly measurement."),
    ("How is revenue at stake worked out?", "It's simple arithmetic from your own numbers: leads per month, multiplied by the share that wait more than five minutes, multiplied by your close rate and average customer value. It shows how much revenue depends on leads that wait. It isn't a prediction of how much you will lose."),
    ("Why five minutes?", "The MIT and InsideSales Lead Response Management Study found the odds of contacting a lead dropped 100 times when the first call was made at 30 minutes instead of 5, which is where the common 5-minute rule comes from."),
    ("Do you store my answers?", "No. The test runs entirely in your browser. Nothing you enter is sent to us or saved."),
]


def speed_to_lead_test(cfg, fonts, logo, page, crumbs_html, faq_schema):
    path = "/tools/speed-to-lead-test/"
    crumbs = [("Home", "/"), ("Speed to Lead Test", path)]
    opts = "".join(f'<option value="{v}"{" selected" if v == "18" else ""}>{E(t)}</option>' for v, t in BANDS)
    checks = "".join(f'<label><input type="checkbox" data-k="{k}"><span>{E(t)}</span></label>' for k, t, _, _ in CHECKS)
    fixes = json.dumps({k: [u, f] for k, _, u, f in CHECKS})
    faq_html = "".join(f'<section><h2>{E(q)}</h2><p>{E(a)}</p></section>' for q, a in FAQS)
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in">
      {crumbs_html(crumbs)}
      <h1>Free Speed to Lead Test</h1>
      <p class="nf-sub"><b>How fast do you really reply to new leads?</b> Answer a few questions to get your speed to lead score out of 100, the leads and revenue that wait more than five minutes, and the fixes that matter most. Free, instant, no sign-up.</p>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:48px">
  <div class="nf-wrap">
    <div class="st-grid">
      <form class="st-card" id="st-form" onsubmit="return false">
        <h2>Your numbers</h2>
        <p class="hint">Rough numbers are fine. Everything stays in your browser.</p>
        <div class="st-q"><label class="t" for="st-band">How long does a new lead usually wait for your first reply?</label>
          <select class="st-in" id="st-band">{opts}</select>
          <small>Not sure? Fill out your own website form tonight and time the reply.</small></div>
        <div class="st-q st-two">
          <div><label class="t" for="st-leads">New leads per month</label><input class="st-in" id="st-leads" type="number" min="0" step="1" value="100" inputmode="numeric"></div>
          <div><label class="t" for="st-value">Average customer value ($)</label><input class="st-in" id="st-value" type="number" min="0" step="1" value="500" inputmode="numeric"></div>
        </div>
        <div class="st-q"><label class="t" for="st-close">Share of leads that become customers</label>
          <div class="st-range"><input id="st-close" type="range" min="1" max="60" value="15"><output id="st-close-o">15%</output></div></div>
        <div class="st-q"><label class="t" for="st-fast">Share of leads that get a reply within 5 minutes</label>
          <div class="st-range"><input id="st-fast" type="range" min="0" max="100" value="30"><output id="st-fast-o">30%</output></div></div>
        <div class="st-q"><span class="t" style="display:block;font-family:var(--display);font-weight:600;font-size:15px;color:var(--ink);margin-bottom:8px">Which of these are true for your business?</span>
          <div class="st-checks">{checks}</div></div>
      </form>
      <div class="st-card st-res" aria-live="polite">
        <h2>Your speed to lead score</h2>
        <div class="st-score"><div class="st-ring" id="st-ring"><span id="st-n">0</span></div>
          <div><div class="st-grade" id="st-grade"></div><p class="st-gtxt" id="st-gtxt"></p></div></div>
        <div class="st-nums">
          <div><b id="st-slow">0</b><small>leads a month wait more than 5 minutes</small></div>
          <div><b id="st-rev">$0</b><small>monthly revenue tied to those leads</small></div>
        </div>
        <div class="st-fix"><h3>Your top fixes</h3><ol id="st-fixes"></ol></div>
        <a class="nf-btn nf-btn--aqua nf-btn--lg" href="/#get-started">Fix my speed to lead</a>
        <p class="st-note">Revenue tied to slow leads = leads × share waiting over 5 minutes × close rate × customer value. It shows what depends on fast replies, not a forecast of losses.</p>
      </div>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:24px">
  <div class="nf-wrap"><article class="nf-doc" style="margin-inline:auto">
    <section><h2>Why speed to lead matters</h2>
    <p>Speed to lead is the time it takes your business to reply after someone fills out a form, calls or messages you. Research has found it makes a big difference:</p>
    <ul>
    <li>A <a href="https://hbr.org/2011/03/the-short-life-of-online-sales-leads" rel="noopener" target="_blank">Harvard Business Review study</a> found firms that replied within an hour were nearly seven times as likely to qualify a lead as those that waited even an hour longer.</li>
    <li>The <a href="https://www.mortech.com/hs-fs/hub/25649/file-13535879-pdf/docs/mit_study.pdf" rel="noopener" target="_blank">MIT and InsideSales Lead Response Management Study</a> found the odds of contacting a lead dropped 100 times when the first call came at 30 minutes instead of 5.</li>
    </ul>
    <p>Read the full <a href="/guides/speed-to-lead/">speed to lead guide</a> for the research, the 7 ways to improve and how to automate replies.</p></section>
    {faq_html}
  </article></div>
</section>
<script>
(function(){{
  var F={fixes};
  function $(i){{return document.getElementById(i)}}
  function money(n){{return "$"+Math.round(n).toLocaleString("en-US")}}
  function run(){{
    var band=+$("st-band").value, leads=Math.max(0,+$("st-leads").value||0), val=Math.max(0,+$("st-value").value||0);
    var close=+$("st-close").value, fast=+$("st-fast").value;
    $("st-close-o").textContent=close+"%"; $("st-fast-o").textContent=fast+"%";
    var boxes=[].slice.call(document.querySelectorAll(".st-checks input"));
    var yes=boxes.filter(function(b){{return b.checked}}).length;
    var score=Math.round(band+yes*60/7);
    $("st-n").textContent=score; $("st-ring").style.setProperty("--p",score);
    var g,t;
    if(score>=85){{g="Fast";t="You reply faster than most businesses. Keep measuring so it stays that way."}}
    else if(score>=60){{g="Good, with gaps";t="Most leads hear back quickly, but some still wait. Close the gaps below."}}
    else if(score>=35){{g="Leaking leads";t="Many leads wait too long for a reply. These fixes will make the biggest difference."}}
    else{{g="Slow";t="Most leads wait too long. Automating your first reply is the fastest win."}}
    $("st-grade").textContent=g; $("st-gtxt").textContent=t;
    var slow=Math.round(leads*(100-fast)/100);
    $("st-slow").textContent=slow.toLocaleString("en-US");
    $("st-rev").textContent=money(slow*close/100*val);
    var out=$("st-fixes"); out.innerHTML="";
    var miss=boxes.filter(function(b){{return !b.checked}}).slice(0,3);
    if(band<32){{var li=document.createElement("li");li.textContent="Get your first reply under 5 minutes: automate it so no one has to remember.";out.appendChild(li)}}
    miss.forEach(function(b){{var f=F[b.getAttribute("data-k")],li=document.createElement("li"),a=document.createElement("a");a.href=f[0];a.textContent=f[1];li.appendChild(a);out.appendChild(li)}});
    if(!out.children.length){{var l2=document.createElement("li");l2.textContent="You're doing everything on this list. Track your median response time weekly to stay fast.";out.appendChild(l2)}}
  }}
  document.getElementById("st-form").addEventListener("input",run);
  document.getElementById("st-form").addEventListener("change",run);
  run();
}})();
</script>'''
    title = "Free Speed to Lead Test: Score Your Lead Response Time"
    desc = "Free speed to lead test: score how fast you reply to new leads out of 100, see the revenue tied to leads that wait over 5 minutes, and get your top fixes."
    app = {"@type": "WebApplication", "name": "Speed to Lead Test", "url": cfg["domain"] + path,
           "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
           "publisher": {"@id": cfg["domain"] + "/#org"}, "description": desc}
    htm = page(cfg, fonts, path, title, desc, crumbs, body, logo, [faq_schema(FAQS), app])
    htm = htm.replace("</head>", f"<style>{TOOL_CSS}</style>\n</head>", 1)
    return path, htm
