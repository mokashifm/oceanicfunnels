"""Builds oceanicfunnels.com from one source of truth.  Run from src/: python3 build.py  (writes ../site)
Outputs:
  out/1-ghl-body-code.html   -> paste into a Custom JS/HTML element
  out/2-ghl-head-code.html   -> paste into Page Settings > Head Tracking Code
  preview.html               -> artifact preview
"""
import json, html, os, datetime
import pages

CONFIG = {
    "brand": "Oceanic Funnels",
    "product": "Oceanic Funnels OS",
    "domain": "https://oceanicfunnels.com",
    "path": "/",                                  # homepage
    "email": "hello@oceanicfunnels.com",
    # Replace these with your real links (checkout / order form per plan, app login, contact calendar)
    "plan1": "https://checkout.oceanicfunnels.com/oceanic_funnels", "plan2": "https://checkout.oceanicfunnels.com/oceanic_funnels", "plan3": "https://checkout.oceanicfunnels.com/oceanic_funnels",
    "login": "https://app.oceanicfunnels.com", "book_url": "#get-started",
    "updated": datetime.date.today().isoformat(),
}
B, P = CONFIG["brand"], CONFIG["product"]

FAQ = [
    (f"What is {P}?",
     f"{P} is an all-in-one sales funnel, CRM and marketing automation system. It replaces separate tools for funnels and websites, email and SMS, scheduling, website chat, reviews, invoicing and courses with one login and one monthly bill, starting at $67 a month."),
    ("What is a sales funnel?",
     "A sales funnel is the step-by-step path a stranger takes to become a paying customer: an ad or search result, a landing page, an offer, a checkout or booked call, and the email and SMS follow-up in between. Each step filters people out, so fewer reach the end, which is why it is drawn as a funnel."),
    ("What is included in the $67 OS plan?",
     "The full system: unlimited contacts and users, funnels, websites and forms, CRM and sales pipelines, email and SMS automations, calendars and booking, one inbox for every channel, invoices and payments, reviews and courses. You build and run it yourself, with ticket support that replies within 24 hours."),
    ("What is the difference between Growth and Done-For-You?",
     "Growth ($197 a month) sets up the system for you in the first week, installs five core automations and an AI chat agent trained on your business, and adds 24/7 live support, five edit requests a month and a monthly strategy call. Done-For-You ($397 a month) adds a custom sales funnel built from scratch with strategy, copy and design, a full automated backend, a dedicated account manager and ten edits or one new page every month."),
    ("Are contacts really unlimited?",
     "Yes. Every plan includes unlimited contacts and unlimited team users. You never pay more because your list or your team grows."),
    ("How do email, SMS and AI costs work?",
     "Email, SMS and calls are pay-as-you-go, billed from your account wallet at transparent per-use rates. AI agents are pay-as-you-go too: chat replies are billed by the tokens they use and voice calls by the minute, so you only pay for what your agents actually do. If you want unlimited AI replies and voice minutes, add AI Agent Unlimited for $147 a month."),
    ("Can I build more than one funnel?",
     "Yes. Every plan includes unlimited funnels and websites that you build yourself. If you want our team to build an extra funnel for you, it is $297 one time per funnel."),
    ("Is WhatsApp included?",
     "WhatsApp messaging is an add-on for $19 a month. WhatsApp's own per-message fees are billed from your account wallet, and replies inside an open customer conversation are often free."),
    ("How long does setup take?",
     "On OS you can start building the moment you sign up. On Growth, your system is set up within the first week. On Done-For-You, your sales funnel and automated backend go live within 14 days, or your next month is free."),
    ("Can I move my contacts from my current tools?",
     "Yes. You can import contacts from a spreadsheet or your current CRM. On Growth and Done-For-You, our team does the import for you."),
    ("Is there a contract or a guarantee?",
     "OS and Growth are month to month with a 30-day money-back guarantee. Done-For-You has a 3-month minimum because our team builds your funnel and backend up front."),
    ("What is founding member pricing?",
     "The first 50 businesses to join keep the price they signed up at for life, even when our prices go up, as long as their plan stays active."),
]

