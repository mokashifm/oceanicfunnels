"""Single source of truth for plans and the feature comparison table."""
from html import escape as E

# name, monthly price, one-line pitch, card bullets (first item is the lead line), CTA, note under button
PLANS = [
    dict(key="launch", name="Launch", price=17,
         pitch="Sell online with funnels, websites and a store.",
         bullets=["Build and sell online:", "Unlimited sales funnels", "Unlimited websites", "E-commerce store"],
         cta="Start with Launch", after="Cancel anytime"),
    dict(key="growth", name="Growth", price=97,
         pitch="The full system to catch, follow up and close, without AI.",
         bullets=["Everything in Launch, plus:", "CRM, contacts and sales pipelines", "Phone system and missed call text back",
                  "SMS and email marketing", "Calendars and appointments", "Automation workflows",
                  "Invoices, payments and subscriptions", "Courses, communities and client portal",
                  "Reviews, social planner and ad manager", "Dashboards, reporting and integrations"],
         cta="Get Growth", after="30-day money-back guarantee"),
    dict(key="aipro", name="AI Pro", price=197, pop=True,
         pitch="Every feature, including all AI.",
         bullets=["Everything in Growth, plus:", "Conversation AI for chat, SMS and social", "Voice AI that answers your calls",
                  "Content AI and Reviews AI", "Workflow AI and Website and Funnel AI", "AI Studio and Agent Studio",
                  "AI Knowledge Base and Ask AI"],
         cta="Get AI Pro", after="30-day money-back guarantee"),
    dict(key="scale", name="Scale", price=297,
         pitch="Everything in AI Pro, plus people to help you grow.",
         bullets=["Everything in AI Pro, plus:", "A dedicated account manager", "A builder who helps you grow and scale your business"],
         cta="Scale with us", after="Cancel anytime"),
]
PLAN_BY = {p["key"]: p for p in PLANS}

AI = ["Conversation AI", "Voice AI", "Content AI", "Reviews AI", "Workflow AI", "Website and Funnel AI",
      "AI Studio", "Agent Studio", "AI Knowledge Base", "Ask AI"]
LAUNCH = {"Funnel Builder", "Website Builder", "E-commerce Store"}
TEAM = ["Dedicated Account Manager", "Builder to Help You Grow and Scale"]

FEATURES = [
    ("CRM and communication", ["Customer Relationship Manager (CRM)", "Contact Management", "Sales Pipelines and Opportunities",
                               "Phone System", "Missed Call Text Back", "SMS Marketing", "Email Builder and Marketing",
                               "Calendar and Appointments", "Automation Workflows"]),
    ("Funnels and websites", ["Funnel Builder", "Website Builder", "Forms", "Surveys", "Quizzes", "Chat Widget",
                              "QR Code Builder", "Blog Builder", "WordPress Hosting"]),
    ("Marketing and reputation", ["Social Media Planner", "Ad Manager", "Reputation Management", "Review Requests",
                                  "Business Listings", "Video Testimonials", "Affiliate Manager"]),
    ("Payments and commerce", ["Invoices and Estimates", "Documents and Contracts", "Payment Links", "Products and Payments",
                               "Subscriptions", "E-commerce Store", "Gift Cards"]),
    ("Courses, community and services", ["Courses and Memberships", "Communities", "Certificates", "Client Portal",
                                         "Services and Rentals", "Events and Webinars"]),
    ("AI", AI),
    ("Reporting and integrations", ["Dashboards and Reporting", "Ad Tracking and Attribution", "Integrations", "API and Webhooks"]),
    ("Your team", TEAM),
]


def included(feature, key):
    if feature in TEAM:
        return key == "scale"
    if key == "launch":
        return feature in LAUNCH
    if key == "growth":
        return feature not in AI
    return True


def n_features():
    return sum(len(f) for _, f in FEATURES)


def cards_html(links):
    out = []
    for p in PLANS:
        pop = p.get("pop")
        lis = "".join(f'<li class="lead">{E(b)}</li>' if i == 0 else f"<li>{E(b)}</li>" for i, b in enumerate(p["bullets"]))
        out.append(
            f'<article class="nf-price{" nf-price--pop" if pop else ""}">'
            + ('<span class="pop">MOST POPULAR</span>' if pop else "")
            + f'<span class="plan">{E(p["name"])}</span>'
            f'<div class="amt"><span class="v">${p["price"]}</span> <small>/month</small></div>'
            f'<p class="for">{E(p["pitch"])}</p><ul>{lis}</ul>'
            f'<a class="nf-btn {"nf-btn--aqua" if pop else "nf-btn--ink"}" href="{links[p["key"]]}">{E(p["cta"])}</a>'
            f'<p class="after">{E(p["after"])}</p></article>')
    return "".join(out)


def table_html():
    head = "".join(f'<th scope="col"><b>{E(p["name"])}</b><small>${p["price"]}/mo</small></th>' for p in PLANS)
    body = []
    for group, feats in FEATURES:
        labels = "".join(f'<td aria-hidden="true">{E(p["name"])}</td>' for p in PLANS)
        body.append(f'<tr class="grp"><th scope="rowgroup">{E(group)}</th>{labels}</tr>')
        for f in feats:
            cells = "".join(
                '<td><span class="yes" role="img" aria-label="Included">✓</span></td>' if included(f, p["key"])
                else '<td><span class="no" role="img" aria-label="Not included">✕</span></td>' for p in PLANS)
            body.append(f'<tr><th scope="row">{E(f)}</th>{cells}</tr>')
    cols = '<colgroup><col class="cf">' + '<col class="cp">' * len(PLANS) + '</colgroup>'
    return (f'<table class="nf-ftable"><caption class="nf-sr">Features included in each plan</caption>{cols}'
            f'<thead><tr><th scope="col" class="f">Feature</th>{head}</tr></thead><tbody>{"".join(body)}</tbody></table>')


def summary_text():
    """Plain-text plan summary used in FAQs, llms.txt and legal."""
    return ("Launch $17/month (unlimited sales funnels, websites and an e-commerce store), "
            "Growth $97/month (every feature except AI), AI Pro $197/month (every feature, including all AI), "
            "and Scale $297/month (everything in AI Pro plus a dedicated account manager and a builder to help you grow and scale)")
