"""Builds the extra pages: /privacy/, /terms/, /compare/ and /compare/<competitor>/.
Shares the homepage design: its stylesheet is extracted to /assets/site.css.
"""
import html, json, os, re
import legal
from competitors import COMPETITORS, OF, ROW_LABELS, CHECKED
from industries import INDUSTRIES, GENERIC_FAQ, CATEGORIES
from guides_a import G_A
from guides_b import G_B
from guides_c import G_C
from guides_d import G_D
from guides_e import G_E
GUIDES = G_A + G_B + G_C + G_D + G_E
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
CK = "https://checkout.oceanicfunnels.com/oceanic_funnels"
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
.nf-gcta{background:var(--aqua-l);border-radius:var(--r);padding:26px 28px;margin:8px 0 28px;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between}
.nf-gcta b{font-family:var(--display);font-size:20px;color:var(--ink);display:block}
.nf-gcta span{font-size:15px;color:var(--text)}
.nf-gcard .vs{color:var(--aqua-d)!important}
.nf-gcard .rt{font-size:13px;color:var(--muted)}
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
      <p>Oceanic Funnels OS: the all-in-one sales funnel, CRM and automation system, from $67 a month.</p>
      <a class="nf-btn nf-btn--aqua" href="{CK}">Build my net</a>
    </div>
    <nav class="nf-foot-cols" aria-label="Footer">
      <div><b>Product</b><a href="/#features">Features</a><a href="/#all-in-one">All-in-one</a><a href="/#pricing">Pricing</a><a href="/guides/">Guides</a><a href="/#faq">FAQ</a></div>
      <div><b>Industries</b>{inds}<a href="/industries/">All industries</a></div>
      <div><b>Compare</b>{comp}<a href="/compare/">All comparisons</a></div>
      <div><b>Company</b><span>{E(cfg["email"])}</span><a href="{cfg["login"]}">Log in</a><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a></div>
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
<meta property="og:image" content="{cfg["domain"]}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
{fonts}
<link rel="stylesheet" href="/assets/site.css">
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

def compare_page(cfg, fonts, logo, c):
    n = c["name"]; path = f'/compare/{c["slug"]}/'
    crumbs = [("Home", "/"), ("Compare", "/compare/"), (f"vs {n}", path)]
    rows = "".join(f'<tr><th scope="row">{E(ROW_LABELS[k])}</th><td class="us" data-l="Oceanic Funnels OS">✓ {E(OF[k])}</td><td data-l="{E(n)}">{E(v)}</td></tr>' for k, v in c["rows"].items())
    rows += f'<tr><th scope="row">{E(ROW_LABELS["allinone"])}</th><td class="us" data-l="Oceanic Funnels OS">✓ {E(OF["allinone"])}</td><td data-l="{E(n)}">{E(n)} is {E(art(c["kind"]))}</td></tr>'
    plans = "".join(f'<li><b>{E(a)}</b><span>{E(b)}</span></li>' for a, b in c["plans"])
    srcs = " · ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{E(t)}</a>' for t, u in c["sources"])
    more = "".join(f'<a href="/compare/{o["slug"]}/">vs {E(o["name"])}</a>' for o in COMPETITORS if o["slug"] != c["slug"])
    cheap = f'Oceanic Funnels OS starts at $67 a month with unlimited contacts and users on every plan. {n}\'s published pricing: {c["rows"]["price"][0].lower() + c["rows"]["price"][1:]}.'
    faqs = [
      (f"What is the difference between Oceanic Funnels and {n}?", c["answer"]),
      (f"Is Oceanic Funnels OS cheaper than {n}?", cheap + " Usage like SMS and AI is pay-as-you-go."),
      (f"How do I switch from {n}?", c["switch"]),
      (f"When is {n} the better choice?", c["better"]),
      ("Will you build it for me?", "Yes. On the Growth plan ($197 a month) our team sets up your system in the first week. On the Done-For-You plan ($297 a month plus a one-time $997 build fee) we build your sales funnel and the full automated backend for you."),
    ]
    faq = "\n".join(f'<details class="nf-q"{" open" if i == 0 else ""}><summary><h3>{E(q)}</h3><span aria-hidden="true">+</span></summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(faqs))
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in">
      {crumbs_html(crumbs)}
      <span class="nf-vs">Oceanic Funnels <i>vs</i> {E(n)}</span>
      <h1>{E(c["h1"])}</h1>
      <p class="nf-sub">One system for funnels, CRM, email, SMS, AI agents, booking and payments, with unlimited contacts and users. From $67 a month, or we build it all for you.</p>
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
        <p class="nf-updated">Prices checked {CHECKED} from public sources</p>
      </div>
      <ul class="nf-facts">
        <li><b>Oceanic Funnels</b><span>All-in-one sales funnel, CRM and automation system</span></li>
        <li><b>{E(n)}</b><span>{E(c["kind"][0].upper() + c["kind"][1:])}</span></li>
        <li><b>Starts at</b><span>$67/month vs {E(c["plans"][0][1] if "$0" not in c["plans"][0][1] else c["plans"][1][1])}</span></li>
        <li><b>Contacts</b><span>Unlimited on every Oceanic plan</span></li>
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
    <p class="nf-srcs">{E(n)} details from public pricing pages and reviews, checked {CHECKED}. Plans and prices change, so confirm on {E(n)}'s website. Sources: {srcs}</p>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Pricing at a glance</span>
      <h2>What you pay <span class="g">each month</span></h2>
    </div>
    <div class="nf-two">
      <div class="nf-box ink">
        <h3>Oceanic Funnels OS</h3>
        <ul class="nf-plist"><li><b>OS</b><span>$67/month</span></li><li><b>Growth (set up for you)</b><span>$197/month</span></li><li><b>Done-For-You (we build it)</b><span>$297/month + $997 one-time build</span></li></ul>
        <p style="margin-top:16px">Unlimited contacts, users and funnels on every plan. SMS, email and AI usage is pay-as-you-go.</p>
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
      <h2>Everything {E(n)} does, <span class="g">plus the rest of your stack</span></h2>
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
                      "Compare Oceanic Funnels OS with ClickFunnels, HubSpot, ActiveCampaign, Keap, Kartra, Klaviyo, Zoho, Salesforce and Linktree on features and pricing.", crumbs, body, logo)

