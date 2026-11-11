# Builds the one-click upsell ($97) and downsell ($67) pages for GHL as ONE custom-code block each.
# The red buttons in the design click two native GHL buttons (texts OTO-YES / OTO-NO) that the script hides.

CSS = r'''<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
.oto{--ink:#0E1A1B;--aqua:#3DE3C8;--aqd:#0E9C87;--aql:#DDF7F2;--red:#E0242B;--redd:#B81A20;--mist:#EEF5F3;--line:#DCE6E3;--mut:#5B6967;
 font-family:Inter,system-ui,sans-serif;color:#25302F;background:#F3F7F6 url(https://assets.cdn.filesafe.space/NgdMDKbJ5CKK0QEKnkDw/media/6679e1ebcb186051ca415a59.png) repeat center top;padding:22px 0 10px;overflow:hidden}
.oto.top{padding-bottom:6px}.oto.rest{padding-top:6px}
.oto *{box-sizing:border-box;margin:0;padding:0}
.oto-w{max-width:860px;margin:0 auto;padding:0 18px}
.oto-prog{max-width:420px;margin:0 auto;background:#E2EAE8;border-radius:999px;height:22px;overflow:hidden;position:relative}
.oto-prog i{position:absolute;inset:0 18% 0 0;border-radius:999px;background:repeating-linear-gradient(-45deg,var(--aqd) 0 12px,#13B39B 12px 24px);animation:otoBar 1.2s linear infinite;background-size:34px 34px}
.oto-prog span{position:relative;display:block;text-align:center;font-size:12px;font-weight:700;color:#fff;line-height:22px;letter-spacing:.04em}
@keyframes otoBar{to{background-position:34px 0}}
.oto-kick{text-align:center;margin-top:20px;font-family:Anton,Impact,sans-serif;font-size:22px;letter-spacing:.02em;text-transform:uppercase;color:var(--ink)}
.oto-kick b{font-weight:400;color:var(--aqd)}
.oto h1{text-align:center;font-family:Anton,Impact,sans-serif;font-weight:400;font-size:64px;line-height:1.02;text-transform:uppercase;color:var(--ink);margin-top:6px;letter-spacing:.005em}
.oto h1 em{font-style:normal;color:var(--aqd)}
.oto h1 u{text-decoration:none;color:var(--red)}
.oto-sub{text-align:center;font-size:19px;line-height:1.55;color:var(--mut);max-width:640px;margin:14px auto 0}
.oto-hero{position:relative;margin:26px auto 0;max-width:720px;background:#fff;border:6px solid var(--aqua);border-radius:14px;padding:26px 22px 18px;box-shadow:0 26px 50px -30px rgba(14,26,27,.55)}
.oto-hero img{display:block;width:100%;height:auto}
.oto-split.rev{grid-template-columns:.8fr 1.2fr}
.oto-badge{position:absolute;top:-18px;left:50%;transform:translateX(-50%);background:var(--ink);color:var(--aqua);font-family:Anton,Impact,sans-serif;font-size:18px;letter-spacing:.06em;text-transform:uppercase;padding:7px 18px;border-radius:999px;white-space:nowrap}
.oto-cta{max-width:640px;margin:26px auto 0;text-align:center}
.oto-btn{display:block;width:100%;border:0;cursor:pointer;background:var(--red);color:#fff;font-family:Inter,sans-serif;font-weight:800;font-size:21px;letter-spacing:.01em;text-transform:uppercase;padding:18px 18px 14px;border-radius:10px;box-shadow:0 5px 0 var(--redd),0 16px 30px -12px rgba(224,36,43,.65);transition:transform .12s,box-shadow .12s;animation:otoPulse 2.4s ease-in-out infinite;text-decoration:none}
.oto-btn small{display:block;font-size:13.5px;font-weight:500;text-transform:none;opacity:.92;margin-top:4px;letter-spacing:0}
.oto-btn:hover{transform:translateY(2px);box-shadow:0 3px 0 var(--redd),0 10px 22px -12px rgba(224,36,43,.65)}
.oto-btn[disabled]{opacity:.75;cursor:wait;animation:none}
@keyframes otoPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.025)}}
.oto-no{display:inline-block;margin-top:12px;background:none;border:0;cursor:pointer;font:500 14px Inter,sans-serif;color:var(--mut);text-decoration:underline}
.oto-sec{margin-top:54px}
.oto h2{font-family:Anton,Impact,sans-serif;font-weight:400;font-size:40px;line-height:1.08;text-transform:uppercase;color:var(--ink);letter-spacing:.01em}
.oto h2 em{font-style:normal;color:var(--aqd)}
.oto-split{display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.oto-p{font-size:17px;line-height:1.6;margin-top:12px}
.oto-ok,.oto-x{list-style:none;display:grid;gap:12px;margin-top:16px}
.oto-ok li,.oto-x li{position:relative;padding-left:36px;font-size:17px;line-height:1.5}
.oto-ok li:before,.oto-x li:before{position:absolute;left:0;top:0;width:25px;height:25px;border-radius:6px;display:grid;place-items:center;font-size:14px;font-weight:800}
.oto-ok li:before{content:"\2713";background:var(--aqd);color:#fff}
.oto-x li:before{content:"\2715";background:#FFE1E1;color:var(--red)}
.oto-ok b,.oto-x b{color:var(--ink)}
.oto-chart{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px 22px 16px;box-shadow:0 20px 40px -30px rgba(14,26,27,.5)}
.oto-chart .t{display:flex;justify-content:space-between;font-size:13px;font-weight:700;color:var(--mut)}
.oto-chart .t b{color:var(--aqd);font-size:22px;font-weight:800}
.oto-bars{display:flex;align-items:flex-end;gap:10px;height:150px;margin-top:14px;border-bottom:2px solid var(--line)}
.oto-bars i{flex:1;border-radius:7px 7px 0 0;background:linear-gradient(var(--aqua),var(--aqd))}
.oto-chart .n{display:flex;gap:10px;margin-top:8px;font-size:11px;color:var(--mut)}
.oto-chart .n span{flex:1;text-align:center}
.oto-toast{display:flex;align-items:center;gap:10px;margin-top:14px;background:var(--mist);border-radius:12px;padding:10px 12px;font-size:13.5px}
.oto-toast i{width:30px;height:30px;border-radius:50%;background:var(--aqd);color:#fff;display:grid;place-items:center;font-style:normal;font-weight:800}
.oto-toast b{color:var(--ink)}
.oto-card{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 24px 50px -36px rgba(14,26,27,.5)}
.oto-card-in{display:grid;grid-template-columns:200px 1fr;gap:28px;align-items:center;padding:30px}
.oto-band{background:var(--aqd);padding:24px 24px 22px;text-align:center}
.oto-band h3{font-family:Anton,Impact,sans-serif;font-weight:400;font-size:28px;text-transform:uppercase;color:#fff;letter-spacing:.02em}
.oto-band .oto-cta{margin-top:16px}
.oto-band .oto-no{color:#E6FFFA}
.oto-tag{display:inline-block;font-size:12.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--aqd);background:var(--aql);padding:5px 12px;border-radius:999px;margin-bottom:10px}
.oto-phone{width:230px;margin:0 auto;background:#1B2323;border-radius:34px;padding:10px;box-shadow:0 30px 50px -24px rgba(14,26,27,.6);transform:rotate(-4deg)}
.oto-phone img{display:block;width:100%;height:auto;border-radius:25px}
.oto-panel{background:#fff;border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 24px 50px -36px rgba(14,26,27,.5)}
.oto-panel-h{background:var(--ink);padding:16px 22px;text-align:center}
.oto-panel-h h3{font-family:Anton,Impact,sans-serif;font-weight:400;font-size:28px;text-transform:uppercase;color:var(--aqua);letter-spacing:.02em}
.oto-panel-b{padding:28px 30px 30px}
.oto-real{text-align:center}
.oto-real .line{width:120px;height:5px;border-radius:5px;background:var(--aqua);margin:12px auto 0}
.oto-real .oto-p{max-width:560px;margin-left:auto;margin-right:auto}
.oto-real .oto-ok{max-width:420px;margin:18px auto 0;text-align:left}
.oto-price{margin-top:28px;font-family:Anton,Impact,sans-serif;font-size:40px;text-transform:uppercase;color:var(--ink)}
.oto-price em{font-style:normal;color:var(--aqd)}
.oto-price s{color:var(--red);font-size:.7em;margin-right:8px}
.oto-note{font-size:15px;color:var(--mut);margin-top:6px}
.oto-faq{display:grid;gap:10px;margin-top:20px}
.oto-faq details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:15px 18px}
.oto-faq summary{cursor:pointer;font-weight:700;font-size:16px;color:var(--ink);list-style:none}
.oto-faq summary::-webkit-details-marker{display:none}
.oto-faq summary:after{content:"+";float:right;color:var(--aqd);font-weight:800}
.oto-faq details[open] summary:after{content:"\2212"}
.oto-faq p{margin-top:10px;font-size:15px;line-height:1.6;color:var(--mut)}
.oto-foot{text-align:center;margin:44px 0 18px;font-size:13px;color:#9DB0AD}
.oto-foot a{color:var(--mut)}
@media(max-width:720px){
 .oto h1{font-size:42px}.oto-kick{font-size:17px}.oto h2{font-size:31px}.oto-sub{font-size:17px}
 .oto-split,.oto-split.rev,.oto-card-in{grid-template-columns:1fr}.oto-card-in{padding:24px 20px}.oto-card-in svg{max-width:170px;margin:0 auto}
 .oto-btn{font-size:17px;padding:16px 12px 13px}.oto-band h3,.oto-panel-h h3{font-size:22px}.oto-price{font-size:32px}
 .oto-hero{padding:20px 12px 12px;border-width:5px}.oto-panel-b{padding:22px 20px}.oto-phone{width:200px}
 .oto-ok li,.oto-x li,.oto-p{font-size:16px}}
@media(prefers-reduced-motion:reduce){.oto-btn,.oto-prog i{animation:none}}
</style>
'''

