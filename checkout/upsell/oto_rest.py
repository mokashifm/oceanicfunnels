# Block 2 (everything below the GHL buttons) for the upsell/downsell pages.
# Uses the base styles from block 1 (.oto, .oto-btn, .oto-faq ...) plus its own premium elements (.ox-*).

CSS2 = r'''<style>
.ox-sec{margin-top:64px}
.ox-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#0E9C87}
.ox-eyebrow:before{content:"";width:7px;height:7px;border-radius:50%;background:#3DE3C8;box-shadow:0 0 0 4px rgba(61,227,200,.18)}
.ox-dark .ox-eyebrow{color:#3DE3C8}
.ox-c{text-align:center}
.ox-c .oto-p{max-width:600px;margin-left:auto;margin-right:auto}
.oto h2.ox-h{margin-top:10px}

/* reveal on scroll */
.ox-rv{opacity:0;transform:translateY(26px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
.ox-rv.in{opacity:1;transform:none}

/* 1. race card: on your own vs with our team */
.ox-race{background:#fff;border:1px solid #DCE6E3;border-radius:22px;padding:28px 28px 24px;margin-top:26px;box-shadow:0 30px 60px -44px rgba(14,26,27,.55)}
.ox-lane+.ox-lane{margin-top:26px;padding-top:24px;border-top:1px dashed #DCE6E3}
.ox-lane-h{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.ox-lane-h b{font-size:15px;font-weight:800;color:#0E1A1B}
.ox-lane-h span{font-size:13px;color:#5B6967}
.ox-steps{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.ox-steps i{font-style:normal;font-size:13px;font-weight:600;padding:7px 12px;border-radius:999px;background:#F1F4F3;color:#5B6967;border:1px solid #E3EAE8}
.ox-lane.us .ox-steps i{background:#DDF7F2;color:#0A7F6E;border-color:#BDEFE5}
.ox-track{position:relative;height:12px;border-radius:99px;background:#EEF2F1;margin-top:16px;overflow:visible}
.ox-track u{position:absolute;left:0;top:0;bottom:0;border-radius:99px;width:0;transition:width 2.2s cubic-bezier(.3,.7,.2,1) .2s}
.ox-lane.me .ox-track u{background:repeating-linear-gradient(-45deg,#C9D3D1 0 8px,#D8E0DE 8px 16px)}
.ox-lane.us .ox-track u{background:linear-gradient(90deg,#3DE3C8,#0E9C87);box-shadow:0 6px 18px -6px rgba(14,156,135,.7)}
.ox-race.in .ox-lane.me .ox-track u{width:92%}
.ox-race.in .ox-lane.us .ox-track u{width:34%}
.ox-pin{position:absolute;top:50%;transform:translate(-50%,-50%);white-space:nowrap;font-size:12px;font-weight:800;padding:6px 11px;border-radius:999px;opacity:0;transition:opacity .5s 2.2s}
.ox-race.in .ox-pin{opacity:1}
.ox-lane.me .ox-pin{left:92%;background:#fff;color:#BF3A1F;border:1.5px dashed #F2A08E}
.ox-lane.us .ox-pin{left:34%;background:#0E1A1B;color:#3DE3C8;box-shadow:0 0 0 6px rgba(61,227,200,.18)}

/* dark panels */
.ox-dark{position:relative;background:#0B1516;color:#C9D6D3;border-radius:28px;padding:56px 36px 44px;overflow:hidden;isolation:isolate}
.ox-dark:before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(60% 50% at 50% 0%,rgba(61,227,200,.16),transparent 70%)}
.ox-dark .oto-p{color:#B7C6C3}
.ox-dark .oto-p b{color:#fff}
.oto .ox-dark h2{color:#fff}
.oto .ox-dark h2 em{color:#3DE3C8}

/* 2. page covers */
.ox-covers{display:grid;grid-template-columns:repeat(var(--n,3),minmax(0,1fr));gap:22px;max-width:680px;margin:36px auto 0;perspective:900px}
.ox-cover{position:relative;aspect-ratio:3/4;border-radius:4px 10px 10px 4px;padding:16% 13% 12% 19%;display:flex;flex-direction:column;overflow:hidden;
 background:linear-gradient(158deg,var(--c1),var(--c2));color:var(--fg);box-shadow:inset 0 1px 0 rgba(255,255,255,.1),0 36px 46px -28px rgba(0,0,0,.8),0 12px 18px -10px rgba(0,0,0,.5);
 transition:transform .6s cubic-bezier(.2,.7,.2,1);text-align:left}
.ox-cover:hover{transform:translateY(-8px) rotateX(4deg)}
.ox-cover:before{content:"";position:absolute;inset:0 auto 0 0;width:8%;background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(255,255,255,.12) 65%,rgba(0,0,0,.15))}
.ox-cover:after{content:"";position:absolute;top:10%;right:12%;width:22%;aspect-ratio:100/138;border:1px solid currentColor;border-bottom:0;border-radius:999px 999px 0 0;opacity:.5}
.ox-cover small{font-size:11px;font-weight:600;letter-spacing:.06em;opacity:.85}
.ox-cover b{margin-top:auto;font-family:Anton,Impact,sans-serif;font-weight:400;font-size:27px;line-height:1.02;text-transform:uppercase;letter-spacing:.01em}
.ox-cover em{font-style:normal;margin-top:12px;font-size:9px;font-weight:700;letter-spacing:.32em;opacity:.7}
.ox-cover .gl{position:absolute;inset:0;pointer-events:none;background:radial-gradient(circle at var(--gx,30%) var(--gy,18%),rgba(255,255,255,.28),transparent 48%)}
.ox-c1{--c1:#1B2B2C;--c2:#060D0E;--fg:#3DE3C8}
.ox-c2{--c1:#4AF0D4;--c2:#11B79E;--fg:#0E1A1B}
.ox-c3{--c1:#FFFFFF;--c2:#E4ECEA;--fg:#0E1A1B}
.ox-offer{margin:40px auto 0;max-width:640px;text-align:center}
.ox-offer h3{font-family:Anton,Impact,sans-serif;font-weight:400;font-size:26px;letter-spacing:.03em;text-transform:uppercase;color:#fff}

/* 3. what you get */
.ox-get{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:26px}
.ox-get div{display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #DCE6E3;border-radius:16px;padding:18px 18px;transition:border-color .3s,transform .3s,box-shadow .3s}
.ox-get div:hover{border-color:#3DE3C8;transform:translateY(-3px);box-shadow:0 22px 40px -30px rgba(14,26,27,.6)}
.ox-get svg{flex:0 0 26px;margin-top:1px}
.ox-get p{font-size:16px;line-height:1.5}
.ox-get p b{display:block;color:#0E1A1B;font-size:16.5px}
.ox-get p span{color:#5B6967;font-size:14.5px}

/* 4. highlight-on-scroll list */
.ox-why{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;text-align:left}
.ox-why-l{position:sticky;top:90px;align-self:start}
.ox-why-list{display:grid}
.ox-why-list div{padding:22px 0;border-top:1px solid rgba(255,255,255,.1);opacity:.32;transition:opacity .5s}
.ox-why-list div.lit{opacity:1}
.ox-why-list h4{font-size:21px;font-weight:700;color:#fff;letter-spacing:-.01em}
.ox-why-list div.lit h4{color:#3DE3C8}
.ox-why-list p{margin-top:8px;font-size:15.5px;line-height:1.6;color:#B7C6C3}

/* 5. final: arches + seal */
.ox-final{text-align:center;padding-top:64px}
.ox-arches{position:absolute;left:50%;top:40px;transform:translateX(-50%);width:900px;height:900px;z-index:-1;pointer-events:none}
.ox-arches i{position:absolute;left:50%;top:0;transform:translateX(-50%);border:1px solid rgba(61,227,200,.13);border-bottom:0;border-radius:999px 999px 0 0;height:100%}
.ox-seal{position:relative;width:130px;height:130px;margin:0 auto 26px;color:#3DE3C8}
.ox-seal svg{width:100%;height:100%;overflow:visible}
.ox-seal .ring{transform-origin:50% 50%;animation:oxSpin 22s linear infinite}
.ox-seal text{fill:currentColor;font:700 9.5px Inter,sans-serif;letter-spacing:3.6px}
@keyframes oxSpin{to{transform:rotate(360deg)}}
.ox-final .oto-ok{max-width:380px;margin:18px auto 0;text-align:left}
.ox-final .oto-ok li{color:#E6F2EF}
.ox-price{margin-top:30px;display:inline-flex;align-items:baseline;gap:12px;padding:14px 26px;border-radius:16px;border:1px solid rgba(61,227,200,.35);background:rgba(61,227,200,.06)}
.ox-price span{font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#B7C6C3}
.ox-price b{font-family:Anton,Impact,sans-serif;font-weight:400;font-size:48px;line-height:1;color:#fff}
.ox-note{font-size:14px;color:#8FA3A0;margin-top:10px}

@media(max-width:720px){
 .ox-sec{margin-top:48px}
 .ox-race{padding:22px 18px 20px}
 .ox-dark{padding:44px 20px 34px;border-radius:22px}
 .ox-covers{gap:10px}.ox-cover b{font-size:16px}.ox-cover small{font-size:9px}.ox-cover em{font-size:7px;letter-spacing:.2em}
 .ox-get{grid-template-columns:1fr}
 .ox-why{grid-template-columns:1fr;gap:10px}.ox-why-l{position:static}
 .ox-price b{font-size:40px}
 .ox-lane.me .ox-pin{left:78%}.ox-race.in .ox-lane.me .ox-track u{width:78%}
 .ox-race.in .ox-lane.us .ox-track u{width:40%}.ox-lane.us .ox-pin{left:40%}}
@media(prefers-reduced-motion:reduce){.ox-rv{opacity:1;transform:none;transition:none}.ox-seal .ring{animation:none}.ox-track u,.ox-pin{transition:none}}
</style>
'''