def industry_page(cfg, fonts, logo, d):
    path = f"/industries/{d['slug']}/"; n = d["name"]; W = d["who"].split(" like ")[0]
    crumbs = [("Home", "/"), ("Industries", "/industries/"), (n, path)]
    leaks = "".join(f'<li><span class="n">Leak {i+1}</span><b>{E(t)}</b><span>{E(x)}</span></li>' for i, (t, x) in enumerate(d["leaks"]))
    flow = "".join(f'<li><span class="t">{E(t)}</span><span class="d">{i+1}</span><b>{E(h)}</b><p>{E(x)}</p></li>' for i, (t, h, x) in enumerate(d["flow"]))
    autos = "".join(f'<li><b>{E(t)}</b><span>{E(x)}</span></li>' for t, x in d["autos"])
    funnels = "".join(f'<li>{E(f)}</li>' for f in d["funnels"])
    faqs = [(f"How do {d['who']} automate their sales with Oceanic Funnels?", d["answer"])] + d["faqs"] + GENERIC_FAQ
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
      <p class="nf-sub"><b>{E(d["hook"])}.</b> {E(d["sub"])}</p>
      <div class="nf-hero-cta">
        <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">Build my net <span class="ar" aria-hidden="true">→</span></a>
        <a class="nf-btn nf-btn--line" href="#how-it-runs">See how it runs</a>
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
        <li><b>Leads from</b><span>Funnels, ads, social DMs, calls and your website</span></li>
        <li><b>Replies</b><span>Within seconds, by SMS, email, WhatsApp and AI agent</span></li>
        <li><b>Booking</b><span>Calendars with automatic reminders</span></li>
        <li><b>Starts at</b><span>$67/month, unlimited contacts and users</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="nf-band" style="padding-top:0">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Where customers slip away</span>
      <h2>Three leaks in most <span class="g">{E(W)}</span></h2>
    </div>
    <ul class="nf-leaks">{leaks}</ul>
  </div>
</section>

<section class="nf-band nf-dark" id="how-it-runs">
  <div class="nf-wrap">
    <div class="nf-caps">
      <span class="nf-eyebrow">Your net, step by step</span>
      <h2>How the system runs <span class="g">without you</span></h2>
    </div>
    <ol class="nf-run">{flow}</ol>
  </div>
