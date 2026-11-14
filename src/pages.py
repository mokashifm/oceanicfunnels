"""Builds the extra pages: /privacy/, /terms/, /compare/ and /compare/<competitor>/.
Shares the homepage design: its stylesheet is extracted to /assets/site.css.
"""
import tools
import html, json, os, re
import legal
from competitors import COMPETITORS, OF, ROW_LABELS, CHECKED, FEATS, MATRIX
from industries import INDUSTRIES, GENERIC_FAQ, CATEGORIES
from ind_deep import DEEP
from guides_a import G_A
from guides_b import G_B
from guides_c import G_C
from guides_d import G_D
from guides_e import G_E
from guides_expand import apply as _expand
GUIDES = _expand(G_A + G_B + G_C + G_D + G_E)
GUIDE_CATS = ["Lead response", "AI agents", "Messaging", "Lead capture", "Booking", "CRM", "Automation", "Follow-up", "Reviews", "Sales funnels", "Websites and SEO", "Ecommerce and payments", "Courses and communities", "Marketing", "Reporting", "Compliance"]
assert all(g["cat"] in GUIDE_CATS for g in GUIDES), [g["cat"] for g in GUIDES if g["cat"] not in GUIDE_CATS]
assert len({g['slug'] for g in GUIDES}) == len(GUIDES)
GUIDE_DATE = "2026-10-26"

E = html.escape
CLARITY = """<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "z3wchhfmwo");
</script>"""

# Meta Pixels. The med spa funnel keeps its own dataset; every other page (site + funnels) uses the global pixel.
META_PIXELS = {
    "/lp/med-spas/": "1759319485158087",          # Med spa funnel dataset
}
GLOBAL_PIXEL = "2113854352568666"                # Oceanic Funnels website (global)
def pixel_for(path):
    for pre, pid in META_PIXELS.items():
        if path.startswith(pre):
            return PIXEL_TPL.replace("PIXELID", pid)
    return PIXEL_TPL.replace("PIXELID", GLOBAL_PIXEL)
PIXEL_TPL = """
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','PIXELID');
window.ofT=function(n,d){var id=n+'.'+Date.now().toString(36)+'.'+Math.random().toString(36).slice(2,10);d=d||{};fbq('track',n,d,{eventID:id});
try{var body=JSON.stringify({p:'PIXELID',e:n,id:id,d:d,u:location.href});if(navigator.sendBeacon){navigator.sendBeacon('/api/e',new Blob([body],{type:'application/json'}))}else{fetch('/api/e',{method:'POST',body:body,keepalive:true,headers:{'Content-Type':'application/json'}})}}catch(x){}};
ofT('PageView');
if(location.pathname.indexOf('/lp/')===0||location.pathname.indexOf('/industries/')===0){ofT('ViewContent',{content_name:location.pathname})}
var pr=document.getElementById('pricing');if(pr&&'IntersectionObserver' in window){var io=new IntersectionObserver(function(en){if(en[0].isIntersecting){ofT('ViewContent',{content_name:'pricing'});io.disconnect()}},{threshold:.3});io.observe(pr)}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href')||'';
if(h.indexOf('checkout.oceanicfunnels.com')>-1){ofT('InitiateCheckout',{content_name:h.split('/').pop()})}});
</script>
<noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id=PIXELID&ev=PageView&noscript=1"></noscript>"""
CK = "https://checkout.oceanicfunnels.com/oceanic_funnels-page"
CAL_MED = "/lp/med-spas/book/"
CAL_EMBED = "https://links.oceanicfunnels.com/widget/booking/0Fq9d6ETDejl4rKothS4"
CK_IND = {"med-spas": "https://checkout.oceanicfunnels.com/oceanic_funnels_med-spas"}
SOCIAL = [("Facebook", "https://www.facebook.com/oceanicfunnels"), ("LinkedIn", "https://www.linkedin.com/company/oceanicfunnels"), ("Instagram", "https://www.instagram.com/oceanicfunnels/")]
def art(w): return ("an " if w[:1].lower() in "aeiou" else "a ") + w

PAGE_CSS = r"""
/* ---------- inner pages */
.nf-sub-hero{background:linear-gradient(180deg,#DEF4F0 0%,#EEF3F2 70%,#FBEEE9 100%)}
.nf-sub-in{padding-block:48px 72px;max-width:900px}
.nf-sub-in.c{margin:0 auto;text-align:center}
.nf-sub-in.c .nf-sub{margin-left:auto;margin-right:auto}
.nf-sub-in h1{font-size:clamp(38px,5.6vw,72px);line-height:1.02}
.nf-crumbs{display:flex;flex-wrap:wrap;gap:8px;font-size:14px;color:var(--muted);margin-bottom:22px}
.nf-sub-in.c .nf-crumbs{justify-content:center}
.nf-crumbs a{color:var(--ink);text-decoration:none}
.nf-crumbs a:hover{text-decoration:underline}
.nf-sub-in .nf-hero-cta{justify-content:flex-start;margin-top:32px}
.nf-sub-in.c .nf-hero-cta{justify-content:center}
.nf-vs{display:inline-flex;align-items:center;gap:10px;font-family:var(--display);font-weight:700;font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);background:#fff;border-radius:999px;padding:8px 16px;box-shadow:inset 0 0 0 1px rgba(14,26,27,.12);margin-bottom:22px}
.nf-vs i{font-style:normal;color:var(--coral-d)}
.nf-cmp .nf-table td.us{width:38%}
.nf-cmp .nf-table td{width:36%}
.nf-two{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:48px}
.nf-box{background:var(--mist);border-radius:var(--r);padding:36px}
.nf-box.ink{background:var(--ink);color:#fff}
.nf-box.ink h3{color:#fff}
.nf-box h3{font-size:24px;margin-bottom:16px}
.nf-box p{color:var(--text);font-size:16px}
.nf-box.ink p{color:#C9D6D4}
.nf-plist{display:grid;gap:0;margin-top:6px}
.nf-plist li{display:flex;justify-content:space-between;gap:16px;padding:13px 0;border-bottom:1px solid var(--line);font-size:15px}
.nf-box.ink .nf-plist li{border-color:#2A3A3A}
.nf-plist li:last-child{border-bottom:0}
.nf-plist b{font-family:var(--display);font-weight:600;color:var(--ink)}
.nf-box.ink .nf-plist b{color:#fff}
.nf-plist span{text-align:right;color:var(--muted)}
.nf-box.ink .nf-plist span{color:var(--aqua)}
.nf-srcs{margin-top:22px;font-size:13px;color:var(--muted)}
.nf-srcs a{color:var(--ink)}
.nf-feat{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:48px}
.nf-feat li{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:24px}
.nf-feat b{display:block;font-family:var(--display);font-size:18px;font-weight:600;color:var(--ink);margin-bottom:6px}
.nf-feat span{font-size:14.5px;color:var(--muted)}
.nf-cta-band{background:var(--ink);border-radius:var(--r);padding:56px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:28px}
.nf-cta-band h2{color:#fff;text-transform:uppercase;font-weight:700;letter-spacing:-.03em;line-height:.98;font-size:clamp(30px,3.6vw,46px);max-width:18ch}
.nf-cta-band p{color:#C9D6D4;margin-top:12px;max-width:48ch}
.nf-more{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}
.nf-more a{font-family:var(--display);font-weight:600;font-size:15px;padding:10px 18px;border-radius:999px;color:var(--ink);text-decoration:none;box-shadow:inset 0 0 0 1.5px var(--ink)}
.nf-more a:hover{background:var(--ink);color:#fff}
.nf-hub{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:8px}
.nf-hub a{display:flex;flex-direction:column;gap:10px;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px;text-decoration:none;color:var(--text);transition:border-color .15s}
.nf-hub a:hover{border-color:var(--ink)}
.nf-hub .vs{font-family:var(--display);font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--coral-d)}
.nf-hub h2,.nf-hub h3{font-size:22px;line-height:1.18}
.nf-hubgrp{margin-bottom:56px;scroll-margin-top:24px}
.nf-hubgrp>h2{font-size:clamp(26px,3vw,34px);letter-spacing:-.02em;margin-bottom:20px}
.nf-more-h{font-size:18px;margin-top:36px;letter-spacing:-.01em}
.nf-hub p{font-size:14.5px;color:var(--muted)}
.nf-hub .go{margin-top:auto;padding-top:8px;font-family:var(--display);font-weight:600;color:var(--ink)}
.nf-doc-wrap{display:grid;grid-template-columns:240px minmax(0,1fr);gap:64px;align-items:start}
.nf-toc{position:sticky;top:24px;font-size:14px}
.nf-toc b{display:block;font-family:var(--display);font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);margin-bottom:12px}
.nf-toc ol{display:grid;gap:8px;list-style:decimal;padding-left:18px;color:var(--muted)}
.nf-toc a{color:var(--muted);text-decoration:none}
.nf-toc a:hover{color:var(--ink)}
.nf-doc{max-width:760px}
.nf-doc section{padding-block:8px 20px;border-bottom:1px solid var(--line);margin-bottom:20px;scroll-margin-top:24px}
.nf-doc section:last-child{border-bottom:0}
.nf-doc h2{font-size:24px;letter-spacing:-.02em;margin-bottom:12px}
.nf-doc p{font-size:16px;line-height:1.7;color:var(--text);margin-bottom:12px}
.nf-doc ul{list-style:disc;padding-left:22px;display:grid;gap:8px;margin-bottom:12px}
.nf-doc li{font-size:16px;line-height:1.65;color:var(--text)}
.nf-doc b{color:var(--ink)}
.nf-doc a:not(.nf-btn){color:var(--ink)}
.nf-note{background:var(--coral-l);color:#7A2A17;border-radius:var(--r);padding:14px 18px;font-size:14.5px;margin-bottom:28px}
@media (max-width:1060px){.nf-two{grid-template-columns:1fr}.nf-feat,.nf-hub{grid-template-columns:1fr 1fr}.nf-doc-wrap{grid-template-columns:1fr;gap:28px}.nf-toc{position:static}}
@media (max-width:680px){
.nf-cmp .nf-table{min-width:0}
.nf-cmp .nf-table thead{display:none}
.nf-cmp .nf-table,.nf-cmp .nf-table tbody,.nf-cmp .nf-table tr,.nf-cmp .nf-table th,.nf-cmp .nf-table td{display:block;width:auto}
.nf-cmp .nf-table tr{border-bottom:1px solid var(--line)}
.nf-cmp .nf-table tbody th{background:var(--mist);border:0;padding:12px 16px;width:auto}
.nf-cmp .nf-table td,.nf-cmp .nf-table td.us{border:0;padding:10px 16px;width:auto}
.nf-cmp .nf-table td::before{content:attr(data-l);display:block;font-family:var(--display);font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin-bottom:2px;opacity:.75}
.nf-cmp .nf-table td.us::before{color:var(--aqua)}
.nf-feat,.nf-hub{grid-template-columns:1fr}.nf-box,.nf-cta-band{padding:28px 22px}.nf-sub-in{padding-block:32px 56px}.nf-plist li{flex-direction:column;gap:2px}.nf-plist span{text-align:left}}
"""

PAGE_CSS += r"""
/* ---------- industry pages */
.nf-leaks{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:48px}
.nf-leaks li{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px;display:flex;flex-direction:column;gap:10px}
.nf-leaks .n{font-family:var(--display);font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--coral-d)}
.nf-leaks b{font-family:var(--display);font-size:20px;font-weight:600;color:var(--ink);line-height:1.2}
.nf-leaks span{font-size:15px;color:var(--muted)}
.nf-run{list-style:none;margin-top:48px;display:grid;gap:0;max-width:900px}
.nf-run li{display:grid;grid-template-columns:150px 44px minmax(0,1fr);grid-template-rows:auto auto;gap:0 20px;align-items:start;padding-bottom:32px;position:relative}
.nf-run li:not(:last-child)::before{content:"";position:absolute;left:191px;top:44px;bottom:0;width:2px;background:#2A3A3A}
.nf-run li:last-child{padding-bottom:0}
.nf-run .t{grid-column:1;grid-row:1;font-family:var(--display);font-weight:600;font-size:14px;color:var(--aqua);text-align:right;padding-top:12px}
.nf-run .d{grid-column:2;grid-row:1/3;width:44px;height:44px;border-radius:50%;background:var(--aqua);color:var(--ink);font-family:var(--display);font-weight:700;display:grid;place-items:center}
.nf-run b{grid-column:3;grid-row:1;display:block;font-family:var(--display);font-size:20px;font-weight:600;color:#fff;padding-top:9px}
.nf-run p{grid-column:3;grid-row:2;color:#C9D6D4;font-size:15.5px;margin-top:4px;max-width:60ch}
.nf-chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.nf-chips li{font-family:var(--display);font-weight:600;font-size:15px;padding:10px 18px;border-radius:999px;background:#fff;color:var(--ink);box-shadow:inset 0 0 0 1px var(--line)}
@media (max-width:1060px){.nf-leaks{grid-template-columns:1fr}}
@media (max-width:680px){
.nf-run li{grid-template-columns:44px minmax(0,1fr);grid-template-rows:auto auto auto;gap:0 16px}
.nf-run li:not(:last-child)::before{left:21px}
.nf-run .d{grid-column:1;grid-row:1/4}
.nf-run .t{grid-column:2;grid-row:1;text-align:left;padding-top:2px;font-size:13px}
.nf-run b{grid-column:2;grid-row:2;padding-top:2px;font-size:18px}
.nf-run p{grid-column:2;grid-row:3}
}
"""

PAGE_CSS += r"""
/* ---------- guides */
.nf-meta{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:22px;font-size:14px;color:var(--muted)}
.nf-meta b{color:var(--ink);font-weight:600}
.nf-answer{background:var(--ink);color:#E6EEEC;border-radius:var(--r);padding:26px 28px;margin-bottom:36px;position:relative;overflow:hidden}
.nf-answer b.k{display:block;font-family:var(--display);font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--aqua);margin-bottom:8px}
.nf-answer p{color:#E6EEEC!important;font-size:17px!important;line-height:1.65!important;margin:0!important}
.nf-doc ol{list-style:decimal;padding-left:22px;display:grid;gap:10px;margin-bottom:14px}
.nf-doc ol li{font-size:16px;line-height:1.65;color:var(--text)}
.nf-doc ol.nf-steps-list{list-style:none;padding:0;counter-reset:st;gap:12px}
.nf-doc ol.nf-steps-list li{counter-increment:st;position:relative;padding:14px 16px 14px 58px;background:var(--mist);border-radius:14px}
.nf-doc ol.nf-steps-list li::before{content:counter(st);position:absolute;left:14px;top:12px;width:30px;height:30px;border-radius:50%;background:var(--aqua);color:var(--ink);font-family:var(--display);font-weight:700;font-size:14px;display:grid;place-items:center}
.nf-doc i{color:var(--ink)}
.nf-doc code{font-size:14px;background:var(--mist);padding:2px 6px;border-radius:6px}
.nf-doc h2{scroll-margin-top:24px}
.nf-doc .nf-srcs{margin-top:8px}
.nf-doc ul.nf-check{list-style:none;padding-left:0}.nf-doc ul.nf-check li{position:relative;padding-left:30px}.nf-doc ul.nf-check li::before{content:"\2713";position:absolute;left:0;top:0;width:20px;height:20px;border-radius:50%;background:var(--aqua);color:var(--ink);font-size:12px;font-weight:800;display:grid;place-items:center;margin-top:3px}
.nf-gcta{background:var(--aqua-l);border-radius:var(--r);padding:26px 28px;margin:8px 0 28px;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between}
.nf-gcta b{font-family:var(--display);font-size:20px;color:var(--ink);display:block}
.nf-gcta span{font-size:15px;color:var(--text)}
.nf-gcard .vs{color:var(--aqua-d)!important}
.nf-gcard .rt{font-size:13px;color:var(--muted)}
"""

