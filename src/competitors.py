"""Comparison page data. Every competitor figure here was checked against a public source
(listed in `sources`) in October 2026. Only claims we could verify are included.
Re-check prices every quarter: they change often.
"""

CHECKED = "October 30, 2026"

# Oceanic Funnels OS values, reused on every page
OF = {
    "price": "From $67/month, one bill",
    "contacts": "Unlimited on every plan",
    "users": "Unlimited on every plan",
    "funnels": "Unlimited funnels and websites",
    "crm": "CRM and sales pipelines built in",
    "sms": "Built-in SMS and two-way texting",
    "email": "Email campaigns and automations built in",
    "booking": "Calendars, booking and reminders built in",
    "courses": "Courses, memberships and communities",
    "ai": "AI chat and voice agents built in",
    "setup": "Done for you on Growth and Done-For-You plans",
    "fee": "No platform fee on your sales",
    "onboard": "No onboarding fee",
    "store": "Online store, products and checkout built in",
    "support": "Ticket support on OS, 24/7 live support on Growth, a team that builds it on Done-For-You",
    "traffic": "No visitor limits on your funnels",
    "allinone": "Funnels, CRM, email, SMS, booking, payments and reviews in one system",
}

ROW_LABELS = {
    "price": "Starting price",
    "contacts": "Contacts",
    "users": "Team users",
    "funnels": "Funnels and websites",
    "crm": "CRM and pipelines",
    "sms": "SMS and two-way texting",
    "email": "Email marketing",
    "booking": "Appointment booking",
    "courses": "Courses and memberships",
    "ai": "AI agents",
    "setup": "Done-for-you setup",
    "fee": "Fees on your sales",
    "onboard": "Onboarding fee",
    "store": "Online store and checkout",
    "support": "Help from a real team",
    "traffic": "Visitor limits",
    "allinone": "What's included",
}

