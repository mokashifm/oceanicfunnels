# 4 med spa reels on a 3D clinic set. Usage: reels3d.py <reel_id|all> <three_dir> <tts_dir>
import sys, json, os, subprocess, soundfile as sf
ROOT = sys.argv[2]; TTS = sys.argv[3]; WANT = sys.argv[1]
LOGO = open('/home/claude/shot/logo_on_dark.svg').read()
WAVE = '<div class="wave">' + '<i></i>' * 22 + '</div>'
def end(h): return ("end", False, "Oceanic Funnels builds this for your med spa in fourteen days. Book your free info call.",
  f'<div class="panel"><span class="k">Built in 14 days</span><h2>{h}</h2><p>No sales team needed.</p><div class="btn">Book a free info call →</div>{LOGO}</div>', "wide")
R = {}
R["A-after-hours"] = [
 ("s", True, "It's nine fourteen on a Saturday night. Your med spa closed hours ago.",
  '<span class="k">Saturday · 9:14 PM</span><div class="panel ap" data-at=".2"><div class="clock">9:14</div><h1>Your med spa<br>is closed.</h1></div>', "wide"),
 ("s", True, "But new clients are still messaging you.",
  '<span class="k">Still coming in</span><div class="card ap" data-at=".2"><div class="h">Instagram <i>now</i></div>Hi! How much is lip filler? Anything this week?</div><div class="card ap" data-at=".8"><div class="h">Website chat <i>2m ago</i></div>Do you do laser hair removal?</div><div class="card ap" data-at="1.4"><div class="h">Facebook <i>5m ago</i></div>Is Botox available Saturday?</div>', "desk"),
 ("s", True, "The A.I. replies in seconds, answers their questions, and offers real times from your calendar.",
  '<span class="k">Instagram DM · 9:15 PM</span><div class="ph"><div class="q ap" data-at=".1">Hi! How much is lip filler? Anything this week?</div><div class="a ap" data-at="1.3"><span class="who">Your clinic</span>Lip filler starts from $650. We have Thursday 4:00 or Saturday 11:00. Which works?</div><div class="q ap" data-at="3.3">Saturday 11 please!</div></div>', "bed"),
 ("s", True, "Then it books the consultation, and takes a deposit to hold the spot.",
  '<span class="k">Booked · 9:16 PM</span><div class="card ap" data-at=".2"><div class="pay"><div class="ic">$</div><div><b>$50 deposit paid</b><span>Lip filler consultation</span></div></div></div><div class="cal ap" data-at="1.2"><div class="lb">Saturday</div><div class="slot"><b>10:00</b>Facial</div><div class="slot on"><b>11:00</b>Lip filler consult<span class="tg">NEW</span></div><div class="slot"><b>12:30</b>Botox</div></div>', "cart"),
 ("s", False, "You wake up to new bookings, not unread messages.",
  '<span class="k">Sunday · 8:00 AM</span><div class="dash ap" data-at=".2"><div class="lb">Booked overnight</div><div><span class="num cnt" data-to="3" data-at=".4">0</span><span class="up">while you slept</span></div><small>Example. Illustration only.</small></div>', "wide"),
 end('Every DM answered <span class="aq">and booked. 24/7.</span>'),
]
R["B-mid-treatment"] = [
 ("s", False, "Your injector is mid-treatment. Then the front desk phone rings.",
  '<span class="k">Tuesday · 2:47 PM</span><div class="card ap red" data-at=".6"><div class="h">Incoming call <i>Front desk</i></div>(512) ••• ••21</div>', "cart"),
 ("s", False, "Nobody can pick up. That caller was ready to book.",
  '<span class="k">Missed call</span><div class="panel ap" data-at=".2"><div class="call"><div class="av red" style="color:#FF7657"><div class="ring"></div>✕</div><h3>Missed call</h3><div class="sub">(512) ••• ••21 · 2:47 PM</div></div></div>', "desk"),
 ("s", False, "Now the A.I. receptionist answers instead.",
  '<span class="k">Answered · 2:47 PM</span><div class="panel ap" data-at=".1"><div class="call"><div class="av" style="color:#3DE3C8"><div class="ring"></div>AI</div><h3>AI receptionist</h3><div class="sub tm">0:00</div>' + WAVE + '</div></div><div class="ph"><div class="q ap" data-at=".9">Hi, do you have Botox this Thursday?</div><div class="a ap" data-at="2.0"><span class="who">Your clinic</span>Yes! 2:30 or 5:00. Which works?</div></div>', "desk"),
 ("s", False, "It books the caller into a free slot, and texts the confirmation.",
  '<span class="k">Text · 2:49 PM</span><div class="ph"><div class="a ap" data-at=".2"><span class="who">Your clinic</span>You are booked for Botox on Thursday at 2:30. Reply R to reschedule.</div><div class="q ap" data-at="1.6">Perfect, thank you!</div><div class="chip ap" data-at="2.4">✓ Booked from a missed call</div></div>', "bed"),
 ("s", False, "Your team never stops the treatment. And you never lose the booking.",
  '<span class="k">Thursday</span><div class="cal ap" data-at=".2"><div class="lb">Thursday</div><div class="slot"><b>1:00</b>Microneedling</div><div class="slot on"><b>2:30</b>Botox<span class="tg">FROM A MISSED CALL</span></div><div class="slot"><b>4:00</b>Filler review</div></div>', "wide"),
 end('Every call answered, <span class="aq">even mid-treatment.</span>'),
]
R["C-no-shows"] = [
 ("s", False, "An empty chair is the most expensive thing in your med spa.",
  '<span class="k">11:00 AM · Today</span><div class="cal ap" data-at=".3"><div class="lb">Today</div><div class="slot"><b>10:00</b>Hydrafacial</div><div class="slot off"><b>11:00</b>Consultation<span class="tg">NO-SHOW</span></div><div class="slot"><b>12:30</b>Botox</div></div>', "bed"),
 ("s", False, "Now every consultation is booked with a deposit,",
  '<span class="k">At booking</span><div class="card ap" data-at=".2"><div class="pay"><div class="ic">$</div><div><b>$50 deposit paid</b><span>Credited to the treatment</span></div></div></div>', "cart"),
 ("s", False, "and clients get reminders by text and by email.",
  '<span class="k">Day before · 10:00 AM</span><div class="ph"><div class="a ap" data-at=".1"><span class="who">Text from your clinic</span>Reminder: your consultation is tomorrow at 11:00. Reply C to confirm.</div><div class="q ap" data-at="1.0">C</div></div><div class="mail ap" data-at="1.8"><div class="top"><span>Email · Your clinic</span><span>10:00 AM</span></div><div class="bd"><b>See you tomorrow at 11:00</b><br>Your consultation is confirmed.<br><span class="btn2">Reschedule</span></div></div>', "desk"),
 ("s", False, "If something comes up, they reschedule in one tap, and the deposit carries over.",
  '<span class="k">Rescheduled</span><div class="ph"><div class="q ap" data-at=".1">Something came up, can I move it?</div><div class="a ap" data-at="1.2"><span class="who">Your clinic</span>No problem! Your deposit carries over. Friday 2:00 or Saturday 10:30?</div><div class="q ap" data-at="2.6">Saturday works</div><div class="chip ap" data-at="3.4">✓ Moved · deposit kept</div></div>', "shelf"),
 ("s", False, "So your chairs stay full.",
  '<span class="k">This week</span><div class="cal ap" data-at=".2"><div class="lb">Saturday</div><div class="slot on"><b>10:00</b>Hydrafacial</div><div class="slot on"><b>10:30</b>Consultation<span class="tg">MOVED</span></div><div class="slot on"><b>12:30</b>Botox</div><div class="slot on"><b>2:00</b>Filler</div></div>', "wide"),
 end('Fewer no-shows. <span class="aq">Deposits held.</span>'),
]
R["D-rebook"] = [
 ("s", False, "Botox wears off. The question is: who do your clients rebook with?",
  '<span class="k">Month 4</span><div class="panel ap" data-at=".3"><h1>Botox wears off.<br><span class="aq">Who do they rebook with?</span></h1></div>', "mirror"),
 ("s", False, "Most clinics wait for clients to remember.",
  '<span class="k">Your client list</span><div class="cal ap" data-at=".2"><div class="lb">Due for Botox</div><div class="row">Sarah M.<small>4 months ago</small></div><div class="row">Priya K.<small>4 months ago</small></div><div class="row">Emma L.<small>5 months ago</small></div></div>', "shelf"),
 ("s", False, "Your system remembers for you.",
  '<span class="k">Automatic</span><div class="cal ap" data-at=".2"><div class="lb">Rebooking reminders</div><div class="tl"><div class="st"><div class="dot">1</div><div><b>Day 0</b><span>Treatment done, review request sent</span></div></div><div class="st"><div class="dot">2</div><div><b>Month 3</b><span>Friendly check-in text</span></div></div><div class="st"><div class="dot">3</div><div><b>Month 4</b><span>Rebooking link with her injector</span></div></div></div></div>', "desk"),
 ("s", False, "It texts each client at the right time, with a link to book their usual injector.",
  '<span class="k">Text · Month 4</span><div class="ph"><div class="a ap" data-at=".1"><span class="who">Your clinic</span>Hi Sarah! It\'s about 4 months since your last Botox. Want to book before it wears off?</div><div class="q ap" data-at="1.8">Yes please, same injector</div><div class="a ap" data-at="2.8"><span class="who">Your clinic</span>Done! Booked with Jess on the 14th at 2:00.</div></div>', "bed"),
 ("s", False, "So they come back to you, not to the clinic running a promo that week.",
  '<span class="k">Rebooked</span><div class="dash ap" data-at=".2"><div class="lb">Rebooked this month</div><div><span class="num cnt" data-to="23" data-at=".4">0</span><span class="up">from reminders</span></div><small>Example. Illustration only.</small></div>', "wide"),
 end('Clients rebooked <span class="aq">before it wears off.</span>'),
]
ENGINE = r'''
const SC=__SC__,END=__END__;const ov=document.getElementById('ov');
ov.innerHTML='<div class="scrim"></div>'+SC.map((s,i)=>`<div class="sc ${s.cls}" id="s${i}">${s.html}</div>`).join('')+'<div class="cc" id="cc"></div>';
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);let lastMode=null;
function sh(el,t,t0,d=.35,dy=40){el.style.display=t<t0?'none':'';const p=ease((t-t0)/d);el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px)`}
window.render=function(t){let cur=0;for(let i=0;i<SC.length;i++)if(t>=SC[i].st-0.15)cur=i;
 const s=SC[cur];if(lastMode!==s.night){setMode(s.night);lastMode=s.night}
 const a=s.st-0.15,b=cur<SC.length-1?SC[cur+1].st-0.15:END;shot(s.shot,(t-a)/(b-a));
 SC.forEach((x,i)=>{const el=document.getElementById('s'+i);const A=x.st-0.15,B=i<SC.length-1?SC[i+1].st-0.15:END+1;const o=Math.min(ease((t-A)/.3),1-ease((t-B+.3)/.3));el.style.opacity=o;el.style.visibility=o>0?'visible':'hidden';
  if(o<=0)return;el.querySelectorAll('.ap').forEach(e=>sh(e,t,x.st+ +e.dataset.at));
  el.querySelectorAll('.cnt').forEach(e=>{e.textContent=Math.round(+e.dataset.to*ease((t-x.st-+e.dataset.at)/2.2))});
  el.querySelectorAll('.wave i').forEach((w,j)=>{w.style.height=(18+80*Math.abs(Math.sin(t*9+j*.7))*Math.abs(Math.sin(t*2.3+j)))+'px'});
  el.querySelectorAll('.ring').forEach(r=>{const p=((t-x.st)*1.1)%1;r.style.transform=`scale(${1+p*.55})`;r.style.opacity=1-p});
  el.querySelectorAll('.tm').forEach(r=>{r.textContent='0:'+String(Math.max(0,Math.floor(t-x.st))).padStart(2,'0')});});
 let c='';SC.forEach(x=>{if(t>=x.st&&t<x.st+x.dur+.25)c=x.vo});document.getElementById('cc').innerHTML=c?'<span>'+c+'</span>':'';
};
'''
from kokoro_onnx import Kokoro
k = Kokoro(TTS + "/kokoro-v1.0.onnx", TTS + "/voices-v1.0.bin")
for rid, scenes in R.items():
    if WANT not in ("all", rid): continue
    out = f"{ROOT}/out_{rid}"; os.makedirs(out, exist_ok=True)
    SC = []; t = 0.3
    for i, (kind, night, vo, html, shot) in enumerate(scenes):
        a, sr = k.create(vo, voice="af_heart", speed=1.03, lang="en-us"); sf.write(f"{out}/vo{i}.wav", a, sr)
        d = round(len(a) / sr, 3)
        SC.append({"st": round(t, 3), "dur": d, "vo": vo.replace("A.I.", "AI"), "html": html, "night": night, "shot": shot, "cls": "end" if kind == "end" else ""})
        t += d + 0.55
    END = round(t - 0.55 + 2.6, 2)
    js = ENGINE.replace("__SC__", json.dumps(SC)).replace("__END__", str(END))
    open(f"{ROOT}/reel_{rid}.js", "w").write(js)
    json.dump({"END": END, "st": [x["st"] for x in SC]}, open(f"{out}/timing.json", "w"))
    print(rid, END)
