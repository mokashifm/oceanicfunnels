# Builds the upsell ($97) and downsell ($67) custom-code blocks for GHL.
CSS = '''<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@700;800;900&display=swap" rel="stylesheet">
<style>
.oto{font-family:Inter,system-ui,sans-serif;color:#25302F;max-width:760px;margin:0 auto;padding:0 18px;text-align:center}
.oto *{box-sizing:border-box;margin:0;padding:0}
.oto-bar{background:#EEF5F3;border-radius:999px;height:10px;max-width:420px;margin:28px auto 8px;overflow:hidden}
.oto-bar i{display:block;height:100%;width:85%;background:linear-gradient(90deg,#3DE3C8,#0E9C87);border-radius:999px}
.oto-step{font-size:13px;font-weight:600;color:#5B6967;letter-spacing:.04em;text-transform:uppercase}
.oto-wait{display:inline-block;margin-top:22px;background:#FFE6DF;color:#BF3A1F;font-weight:700;font-size:14px;padding:7px 16px;border-radius:999px}
.oto h1{font-family:"Inter Tight",Inter,sans-serif;font-weight:900;font-size:44px;line-height:1.08;letter-spacing:-.03em;color:#0E1A1B;margin-top:14px}
.oto h1 span{color:#0E9C87}
.oto h2{font-family:"Inter Tight",Inter,sans-serif;font-weight:800;font-size:30px;line-height:1.15;letter-spacing:-.02em;color:#0E1A1B}
.oto-sub{font-size:19px;line-height:1.55;color:#5B6967;margin:14px auto 0;max-width:620px}
.oto-img{display:block;width:100%;max-width:620px;height:auto;margin:26px auto 0}
.oto-price{margin-top:20px;font-family:"Inter Tight",Inter,sans-serif}
.oto-price b{font-size:46px;font-weight:900;color:#0E1A1B;letter-spacing:-.03em}
.oto-price s{font-size:24px;color:#D9472A;margin-right:10px;font-weight:700}
.oto-price small{display:block;font-family:Inter,sans-serif;font-size:14px;color:#5B6967;margin-top:2px}
.oto-sec{margin-top:44px;text-align:left}
.oto-sec h2{text-align:center}
.oto-card{background:#fff;border:1px solid #DCE6E3;border-radius:18px;padding:26px 26px;margin-top:20px}
.oto-x,.oto-ok{list-style:none;display:grid;gap:12px}
.oto-x li,.oto-ok li{position:relative;padding-left:34px;font-size:17px;line-height:1.5}
.oto-x li:before,.oto-ok li:before{position:absolute;left:0;top:1px;width:23px;height:23px;border-radius:50%;display:grid;place-items:center;font-size:13px;font-weight:800}
.oto-x li:before{content:"\\2715";background:#FFE6DF;color:#BF3A1F}
.oto-ok li:before{content:"\\2713";background:#DDF7F2;color:#0A7F6E}
.oto-ok li b,.oto-x li b{color:#0E1A1B}
.oto-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:20px}
.oto-steps div{background:#EEF5F3;border-radius:16px;padding:20px 18px;text-align:left}
.oto-steps i{font-style:normal;display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:#0E1A1B;color:#3DE3C8;font-weight:800;font-family:"Inter Tight",sans-serif}
.oto-steps b{display:block;margin-top:12px;font-size:16px;color:#0E1A1B}
.oto-steps span{display:block;margin-top:4px;font-size:14.5px;line-height:1.5;color:#5B6967}
.oto-box{margin-top:26px;background:#0E1A1B;color:#fff;border-radius:20px;padding:28px 24px;text-align:center}
.oto-box .tag{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#3DE3C8}
.oto-box b{display:block;font-family:"Inter Tight",sans-serif;font-size:48px;font-weight:900;letter-spacing:-.03em;margin-top:4px}
.oto-box b s{font-size:24px;color:#9DB0AD;margin-right:10px;font-weight:700}
.oto-box p{font-size:15px;line-height:1.55;color:#C9D6D3;margin-top:6px}
.oto-faq{margin-top:20px;display:grid;gap:10px;text-align:left}
.oto-faq details{background:#fff;border:1px solid #DCE6E3;border-radius:14px;padding:16px 18px}
.oto-faq summary{cursor:pointer;font-weight:700;font-size:16px;color:#0E1A1B;list-style:none}
.oto-faq summary::-webkit-details-marker{display:none}
.oto-faq summary:after{content:"+";float:right;color:#0E9C87;font-weight:800}
.oto-faq details[open] summary:after{content:"\\2212"}
.oto-faq p{margin-top:10px;font-size:15px;line-height:1.6;color:#5B6967}
.oto-foot{margin:40px 0 24px;font-size:13px;color:#9DB0AD}
.oto-foot a{color:#5B6967}
@media(max-width:640px){.oto h1{font-size:32px}.oto h2{font-size:24px}.oto-sub{font-size:17px}.oto-steps{grid-template-columns:1fr}.oto-price b,.oto-box b{font-size:38px}.oto-x li,.oto-ok li{font-size:16px}}
</style>
'''
IMG = "https://oceanicfunnels.com/assets/launch/checkout-bundle.webp"