CHECK = '<svg viewBox="0 0 26 26" width="26" height="26" aria-hidden="true"><circle cx="13" cy="13" r="13" fill="#DDF7F2"/><path d="M7.5 13.5l3.6 3.6 7.4-8" fill="none" stroke="#0E9C87" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

SEAL = '''<div class="ox-seal" aria-hidden="true"><svg viewBox="0 0 130 130">
  <defs><path id="oxc" d="M65,65 m-52,0 a52,52 0 1,1 104,0 a52,52 0 1,1 -104,0"/></defs>
  <g class="ring"><text><textPath href="#oxc" textLength="322" lengthAdjust="spacing">OCEANIC FUNNELS &#8226; DONE FOR YOU &#8226; </textPath></text></g>
  <circle cx="65" cy="65" r="36" fill="none" stroke="currentColor" stroke-opacity=".45"/>
  <path d="M50 52h30l-11 13v12l-8 4v-16z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/>
</svg></div>'''

JS2 = r'''<script>
(function(){
  var rv=document.querySelectorAll('.oto .ox-rv');
  if(!('IntersectionObserver' in window)){rv.forEach(function(e){e.classList.add('in')});document.querySelectorAll('.ox-why-list div').forEach(function(e){e.classList.add('lit')});}
  else{
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.18});
    rv.forEach(function(e){io.observe(e)});
    var lo=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)e.target.classList.add('lit')})},{rootMargin:'-35% 0px -45% 0px'});
    document.querySelectorAll('.ox-why-list div').forEach(function(e){lo.observe(e)});
  }
  document.querySelectorAll('.ox-cover').forEach(function(c){c.addEventListener('mousemove',function(ev){var r=c.getBoundingClientRect();
    c.style.setProperty('--gx',((ev.clientX-r.left)/r.width*100)+'%');c.style.setProperty('--gy',((ev.clientY-r.top)/r.height*100)+'%');});});
})();
</script>
'''


