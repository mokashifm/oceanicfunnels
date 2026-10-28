"""Researched visual carousels, batch 1: 60 posts (Oct 28 - Nov 26, 2026), Facebook + Instagram.
Markup in slide text: [[x]] = aqua emphasis, {{x}} = coral emphasis.
Every figure is from a named source, printed on the slide.

SOURCES (verified Oct 28, 2026)
BL26  BrightLocal Local Consumer Review Survey 2026 (published Feb 11 2026; 1,002 US adults)
BLAI  BrightLocal LCRS 2026 AI trust analysis (published Mar 10 2026; 455 AI users of 1,002 US adults)
QB26  QuickBooks/Intuit 2026 AI Impact Report (May 12 2026; 34,000+ SMB owners, US/CA/UK/AU)
GS26  Goldman Sachs 10,000 Small Businesses survey (Mar 17 2026; 1,256 US owners)
HBR   Harvard Business Review, "The Short Life of Online Sales Leads" (2011; 2,241 US companies audited; 1.25M leads)
TEL   TelePA phone study (142 UK small businesses)
GMY   Gmail and Yahoo bulk sender requirements (Feb 2024, unsubscribe Jun 2024) via Customer.io
LTR   Later, Instagram hashtags (Apr 2026): 5-hashtag cap from Dec 2025
SI26  Socialinsider Instagram benchmarks 2026 (67.5M posts)
SP26  SocialPilot LinkedIn algorithm 2026 (Sep 2026)
SPR   Sprout Social best times to post 2026 (~2B engagements, 307K profiles)
WS26  Whitespark guide to Google AI Mode for local businesses (May 2026)
GRP   Google review policy (incentives and selective asking prohibited)
"""

BL = "Source: BrightLocal Local Consumer Review Survey 2026 (1,002 US adults)"
QB = "Source: QuickBooks 2026 AI Impact Report (34,000+ owners, US/UK/CA/AU)"
GS = "Source: Goldman Sachs 10,000 Small Businesses survey, March 2026 (1,256 US owners)"
HBR = "Source: Harvard Business Review, The Short Life of Online Sales Leads"

def cta(h, note, kicker="Save this post"):
    return dict(t="cta", k=kicker, h=h, note=note)