PAGE_CSS += r"""
/* ---------- deep industry pages */
.nf-money{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:48px}
.nf-money li{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px;display:flex;flex-direction:column;gap:10px}
.nf-money .n{font-family:var(--display);font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--coral-d)}
.nf-money b{font-family:var(--display);font-size:21px;font-weight:600;color:var(--ink);line-height:1.2}
.nf-money p{font-size:15.5px;color:var(--muted);line-height:1.6}
.nf-money p.fix{margin-top:auto;padding:14px 16px;background:var(--aqua-l);border-radius:12px;color:var(--ink);font-size:15px}
.nf-money p.fix span{display:block;font-family:var(--display);font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#086455;margin-bottom:4px}
.nf-treat .nf-table tbody th{width:28%}
.nf-treat .nf-table td{width:30%}
.nf-dfy{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:40px;margin-top:44px;align-items:start}
.nf-dfy-list{display:grid;gap:12px;counter-reset:dfy}
.nf-dfy-list li{counter-increment:dfy;display:flex;gap:14px;align-items:flex-start;color:#E6EEEC;font-size:16.5px;line-height:1.5}
.nf-dfy-list li::before{content:counter(dfy);flex:none;width:28px;height:28px;border-radius:50%;background:var(--aqua);color:var(--ink);font-family:var(--display);font-weight:700;font-size:13px;display:grid;place-items:center;margin-top:-1px}
.nf-dfy-card{background:#fff;color:var(--ink);border-radius:var(--r);padding:34px 30px;position:sticky;top:24px;text-align:center}
.nf-dfy-card .plan{display:inline-block;font-family:var(--display);font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:7px 16px;border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--ink)}
.nf-dfy-card .amt{font-family:var(--display);font-size:60px;font-weight:600;letter-spacing:-.05em;line-height:1;margin-top:20px;display:flex;justify-content:center;align-items:baseline;gap:6px}
.nf-dfy-card .amt small{font-family:var(--body);font-size:15px;font-weight:500;letter-spacing:0;color:var(--muted)}
.nf-dfy-card .fee{font-size:15px;font-weight:600;color:var(--coral-d);margin-top:10px}
.nf-dfy-card ul{display:grid;gap:0;margin:22px 0;text-align:left}
.nf-dfy-card ul li{padding:11px 0;border-bottom:1px solid var(--line);font-size:15px;color:var(--text);display:flex;gap:10px}
.nf-dfy-card ul li::before{content:"\2713";color:var(--aqua-d);font-weight:700}
.nf-dfy-card .nf-btn{width:100%;justify-content:center}
.nf-dfy-card .small{font-size:14px;color:var(--muted);margin-top:14px}
.nf-dfy-card .small a{color:var(--ink)}
#leak-calculator .nf-field label{align-items:flex-start;gap:12px}
#leak-calculator .nf-field output{flex:none;line-height:1.6;white-space:nowrap}
@media (max-width:1060px){.nf-money,.nf-dfy{grid-template-columns:1fr}.nf-dfy-card{position:static}}
@media (max-width:680px){
.nf-treat .nf-table{min-width:0}
.nf-treat .nf-table thead{display:none}
.nf-treat .nf-table,.nf-treat .nf-table tbody,.nf-treat .nf-table tr,.nf-treat .nf-table th,.nf-treat .nf-table td{display:block;width:auto}
.nf-treat .nf-table tr{border-bottom:1px solid var(--line)}
.nf-treat .nf-table tbody th{background:var(--mist);border:0;padding:12px 16px;width:auto}
.nf-treat .nf-table td,.nf-treat .nf-table td.us{border:0;padding:10px 16px;width:auto}
.nf-treat .nf-table td::before{content:attr(data-l);display:block;font-family:var(--display);font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin-bottom:2px;opacity:.75}
.nf-treat .nf-table td.us::before{color:var(--aqua)}
.nf-money li,.nf-dfy-card{padding:24px 20px}
}
"""

def extract(src):
    css = src[src.index('<style>') + 7: src.index('</style>')]
    logo = re.search(r'<a class="nf-logo".*?</a>', src, re.S).group(0).replace('href="#top"', 'href="/"')
    return css, logo

def footer(cfg):
    comp = "".join(f'<a href="/compare/{c["slug"]}/">vs {E(c["name"])}</a>' for c in COMPETITORS[:6])
    inds = "".join(f'<a href="/industries/{i["slug"]}/">{E(i["short"])}</a>' for i in INDUSTRIES[:6])
    return f'''<footer class="nf-foot">
  <div class="nf-wrap nf-foot-top">
    <div>
      <h2>Stop fishing. Build the net.</h2>
      <p>Oceanic Funnels OS: the all-in-one sales funnel, CRM and automation system. Full system from $97 a month.</p>
      <a class="nf-btn nf-btn--aqua" href="/#pricing">Build my net</a>
    </div>
    <nav class="nf-foot-cols" aria-label="Footer">
      <div><span class="fh">Product</span><a href="/#features">Features</a><a href="/#all-in-one">All-in-one</a><a href="/#pricing">Pricing</a><a href="/guides/">Guides</a><a href="/tools/speed-to-lead-test/">Speed to Lead Test</a><a href="/#faq">FAQ</a></div>
      <div><span class="fh">Industries</span>{inds}<a href="/industries/">All industries</a></div>
      <div><span class="fh">Compare</span>{comp}<a href="/compare/">All comparisons</a></div>
      <div><span class="fh">Company</span><span>{E(cfg["email"])}</span><a href="/about/">About</a><a href="{cfg["login"]}">Log in</a><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a>{"".join(f'<a href="{u}" rel="me noopener" target="_blank">{n}</a>' for n, u in SOCIAL)}</div>
    </nav>
  </div>
  <div class="nf-wrap nf-foot-bot"><span>© 2026 {E(cfg["brand"])}. All rights reserved.</span><span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a></span></div>
  <div class="nf-wordmark" aria-hidden="true">OCEANIC</div>
</footer>'''

def header(logo, cfg):
    return f'''<header class="nf-head">
      {logo}
      <nav aria-label="Main">
        <a class="l" href="/#features">Features</a>
        <a class="l" href="/industries/">Industries</a>
        <a class="l" href="/guides/">Guides</a>
        <a class="l" href="/#pricing">Pricing</a>
        <a class="l" href="/compare/">Compare</a>
        <a class="nf-btn nf-btn--line" href="{cfg["login"]}">Log in</a>
        <a class="nf-btn nf-btn--ink" href="{CK}">Build my net</a>
      </nav>
    </header>'''

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def page(cfg, fonts, path, title, desc, crumbs, body, logo, extra=()):
    url = cfg["domain"] + path
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": cfg["domain"] + p} for i, (n, p) in enumerate(crumbs)]
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#page", "url": url, "name": title, "description": desc,
         "isPartOf": {"@id": cfg["domain"] + "/#page"}, "publisher": {"@id": cfg["domain"] + "/#org"},
         "dateModified": cfg["updated"], "inLanguage": "en"},
        {"@type": "BreadcrumbList", "itemListElement": items}, *extra]}
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0E1A1B">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{E(cfg["brand"])}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{cfg["domain"]}/{"og-launch.png" if path.startswith("/lp/launch") else "og-image.png"}?v=3">
<meta name="twitter:card" content="summary_large_image">
{fonts}
<link rel="stylesheet" href="/assets/site.css?v={CSS_VER}">
<script type="application/ld+json">
{json.dumps(schema, indent=1)}
</script>
{CLARITY}
</head>
<body style="margin:0;background:#FFFFFF">
<div class="nf">
{body.replace("{{HEADER}}", header(logo, cfg))}
{footer(cfg)}
</div>
</body>
</html>
'''

def crumbs_html(crumbs):
    out = []
    for i, (n, p) in enumerate(crumbs):
        out.append(f'<span>{E(n)}</span>' if i == len(crumbs) - 1 else f'<a href="{p}">{E(n)}</a><span aria-hidden="true">/</span>')
    return '<nav class="nf-crumbs" aria-label="Breadcrumb">' + "".join(out) + '</nav>'

def legal_page(cfg, fonts, logo, slug, title, h1, intro, sections):
    path = f"/{slug}/"
    crumbs = [("Home", "/"), (h1, path)]
    ids = [re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") for t, _ in sections]
    toc = "".join(f'<li><a href="#{i}">{E(t)}</a></li>' for i, (t, _) in zip(ids, sections))
    secs = "".join(f'<section id="{i}"><h2>{E(t)}</h2>{c}</section>' for i, (t, c) in zip(ids, sections))
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in">
      {crumbs_html(crumbs)}
      <h1>{E(h1)}</h1>
      <p class="nf-sub">{E(intro)} Effective {legal.EFFECTIVE}.</p>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:64px">
  <div class="nf-wrap nf-doc-wrap">
    <aside class="nf-toc"><b>On this page</b><ol>{toc}</ol></aside>
    <article class="nf-doc">{secs}</article>
  </div>
</section>'''
    return path, page(cfg, fonts, path, title, intro, crumbs, body, logo)

ABOUT = [
 ("Who we are", """<p>Oceanic Funnels is the company behind Oceanic Funnels OS, an all-in-one sales funnel, CRM and marketing automation system for small and growing businesses. We sell it, set it up, build on it and support it.</p>
<p>Start with funnels, websites and a store on Launch, run the full system yourself on Growth, add every AI feature on AI Pro, or work with a dedicated account manager and builder on Scale.</p>"""),
 ("Where we are", """<p>Oceanic Funnels is based in Bahawalpur, Pakistan, and works with businesses worldwide. All plans are priced in US dollars.</p>"""),
 ("Who you deal with", """<p>You deal with Oceanic Funnels directly. You sign up and pay with us, our team onboards you and answers your support requests, and on Scale your dedicated account manager and builder work with you directly. There is no third party between you and the people who look after your account.</p>"""),
 ("Support", """<ul><li><b>24/7 support.</b> Our team replies within the same hour, day or night.</li><li><b>Instant answers.</b> Our AI support assistant replies straight away while a person picks up your request.</li><li><b>Email:</b> <a href="mailto:hello@oceanicfunnels.com">hello@oceanicfunnels.com</a></li></ul>"""),
 ("Your data and your freedom to leave", """<ul><li><b>You own your contacts.</b> Export your contacts and data at any time.</li><li><b>Your domain stays in your name.</b> If you connect your own domain, it is registered to you, not to us.</li><li><b>No lock-in.</b> Every plan is month to month. Cancel anytime.</li></ul>"""),
 ("Plans", """<ul><li><b>Launch:</b> $17 a month. Unlimited sales funnels, websites and an e-commerce store, with payments and contacts. No email or SMS sending.</li><li><b>Growth:</b> $97 a month. Every feature except AI.</li><li><b>AI Pro:</b> $197 a month. Every feature, including all AI.</li><li><b>Scale:</b> $297 a month. Everything in AI Pro, plus a dedicated account manager and a builder to help you grow and scale.</li></ul><p>Every plan is month to month. Growth and AI Pro include a 30-day money-back guarantee. See <a href="/#pricing">pricing</a> to compare every feature.</p>"""),
]

