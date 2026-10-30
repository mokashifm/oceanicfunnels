# Build a reel from AI footage clips + HTML overlays + Kokoro VO + music.
# Usage: build_footage_reel.py <reel_id> <clips_dir> <work_dir> <tts_dir>
import sys, json, os, subprocess, soundfile as sf
RID, CLIPS, WORK, TTS = sys.argv[1:5]
LOGO = open('/home/claude/shot/logo_on_dark.svg').read()
END_HTML = lambda h: f'<div class="panel ap" data-at=".1" style="display:flex;flex-direction:column;align-items:center;text-align:center;padding:56px 50px"><span class="k" style="align-self:center">Built in 14 days</span><h2 class="endh">{h}</h2><p>No sales team needed.</p><div class="btn">Book a free info call →</div>{LOGO}</div>'
END_VO = "Oceanic Funnels builds this for your med spa in fourteen days. Book your free info call."
REELS = {
 "A": [
  dict(clip="A1", inp=0, vo="It's nine fourteen on a Saturday night. Your med spa closed hours ago.",
       html='<span class="k ap" data-at=".2">Saturday · 9:14 PM</span><div class="panel ap" data-at=".6"><div class="clock">9:14</div><h1>Your med spa<br>is closed.</h1></div>'),
  dict(clip="A2", inp=0, vo="But new clients are still messaging you.",
       html='<span class="k ap" data-at=".1">Still coming in</span><div class="card ap" data-at=".3"><div class="h">Instagram <i>now</i></div>Hi! How much is lip filler? Anything this week?</div><div class="card ap" data-at="1.0"><div class="h">Website chat <i>2m ago</i></div>Do you do laser hair removal?</div><div class="card ap" data-at="1.7"><div class="h">Facebook <i>5m ago</i></div>Is Botox available Saturday?</div>'),
  dict(clip="A3", inp=0, vo="The A.I. replies in seconds, answers their questions, and offers real times from your calendar.",
       html='<span class="k ap" data-at=".1">Instagram DM · 9:15 PM</span><div class="ph ap" data-at=".1"><div class="q ap" data-at=".2">Hi! How much is lip filler? Anything this week?</div><div class="a ap" data-at="1.4"><span class="who">Your clinic</span>Lip filler starts from $650. We have Thursday 4:00 or Saturday 11:00. Which works?</div><div class="q ap" data-at="3.4">Saturday 11 please!</div></div>'),
  dict(clip="A2", inp=3.0, vo="Then it books the consultation, and takes a deposit to hold the spot.",
       html='<span class="k ap" data-at=".1">Booked · 9:16 PM</span><div class="card ap" data-at=".3"><div class="pay"><div class="ic">$</div><div><b>$50 deposit paid</b><span>Lip filler consultation</span></div></div></div><div class="cal ap" data-at="1.3"><div class="lb">Saturday</div><div class="slot"><b>10:00</b>Facial</div><div class="slot on"><b>11:00</b>Lip filler consult<span class="tg">NEW</span></div><div class="slot"><b>12:30</b>Botox</div></div>'),
  dict(clip="A4", inp=0, vo="You wake up to new bookings, not unread messages.",
       html='<span class="k ap" data-at=".1">Sunday · 8:00 AM</span><div class="dash ap" data-at=".4"><div class="lb">Booked overnight</div><div><span class="num cnt" data-to="3" data-at=".6">0</span><span class="up">while you slept</span></div><small>Example. Illustration only.</small></div>'),
  dict(clip="A1", inp=0, vo=END_VO, html=END_HTML('Every DM answered <span class="aq">and booked. 24/7.</span>'), dim=True),
 ],
 "B": [
  dict(clip="B1", inp=0, vo="Your injector is mid-treatment. Then the front desk phone rings.",
       html='<span class="k ap" data-at=".2">Tuesday · 2:47 PM</span><div class="card red ap" data-at="1.6"><div class="h">Incoming call <i>Front desk</i></div>(512) ••• ••21 is calling…</div>'),
  dict(clip="B3", inp=0, vo="Nobody can pick up. That caller was ready to book.",
       html='<span class="k ap" data-at=".1">Missed call</span><div class="panel ap" data-at=".3"><div class="call"><div class="av red" style="color:#FF7657"><div class="ring"></div><span style="color:#0E1A1B">✕</span></div><h3>Missed call</h3><div class="sub">(512) ••• ••21 · 2:47 PM</div></div></div>'),
  dict(clip="B2", inp=0, minlen=5.6, vo="Now the A.I. receptionist answers instead.",
       html='<span class="k ap" data-at=".1">Answered · 2:47 PM</span><div class="panel ap" data-at=".2"><div class="call"><div class="av" style="color:#3DE3C8"><div class="ring"></div><span style="color:#0E1A1B">AI</span></div><h3>AI receptionist</h3><div class="sub tm">0:00</div><div class="wave"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div></div><div class="ph ap" data-at="1.0"><div class="q ap" data-at="1.2">Hi, do you have Botox this Thursday?</div><div class="a ap" data-at="2.6"><span class="who">Your clinic</span>Yes! 2:30 or 5:00. Which works?</div></div>'),
  dict(clip="B1", inp=2.2, vo="It books the caller into a free slot, and texts the confirmation.",
       html='<span class="k ap" data-at=".1">Text · 2:49 PM</span><div class="ph ap" data-at=".2"><div class="a ap" data-at=".3"><span class="who">Your clinic</span>You are booked for Botox on Thursday at 2:30. Reply R to reschedule.</div><div class="q ap" data-at="1.8">Perfect, thank you!</div><div class="chip ap" data-at="2.6">✓ Booked from a missed call</div></div>'),
  dict(clip="B4", inp=0, vo="Your team never stops the treatment. And you never lose the booking.",
       html='<span class="k ap" data-at=".1">Thursday</span><div class="cal ap" data-at=".3"><div class="lb">Thursday</div><div class="slot"><b>1:00</b>Microneedling</div><div class="slot on"><b>2:30</b>Botox<span class="tg">FROM A MISSED CALL</span></div><div class="slot"><b>4:00</b>Filler review</div></div>'),
  dict(clip="B3", inp=0, vo=END_VO, html=END_HTML('Every call answered, <span class="aq">even mid-treatment.</span>'), dim=True),
 ],
}
SC = REELS[RID]; os.makedirs(WORK, exist_ok=True)
from kokoro_onnx import Kokoro
k = Kokoro(TTS + "/kokoro-v1.0.onnx", TTS + "/voices-v1.0.bin")
t = 0.0; PAD = 0.5
for i, s in enumerate(SC):
    a, sr = k.create(s["vo"], voice="af_heart", speed=1.03, lang="en-us"); sf.write(f"{WORK}/vo{i}.wav", a, sr)
    s["dur"] = round(len(a) / sr, 3); s["st"] = round(t, 3)
    s["len"] = round(max(s.get("minlen", 3.6), s["dur"] + PAD) + (0.4 if i == 0 else 0) + (2.4 if i == len(SC) - 1 else 0), 3)
    s["vost"] = round(t + (0.4 if i == 0 else 0.15), 3); t += s["len"]