JS = r'''<script>
/* Red buttons scroll back up to your GHL one-click button (placed right under block 1). */
(function(){document.querySelectorAll('.oto [data-oto]').forEach(function(b){b.addEventListener('click',function(e){
  e.preventDefault();var t=document.getElementById('oto-buy');
  if(t){t.scrollIntoView({behavior:'smooth',block:'center'})}else{window.scrollTo({top:0,behavior:'smooth'})}
});});})();
</script>
'''

IMG = "https://oceanicfunnels.com/assets/launch/"

FUNNEL_SVG = '''<svg viewBox="0 0 200 200" fill="none" aria-hidden="true">
 <circle cx="100" cy="100" r="92" fill="#DDF7F2"/>
 <path d="M42 52h116l-40 52v40l-36 18v-58z" fill="#3DE3C8" stroke="#0E1A1B" stroke-width="5" stroke-linejoin="round"/>
 <path d="M58 72h84" stroke="#0E1A1B" stroke-width="4" stroke-linecap="round" opacity=".35"/>
 <circle cx="62" cy="34" r="9" fill="#0E9C87"/><circle cx="100" cy="28" r="9" fill="#0E9C87"/><circle cx="138" cy="34" r="9" fill="#0E9C87"/>
 <circle cx="152" cy="150" r="22" fill="#fff" stroke="#0E1A1B" stroke-width="5"/>
 <path d="M152 138v24M158 142c-2-3-12-4-12 2s12 3 12 9-10 5-12 2" stroke="#0E9C87" stroke-width="4" stroke-linecap="round"/>
</svg>'''