def rest(kind, up, p, B, q, pain_intro, pain, pain_end, diff_h, diff, band, get):
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    covers = [("ox-c1", "Page 01", "Sales<br>page"), ("ox-c2", "Page 02", "Checkout<br>page")]
    if up:
        covers.append(("ox-c3", "Page 03", "Thank-you<br>page"))
    cov = "".join(f'<div class="ox-cover {c}"><small>{t}</small><b>{n}</b><em>OCEANIC FUNNELS</em><span class="gl"></span></div>' for c, t, n in covers)

    def get_item(x):
        head, _, tail = x.partition("</b>")
        return f'<div>{CHECK}<p><b>{head.replace("<b>", "")}</b><span>{tail.strip(" ,")}</span></p></div>'
    gets = "".join(get_item(x) for x in get)

    me_steps = "".join(f"<i>{x}</i>" for x in ["Learn the builder", "Write the copy", "Design the pages", "Connect checkout", "Fix it on mobile"])
    us_steps = "".join(f"<i>{x}</i>" for x in ["Tell us about your offer", "We build it for you"])

    return f'''<!-- OCEANIC FUNNELS {kind.upper()} ({p}) BLOCK 2 of 2: Custom Code element BELOW your GHL buttons. Red buttons scroll back up to them. -->
{CSS2}<section class="oto rest"><div class="oto-w">

  <div class="ox-sec ox-c ox-rv">
    <span class="ox-eyebrow">{"The real problem" if up else "You're not alone"}</span>
    <h2 class="ox-h">{q}</h2>
    <p class="oto-p">{pain_intro} {pain[0].lower()}, {pain[1].lower()}, and {pain[2][0].lower() + pain[2][1:].rstrip(".").lower()}. <b>{pain_end}</b></p>
  </div>
  <div class="ox-race ox-rv" aria-label="Doing it yourself compared with having it built">
    <div class="ox-lane me">
      <div class="ox-lane-h"><b>Doing it on your own</b><span>one step at a time</span></div>
      <div class="ox-steps">{me_steps}</div>
      <div class="ox-track"><u></u><span class="ox-pin">Still not live</span></div>
    </div>
    <div class="ox-lane us">
      <div class="ox-lane-h"><b>With our team</b><span>{p}, one time</span></div>
      <div class="ox-steps">{us_steps}</div>
      <div class="ox-track"><u></u><span class="ox-pin">&#10003; Live</span></div>
    </div>
  </div>

  <div class="ox-sec ox-dark ox-c ox-rv">
    <span class="ox-eyebrow">{"What changes" if up else "The smaller version"}</span>
    <h2 class="ox-h">{diff_h}</h2>
    {diff}
    <div class="ox-covers" style="--n:{len(covers)}">{cov}</div>
    <div class="ox-offer"><h3>{band}</h3>{B}</div>
  </div>

  <div class="ox-sec ox-c ox-rv">
    <span class="ox-eyebrow">Included for {p}</span>
    <h2 class="ox-h">What you're <em>getting</em></h2>
  </div>
  <div class="ox-get ox-rv">{gets}</div>
  {B}

  <div class="ox-sec ox-dark ox-rv">
    <div class="ox-why">
      <div class="ox-why-l"><span class="ox-eyebrow">How we build</span><h2 class="ox-h">What makes this <em>powerful</em></h2>
        <p class="oto-p">You don't get a template and a "good luck." <b>You're not doing this alone.</b></p></div>
      <div class="ox-why-list">
        <div><h4>A clear path to checkout</h4><p>Every section walks your visitor one step closer to buying, from the headline to the order button.</p></div>
        <div><h4>Your offer, positioned clearly</h4><p>We shape the page around what you sell and who it's for, so people understand it in seconds.</p></div>
        <div><h4>Set up to sell</h4><p>Your checkout is connected and ready, so the page can take payments from day one.</p></div>
        <div><h4>Yours to edit</h4><p>Everything is built inside your own account. Change words, images and prices whenever you like.</p></div>
      </div>
    </div>
    {B}
  </div>

  <div class="ox-sec ox-dark ox-final ox-rv">
    <div class="ox-arches"><i style="width:900px"></i><i style="width:700px;top:100px;height:800px"></i><i style="width:500px;top:200px;height:700px"></i></div>
    {SEAL}
    <h2 class="ox-h">Let's be <em>real</em></h2>
    <p class="oto-p">Without a sales funnel, you can't sell your offer. You're just preparing. This upgrade helps you:</p>
    <ul class="oto-ok"><li>Get your offer live</li><li>Start collecting customers</li><li>Move toward your first sale faster</li></ul>
    <div class="ox-price"><span>One-time upgrade</span><b>{p}</b></div>
    <p class="ox-note">One-time payment, no subscription. This offer is only available on this page.</p>
    {B}
  </div>

  <div class="ox-sec">
    <h2 style="text-align:center">Questions</h2>
    <div class="oto-faq">
      <details><summary>Do I need to enter my card again?</summary><p>No. Click the red button and it's added to the order you just placed.</p></details>
      <details><summary>Is this a subscription?</summary><p>No. It's a one-time payment of {p}. Your Launch plan stays $17/month.</p></details>
      <details><summary>Can I edit the funnel after you build it?</summary><p>Yes. It's built inside your own account, so you can change text, images and prices anytime.</p></details>
      <details><summary>What if I don't have an offer yet?</summary><p>That's fine. Tell us what you know or what you'd like to sell, and we'll help you shape it into a first offer.</p></details>
    </div>
  </div>
  <p class="oto-foot">&copy; 2026 Oceanic Funnels &middot; <a href="https://oceanicfunnels.com/privacy/">Privacy</a> &middot; <a href="https://oceanicfunnels.com/terms/">Terms</a> &middot; <a href="mailto:hello@oceanicfunnels.com">hello@oceanicfunnels.com</a></p>
</div></section>
{JS2}'''