def schema():
    url = CONFIG["domain"] + CONFIG["path"]
    org_id = CONFIG["domain"] + "/#org"
    def offer(name, price):
        return {"@type": "Offer", "name": name, "price": price, "priceCurrency": "USD",
                "priceSpecification": {"@type": "UnitPriceSpecification", "price": price, "priceCurrency": "USD",
                                       "unitText": "MONTH", "billingDuration": 1, "billingIncrement": 1}}
    graph = [
        {"@type": "Organization", "@id": org_id, "name": B, "url": CONFIG["domain"], "email": CONFIG["email"],
         "knowsAbout": ["Sales funnels", "CRM", "Marketing automation", "AI agents", "Email and SMS marketing"]},
        {"@type": "WebPage", "@id": url + "#page", "url": url,
         "name": f"All-in-One Sales Funnel & CRM Software | {B}",
         "about": {"@id": url + "#software"}, "publisher": {"@id": org_id},
         "dateModified": CONFIG["updated"], "inLanguage": "en"},
        {"@type": "SoftwareApplication", "@id": url + "#software", "name": P,
         "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
         "publisher": {"@id": org_id},
         "description": "All-in-one sales funnel, CRM and marketing automation system with unlimited contacts, users and funnels: funnels and websites, email and SMS automations, AI agents, calendars, one inbox for every channel, invoices and payments, reviews and courses.",
         "offers": [offer("OS", "67"), offer("Growth", "197"), offer("Done-For-You", "397")]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": url}]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap">')

def faq_html():
    return "\n".join(
        f'<details class="nf-q"{" open" if i == 0 else ""}><summary><h3>{html.escape(q)}</h3>'
        f'<span aria-hidden="true">+</span></summary><p>{html.escape(a)}</p></details>'
        for i, (q, a) in enumerate(FAQ))


# "What's included" table: one representative tool per job, starting paid price, checked October 2026
REPLACES = [
    ("CRM and sales pipelines", "HubSpot Sales Hub", 100, "per seat", "https://encharge.io/hubspot-pricing/"),
    ("Sales funnels", "ClickFunnels", 97, "", "https://support.clickfunnels.com/en/articles/12734340-clickfunnels-2-0-pricing"),
    ("Website builder", "Wix", 36, "", "https://www.websitebuilderexpert.com/website-builders/wix/wix-pricing/"),
    ("Online store and checkout", "Shopify", 39, "", "https://www.swell.is/content/shopify-pricing"),
    ("Email marketing", "ActiveCampaign", 49, "", "https://drry.com/guides/activecampaign-pricing"),
    ("Two-way SMS", "SimpleTexting", 39, "", "https://textbolt.com/blog/simpletexting-pricing/"),
    ("Forms and surveys", "Typeform", 39, "", "https://www.jetadmin.io/blog/typeform-pricing/"),
    ("Appointment booking", "Calendly", 12, "per seat", "https://zeeg.me/en/blog/post/calendly-pricing-guide"),
    ("Courses and memberships", "Kajabi", 179, "", "https://revenuegeeks.com/guides/kajabi-pricing"),
    ("Communities", "Skool", 99, "", "https://schoolmaker.com/blog/skool-pricing"),
    ("Call tracking", "CallRail", 55, "", "https://www.capterra.com/p/141829/CallRail/pricing/"),
    ("Review management", "Birdeye", 299, "per location", "https://costbench.com/software/review-management/birdeye"),
    ("Document signing", "DocuSign", 30, "per user", "https://automationatlas.io/answers/docusign-pricing-explained-2026/"),
    ("Social media planner", "Buffer", 6, "per channel", "https://napoleoncat.com/blog/buffer-pricing/"),
    ("Link-in-bio page", "Linktree", 15, "", "https://u2l.ai/blog/linktree-pricing"),
]

def replaces_html():
    tot = sum(r[2] for r in REPLACES)
    rows = "".join(
        f'<tr><th scope="row">{f}</th><td data-l="Replaces"><span class="nf-tool">{t}</span></td>'
        f'<td data-l="Their price" class="num">${c}<small>/mo{(" " + u) if u else ""}</small></td>'
        f'<td data-l="Oceanic Funnels" class="us">✓ Included</td></tr>' for f, t, c, u, _ in REPLACES)
    rows += (f'<tr class="tot"><th scope="row">Overall</th><td data-l="Replaces">{len(REPLACES)} separate tools</td>'
             f'<td data-l="Their price" class="num">${tot:,}<small>/mo</small></td>'
             f'<td data-l="Oceanic Funnels" class="us"><b>$67</b>/month</td></tr>')
    src = " · ".join(f'<a href="{l}" rel="nofollow noopener" target="_blank">{t}</a>' for _, t, _, _, l in REPLACES)
    return rows, str(len(REPLACES)), f"{tot:,}", src

def body():
    src = open("body.src.html").read()
    rep = {"{{BRAND}}": B, "{{BOOK}}": CONFIG["book_url"], "{{EMAIL}}": CONFIG["email"],
           "{{LOGIN}}": CONFIG["login"], "{{PLAN1}}": CONFIG["plan1"], "{{PLAN2}}": CONFIG["plan2"],
           "{{PLAN3}}": CONFIG["plan3"], "{{FAQ}}": faq_html(), "{{FAQ_N}}": str(len(FAQ)),
           "{{UPDATED}}": datetime.date.fromisoformat(CONFIG["updated"]).strftime("%B %Y"), "{{FOOTER}}": pages.footer(CONFIG)}
    r_rows, r_n, r_tot, r_src = replaces_html()
    rep.update({"{{REPL_ROWS}}": r_rows, "{{REPL_N}}": r_n, "{{REPL_TOTAL}}": r_tot, "{{REPL_SRC}}": r_src})
    for k, v in rep.items():
        src = src.replace(k, v)
    assert "{{" not in src, "unreplaced placeholder: " + src[src.index("{{"):src.index("{{")+30]
    return src

os.makedirs("out", exist_ok=True)  # embeddable snippet + preview (gitignored)
head = f'{FONTS}\n<script type="application/ld+json">\n{schema()}\n</script>\n'
page = body()
open("out/1-ghl-body-code.html", "w").write(page)
open("out/2-ghl-head-code.html", "w").write(head)
open("preview.html", "w").write(
    f'<title>{B}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{head}\n'
    f'<style>body{{background:#0E1A1B}}</style>\n{page}')
print("body", len(page)//1024, "KB")

# ---------- standalone static site (Cloudflare Pages / Workers static assets)
import shutil
SITE = "../site"
TITLE = f"All-in-One Sales Funnel & CRM Software | {B}"
DESC = ("Stop fishing for customers. Build the net. Funnels, CRM, email, SMS, AI agents and payments "
        "in one system with unlimited contacts. Plans from $67 a month.")
url = CONFIG["domain"] + "/"
seo_head = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0E1A1B">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{B}">
<meta property="og:title" content="Stop fishing for customers. Build the net.">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{CONFIG['domain']}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Stop fishing for customers. Build the net.">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{CONFIG['domain']}/og-image.png">"""
os.makedirs(SITE, exist_ok=True)
open(f"{SITE}/index.html", "w").write(
    f'<!doctype html>\n<html lang="en">\n<head>\n{seo_head}\n{head}<style>html,body{{margin:0;background:#FFFFFF}}</style>\n</head>\n<body>\n{page}\n</body>\n</html>\n')
today = CONFIG["updated"]
open(f"{SITE}/robots.txt", "w").write(f"""User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {CONFIG['domain']}/sitemap.xml
""")
extra = pages.build_all(CONFIG, FONTS, open("body.src.html").read(), SITE)
def _u(p, pr): return f"  <url><loc>{CONFIG['domain']}{p}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>"
open(f"{SITE}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join([_u("/", "1.0")] + [_u(p, "0.3" if p in ("/privacy/", "/terms/") else "0.8") for p in extra]) + "\n</urlset>\n")

open(f"{SITE}/_headers", "w").write("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()

/*.png
  Cache-Control: public, max-age=31536000, immutable
/*.svg
  Cache-Control: public, max-age=31536000, immutable
/*.ico
  Cache-Control: public, max-age=31536000, immutable
""")

open(f"{SITE}/404.html", "w").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | {B}</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600;700&family=Inter:wght@400&display=swap">
<style>body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#0E1A1B;color:#fff;font-family:Inter,Arial,sans-serif;text-align:center;padding:24px;box-sizing:border-box}}
h1{{font-family:"Inter Tight",Arial,sans-serif;font-size:clamp(40px,8vw,80px);letter-spacing:-.04em;margin:0}}p{{color:#9DB0AD;font-size:18px}}
a{{display:inline-block;margin-top:16px;background:#3DE3C8;color:#0E1A1B;font-family:"Inter Tight",Arial,sans-serif;font-weight:600;text-decoration:none;padding:14px 28px;border-radius:999px}}</style></head>
<body><main><img src="/icon.svg" alt="" width="72" height="72"><h1>This fish got away.</h1><p>The page you're looking for isn't here.</p><a href="/">Back to the homepage</a></main></body></html>
""")
kit = "../brand"
for src, dst in [("svg/oceanic-icon.svg", "icon.svg"), ("png/favicon.ico", "favicon.ico"),
                 ("png/oceanic-icon-app-dark-192.png", "icon-192.png"), ("png/oceanic-icon-app-dark-512.png", "icon-512.png"),
                 ("svg/oceanic-funnels-logo-light.svg", "assets/logo-light.svg"), ("svg/oceanic-funnels-logo-dark.svg", "assets/logo-dark.svg")]:
    shutil.copy(f"{kit}/{src}", f"{SITE}/{dst}")
print("site built")
