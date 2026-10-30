import html, json, os, sys
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
s = open('/home/claude/shot/og.html').read()
FONTS = s[s.find('<style>') + 7:s.find('body{')]
LOGO = open('/home/claude/shot/logo_on_dark.svg').read()
E = html.escape

ADS = [
 dict(id="01-dm-9pm", kick="Instagram DM · 9:14 PM",
      h='She asked about lip filler at 9 PM. <span class="aq">Who answered?</span>',
      chat=[("u","Hi! How much is lip filler and do you have anything this week?"),
            ("a","Hi! Lip filler starts from $650. We have Thursday 4:00 or Saturday 11:00. Which works?"),
            ("u","Saturday 11 please!"),
            ("a","Booked ✓ Here is your $50 deposit link to hold the spot.")],
      foot="Every DM answered in seconds, 24/7."),
 dict(id="02-missed-call", kick="Missed call · 2:47 PM",
      h='Mid-treatment when the phone rings? <span class="aq">It texts them back.</span>',
      chat=[("sys","Missed call from (512) ••• ••21"),
            ("a","Hi, sorry we missed your call! We are with a client. Want to book a consultation? Tap here: [link]"),
            ("u","Yes, looking for Botox next week"),
            ("a","Perfect. Tuesday 1:30 or Wednesday 5:00?")],
      foot="Missed calls turned into bookings, automatically."),
 dict(id="03-no-shows", kick="Day before · 10:00 AM",
      h='Free consults that never show? <span class="aq">Deposits and reminders.</span>',
      chat=[("a","Reminder: your consultation is tomorrow at 11:00. Reply C to confirm or R to reschedule."),
            ("u","R, something came up"),
            ("a","No problem! Your deposit carries over. Friday 2:00 or Saturday 10:30?"),
            ("u","Saturday works")],
      foot="Fewer empty chairs. Rescheduled, not lost."),
 dict(id="04-rebook-month4", kick="Text message · Month 4",
      h='Botox clients drifting past month four? <span class="aq">Rebooked on time.</span>',
      chat=[("a","Hi Sarah! It's about 4 months since your last Botox. Want to book before it wears off? [link]"),
            ("u","Yes please, same injector"),
            ("a","Done! Booked with Jess on the 14th at 2:00.")],
      foot="Rebooking reminders for every treatment on your menu."),
]

CSS = FONTS + '''
*{box-sizing:border-box}
body{margin:0;width:1080px;height:HPX;overflow:hidden;font-family:Inter,sans-serif;background:#0E1A1B;color:#fff;position:relative}
.hatch{position:absolute;top:0;right:0;width:46%;height:420px;background:repeating-linear-gradient(135deg,#3DE3C8 0 3px,transparent 3px 14px);-webkit-mask-image:linear-gradient(225deg,#000 0%,transparent 62%);opacity:.55}
.glow{position:absolute;left:0;bottom:0;width:100%;height:600px;background:radial-gradient(60% 80% at 0% 100%,rgba(255,118,87,.16),transparent 70%)}
.w{position:absolute;inset:PADT 80px PADB;display:flex;flex-direction:column}
.k{align-self:flex-start;font-family:"Inter Tight";font-weight:600;font-size:26px;letter-spacing:.06em;text-transform:uppercase;padding:10px 20px;border-radius:999px;background:#FF7657;color:#0E1A1B}
h1{font-family:"Inter Tight";font-weight:600;letter-spacing:-.045em;line-height:1.02;margin:30px 0 0;font-size:HSIZEpx;text-wrap:balance}
.aq{color:#3DE3C8}
.ph{margin-top:GAPpx;background:#F4F8F7;border-radius:30px;padding:30px;color:#0E1A1B;font-size:CHATpx;line-height:1.38;display:flex;flex-direction:column;gap:20px}
.q{align-self:flex-end;background:#0E1A1B;color:#fff;border-radius:22px 22px 6px 22px;padding:20px 26px;max-width:80%}
.a{align-self:flex-start;background:#fff;border:1px solid #DCE5E3;border-radius:22px 22px 22px 6px;padding:20px 26px;max-width:88%}
.who{display:block;font-family:"Inter Tight";font-weight:600;font-size:19px;letter-spacing:.06em;text-transform:uppercase;color:#0E9C87;margin-bottom:4px}
.sys{align-self:center;font-size:20px;font-weight:600;color:#BF3A1F;background:#FDE9E4;padding:8px 16px;border-radius:999px}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;gap:24px;border-top:2px solid #2A3A3A;padding-top:26px}
.foot p{margin:0;font-family:"Inter Tight";font-weight:600;font-size:34px;letter-spacing:-.02em;line-height:1.2;max-width:560px}
.foot p small{display:block;font-family:Inter;font-weight:500;font-size:22px;color:#9DB0AD;letter-spacing:0;margin-top:8px}
.foot svg{height:52px;width:auto;flex:none}
'''

def page(ad, h):
    tall = h > 1500
    css = (CSS.replace('HPX', f'{h}px').replace('PADT', '250px' if tall else '78px').replace('PADB', '300px' if tall else '68px')
              .replace('HSIZE', '88' if tall else '76').replace('GAP', '60' if tall else '40').replace('CHAT', '34' if tall else '31'))
    chat = []
    for w, t in ad["chat"]:
        if w == "u": chat.append(f'<div class="q">{E(t)}</div>')
        elif w == "sys": chat.append(f'<div class="sys">{E(t)}</div>')
        else: chat.append(f'<div class="a"><span class="who">Your clinic</span>{E(t)}</div>')
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="hatch"></div><div class="glow"></div>
<div class="w"><span class="k">{E(ad["kick"])}</span><h1>{ad["h"]}</h1>
<div class="ph">{"".join(chat)}</div>
<div class="foot"><p>{E(ad["foot"])}<small>Built for your med spa in 14 days.</small></p>{LOGO}</div></div></body></html>'''

jobs = []
for ad in ADS:
    for tag, h in (("4x5", 1350), ("9x16", 1920)):
        f = f'{OUT}/{ad["id"]}_{tag}.html'
        open(f, 'w').write(page(ad, h)); jobs.append([f, f[:-5] + '.png', h])
json.dump(jobs, open(f'{OUT}/jobs.json', 'w'))