def about_page(cfg, fonts, logo):
    path = "/about/"
    crumbs = [("Home", "/"), ("About", path)]
    intro = "The company behind Oceanic Funnels OS: where we are, who you deal with, how support works and how you keep control of your data."
    ids = [re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") for t, _ in ABOUT]
    toc = "".join(f'<li><a href="#{i}">{E(t)}</a></li>' for i, (t, _) in zip(ids, ABOUT))
    secs = "".join(f'<section id="{i}"><h2>{E(t)}</h2>{c}</section>' for i, (t, c) in zip(ids, ABOUT))
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in">
      {crumbs_html(crumbs)}
      <h1>About Oceanic Funnels</h1>
      <p class="nf-sub">{E(intro)}</p>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:64px">
  <div class="nf-wrap nf-doc-wrap">
    <aside class="nf-toc"><b>On this page</b><ol>{toc}</ol></aside>
    <article class="nf-doc">{secs}</article>
  </div>
</section>'''
    htm = page(cfg, fonts, path, "About Oceanic Funnels | Company, Support and Your Data", intro, crumbs, body, logo)
    org = {"@context": "https://schema.org", "@type": "AboutPage", "url": cfg["domain"] + path, "name": "About Oceanic Funnels",
           "mainEntity": {"@id": cfg["domain"] + "/#org"}}
    htm = htm.replace("</head>", f'<script type="application/ld+json">{json.dumps(org)}</script>\n</head>', 1)
    return path, htm

def compare_page(cfg, fonts, logo, c):
    n = c["name"]; path = f'/compare/{c["slug"]}/'
    crumbs = [("Home", "/"), ("Compare", "/compare/"), (f"vs {n}", path)]
    rows = "".join(f'<tr><th scope="row">{E(ROW_LABELS[k])}</th><td class="us" data-l="Oceanic Funnels OS">✓ {E(OF[k])}</td><td data-l="{E(n)}">{E(v)}</td></tr>' for k, v in c["rows"].items())
    rows += f'<tr><th scope="row">{E(ROW_LABELS["allinone"])}</th><td class="us" data-l="Oceanic Funnels OS">✓ {E(OF["allinone"])}</td><td data-l="{E(n)}">{E(n)} is {E(art(c["kind"]))}</td></tr>'
    plans = "".join(f'<li><b>{E(a)}</b><span>{E(b)}</span></li>' for a, b in c["plans"])
    srcs = " · ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{E(t)}</a>' for t, u in c["sources"])
    more = "".join(f'<a href="/compare/{o["slug"]}/">vs {E(o["name"])}</a>' for o in COMPETITORS if o["slug"] != c["slug"])
    mx = MATRIX.get(c["slug"], {})
    ICON = {"yes": ("✓", "y", "Included"), "part": ("◐", "p", "Limited"), "add": ("＋", "a", "Extra app or add-on"), "no": ("✕", "n", "Not included")}
    mrows = ""; theirs = 0; missing = []
    for k, label, plan in FEATS:
        if k not in mx: continue
        st, note = mx[k]
        ic, cls, word = ICON[st]
        if st == "yes": theirs += 1
        else: missing.append((label, st, note))
        mrows += (f'<tr><th scope="row">{E(label)}</th><td class="us" data-l="Oceanic Funnels OS"><span class="mx y">✓</span> Included'
                  f'<small>{E(plan)} plan</small></td><td data-l="{E(n)}"><span class="mx {cls}">{ic}</span> {E(word)}'
                  f'{f"<small>{E(note)}</small>" if note else ""}</td></tr>')
    total = sum(1 for k, _, _ in FEATS if k in mx)
    stack = "".join(f'<li><b>{E(l)}</b><span>{E(nt) if nt else ("Not included in " + E(n))}</span></li>' for l, st, nt in missing)
    matrix = f'''<section class="nf-band nf-cmp" id="features" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Feature by feature</span>
      <h2>One system <span class="g">vs one tool</span></h2>
      <p class="nf-sub" style="margin-top:12px">Of the {total} features below, {E(n)} fully includes {theirs}. Oceanic Funnels OS includes all {total}, in one login, with one bill.</p>
    </div>
    <div class="nf-score"><div class="us"><b>{total}/{total}</b><span>Oceanic Funnels OS</span></div><div><b>{theirs}/{total}</b><span>{E(n)}</span></div></div>
    <div class="nf-tablewrap">
      <table class="nf-table nf-mx">
        <thead><tr><th scope="col"><span hidden>Feature</span></th><th scope="col" class="us">Oceanic Funnels OS</th><th scope="col">{E(n)}</th></tr></thead>
        <tbody>{mrows}</tbody>
      </table>
    </div>
    <p class="nf-srcs">✓ included · ◐ limited · ＋ needs an extra app, add-on or separate product · ✕ not included. {E(n)} features from {E(n)}'s own pricing and feature pages, checked November 2026. Features we could not confirm are left out.</p>
    {"" if not missing else f'''<div class="nf-xstack"><h3>To match Oceanic Funnels with {E(n)}, you would still need:</h3><ul>{stack}</ul>
    <p>Every extra tool is another login, another bill and another place your leads can slip through. With Oceanic Funnels OS it is all in one system from $97 a month.</p>
    <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">Get the full system <span class="ar" aria-hidden="true">→</span></a></div>'''}
  </div>
</section>'''
    cheap = f'The full Oceanic Funnels system with CRM, email, SMS and automations is $97 a month, and AI Pro, with every AI feature, is $197 a month. A separate Launch plan at $17 a month covers only funnels, websites and a store. {n}\'s published pricing: {c["rows"]["price"][0].lower() + c["rows"]["price"][1:]}.'
    faqs = [
      (f"What is the difference between Oceanic Funnels and {n}?", c["answer"]),
      (f"Is Oceanic Funnels OS cheaper than {n}?", cheap + " Usage like SMS and AI is pay-as-you-go."),
      (f"How do I switch from {n}?", c["switch"]),
      (f"When is {n} the better choice?", c["better"]),
      ("Will you help me build it?", "Yes. On the Scale plan ($297 a month), a dedicated account manager and a builder work with you to set up, grow and scale your system. If you only need one extra funnel built, our team can build it for $297 one time."),
    ]
    faq = "\n".join(f'<details class="nf-q"{" open" if i == 0 else ""}><summary><h3>{E(q)}</h3><span aria-hidden="true">+</span></summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(faqs))
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in">
      {crumbs_html(crumbs)}
      <span class="nf-vs">Oceanic Funnels <i>vs</i> {E(n)}</span>
      <h1>{E(c["h1"])}</h1>
      <p class="nf-sub">{E(n)} is {E(art(c["kind"]))}. Oceanic Funnels OS is the whole system: funnels, website, store, CRM, email, SMS, booking, courses, communities, payments, reviews and AI agents, with unlimited contacts and users. The full system starts at $97 a month.</p>
      <div class="nf-hero-cta">
        <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">Build my net <span class="ar" aria-hidden="true">→</span></a>
        <a class="nf-btn nf-btn--line" href="#comparison">See the comparison</a>
      </div>
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:72px">
  <div class="nf-wrap">
    <div class="nf-panel">
      <div>
        <span class="nf-eyebrow">The short answer</span>
        <h2>Oceanic Funnels vs {E(n)}: <span class="g">what's the difference?</span></h2>
        <p class="nf-def">{E(c["answer"])}</p>
        <p class="nf-updated">Prices checked {CHECKED} on {E(n)}'s own website</p>
      </div>
      <ul class="nf-facts">
        <li><span class="k">Oceanic Funnels</span><span>All-in-one sales funnel, CRM and automation system</span></li>
        <li><span class="k">{E(n)}</span><span>{E(c["kind"][0].upper() + c["kind"][1:])}</span></li>
        <li><span class="k">Starts at</span><span>$97/month (full system) vs {E(c["plans"][0][1] if "$0" not in c["plans"][0][1] else c["plans"][1][1])}</span></li>
        <li><span class="k">Contacts</span><span>Unlimited on Growth, AI Pro and Scale</span></li>
        <li><span class="k">Features</span><span>Oceanic Funnels includes {total} of {total} in our feature table. {E(n)} fully includes {theirs}. <a href="#features">See all</a></span></li>
      </ul>
    </div>
  </div>
</section>

<section class="nf-band nf-cmp" id="comparison" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Side by side</span>
      <h2>Oceanic Funnels vs {E(n)}</h2>
    </div>
    <div class="nf-tablewrap">
      <table class="nf-table">
        <thead><tr><th scope="col"><span hidden>Feature</span></th><th scope="col" class="us">Oceanic Funnels OS</th><th scope="col">{E(n)}</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p class="nf-srcs">{E(n)} details from {E(n)}'s own pricing pages, checked {CHECKED}. Plans and prices change, so confirm on {E(n)}'s website. Sources: {srcs}</p>
  </div>
</section>

{matrix}

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Pricing at a glance</span>
      <h2>What you pay <span class="g">each month</span></h2>
    </div>
    <div class="nf-two">
      <div class="nf-box ink">
        <h3>Oceanic Funnels OS</h3>
        <ul class="nf-plist"><li><b>Launch (funnels, websites, store)</b><span>$17/month</span></li><li><b>Growth (every feature except AI)</b><span>$97/month</span></li><li><b>AI Pro (every feature and all AI)</b><span>$197/month</span></li><li><b>Scale (plus account manager and builder)</b><span>$297/month</span></li></ul>
        <p style="margin-top:16px">Unlimited funnels on every plan, and unlimited contacts and users from Growth up. SMS, email and AI usage is pay-as-you-go.</p>
      </div>
      <div class="nf-box">
        <h3>{E(n)}</h3>
        <ul class="nf-plist">{plans}</ul>
      </div>
    </div>
  </div>
</section>

<section class="nf-band nf-results" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">All-in-one vs piece-by-piece</span>
      <h2>One login <span class="g">instead of a stack of tools</span></h2>
    </div>
    <ul class="nf-feat">
      <li><b>Funnels and websites</b><span>Unlimited funnels, landing pages and websites, on every plan.</span></li>
      <li><b>CRM and pipelines</b><span>Every lead, deal and conversation in one record.</span></li>
      <li><b>Email and SMS</b><span>Campaigns, automations and two-way texting built in.</span></li>
      <li><b>AI agents</b><span>Chat and voice agents that reply to leads in seconds, day and night.</span></li>
      <li><b>Booking</b><span>Calendars, reminders and no-show follow-up.</span></li>
      <li><b>Payments</b><span>Invoices, text-to-pay, order forms and subscriptions.</span></li>
    </ul>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-two" style="margin-top:0">
      <div class="nf-box"><h3>When {E(n)} might suit you better</h3><p>{E(c["better"])}</p></div>
      <div class="nf-box"><h3>How to switch from {E(n)}</h3><p>{E(c["switch"])}</p></div>
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap nf-faq">
    <div>
      <span class="nf-eyebrow">FAQ</span>
      <h2>Oceanic Funnels vs {E(n)}, <span class="g">answered</span></h2>
    </div>
    <div class="nf-faq-list">
{faq}
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-cta-band nf-hatch" style="--hc:var(--coral)">
      <div><h2>Stop fishing for customers. Build the net.</h2><p>One system, one bill, unlimited contacts. Founding member pricing locks in for life.</p></div>
      <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">Build my net <span class="ar" aria-hidden="true">→</span></a>
    </div>
    <div class="nf-more" aria-label="Other comparisons">{more}<a href="/compare/">All comparisons</a></div>
  </div>
</section>'''
    title = f"Oceanic Funnels vs {n}: The {n} Alternative | Oceanic Funnels"
    if len(title) > 62: title = f"Oceanic Funnels vs {n} | {n} Alternative"
    if c.get("title"): title = c["title"]
    extra = [faq_schema(faqs)]
    desc = c["answer"]
    if len(desc) > 158: desc = desc[:155].rsplit(" ", 1)[0] + "…"
    return path, page(cfg, fonts, path, title, desc, crumbs, body, logo, extra)

def hub_page(cfg, fonts, logo):
    path = "/compare/"; crumbs = [("Home", "/"), ("Compare", path)]
    cards = "".join(f'''<a href="/compare/{c["slug"]}/"><span class="vs">vs {E(c["name"])}</span><h2>{E(c["h1"])}</h2><p>{E(c["name"])} is {E(art(c["kind"]))}. See features, pricing and how to switch.</p><span class="go">Compare →</span></a>''' for c in COMPETITORS)
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in c">
      {crumbs_html(crumbs)}
      <h1>Compare Oceanic Funnels</h1>
      <p class="nf-sub">See how Oceanic Funnels OS compares with the funnel builders, CRMs and marketing tools you might be paying for today. Prices checked {CHECKED}.</p>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:64px">
  <div class="nf-wrap"><div class="nf-hub">{cards}</div></div>
</section>'''
    return path, page(cfg, fonts, path, "Compare Oceanic Funnels vs ClickFunnels, HubSpot and More",
                      "Compare Oceanic Funnels OS with Skool, ClickFunnels, Kajabi, HubSpot, Shopify, ActiveCampaign, Keap, Klaviyo and Salesforce, using their own published pricing.", crumbs, body, logo)

def deep_sections(d, X):
    money = "".join(f'<li><span class="n">Leak {i+1}</span><b>{E(t)}</b><p>{E(x)}</p><p class="fix"><span>The fix</span>{E(f)}</p></li>' for i, (t, x, f) in enumerate(X["money"]))
    rows = "".join(f'<tr><th scope="row">{E(a)}</th><td data-l="Typical rhythm">{E(b)}</td><td data-l="What the system does" class="us">✓ {E(c)}</td></tr>' for a, b, c in X["treatments"])
    dfy = "".join(f'<li>{E(x)}</li>' for x in X["dfy"])
    c = X["calc"]
    fields = "".join(f'<div class="nf-field"><label for="dc-{k}">{E(v[0])} <output id="dc-{k}-o"></output></label><input id="dc-{k}" type="range" min="{v[2]}" max="{v[3]}" step="{v[4]}" value="{v[1]}"></div>' for k, v in c.items())
    top = f'''<section class="nf-band" style="padding-top:0" id="leaks">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">The leaks</span>
      <h2>{E(X["money_h"][0])} <span class="g">{E(X["money_h"][1])}</span></h2>
    </div>
    <ul class="nf-money">{money}</ul>
  </div>
</section>

<section class="nf-band" style="padding-top:0" id="treatments">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Treatment by treatment</span>
      <h2>{E(X["treat_h"][0])} <span class="g">{E(X["treat_h"][1])}</span></h2>
    </div>
    <div class="nf-tablewrap nf-treat">
      <table class="nf-table">
        <thead><tr><th scope="col">Treatment</th><th scope="col">Typical rhythm</th><th scope="col" class="us">What the system does</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p class="nf-replnote">{E(X["treat_note"])}</p>
  </div>
</section>'''
    mid = f'''<section class="nf-band" id="leak-calculator">
  <div class="nf-wrap">
    <div class="nf-calc">
      <div>
        <span class="nf-eyebrow">Quick math</span>
        <h2>What slow replies <span class="g">cost you</span></h2>
        <p class="nf-sub">Example numbers. Move the sliders to match your clinic.</p>
        <div class="nf-inputs">{fields}</div>
      </div>
      <div class="nf-result" aria-live="polite">
        <div class="row"><span>Enquiries waiting too long</span><span id="dc-r1"></span></div>
        <div class="row"><span>Clients you could be winning</span><span id="dc-r2"></span></div>
        <div class="row"><span>Per month</span><span id="dc-r3"></span></div>
        <div class="big">Per year, first visits only<strong id="dc-r4"></strong></div>
        <p class="note">Before rebooking, memberships or referrals. A model, not a promise.</p>
        <a class="nf-btn nf-btn--aqua nf-btn--lg" href="#scale-plan">Stop the leak <span class="ar" aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>
</section>

<section class="nf-band nf-dark" id="scale-plan">
  <div class="nf-wrap">
    <div class="nf-caps">
      <span class="nf-eyebrow">Scale plan</span>
      <h2>{E(X["dfy_h"][0])} <span class="g">{E(X["dfy_h"][1])}</span></h2>
    </div>
    <div class="nf-dfy">
      <ul class="nf-dfy-list">{dfy}</ul>
      <aside class="nf-dfy-card">
        <span class="plan">Scale</span>
        <div class="amt"><span class="v">$297</span><small>/month</small></div>
        <p class="fee">No build fee</p>
        <ul><li>Every feature, including all AI</li><li>Dedicated account manager</li><li>A builder who sets it up with you</li><li>Live in 14 days</li><li>Cancel anytime</li></ul>
        <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">Get it built for me <span class="ar" aria-hidden="true">→</span></a>
        <p class="small">Rather build it yourself? <a href="/#pricing">Start on Growth from $97/month</a>.</p>
      </aside>
    </div>
  </div>
</section>
<script>
(function(){{var $=function(i){{return document.getElementById(i)}},n=function(x){{return Math.round(x).toLocaleString("en-US")}};
function u(){{var e=+$("dc-enq").value,m=+$("dc-miss").value/100,c=+$("dc-close").value/100,v=+$("dc-val").value;
$("dc-enq-o").textContent=n(e);$("dc-miss-o").textContent=Math.round(m*100)+"%";$("dc-close-o").textContent=Math.round(c*100)+"%";$("dc-val-o").textContent="$"+n(v);
var w=e*m,k=w*c;$("dc-r1").textContent=n(w);$("dc-r2").textContent=n(k);$("dc-r3").textContent="$"+n(k*v);$("dc-r4").textContent="$"+n(k*v*12)}}
["enq","miss","close","val"].forEach(function(k){{$("dc-"+k).addEventListener("input",u)}});u()}})();
</script>'''
    return top, mid

def industry_page(cfg, fonts, logo, d):
    path = f"/industries/{d['slug']}/"; n = d["name"]; W = d["who"].split(" like ")[0]
    X = DEEP.get(d["slug"])
    hook, sub = (X["hook"], X["sub"]) if X else (d["hook"], d["sub"])
    crumbs = [("Home", "/"), ("Industries", "/industries/"), (n, path)]
    leaks = "".join(f'<li><span class="n">Leak {i+1}</span><b>{E(t)}</b><span>{E(x)}</span></li>' for i, (t, x) in enumerate(d["leaks"]))
    flow = "".join(f'<li><span class="t">{E(t)}</span><span class="d">{i+1}</span><b>{E(h)}</b><p>{E(x)}</p></li>' for i, (t, h, x) in enumerate(d["flow"]))
    autos = "".join(f'<li><b>{E(t)}</b><span>{E(x)}</span></li>' for t, x in d["autos"])
    funnels = "".join(f'<li>{E(f)}</li>' for f in d["funnels"])
    faqs = [(f"How do {d['who']} automate their sales with Oceanic Funnels?", d["answer"])] + (X["faqs"] + d["faqs"] if X else d["faqs"] + GENERIC_FAQ)
    deep_top, deep_mid = deep_sections(d, X) if X else ("", "")
    LEAKS = f'''<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Where customers slip away</span>
      <h2>Three leaks in most <span class="g">{E(W)}</span></h2>
    </div>
    <ul class="nf-leaks">{leaks}</ul>
  </div>
</section>'''
    faq = "\n".join(f'<details class="nf-q"{" open" if i == 0 else ""}><summary><h3>{E(q)}</h3><span aria-hidden="true">+</span></summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(faqs))
    more = "".join(f'<a href="/industries/{o["slug"]}/">{E(o["name"])}</a>' for o in INDUSTRIES if o["slug"] != d["slug"] and o["cat"] == d["cat"])
    rg = [g for g in GUIDES if d["slug"] in g["related_ind"]]
    rg += [g for g in GUIDES if g["slug"] in ("missed-call-text-back", "speed-to-lead", "ai-chat-agent-for-business", "get-more-google-reviews") and g not in rg]
    guides = "".join(f'<a href="/guides/{g["slug"]}/">{E(g["kw"].split(":")[0])}</a>' for g in rg[:6])
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in">
      {crumbs_html(crumbs)}
      <span class="nf-vs">For {E(n)}</span>
      <h1>{E(d["h1"])}</h1>
      <p class="nf-sub"><b>{E(hook)}.</b> {E(sub)}</p>
      <div class="nf-hero-cta">
        <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">{"Get it built for me" if X else "Build my net"} <span class="ar" aria-hidden="true">→</span></a>
        <a class="nf-btn nf-btn--line" href="{"#scale-plan" if X else "#how-it-runs"}">{"See what we build" if X else "See how it runs"}</a>
      </div>
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:72px">
  <div class="nf-wrap">
    <div class="nf-panel">
      <div>
        <span class="nf-eyebrow">The short answer</span>
        <h2>How {E(d["who"].split(" like ")[0])} <span class="g">automate with Oceanic Funnels</span></h2>
        <p class="nf-def">{E(d["answer"])}</p>
      </div>
      <ul class="nf-facts">
        <li><span class="k">Leads from</span><span>Funnels, ads, social DMs, calls and your website</span></li>
        <li><span class="k">Replies</span><span>Within seconds, by SMS, email, WhatsApp and AI agent</span></li>
        <li><span class="k">Booking</span><span>Calendars with automatic reminders</span></li>
        <li><span class="k">Starts at</span><span>$97/month for the full system, unlimited contacts and users</span></li>
      </ul>
    </div>
  </div>
</section>

{deep_top if X else LEAKS}

<section class="nf-band nf-dark" id="how-it-runs">
  <div class="nf-wrap">
    <div class="nf-caps">
      <span class="nf-eyebrow">Your net, step by step</span>
      <h2>How the system runs <span class="g">without you</span></h2>
    </div>
    <ol class="nf-run">{flow}</ol>
  </div>
</section>
{deep_mid}

<section class="nf-band">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Automations we set up</span>
      <h2>Built for <span class="g">{E(W)}</span></h2>
    </div>
    <ul class="nf-feat">{autos}</ul>
    <div class="nf-two">
      <div class="nf-box"><h3>Funnels you can launch</h3><ul class="nf-chips">{funnels}</ul></div>
      <div class="nf-box ink"><h3>Never lose a lead again</h3><p>Missed call text back, instant replies, AI agents and reminders mean every call, form and DM gets answered, day or night. Unlimited contacts and users from the Growth plan up.</p></div>
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap nf-faq">
    <div>
      <span class="nf-eyebrow">FAQ</span>
      <h2>Questions from <span class="g">{E(W)}</span></h2>
    </div>
    <div class="nf-faq-list">
{faq}
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-cta-band nf-hatch" style="--hc:var(--coral)">
      <div><h2>{E(X["cta_h"]) if X else "Stop fishing for customers. Build the net."}</h2><p>{E(X["cta_p"]) if X else "One system for funnels, CRM, SMS, WhatsApp, AI agents, booking and payments. Or let our team build it for you."}</p></div>
      <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">{"Get it built for me" if X else "Build my net"} <span class="ar" aria-hidden="true">→</span></a>
    </div>
    <h2 class="nf-more-h">Guides for {E(W)}</h2>
    <div class="nf-more" aria-label="Guides">{guides}<a href="/guides/">All guides</a></div>
    <h2 class="nf-more-h">More in {E(d["cat"].lower())}</h2>
    <div class="nf-more" aria-label="Related industries">{more}<a href="/industries/">All {len(INDUSTRIES)} industries</a></div>
  </div>
</section>'''
    title = f"{d['kw']} | Oceanic Funnels"
    if len(title) > 62: title = d["kw"]
    extra = [faq_schema(faqs), {"@type": "Service", "@id": cfg["domain"] + path + "#service", "name": d["kw"],
             "serviceType": "CRM, sales funnel and marketing automation software", "description": d["answer"],
             "provider": {"@id": cfg["domain"] + "/#org"}, "areaServed": "Worldwide",
             "audience": {"@type": "BusinessAudience", "name": n},
             "offers": {"@type": "Offer", "price": "97", "priceCurrency": "USD", "url": CK}}]
    desc = d["answer"]
    if len(desc) > 158: desc = desc[:155].rsplit(" ", 1)[0] + "…"
    return path, page(cfg, fonts, path, title, desc, crumbs, body, logo, extra)

def industries_hub(cfg, fonts, logo):
    path = "/industries/"; crumbs = [("Home", "/"), ("Industries", path)]
    groups = ""
    for cat in CATEGORIES:
        items = [d for d in INDUSTRIES if d["cat"] == cat]
        cid = re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")
        cards = "".join(f'''<a href="/industries/{d["slug"]}/"><span class="vs">{E(d["name"])}</span><h3>{E(d["h1"])}</h3><p>{E(d["sub"])}</p><span class="go">See how it works →</span></a>''' for d in items)
        groups += f'<div class="nf-hubgrp" id="{cid}"><h2>{E(cat)}</h2><div class="nf-hub">{cards}</div></div>'
    jump = "".join(f'<a href="#{re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-")}">{E(c)}</a>' for c in CATEGORIES)
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in c">
      {crumbs_html(crumbs)}
      <h1>CRM and marketing automation for every industry</h1>
      <p class="nf-sub">See how {len(INDUSTRIES)} kinds of business use Oceanic Funnels OS to catch every lead, answer every call, book every appointment and bring customers back, on autopilot.</p>
      <div class="nf-more" style="justify-content:center">{jump}</div>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:64px">
  <div class="nf-wrap">{groups}</div>
</section>'''
    return path, page(cfg, fonts, path, "CRM & Marketing Automation by Industry | Oceanic Funnels",
                      f"How {len(INDUSTRIES)} industries, from home services and dental practices to gyms, real estate and coaches, automate leads, booking and follow-up with Oceanic Funnels OS.", crumbs, body, logo)

def guide_page(cfg, fonts, logo, g):
    path = f"/guides/{g['slug']}/"
    crumbs = [("Home", "/"), ("Guides", "/guides/"), (g["title"], path)]
    ids = [re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-") for h, _ in g["sections"]]
    toc = "".join(f'<li><a href="#{i}">{E(h)}</a></li>' for i, (h, _) in zip(ids, g["sections"]))
    toc += '<li><a href="#faq">FAQ</a></li>'
    secs = "".join(f'<section id="{i}"><h2>{E(h)}</h2>{c}</section>' for i, (h, c) in zip(ids, g["sections"]))
    faq = "\n".join(f'<details class="nf-q"{" open" if i == 0 else ""}><summary><h3>{E(q)}</h3><span aria-hidden="true">+</span></summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(g["faqs"]))
    srcs = ""
    if g["sources"]:
        srcs = '<section><h2>Sources</h2><ul>' + "".join(f'<li><a href="{u}" rel="nofollow noopener" target="_blank">{E(t)}</a></li>' for t, u in g["sources"]) + '</ul></section>'
    inds = [d for d in INDUSTRIES if d["slug"] in g["related_ind"]]
    indl = "".join(f'<a href="/industries/{d["slug"]}/">{E(d["name"])}</a>' for d in inds)
    rel = [o for o in GUIDES if o["slug"] != g["slug"] and o["cat"] == g["cat"]] + [o for o in GUIDES if o["slug"] != g["slug"] and o["cat"] != g["cat"]]
    more = "".join(f'<a href="/guides/{o["slug"]}/">{E(o["kw"].split(":")[0])}</a>' for o in rel[:10]) + '<a href="/guides/">All guides</a>' 
    pbox = ""
    if g.get("plan") == "launch":
        pbox = (f'<div class="nf-gcta"><div><b>Build this on Launch for $17/month</b><span>Unlimited funnels and websites, an online store, checkout and payments. No coding. Cancel anytime.</span></div>'
                f'<a class="nf-btn nf-btn--ink" href="/lp/launch/?utm_source=site&amp;utm_medium=guide&amp;utm_campaign={g["slug"]}">Start for $17/month</a></div>')
    elif g.get("plan_box"):
        t, d, u, b = g["plan_box"]
        pbox = f'<div class="nf-gcta"><div><b>{E(t)}</b><span>{E(d)}</span></div><a class="nf-btn nf-btn--ink" href="{u}">{E(b)}</a></div>'
    upd = g.get("updated", GUIDE_DATE)
    date = datetime_fmt(upd)
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in">
      {crumbs_html(crumbs)}
      <span class="nf-vs">{E(g["cat"])}</span>
      <h1 style="font-size:clamp(34px,4.6vw,58px)">{E(g["title"])}</h1>
      <p class="nf-sub">{E(g["desc"])}</p>
      <div class="nf-meta"><span>By <b>Oceanic Funnels Team</b></span><span>Updated <time datetime="{upd}">{date}</time></span><span>{g["read"]} min read</span></div>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:56px">
  <div class="nf-wrap nf-doc-wrap">
    <aside class="nf-toc"><b>In this guide</b><ol>{toc}</ol></aside>
    <article class="nf-doc">
      <div class="nf-answer"><b class="k">The short answer</b><p>{E(g["short"])}</p></div>
      {pbox}
      {secs}
      {pbox if pbox else '<div class="nf-gcta"><div><b>Want help setting this up?</b><span>On Scale, your dedicated account manager and builder help you set it up and grow.</span></div><a class="nf-btn nf-btn--ink" href="' + CK + '">Build my net</a></div>'}
      {srcs}
    </article>
  </div>
</section>
<section class="nf-band" id="faq" style="padding-top:0">
  <div class="nf-wrap nf-faq">
    <div><span class="nf-eyebrow">FAQ</span><h2>Questions, <span class="g">answered</span></h2></div>
    <div class="nf-faq-list">
{faq}
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-cta-band nf-hatch" style="--hc:var(--coral)">
      <div><h2>Stop fishing for customers. Build the net.</h2><p>Funnels, CRM, email, SMS, WhatsApp, AI agents, booking and payments in one system, from $97 a month.</p></div>
      <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">Build my net <span class="ar" aria-hidden="true">→</span></a>
    </div>
    <h2 class="nf-more-h">Built for these industries</h2>
    <div class="nf-more">{indl}<a href="/industries/">All industries</a></div>
    <h2 class="nf-more-h">More guides</h2>
    <div class="nf-more">{more}</div>
  </div>
</section>'''
    title = f"{g['kw']} | Oceanic Funnels"
    if len(title) > 62: title = g["kw"]
    extra = [faq_schema(g["faqs"]), {"@type": "BlogPosting", "@id": cfg["domain"] + path + "#article", "headline": g["title"],
             "description": g["desc"], "datePublished": GUIDE_DATE, "dateModified": upd, "inLanguage": "en",
             "author": {"@type": "Organization", "name": "Oceanic Funnels Team", "url": cfg["domain"] + "/"},
             "publisher": {"@id": cfg["domain"] + "/#org"}, "mainEntityOfPage": cfg["domain"] + path,
             "image": cfg["domain"] + "/og-image.png", "articleSection": g["cat"]}]
    return path, page(cfg, fonts, path, title, g["desc"], crumbs, body, logo, extra)

def datetime_fmt(iso):
    import datetime as _dt
    d = _dt.date.fromisoformat(iso)
    return d.strftime("%B ") + str(d.day) + d.strftime(", %Y")

def guides_hub(cfg, fonts, logo):
    path = "/guides/"; crumbs = [("Home", "/"), ("Guides", path)]
    groups = ""
    for cat in GUIDE_CATS:
        items = [g for g in GUIDES if g["cat"] == cat]
        if not items: continue
        cid = re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")
        cards = "".join(f'''<a class="nf-gcard" href="/guides/{g["slug"]}/"><span class="vs">{E(g["cat"])}</span><h3>{E(g["title"])}</h3><p>{E(g["desc"])}</p><span class="rt">{g["read"]} min read</span><span class="go">Read the guide →</span></a>''' for g in items)
        groups += f'<div class="nf-hubgrp" id="{cid}"><h2>{E(cat)}</h2><div class="nf-hub">{cards}</div></div>'
    jump = "".join(f'<a href="#{re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-")}">{E(c)}</a>' for c in GUIDE_CATS if any(g["cat"] == c for g in GUIDES))
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in c">
      {crumbs_html(crumbs)}
      <h1>Sales and marketing automation guides</h1>
      <p class="nf-sub">{len(GUIDES)} practical, step-by-step guides to answering every lead, booking more appointments, building websites and funnels, selling online and automating your business.</p>
      <div class="nf-more" style="justify-content:center">{jump}</div>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:64px">
  <div class="nf-wrap">{groups}</div>
</section>'''
    extra = [{"@type": "CollectionPage", "@id": cfg["domain"] + path + "#collection", "name": "Sales and marketing automation guides",
              "hasPart": [{"@type": "BlogPosting", "headline": g["title"], "url": cfg["domain"] + f"/guides/{g['slug']}/"} for g in GUIDES]}]
    return path, page(cfg, fonts, path, "Sales & Marketing Automation Guides | Oceanic Funnels",
                      f"{len(GUIDES)} step-by-step guides on CRM, automation, AI agents, websites, SEO, online stores, courses, communities, payments, reviews and more.", crumbs, body, logo, extra)

CSS_VER = "1"

def build_all(cfg, fonts, src, site):
    css, logo = extract(src)
    os.makedirs(f"{site}/assets", exist_ok=True)
    global CSS_VER
    full = css + PAGE_CSS
    CSS_VER = __import__("hashlib").md5(full.encode()).hexdigest()[:10]
    open(f"{site}/assets/site.css", "w").write(full)
    out = [legal_page(cfg, fonts, logo, "privacy", "Privacy Policy | Oceanic Funnels", "Privacy Policy",
                      "How Oceanic Funnels collects, uses, shares and protects personal information, including SMS consent, cookies, analytics and your privacy rights.", legal.PRIVACY),
           legal_page(cfg, fonts, logo, "terms", "Terms of Service | Oceanic Funnels", "Terms of Service",
                      "The terms of service that apply when you use oceanicfunnels.com, use Oceanic Funnels OS and our account services: billing, cancellation and data.", legal.TERMS),
           hub_page(cfg, fonts, logo), about_page(cfg, fonts, logo),
           tools.speed_to_lead_test(cfg, fonts, logo, page, crumbs_html, faq_schema)]
    out += [compare_page(cfg, fonts, logo, c) for c in COMPETITORS]
    out += [industries_hub(cfg, fonts, logo)] + [industry_page(cfg, fonts, logo, d) for d in INDUSTRIES]
    out += [guides_hub(cfg, fonts, logo)] + [guide_page(cfg, fonts, logo, g) for g in GUIDES]
    for path, htm in out + [lp_med_spa(cfg, fonts, logo), lp_med_book(cfg, fonts, logo), lp_med_booked(cfg, fonts, logo), lp_med_welcome(cfg, fonts, logo), lp_launch(cfg, fonts, logo), thank_you(cfg, fonts, logo)]:
        d = site + path
        os.makedirs(d, exist_ok=True)
        px = pixel_for(path)
        if px:
            htm = htm.replace("</head>", px + "\n</head>", 1)
        open(d + "index.html", "w").write(htm)
    return [p for p, _ in out]


# ---------------- Ad landing pages (noindex, not in sitemap) ----------------
LP_CSS = r"""
.lp-head{display:flex;justify-content:space-between;align-items:center;gap:16px;padding-block:18px}
.lp-hero{background:linear-gradient(180deg,#DEF4F0 0%,#EEF3F2 60%,#FBEEE9 100%)}
.lp-hero .in{padding-block:48px 72px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:48px;align-items:center}
.lp-kick{display:inline-block;font-family:var(--display);font-size:13px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--coral-d)}
.lp-hero h1{font-size:clamp(38px,5.2vw,64px);line-height:1.02;letter-spacing:-.045em;margin-top:14px}
.lp-hero h1 em{font-style:normal;background:linear-gradient(transparent 64%,var(--aqua) 64% 90%,transparent 90%)}
.lp-hero .sub{font-size:19px;line-height:1.55;margin-top:20px;color:var(--text);max-width:52ch}
.lp-ticks{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:22px;font-size:15px}
.lp-ticks span::before{content:"\2713";display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--ink);color:var(--aqua);font-size:11px;font-weight:700;margin-right:8px;vertical-align:-3px}
.lp-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.lp-phone{background:var(--ink);border-radius:34px;padding:14px;box-shadow:0 30px 60px -30px rgba(14,26,27,.55);max-width:380px;margin-inline:auto;width:100%}
.lp-phone .scr{background:#F4F8F7;border-radius:24px;padding:18px 16px 20px;display:flex;flex-direction:column;gap:12px;font-size:15px;line-height:1.4}
.lp-phone .bar{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);font-weight:600}
.lp-phone .ch{font-family:var(--display);font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);text-align:center}
.lp-q{align-self:flex-end;background:var(--ink);color:#fff;border-radius:18px 18px 4px 18px;padding:11px 14px;max-width:85%}
.lp-a{align-self:flex-start;background:#fff;border:1px solid var(--line);border-radius:18px 18px 18px 4px;padding:11px 14px;max-width:90%}
.lp-a b{display:block;font-family:var(--display);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--coral-d);margin-bottom:3px}
.lp-tag{align-self:center;font-size:12px;font-weight:600;color:var(--aqua-d);background:var(--aqua-l);padding:5px 12px;border-radius:999px}
.lp-three{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:44px}
.lp-three .lp-phone{max-width:none;border-radius:28px;padding:10px}
.lp-three .lp-phone .scr{border-radius:20px;min-height:330px}
.lp-three h3{font-size:21px;margin-top:20px}
.lp-three p.d{font-size:15.5px;color:var(--text);margin-top:6px;line-height:1.5}
.lp-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:40px}
.lp-stat{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px}
.lp-stat .n{font-family:var(--display);font-size:56px;font-weight:700;letter-spacing:-.05em;line-height:1;color:var(--ink)}
.lp-stat p{margin-top:12px;font-size:16px;line-height:1.5}
.lp-stat small{display:block;margin-top:12px;font-size:13px;color:var(--muted)}
.lp-vs{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:40px}
.lp-vs>div{border-radius:var(--r);padding:30px}
.lp-vs .no{background:#fff;border:1px solid var(--line)}
.lp-vs .yes{background:var(--ink);color:#fff}
.lp-vs h3{font-size:20px}.lp-vs .yes h3{color:var(--aqua)}
.lp-vs ul{list-style:none;margin-top:16px;display:grid;gap:12px;font-size:16px;line-height:1.45}
.lp-vs .no li::before{content:"\00D7";color:var(--coral-d);font-weight:700;margin-right:10px}
.lp-vs .yes li::before{content:"\2713";color:var(--aqua);font-weight:700;margin-right:10px}
.lp-book{background:var(--ink);color:#fff;text-align:center}
.lp-book h2{color:#fff}
.lp-book p{color:#C9D6D4;font-size:18px;max-width:56ch;margin:16px auto 0;line-height:1.55}
.lp-book .lp-cta{justify-content:center}
.lp-pains{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-top:40px}
.lp-pain{background:#fff;border:1px solid var(--line);border-left:4px solid var(--coral);border-radius:var(--r);padding:20px 20px;font-size:16px;line-height:1.45;color:var(--text)}
.lp-pain b{display:block;font-family:var(--display);font-size:18px;letter-spacing:-.01em;color:var(--ink);margin-bottom:4px}
.lp-three{grid-template-columns:repeat(4,minmax(0,1fr))!important}
.lp-guar{margin:14px 0 4px;background:var(--aqua-l);color:var(--ink);border-radius:10px;padding:12px 14px;font-weight:600;font-size:15px;line-height:1.4}
.lp-guar small{display:block;font-weight:400;font-size:12.5px;color:var(--muted);margin-top:4px}
.lp-pay{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:48px;max-width:960px;margin-inline:auto;align-items:stretch}
.lp-pay .nf-price .for{min-height:0}
.lp-pay .nf-price .for b{display:block;font-family:var(--display);font-size:19px;color:var(--ink);margin-bottom:4px}
.lp-pay .nf-price--pop .for b{color:#fff}
.lp-pay .nf-price li{padding:11px 6px}
.lp-pay .nf-price--pop .plan{color:var(--aqua);box-shadow:inset 0 0 0 1.5px var(--aqua)}
.lp-pay .nf-price .after{margin-top:18px}
.lp-pay .nf-hatch::after{width:44%;height:190px}
.lp-sum.nf-hatch::after{width:34%;height:100%}
.lp-vs .yes.nf-hatch::after{width:40%;height:150px}
.nf-result.nf-hatch::after{width:40%;height:140px}
.lp-sum{max-width:960px;margin:18px auto 0;background:var(--ink);color:#fff;border-radius:var(--r);padding:30px 34px;display:grid;grid-template-columns:1fr 1fr;gap:6px 34px;align-items:center}
.lp-sum .row{display:flex;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid #2A3A3A;color:#C9D6D4;font-size:16px}
.lp-sum .row b{color:#fff;text-align:right}
.lp-sum .lp-guar{grid-column:2;grid-row:1/3;margin:0}
.lp-sum .nf-btn{grid-column:1/-1;justify-self:center;margin-top:18px}
.lp-sum .small{grid-column:1/-1;text-align:center;color:#B9C9C6;font-size:14px;margin-top:4px}
.lp-sum .small a{color:#fff}
@media(max-width:800px){.lp-sum.nf-hatch::after{height:90px;width:30%}.lp-pay{grid-template-columns:1fr}.lp-sum{grid-template-columns:1fr;padding:24px 20px}.lp-sum .lp-guar{grid-column:1;grid-row:auto;margin-top:12px}.lp-sum .nf-btn{white-space:normal;text-align:center;max-width:100%}}
.lp-sticky{display:none}
@media (max-width:1100px){.lp-three{grid-template-columns:repeat(2,minmax(0,1fr))!important}.lp-pains{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:700px){.lp-three,.lp-pains{grid-template-columns:1fr!important}
.lp-sticky{display:block;position:fixed;left:0;right:0;bottom:0;z-index:50;padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:rgba(14,26,27,.94);backdrop-filter:blur(6px)}
.lp-sticky .nf-btn{width:100%;justify-content:center}
body:has(.lp-sticky){padding-bottom:76px}}
.lp-m{display:none}
@media (max-width:600px){.lp-d{display:none}.lp-m{display:inline}.lp-head .nf-btn{padding:10px 16px;font-size:14.5px}.lp-book .nf-btn{white-space:normal;text-align:center;font-size:15.5px;padding:16px 22px;max-width:100%}}
@media (max-width:900px){.lp-hero .in{grid-template-columns:1fr;gap:36px;padding-block:28px 56px}.lp-three,.lp-stats,.lp-vs{grid-template-columns:1fr}}
"""
PAGE_CSS += LP_CSS


def lp_med_spa(cfg, fonts, logo):
    X = DEEP["med-spas"]
    path = "/lp/med-spas/"
    book = CAL_MED
    mail = CAL_MED
    head = f'<header class="lp-head nf-wrap">{logo}<a class="nf-btn nf-btn--ink" href="{book}"><span class="lp-d">Book a free info call</span><span class="lp-m">Free info call</span></a></header>'
    def phone(ch, msgs, tag=None):
        inner = "".join((f'<div class="lp-q">{E(t)}</div>' if w == "u" else f'<div class="lp-a"><b>{E(w)}</b>{E(t)}</div>') for w, t in msgs)
        return f'<div class="lp-phone"><div class="scr"><div class="bar"><span>{E(ch[0])}</span><span>{E(ch[1])}</span></div><div class="ch">{E(ch[2])}</div>{inner}{f"<span class=lp-tag>{E(tag)}</span>" if tag else ""}</div></div>'
    hero_phone = phone(("9:14 PM", "Saturday", "Instagram DM"), [
        ("u", "Hi! How much is lip filler and do you have anything this week?"),
        ("AI agent", "Hi! Lip filler starts from $650. Your provider confirms the plan at your consultation. We have Thursday 4:00 or Saturday 11:00. Which works?"),
        ("u", "Saturday please!"),
        ("AI agent", "Booked for Saturday at 11:00. A $50 deposit link is on its way to hold your spot.")], "Booked in 2 minutes. Deposit paid.")
    three = [
        (phone(("11:02 PM", "Wednesday", "Website chat"), [("u", "Do you do laser hair removal? How many sessions?"), ("AI agent", "We do! Most clients need several sessions a few weeks apart, and your provider sets your plan. Want a consultation Monday 5:00 or Tuesday 9:30?"), ("u", "Tuesday"), ("AI agent", "Booked. Confirmation and intake form sent.")]),
         "Website and social enquiries answered 24/7", "Your AI agent knows your menu, prices and policies, books the consultation and hands anything clinical to your team."),
        (phone(("2:47 PM", "Tuesday", "Text message"), [("Clinic", "Hi, it's Glow Aesthetics. Sorry we missed your call, we're with a client. How can we help?"), ("u", "Looking to book a HydraFacial this week"), ("Clinic", "Thursday 11:00 or Friday 3:00? Book here: [link]")]),
         "No missed call goes to a competitor", "The moment a call goes unanswered, the caller gets a text from your number and the conversation keeps going."),
        (phone(("9:00 AM", "Day before", "Text message"), [("Clinic", "Reminder: your consultation is tomorrow at 2:00 with Dr. Lee. Reply C to confirm or R to reschedule."), ("u", "R"), ("Clinic", "No problem! Pick a new time here: [link]. Your deposit carries over.")]),
         "Fewer no-shows, deposits held", "Deposits at booking, reminders before every visit and a one-tap reschedule link, so empty chairs get refilled."),
        (phone(("10:00 AM", "Month 4", "Text message"), [("Clinic", "Hi Sarah! It's about 4 months since your last Botox. Want to book your next appointment before it wears off? [link]"), ("u", "Yes please, same injector"), ("Clinic", "Done! Booked with Jess on the 14th at 2:00.")]),
         "Clients rebooked on time", "Rebooking reminders timed to each treatment, so clients come back to you instead of whoever runs a promo that week."),
    ]
    three_html = "".join(f'<div>{p}<h3>{E(h)}</h3><p class="d">{E(d)}</p></div>' for p, h, d in three)
    c = X["calc"]
    fields = "".join(f'<div class="nf-field"><label for="dc-{k}">{E(v[0])} <output id="dc-{k}-o"></output></label><input id="dc-{k}" type="range" min="{v[2]}" max="{v[3]}" step="{v[4]}" value="{v[1]}"></div>' for k, v in c.items())
    dfy = "".join(f'<li>{E(x)}</li>' for x in X["dfy"][:10])
    build = "".join(f'<li>{E(x)}</li>' for x in [
        "Booking pages for your top three treatments",
        "Consultation booking with a deposit or card on file",
        "An AI agent trained on your menu, prices and policies, answering Instagram, Facebook, website chat and text",
        "Missed call text back on your business number",
        "Intake and consent forms sent before every visit",
        "Reminders and no-show rebooking",
        "Rebooking reminders for each treatment",
        "Membership and package plans",
        "Review requests after every visit",
        "A campaign to bring back past clients",
        "Meta Pixel, Conversions API and GA4 for your ads"])
    monthly = "".join(f'<li>{E(x)}</li>' for x in [
        "One inbox for Instagram, Facebook, text, email and website chat",
        "Your client list and pipeline, from enquiry to member",
        "Online calendar, deposits, payments and memberships",
        "All your automations running 24/7",
        "24/7 support",
        "Every AI feature: chat and voice agents, content and reviews AI",
        "Founding price locked for life (first 50 clinics)",
        "No contract, cancel anytime"])
    faqs = [
        ("Do we need a sales team or appointment setters?", "No. The AI agent answers enquiries, books consultations and sends deposit links, and automations handle reminders, no-shows and rebooking. Your front desk only steps in when a client needs a person."),
        ("Does it replace our EMR or booking software?", "Most med spas keep their EMR for charts and clinical notes. Oceanic Funnels handles enquiries, consultation booking, reminders, rebooking, memberships, payments and marketing. We agree with you which bookings live where."),
        ("Do you run our ads?", "No. We build and run the system that catches and converts your leads. If you run ads, we install the Meta Pixel, Conversions API and GA4 so you can see which ads lead to booked treatments."),
        ("How fast will it be live?", "With Done-For-You Setup, usually within 14 days of getting your content, logins and approvals, and your team reviews everything before it goes live. If you set it up yourself, you can start building the day you sign up."),
        ("What happens to our data if we cancel?", "You keep it. You can export your contacts and data at any time, your domain stays in your name, and every plan is month to month with no lock-in."),
        ("What does it cost?", "The system is $197 a month on our AI Pro plan, with no contract. If you want us to build it all for you, add Done-For-You Setup for a one-time $997. Usage like texts, emails and AI replies is pay-as-you-go from your wallet."),
    ]
    faq = "\n".join(f'<details class="nf-q"{" open" if i == 0 else ""}><summary><h3>{E(q)}</h3><span aria-hidden="true">+</span></summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(faqs))
    body = f'''<section class="lp-hero">
  {head}
  <div class="nf-wrap in">
    <div>
      <span class="lp-kick">For med spas and aesthetic clinics</span>
      <h1>Stop losing Botox and filler bookings to <em>slow replies.</em></h1>
      <p class="sub">We build your med spa a system that answers every DM, call and enquiry in seconds, books consultations with a deposit and rebooks clients on time. No sales team needed. Run it yourself, or have us build it for you in 14 days.</p>
      <div class="lp-ticks"><span>Done for you in 14 days</span><span>No contract</span><span>You own the system</span></div>
      <div class="lp-cta">
        <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{book}">Install my revenue system <span class="ar" aria-hidden="true">→</span></a>
      </div>
    </div>
    {hero_phone}
  </div>
</section>

<section class="nf-band lp-pains-band">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Sound familiar?</span>
      <h2>Where med spas lose bookings <span class="g">every week</span></h2>
      <p class="nf-sub">If two or more of these happen at your clinic, money is slipping out every week.</p>
    </div>
    <div class="lp-pains"><div class="lp-pain"><b>You pay for every lead</b> then someone replies hours later, after they've booked elsewhere.</div><div class="lp-pain"><b>The phone rings mid-treatment</b> and the caller hangs up and tries the next clinic on Google.</div><div class="lp-pain"><b>DMs from 10 PM</b> get answered at 10 AM, when the client has already moved on.</div><div class="lp-pain"><b>Free consults book</b> then never show, and a provider's hour disappears.</div><div class="lp-pain"><b>Botox clients drift past month four</b> because nobody reminds them it's time.</div><div class="lp-pain"><b>Happy clients leave</b> without ever leaving a Google review.</div><div class="lp-pain"><b>Past clients sit untouched</b> in your booking software, years of revenue nobody contacts.</div><div class="lp-pain"><b>Memberships and packages</b> tracked by hand, with failed payments nobody chases.</div></div>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">See it work</span>
      <h2>What your clients see, <span class="g">day and night</span></h2>
    </div>
    <div class="lp-three">{three_html}</div>
    <p class="nf-srcs" style="text-align:center;margin-top:18px">Illustrations. Clinic names, prices and times are examples.</p>
  </div>
</section>

<section class="nf-band" style="padding-top:0" id="leak-calculator">
  <div class="nf-wrap">
    <div class="nf-calc">
      <div>
        <span class="nf-eyebrow">Your numbers</span>
        <h2>What slow replies <span class="g">cost your clinic</span></h2>
        <p class="nf-sub">Move the sliders to match your med spa.</p>
        <div class="nf-inputs">{fields}</div>
      </div>
      <div class="nf-result nf-hatch" aria-live="polite">
        <div class="row"><span>Enquiries waiting too long</span><span id="dc-r1"></span></div>
        <div class="row"><span>Clients you could be winning</span><span id="dc-r2"></span></div>
        <div class="row"><span>Per month</span><span id="dc-r3"></span></div>
        <div class="big">Per year, first visits only<strong id="dc-r4"></strong></div>
        <p class="note">Before rebooking, memberships or referrals. A model, not a promise.</p>
        <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{book}">Fix this for my clinic <span class="ar" aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Why speed matters</span>
      <h2>The first clinic to reply <span class="g">usually wins</span></h2>
    </div>
    <div class="lp-stats">
      <div class="lp-stat"><div class="n">7&times;</div><p>Firms that contacted a lead within an hour were nearly 7 times as likely to qualify it as firms that waited an hour longer.</p><small>Harvard Business Review, The Short Life of Online Sales Leads</small></div>
      <div class="lp-stat"><div class="n">74%</div><p>of consumers only care about reviews from the last three months, so fresh reviews after every visit matter.</p><small>BrightLocal Local Consumer Review Survey 2026</small></div>
      <div class="lp-stat"><div class="n">45%</div><p>of US consumers now use AI tools to find local businesses, up from 6% a year earlier.</p><small>BrightLocal Local Consumer Review Survey 2026</small></div>
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">The difference</span>
      <h2>Your clinic today vs <span class="g">with the system</span></h2>
    </div>
    <div class="lp-vs">
      <div class="no"><h3>Today</h3><ul><li>DMs answered the next morning</li><li>Missed calls go to voicemail</li><li>Free consults that never show up</li><li>Botox clients drifting past month four</li><li>Reviews only when someone remembers to ask</li></ul></div>
      <div class="yes nf-hatch"><h3>With Oceanic Funnels</h3><ul><li>Every DM answered in seconds, 24/7</li><li>Missed calls texted back instantly</li><li>Deposits and reminders cut no-shows</li><li>Rebooking reminders timed to each treatment</li><li>A review request after every visit</li></ul></div>
    </div>
  </div>
</section>

<section class="nf-band nf-pricing" id="price">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Pricing</span>
      <h2>What you pay for, <span class="g">in plain words</span></h2>
    </div>
    <div class="lp-pay">
      <article class="nf-price">
        <span class="plan">AI Pro plan</span>
        <div class="amt"><span class="v">$197</span> <small>/month</small></div>
        <p class="for"><b>The system your clinic runs on.</b> Every feature, including the AI agent that answers and books for you 24/7.</p>
        <ul><li class="lead">Every month you get:</li>{monthly}</ul>
        <p class="after">30-day money-back guarantee. Texts, emails, calls and AI replies are pay-as-you-go from your account wallet.</p>
      </article>
      <article class="nf-price nf-price--pop nf-hatch">
        <span class="plan">Done-For-You Setup</span>
        <div class="amt"><span class="v">$997</span> <small>one time</small></div>
        <p class="for"><b>Optional: we build it for you.</b> Our team sets up your whole system and launches it in 14 days.</p>
        <ul><li class="lead">What we build:</li>{build}</ul>
        <p class="after">Add it at checkout. Paid once.</p>
      </article>
    </div>
    <div class="lp-sum nf-hatch" style="--hc:var(--coral)">
      <div class="row"><span>Set it up yourself</span><b>$197 today, then $197/month</b></div>
      <div class="row"><span>Done for you</span><b>$1,194 today ($997 setup + first month), then $197/month</b></div>
      <p class="lp-guar">With Done-For-You Setup, if you're not live in 14 days, your first $197 month is free.<small>The 14 days start once we have your content and logins. Cancel the plan anytime.</small></p>
      <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{book}">Install my revenue system <span class="ar" aria-hidden="true">→</span></a>
      <p class="small">Ready now? <a href="{CK_IND["med-spas"]}">Go to checkout</a>.</p>
    </div>
  </div>
</section>

<section class="nf-band" id="faq">
  <div class="nf-wrap nf-faq">
    <div><span class="nf-eyebrow">Questions</span><h2>Before you <span class="g">book</span></h2></div>
    <div class="nf-faq-list">
{faq}
    </div>
  </div>
</section>

<div class="lp-sticky"><a class="nf-btn nf-btn--aqua" href="{book}">Install my revenue system <span class="ar" aria-hidden="true">→</span></a></div>
<section class="nf-band lp-book nf-hatch" id="book" style="--hc:var(--coral)">
  <div class="nf-wrap">
    <span class="nf-eyebrow" style="color:var(--aqua)">Free, 15 minutes</span>
    <h2>Ready to install your revenue system?</h2>
    <p>Book a free 15-minute info call. We show you how the system works for your clinic, what we build and how fast it goes live. No pressure, no pitch deck.</p>
    <div class="lp-cta"><a class="nf-btn nf-btn--aqua nf-btn--lg" href="{mail}">I'm ready to install my revenue system <span class="ar" aria-hidden="true">→</span></a></div>
  </div>
</section>
<script>
(function(){{var $=function(i){{return document.getElementById(i)}},n=function(x){{return Math.round(x).toLocaleString("en-US")}};
function u(){{var e=+$("dc-enq").value,m=+$("dc-miss").value/100,c=+$("dc-close").value/100,v=+$("dc-val").value;
$("dc-enq-o").textContent=n(e);$("dc-miss-o").textContent=Math.round(m*100)+"%";$("dc-close-o").textContent=Math.round(c*100)+"%";$("dc-val-o").textContent="$"+n(v);
var w=e*m,k=w*c;$("dc-r1").textContent=n(w);$("dc-r2").textContent=n(k);$("dc-r3").textContent="$"+n(k*v);$("dc-r4").textContent="$"+n(k*v*12);}}
["dc-enq","dc-miss","dc-close","dc-val"].forEach(function(i){{$(i).addEventListener("input",u)}});u();}})();
</script>'''
    return lp_shell(cfg, fonts, logo, path, "Med Spa Booking System, Built for You | Oceanic Funnels",
               "Every DM, call and enquiry answered in seconds, booked with a deposit and rebooked on time. Run it yourself or have it built for you in 14 days.", body)

def lp_shell(cfg, fonts, logo, path, title, desc, body, book=None, cta=True):
    book = book or CAL_MED
    htm = page(cfg, fonts, path, title, desc, [("Home", "/"), ("Med spas", "/lp/med-spas/")], body, logo)
    htm = htm.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex, follow">')
    i = htm.find('<footer class="nf-foot">'); j = htm.find('</footer>', i) + len('</footer>')
    mini = ('<footer class="nf-foot"><div class="nf-wrap nf-foot-top" style="grid-template-columns:1fr"><div style="max-width:640px">'
            '<h2>Stop fishing. Build the net.</h2>'
            '<p>Every DM, call and enquiry answered in seconds, booked with a deposit and rebooked on time. Run it yourself or have it built for you in 14 days.</p>'
            + (f'<a class="nf-btn nf-btn--aqua" href="{book}">Install my revenue system</a>' if cta else '') + '</div></div>'
            f'<div class="nf-wrap nf-foot-bot"><span>© 2026 {E(cfg["brand"])}. All rights reserved.</span>'
            '<span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a></span></div>'
            '<div class="nf-wordmark" aria-hidden="true">OCEANIC</div></footer>')
    htm = htm[:i] + mini + htm[j:]
    return path, htm

LP_BOOK_CSS = """
.lp-bk{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:44px;align-items:start;padding-block:28px 72px}
.lp-bk h1{font-family:var(--display);font-size:clamp(34px,4.6vw,52px);line-height:1.03;letter-spacing:-.035em;margin-top:14px}
.lp-bk h1 em{font-style:normal;color:var(--aqua-d)}
.lp-bk .sub{font-size:17px;color:var(--text);margin-top:14px;line-height:1.55}
.lp-bk ul{list-style:none;margin-top:22px;display:grid;gap:12px}
.lp-bk li{display:flex;gap:12px;font-size:16px;line-height:1.45;color:var(--ink)}
.lp-bk li::before{content:"\\2713";flex:none;width:22px;height:22px;border-radius:50%;background:var(--aqua);color:var(--ink);font-size:11px;font-weight:700;display:grid;place-items:center;margin-top:1px}
.lp-bk .meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.lp-bk .meta span{font-size:13px;font-weight:600;background:#fff;border:1px solid var(--line);padding:6px 12px;border-radius:999px;color:var(--ink)}
.lp-bk .price{margin-top:22px;font-size:14.5px;color:var(--muted)}
.lp-cal{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:8px;min-height:720px;box-shadow:0 20px 50px -30px rgba(14,26,27,.35)}
.lp-cal iframe{width:100%;min-height:700px;border:0;display:block}
.lp-done{max-width:720px;margin:0 auto;padding-block:40px 80px;text-align:center}
.lp-done .ok{width:64px;height:64px;border-radius:50%;background:var(--aqua);color:var(--ink);display:grid;place-items:center;margin:0 auto;font-size:30px;font-weight:700}
.lp-done h1{font-family:var(--display);font-size:clamp(36px,5vw,56px);letter-spacing:-.035em;margin-top:18px;line-height:1.03}
.lp-done .sub{font-size:18px;color:var(--text);margin-top:14px;line-height:1.55}
.lp-prep{list-style:none;counter-reset:p;display:grid;gap:12px;margin-top:30px;text-align:left}
.lp-prep li{counter-increment:p;display:flex;gap:14px;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:18px 20px;font-size:16px;line-height:1.45}
.lp-prep li::before{content:counter(p);flex:none;width:28px;height:28px;border-radius:50%;background:var(--ink);color:#fff;font-family:var(--display);font-weight:700;font-size:13px;display:grid;place-items:center}
.lp-prep b{display:block;color:var(--ink)}
@media(max-width:900px){.lp-bk{grid-template-columns:1fr;gap:24px;padding-block:16px 56px}.lp-bk ul,.lp-bk .meta{display:none}}
"""

PAGE_CSS += LP_BOOK_CSS

def lp_med_book(cfg, fonts, logo):
    path = "/lp/med-spas/book/"
    head = f'<header class="lp-head nf-wrap">{logo}<span class="lp-tag" style="background:#fff">Free, 15 minutes</span></header>'
    body = f'''<section class="lp-hero nf-hatch">
  {head}
  <div class="nf-wrap lp-bk">
    <div>
      <span class="lp-kick">Med spas and aesthetic clinics</span>
      <h1>Book your free <em>info call.</em></h1>
      <p class="sub">Pick a time that suits you. In 15 minutes we show you how the system works for your clinic and whether it is a fit.</p>
      <ul>
        <li>Where your clinic is losing bookings right now</li>
        <li>How the system answers, books and rebooks for you, 24/7</li>
        <li>What we build in your first 14 days</li>
        <li>Clear pricing, no pressure, no pitch deck</li>
      </ul>
      <div class="meta"><span>15 minutes</span><span>No obligation</span><span>Free</span></div>
      <p class="price">$197/month on AI Pro, plus optional Done-For-You Setup for $997 one time. No contract.</p>
    </div>
    <div class="lp-cal">
      <iframe src="{CAL_EMBED}" allow="payment" scrolling="no" id="0Fq9d6ETDejl4rKothS4_1793371640258" title="Book your free info call"></iframe>
    </div>
  </div>
</section>
<script src="https://links.oceanicfunnels.com/js/form_embed.js" type="text/javascript"></script>'''
    return lp_shell(cfg, fonts, logo, path, "Book Your Free Info Call | Oceanic Funnels",
                    "Book a free 15-minute info call to see how the system answers, books and rebooks for your med spa.", body)

def lp_med_booked(cfg, fonts, logo):
    path = "/lp/med-spas/booked/"
    head = f'<header class="lp-head nf-wrap">{logo}</header>'
    body = f'''<section class="lp-hero">
  {head}
  <div class="nf-wrap lp-done">
    <div class="ok" aria-hidden="true">&#10003;</div>
    <h1>You're booked.</h1>
    <p class="sub">Your confirmation and calendar invite are on the way by email and text. To get the most from 15 minutes, have these ready:</p>
    <ol class="lp-prep">
      <li><span><b>Your top three treatments and prices</b>For example Botox, filler and laser, so we can show you the right booking flows.</span></li>
      <li><span><b>Roughly how many enquiries you get a month</b>DMs, calls and website forms. A rough guess is fine.</span></li>
      <li><span><b>The booking or EMR software you use today</b>So we can show you how the system works alongside it.</span></li>
    </ol>
    <div class="lp-cta" style="justify-content:center;margin-top:30px"><a class="nf-btn nf-btn--ink" href="/lp/med-spas/#price">See what we build <span class="ar" aria-hidden="true">→</span></a></div>
  </div>
</section>
<script>if(window.fbq){{fbq('track','Schedule',{{content_name:'med-spa-info-call'}})}}</script>'''
    return lp_shell(cfg, fonts, logo, path, "You're Booked | Oceanic Funnels",
                    "Your free info call is booked.", body, cta=False)

def lp_med_welcome(cfg, fonts, logo):
    path = "/lp/med-spas/welcome/"
    head = f'<header class="lp-head nf-wrap">{logo}</header>'
    body = f'''<section class="lp-hero">
  {head}
  <div class="nf-wrap lp-done">
    <div class="ok" aria-hidden="true">&#10003;</div>
    <h1>Welcome aboard. You&#39;re in.</h1>
    <p class="sub">Your payment went through. Your receipt and your login invite are on their way by email. Here is what happens next.</p>
    <ol class="lp-prep">
      <li><span><b>Check your email for your login invite</b>Open the email from us, set your password and sign in to your system. Check spam if it is not in your inbox.</span></li>
      <li><span><b>Added Done-For-You Setup? Fill in your onboarding form</b>We email it to you. It covers your logo, treatment menu and prices, providers, booking and cancellation policies, and any before-and-after photos you have consent to use.</span></li>
      <li><span><b>Give us access to your accounts</b>For Done-For-You Setup: admin access to your Instagram and Facebook page and your website or domain. Your business phone line is set up inside the system.</span></li>
      <li><span><b>We build and launch in 14 days</b>With Done-For-You Setup, the 14 days start once we have your onboarding form and access, and your team reviews everything before it goes live. Setting it up yourself? You can start building as soon as you sign in.</span></li>
    </ol>
    <p class="sub" style="font-size:15px;margin-top:26px">Questions? Email <a href="mailto:{E(cfg["email"])}" style="color:var(--aqua-d);font-weight:600">{E(cfg["email"])}</a></p>
  </div>
</section>'''
    return lp_shell(cfg, fonts, logo, path, "Welcome to Oceanic Funnels | Your Account Is Ready",
                    "Welcome to Oceanic Funnels. Here is what happens next.", body, cta=False)


# ---------------- Launch $17 ad landing page ----------------
LAUNCH_CK = "https://checkout.oceanicfunnels.com/oceanic_funnels-launch-offer"
LAUNCH_CSS = r"""
.ln-sec{padding-block:72px}
.ln-sec.alt{background:#F4F8F7}
.ln-sec h2{font-family:var(--display);font-size:clamp(30px,4vw,46px);line-height:1.05;letter-spacing:-.035em;max-width:22ch}
.ln-sec .lead{font-size:18px;line-height:1.6;color:var(--text);margin-top:16px;max-width:60ch}
.ln-center{text-align:center}.lp-book.ln-sec h2{margin-inline:auto}.ln-center h2,.ln-center .lead{margin-inline:auto}
.ln-hook{font-family:var(--display);font-size:20px;font-weight:700;color:var(--ink);margin-top:18px}
.ln-note{font-size:14px;color:var(--muted);margin-top:12px}
.ln-flow{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:8px}
.ln-win{background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 24px 50px -32px rgba(14,26,27,.45)}
.ln-win .tb{display:flex;align-items:center;gap:6px;padding:9px 12px;background:#EEF3F2;border-bottom:1px solid var(--line);font-size:11px;color:var(--muted)}
.ln-win .tb i{width:8px;height:8px;border-radius:50%;background:#D5DEDC;display:inline-block}
.ln-win .tb span{margin-left:8px;background:#fff;border-radius:6px;padding:2px 8px;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ln-win .pg{padding:16px;font-size:12.5px;line-height:1.45;color:var(--text);min-height:250px;display:flex;flex-direction:column;gap:9px}
.ln-win .pg .k{font-size:9.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--coral-d)}
.ln-win .pg h4{font-family:var(--display);font-size:17px;line-height:1.1;color:var(--ink);letter-spacing:-.02em}
.ln-win .img{height:62px;border-radius:9px;background:linear-gradient(135deg,#DEF4F0,#FBEEE9)}
.ln-win .bt{align-self:flex-start;background:var(--ink);color:#fff;font-weight:700;font-size:11.5px;border-radius:999px;padding:7px 12px}
.ln-win .fld{border:1px solid var(--line);border-radius:7px;padding:7px 9px;color:var(--muted);font-size:11.5px}
.ln-win .row{display:flex;justify-content:space-between;border-bottom:1px dashed var(--line);padding-bottom:6px}
.ln-win .ok{width:34px;height:34px;border-radius:50%;background:var(--aqua);display:grid;place-items:center;font-weight:800;color:var(--ink)}
.ln-cap{text-align:center;font-family:var(--display);font-weight:700;font-size:15px;margin-top:12px;color:var(--ink)}
.ln-cap small{display:block;font-family:inherit;font-weight:400;color:var(--muted);font-size:13px}
.ln-feat{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:40px}
.ln-feat div{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:24px}
.ln-feat b{display:block;font-family:var(--display);font-size:19px;color:var(--ink);letter-spacing:-.01em}
.ln-feat p{margin-top:8px;font-size:15.5px;line-height:1.5;color:var(--text)}
.ln-steps{list-style:none;counter-reset:s;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:40px}
.ln-steps li{counter-increment:s;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:26px}
.ln-steps li::before{content:counter(s);display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--ink);color:var(--aqua);font-family:var(--display);font-weight:700}
.ln-steps b{display:block;font-family:var(--display);font-size:19px;margin-top:14px;color:var(--ink)}
.ln-steps p{margin-top:6px;font-size:15.5px;line-height:1.5;color:var(--text)}
.ln-who{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px;margin-top:40px}
.ln-who div{background:#fff;border:1px solid var(--line);border-top:4px solid var(--aqua);border-radius:var(--r);padding:20px;font-size:15px;line-height:1.5;color:var(--text)}
.ln-who b{display:block;font-family:var(--display);font-size:17px;color:var(--ink);margin-bottom:6px}
.ln-price{max-width:520px;margin:40px auto 0;background:var(--ink);color:#fff;border-radius:22px;padding:34px 32px;text-align:left}
.ln-price .pl{font-family:var(--display);font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--aqua)}
.ln-price .amt{font-family:var(--display);font-size:64px;font-weight:700;letter-spacing:-.05em;line-height:1;margin-top:10px}
.ln-price .amt small{font-size:20px;letter-spacing:0;color:#C9D6D4;font-weight:600}
.ln-price .tag{color:#C9D6D4;margin-top:10px;font-size:16px}
.ln-price ul{list-style:none;display:grid;gap:10px;margin-top:22px;font-size:16px}
.ln-price li::before{content:"\2713";color:var(--aqua);font-weight:700;margin-right:10px}
.ln-price .nf-btn{width:100%;justify-content:center;margin-top:26px}
.ln-price .fine{font-size:13.5px;color:#B9C9C6;text-align:center;margin-top:10px}
.ln-good{max-width:520px;margin:16px auto 0;font-size:14.5px;line-height:1.55;color:var(--text);background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.ln-faq{max-width:780px;margin:36px auto 0;display:grid;gap:10px}
.ln-faq details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 20px}
.ln-faq summary{cursor:pointer;font-family:var(--display);font-weight:700;font-size:17px;color:var(--ink);list-style:none}
.ln-faq summary::-webkit-details-marker{display:none}
.ln-faq summary::after{content:"+";float:right;color:var(--muted)}
.ln-faq details[open] summary::after{content:"\2212"}
.ln-faq p{margin-top:10px;font-size:15.5px;line-height:1.55;color:var(--text)}
.ln-hin{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:56px;align-items:center;padding-block:28px 88px}
.ln-copy h1{font-family:var(--display);font-size:clamp(38px,4.8vw,62px);line-height:1.02;letter-spacing:-.045em;margin-top:14px;max-width:16ch}
.ln-copy .sub{font-size:18.5px;line-height:1.55;margin-top:14px;max-width:46ch;color:var(--text)}
.ln-dev{position:relative;padding-bottom:36px}
.ln-vwrap{text-align:center}
.ln-vid{position:relative;border:10px solid var(--aqua);border-radius:16px;overflow:hidden;background:#fff;aspect-ratio:16/9;box-shadow:0 18px 40px -26px rgba(10,127,110,.45)}
.ln-vid video{width:100%;height:100%;display:block;object-fit:cover;cursor:pointer}
.ln-play{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;border:0;cursor:pointer;background:rgba(255,255,255,.08);color:#fff;font:inherit}
.ln-play .ic{width:84px;height:84px;border-radius:50%;background:var(--aqua);color:var(--ink);display:grid;place-items:center;padding-left:5px;box-shadow:0 12px 26px -10px rgba(14,26,27,.45);transition:transform .2s}
.ln-play:hover .ic{transform:scale(1.07)}
.ln-play .tx{font-weight:700;font-size:16px;background:var(--ink);padding:7px 14px;border-radius:999px}
.ln-vid.on .ln-play{display:none}
.ln-prog{position:absolute;left:0;right:0;bottom:0;height:5px;background:rgba(14,26,27,.12)}
.ln-prog i{display:block;height:100%;width:0;background:var(--aqua-d)}
.ln-vcd{display:flex;justify-content:center;gap:14px;margin-top:22px}
.ln-vcd div{display:flex;flex-direction:column;align-items:center;gap:8px}
.ln-vcd b{width:76px;height:70px;border-radius:10px;background:var(--ink);color:#fff;display:grid;place-items:center;font-family:var(--display);font-weight:800;font-size:34px;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.ln-vcd span{font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink);background:var(--aqua-l);padding:3px 10px;border-radius:4px}
.ln-vcd-t{margin-top:12px;font-size:14px;color:var(--muted)}
@media(max-width:600px){.ln-vid{border-width:7px}.ln-vcd{gap:10px}.ln-vcd b{width:62px;height:58px;font-size:28px}.ln-play .ic{width:68px;height:68px}}
.ln-lap .scr{border:10px solid #1B1F22;border-bottom-width:14px;border-radius:18px 18px 6px 6px;overflow:hidden;background:#1B1F22;aspect-ratio:16/10;box-shadow:0 40px 70px -40px rgba(14,26,27,.6)}
.ln-lap img,.ln-bw img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.ln-lap .base{height:14px;margin:0 -6%;background:linear-gradient(#E3E6E9,#A9AFB6);border-radius:0 0 16px 16px}
.ln-ph{position:absolute;right:-14px;bottom:0;width:29%;border:7px solid #1B1F22;border-radius:28px;overflow:hidden;background:#fff;box-shadow:0 30px 50px -25px rgba(14,26,27,.6)}
.ln-ph img{width:100%;height:auto;display:block}
.ln-rot{display:grid}.ln-rot img{grid-area:1/1;opacity:0;transition:opacity .7s ease}.ln-rot img.on{opacity:1}
.ln-toast b,.ln-toast small{transition:opacity .3s}
@media(prefers-reduced-motion:reduce){.ln-rot img,.ln-toast b,.ln-toast small{transition:none}}
.ln-toast{position:absolute;left:-28px;top:56%;display:flex;gap:12px;align-items:center;background:#fff;border-radius:16px;padding:12px 18px 12px 12px;box-shadow:0 24px 44px -20px rgba(14,26,27,.5);animation:lnIn .6s .9s both}
.ln-toast .ic{width:38px;height:38px;border-radius:50%;background:var(--aqua);color:var(--ink);display:grid;place-items:center;font-weight:800;font-size:17px;flex:none}
.ln-toast b{display:block;font-size:15px;color:var(--ink)}.ln-toast small{font-size:12.5px;color:var(--muted)}
@keyframes lnIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){.ln-toast{animation:none}}
.ln-gal{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:40px}
.ln-gal figure{margin:0}
.ln-bw{border-radius:12px;overflow:hidden;border:1px solid var(--line);background:#fff;box-shadow:0 26px 50px -34px rgba(14,26,27,.5)}
.ln-bw .tb{display:flex;gap:6px;align-items:center;padding:9px 12px;background:#EEF3F2;border-bottom:1px solid var(--line)}
.ln-bw .tb i{width:8px;height:8px;border-radius:50%;background:#D5DEDC}
.ln-bw .im{aspect-ratio:16/10}
.ln-gal figcaption{margin-top:14px}
.ln-gal figcaption b{display:block;font-family:var(--display);font-size:18px;color:var(--ink)}
.ln-gal figcaption span{font-size:15px;color:var(--text)}
.ln-feat div:nth-child(7):last-child{grid-column:1/-1;display:grid;grid-template-columns:44px 1fr;column-gap:16px;align-items:center;background:var(--aqua-l);border-color:transparent}
.ln-feat div:nth-child(7):last-child .ico{grid-row:span 2;margin:0;background:#fff}
.ln-feat div:nth-child(7):last-child p{margin-top:2px}
.ln-feat .ico{width:44px;height:44px;border-radius:12px;background:var(--aqua-l);display:grid;place-items:center;margin-bottom:14px}
.ln-feat .ico svg{width:22px;height:22px;fill:none;stroke:var(--ink);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
@media(max-width:900px){.ln-hin{grid-template-columns:1fr;gap:40px;padding-block:20px 64px}.ln-gal{grid-template-columns:1fr}.ln-toast{left:6px;top:auto;bottom:6px}.ln-ph{right:-4px;width:31%}.ln-dev{padding:0 10px 40px 0}}
.ln-bar{background:var(--ink);color:#fff;font-size:14.5px}
.ln-bar-in{display:flex;justify-content:center;align-items:center;gap:8px 18px;flex-wrap:wrap;padding-block:10px;text-align:center}
.ln-bar s,.ln-hp s{opacity:.6}.ln-bar b{color:var(--aqua)}
.ln-cd{display:inline-flex;gap:4px;align-items:baseline;font-weight:600;white-space:nowrap}
.ln-cd i{font-style:normal;font-variant-numeric:tabular-nums;font-weight:800;background:rgba(61,227,200,.16);color:var(--aqua);border-radius:6px;padding:2px 6px;min-width:2.1em;text-align:center}
.ln-hp{margin-top:14px;font-size:17px;color:var(--ink)}.ln-hp b{font-weight:800}
.ln-price .amt s{font-size:30px;color:#8FA3A0;font-weight:600;margin-right:10px;letter-spacing:-.02em}
.ln-pr-cd{margin-top:16px;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:12px;padding:10px 14px;font-size:14px;color:#DDE7E5}
.ln-ended .ln-cd{display:none}
@media(max-width:600px){.ln-bar{font-size:13.5px}.ln-bar-in{flex-wrap:nowrap;gap:8px}}
.ln-show{margin-top:56px}
.ln-show h3{font-family:var(--display);font-size:clamp(22px,2.6vw,28px);color:var(--ink);text-align:center;letter-spacing:-.01em}
.ln-show-hint{text-align:center;font-size:14px;color:var(--muted);margin-top:6px}
.ln-show-vp{overflow:hidden;margin:18px -24px 0;padding:14px 0 20px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)}
.ln-track{display:flex;gap:22px;width:max-content;animation:lnSlide 40s linear infinite}
.ln-show-vp:hover .ln-track,.ln-show-vp.paused .ln-track{animation-play-state:paused}
@keyframes lnSlide{to{transform:translateX(calc(-50% - 11px))}}
.ln-fc{flex:0 0 300px;background:#fff;border-radius:12px;overflow:hidden;cursor:pointer;box-shadow:0 22px 40px -24px rgba(14,26,27,.5),0 0 0 1px rgba(14,26,27,.08);transition:transform .3s,box-shadow .3s}
.ln-fc:hover,.ln-fc.on{transform:translateY(-6px);box-shadow:0 30px 50px -24px rgba(14,26,27,.55),0 0 0 3px var(--aqua)}
.ln-fc .tb{height:24px;background:#E9EEED;display:flex;align-items:center;gap:6px;padding:0 10px}
.ln-fc .tb i{width:8px;height:8px;border-radius:50%;background:#FF6B5E}.ln-fc .tb i:nth-child(2){background:#FFBE2E}.ln-fc .tb i:nth-child(3){background:#2ACB42}
.ln-fc .vw{height:380px;overflow:hidden}
.ln-fc .vw img{display:block;width:100%;height:auto;transition:transform 1s ease-out}
.ln-fc:hover .vw img,.ln-fc.on .vw img{transform:translateY(calc(-100% + 380px));transition:transform var(--d) linear}
@media(max-width:700px){.ln-fc{flex-basis:240px}.ln-fc .vw{height:320px}.ln-fc:hover .vw img,.ln-fc.on .vw img{transform:translateY(calc(-100% + 320px))}.ln-track{animation-duration:30s}.ln-show-vp{margin-inline:-16px}}
@media(prefers-reduced-motion:reduce){.ln-track{animation-duration:120s}}
.ln-galsec{background:linear-gradient(180deg,#F4F8F7,#EAF3F1)}
.ln-stop{background:var(--ink);color:#fff;position:relative;overflow:hidden}
.ln-stop::before{content:"";position:absolute;right:-160px;top:-160px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(61,227,200,.22),rgba(61,227,200,0) 70%)}
.ln-stop-in{position:relative;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:56px;align-items:center}
.ln-stop h2{color:#fff}.ln-stop .lead{color:#C9D6D4}.ln-stop .ln-hook{color:var(--aqua)}
.ln-need{background:#fff;color:var(--ink);border-radius:22px;padding:26px;box-shadow:0 40px 70px -40px rgba(0,0,0,.7)}
.ln-need-h{font-size:14px;font-weight:600;color:var(--muted)}
.ln-need ul{list-style:none;display:grid;gap:12px;margin-top:16px}
.ln-need li{display:flex;gap:14px;align-items:flex-start;background:#F4F8F7;border-radius:14px;padding:16px}
.ln-need .ck{flex:none;width:30px;height:30px;border-radius:50%;background:var(--aqua);color:var(--ink);display:grid;place-items:center;font-weight:800}
.ln-need b{display:block;font-size:16.5px}.ln-need small{font-size:14px;color:var(--text)}
.ln-need-f{display:flex;justify-content:space-between;align-items:center;margin-top:16px;padding-top:16px;border-top:1px dashed var(--line);font-weight:600}
.ln-need-f b{font-family:var(--display);font-size:24px;letter-spacing:-.02em}
@media(max-width:900px){.ln-stop-in{grid-template-columns:1fr;gap:32px}}
.ln-pz{background:linear-gradient(180deg,#fff 0%,#EEF6F4 100%)}
.ln-pz-head{text-align:center}.ln-pz-head h2,.ln-pz-head .lead{margin-inline:auto}
.ln-pz-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;max-width:1040px;margin:44px auto 0;align-items:stretch}
.ln-pz .ln-price{max-width:none;margin:0;display:flex;flex-direction:column;position:relative;overflow:hidden;box-shadow:0 40px 70px -40px rgba(14,26,27,.65)}
.ln-pz .ln-price::after{content:"";position:absolute;right:-90px;top:-90px;width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,rgba(61,227,200,.28),rgba(61,227,200,0) 70%);pointer-events:none}
.ln-pr-top{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.ln-pr-badge{background:rgba(61,227,200,.14);color:var(--aqua);border:1px solid rgba(61,227,200,.4);font-size:13px;font-weight:700;padding:6px 12px;border-radius:999px;white-space:nowrap}
.ln-pz .ln-price ul{grid-template-columns:1fr 1fr;gap:12px 18px;font-size:15.5px}
.ln-pz .ln-price .nf-btn{margin-top:auto}
.ln-pz .ln-price ul{margin-bottom:28px}
.ln-pz .ln-price li{display:flex;gap:10px;line-height:1.4}.ln-pz .ln-price li::before{margin:0;flex:none}
.ln-pz-side{display:flex;flex-direction:column;gap:14px;text-align:left}
.ln-pz-side h3{font-family:var(--display);font-size:19px;letter-spacing:-.01em;color:var(--ink)}
.ln-after,.ln-why,.ln-up{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px 24px}
.ln-after ol{list-style:none;counter-reset:a;display:grid;gap:14px;margin-top:16px}
.ln-after li{counter-increment:a;display:grid;grid-template-columns:30px 1fr;column-gap:12px}
.ln-after li::before{content:counter(a);grid-row:1/3;width:30px;height:30px;border-radius:50%;background:var(--ink);color:var(--aqua);font-family:var(--display);font-weight:700;font-size:14px;display:grid;place-items:center}
.ln-after b{font-size:16px;color:var(--ink)}.ln-after span{font-size:14.5px;color:var(--text);line-height:1.45}
.ln-why{background:var(--aqua-l);border-color:transparent}
.ln-why p,.ln-up p{margin-top:6px;font-size:15px;line-height:1.5;color:var(--text)}
.ln-fees{font-size:13px;color:var(--muted);padding-inline:4px}
@media(max-width:860px){.ln-pz-grid{grid-template-columns:1fr}.ln-pz .ln-price ul{grid-template-columns:1fr}}
@media(max-width:1000px){.ln-who{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:800px){.ln-flow,.ln-feat,.ln-steps{grid-template-columns:1fr}.ln-sec{padding-block:52px}.ln-price{padding:28px 22px}}
@media(max-width:520px){.ln-who{grid-template-columns:1fr}}
"""
PAGE_CSS += LAUNCH_CSS
PAGE_CSS += r"""
.nf-score{display:flex;justify-content:center;gap:18px;margin:26px auto 22px;flex-wrap:wrap}
.nf-score>div{min-width:200px;text-align:center;padding:18px 26px;border-radius:16px;background:#fff;border:1px solid var(--line,#DCE6E3)}
.nf-score>div.us{background:var(--ink,#0E1A1B);color:#fff;border-color:transparent}
.nf-score b{display:block;font-family:var(--display);font-weight:800;font-size:44px;letter-spacing:-.03em;line-height:1}
.nf-score>div.us b{color:var(--aqua,#3DE3C8)}
.nf-score span{display:block;margin-top:6px;font-size:14px;font-weight:600;opacity:.8}
.nf-mx td{vertical-align:top}
.nf-mx td small{display:block;margin-top:3px;font-size:13px;color:var(--muted,#5B6967);font-weight:400}
.nf-mx td.us small{color:inherit;opacity:.75}
.mx{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;font-size:13px;font-weight:800;margin-right:6px;vertical-align:-4px}
.mx.y{background:#DDF7F2;color:#0A7F6E}.mx.p{background:#FFF3D6;color:#9A6400}.mx.a{background:#FFE7DF;color:#C2410C}.mx.n{background:#F3E1E1;color:#B42318}
.nf-xstack{margin:34px auto 0;max-width:860px;background:var(--ink,#0E1A1B);color:#fff;border-radius:20px;padding:32px 34px;display:block}
.nf-xstack h3{color:#fff;font-family:var(--display);font-size:24px;font-weight:800;letter-spacing:-.02em;margin:0}
.nf-xstack ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:12px 26px;margin:18px 0;padding:0}
.nf-xstack li{display:block;padding-left:24px;position:relative;font-size:15.5px;line-height:1.4;color:#fff}
.nf-xstack li:before{content:"✕";position:absolute;left:0;top:0;color:#FF8E73;font-weight:800}
.nf-xstack li b{display:block;color:#fff}.nf-xstack li span{display:block;opacity:.7;font-size:14px}
.nf-xstack p{color:#fff;opacity:.85;margin:6px 0 18px;font-size:15.5px;max-width:none}
.nf-xstack .nf-btn{display:inline-flex;width:auto}
@media(max-width:700px){.nf-xstack ul{grid-template-columns:1fr}.nf-xstack{padding:24px 20px}.nf-score>div{min-width:140px}.nf-score b{font-size:36px}}
"""


def lp_launch(cfg, fonts, logo):
    path = "/lp/launch/"
    ck = LAUNCH_CK
    btn = lambda t="Start Building for $17/Month", cls="nf-btn--aqua nf-btn--lg": f'<a class="nf-btn {cls}" href="{ck}">{E(t)} →</a>'
    head = f'<header class="lp-head nf-wrap">{logo}<a class="nf-btn nf-btn--ink" href="{ck}"><span class="lp-d">Start for $17/month</span><span class="lp-m">Start for $17</span></a></header>'
    win = lambda url, inner: f'<div class="ln-win"><div class="tb"><i></i><i></i><i></i><span>{E(url)}</span></div><div class="pg">{inner}</div></div>'
    flow = f'''<div class="ln-flow">
  <div>{win("yourbrand.com/guide", '<span class="k">New guide</span><h4>The 30-Day Meal Prep Plan</h4><div class="img"></div><p>Simple recipes, shopping lists and a weekly plan you can start tonight.</p><span class="bt">Get the guide · $27</span>')}<p class="ln-cap">1. Sales page<small>Explains your offer</small></p></div>
  <div>{win("yourbrand.com/checkout", '<span class="k">Checkout</span><h4>Complete your order</h4><div class="row"><span>30-Day Meal Prep Plan</span><b>$27.00</b></div><div class="fld">Email address</div><div class="fld">Card number</div><span class="bt">Pay $27.00</span>')}<p class="ln-cap">2. Checkout<small>Takes the payment</small></p></div>
  <div>{win("yourbrand.com/thank-you", '<div class="ok">✓</div><h4>You are in!</h4><p>Your guide is on its way to your inbox. Thanks for your order.</p><span class="bt">Download now</span>')}<p class="ln-cap">3. Thank-you page<small>Delivers what they bought</small></p></div>
</div>'''
    feats = [("Unlimited Sales Funnels", "Build sales pages, checkout journeys and thank-you pages for your products and services."),
             ("Unlimited Websites", "Create professional websites that represent your brand. Connect your own domain and publish."),
             ("Your Own Online Store", "Add products, create storefront pages and give customers somewhere to shop."),
             ("Built-In Payment Collection", "Connect a supported payment provider and accept payments through your store or checkout."),
             ("Drag-and-Drop Page Builder", "Choose a template, customize the design, add your content and publish without writing code."),
             ("One Place to Build and Sell", "Manage your websites, funnels, storefronts and selling pages from one Oceanic Funnels account."),
             ("24/7 Support", "Stuck on something? Our support team is here 24/7 to help you get your pages live.")]
    who = [("Coaches, teachers and nurses", "Turn what you know into guides, classes or sessions people can buy."),
           ("Entrepreneurs", "Give your new business idea a website or funnel people can actually visit."),
           ("Online Sellers", "Build an online storefront, show your products and accept payments."),
           ("Creators", "Create sales pages for your templates, resources and other products."),
           ("Small Businesses", "Build a professional online presence without hiring a developer for every new page.")]
    incl = ["Unlimited sales funnels", "Unlimited websites", "Online store builder", "Product pages and checkout",
            "Payment provider integration", "Drag-and-drop page editing", "Custom domain connection", "Ready-to-customize templates", "24/7 support"]
    faqs = [("Can I build a complete sales funnel?", "Yes. You can create sales pages, checkout pages and thank-you pages for your products and offers."),
            ("Can I create an online store?", "Yes. Add products, build your storefront and connect a supported payment provider."),
            ("Do I need coding experience?", "No. Oceanic Funnels includes a visual page builder, so you can create and customize pages without writing code."),
            ("Can I connect my own domain?", "Yes. You can connect a domain you own. Domain registration is separate if you need to buy one."),
            ("Can I collect payments?", "Yes. Connect a supported payment account to accept payments. Standard payment-processing fees may apply."),
            ("Does Launch include email and SMS marketing?", "No. Email and SMS marketing tools are available on Growth, with usage charges."),
            ("Can I upgrade later?", "Yes. You can move to Growth when you need more tools, such as CRM pipelines, lead capture forms and marketing automation."),
            ("Can your team build everything for me?", "Yes. Optional Done-For-You Setup is available for $997, with a defined scope of work."),
            ("Can I cancel anytime?", "Yes. Launch is a month-to-month subscription with no long-term contract.")]
    faq_schema = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    ICO = {'Unlimited Sales Funnels': '<path d="M3 4h18l-7 8v6l-4 2v-8z"/>', 'Unlimited Websites': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/>', 'Your Own Online Store': '<path d="M4 8h16l-1 12H5z"/><path d="M9 8a3 3 0 0 1 6 0"/>', 'Built-In Payment Collection': '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>', 'Drag-and-Drop Page Builder': '<rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/><path d="M15 3h6v6M9 21H3v-6"/>', 'One Place to Build and Sell': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>', '24/7 Support': '<path d="M4 13v-1a8 8 0 0 1 16 0v1"/><rect x="2.5" y="13" width="4" height="6" rx="1.5"/><rect x="17.5" y="13" width="4" height="6" rx="1.5"/><path d="M19.5 19c0 1.5-2 2.5-5 2.5"/>'}
    SHOW = [("mindset", 2574), ("strategy-call", 2150), ("salon-seo", 4691), ("sales-coach", 1557)]
    SHOW_CARDS = "".join(f'<div class="ln-fc" style="--d:{max(4, round(h/380))}s"><div class="tb"><i></i><i></i><i></i></div><div class="vw"><img src="/assets/showcase/{k}-full.webp" alt="A sales funnel built on Oceanic Funnels" width="560" height="{h}" loading="lazy"></div></div>' for k, h in SHOW)
    gal = "".join(f'<figure><div class="ln-bw"><div class="tb"><i></i><i></i><i></i></div><div class="im"><img src="/assets/launch/{f}.webp" alt="{E(alt)}" width="1920" height="1200" loading="lazy"></div></div><figcaption><b>{E(t)}</b><span>{E(d)}</span></figcaption></figure>'
                  for f, t, d, alt in [("sales", "Sales funnels for any offer", "A sales page, checkout and thank-you page for a product, service, program or download. Shown: a recipe guide.", "Example sales page for a meal prep guide"),
                                       ("store", "Online stores", "Product pages, prices and checkout for anything you ship or deliver. Shown: handmade ceramics.", "Example online store selling handmade ceramics"),
                                       ("teach", "Websites for your business", "A home for your brand, your services and your digital products. Shown: a teacher's resource site.", "Example website selling a teacher's reading kit")])
    body = f'''<div class="ln-bar" data-cd><div class="nf-wrap ln-bar-in"><span class="lp-d">Launch price <s>$37</s> <b>$17/month</b>. The price goes up to $37 on November 20.</span><span class="lp-m"><s>$37</s> <b>$17/month</b> ends in</span><span class="ln-cd" aria-label="Time left at $17"><i data-u="d">0</i>d <i data-u="h">00</i>h <i data-u="m">00</i>m <i data-u="s">00</i>s</span></div></div>
<section class="lp-hero nf-hatch">
  {head}
  <div class="nf-wrap ln-hin">
    <div class="ln-copy">
      <span class="lp-kick">Oceanic Funnels Launch, $17/month</span>
      <h1 id="ln-h1">Build Your First Sales Funnel. Start Selling Online.</h1>
      <p class="ln-hook">Your business idea isn't going to launch itself.</p>
      <p class="sub">Build unlimited sales funnels, professional websites and online stores. Add your products, connect payments and give your business a real place online. No coding. No developer needed.</p>
      <div class="lp-cta">{btn()}</div>
      <p class="ln-hp"><s>$37</s> <b>$17/month</b> until November 20</p>
      <p class="ln-note">Month-to-month. Cancel anytime. No mandatory setup fee.</p>
    </div>
    <div class="ln-vwrap">
      <div class="ln-vid" id="ln-vid">
        <video id="ln-video" src="/assets/video/oceanic-demo.mp4?v=2" poster="/assets/video/oceanic-demo-poster.webp" preload="none" playsinline width="1280" height="720"></video>
        <button class="ln-play" type="button" aria-label="Play the 1-minute demo"><span class="ic"><svg viewBox="0 0 24 24" width="30" height="30" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg></span><span class="tx">Watch the 1-minute demo</span></button>
        <div class="ln-prog" aria-hidden="true"><i></i></div>
      </div>
      <div class="ln-vcd ln-cd" data-cd aria-label="Time left at $17">
        <div><b data-u="d">0</b><span>Days</span></div><div><b data-u="h">00</b><span>Hours</span></div><div><b data-u="m">00</b><span>Minutes</span></div><div><b data-u="s">00</b><span>Seconds</span></div>
      </div>
      <p class="ln-vcd-t">$17/month ends November 20. Then it's $37.</p>
    </div>
  </div>
</section>
<section class="ln-sec ln-galsec"><div class="nf-wrap">
  <h2>What you can build with Launch</h2>
  <p class="lead">Whatever you sell, Launch gives you the pages to sell it: products, services, programs or digital downloads. Pick a template, add your own words and products, and publish.</p>
  <div class="ln-gal">{gal}</div>
  <div class="ln-show">
    <h3>Real funnels built on Oceanic Funnels</h3>
    <p class="ln-show-hint">Hover a funnel to scroll through the whole page</p>
    <div class="ln-show-vp"><div class="ln-track">{SHOW_CARDS}{SHOW_CARDS}</div></div>
  </div>
  <script>(function(){{var v=document.querySelector('.ln-show-vp');if(!v)return;v.querySelectorAll('.ln-fc').forEach(function(c){{c.addEventListener('click',function(){{var on=!c.classList.contains('on');v.querySelectorAll('.ln-fc.on').forEach(function(x){{x.classList.remove('on')}});if(on)c.classList.add('on');v.classList.toggle('paused',on);}});}});if('ontouchstart' in window){{var h=document.querySelector('.ln-show-hint');if(h)h.textContent='Tap a funnel to scroll through the whole page';}}}})();</script>
</div></section>
<section class="ln-sec ln-stop"><div class="nf-wrap ln-stop-in">
  <div>
    <h2>Stop Planning. Start Building.</h2>
    <p class="lead">You have the idea. Maybe it's a product you've wanted to sell, a skill you could turn into a business, or an online store you've been thinking about launching. But an idea doesn't become a business just because you keep thinking about it.</p>
    <p class="lead">At some point, you need to build something. That's where Oceanic Funnels comes in.</p>
    <p class="ln-hook">Start building your business online for $17 a month.</p>
    <div class="lp-cta">{btn()}</div>
  </div>
  <div class="ln-need">
    <p class="ln-need-h">What your idea needs to become a business</p>
    <ul>
      <li><span class="ck">✓</span><div><b>A website people can visit</b><small>Your own domain, your own brand</small></div></li>
      <li><span class="ck">✓</span><div><b>A sales page that explains your offer</b><small>What it is, who it's for, what it costs</small></div></li>
      <li><span class="ck">✓</span><div><b>A checkout where customers can buy</b><small>Card payments, straight to your account</small></div></li>
    </ul>
    <div class="ln-need-f"><span>All three, in one place</span><b>$17/month</b></div>
  </div>
</div></section>
<section class="ln-sec alt"><div class="nf-wrap">
  <h2>Your Idea. Your Website. Your Sales Funnel. Your Store.</h2>
  <p class="lead">Everything you need to start selling online.</p>
  <div class="ln-feat">{"".join(f'<div><span class="ico"><svg viewBox="0 0 24 24">{ICO[t]}</svg></span><b>{E(t)}</b><p>{E(d)}</p></div>' for t, d in feats)}</div>
  <div class="lp-cta">{btn()}</div>
</div></section>
<section class="ln-sec"><div class="nf-wrap">
  <h2>From Idea to Live Website in 3 Steps.</h2>
  <ol class="ln-steps">
    <li><b>Choose your starting point</b><p>Start with a funnel, website or online store. Pick a template or build from scratch.</p></li>
    <li><b>Make it yours</b><p>Add your brand, products, images, content, pricing and payment connection.</p></li>
    <li><b>Publish and share</b><p>Make your page live, share your link and give people a way to buy.</p></li>
  </ol>
  <p class="ln-hook">Your first launch doesn't have to be perfect. It just has to begin.</p>
</div></section>
<section class="ln-sec alt"><div class="nf-wrap">
  <h2>For People Ready to Build Something of Their Own.</h2>
  <div class="ln-who">{"".join(f"<div><b>{E(t)}</b>{E(d)}</div>" for t, d in who)}</div>
  <p class="lead">Whatever you're building, start with one offer and grow from there.</p>
</div></section>
<section class="ln-sec ln-pz" id="pricing"><div class="nf-wrap">
  <div class="ln-pz-head"><h2>Big Ideas Don't Always Need Big Budgets.</h2>
  <p class="lead">You don't need a huge software investment to start building your online presence.</p></div>
  <div class="ln-pz-grid">
    <div class="ln-price">
      <div class="ln-pr-top"><div><span class="pl">Launch plan</span><div class="amt"><s>$37</s>$17<small>/month</small></div></div><span class="ln-pr-badge">No setup fee</span></div>
      <div class="ln-pr-cd" data-cd><span>Price goes up to $37 on November 20</span><span class="ln-cd"><i data-u="d">0</i>d <i data-u="h">00</i>h <i data-u="m">00</i>m <i data-u="s">00</i>s</span></div>
      <p class="tag">Everything you need to build your pages and start selling.</p>
      <ul>{"".join(f"<li>{E(i)}</li>" for i in incl)}</ul>
      {btn()}
      <p class="fine">Month-to-month. Cancel anytime. No long-term contract.</p>
    </div>
    <div class="ln-pz-side">
      <div class="ln-after">
        <h3>What happens after you sign up</h3>
        <ol>
          <li><b>Your login arrives by email</b><span>Open your account and you're in.</span></li>
          <li><b>Pick a template</b><span>Choose a sales page, website or store to start from.</span></li>
          <li><b>Publish and share your link</b><span>Add your offer and price, connect payments and go live.</span></li>
        </ol>
      </div>
      <div class="ln-why"><h3>Why only $17?</h3><p>Launch gives you the tools to build and sell, and leaves out email, SMS and AI. That's how we keep it at $17.</p></div>
      <div class="ln-up"><h3>Need more later?</h3><p>Add email and SMS marketing, lead forms, a CRM and automated follow-ups anytime with Growth ($97/month).</p></div>
      <p class="ln-fees">Payment-processing fees, domain purchases and applicable taxes may cost extra.</p>
    </div>
  </div>
</div></section>
<section class="ln-sec alt"><div class="nf-wrap">
  <h2 class="ln-center" style="margin-inline:auto;text-align:center">Frequently Asked Questions</h2>
  <div class="ln-faq">{"".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs)}</div>