def page(kind):
    up = kind == "upsell"
    price = "$97" if up else "$67"
    top = f'''<!-- OCEANIC FUNNELS {kind.upper()} ({price}) block 1 of 3: paste in a Custom Code element at the top. Put the native YES button + NO link right below it. -->
{CSS}<section class="oto">
  <div class="oto-bar"><i></i></div>
  <div class="oto-step">Step 2 of 2: one last thing</div>
  <div class="oto-wait">{"Wait! Your order isn't finished yet" if up else "Hold on. Before you go"}</div>
  <h1>{"Want us to design <span>your first sales funnel</span> for you?" if up else "Get your first sales funnel <span>built for $67</span> instead"}</h1>
  <p class="oto-sub">{"Your Launch plan is ready. Skip the blank page and let our team build your first funnel, so you can start selling sooner." if up else "We get it, the timing isn't right for everyone. Here's a smaller version, so your first funnel still gets built."}</p>
  <img class="oto-img" src="{IMG}" alt="Sales pages, store and checkout designed by Oceanic Funnels" width="1000" height="572">
  <div class="oto-price"><b>{price}</b><small>One-time payment. Added to your order with one click.</small></div>
</section>
'''
    if up:
        pain = '''<li><b>You open the builder</b> and don't know where to start</li>
      <li><b>You keep rewriting the headline</b> instead of selling</li>
      <li><b>Weeks go by</b> and your offer still isn't live</li>'''
        get = '''<li><b>A sales page</b> for your offer, designed for you</li>
      <li><b>A checkout page</b> connected so you can take payments</li>
      <li><b>A thank-you page</b> that tells customers what happens next</li>
      <li><b>Mobile and desktop ready</b>, so it looks right on every screen</li>
      <li><b>Built inside your account</b>, so you can edit it anytime</li>'''
    else:
        pain = '''<li><b>You're not sure what to sell yet,</b> so you put it off</li>
      <li><b>Setting things up</b> feels like a lot</li>
      <li><b>You want it done right</b> but don't want to spend much</li>'''
        get = '''<li><b>A sales page</b> for your offer, designed for you</li>
      <li><b>A checkout page</b> connected so you can take payments</li>
      <li><b>Mobile and desktop ready</b>, so it looks right on every screen</li>
      <li><b>Built inside your account</b>, so you can edit it anytime</li>'''
    mid = f'''<!-- OCEANIC FUNNELS {kind.upper()} ({price}) block 2 of 3: paste in a Custom Code element below the first YES button + NO link. Put the native YES button + NO link right below it again. -->
<section class="oto">
  <div class="oto-sec">
    <h2>{"Does this sound familiar?" if up else "Not ready? That's normal."}</h2>
    <div class="oto-card"><ul class="oto-x">
      {pain}
    </ul></div>
  </div>
  <div class="oto-sec">
    <h2>{"Here's what we build for you" if up else "Here's what you get for $67"}</h2>
    <div class="oto-card"><ul class="oto-ok">
      {get}
    </ul></div>
  </div>
  <div class="oto-sec">
    <h2>How it works</h2>
    <div class="oto-steps">
      <div><i>1</i><b>Click yes</b><span>It's added to your order. No need to enter your card again.</span></div>
      <div><i>2</i><b>Tell us about your offer</b><span>We'll email you a short form about what you sell.</span></div>
      <div><i>3</i><b>We build it</b><span>Your funnel is designed in your account, ready for you to review.</span></div>
    </div>
  </div>
  <div class="oto-box">
    <div class="tag">{"One-time offer" if up else "Last chance on this offer"}</div>
    <b>{price}</b>
    <p>{"This offer is only available on this page." if up else "This price is only available on this page."} One-time payment, no subscription.</p>
  </div>
</section>
'''
    faq = f'''<!-- OCEANIC FUNNELS {kind.upper()} ({price}) block 3 of 3: paste in a Custom Code element at the bottom (below the last YES button + NO link). -->
<section class="oto">
  <div class="oto-sec">
    <h2>Questions</h2>
    <div class="oto-faq">
      <details><summary>Do I need to enter my card again?</summary><p>No. Click the yes button and it's added to the order you just placed.</p></details>
      <details><summary>Is this a subscription?</summary><p>No. It's a one-time payment of {price}. Your Launch plan stays $17/month.</p></details>
      <details><summary>Can I edit the funnel after you build it?</summary><p>Yes. It's built inside your own account, so you can change text, images and prices anytime.</p></details>
      <details><summary>What if I don't have an offer yet?</summary><p>That's fine. Tell us what you know or what you'd like to sell, and we'll help you shape it into a first offer.</p></details>
    </div>
  </div>
  <p class="oto-foot">&copy; 2026 Oceanic Funnels &middot; <a href="https://oceanicfunnels.com/privacy/">Privacy</a> &middot; <a href="https://oceanicfunnels.com/terms/">Terms</a> &middot; <a href="mailto:hello@oceanicfunnels.com">hello@oceanicfunnels.com</a></p>
</section>
'''
    for n, s in (("1-top", top), ("2-offer", mid), ("3-faq", faq)):
        open(f"{kind}-{n}.html", "w").write(s)

page("upsell"); page("downsell")