COMPETITORS = [{'slug': 'skool',
  'name': 'Skool',
  'kind': 'community and course platform',
  'h1': 'The Skool alternative with your community, CRM, email and SMS in one place',
  'answer': "Skool's Hobby plan is $9 a month with a 10% transaction fee, and its Pro plan is $99 a month with a 2.9% transaction fee. "
            "Skool's pricing page lists community, courses, videos and live calls, but not email marketing, a website or funnels. Oceanic "
            'Funnels OS includes paid communities, courses and memberships plus a CRM, email, SMS, funnels and AI agents, from $67 a month '
            'with no platform fee on your sales.',
  'rows': {'price': '$9/month (Hobby) or $99/month (Pro)',
           'fee': '10% (Hobby) or 2.9% (Pro) per transaction',
           'courses': 'Unlimited courses, videos and live calls',
           'email': "Not listed on Skool's pricing page",
           'funnels': "Not listed on Skool's pricing page"},
  'plans': [('Hobby', '$9/month, 10% transaction fee'), ('Pro', '$99/month, 2.9% transaction fee')],
  'better': "You only need a simple community with courses, and you want new members to find you through Skool's own discovery page.",
  'switch': 'Export your member list, recreate your community, courses and pricing in Oceanic Funnels OS (or let our team do it on '
            'Done-For-You), then invite your members and turn on email and SMS follow-up.',
  'sources': [('Skool pricing (skool.com)', 'https://www.skool.com/pricing')]},
 {'slug': 'clickfunnels',
  'name': 'ClickFunnels',
  'kind': 'funnel builder',
  'h1': 'The ClickFunnels alternative with CRM, SMS and AI built in',
  'answer': "ClickFunnels' Launch plan is $97 a month ($81 billed yearly) for 10,000 contacts and 2 team members. Oceanic Funnels OS "
            'includes unlimited funnels too, plus a full CRM, built-in two-way SMS, AI agents, booking and payments, with unlimited '
            'contacts and users from $67 a month.',
  'rows': {'price': 'From $97/month (Launch), $81/month billed yearly',
           'contacts': '10,000 on Launch, 75,000 on Scale, 150,000 on Optimize',
           'users': '2 team members on Launch, 5 on Scale',
           'funnels': 'Unlimited funnels on every plan'},
  'plans': [('Launch', '$97/month ($81 yearly), 10K contacts, 2 team members'),
            ('Scale', '$197/month ($164 yearly), 75K contacts, 5 team members'),
            ('Optimize', '$297/month ($248 yearly), 150K contacts, 10 team members'),
            ('Dominate', '$5,997/year, annual only, 400K contacts')],
  'better': "You only need funnel pages, and you're happy inside the ClickFunnels community and training.",
  'switch': 'Rebuild your funnels in Oceanic Funnels OS (or let our team do it on the Done-For-You plan), import your contacts from a CSV '
            'export, and turn on the built-in SMS and follow-up automations you were paying other tools for.',
  'sources': [('ClickFunnels pricing (clickfunnels.com)', 'https://www.clickfunnels.com/pricing')]},
 {'slug': 'kajabi',
  'name': 'Kajabi',
  'kind': 'course and creator platform',
  'h1': 'The Kajabi alternative with unlimited contacts, CRM and SMS',
  'answer': "Kajabi's Basic plan is $179 a month ($143 billed yearly) for 5 products, 2,500 contacts and 2 admin users, and it charges an "
            'extra 2% when you use a third-party payment provider. Oceanic Funnels OS includes courses, memberships and communities too, '
            'plus a full CRM, two-way SMS, AI agents, booking and an online store, with unlimited contacts and users from $67 a month.',
  'rows': {'price': 'From $179/month (Basic), $143/month billed yearly',
           'contacts': '2,500 on Basic, 25,000 on Growth, 100,000 on Pro',
           'users': '2 admin users on Basic, 11 on Growth, 26 on Pro',
           'courses': '5 products on Basic, 50 on Growth',
           'fee': 'Kajabi Payments 2.9% + $0.30 on Basic (US), or 2% extra with a third-party provider'},
  'plans': [('Basic', '$179/month ($143 yearly), 5 products, 2,500 contacts'),
            ('Growth', '$249/month ($199 yearly), 50 products, 25,000 contacts'),
            ('Pro', '$499/month ($399 yearly), unlimited products, 100,000 contacts')],
  'better': "You're a creator who only sells courses and digital products, and you like Kajabi's creator-focused templates.",
  'switch': 'Export your contacts and course content, rebuild your courses, memberships and sales pages in Oceanic Funnels OS (or let our '
            'team do it on Done-For-You), then turn on SMS follow-up and booking.',
  'sources': [('Kajabi pricing (kajabi.com)', 'https://www.kajabi.com/pricing')]},
 {'slug': 'funnelish',
  'name': 'Funnelish',
  'kind': 'ecommerce funnel builder',
  'h1': 'The Funnelish alternative with a full CRM and no visitor caps',
  'answer': 'Funnelish is a checkout and funnel builder for online stores, with a Basic plan at $49 a month for up to 20,000 visitors, 20 '
            'funnels, 1 store and 2 team members. Oceanic Funnels OS gives you unlimited funnels plus a CRM, email, SMS, AI agents, '
            'booking and courses, with unlimited contacts and users from $67 a month.',
  'rows': {'price': 'From $49/month (Basic), $41/month billed yearly',
           'traffic': 'Up to 20,000 visitors a month on Basic',
           'funnels': '20 ecommerce funnels on Basic',
           'store': '1 store on Basic',
           'users': '2 team members on Basic',
           'fee': '0% extra processing fees'},
  'plans': [('Basic', '$49/month ($41 yearly), 20,000 visitors'),
            ('Pro', '$99/month ($83 yearly), 100,000 visitors'),
            ('Advanced', '$249/month ($208 yearly), unlimited visitors'),
            ('Enterprise', 'Custom pricing')],
  'better': 'You only sell physical products through checkout funnels and already run your email and SMS in other tools.',
  'switch': 'Rebuild your checkout funnels and products in Oceanic Funnels OS, import your customer list, and turn on built-in email and '
            'SMS follow-up so you can drop the extra tools.',
  'sources': [('Funnelish pricing (funnelish.com)', 'https://funnelish.com/pricing')]},
 {'slug': 'shopify',
  'name': 'Shopify',
  'kind': 'ecommerce platform',
  'h1': 'The Shopify alternative with funnels, CRM, SMS and booking built in',
  'answer': "Shopify's Basic plan is $39 a month, and it charges a 2% fee on Basic when you use a third-party payment provider. Oceanic "
            'Funnels OS includes an online store and checkout, plus sales funnels, a CRM, email, SMS, AI agents, booking and courses, from '
            '$67 a month with no platform fee on your sales.',
  'rows': {'price': 'From $39/month (Basic), $29/month billed yearly',
           'fee': '2% on Basic with a third-party payment provider (1% Grow, 0.6% Advanced)',
           'users': 'No additional staff accounts on Basic, 5 on Grow',
           'store': "Yes, Shopify's specialty"},
  'plans': [('Basic', '$39/month ($29 yearly)'),
            ('Grow', '$105/month ($79 yearly)'),
            ('Advanced', '$399/month ($299 yearly)'),
            ('Plus', 'Starts at $2,300/month')],
  'better': "You run a large online store with a big catalog and depend on Shopify's theme and app ecosystem.",
  'switch': 'Export your products and customers from Shopify, import them into Oceanic Funnels OS, and build your store and sales funnels '
            'in one place. On Done-For-You, our team builds it for you.',
  'sources': [('Shopify pricing (shopify.com)', 'https://www.shopify.com/pricing')]},
 {'slug': 'hubspot',
  'name': 'HubSpot',
  'kind': 'CRM and marketing suite',
  'h1': 'The HubSpot alternative without per-seat and per-contact pricing',
  'answer': "HubSpot prices by seat and by marketing contact. Texting needs Marketing Hub Professional or Enterprise plus HubSpot's "
            'Marketing SMS add-on, and Professional is $890 a month ($800 billed yearly) with a required $3,000 onboarding fee. Oceanic '
            'Funnels OS includes the CRM, email, SMS, funnels and booking with unlimited contacts and users from $67 a month.',
  'rows': {'price': 'Marketing Hub Starter $20/seat/month (monthly billing)',
           'contacts': '1,000 marketing contacts on Starter, 2,000 on Professional',
           'users': 'Priced per seat (3 Core Seats on Professional)',
           'sms': 'Needs Marketing Hub Professional or Enterprise plus the Marketing SMS add-on',
           'onboard': '$3,000 on Marketing Hub Professional, $7,000 on Enterprise',
           'crm': 'CRM included'},
  'plans': [('Marketing Hub Starter', '$20/seat/month'),
            ('Marketing Hub Professional', '$890/month ($800 yearly), 3 seats, 2,000 contacts, plus $3,000 onboarding'),
            ('Marketing Hub Enterprise', '$3,600/month, 5 seats, 10,000 contacts, plus $7,000 onboarding'),
            ('Sales Hub Professional', '$100/seat/month ($90 yearly), plus $1,500 onboarding')],
  'better': "You're a larger company with a dedicated marketing team, you need HubSpot's advanced reporting and enterprise permissions, "
            'and your budget allows for per-seat and per-contact growth.',
  'switch': 'Export your contacts and deals from HubSpot, import them into Oceanic Funnels OS, and rebuild your key emails, forms and '
            'pipelines. On Growth and Done-For-You, our team does the setup for you.',
  'sources': [('Marketing Hub pricing (hubspot.com)', 'https://www.hubspot.com/pricing/marketing'),
              ('Sales Hub pricing (hubspot.com)', 'https://www.hubspot.com/pricing/sales'),
              ('SMS requirements (HubSpot Knowledge Base)', 'https://knowledge.hubspot.com/sms/set-up-sms-messaging')]},
 {'slug': 'activecampaign',
  'name': 'ActiveCampaign',
  'kind': 'email marketing and automation tool',
  'h1': 'The ActiveCampaign alternative with funnels, SMS and booking included',
  'answer': 'ActiveCampaign is an email automation tool priced by contact count, starting at $15 a month billed yearly for 1,000 contacts '
            'with 1 user seat. Oceanic Funnels OS includes email automation plus funnels, built-in SMS, booking, payments and a CRM, with '
            'unlimited contacts and users from $67 a month.',
  'rows': {'price': 'From $15/month billed yearly, for 1,000 contacts',
           'contacts': 'Price rises with your contact count',
           'users': '1 user seat on Starter and Plus, 3 on Pro, 5 on Enterprise',
           'email': '10,000 email sends a month on Starter (1,000 contacts)'},
  'plans': [('Starter', '$15/month billed yearly, 1,000 contacts, 1 seat'),
            ('Plus', '$49/month billed yearly, 1,000 contacts, 1 seat'),
            ('Pro', '$79/month billed yearly, 1,000 contacts, 3 seats'),
            ('Enterprise', '$145/month billed yearly, 1,000 contacts, 5 seats')],
  'better': "Email is your only channel, you don't need funnels, booking or payments in the same tool, and your list is small enough that "
            'per-contact pricing stays low.',
  'switch': 'Export your contacts and tags, import them into Oceanic Funnels OS, and rebuild your main automations. Then add the funnels, '
            "SMS follow-up and booking that ActiveCampaign doesn't include.",
  'sources': [('ActiveCampaign pricing (activecampaign.com)', 'https://www.activecampaign.com/pricing')]},
 {'slug': 'keap',
  'name': 'Keap',
  'kind': 'CRM and automation platform',
  'h1': 'The Keap alternative at a fraction of the price',
  'answer': 'Keap starts at $299 a month, or $2,988 billed yearly, with 2 users included and extra users at $39 a month each. '
            'Implementation is required and priced separately, and annual contracts carry a $299 early termination fee. Oceanic Funnels OS '
            'includes CRM, automations, SMS, funnels, booking and payments with unlimited contacts and users from $67 a month.',
  'rows': {'price': 'From $299/month, or $2,988 billed yearly',
           'contacts': 'Price depends on your contact count',
           'users': '2 users included, extra users $39/month each',
           'setup': 'Implementation required, priced separately'},
  'plans': [('Starting plan', '$299/month or $2,988/year, 2 users'), ('More contacts', "Priced by contact count on Keap's pricing page")],
  'better': "You've been on Keap for years with complex automations you don't want to rebuild, and the price difference doesn't matter to "
            'your business.',
  'switch': 'Export your contacts, tags and products from Keap, import them into Oceanic Funnels OS, and rebuild your key campaigns. On '
            'Done-For-You, our team rebuilds your funnel and backend for you.',
  'sources': [('Keap pricing (keap.com)', 'https://keap.com/pricing')]},
 {'slug': 'klaviyo',
  'name': 'Klaviyo',
  'kind': 'email and SMS tool for online stores',
  'h1': 'The Klaviyo alternative for service businesses',
  'answer': 'Klaviyo is an email and SMS tool billed on active profiles. Its free plan covers up to 250 active profiles and 500 email '
            'sends a month, and paid plans are priced by profile count. Oceanic Funnels OS includes email and SMS too, plus funnels, a CRM '
            'pipeline, booking and invoicing, with unlimited contacts from $67 a month.',
  'rows': {'price': 'Free up to 250 active profiles; paid plans priced by profile count',
           'contacts': 'Billed on active profiles',
           'sms': 'Free plan includes $5 of mobile messages a month'},
  'plans': [('Free', 'Up to 250 active profiles, 500 email sends/month'),
            ('Paid', "Priced by number of profiles on Klaviyo's pricing page")],
  'better': 'You run a Shopify or ecommerce store and need deep product-feed, browse-abandonment and store-revenue reporting.',
  'switch': 'Export your profiles and lists, import them into Oceanic Funnels OS, and rebuild your key flows. Add the funnels, booking and '
            'pipeline tools a service business needs.',
  'sources': [('Klaviyo pricing (klaviyo.com)', 'https://www.klaviyo.com/pricing')]},
 {'slug': 'zoho',
  'name': 'Zoho CRM',
  'kind': 'CRM',
  'h1': 'The Zoho CRM alternative with funnels and messaging in one place',
  'answer': 'Zoho CRM is free for up to 3 users, and its paid editions are priced per user. Oceanic Funnels OS puts the CRM, funnels, '
            'email, SMS, booking and payments in one system with unlimited users from $67 a month.',
  'rows': {'price': 'Free for up to 3 users; paid editions priced per user', 'users': 'Priced per user', 'crm': 'CRM'},
  'plans': [('Free', 'Up to 3 users'), ('Standard, Professional, Enterprise, Ultimate', "Priced per user on Zoho's pricing page")],
  'better': 'You already use several Zoho apps like Books and Desk, and you want your CRM inside that ecosystem.',
  'switch': 'Export your leads, contacts and deals from Zoho, import them into Oceanic Funnels OS, and rebuild your pipeline stages. Your '
            'funnels and messaging then live in the same place.',
  'sources': [('Zoho CRM pricing (zoho.com)', 'https://www.zoho.com/crm/zohocrm-pricing.html')]},
 {'slug': 'salesforce',
  'name': 'Salesforce',
  'kind': 'enterprise CRM',
  'h1': 'The Salesforce alternative built for small businesses',
  'answer': 'Salesforce is priced per user: Starter Suite is $25 a month per user, billed monthly or yearly, and Pro Suite is $100 per '
            'user, billed yearly with a contract. Oceanic Funnels OS includes the CRM, funnels, email, SMS, AI agents and booking with '
            'unlimited users from $67 a month.',
  'rows': {'price': 'Starter Suite from $25/user/month',
           'users': 'Priced per user (Pro Suite $100/user/month, billed yearly)',
           'crm': 'CRM'},
  'plans': [('Starter Suite', '$25/user/month, billed monthly or yearly'),
            ('Pro Suite', '$100/user/month, billed yearly, contract required'),
            ('Sales Cloud Core', '$195/user/month, billed yearly'),
            ('Sales Cloud Advanced', '$395/user/month, billed yearly')],
  'better': "You're a large company with complex sales processes, many departments and an in-house admin or Salesforce partner.",
  'switch': 'Export your accounts, contacts and opportunities, import them into Oceanic Funnels OS, and set up your pipeline. Most small '
            'teams are running in a week, or our team sets it up for you.',
  'sources': [('Small business pricing (salesforce.com)', 'https://www.salesforce.com/small-business/pricing/'),
              ('Sales Cloud pricing (salesforce.com)', 'https://www.salesforce.com/products/sales-cloud-pricing/')]},
 {'slug': 'linktree',
  'name': 'Linktree',
  'kind': 'link-in-bio tool',
  'h1': 'The Linktree alternative that turns clicks into customers',
  'answer': 'Linktree is a link-in-bio page with a free plan and paid plans from $9 a month ($7 billed yearly). Its pricing page lists 0% '
            'fees on sales from the Pro plan up. Oceanic Funnels OS gives you full funnels and websites, plus the CRM, email, SMS and '
            'booking to follow up with every visitor, from $67 a month.',
  'rows': {'price': 'Free; paid plans from $9/month ($7 billed yearly)',
           'fee': '0% fees on sales on Pro and Premium',
           'funnels': 'Link-in-bio page'},
  'plans': [('Free', '$0'),
            ('Starter', '$9/month ($7 yearly)'),
            ('Pro', '$17/month ($14 yearly), 0% fees on sales'),
            ('Premium', '$35/month ($30 yearly)')],
  'better': "You only need a simple page of links for your social profiles and don't plan to follow up with the people who click.",
  'switch': 'Build a link-in-bio page or full funnel in Oceanic Funnels OS, point your social bios to it, and every visitor who opts in '
            'lands in your CRM with automatic follow-up.',
  'sources': [('Linktree pricing (linktr.ee)', 'https://linktr.ee/s/pricing')]}]