</div></section>
<section class="lp-book ln-sec"><div class="nf-wrap">
  <h2>Another Month of Planning, or Your First Step Forward?</h2>
  <p>You've already spent time thinking about the business you want to build. Now give that idea a real place online. Your website. Your funnel. Your store.</p>
  <p style="color:#fff;font-weight:700">The first step starts at $17/month.</p>
  <div class="lp-cta">{btn("Invest $17 in Your Next Step")}</div>
  <p style="font-size:14px">Month-to-month. Cancel anytime.</p>
</div></section>
<div class="lp-sticky">{btn("Start Building for $17/Month", "nf-btn--aqua")}</div>
<script>
(function(){{var h={{"b":"Build an Online Store and Take Payments.","d":"Invest $17 in Yourself. Sell What You Know Online."}};
var v=(new URLSearchParams(location.search).get("utm_content")||"").toLowerCase();if(h[v]){{document.getElementById("ln-h1").textContent=h[v]}}}})();
(function(){{var end=new Date("2026-11-20T00:00:00-05:00").getTime(),B=document.querySelectorAll("[data-cd]");
function p(n){{return n<10?"0"+n:""+n}}
function t(){{var ms=end-Date.now();if(ms<=0){{B.forEach(function(b){{b.style.display="none"}});return false}}
var s=Math.floor(ms/1000),v={{d:p(Math.floor(s/86400)),h:p(Math.floor(s%86400/3600)),m:p(Math.floor(s%3600/60)),s:p(s%60)}};
document.querySelectorAll(".ln-cd [data-u]").forEach(function(i){{i.textContent=v[i.dataset.u]}});return true}}
if(t())setInterval(t,1000)}})();
(function(){{var w=document.getElementById("ln-vid"),v=document.getElementById("ln-video");if(!w||!v)return;var bar=w.querySelector(".ln-prog i");
function tog(){{if(v.paused){{v.play()}}else{{v.pause()}}}}
w.querySelector(".ln-play").addEventListener("click",function(e){{e.stopPropagation();v.play()}});
v.addEventListener("click",tog);
v.addEventListener("play",function(){{w.classList.add("on")}});v.addEventListener("pause",function(){{w.classList.remove("on")}});
v.addEventListener("timeupdate",function(){{if(v.duration)bar.style.width=(v.currentTime/v.duration*100)+"%"}});
v.addEventListener("ended",function(){{w.classList.remove("on");v.currentTime=0}});}})();
</script>'''
    htm = page(cfg, fonts, path, "Build Your First Sales Funnel for $17/Month | Oceanic Funnels",
               "Build unlimited sales funnels, websites and online stores and take payments. No coding. $17/month, cancel anytime.",
               [("Home", "/"), ("Launch", path)], body, logo, extra=(faq_schema,))
    htm = htm.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex, follow">')
    i = htm.find('<footer class="nf-foot">'); j = htm.find('</footer>', i) + len('</footer>')
    mini = (f'<footer class="nf-foot"><div class="nf-wrap nf-foot-bot"><span>© 2026 {E(cfg["brand"])}. All rights reserved.</span>'
            '<span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a></span></div>'
            '<div class="nf-wordmark" aria-hidden="true">OCEANIC</div></footer>')
    return path, htm[:i] + mini + htm[j:]


# ---------------- Global thank-you page (all plans, all funnels) ----------------
def thank_you(cfg, fonts, logo):
    path = "/thank-you/"
    head = f'<header class="lp-head nf-wrap">{logo}</header>'
    body = f'''<section class="lp-hero nf-hatch">
  {head}
  <div class="nf-wrap lp-done">
    <div class="ok" aria-hidden="true">&#10003;</div>
    <h1>You&#39;re in. Welcome to Oceanic Funnels.</h1>
    <p class="sub" id="ty-sub">Your payment went through. Your receipt and your login invite are on their way by email.</p>
    <ol class="lp-prep">
      <li><span><b>Check your email for your login invite</b>Open the email from us, set your password and sign in. If it isn&#39;t in your inbox within a few minutes, check spam or promotions.</span></li>
      <li><span><b>Pick a template</b>Start with a sales page, website or store template, or build from scratch.</span></li>
      <li><span><b>Add your offer and connect payments</b>Put in your words, photos and prices, then connect your payment account.</span></li>
      <li><span><b>Publish and share your link</b>Your page is live the moment you publish. Share the link wherever your customers are.</span></li>
    </ol>
    <p class="sub" id="ty-dfy" style="display:none;font-size:16px;margin-top:22px"><b>Added Done-For-You Setup?</b> We&#39;ll email you an onboarding form. Your setup starts once we have it.</p>
    <p class="sub" style="font-size:15px;margin-top:26px">Questions? Email <a href="mailto:{E(cfg["email"])}" style="color:var(--aqua-d);font-weight:600">{E(cfg["email"])}</a></p>
  </div>