POSTS = [
# 1 (Oct 28 AM) AI search
dict(cap="Almost half of US consumers now ask AI tools like ChatGPT which local business to use. A year earlier it was 6%.\n\nSwipe for which tools they use, why reviews still decide the sale, and 5 ways to get recommended.\n\nSave this so you can work through the checklist.",
 tags="#aisearch #chatgpt #localbusiness #localseo",
 slides=[
  dict(t="cover_stat", k="AI search", big="45%", h="of US consumers now use AI to find [[local businesses.]]", bars=[("A year earlier",6,"6%"),("2026",45,"45%")], src="Source: BrightLocal, 2026"),
  dict(t="bars", k="Which AI tools", h="Where they ask [[for recommendations]]", lead="Share of US consumers who used each tool to find a local business:", items=[("ChatGPT",31,"31%"),("Google AI Mode",23,"23%")], note="If these tools can't find clear information about your business, they can't recommend you.", src=BL),
  dict(t="donut", k="Reviews still decide", h="AI makes the shortlist. {{Reviews win the call.}}", pct=97, note="of people who use AI for local recommendations sometimes double-check its picks against real reviews.", src=BL),
  dict(t="chat", k="What your customer sees", h="They ask AI. AI [[names a few businesses.]]", msgs=[("u","Best med spa near me that's open Saturday and has good reviews?"),("ai","Here are a few options nearby:\n1. Clinic A · 4.9 ★ (212 reviews) · Open Sat 9–5\n2. Clinic B · 4.8 ★ (164 reviews) · Open Sat 10–4\n3. Clinic C · 4.7 ★ (98 reviews) · Online booking")], after="Is your business on that list?", src="Illustration. Business names are examples."),
  dict(t="list", k="How to show up", h="5 ways to get [[recommended by AI]]", items=[("Match your name, address, phone and hours everywhere","Website, Google Business Profile and listings"),("Answer real customer questions on your website","Plain-language FAQs AI can quote"),("Get fresh reviews every month","And reply to them, good and bad"),("Add recent, real photos","Website, profile and social"),("Get mentioned on other local sites","Associations, sponsorships, local press")], src="Based on Whitespark's guide to Google AI Mode for local businesses (2026)"),
  cta("Get found by AI. [[Answer every lead it sends you.]]","Oceanic Funnels keeps your reviews, listings and website working together, and replies to every new lead in seconds, 24/7."),
 ]),
# 2 (Oct 28 PM) about us: while you sleep
dict(cap="Your business shouldn't stop selling when you close.\n\nHere's an example night with Oceanic Funnels OS running in the background: messages answered, missed calls texted back, invoices paid and reminders sent, while you sleep.",
 tags="#automation #smallbusiness #aiagents #marketingautomation",
 slides=[
  dict(t="cover_text", k="While you sleep", h="Your business keeps working [[while you sleep.]]", sub="An example night with automations and AI agents running in the background.", swipe=True),
  dict(t="timeline", k="Evening", h="9 PM to midnight", items=[("9:14 PM","Instagram DM","Someone asks what lip filler costs. The AI agent answers in seconds and books a consultation."),("10:02 PM","Missed call","A text goes back instantly. The caller books online."),("11:38 PM","Abandoned checkout","A reminder email and text bring the visitor back to finish.")]),
  dict(t="timeline", k="Overnight", h="Midnight to morning", items=[("1:47 AM","Invoice paid","A customer pays from the text-to-pay link you never had to chase."),("6:00 AM","Reminders sent","Everyone booked today gets a reminder with a reschedule link."),("7:30 AM","Old leads woken up","A reactivation campaign goes out. Replies are waiting in your inbox.")]),
  cta("Stop fishing for customers. [[Build the net.]]","One system for funnels, CRM, AI agents, booking, reminders, reviews and payments. From $67 a month, or built for you.", kicker="Oceanic Funnels"),
 ]),
# 3 (Oct 29 AM) speed to lead HBR
dict(cap="Harvard Business Review studied 1.25 million sales leads. Companies that contacted a lead within an hour were nearly 7 times as likely to qualify it as companies that waited just one hour longer.\n\nSwipe for the numbers and how to never be slow again.",
 tags="#speedtolead #sales #leadgeneration #salestips",
 slides=[
  dict(t="cover_stat", k="Speed to lead", big="7×", h="more likely to qualify a lead if you reply [[within an hour.]]", sub="Compared with waiting one hour longer.", src="Source: Harvard Business Review"),
  dict(t="bars", k="It gets worse", h="Wait a day and the odds [[collapse]]", lead="How much more likely firms replying within an hour were to qualify a lead:", items=[("vs. waiting 1 more hour",7,"~7×"),("vs. waiting 24 hours or more",60,"60×+")], max=60, note="Based on 1.25 million leads across 42 US companies.", src=HBR),
  dict(t="list", k="Fix it", h="Never be slow [[again]]", items=[("Reply automatically in seconds","A text and email the moment a lead comes in"),("Ask one simple question","So the conversation keeps going"),("Send a booking link","Let them pick a time without waiting for you"),("Alert your team","So a person follows up the same day")]),
  cta("Be the first reply, [[every time.]]","Oceanic Funnels answers every new lead in seconds by text, email or AI agent, day and night."),
 ]),
# 4 (Oct 29 PM) HBR audit
dict(cap="When Harvard Business Review sent test leads to 2,241 US companies, 23% never replied at all. The average reply took 42 hours.\n\nYour competitors might be slow. That's your opportunity.",
 tags="#sales #customerservice #leadgeneration #smallbusiness",
 slides=[
  dict(t="cover_stat", k="Reality check", big="23%", h="of companies [[never replied]] to a new lead at all.", sub="Out of 2,241 US companies sent a test enquiry.", src="Source: Harvard Business Review"),
  dict(t="bars", k="Who replied, and when", h="How fast companies [[actually replied]]", items=[("Within 1 hour",37,"37%"),("1 to 24 hours",16,"16%"),("More than 24 hours",24,"24%"),("Never",23,"23%")], max=40, src=HBR),
  dict(t="cover_text", k="The average", h="[[42 hours]] to reply, for the companies that did.", sub="Two days is long enough for a customer to book someone else."),
  cta("Reply in seconds. [[Win the deals they miss.]]","Automatic replies and follow-up from Oceanic Funnels, so no lead waits, even at weekends."),
 ]),
# 5 (Oct 30 AM) reviews recency
dict(cap="Old reviews don't sell. In BrightLocal's 2026 survey, 74% of consumers only care about reviews from the last three months.\n\nIf your newest review is from spring, many customers will treat you as if you had none.",
 tags="#googlereviews #reviews #reputation #localbusiness",
 slides=[
  dict(t="cover_stat", k="Reviews", big="74%", h="of consumers only care about reviews from the [[last 3 months.]]", src="Source: BrightLocal, 2026"),
  dict(t="bars", k="How recent is recent?", h="What consumers count as [[a recent review]]", items=[("Only the last week",18,"18%"),("The last two weeks",32,"32%"),("The last three months",74,"74%")], max=80, note="The two-week group grew from 20% in 2025 to 32% in 2026.", src=BL),
  dict(t="list", k="Stay fresh", h="Keep reviews coming [[every week]]", items=[("Ask after every job or visit","Automatically, by text or email"),("Time it to the result","When the customer is happiest"),("Use one tap","A direct link to your review page"),("Reply to every review","So new customers see you care")]),
  cta("Fresh reviews, [[on autopilot.]]","Oceanic Funnels sends a review request after every visit and lets you reply to reviews from one place."),
 ]),
# 6 (Oct 30 PM) about us: 15 apps
dict(cap="Most businesses pay for a stack of separate tools that don't talk to each other.\n\nWe added up the list prices of 15 common ones: $1,094 a month. Oceanic Funnels OS replaces them from $67 a month, with unlimited contacts and users.",
 tags="#allinone #crm #saas #smallbusiness",
 slides=[
  dict(t="compare_cost", k="Fire your 15 apps", h="$1,094 a month vs [[$67 a month]]", left=[("CRM (HubSpot)","$100"),("Funnels (ClickFunnels)","$97"),("Courses (Kajabi)","$179"),("Reviews (Birdeye)","$299"),("Community (Skool)","$99"),("Call tracking (CallRail)","$55"),("Email (ActiveCampaign)","$49"),("+ 8 more tools","$216")], total="$1,094", ours="$67", src="Typical published starting prices, Oct 2026. Some are per seat or location."),
  dict(t="list", k="All inside one login", h="What you [[stop juggling]]", items=[("One contact record per customer","Every message, booking and payment together"),("One inbox","Text, email, Facebook, Instagram, WhatsApp, chat"),("One bill","Instead of 15 renewals"),("Unlimited contacts and users","On every plan")]),
  cta("Keep one bill. [[Fire the rest.]]","See the full comparison and plans at oceanicfunnels.com", kicker="Oceanic Funnels"),
 ]),
# 7 (Oct 31 AM) star thresholds
dict(cap="Consumers got pickier in 2026. BrightLocal found 68% will only use a business rated 4 stars or more, up from 55% a year earlier.\n\nAnd almost half want to see at least 20 reviews.",
 tags="#reviews #googlereviews #reputationmanagement #smallbusiness",
 slides=[
  dict(t="cover_stat", k="Star ratings", big="68%", h="will only use a business with [[4 stars or more.]]", sub="Up from 55% in 2025.", src="Source: BrightLocal, 2026"),
  dict(t="bars", k="The bar keeps rising", h="Minimum rating consumers [[will accept]]", items=[("4 stars or more",68,"68%"),("4.5 stars or more",31,"31%"),("Only 5 stars",10,"10%")], max=70, note="The 4.5+ group nearly doubled, from 17% in 2025.", src=BL),
  dict(t="cover_stat", k="Volume matters too", big="47%", h="won't use a business with [[fewer than 20 reviews.]]", src=BL),
  cta("More reviews. [[Better rating.]]","Ask every happy customer, automatically, after every job. That's how ratings climb and stay there."),
 ]),
# 8 (Oct 31 PM) about us: missed call text back
dict(cap="What happens when you miss a call with Oceanic Funnels?\n\nThe caller gets a text from your business number within seconds, and the conversation keeps going until they're booked.",
 tags="#missedcalltextback #smallbusiness #automation #customerservice",
 slides=[
  dict(t="cover_text", k="Missed calls", h="You missed the call. [[You didn't miss the customer.]]", swipe=True),
  dict(t="chat", k="What the caller gets", h="A text, [[seconds after the missed call]]", msgs=[("biz","Hi, it's Bright Smile Dental. Sorry we missed your call! How can we help?"),("u","Do you have anything for a cleaning this week?"),("biz","We do! Thursday 10:30 or Friday 2:00. Book here: [booking link]"),("u","Thursday works, booked. Thanks!")], src="Illustration. Business name is an example."),
  dict(t="list", k="Why it works", h="It turns a hang-up into [[a conversation]]", items=[("Instant","Sent automatically while you're busy"),("From your business number","So they recognise you"),("24/7","Nights and weekends too"),("Two-way","Your team or AI agent replies in one inbox")]),
  cta("Never lose a caller [[to voicemail again.]]","Missed call text back is included in Oceanic Funnels OS, from $67 a month.", kicker="Oceanic Funnels"),
 ]),
# 9 (Nov 1 AM) responding to reviews
dict(cap="89% of consumers expect business owners to respond to reviews, according to BrightLocal's 2026 survey. And half are put off by generic, copy-paste replies.\n\nSwipe for what customers expect and how fast.",
 tags="#reviews #customerservice #reputation #localbusiness",
 slides=[
  dict(t="cover_stat", k="Review replies", big="89%", h="of consumers expect owners to [[reply to reviews.]]", src="Source: BrightLocal, 2026"),
  dict(t="bars", k="Replies win business", h="What replies do to [[your chances]]", items=[("Likely to use a business that replies to all reviews",80,"80%"),("Unlikely to use a business that never replies",42,"42%"),("Put off by generic, templated replies",50,"50%")], max=80, src=BL),
  dict(t="bars", k="How fast?", h="When customers [[expect a reply]]", items=[("Same day",19,"19%"),("By the next day",32,"32%"),("Within a week",81,"81%")], max=90, note="Same-day expectations jumped from 6% in 2025.", src=BL),
  cta("Reply to every review, [[from one place.]]","Oceanic Funnels brings your reviews together so you can respond quickly, in your own words."),
 ]),
# 10 (Nov 1 PM) about us: AI agent DM
dict(cap="This is what an AI agent trained on your business does with a 9pm Instagram DM.\n\nIt answers, it books, and it hands anything sensitive to your team.",
 tags="#aiagents #instagram #medspa #automation",
 slides=[
  dict(t="cover_text", k="AI agent", h="9:14 PM. A new DM. [[Answered in seconds.]]", swipe=True),
  dict(t="chat", k="Instagram DM", h="The AI agent [[answers and books]]", msgs=[("u","Hi! How much is lip filler and do you have anything this week?"),("ai","Hi! Lip filler starts from $650 and your provider will confirm the exact plan at your consultation. We have Thursday 4:00 or Saturday 11:00. Which works?"),("u","Saturday please"),("ai","You're booked for Saturday at 11:00. You'll get a confirmation text and a short form to fill in before your visit.")], src="Illustration. Prices and times are examples."),
  dict(t="list", k="Set the rules", h="What a good AI agent [[always does]]", items=[("Uses your real menu, prices and policies","No guessing"),("Books into your calendar","With confirmations and reminders"),("Hands clinical questions to your team","Never gives medical advice"),("Logs every conversation","In one inbox your team can see")]),
  cta("Answer every DM, [[even at 9pm.]]","AI agents are part of Oceanic Funnels. Or let our team set yours up for you.", kicker="Oceanic Funnels"),
 ]),
# 11 (Nov 2 AM) Asking for reviews
dict(cap="Most customers will write a review if you ask. BrightLocal found 94% are open to writing reviews, and 28% will always write one when asked.\n\nThe businesses with the most reviews aren't luckier. They ask, every time.",
 tags="#googlereviews #reviews #smallbusiness #marketingtips",
 slides=[
  dict(t="cover_stat", k="Just ask", big="94%", h="of consumers are [[open to writing reviews.]]", src="Source: BrightLocal, 2026"),
  dict(t="bars", k="Asking works", h="What happens when [[you ask]]", items=[("Were asked for a review in the last year",78,"78%"),("Wrote at least one review in the last year",69,"69%"),("Will always write a review when asked",28,"28%")], max=80, note="The 'always' group rose from 16% in 2025.", src=BL),
  dict(t="compare", k="Google's rules", h="How to ask [[the right way]]", lh="Do", left=["Ask every customer","Send a direct review link","Ask soon after the visit","Reply to every review"], rh="Don't", right=["Offer gifts or discounts for reviews","Only ask customers you expect to be happy","Set staff review quotas","Ask for specific wording or names"], src="Based on Google's review policies, including the April 2026 update."),
  cta("Ask every customer, [[automatically.]]","Oceanic Funnels sends review requests after every job or visit, the right way."),
 ]),
# 12 (Nov 2 PM) about us: plans
dict(cap="Three ways to work with Oceanic Funnels. Every plan includes the full system with unlimited contacts, users and funnels. The difference is how much our team builds for you.",
 tags="#oceanicfunnels #crm #salesfunnel #smallbusiness",
 slides=[
  dict(t="cover_text", k="Plans", h="Pick how much [[we do for you.]]", sub="Same system on every plan. Unlimited contacts, users and funnels.", swipe=True),
  dict(t="plans", k="Three ways to start", h="Run it yourself, or [[let us build it]]", plans=[("OS","$67","/month","Run it yourself. Full system, ticket support."),("Growth","$197","/month","We set it up for you in week one, with 24/7 support."),("Done-For-You","$297","/month + $997 build","Our team builds your whole system. Live in 14 days.")]),
  dict(t="list", k="On every plan", h="No catches", items=[("No contracts","Month to month, cancel anytime"),("30-day money-back guarantee","On OS and Growth"),("Founding member pricing","The first 50 businesses keep their price for life"),("Pay-as-you-go usage","Texts, emails and AI replies, paid from your wallet")]),
  cta("Start this week.", "Compare plans at oceanicfunnels.com", kicker="Oceanic Funnels"),
 ]),
# 13 (Nov 3 AM) AI adoption QB
dict(cap="AI isn't a big-company thing anymore. QuickBooks surveyed more than 34,000 small and midsize business owners in the US, UK, Canada and Australia: roughly 7 in 10 now use AI regularly.\n\nIn the US, that jumped from 48% to 77% in under two years.",
 tags="#ai #smallbusiness #artificialintelligence #businessowner",
 slides=[
  dict(t="cover_stat", k="AI for business", big="7 in 10", h="small businesses now [[use AI regularly.]]", sub="Across the US, UK, Canada and Australia.", src="Source: QuickBooks 2026 AI Impact Report"),
  dict(t="bars", k="US growth", h="Regular AI use among [[US small businesses]]", items=[("July 2024",48,"48%"),("2026",77,"77%")], max=80, src=QB),
  dict(t="list", k="Where they start", h="The first jobs businesses [[hand to AI]]", items=[("Admin","Drafting, summarising, organising"),("Customer communication","Replies, follow-ups, FAQs"),("Scheduling","Bookings, reminders, rescheduling")], src=QB),
  cta("Put AI on the jobs [[that cost you customers.]]","Oceanic Funnels uses AI for replies, booking and follow-up, so leads never wait."),
 ]),
# 14 (Nov 3 PM) about us: 14 day build
dict(cap="From sign-up to a working system in 14 days. Here's exactly what happens.",
 tags="#doneforyou #salesfunnel #automation #smallbusiness",
 slides=[
  dict(t="cover_text", k="How it works", h="From sign-up to a working system [[in 14 days.]]", swipe=True),
  dict(t="timeline", k="The 14 days", h="What happens, [[step by step]]", items=[("Day 1","Pick your plan","Build it yourself on OS, or let our team handle it on Growth or Done-For-You."),("Days 2–7","We set up your system","Domain, business email, phone number, text registration, automations and your AI agent."),("Days 7–14","Go live","Your funnel and automations start catching, replying to and booking every lead."),("Every month","Keep growing","Edit requests, strategy calls and reports.")]),
  cta("Live in 14 days. [[Built by our team.]]","Done-For-You: $297 a month plus a one-time $997 build. Details at oceanicfunnels.com", kicker="Oceanic Funnels"),
 ]),
# 15 (Nov 4 AM) Goldman gap
dict(cap="Most small businesses use AI. Very few have built it into how they actually run.\n\nGoldman Sachs surveyed 1,256 US small business owners: 76% use AI, but only 14% have fully integrated it into core operations.",
 tags="#ai #smallbusiness #automation #digitaltransformation",
 slides=[
  dict(t="cover_stat", k="The AI gap", big="14%", h="of small businesses have fully [[built AI into their operations.]]", sub="Even though 76% use AI.", src="Source: Goldman Sachs, 2026"),
  dict(t="bars", k="Using vs building in", h="Most are still [[experimenting]]", items=[("Use AI",76,"76%"),("Fully integrated into core operations",14,"14%")], max=80, src=GS),
  dict(t="compare", k="What the difference looks like", h="Using AI vs [[building it in]]", lh="Using AI", left=["Ask ChatGPT to write a post","Copy and paste answers","Remember to follow up","Check messages when you can"], rh="Built in", right=["Every lead gets an instant reply","Bookings land in your calendar","Follow-ups send themselves","Every message in one inbox"]),
  cta("Build AI [[into the work itself.]]","That's what Oceanic Funnels sets up for you: AI connected to your inbox, calendar, CRM and payments."),
 ]),
# 16 (Nov 4 PM) about us: everything included
dict(cap="59 tools in one login. If something in your business is slow, manual or leaking money, there's probably a tool here for it.",
 tags="#allinone #marketingautomation #crm #smallbusiness",
 slides=[
  dict(t="cover_stat", k="Everything included", big="59", h="tools in one login. [[One bill.]]", swipe=True),
  dict(t="grid", k="Capture and convert", h="Get leads [[and close them]]", groups=[("Capture","Funnels, websites, forms, surveys, quizzes, live chat, blogs, webinars, stores"),("AI 24/7","AI chat agent, AI voice receptionist, missed call text back, instant replies"),("CRM and sales","Contacts, smart lists, pipelines, lead assignment, tasks"),("Booking","Calendars, round robin, classes and events, reminders")]),
  dict(t="grid", k="Grow and get paid", h="Keep customers [[coming back]]", groups=[("Get paid","Invoices, estimates, text-to-pay, subscriptions, e-signature, upsells"),("Marketing","Email and SMS campaigns, social planner, affiliate programs"),("Reviews","Review requests, replies, listings (add-on)"),("Courses","Online courses, memberships, paid communities")]),
  cta("Everything you pay 15 apps for. [[Already inside.]]","See the full list at oceanicfunnels.com", kicker="Oceanic Funnels"),
 ]),
# 17 (Nov 5 AM) barriers
dict(cap="What's really stopping small businesses from getting more out of AI? Not cost. In Goldman Sachs' 2026 survey, the top barriers were privacy, expertise and choosing the right tools.",
 tags="#ai #smallbusiness #aitools #businessowner",
 slides=[
  dict(t="cover_text", k="AI barriers", h="The biggest AI barrier [[isn't the price.]]", swipe=True),
  dict(t="bars", k="Top barriers", h="What holds AI users [[back]]", items=[("Data privacy and security",50,"50%"),("Lack of technical expertise",49,"49%"),("Choosing the right tools",48,"48%")], max=60, src=GS),
  dict(t="cover_stat", k="What they want", big="73%", h="say their business would benefit from [[more AI training and resources.]]", src=GS),
  cta("You don't need to become [[an AI expert.]]","Our team sets up AI that's connected to how your business actually works. You approve it, and it runs."),
 ]),
# 18 (Nov 5 PM) med spa rebooking
dict(cap="Med spa owners: every treatment on your menu has a natural rebooking window. Without reminders, clients drift, or book wherever is running a promotion that week.",
 tags="#medspa #aesthetics #botox #clientretention",
 slides=[
  dict(t="cover_text", k="Med spas", h="Botox fades in 3 to 6 months. [[Does your rebooking reminder?]]", swipe=True),
  dict(t="table", k="Rebooking windows", h="Follow-up for [[every treatment]]", rows=[("Neurotoxins","Typically 3–6 months"),("Dermal fillers","Commonly 6–18 months"),("Laser hair removal","Usually 4–8 sessions, 3–6 weeks apart"),("Chemical peels and facials","Often monthly"),("Microneedling","A series, several weeks apart")], src="Typical ranges from published patient guidance. Your providers set the exact intervals."),
  dict(t="list", k="Automate it", h="What runs [[after every visit]]", items=[("Aftercare message","The same day"),("Review request","Once results show"),("Rebooking reminder","Timed to the treatment"),("Membership offer","For regular clients")]),
  cta("Keep every client [[on schedule.]]","Built for med spas by Oceanic Funnels, and live in 14 days with Done-For-You.", kicker="Oceanic Funnels"),
 ]),
# 19 (Nov 6 AM) AI recommendation platforms
dict(cap="Where do people look for a local business now? Google is still first, but its share is falling, and AI tools have jumped to third place in one year.",
 tags="#localseo #aisearch #googlebusinessprofile #localbusiness",
 slides=[
  dict(t="cover_text", k="Search is changing", h="Google is still first. [[AI is catching up fast.]]", swipe=True),
  dict(t="bars", k="Where people look", h="Sources used to find [[local businesses]]", items=[("Google",71,"71%"),("ChatGPT and AI tools",45,"45%"),("Local news sites",29,"29%"),("Apple Maps",27,"27%")], max=80, note="In one year: Google fell from 83%, AI tools rose from 6%.", src=BL),
  dict(t="list", k="What to do", h="Be findable [[everywhere]]", items=[("Complete your Google Business Profile","Hours, services, photos, posts"),("Claim Apple Business Connect","Apple Maps shows your details"),("Keep listings consistent","Same name, address and phone everywhere"),("Answer questions on your website","For people and AI")]),
  cta("Show up wherever [[customers search.]]","Oceanic Funnels helps manage your website, reviews and listings in one place."),
 ]),
# 20 (Nov 6 PM) about us: one inbox
dict(cap="Text, email, Facebook, Instagram, WhatsApp, website chat. When messages are spread across apps, customers get missed. One inbox fixes that.",
 tags="#customerservice #inbox #crm #smallbusiness",
 slides=[
  dict(t="cover_text", k="One inbox", h="Six apps of messages. [[One inbox.]]", swipe=True),
  dict(t="inbox", k="Every channel", h="Every conversation, [[one screen]]", rows=[("SMS","Do you have anything Saturday?","2m"),("Instagram","How much is a facial?","9m"),("WhatsApp","Running 5 min late!","14m"),("Email","Quote for the kitchen job","1h"),("Facebook","Are you open on holidays?","2h"),("Website chat","Do you offer payment plans?","3h")], src="Illustration."),
  dict(t="list", k="Why it matters", h="Nobody waits, [[nobody gets missed]]", items=[("Full history next to every message","See what they bought and booked"),("Team-friendly","Assign conversations and see who replied"),("AI can answer first","Your team takes over when needed")]),
  cta("All your messages. [[One place.]]","One inbox is included in every Oceanic Funnels plan.", kicker="Oceanic Funnels"),
 ]),
# 21 (Nov 7 AM) AI productivity/revenue
dict(cap="Is AI actually paying off for small businesses? QuickBooks' 2026 data says yes: 78% of US small businesses say AI improved productivity, and 43% say it increased revenue. Only 2% say revenue fell.",
 tags="#ai #productivity #revenue #smallbusiness",
 slides=[
  dict(t="cover_stat", k="Does AI pay off?", big="43%", h="of US small businesses say AI [[increased their revenue.]]", sub="Only 2% say it decreased.", src="Source: QuickBooks, 2026"),
  dict(t="bars", k="Productivity", h="Say AI improved [[productivity]]", items=[("July 2024",46,"46%"),("2026",78,"78%")], max=80, src=QB),
  dict(t="cover_stat", k="Jobs", big="4×", h="more businesses report [[hiring more]] because of AI than hiring less.", src=QB),
  cta("Use AI to win [[more customers, faster.]]","Instant replies, booking and follow-up: where AI turns into revenue."),
 ]),
# 22 (Nov 7 PM) gyms
dict(cap="Gym and studio owners: the first week decides whether a new member sticks. Here's a simple automated first week that keeps new members coming back.",
 tags="#gymowner #fitnessbusiness #membership #automation",
 slides=[
  dict(t="cover_text", k="Gyms and studios", h="Win the first week, [[keep the member.]]", swipe=True),
  dict(t="timeline", k="Week one", h="The automated [[first week]]", items=[("Day 0","Welcome","A friendly text and what to bring."),("Day 1","After first class","A check-in: how did it go?"),("Day 4","No second visit yet","A nudge with an easy booking link."),("Day 6","Trial ending","An offer to join, with payment set up in one tap.")]),
  cta("Turn trials into [[members.]]","Class booking, reminders, memberships and billing in one system: Oceanic Funnels.", kicker="Oceanic Funnels"),
 ]),
# 23 (Nov 8 AM) Gmail/Yahoo rules
dict(cap="Sending email campaigns? Gmail and Yahoo require bulk senders to authenticate their domain, include one-click unsubscribe, and keep spam complaints under 0.3%. Miss these and you land in spam.",
 tags="#emailmarketing #deliverability #gmail #smallbusiness",
 slides=[
  dict(t="cover_stat", k="Email rules", big="0.3%", h="the maximum spam complaint rate [[Gmail and Yahoo allow.]]", src="Source: Gmail and Yahoo sender requirements, 2024"),
  dict(t="list", k="The requirements", h="What bulk senders [[must have]]", items=[("SPF, DKIM and DMARC","Prove your emails really come from you"),("One-click unsubscribe","Required since June 2024"),("Low spam complaints","Under 0.3%"),("Once a bulk sender, always","Gmail treats you as one permanently")], src="Source: Gmail and Yahoo bulk sender requirements (Feb 2024; unsubscribe Jun 2024)"),
  dict(t="list", k="Good habits", h="Stay in [[the inbox]]", items=[("Email people who asked to hear from you","And clean out bounces"),("One message, one link","Clear and simple"),("Make leaving easy","A visible unsubscribe link")]),
  cta("Set up properly [[from day one.]]","Domain authentication is part of our Growth and Done-For-You setup."),
 ]),
# 24 (Nov 8 PM) home services
dict(cap="Plumbers, HVAC, roofers, cleaners: when someone needs help now, they call the first business that answers. Here's how to be that business, even when you're on a job.",
 tags="#homeservices #plumbing #hvac #smallbusiness",
 slides=[
  dict(t="cover_text", k="Home services", h="The first business to reply [[usually gets the job.]]", swipe=True),
  dict(t="timeline", k="One job, automated", h="From missed call [[to five-star review]]", items=[("Missed call","Text back in seconds","While you're under a sink."),("Quote","Estimate sent by text","Accepted with one tap."),("Day before","Reminder","Time window and what to expect."),("After the job","Invoice and review","Text-to-pay, then a review request.")]),
  cta("Catch every job. [[Get paid faster.]]","Built for home service businesses by Oceanic Funnels.", kicker="Oceanic Funnels"),
 ]),
# 25 (Nov 9 AM) AI trust
dict(cap="Do people trust AI recommendations? Among consumers who use AI to find local businesses, 63% trust its recommendations, and 64% trust tools like ChatGPT as much as reviews.",
 tags="#ai #aisearch #consumertrends #localbusiness",
 slides=[
  dict(t="cover_stat", k="Trust in AI", big="63%", h="of AI users [[trust AI's business recommendations.]]", sub="Only 10% distrust them.", src="Source: BrightLocal, 2026"),
  dict(t="bars", k="AI vs reviews", h="Trust AI as much as [[reviews]]", items=[("AI users",64,"64%"),("All consumers",42,"42%")], max=70, src="Source: BrightLocal LCRS 2026 AI analysis (455 AI users of 1,002 US adults)"),
  dict(t="bars", k="By age", h="Who uses AI for [[local recommendations]]", items=[("Ages 30–44",64,"64%"),("Over 60",24,"24%")], max=70, src="Source: BrightLocal LCRS 2026 AI analysis"),
  cta("Make sure AI [[gets you right.]]","Clear website answers, consistent listings and fresh reviews. We help with all three."),
 ]),
# 26 (Nov 9 PM) about us: get paid
dict(cap="Send the invoice by text. Get paid from a phone in a few taps. Let reminders do the chasing.",
 tags="#invoicing #getpaid #payments #smallbusiness",
 slides=[
  dict(t="cover_text", k="Get paid", h="Stop chasing invoices. [[Let reminders do it.]]", swipe=True),
  dict(t="chat", k="Text-to-pay", h="An invoice they can pay [[in seconds]]", msgs=[("biz","Hi Sam, thanks for choosing us! Your invoice for $240 is ready: [pay link]"),("biz","Friendly reminder: your $240 invoice is due tomorrow. [pay link]"),("u","Paid, thanks!")], src="Illustration."),
  dict(t="list", k="Included", h="Everything to [[get paid]]", items=[("Estimates and invoices","Turn an accepted estimate into an invoice"),("Text-to-pay and payment links","Card payments from any phone"),("Recurring billing","Memberships, plans and retainers"),("Contracts and e-signature","Signed and paid in one flow")]),
  cta("Get paid [[without the awkward calls.]]","Payments are built into every Oceanic Funnels plan.", kicker="Oceanic Funnels"),
 ]),
# 27 (Nov 10 AM) prompt: FAQ
dict(cap="AI tools and Google read your website to answer questions about you. Here's a prompt that turns real customer questions into clear website answers. Save it and try it today.",
 tags="#aiprompts #chatgpt #seo #smallbusiness",
 slides=[
  dict(t="cover_text", k="Prompt of the day", h="Turn customer questions into [[answers AI can quote.]]", swipe=True),
  dict(t="prompt", k="Copy this prompt", h="Paste into ChatGPT, Claude or Gemini", text="I run a [type of business] in [city]. Here are 10 questions customers ask me: [paste questions].\n\nFor each, write a clear 2–3 sentence answer for my website FAQ page. Use plain language, include prices or timeframes where I give them, and don't make anything up."),
  dict(t="list", k="Then", h="Before you [[publish]]", items=[("Check every fact","AI fills gaps if you let it"),("Add your real prices and times","Specific answers get used"),("One question per heading","Easy for people and AI to scan")]),
  cta("Clear answers [[get recommended.]]","Want it done for you? Our team builds FAQ-rich pages as part of Done-For-You."),
 ]),
# 28 (Nov 10 PM) dentists / clinics
dict(cap="Dental and healthcare practices: recall reminders fill the diary without a single phone call. Here's the automated patient journey.",
 tags="#dentalpractice #healthcare #patientcare #automation",
 slides=[
  dict(t="cover_text", k="Dental and clinics", h="Fill the diary [[without picking up the phone.]]", swipe=True),
  dict(t="timeline", k="Patient journey", h="Automated, [[start to finish]]", items=[("New enquiry","Instant reply","Answered in seconds, with a booking link."),("Booked","Forms and reminders","Intake forms sent before the visit."),("After the visit","Review request","Sent once they're home."),("6 months later","Recall reminder","Time to book their next check-up.")]),
  cta("Keep patients [[coming back on time.]]","Oceanic Funnels runs marketing and reminders. Clinical records stay in your practice software.", kicker="Oceanic Funnels"),
 ]),
# 29 (Nov 11 AM) Instagram hashtags
dict(cap="Instagram now allows a maximum of 5 hashtags per post. And hashtags help Instagram understand your post rather than pushing it to new people.\n\nHere's what actually drives reach.",
 tags="#instagramtips #socialmediamarketing #hashtags #smallbusiness",
 slides=[
  dict(t="cover_stat", k="Instagram", big="5", h="hashtags maximum per post, [[since December 2025.]]", src="Source: Later, 2026"),
  dict(t="list", k="Use them well", h="How to pick your [[5 hashtags]]", items=[("2 niche community tags","Where your customers actually are"),("2 topic tags","What the post is about"),("1 branded or location tag","Who you are, or where")], src="Based on Later's 2026 Instagram hashtag guidance"),
  dict(t="bars", k="What drives reach", h="Engagement rate by [[post format]]", items=[("Carousels",55,"0.55%"),("Reels",52,"0.52%"),("Single images",37,"0.37%")], max=60, note="Carousels also lead on saves and views.", src="Source: Socialinsider Instagram benchmarks, 67.5M business posts"),
  cta("Post less noise. [[Post more value.]]","Like this carousel? Save it and follow for weekly tips for business owners."),
 ]),
# 30 (Nov 11 PM) soccer academies
dict(cap="Soccer clubs and academies: a free trial is where most families decide. Here's how to turn more trial sessions into registered players.",
 tags="#soccer #youthsports #sportsacademy #automation",
 slides=[
  dict(t="cover_text", k="Sports academies", h="Trial session booked. [[Then what?]]", swipe=True),
  dict(t="timeline", k="Trial to registration", h="The automated [[parent journey]]", items=[("Booked","Confirmation","What to bring and where to go."),("Day before","Reminder","Time, location, reschedule link."),("After the trial","Follow-up","How it went, and how to join."),("Joining","Payment","Season or monthly plan in one tap.")]),
  cta("More trials. [[More registered players.]]","Booking, reminders, registrations and payments in one system.", kicker="Oceanic Funnels"),
 ]),
# 31 (Nov 12 AM) LinkedIn
dict(cap="On LinkedIn in 2026, personal profiles get far more reach than company pages, and posts with links get much less. If you use LinkedIn for business, this changes what you post.",
 tags="#linkedintips #linkedin #b2bmarketing #personalbranding",
 slides=[
  dict(t="cover_text", k="LinkedIn 2026", h="Your personal profile [[beats your company page.]]", swipe=True),
  dict(t="bars", k="Share of feed distribution", h="Who gets [[the reach]]", items=[("Personal profiles",65,"~65%"),("Company pages",5,"~5%")], max=70, src="Source: SocialPilot, LinkedIn algorithm 2026"),
  dict(t="list", k="What works now", h="LinkedIn in [[2026]]", items=[("Keep links out of the post","Posts with links get about 60% less reach"),("Use 1–3 hashtags","More can reduce reach"),("Try document carousels","The highest engagement format"),("Company pages: max 1 post a day","Let each post breathe")], src="Source: SocialPilot, LinkedIn algorithm 2026 (Sep 2026)"),
  cta("Post where [[the reach is.]]","Save this before your next LinkedIn post."),
 ]),
# 32 (Nov 12 PM) about us: Done-For-You
dict(cap="Done-For-You means our team builds your whole system. Here's exactly what's included.",
 tags="#doneforyou #marketingautomation #salesfunnel #smallbusiness",
 slides=[
  dict(t="cover_text", k="Done-For-You", h="You run the business. [[We build the system.]]", swipe=True),
  dict(t="grid", k="What we build", h="Everything, [[set up for you]]", groups=[("Funnels","For your main offers, with booking and payments"),("AI agent","Trained on your services, prices and policies"),("Automations","Missed call text back, follow-up, reminders, rebooking"),("Reviews and reporting","Review requests, pipeline, monthly report and call")]),
  dict(t="plans", k="Price", h="One build, [[then month to month]]", plans=[("Done-For-You","$297","/month","Plus a one-time $997 build fee. Live in 14 days. Cancel anytime.")]),
  cta("Get it [[built for you.]]","See what's included at oceanicfunnels.com", kicker="Oceanic Funnels"),
 ]),
# 33 (Nov 13 AM) best times
dict(cap="When should a business post? Sprout Social analysed around 2 billion engagements across 307,000 profiles. Weekdays from late morning to afternoon win on every major platform, and weekends are weakest.",
 tags="#socialmediatips #socialmediamarketing #contentstrategy #smallbusiness",
 slides=[
  dict(t="cover_text", k="Posting times", h="When your posts [[get the most engagement]]", swipe=True),
  dict(t="table", k="Best windows (local time)", h="Weekdays win, [[weekends lose]]", rows=[("Facebook","Tue–Wed, 12–8 pm"),("Instagram","Wed, 12–9 pm · Tue, 1–7 pm"),("LinkedIn","Tue–Wed, 11 am–4/5 pm"),("Weakest","Weekends, on all three")], src="Source: Sprout Social, ~2B engagements across 307K profiles (Nov 2025–Feb 2026)"),
  dict(t="list", k="Use it", h="Then [[test your own]]", items=[("Start with these windows","They're averages, not rules"),("Check your Insights after 4 weeks","Your audience may differ"),("Schedule in bulk","So posting never depends on remembering")]),
  cta("Plan a month [[in one sitting.]]","Our social planner schedules Facebook, Instagram, LinkedIn and more from one calendar."),
 ]),
# 34 (Nov 13 PM) real estate
dict(cap="Real estate agents: buyer enquiries come in at night and at weekends, when people are actually browsing. Here's how to answer every one within seconds.",
 tags="#realestate #realtor #leadgeneration #automation",
 slides=[
  dict(t="cover_text", k="Real estate", h="A 10pm buyer enquiry [[can't wait until tomorrow.]]", swipe=True),
  dict(t="chat", k="Instant reply", h="Qualified and booked, [[while you sleep]]", msgs=[("u","Is the 3-bed on Maple Street still available?"),("ai","It is! Are you looking to buy within the next 3 months, and are you pre-approved?"),("u","Yes, pre-approved, hoping to move by spring"),("ai","Great. Viewings are available Saturday at 10:00 or 11:30. Which suits you?")], src="Illustration."),
  cta("Answer every enquiry. [[Book more viewings.]]","Instant replies, qualification and a pipeline for every lead, with Oceanic Funnels.", kicker="Oceanic Funnels"),
 ]),
# 35 (Nov 14 AM) missed calls UK study
dict(cap="How many calls do small businesses miss? When one UK study phoned 142 small businesses, 47% didn't answer. Most of those had no message-taking service at all.",
 tags="#missedcalls #customerservice #smallbusinessuk #smallbusiness",
 slides=[
  dict(t="cover_stat", k="Missed calls", big="47%", h="of small businesses [[didn't answer]] the phone.", sub="In a test of 142 UK small businesses.", src="Source: TelePA phone study, 142 UK small businesses"),
  dict(t="cover_text", k="And then", h="Over half of those [[had no way to take a message.]]", sub="No voicemail service, no call forwarding, no follow-up."),
  dict(t="list", k="Simple fixes", h="Catch the calls [[you can't take]]", items=[("Missed call text back","An instant text from your number"),("AI voice receptionist","Answers and books when you can't"),("Call tracking","See which ads make the phone ring")]),
  cta("Every missed call [[gets a reply.]]","Missed call text back is included in every Oceanic Funnels plan."),
 ]),
# 36 (Nov 14 PM) about us: after booking timeline
dict(cap="One booking, six automatic touchpoints, zero admin. Here's what happens after a customer books with a business using Oceanic Funnels.",
 tags="#customerjourney #automation #appointments #smallbusiness",
 slides=[
  dict(t="cover_text", k="After the booking", h="One booking. Six touchpoints. [[Zero admin.]]", swipe=True),
  dict(t="timeline", k="Automatic", h="What runs [[by itself]]", items=[("Instantly","Confirmation","By text and email."),("Before the visit","Intake form","Sent automatically."),("Day before","Reminder","With a reschedule link."),("Same day","Reminder","A few hours before."),("After","Thank-you and review request","When they're happiest."),("Later","Rebooking reminder","At the right interval.")]),
  cta("Fewer no-shows. [[More repeat visits.]]","Booking and reminders are part of every Oceanic Funnels plan.", kicker="Oceanic Funnels"),
 ]),
# 37 (Nov 15 AM) AI agent rules safety
dict(cap="AI agents answer customers in seconds, day and night. But only if you set them up properly. Three rules before you let AI talk to your customers.",
 tags="#aiagents #aisafety #customerservice #smallbusiness",
 slides=[
  dict(t="cover_text", k="AI safety", h="3 rules before AI [[talks to your customers]]", swipe=True),
  dict(t="list", k="The rules", h="Set it up [[like a new hire]]", items=[("Give it your real information","Services, prices, hours, policies. AI guesses when it doesn't know."),("Tell it what not to answer","Medical, legal or financial specifics go to a person"),("Review conversations weekly","Fix anything it got wrong")]),
  dict(t="compare", k="Good vs bad", h="What a good AI agent [[does and doesn't do]]", lh="Does", left=["Answers in seconds","Books into your calendar","Admits when it doesn't know","Hands over to your team"], rh="Doesn't", right=["Make up prices","Give medical advice","Promise results","Trap customers in loops"]),
  cta("AI that represents you [[properly.]]","We train and test every AI agent we set up, before it goes live."),
 ]),
# 38 (Nov 15 PM) coaches
dict(cap="Coaches and course creators: stop running your business from five different tools. Funnels, calls, payments, courses and community, all in one place.",
 tags="#coaching #onlinecourse #coursecreator #onlinebusiness",
 slides=[
  dict(t="cover_text", k="Coaches", h="Your whole coaching business [[in one login.]]", swipe=True),
  dict(t="compare", k="Before vs after", h="Five tools vs [[one system]]", lh="Before", left=["Funnel builder","Calendar app","Course platform","Community app","Email tool"], rh="After", right=["Funnels and websites","Discovery call booking","Courses and memberships","Paid communities","Email and SMS follow-up"]),
  cta("One system. [[One bill.]]","Unlimited contacts and users, from $67 a month.", kicker="Oceanic Funnels"),
 ]),
# 39 (Nov 16 AM) prompt: review themes
dict(cap="Your customers have already written your best marketing. This prompt finds it in your reviews.",
 tags="#aiprompts #reviews #marketing #smallbusiness",
 slides=[
  dict(t="cover_text", k="Prompt of the day", h="Turn your reviews into [[your best marketing.]]", swipe=True),
  dict(t="prompt", k="Copy this prompt", h="Paste in your last 20 reviews", text="Here are my latest customer reviews: [paste reviews].\n\nWhat do customers praise most? List the top 5 themes with a short quote for each. Then suggest 3 website headlines based only on what customers actually said."),
  dict(t="list", k="Use the results", h="Where to [[put them]]", items=[("Your homepage headline","In your customers' words"),("Social posts","One theme per post"),("Your sales calls","Proof, not promises")]),
  cta("More reviews = [[more material.]]","Automatic review requests keep fresh quotes coming."),
 ]),
# 40 (Nov 16 PM) about us: founding pricing
dict(cap="Founding member offer: the first 50 businesses on Oceanic Funnels keep their price for life, even when our prices go up.",
 tags="#oceanicfunnels #smallbusiness #crm #marketingautomation",
 slides=[
  dict(t="cover_stat", k="Founding members", big="50", h="businesses keep their price [[for life.]]", swipe=True),
  dict(t="plans", k="Lock in today", h="Founding prices, [[locked]]", plans=[("OS","$67","/month","Run it yourself."),("Growth","$197","/month","Set up for you in week one."),("Done-For-You","$297","/month + $997 build","Built by our team.")]),
  cta("Lock in [[your price.]]","oceanicfunnels.com", kicker="Oceanic Funnels"),
 ]),
# 41 (Nov 17 AM) AI voice scams
dict(cap="AI can clone a voice from a short audio clip. Businesses have received calls that sound like the owner or a supplier asking for an urgent payment. Three simple protections.",
 tags="#cybersecurity #aiscams #fraudprevention #smallbusiness",
 slides=[
  dict(t="cover_text", k="AI safety", h="That urgent call from the boss [[might be AI.]]", swipe=True),
  dict(t="list", k="Protect your business", h="3 rules for [[every payment request]]", items=[("Never pay on a call or voice note alone","However urgent it sounds"),("Agree a code word","For urgent payment requests"),("Confirm bank detail changes","Through a number you already know")]),
  cta("Use AI. [[Don't let it be used against you.]]","Share this with your team."),
 ]),
# 42 (Nov 17 PM) salons
dict(cap="Salons, barbers, lash and nail studios: fill last-minute gaps and keep regulars on schedule automatically.",
 tags="#salonowner #barbershop #lashtech #automation",
 slides=[
  dict(t="cover_text", k="Salons", h="A 9am cancellation [[doesn't have to mean an empty chair.]]", swipe=True),
  dict(t="chat", k="Gap filler", h="Fill the slot [[in minutes]]", msgs=[("biz","A 2:00 slot just opened today with Jess. Want it? Reply YES to book."),("u","YES!"),("biz","You're booked for 2:00 with Jess. See you soon!")], src="Illustration."),
  dict(t="list", k="Also automated", h="Keep the diary [[full]]", items=[("Reminders","Before every appointment"),("Rebooking prompts","Timed to their usual visit"),("Review requests","After every visit")]),
  cta("Keep every chair [[busy.]]","Booking, reminders and texting in one system: Oceanic Funnels.", kicker="Oceanic Funnels"),
 ]),
# 43 (Nov 18 AM) data privacy
dict(cap="Half of small business AI users name data privacy and security as a concern. They're right to. Here's the simple rule for using free AI tools safely.",
 tags="#dataprivacy #aisafety #cybersecurity #smallbusiness",
 slides=[
  dict(t="cover_stat", k="AI privacy", big="50%", h="of small business AI users are concerned about [[data privacy and security.]]", src="Source: Goldman Sachs, 2026"),
  dict(t="compare", k="The simple rule", h="What goes into [[free AI tools]]", lh="Fine", left=["Drafting posts and emails","Brainstorming ideas","Rewriting your own text","Summaries with names removed"], rh="Keep out", right=["Customer names and phone numbers","Medical or health details","Payment or bank details","Passwords and logins"]),
  cta("Use AI inside systems [[built for business data.]]","Save this and share it with your team."),
 ]),
# 44 (Nov 18 PM) about us: AI voice receptionist
dict(cap="An AI voice receptionist answers when you can't, in a natural voice, and books the caller into your calendar.",
 tags="#voiceai #aireceptionist #smallbusiness #customerservice",
 slides=[
  dict(t="cover_text", k="AI voice", h="AI can now answer your phone [[and book the appointment.]]", swipe=True),
  dict(t="compare", k="Set the rules", h="What it should [[and shouldn't]] do", lh="Should", left=["Greet callers by your business name","Answer hours, location, services","Book, reschedule and confirm","Take a clear message"], rh="Never", right=["Give medical, legal or financial advice","Promise things you haven't approved","Keep callers in circles","Pretend to be a named staff member"]),
  cta("Answer every call, [[24/7.]]","AI voice is available in Oceanic Funnels, with pay-as-you-go usage.", kicker="Oceanic Funnels"),
 ]),
# 45 (Nov 19 AM) cold email benchmarks? -> review policy deep dive (safer): reviews volume 20
dict(cap="47% of consumers won't use a business with fewer than 20 reviews. If you're under 20, here's the fastest honest way to get there.",
 tags="#googlereviews #reviews #localseo #smallbusiness",
 slides=[
  dict(t="cover_stat", k="The 20-review line", big="20", h="reviews: the minimum for [[almost half of consumers.]]", sub="47% won't use a business with fewer.", src="Source: BrightLocal, 2026"),
  dict(t="list", k="Get to 20", h="The honest [[fast track]]", items=[("Message your last 50 customers","A short, personal ask with a direct link"),("Ask every new customer","Automatically after every visit"),("Make it one tap","Link straight to your review form"),("Thank every reviewer","Publicly, by name")]),
  dict(t="compare", k="Stay within the rules", h="Never [[do this]]", lh="Allowed", left=["Asking every customer","Reminding once","Replying to reviews"], rh="Not allowed", right=["Paying or rewarding reviews","Only asking happy customers","Review quotas for staff"], src="Based on Google's review policies."),
  cta("Reach 20 reviews, [[then keep going.]]","Automatic review requests from Oceanic Funnels."),
 ]),
# 46 (Nov 19 PM) restaurants
dict(cap="Restaurants and cafés: regulars are your most valuable customers. Here's how automation helps you make more of them.",
 tags="#restaurant #hospitality #customerloyalty #marketing",
 slides=[
  dict(t="cover_text", k="Restaurants", h="Turn first-time diners [[into regulars.]]", swipe=True),
  dict(t="timeline", k="Stay in touch", h="The automated [[guest journey]]", items=[("Booking","Confirmation","And a reminder on the day."),("Next day","Thank-you","With a review link."),("Birthday","A small treat","Sent automatically every year."),("Monthly","What's on","Events, specials and new menus.")]),
  cta("Bring them [[back again.]]","Bookings, reviews and campaigns in one system.", kicker="Oceanic Funnels"),
 ]),
# 47 (Nov 20 AM) prompt: follow-up
dict(cap="The follow-up you keep forgetting to send? Let AI write it, then automate it so it sends itself.",
 tags="#aiprompts #followup #sales #smallbusiness",
 slides=[
  dict(t="cover_text", k="Prompt of the day", h="Let AI write [[the follow-up you forgot.]]", swipe=True),
  dict(t="prompt", k="Copy this prompt", h="For leads who went quiet", text="Write a short, friendly follow-up text to a customer who asked about [service] 3 days ago but didn't book. Mention [one benefit]. End with a simple question. Under 300 characters. No pressure."),
  dict(t="cover_text", k="Even better", h="Write it once. [[Let it send itself.]]", sub="Turn it into an automation that goes to every lead who goes quiet, and stops when they reply."),
  cta("Follow up with [[every lead, every time.]]","Follow-up sequences are built into Oceanic Funnels."),
 ]),
# 48 (Nov 20 PM) about us: reactivation
dict(cap="Your old leads are worth more than you think. You paid to get every contact in your list. A reactivation campaign gives them a reason to come back.",
 tags="#databasereactivation #emailmarketing #smsmarketing #sales",
 slides=[
  dict(t="cover_text", k="Old leads", h="Your contact list is [[money you already paid for.]]", swipe=True),
  dict(t="timeline", k="A simple reactivation", h="Wake up [[old leads]]", items=[("Day 1","Personal text","A short, friendly message with a reason to come back."),("Day 3","Email","More detail and a booking link."),("Day 7","Final nudge","A last reminder before the offer ends."),("Anytime","Replies","Land in one inbox for your team.")]),
  cta("Turn old leads into [[new bookings.]]","Reactivation campaigns are part of Done-For-You.", kicker="Oceanic Funnels"),
 ]),
# 49 (Nov 21 AM) US texting registration
dict(cap="Sending business texts in the US? Your number needs to be registered for business texting first, or your messages can be blocked or filtered.",
 tags="#smsmarketing #textmessaging #a2p10dlc #smallbusinessusa",
 slides=[
  dict(t="cover_text", k="US business texting", h="Texting customers in the US? [[Register first.]]", swipe=True),
  dict(t="list", k="What's required", h="Before you [[send]]", items=[("A2P 10DLC registration","For local 10-digit numbers"),("Or toll-free verification","For toll-free numbers"),("Clear opt-in","Customers agreed to hear from you"),("Easy opt-out","Reply STOP to unsubscribe")], src="US carrier rules for business texting."),
  cta("We handle [[the registration.]]","Text registration is part of our Growth and Done-For-You setup."),
 ]),
# 50 (Nov 21 PM) pipeline
dict(cap="Do you know where every lead is right now? A sales pipeline shows every lead and deal by stage, so nothing gets forgotten.",
 tags="#salespipeline #crm #sales #smallbusiness",
 slides=[
  dict(t="cover_text", k="Pipelines", h="Do you know where [[every lead is]] right now?", swipe=True),
  dict(t="pipeline", k="See it all", h="Every lead, [[every stage]]", cols=[("New",["Sarah K.","James P.","Ava L."]),("Contacted",["Mia R.","Leo T."]),("Booked",["Noah B.","Emma W."]),("Won",["Olivia S."])], src="Illustration."),
  dict(t="list", k="Automations move them", h="Leads move [[by themselves]]", items=[("They book","Moved to Booked"),("They pay","Moved to Won"),("They go quiet","Follow-up starts")]),
  cta("If you can see it, [[you can fix it.]]","Pipelines are part of every Oceanic Funnels plan.", kicker="Oceanic Funnels"),
 ]),
# 51 (Nov 22 AM) AI agents vs chatbots
dict(cap="A chatbot answers questions. An AI agent gets things done. Here's the difference, and why it matters for your customers.",
 tags="#aiagents #chatbot #ai #customerservice",
 slides=[
  dict(t="cover_text", k="AI explained", h="A chatbot answers questions. [[An AI agent gets things done.]]", swipe=True),
  dict(t="compare", k="The difference", h="Chatbot vs [[AI agent]]", lh="Old chatbot", left=["Follows a fixed script","Gets stuck off-script","Can't take action","Frustrates customers"], rh="AI agent", right=["Understands the question","Looks up your real information","Books appointments","Hands over to a person"]),
  cta("Serve customers, [[don't deflect them.]]","AI agents are built into Oceanic Funnels."),
 ]),
# 52 (Nov 22 PM) about us: industries
dict(cap="Built for the way your business works: 51 industries and counting, from med spas and dentists to soccer academies and roofers.",
 tags="#smallbusiness #localbusiness #crm #automation",
 slides=[
  dict(t="cover_stat", k="Industries", big="51", h="industries, [[one system.]]", swipe=True),
  dict(t="grid", k="Who it's for", h="Set up for [[your kind of business]]", groups=[("Health and beauty","Med spas, dentists, chiropractors, salons, lash and nail"),("Fitness and sports","Gyms, studios, personal trainers, soccer academies, swim schools"),("Home services","HVAC, plumbing, roofing, cleaning, landscaping, solar"),("Professional","Coaches, agencies, real estate, accountants, law firms")]),
  cta("Find your industry [[at oceanicfunnels.com]]","Each industry page shows the exact setup for that business.", kicker="Oceanic Funnels"),
 ]),
# 53 (Nov 23 AM) prompt: bad review
dict(cap="A bad review is a chance to show every future customer how you handle problems. Here's a prompt for a calm, professional reply.",
 tags="#aiprompts #reviews #reputationmanagement #smallbusiness",
 slides=[
  dict(t="cover_text", k="Prompt of the day", h="Reply to a bad review [[without making it worse.]]", swipe=True),
  dict(t="prompt", k="Copy this prompt", h="Paste in the review", text="Write a calm, professional reply to this negative review. Thank them, acknowledge the issue without arguing, briefly explain what we're doing about it, and invite them to contact us directly. Under 80 words. Don't sound templated.\n\n[paste review]"),
  dict(t="cover_stat", k="Why it matters", big="50%", h="of consumers are put off by [[generic, templated replies.]]", sub="Edit the draft so it sounds like you.", src="Source: BrightLocal, 2026"),
  cta("Every review, [[answered properly.]]","Save this for the next tough review."),
 ]),
# 54 (Nov 23 PM) chiropractors / physio
dict(cap="Chiropractors and physiotherapists: someone in pain books with whoever responds first. Here's how to be first, and how to help patients finish their care plans.",
 tags="#chiropractor #physiotherapy #patientcare #automation",
 slides=[
  dict(t="cover_text", k="Chiro and physio", h="Someone in pain books [[with whoever answers first.]]", swipe=True),
  dict(t="timeline", k="Patient journey", h="Answered fast, [[followed up properly]]", items=[("Enquiry","Instant reply","With a link to book a first visit."),("Booked","Intake forms","Sent automatically before the visit."),("Care plan","Session reminders","And a nudge if one is missed."),("Finished","Review request","And a check-in later.")]),
  cta("More enquiries become [[patients.]]","Set up for clinics by Oceanic Funnels.", kicker="Oceanic Funnels"),
 ]),
# 55 (Nov 24 AM) start with one leak
dict(cap="Don't try to automate everything at once. Find the leak that costs you the most, fix it, measure it for a month, then fix the next one.",
 tags="#automation #smallbusiness #productivity #businesstips",
 slides=[
  dict(t="cover_text", k="Where to start", h="Start with one leak, [[not ten.]]", swipe=True),
  dict(t="list", k="The common leaks", h="Which one [[costs you most?]]", items=[("Slow replies to new leads","Fix: instant automatic reply"),("Missed calls","Fix: missed call text back"),("No-shows","Fix: reminders and reschedule links"),("Unpaid invoices","Fix: text-to-pay and reminders"),("Forgotten follow-ups","Fix: follow-up sequences")]),
  cta("Fix the biggest leak [[this month.]]","Not sure which? Ask us, and we'll tell you honestly."),
 ]),
# 56 (Nov 24 PM) about us: social planner
dict(cap="Posting every day is hard when you're running a business. Plan and schedule a month of posts for every platform in one sitting. This post was scheduled that way.",
 tags="#socialmediamarketing #contentplanning #smallbusiness #marketingtips",
 slides=[
  dict(t="cover_text", k="Social planner", h="Plan a month of posts [[in one sitting.]]", swipe=True),
  dict(t="list", k="Included", h="Social, [[sorted]]", items=[("Schedule in bulk","Upload a month at once"),("Every platform","Facebook, Instagram, LinkedIn and more"),("One calendar","See everything that's going out"),("Same login","As your CRM, inbox and funnels")]),
  cta("This post was [[scheduled with it.]]","The social planner is included in Oceanic Funnels.", kicker="Oceanic Funnels"),
 ]),
# 57 (Nov 25 AM) prompt: sales call prep
dict(cap="Two minutes of AI prep before a sales call. Walk in knowing their likely problems, the right questions and the objections they'll raise.",
 tags="#aiprompts #sales #salestips #smallbusiness",
 slides=[
  dict(t="cover_text", k="Prompt of the day", h="Prepare for a sales call [[in two minutes.]]", swipe=True),
  dict(t="prompt", k="Copy this prompt", h="Before your next call", text="I'm about to speak to a [type of business] owner about [your service]. List the 5 problems they most likely have, 5 questions I should ask, and 3 objections they might raise, with a calm answer to each."),
  cta("Listen more [[than you talk.]]","Save this for your next call."),
 ]),
# 58 (Nov 25 PM) about us: what OS includes vs growth support
dict(cap="Not sure whether to build it yourself or have us set it up? Here's the honest difference between OS and Growth.",
 tags="#oceanicfunnels #crm #smallbusiness #marketingautomation",
 slides=[
  dict(t="cover_text", k="OS or Growth?", h="Build it yourself, [[or have it set up?]]", swipe=True),
  dict(t="compare", k="The difference", h="OS vs [[Growth]]", lh="OS · $67/month", left=["The full system","Unlimited contacts and users","Ticket support","You set it up"], rh="Growth · $197/month", right=["Everything in OS","We set it up in week one","24/7 support","Text registration handled"]),
  cta("Pick what fits [[your time.]]","Both include a 30-day money-back guarantee. oceanicfunnels.com", kicker="Oceanic Funnels"),
 ]),
# 59 (Nov 26 AM) AI augments
dict(cap="Will AI replace your team? Small business owners who use it say no: 87% say AI augments their workforce rather than displacing people.",
 tags="#ai #teamwork #futureofwork #smallbusiness",
 slides=[
  dict(t="cover_stat", k="AI and jobs", big="87%", h="of AI-using owners say it [[augments their team]], not replaces it.", src="Source: Goldman Sachs, 2026"),
  dict(t="compare", k="Who does what", h="AI vs [[your team]]", lh="Give to AI", left=["The first reply","Reminders","Follow-ups","Summaries and drafts"], rh="Keep for people", right=["The consultation","Complex questions","Relationships","Judgement calls"]),
  cta("AI handles the waiting. [[Your team handles the people.]]","That's the balance we build at Oceanic Funnels."),
 ]),
# 60 (Nov 26 PM) final CTA
dict(cap="Funnels, CRM, AI agents, booking, reminders, reviews, payments and follow-up in one system that works 24/7. Run it yourself from $67 a month, or let our team build it for you.",
 tags="#oceanicfunnels #salesfunnel #crm #marketingautomation",
 slides=[
  dict(t="cover_text", k="Oceanic Funnels", h="Stop fishing for customers. [[Build the net.]]", swipe=True),
  dict(t="list", k="Every lead caught", h="What the net [[does for you]]", items=[("Catches every lead","Funnels, forms, chat and calls"),("Replies in seconds","AI agents and automations, 24/7"),("Books and reminds","Calendars that fill themselves"),("Gets you paid","Invoices, links and subscriptions"),("Brings them back","Reviews, rebooking and reactivation")]),
  cta("Build your net [[this week.]]","Unlimited contacts and users. No contracts. oceanicfunnels.com", kicker="Oceanic Funnels"),
 ]),
]
assert len(POSTS) == 60, len(POSTS)