def btn(price, kind, sub="Add it to your order with one click."):
    return f'''<div class="oto-cta"><button type="button" class="oto-btn" data-oto="yes">Yes! Build my first sales funnel ({price})<small>{sub}</small></button></div>'''

def page(kind):
    up = kind == "upsell"
    p = "$97" if up else "$67"
    B = btn(p, kind)
    if up:
        kick = "Your Launch plan is <b>confirmed</b>. One last thing&hellip;"
        h1 = "Wait! <u>Don't build</u><br>your first funnel <em>alone</em>"
        sub = "Let our team design your first sales funnel for you, so you can skip the blank page and start selling sooner."
        badge = "Done for you"
        q = "How fast do you want to make <em>your first sale?</em>"
        pain_intro = "Because most people&hellip;"
        pain = ["Get stuck trying to build their first funnel", "Overthink every word on their sales page", "Spend weeks, or months, trying to figure it out"]
        pain_end = "And that's exactly why they never make the sale."
        diff_h = "Here's the <em>difference</em>"
        diff = '''<p class="oto-p">The people who win don't waste time figuring everything out. <b>They get set up fast.</b></p>
        <p class="oto-p"><b>So let us build it for you.</b> Instead of guessing, stressing and losing weeks, our team designs your funnel inside your account.</p>'''
        band = "One-time offer, only on this page"
        get = ["<b>A sales page</b> for your offer, designed for you", "<b>A checkout page</b> connected so you can take payments",
               "<b>A thank-you page</b> that tells customers what happens next", "<b>Mobile and desktop ready</b>, so it looks right everywhere",
               "<b>Built inside your account</b>, so you can edit it anytime"]
    else:
        kick = "Hold on. <b>Before you go&hellip;</b>"
        h1 = "Get your first funnel<br><em>built for just $67</em>"
        sub = "We get it, $97 isn't right for everyone. Here's a smaller version, so your first sales funnel still gets built."
        badge = "Smaller price"
        q = "Not feeling <em>ready yet?</em>"
        pain_intro = "That's normal. Most people tell us&hellip;"
        pain = ["They're not sure what to sell yet", "Setting everything up feels like a lot", "They want it done right, without spending much"]
        pain_end = "Here's the truth: you get ready by getting set up."
        diff_h = "So we made it <em>easier</em>"
        diff = '''<p class="oto-p">You don't need to have it all figured out. <b>You just need your first funnel live.</b></p>
        <p class="oto-p">For $67, our team designs your sales page and checkout inside your account, so you have something real to sell from.</p>'''
        band = "Second chance, only on this page"
        get = ["<b>A sales page</b> for your offer, designed for you", "<b>A checkout page</b> connected so you can take payments",
               "<b>Mobile and desktop ready</b>, so it looks right everywhere", "<b>Built inside your account</b>, so you can edit it anytime"]
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    top = f'''<!-- OCEANIC FUNNELS {kind.upper()} ({p}) BLOCK 1 of 2: Custom Code element at the very top.
     Right under it: GHL Button (One-Click Upsell/Downsell -> {p} product) + GHL "No thanks" button (go to {"downsell page" if up else "thank-you page"}).
     Then BLOCK 2 in a Custom Code element below the buttons. -->
{CSS}<section class="oto top"><div class="oto-w">
  <div class="oto-prog"><i></i><span>Almost done&hellip;</span></div>
  <p class="oto-kick">{kick}</p>
  <h1>{h1}</h1>
  <p class="oto-sub">{sub}</p>
  <div class="oto-hero"><span class="oto-badge">Funnels built by our team</span><img src="https://oceanicfunnels.com/assets/showcase/funnels-built.webp" alt="Sales funnels built by the Oceanic Funnels team" width="1200" height="691"></div>
  <div id="oto-buy"></div>
</div></section>
'''
    html = f'''<!-- OCEANIC FUNNELS {kind.upper()} ({p}) BLOCK 2 of 2: Custom Code element BELOW your GHL buttons. Red buttons scroll back up to them. -->
<section class="oto rest"><div class="oto-w">

  <div class="oto-sec oto-split">
    <div>
      <h2>{q}</h2>
      <p class="oto-p">{pain_intro}</p>
      <ul class="oto-x">{li(pain)}</ul>
      <p class="oto-p"><b>{pain_end}</b></p>
    </div>
    <div class="oto-chart" aria-hidden="true">
      <div class="t"><span>YOUR SALES</span><b>Live</b></div>
      <div class="oto-bars"><i style="height:12%"></i><i style="height:22%"></i><i style="height:34%"></i><i style="height:52%"></i><i style="height:70%"></i><i style="height:94%"></i></div>
      <div class="n"><span>Wk 1</span><span>Wk 2</span><span>Wk 3</span><span>Wk 4</span><span>Wk 5</span><span>Wk 6</span></div>
      <div class="oto-toast"><i>$</i><span><b>New order</b> from your sales page</span></div>
    </div>
  </div>

  <div class="oto-sec oto-card">
    <div class="oto-card-in">{FUNNEL_SVG}<div><h2>{diff_h}</h2>{diff}</div></div>
    <div class="oto-band"><h3>{band}</h3>{B}</div>
  </div>

  <div class="oto-sec oto-split rev">
    <div class="oto-phone"><img src="{IMG}checkout.webp" alt="A checkout page on a phone" width="585" height="1170"></div>
    <div>
      <span class="oto-tag">For {p}</span>
      <h2>What you're <em>getting</em></h2>
      <ul class="oto-ok">{li(get)}</ul>
    </div>
  </div>
  {B}

  <div class="oto-sec oto-panel">
    <div class="oto-panel-h"><h3>Here's what makes this powerful&hellip;</h3></div>
    <div class="oto-panel-b">
      <p class="oto-p" style="margin-top:0">You don't get a template and a "good luck." Our team builds your funnel the way we build every funnel:</p>
      <ul class="oto-ok">
        <li><b>Clear structure</b> that walks visitors from your offer to checkout</li>
        <li><b>Your offer positioned clearly</b> on the page</li>
        <li><b>Set up to sell</b>, with your checkout connected and ready</li>
      </ul>
      <p class="oto-p"><b>You're not doing this alone.</b></p>
      {B}
    </div>
  </div>

  <div class="oto-sec oto-panel oto-real"><div class="oto-panel-b">
    <h2>Let's be real</h2><div class="line"></div>
    <p class="oto-p">Without a sales funnel, you can't sell your offer. You're just preparing.</p>
    <p class="oto-p">This upgrade helps you:</p>
    <ul class="oto-ok"><li>Get your offer live</li><li>Start collecting customers</li><li>Move toward your first sale faster</li></ul>
    <p class="oto-price">One-time upgrade &ndash; <em>{p}</em></p>
    <p class="oto-note">One-time payment, no subscription. This offer is only available on this page.</p>
    <h2 style="margin-top:30px;font-size:32px">Ready to get set up?</h2>
    <p class="oto-p">Stop trying to figure everything out on your own. Let us build your funnel so you can focus on getting paid.</p>
    {B}
  </div></div>

  <div class="oto-sec">
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
{JS}'''
    open(f"{kind}-1-top.html", "w").write(top)
    open(f"{kind}-2-rest.html", "w").write(html)

page("upsell"); page("downsell")