</section>

<section class="nf-band">
  <div class="nf-wrap">
    <div class="nf-center nf-caps">
      <span class="nf-eyebrow">Automations we set up</span>
      <h2>Built for <span class="g">{E(W)}</span></h2>
    </div>
    <ul class="nf-feat">{autos}</ul>
    <div class="nf-two">
      <div class="nf-box"><h3>Funnels you can launch</h3><ul class="nf-chips">{funnels}</ul></div>
      <div class="nf-box ink"><h3>Never lose a lead again</h3><p>Missed call text back, instant replies, AI agents and reminders mean every call, form and DM gets answered, day or night. Unlimited contacts and users on every plan.</p></div>
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
      <div><h2>Stop fishing for customers. Build the net.</h2><p>One system for funnels, CRM, SMS, WhatsApp, AI agents, booking and payments. Or let our team build it for you.</p></div>
      <a class="nf-btn nf-btn--aqua nf-btn--lg" href="{CK}">Build my net <span class="ar" aria-hidden="true">→</span></a>
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
             "offers": {"@type": "Offer", "price": "67", "priceCurrency": "USD", "url": CK}}]
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
    date = datetime_fmt(GUIDE_DATE)
    body = f'''<section class="nf-sub-hero">
  <div class="nf-wrap">
    {{{{HEADER}}}}
    <div class="nf-sub-in">
      {crumbs_html(crumbs)}
      <span class="nf-vs">{E(g["cat"])}</span>
      <h1 style="font-size:clamp(34px,4.6vw,58px)">{E(g["title"])}</h1>
      <p class="nf-sub">{E(g["desc"])}</p>
      <div class="nf-meta"><span>By <b>Oceanic Funnels Team</b></span><span>Updated <time datetime="{GUIDE_DATE}">{date}</time></span><span>{g["read"]} min read</span></div>
    </div>
  </div>
</section>
<section class="nf-band" style="padding-top:56px">
  <div class="nf-wrap nf-doc-wrap">
    <aside class="nf-toc"><b>In this guide</b><ol>{toc}</ol></aside>
    <article class="nf-doc">
      <div class="nf-answer"><b class="k">The short answer</b><p>{E(g["short"])}</p></div>
      {secs}
      <div class="nf-gcta"><div><b>Want this set up for you?</b><span>On Growth and Done-For-You, our team builds it into your system.</span></div><a class="nf-btn nf-btn--ink" href="{CK}">Build my net</a></div>
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
      <div><h2>Stop fishing for customers. Build the net.</h2><p>Funnels, CRM, email, SMS, WhatsApp, AI agents, booking and payments in one system, from $67 a month.</p></div>
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
             "description": g["desc"], "datePublished": GUIDE_DATE, "dateModified": GUIDE_DATE, "inLanguage": "en",
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

def build_all(cfg, fonts, src, site):
    css, logo = extract(src)
    os.makedirs(f"{site}/assets", exist_ok=True)
    open(f"{site}/assets/site.css", "w").write(css + PAGE_CSS)
    out = [legal_page(cfg, fonts, logo, "privacy", "Privacy Policy | Oceanic Funnels", "Privacy Policy",
                      "How Oceanic Funnels collects, uses, shares and protects personal information, including SMS consent, cookies, analytics and your privacy rights.", legal.PRIVACY),
           legal_page(cfg, fonts, logo, "terms", "Terms of Service | Oceanic Funnels", "Terms of Service",
                      "The terms that apply when you use oceanicfunnels.com and Oceanic Funnels OS.", legal.TERMS),
           hub_page(cfg, fonts, logo)]
    out += [compare_page(cfg, fonts, logo, c) for c in COMPETITORS]
    out += [industries_hub(cfg, fonts, logo)] + [industry_page(cfg, fonts, logo, d) for d in INDUSTRIES]
    out += [guides_hub(cfg, fonts, logo)] + [guide_page(cfg, fonts, logo, g) for g in GUIDES]
    for path, htm in out:
        d = site + path
        os.makedirs(d, exist_ok=True)
        open(d + "index.html", "w").write(htm)
    return [p for p, _ in out]
