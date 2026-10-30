# Reel 2: full med spa story with VO timings. Usage: reel2.py timings.json out.html [bgdir]
import sys, json, os, base64
tm = json.load(open(sys.argv[1])); out = sys.argv[2]; bgdir = sys.argv[3] if len(sys.argv) > 3 else ""
s = open('/home/claude/shot/og.html').read(); FONTS = s[s.find('<style>') + 7:s.find('body{')]
LOGO = open('/home/claude/shot/logo_on_dark.svg').read()
PAD, START, HOLD = 0.45, 0.35, 3.2
st = []; t = START
for d in tm["dur"]: st.append(round(t, 3)); t += d + PAD
END = round(t - PAD + HOLD, 2)
bgs = []
for i in range(7):
    f = f"{bgdir}/s{i}.jpg" if bgdir else ""
    bgs.append("data:image/jpeg;base64," + base64.b64encode(open(f, "rb").read()).decode() if f and os.path.exists(f) else "")
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1920px;overflow:hidden;background:#0E1A1B;font-family:Inter,sans-serif;color:#fff;position:relative}}
.bgimg{{position:absolute;inset:-60px;background-size:cover;background-position:center;opacity:0}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,26,27,.55),rgba(14,26,27,.82) 55%,rgba(14,26,27,.95))}}
.bk{{position:absolute;border-radius:50%;filter:blur(40px)}}
.hatch{{position:absolute;top:0;right:0;width:50%;height:520px;background:repeating-linear-gradient(135deg,#3DE3C8 0 3px,transparent 3px 14px);-webkit-mask-image:linear-gradient(225deg,#000 0%,transparent 62%);opacity:.35}}
.sc{{position:absolute;inset:0;padding:190px 80px 0;opacity:0}}
.k{{display:inline-block;font-family:"Inter Tight";font-weight:600;font-size:30px;letter-spacing:.06em;text-transform:uppercase;padding:12px 24px;border-radius:999px;background:#FF7657;color:#0E1A1B}}
.aq{{color:#3DE3C8}}
h1{{font-family:"Inter Tight";font-weight:600;font-size:118px;letter-spacing:-.05em;line-height:1;margin-top:40px}}
.big{{font-family:"Inter Tight";font-weight:600;font-size:250px;letter-spacing:-.06em;line-height:1;margin-top:260px}}
.card{{background:rgba(244,248,247,.97);color:#0E1A1B;border-radius:36px;padding:30px 34px;margin-top:26px;font-size:36px;line-height:1.35;box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}}
.card b.h{{display:flex;justify-content:space-between;font-family:"Inter Tight";font-weight:600;font-size:26px;letter-spacing:.04em;text-transform:uppercase;color:#5B6967;margin-bottom:8px}}
.card b.h i{{font-style:normal;text-transform:none;letter-spacing:0}}
.ph{{background:#F4F8F7;border-radius:40px;padding:34px;color:#0E1A1B;font-size:37px;line-height:1.36;display:flex;flex-direction:column;gap:22px;margin-top:40px}}
.q{{align-self:flex-end;background:#0E1A1B;color:#fff;border-radius:28px 28px 8px 28px;padding:22px 28px;max-width:82%}}
.a{{align-self:flex-start;background:#fff;border:1px solid #DCE5E3;border-radius:28px 28px 28px 8px;padding:22px 28px;max-width:88%}}
.who{{display:block;font-family:"Inter Tight";font-weight:600;font-size:22px;letter-spacing:.06em;text-transform:uppercase;color:#0E9C87;margin-bottom:6px}}
.chip{{align-self:center;background:#3DE3C8;color:#0E1A1B;font-family:"Inter Tight";font-weight:600;font-size:36px;padding:16px 30px;border-radius:999px}}
.call{{text-align:center;margin-top:30px}}
.av{{width:200px;height:200px;border-radius:50%;margin:40px auto 0;background:#3DE3C8;display:grid;place-items:center;color:#0E1A1B;font-family:"Inter Tight";font-weight:600;font-size:64px;position:relative}}
.ring{{position:absolute;inset:0;border-radius:50%;border:4px solid #3DE3C8}}
.call h3{{font-family:"Inter Tight";font-weight:600;font-size:56px;margin-top:34px;letter-spacing:-.03em}}
.call p{{font-size:32px;color:#9DB0AD;margin-top:8px}}
.wave{{display:flex;gap:10px;justify-content:center;align-items:center;height:120px;margin-top:30px}}
.wave i{{display:block;width:14px;border-radius:8px;background:#3DE3C8}}
.tr{{margin-top:24px;display:flex;flex-direction:column;gap:18px;text-align:left;font-size:34px;line-height:1.36;background:#F4F8F7;color:#0E1A1B;border-radius:36px;padding:28px}}
.mail{{background:#fff;color:#0E1A1B;border-radius:32px;overflow:hidden;margin-top:30px;box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}}
.mail .top{{background:#0E1A1B;color:#fff;padding:22px 30px;font-family:"Inter Tight";font-weight:600;font-size:28px;display:flex;justify-content:space-between}}
.mail .bd{{padding:30px;font-size:33px;line-height:1.4}}
.mail .bt{{display:inline-block;margin-top:18px;background:#0E9C87;color:#fff;padding:16px 28px;border-radius:999px;font-family:"Inter Tight";font-weight:600;font-size:28px}}
.dash{{background:#F4F8F7;color:#0E1A1B;border-radius:40px;padding:40px;margin-top:40px}}
.dash .lb{{font-family:"Inter Tight";font-weight:600;font-size:30px;color:#5B6967;text-transform:uppercase;letter-spacing:.05em}}
.dash .num{{font-family:"Inter Tight";font-weight:600;font-size:200px;letter-spacing:-.06em;line-height:1;margin-top:10px}}
.dash .up{{display:inline-block;background:#DDF7F2;color:#0E9C87;font-weight:700;font-size:30px;padding:8px 18px;border-radius:999px;margin-left:16px;vertical-align:middle}}
.bars{{display:flex;gap:16px;align-items:flex-end;height:330px;margin-top:30px;border-bottom:2px solid #DCE5E3}}
.bars i{{flex:1;border-radius:12px 12px 0 0;background:linear-gradient(180deg,#3DE3C8,#0E9C87)}}
.dash small{{display:block;margin-top:18px;font-size:22px;color:#9DB0AD}}
.end{{display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:260px}}
.end h2{{font-family:"Inter Tight";font-weight:600;font-size:98px;letter-spacing:-.045em;line-height:1.02;margin-top:40px}}
.end p{{font-size:42px;color:#C9D6D4;margin-top:30px;line-height:1.35}}
.end .btn{{margin-top:56px;background:#3DE3C8;color:#0E1A1B;font-family:"Inter Tight";font-weight:600;font-size:46px;padding:30px 58px;border-radius:999px}}
.end svg{{height:84px;width:auto;margin-top:64px}}
.cc{{position:absolute;left:70px;right:70px;top:1370px;text-align:center;font-family:"Inter Tight";font-weight:600;font-size:52px;line-height:1.2;letter-spacing:-.02em;text-shadow:0 4px 24px rgba(0,0,0,.6)}}
.cc span{{background:rgba(14,26,27,.82);padding:6px 18px;border-radius:14px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
</style></head><body>
<div id="bg"><div class="bk" id="b1" style="width:700px;height:700px;background:#FF9B82;opacity:.22"></div><div class="bk" id="b2" style="width:600px;height:600px;background:#3DE3C8;opacity:.16"></div><div class="bk" id="b3" style="width:500px;height:500px;background:#F6D9C9;opacity:.14"></div></div>
{"".join(f'<div class="bgimg" id="bi{i}" style="background-image:url({b})"></div>' for i, b in enumerate(bgs) if b)}
<div class="shade"></div><div class="hatch"></div>
<div class="sc" id="s0"><span class="k">Saturday · 9:14 PM</span><div class="big">9:14</div><h1>Your med spa<br>is closed.</h1></div>
<div class="sc" id="s1"><span class="k">Still coming in</span>
<div class="card" id="n1"><b class="h">Instagram <i>now</i></b>Hi! How much is lip filler? Anything this week?</div>
<div class="card" id="n2"><b class="h">Missed call <i>1m ago</i></b>(512) ••• ••21</div>
<div class="card" id="n3"><b class="h">Website chat <i>3m ago</i></b>Do you do laser hair removal?</div>
<div class="card" id="n4"><b class="h">Facebook <i>6m ago</i></b>Is Botox available Saturday?</div></div>
<div class="sc" id="s2"><span class="k">Incoming call · 9:16 PM</span><div class="call"><div class="av"><div class="ring" id="rg"></div>AI</div><h3>AI receptionist answered</h3><p id="ctime">0:00</p>
<div class="wave" id="wv">{"".join("<i></i>" for _ in range(22))}</div>
<div class="tr"><div class="q" id="t1">Hi, do you have Botox this Thursday?</div><div class="a" id="t2"><span class="who">Your clinic</span>Yes! We have 2:30 or 5:00. Which works?</div></div></div></div>
<div class="sc" id="s3"><span class="k">Instagram DM · 9:18 PM</span><div class="ph">
<div class="q" id="d1">Hi! How much is lip filler? Anything this week?</div>
<div class="a" id="d2"><span class="who">Your clinic</span>Lip filler starts from $650. Thursday 4:00 or Saturday 11:00?</div>
<div class="q" id="d3">Saturday 11 please!</div>
<div class="chip" id="d4">✓ Booked · $50 deposit paid</div></div></div>
<div class="sc" id="s4"><span class="k">Day before · 10:00 AM</span>
<div class="ph" style="margin-top:34px"><div class="a" id="r1"><span class="who">Text from your clinic</span>Reminder: your consultation is tomorrow at 11:00. Reply C to confirm.</div><div class="q" id="r2">C</div><div class="chip" id="r3">✓ Confirmed</div></div>
<div class="mail" id="r4"><div class="top"><span>Email · Your clinic</span><span>10:00 AM</span></div><div class="bd"><b>See you tomorrow at 11:00</b><br>Your lip filler consultation is confirmed. Need to change it?<br><span class="bt">Reschedule</span></div></div></div>
<div class="sc" id="s5"><span class="k">Your calendar</span><div class="dash"><div class="lb">Bookings this month</div><div><span class="num" id="cn">0</span><span class="up" id="cu">▲ growing</span></div>
<div class="bars" id="br">{"".join("<i></i>" for _ in range(10))}</div><small>Example dashboard. Illustration only.</small></div></div>
<div class="sc" id="s6"><div class="end"><span class="k">Built in 14 days</span><h2>Answered, booked<br>and <span class="aq">reminded. 24/7.</span></h2><p>No sales team needed.</p><div class="btn">Book a free info call →</div>{LOGO}</div></div>
<div class="cc" id="cc"></div>
<script>
const ST={json.dumps(st)},DU={json.dumps(tm["dur"])},LN={json.dumps(tm["lines"])},END={END};
const $=i=>document.getElementById(i);const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
function show(el,t,t0,d=.35,dy=40){{if(!el)return;el.style.display=t<t0?'none':'';const p=ease((t-t0)/d);el.style.opacity=p;el.style.transform=`translateY(${{(1-p)*dy}}px)`}}
function scene(i,t){{const a=ST[i]-0.15,b=i<6?ST[i+1]-0.15:END+1;const fi=ease((t-a)/.3),fo=ease((t-b)/.3);const o=Math.min(fi,1-fo);$('s'+i).style.opacity=o;$('s'+i).style.transform=`translateY(${{(1-fi)*30}}px)`;const bi=$('bi'+i);if(bi){{bi.style.opacity=o;const z=1+.06*Math.min(1,Math.max(0,(t-a)/(b-a)));bi.style.transform=`scale(${{z}})`}}return o}}
window.render=function(t){{
 $('b1').style.left=(-200+120*Math.sin(t*.3))+'px';$('b1').style.top=(200+80*Math.cos(t*.25))+'px';
 $('b2').style.left=(600+100*Math.cos(t*.22))+'px';$('b2').style.top=(900+120*Math.sin(t*.2))+'px';
 $('b3').style.left=(200+90*Math.sin(t*.35))+'px';$('b3').style.top=(1400+60*Math.cos(t*.3))+'px';
 for(let i=0;i<7;i++)scene(i,t);
 const s1=ST[1];show($('n1'),t,s1+.2);show($('n2'),t,s1+.9);show($('n3'),t,s1+1.6);show($('n4'),t,s1+2.3);
 const s2=ST[2];const rp=((t-s2)*1.2)%1;$('rg').style.transform=`scale(${{1+rp*.5}})`;$('rg').style.opacity=1-rp;
 $('ctime').textContent='0:'+String(Math.max(0,Math.floor(t-s2))).padStart(2,'0');
 [...$('wv').children].forEach((b,j)=>{{b.style.height=(20+80*Math.abs(Math.sin(t*9+j*.7))*Math.abs(Math.sin(t*2.3+j)))+'px'}});
 show($('t1'),t,s2+.6);show($('t2'),t,s2+1.8);
 const s3=ST[3];show($('d1'),t,s3+.1);show($('d2'),t,s3+1.0);show($('d3'),t,s3+2.2);show($('d4'),t,s3+3.1);
 const s4=ST[4];show($('r1'),t,s4+.1);show($('r2'),t,s4+1.0);show($('r3'),t,s4+1.5);show($('r4'),t,s4+2.0,.45,80);
 const s5=ST[5];const cp=ease((t-s5-.2)/2.6);$('cn').textContent=Math.round(48*cp);
 [...$('br').children].forEach((b,j)=>{{const h=[22,30,28,40,46,52,60,70,82,96][j];b.style.height=(h*3.2*ease((t-s5-.2-j*.18)/.6))+'px'}});
 let c='';for(let i=0;i<LN.length;i++)if(t>=ST[i]&&t<ST[i]+DU[i]+.25)c=LN[i].replace('A.I.','AI');$('cc').innerHTML=c?'<span>'+c+'</span>':'';
}};render(0);
</script></body></html>'''
open(out, 'w').write(html); print("END", END, "starts", st)