</section>
<script>
(function(){{
var q=new URLSearchParams(location.search),plan=(q.get("plan")||"").toLowerCase(),oid=q.get("order_id")||q.get("order")||q.get("oid")||"";
var P={{"launch":["Launch",17],"growth":["Growth",97],"ai-pro":["AI Pro",197],"aipro":["AI Pro",197],"scale":["Scale",297],"dfy":["Done-For-You Setup",997]}};
var p=P[plan];if(p){{document.getElementById("ty-sub").textContent="Your "+p[0]+" plan is active. Your receipt and your login invite are on their way by email."}}
if(q.get("dfy")==="1"||plan==="dfy"){{document.getElementById("ty-dfy").style.display="block"}}
if(!p||typeof fbq!=="function")return;
var key="of_purchase_"+(oid||plan);try{{if(localStorage.getItem(key))return;localStorage.setItem(key,"1")}}catch(e){{}}
var v=p[1]+(q.get("dfy")==="1"&&plan!=="dfy"?997:0),opt=oid?{{eventID:oid}}:{{}};
fbq("track","Purchase",{{value:v,currency:"USD",content_name:p[0]}},opt);
}})();
</script>'''
    htm = page(cfg, fonts, path, "Welcome to Oceanic Funnels | You're In",
               "Your Oceanic Funnels account is ready. Here is what happens next.",
               [("Home", "/"), ("Thank you", path)], body, logo)
    htm = htm.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex, nofollow">')
    i = htm.find('<footer class="nf-foot">'); j = htm.find('</footer>', i) + len('</footer>')
    mini = (f'<footer class="nf-foot"><div class="nf-wrap nf-foot-bot"><span>© 2026 {E(cfg["brand"])}. All rights reserved.</span>'
            '<span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a></span></div>'
            '<div class="nf-wordmark" aria-hidden="true">OCEANIC</div></footer>')
    return path, htm[:i] + mini + htm[j:]
