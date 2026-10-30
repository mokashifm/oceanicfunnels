# Reel 1: "9:14 PM" — 12s, 1080x1920. Renders HTML with render(t) for frame capture.
import sys
s = open('/home/claude/shot/og.html').read()
FONTS = s[s.find('<style>') + 7:s.find('body{')]
LOGO = open('/home/claude/shot/logo_on_dark.svg').read()
HTML = '''<!doctype html><html><head><meta charset="utf-8"><style>''' + FONTS + '''
*{box-sizing:border-box;margin:0}
body{width:1080px;height:1920px;overflow:hidden;background:#0E1A1B;font-family:Inter,sans-serif;color:#fff;position:relative}
.hatch{position:absolute;top:0;right:0;width:50%;height:520px;background:repeating-linear-gradient(135deg,#3DE3C8 0 3px,transparent 3px 14px);-webkit-mask-image:linear-gradient(225deg,#000 0%,transparent 62%);opacity:.45}
.sc{position:absolute;inset:0;padding:200px 80px 380px;opacity:0}
.clock{font-family:"Inter Tight";font-weight:600;font-size:230px;letter-spacing:-.05em;text-align:center;line-height:1;margin-top:40px}
.date{text-align:center;font-size:40px;color:#9DB0AD;margin-top:14px}
.cap{font-family:"Inter Tight";font-weight:600;font-size:76px;letter-spacing:-.04em;line-height:1.05;text-align:center;margin-top:70px}
.aq{color:#3DE3C8}
.nt{background:rgba(244,248,247,.96);color:#0E1A1B;border-radius:34px;padding:28px 32px;margin-top:26px;font-size:34px;line-height:1.35;opacity:0}
.nt b{display:flex;justify-content:space-between;font-family:"Inter Tight";font-weight:600;font-size:26px;letter-spacing:.04em;text-transform:uppercase;color:#5B6967;margin-bottom:6px}
.nt b i{font-style:normal;text-transform:none;letter-spacing:0}
.ph{background:#F4F8F7;border-radius:40px;padding:36px;color:#0E1A1B;font-size:38px;line-height:1.38;display:flex;flex-direction:column;gap:24px;margin-top:50px}
.q,.a,.typing,.chip{opacity:0}
.q{align-self:flex-end;background:#0E1A1B;color:#fff;border-radius:28px 28px 8px 28px;padding:24px 30px;max-width:82%}
.a{align-self:flex-start;background:#fff;border:1px solid #DCE5E3;border-radius:28px 28px 28px 8px;padding:24px 30px;max-width:88%}
.who{display:block;font-family:"Inter Tight";font-weight:600;font-size:22px;letter-spacing:.06em;text-transform:uppercase;color:#0E9C87;margin-bottom:6px}
.typing{align-self:flex-start;background:#fff;border:1px solid #DCE5E3;border-radius:28px;padding:22px 30px;font-size:44px;letter-spacing:6px;color:#9DB0AD}
.chip{align-self:center;background:#3DE3C8;color:#0E1A1B;font-family:"Inter Tight";font-weight:600;font-size:36px;padding:16px 30px;border-radius:999px}
.k{display:inline-block;font-family:"Inter Tight";font-weight:600;font-size:30px;letter-spacing:.06em;text-transform:uppercase;padding:12px 24px;border-radius:999px;background:#FF7657;color:#0E1A1B}
.end{display:flex;flex-direction:column;align-items:center;text-align:center;justify-content:center;height:100%}
.end h2{font-family:"Inter Tight";font-weight:600;font-size:96px;letter-spacing:-.045em;line-height:1.02;margin-top:40px}
.end p{font-size:42px;color:#C9D6D4;margin-top:34px;line-height:1.35}
.end .btn{margin-top:60px;background:#3DE3C8;color:#0E1A1B;font-family:"Inter Tight";font-weight:600;font-size:44px;padding:30px 56px;border-radius:999px}
.end svg{height:80px;width:auto;margin-top:70px}
</style></head><body><div class="hatch"></div>
<div class="sc" id="s1"><div class="clock">9:14</div><div class="date">Saturday night</div><div class="cap">Your clinic is closed.<br><span class="aq">Your inbox isn't.</span></div>
<div class="nt" id="n1"><b>Instagram <i>now</i></b>Hi! How much is lip filler? Anything this week?</div>
<div class="nt" id="n2"><b>Missed call <i>2m ago</i></b>(512) ••• ••21</div>
<div class="nt" id="n3"><b>Website chat <i>5m ago</i></b>Do you do laser hair removal?</div></div>
<div class="sc" id="s2"><span class="k">Instagram DM · 9:14 PM</span><div class="ph">
<div class="q" id="c1">Hi! How much is lip filler? Anything this week?</div>
<div class="typing" id="ty">•••</div>
<div class="a" id="c2"><span class="who">Your clinic</span>Lip filler starts from $650. We have Thursday 4:00 or Saturday 11:00. Which works?</div>
<div class="q" id="c3">Saturday 11 please!</div>
<div class="a" id="c4"><span class="who">Your clinic</span>Booked! Here is your $50 deposit link to hold the spot.</div>
<div class="chip" id="c5">✓ Booked · deposit paid</div></div><div class="cap" id="c6" style="opacity:0;margin-top:60px">Answered in seconds.<br><span class="aq">While you were off.</span></div></div>
<div class="sc" id="s3"><div class="end"><span class="k">Answered in seconds · 24/7</span><h2>Every DM, call and enquiry <span class="aq">answered and booked.</span></h2><p>Built for your med spa in 14 days.<br>No sales team needed.</p><div class="btn">Book a free info call →</div>''' + LOGO + '''</div></div>
<script>
const $=i=>document.getElementById(i);
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
function show(el,t,t0,d=.35,dy=40){el.style.display=t<t0?'none':'';const p=ease((t-t0)/d);el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px)`}
function scene(el,t,a,b){const fi=ease((t-a)/.3),fo=ease((t-(b-.3))/.3);el.style.opacity=Math.min(fi,1-fo)}
window.render=function(t){
 scene($('s1'),t,0,4.6); show($('n1'),t,1.3); show($('n2'),t,2.0); show($('n3'),t,2.7);
 scene($('s2'),t,4.6,10.0); show($('c1'),t,4.9);
 const ty=$('ty'); const tp=(t>5.6&&t<6.6); ty.style.display=tp?'block':'none'; ty.style.opacity=tp?1:0; ty.textContent=['•  ','•• ','•••'][Math.floor(t*4)%3];
 show($('c2'),t,6.6); show($('c3'),t,7.7); show($('c4'),t,8.5); const c5=$('c5'); c5.style.display=t<9.1?'none':''; const p=ease((t-9.1)/.3); c5.style.opacity=p; c5.style.transform=`scale(${.85+.15*p})`;
 show($('c6'),t,6.7,.4,30); scene($('s3'),t,10.0,14.5);
}
render(0);
</script></body></html>'''
open(sys.argv[1], 'w').write(HTML)