TOTAL = round(t, 3)
# --- base video: each scene from its clip, scaled to 1080x1920, slowed if the clip is too short
parts = []
for i, s in enumerate(SC):
    src = f"{CLIPS}/{s['clip']}.mp4"
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src]).decode())
    avail = dur - s["inp"]; f = max(1.0, s["len"] / avail)
    vf = f"trim=start={s['inp']},setpts=(PTS-STARTPTS)*{f:.4f},scale=1080:1920:flags=lanczos,fps=30"
    if s.get("dim"): vf += ",eq=brightness=-0.08:saturation=0.9"
    out = f"{WORK}/part{i}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-vf", vf, "-t", str(s["len"]), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", out], check=True)
    parts.append(out)
open(f"{WORK}/parts.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{WORK}/parts.txt", "-c", "copy", f"{WORK}/base.mp4"], check=True)
# --- overlay page
css = open('/tmp/claude-0/-home-claude/4c56178f-3b6b-54ea-a8fd-72eb28719326/scratchpad/three/ov.css').read()
css += '''html,body{margin:0;background:transparent}
.scrim{background:linear-gradient(180deg,rgba(10,16,17,.55) 0%,rgba(10,16,17,.10) 32%,rgba(10,16,17,.10) 62%,rgba(10,16,17,.6) 100%)}
.endh{font-family:"Inter Tight";font-weight:600;font-size:86px;letter-spacing:-.045em;line-height:1.02;margin-top:28px}
.panel .btn{margin-top:40px;background:#3DE3C8;color:#0E1A1B;font-family:"Inter Tight";font-weight:600;font-size:42px;padding:26px 50px;border-radius:999px}
.panel svg{height:70px;width:auto;margin-top:44px}
.sc.endsc{justify-content:center;padding-top:0;padding-bottom:520px}'''
data = [{"st": s["st"], "len": s["len"], "vost": s["vost"], "dur": s["dur"], "vo": s["vo"].replace("A.I.", "AI"), "html": s["html"], "end": i == len(SC) - 1} for i, s in enumerate(SC)]
html = '''<!doctype html><html><head><meta charset="utf-8"><style>''' + css + '''</style></head><body><div id="ov"></div><script>
const SC=''' + json.dumps(data) + ''';const ov=document.getElementById('ov');
ov.innerHTML='<div class="scrim"></div>'+SC.map((s,i)=>`<div class="sc ${s.end?'endsc':''}" id="s${i}">${s.html}</div>`).join('')+'<div class="cc" id="cc"></div>';
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
function sh(el,t,t0,d=.35,dy=40){el.style.display=t<t0?'none':'';const p=ease((t-t0)/d);el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px)`}
window.render=function(t){SC.forEach((x,i)=>{const el=document.getElementById('s'+i);const A=x.st,B=x.st+x.len;const o=Math.min(ease((t-A)/.25),1-ease((t-B+.25)/.25));el.style.opacity=o;el.style.visibility=o>0?'visible':'hidden';if(o<=0)return;
 el.querySelectorAll('.ap').forEach(e=>sh(e,t,x.st+ +e.dataset.at));el.querySelectorAll('.cnt').forEach(e=>{e.textContent=Math.round(+e.dataset.to*ease((t-x.st-+e.dataset.at)/2))});
 el.querySelectorAll('.wave i').forEach((w,j)=>{w.style.height=(18+80*Math.abs(Math.sin(t*9+j*.7))*Math.abs(Math.sin(t*2.3+j)))+'px'});
 el.querySelectorAll('.ring').forEach(r=>{const p=((t-x.st)*1.1)%1;r.style.transform=`scale(${1+p*.55})`;r.style.opacity=1-p});
 el.querySelectorAll('.tm').forEach(r=>{r.textContent='0:'+String(Math.max(0,Math.floor(t-x.st))).padStart(2,'0')})});
 let c='';SC.forEach(x=>{if(t>=x.vost&&t<x.vost+x.dur+.2)c=x.vo});document.getElementById('cc').innerHTML=c?'<span>'+c+'</span>':'';};render(0);
</script></body></html>'''
open(f"{WORK}/overlay.html", "w").write(html)
json.dump({"TOTAL": TOTAL, "vost": [s["vost"] for s in SC]}, open(f"{WORK}/timing.json", "w"))
print("TOTAL", TOTAL, [(s["clip"], s["st"], s["len"]) for s in SC])
