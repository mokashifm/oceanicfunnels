"""Guides part B: bookings, reviews, compliance, funnels and CRM."""

G_B = [
dict(
 slug="reduce-appointment-no-shows", cat="Booking",
 title="How to reduce appointment no-shows with automated reminders",
 kw="How to Reduce Appointment No-Shows with Automated Reminders",
 desc="No-shows cost service businesses hours every week. Here's how automated confirmations, reminders, deposits and easy rescheduling cut no-shows.",
 read=7,
 short="The most effective way to reduce no-shows is a set of automated messages around every booking: an instant confirmation, a reminder a day before, a second reminder an hour or two before, and a one-tap link to reschedule. For appointments that are often missed, add a deposit at booking. In Oceanic Funnels OS, you set these up per calendar under Calendar Settings → Notifications, by SMS, email and WhatsApp.",
 sections=[
  ("Why people don't show up", """
<ul>
<li><b>They forgot.</b> The most common reason, and the easiest to fix.</li>
<li><b>Plans changed and rescheduling was hard.</b> If the only option is a phone call during office hours, many people just don't come.</li>
<li><b>Low commitment.</b> Free consultations and trial sessions booked on impulse are easy to skip.</li>
</ul>"""),
  ("The reminder sequence that works", """
<ol>
<li><b>Instant confirmation</b> with the date, time, address or meeting link, and what to bring.</li>
<li><b>Reminder 24 hours before</b> with a reschedule link.</li>
<li><b>Reminder 1 to 2 hours before</b> by SMS, the channel people see fastest.</li>
<li><b>No-show follow-up</b> within an hour of a missed appointment, with a link to rebook.</li>
<li><b>Follow-up after attended appointments</b> with next steps, a review request or a rebooking offer.</li>
</ol>"""),
  ("Make rescheduling easier than skipping", """
<p>Include a reschedule and cancel link in every reminder. A person who reschedules is still a customer; a person who no-shows often isn't. Rescheduled bookings also free the original slot for someone else.</p>"""),
  ("Use deposits for high-value appointments", """
<p>For consultations, treatments and sessions that are often missed, take a deposit or payment at booking. Even a small amount raises commitment. Oceanic Funnels OS can take a payment as part of the booking flow.</p>"""),
  ("How to set it up in Oceanic Funnels OS", """
<ol class="nf-steps-list">
<li>Go to <b>Calendars → Calendar Settings</b>, choose your calendar and open the <b>Notifications</b> tab.</li>
<li>Turn on <b>Booked</b> confirmations for the contact by email and SMS.</li>
<li>Turn on <b>Reminder</b> and set the timing, for example 24 hours and 2 hours before.</li>
<li>Turn on <b>Follow-up</b> for after the appointment, and the <b>no-show</b> notification.</li>
<li>Add WhatsApp reminders with an approved template if you use the WhatsApp add-on.</li>
<li>Send yourself a test of each message, then save.</li>
</ol>
<p>Make sure your messages include the reschedule and cancel links, which come from the appointment itself.</p>"""),
 ],
 faqs=[
  ("How many reminders should I send?", "Two reminders work well for most businesses: one a day before and one an hour or two before. Add a confirmation at booking and a follow-up if they miss it."),
  ("Should reminders be SMS or email?", "Both. Email is good for details and calendar links; SMS gets read fastest, so use it for the final reminder. WhatsApp works well in countries where customers prefer it."),
  ("Can customers reschedule themselves?", "Yes. Reminders can include links that let customers reschedule or cancel without calling you."),
 ],
 related_ind=["dental-practices", "med-spas", "chiropractors-physiotherapy", "salons-barbershops", "gyms-fitness-studios", "lash-brow-nail-studios"],
 sources=[],
),
dict(
 slug="get-more-google-reviews", cat="Reviews",
 title="How to get more Google reviews automatically (without breaking the rules)",
 kw="How to Get More Google Reviews Automatically",
 desc="Most customers will leave a review if you ask at the right time. Here's how to automate Google review requests, what to say and what to avoid.",
 read=7,
 short="The simplest way to get more Google reviews is to ask every customer, at the moment they're happiest, with a direct link to your review page. Automate it: when a job is marked complete or an appointment is attended, send a short SMS or email with your review link. BrightLocal's 2026 survey found 83% of consumers who were asked to leave a review went on to write one. In Oceanic Funnels OS, connect your Google Business Profile and send review requests automatically from a workflow or manually from Reputation → Requests.",
 sections=[
  ("Why reviews matter more than ever", """
<p>BrightLocal's Local Consumer Review Survey 2026 found that 97% of consumers read reviews for local businesses, and 47% won't use a business with fewer than 20 reviews. Recency matters too: 74% only consider reviews from the last three months. A steady flow of new reviews beats a burst once a year.</p>
<p>Customers are also willing: 78% of people surveyed had been asked to leave a review in the last year, and 83% of those went on to write one.</p>"""),
  ("When to ask", """
<ul>
<li><b>Home services:</b> right after the job is marked complete.</li>
<li><b>Clinics, spas and salons:</b> a few hours after the appointment.</li>
<li><b>Coaches and agencies:</b> after a milestone or a win, not on day one.</li>
<li><b>Ecommerce:</b> after the product has arrived and been used.</li>
</ul>"""),
  ("What to say", """
<p>Keep it short and personal, with one link. For example:</p>
<p><i>"Hi Sarah, thanks for choosing Coastal Plumbing today. If you were happy with the job, would you leave us a quick Google review? It really helps a small business like ours: [link]"</i></p>"""),
  ("What not to do", """
<ul>
<li><b>Don't offer incentives for reviews.</b> Google's policies prohibit offering incentives in exchange for reviews.</li>
<li><b>Don't only ask happy customers.</b> Selectively soliciting positive reviews ("review gating") is against Google's policies. Ask everyone, and handle problems directly.</li>
<li><b>Don't set review quotas or ask for specific content.</b> Since April 2026, Google's policy also bars businesses from asking staff to collect a set number of reviews, or asking for reviews that include specific content, such as a staff member's name.</li>
<li><b>Don't write or buy fake reviews.</b> 97% of consumers in BrightLocal's survey think businesses should be punished for fake reviews.</li>
</ul>"""),
  ("Reply to every review", """
<p>The same survey found 89% of consumers expect owners to respond to reviews, and 50% are unlikely to choose a business that gives templated replies. Reply personally, thank people by name and address any issue calmly.</p>"""),
  ("How to automate review requests in Oceanic Funnels OS", """
<ol class="nf-steps-list">
<li>Connect your <b>Google Business Profile</b> in your settings, or add your review link.</li>
<li>Turn on review requests and customise your SMS and email messages.</li>
<li>Create a workflow triggered when a job is complete, an appointment is marked showed, or an order is fulfilled.</li>
<li>Add the <b>Send Review Request</b> action and choose SMS or email.</li>
<li>Track every request under <b>Reputation → Requests</b>, and send one-off requests from there too.</li>
</ol>"""),
 ],
 faqs=[
  ("Is it allowed to ask customers for Google reviews?", "Yes. Asking customers for reviews is fine. What Google prohibits is offering incentives for reviews and selectively asking only customers you expect to be positive."),
  ("SMS or email for review requests?", "SMS usually gets a faster response because people read texts quickly. Email works well as a reminder or for customers without a mobile number."),
  ("How many reviews do I need?", "BrightLocal's 2026 survey found 47% of consumers won't use a business with fewer than 20 reviews, and most only look at reviews from the last three months, so aim for a steady flow."),
 ],
 related_ind=["home-services", "dental-practices", "restaurants", "auto-repair-shops", "salons-barbershops", "plumbers"],
 sources=[("Local Consumer Review Survey 2026 (BrightLocal)", "https://brightlocal.com/research/local-consumer-review-survey/"),
          ("Prohibited and restricted content (Google Maps user contributed content policy)", "https://support.google.com/contributionpolicy/answer/7400114"),
          ("Google tightens Maps review policy, April 2026 (PPC Land)", "https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/")],
),
dict(
 slug="a2p-10dlc-registration", cat="Compliance",
 title="A2P 10DLC registration explained: how to get your business texting approved",
 kw="A2P 10DLC Registration Explained: Get Texting Approved",
 desc="To text customers from a US local number, you need A2P 10DLC registration. Here's what it is, what you need and how to avoid the most common rejections.",
 read=9,
 short="A2P 10DLC is the registration US carriers require for businesses that send text messages from software using a regular 10-digit local number. You register a brand (your business, with its legal name, EIN and website) and a campaign (what you'll text, how people opt in and sample messages). Most rejections come from mismatched business details, an unclear opt-in, or a website without a privacy policy that says mobile data isn't shared. Since June 30, 2026, new campaigns also need public privacy policy and terms URLs.",
 sections=[
  ("What A2P 10DLC means", """
<p><b>A2P</b> stands for application-to-person: texts sent from software rather than typed by a person on a phone. <b>10DLC</b> means a 10-digit long code, a normal local US phone number. US carriers require this traffic to be registered so they can confirm the sender is a real business and the recipients agreed to receive messages. Unregistered traffic is filtered or blocked.</p>
<p>Registration has three parts: a <b>brand</b> (who is sending), a <b>campaign</b> (what the messages are for) and connecting your numbers to the approved campaign.</p>"""),
  ("What you need before you start", """
<ul>
<li><b>Your legal business name and EIN</b> exactly as they appear on your IRS records.</li>
<li><b>Business address and contact details.</b></li>
<li><b>A live website</b> that matches your business name. Empty, unfinished or password-protected sites get rejected.</li>
<li><b>A privacy policy</b> that states mobile information and SMS opt-in data won't be shared or sold to third parties for marketing.</li>
<li><b>Terms and conditions</b> with your SMS program details.</li>
<li><b>An opt-in method</b> such as a website form with an unchecked SMS consent checkbox.</li>
</ul>
<p>Businesses without an EIN can register as a sole proprietor brand, which has lower limits. If you have an EIN, register as a standard brand.</p>"""),
  ("Writing a campaign that gets approved", """
<ul>
<li><b>Campaign description:</b> say who sends the messages, who receives them and why. "Appointment reminders and follow-ups for patients of Bloom Dental who booked online" works; "We send messages to customers" doesn't.</li>
<li><b>Opt-in (message flow):</b> describe exactly how people agree. Include the program name, message frequency, "message and data rates may apply", how to opt out (reply STOP) and links to your terms and privacy policy.</li>
<li><b>Sample messages:</b> realistic examples that include your business name and opt-out language.</li>
</ul>"""),
  ("Common rejection reasons", """
<ul>
<li>The business name or EIN doesn't match official records.</li>
<li>Registering as a sole proprietor when you have an EIN.</li>
<li>The website can't be verified or doesn't match the business.</li>
<li>Missing or vague opt-in description.</li>
<li>No privacy policy, or one that doesn't address sharing of mobile data.</li>
<li>A vague campaign description.</li>
</ul>"""),
  ("The 2026 change: privacy policy and terms URLs", """
<p>From June 30, 2026, new A2P 10DLC campaign submissions must include both a privacy policy URL and a terms and conditions URL, and both must be valid, publicly accessible pages. Existing approved campaigns aren't affected.</p>"""),
  ("Registering in Oceanic Funnels OS", """
<p>In Oceanic Funnels OS, go to <b>Settings → Phone Numbers → Trust Center</b>. The registration walks you through your business profile (legal name, tax ID and address), brand, campaign (use case and sample messages with opt-out language) and consent (how contacts opt in), then a review screen before you submit. Approval times vary, so start as soon as your website and policies are live. On the Growth and Done-For-You plans, text registration is part of the setup our team does for you, including your privacy policy and terms pages.</p>"""),
 ],
 faqs=[
  ("Do I need A2P 10DLC registration?", "If you send texts to US numbers from a local 10-digit business number using software, yes. Toll-free numbers use a separate toll-free verification process instead."),
  ("How long does A2P approval take?", "It varies with carrier review queues. Have your website, privacy policy, terms and opt-in ready before you submit, because resubmissions after a rejection add more time."),
  ("What should my privacy policy say about SMS?", "It should state that mobile information and SMS opt-in data will not be shared or sold to third parties or affiliates for marketing or promotional purposes."),
  ("Can I register without a website?", "Carriers need to verify your business online. A live website is strongly recommended; some providers accept public social media pages if a website isn't ready."),
 ],
 related_ind=["home-services", "real-estate", "dental-practices", "insurance-agencies", "gyms-fitness-studios", "auto-repair-shops"],
 sources=[("Improving your chances of A2P 10DLC registration approval (Twilio)", "https://www.twilio.com/en-us/blog/insights/best-practices/improving-your-chances-of-a2p10dlc-registration-approval"),
          ("A2P 10DLC campaign registration will require privacy policy and terms URLs (Twilio changelog)", "https://www.twilio.com/en-us/changelog/a2p-10dlc-campaign-registration-will-require-privacy-policy-and-")],
),
dict(
 slug="email-deliverability-spf-dkim-dmarc", cat="Compliance",
 title="Email deliverability for small business: SPF, DKIM, DMARC and the bulk sender rules",
 kw="Email Deliverability: SPF, DKIM, DMARC and Bulk Sender Rules",
 desc="Why your emails land in spam and how to fix it: SPF, DKIM and DMARC explained, Gmail, Yahoo and Outlook sender rules, and a setup checklist.",
 read=9,
 short="To land in the inbox, your sending domain needs three DNS records: SPF (which servers may send for you), DKIM (a signature proving the email wasn't altered) and DMARC (what to do with mail that fails). Gmail and Yahoo have required these for bulk senders since February 2024, and Outlook since May 2025, along with one-click unsubscribe and a spam complaint rate below 0.3%. In Oceanic Funnels OS, add a dedicated sending subdomain under Settings → Email Services → Sending Domain.",
 sections=[
  ("Why emails go to spam", """
<p>Mailbox providers decide where your email goes based on two things: whether they can prove it's really from you (authentication) and whether recipients want it (engagement and complaints). If either is weak, you land in spam or get rejected.</p>"""),
  ("SPF, DKIM and DMARC in plain English", """
<ul>
<li><b>SPF</b> is a DNS record listing the services allowed to send email for your domain. You can only have one SPF record per domain, and it's limited to 10 DNS lookups.</li>
<li><b>DKIM</b> adds a digital signature to every email. The matching public key sits in your DNS, so receivers can check the email wasn't forged or changed.</li>
<li><b>DMARC</b> tells receivers what to do when an email fails SPF or DKIM, and sends you reports. Start with <code>p=none</code> to monitor, then tighten to quarantine or reject once you're sure all legitimate mail passes.</li>
</ul>"""),
  ("The bulk sender rules", """
<p>Since February 2024, Gmail and Yahoo require anyone sending around 5,000 or more emails a day to their users to:</p>
<ul>
<li>Pass both SPF and DKIM, with a DMARC record (at least <code>p=none</code>) aligned with your From domain.</li>
<li>Offer one-click unsubscribe on marketing email and honour it within two days.</li>
<li>Keep the spam complaint rate below 0.3%, ideally under 0.1%.</li>
</ul>
<p>Outlook.com introduced similar requirements for high-volume senders in May 2025. Even if you send less, following these rules is the best way to reach the inbox.</p>"""),
  ("Use a dedicated sending subdomain", """
<p>Send marketing email from a subdomain such as <code>mail.yourbusiness.com</code>. It keeps your marketing reputation separate from your main domain, so a campaign that gets complaints doesn't affect your everyday email. Make sure the From address uses the same authenticated domain.</p>"""),
  ("Setup checklist in Oceanic Funnels OS", """
<ol class="nf-steps-list">
<li>Go to <b>Settings → Email Services → Sending Domain</b> and add a subdomain, such as mail.yourbusiness.com.</li>
<li>Add the DNS records shown (SPF, DKIM and others) at your domain provider, then verify.</li>
<li>Add a DMARC record with <code>p=none</code> and a reporting address.</li>
<li>Update your From address in campaigns and automations to use the authenticated domain.</li>
<li>Watch DMARC reports for 2 to 4 weeks before moving to quarantine or reject.</li>
</ol>"""),
  ("Habits that keep you in the inbox", """
<ul>
<li>Only email people who opted in. Never buy lists.</li>
<li>Remove contacts who bounce or haven't opened in months.</li>
<li>Send consistently instead of rare huge blasts.</li>
<li>Write like a person: clear subject lines, few links, no spammy phrases.</li>
</ul>"""),
 ],
 faqs=[
  ("Do I need DMARC if I send small volumes?", "It's strongly recommended. Major providers increasingly expect it from all senders, and it protects your domain from being spoofed."),
  ("Should I send from my main domain or a subdomain?", "Use a subdomain for marketing email. It protects the reputation of your main domain, which you use for everyday email."),
  ("What spam complaint rate is too high?", "Gmail and Yahoo require bulk senders to stay below 0.3%. Aim for under 0.1%."),
 ],
 related_ind=["ecommerce-brands", "course-creators", "coaches-consultants", "accountants-cpas", "financial-advisors", "nonprofits"],
 sources=[("Google and Yahoo sender requirements guide (Warmy)", "https://www.warmy.io/guides/google-yahoo-sender-requirements/")],
),
dict(
 slug="how-to-build-a-sales-funnel", cat="Sales funnels",
 title="How to build a sales funnel that converts: a step-by-step guide",
 kw="How to Build a Sales Funnel That Converts (Step-by-Step)",
 desc="A step-by-step guide to building a sales funnel: choose your offer, build the landing page, capture leads, follow up automatically and measure each step.",
 read=10,
 short="A sales funnel is the path a stranger takes to become a customer: they see your ad or content, land on a page with one clear offer, give their details, and get followed up until they buy or book. To build one: pick one offer and one audience, create a focused landing page, add a form or checkout, connect it to your CRM, automate instant follow-up by email and SMS, and measure the conversion rate at each step. The funnel page gets the lead; the automated follow-up closes the sale.",
 sections=[
  ("What a sales funnel is", """
<p>A sales funnel turns attention into customers in stages. Fewer people move through each stage, which is why it's drawn as a funnel. A simple version has four steps:</p>
<ol>
<li><b>Traffic:</b> ads, social posts, search, referrals.</li>
<li><b>Landing page:</b> one page, one offer, one action.</li>
<li><b>Conversion:</b> a form, booking or checkout.</li>
<li><b>Follow-up:</b> the automated emails, texts and calls that turn the lead into a customer.</li>
</ol>"""),
  ("Step 1: Choose one offer for one audience", """
<p>The most common funnel mistake is trying to sell everything to everyone. Pick one offer that's easy to say yes to: a free estimate, a trial class, a consultation, a guide, or a single product. Write down who it's for and what problem it solves.</p>"""),
  ("Step 2: Build a focused landing page", """
<ul>
<li><b>Headline</b> that states the outcome, not the feature.</li>
<li><b>Short proof:</b> reviews, results or credentials.</li>
<li><b>One call to action</b>, repeated down the page. Remove the menu and links that lead away.</li>
<li><b>Mobile first:</b> most visitors arrive on a phone.</li>
</ul>"""),
  ("Step 3: Capture the lead or the sale", """
<p>Use the lightest form that works: name, email and phone for a lead magnet, a calendar for a consultation, or a checkout for a product. For product funnels, a two-step order form with an <a href="/guides/order-bumps-and-upsells/">order bump and upsell</a> raises the value of every sale.</p>"""),
  ("Step 4: Connect it to your CRM and follow up automatically", """
<p>This is where most funnels leak. Every lead should land in your CRM and get an <a href="/guides/speed-to-lead/">instant reply</a>, then a short sequence over the next days. Add <a href="/guides/reduce-appointment-no-shows/">reminders</a> for bookings and an <a href="/guides/ai-chat-agent-for-business/">AI agent</a> to answer questions.</p>"""),
  ("Step 5: Measure and improve", """
<ul>
<li><b>Landing page conversion rate:</b> visitors who become leads.</li>
<li><b>Booking or sales rate:</b> leads who book or buy.</li>
<li><b>Cost per lead and cost per customer</b> if you run ads.</li>
</ul>
<p>Change one thing at a time, such as the headline or the offer, and compare.</p>"""),
  ("Building funnels in Oceanic Funnels OS", """
<p>Oceanic Funnels OS includes unlimited funnels and websites on every plan, with a drag-and-drop builder, forms, surveys, calendars, order forms and checkout, all connected to the CRM, email, SMS and automations. Build it yourself on the OS plan, or on Done-For-You our team builds your sales funnel and the automated backend for you. See <a href="/#pricing">pricing</a>.</p>"""),
 ],
 faqs=[
  ("What's the difference between a website and a sales funnel?", "A website has many pages for many purposes. A sales funnel is a focused path with one offer and one action, built to turn visitors into leads or customers."),
  ("How many pages does a sales funnel need?", "Often just one or two: a landing page and a thank-you or booking page. Product funnels may add an upsell page."),
  ("What's a good funnel conversion rate?", "It varies widely by offer, audience and traffic source. Measure your own baseline, then improve one step at a time."),
 ],
 related_ind=["coaches-consultants", "course-creators", "ecommerce-brands", "med-spas", "solar-installers", "real-estate"],
 sources=[],
),
dict(
 slug="database-reactivation", cat="Follow-up",
 title="Database reactivation: how to turn old leads into booked appointments",
 kw="Database Reactivation: Turn Old Leads into Booked Appointments",
 desc="Your old leads and past customers are your cheapest new sales. Here's how to run a database reactivation campaign by SMS and email, step by step.",
 read=7,
 short="Database reactivation is a campaign that contacts old leads and past customers who went quiet, with a simple, relevant message that invites a reply. Because these people already know you, it's usually the fastest and cheapest way to book new business. Clean your list, segment it, send a short personal message by SMS or email, let an AI agent or your team handle replies, and book them straight into your calendar.",
 sections=[
  ("Why reactivation works", """
<p>Every business has a list of people who enquired and didn't buy, or bought once and never came back. They already know your name. Many didn't say no; the timing was wrong. A good reactivation message reaches them when the timing might be right.</p>"""),
  ("Step 1: Get your list into one place", """
<p>Import old leads and past customers from spreadsheets, your old CRM or your booking system into your CRM. Only include people who gave you permission to contact them, and respect anyone who has opted out.</p>"""),
  ("Step 2: Segment", """
<ul>
<li><b>Old leads</b> who never bought.</li>
<li><b>Past customers</b> due for a repeat service.</li>
<li><b>Lapsed members</b> who cancelled.</li>
</ul>
<p>Each group gets a different message.</p>"""),
  ("Step 3: Write messages that get replies", """
<p>Short, personal and easy to answer. A question works better than an offer:</p>
<ul>
<li><i>"Hi James, it's Mia from Peak Fitness. Are you still looking to get back into training this year?"</i></li>
<li><i>"Hi Lisa, it's been about a year since your last check-up with Bright Smile Dental. Want me to find you a time this month?"</i></li>
</ul>
<p>Send in batches rather than all at once, so your team can handle the replies.</p>"""),
  ("Step 4: Handle replies fast", """
<p>Replies come in quickly after a reactivation message. An AI agent can answer and book appointments automatically, or your team can work through them in the unified inbox. Tag everyone who replies and move them into your pipeline.</p>"""),
  ("Step 5: Follow up and keep it running", """
<p>Send one or two follow-ups to people who didn't reply, then stop. Afterwards, turn reactivation into an always-on automation: anyone who hasn't booked in a set number of months gets a check-in automatically.</p>"""),
  ("Doing it in Oceanic Funnels OS", """
<p>Import your list, tag segments, and build a workflow that sends the SMS or email, waits for a reply and routes responders to your AI agent or team. Bookings go straight into your calendar with reminders. On Done-For-You, our team builds this for you as part of your backend.</p>"""),
 ],
 faqs=[
  ("Is it legal to text old leads?", "Only text people who have given you permission to contact them by text, and always include a way to opt out. Rules vary by country, so check what applies to you. In the US, your number must also be registered for business texting."),
  ("SMS or email for reactivation?", "SMS usually gets more replies because it's read quickly and feels personal. Email is a good second touch and works for people without mobile consent."),
  ("How often should I run reactivation?", "Run a one-off campaign to start, then keep an automated check-in running for anyone inactive for a set period, such as six months."),
 ],
 related_ind=["gyms-fitness-studios", "dental-practices", "med-spas", "real-estate", "auto-dealerships", "chiropractors-physiotherapy"],
 sources=[],
),
dict(
 slug="order-bumps-and-upsells", cat="Sales funnels",
 title="Order bumps and upsells: how to raise your average order value",
 kw="Order Bumps and Upsells: How to Raise Average Order Value",
 desc="Order bumps and one-click upsells increase how much each customer spends. Here's how they work, what to offer and how to set them up in your checkout.",
 read=6,
 short="An order bump is a small, related add-on offered with a checkbox on the checkout page, such as express shipping or a bonus guide. An upsell is a second offer shown right after purchase, often bought in one click without re-entering card details. Both raise average order value because they're offered when the customer has already decided to buy. Keep bumps cheap and closely related to the main product, and make upsells a natural next step.",
 sections=[
  ("Order bump vs upsell vs downsell", """
<ul>
<li><b>Order bump:</b> a tick-box add-on on the order form, before payment.</li>
<li><b>Upsell:</b> an offer on the page after purchase, accepted in one click.</li>
<li><b>Downsell:</b> a smaller alternative shown if they decline the upsell.</li>
</ul>"""),
  ("What makes a good order bump", """
<ul>
<li>Directly related to what they're buying.</li>
<li>A fraction of the main price, so it's an easy yes.</li>
<li>Explained in one or two sentences.</li>
</ul>
<p>Examples: an extra product refill, a bonus template pack with a course, priority booking with a service, or a gift wrap option.</p>"""),
  ("What makes a good upsell", """
<ul>
<li>The logical next step after the main purchase: the advanced course, the bundle, the done-for-you version.</li>
<li>A clear reason to buy now, such as a price only available on this page.</li>
<li>A one-click yes and an easy no.</li>
</ul>"""),
  ("Two-step order forms", """
<p>A two-step order form asks for contact details first, then payment. Because the contact is saved after step one, you can follow up with anyone who doesn't finish checkout, by email and SMS.</p>"""),
  ("Setting it up in Oceanic Funnels OS", """
<ol class="nf-steps-list">
<li>Add your products to the funnel step's products, and mark the add-on as a <b>Bump Product</b>.</li>
<li>Open the order form on the page, go to its advanced settings and open <b>Order bump options</b>.</li>
<li>Turn on <b>Order Bump</b>, choose the bump product and save.</li>
<li>Add an upsell step after the checkout step in the funnel for your one-click offer.</li>
</ol>
<p>Funnel checkouts in Oceanic Funnels OS support two-step order forms, order bumps and upsell pages after purchase. Abandoned checkouts can trigger an automatic follow-up sequence. On Done-For-You, our team builds the checkout and follow-up for you.</p>"""),
 ],
 faqs=[
  ("Do order bumps annoy customers?", "Not when they're relevant and inexpensive. A single, clearly described add-on is easy to skip and often welcome."),
  ("How many upsells should I offer?", "One upsell, and optionally one downsell, is usually enough. More than that can frustrate buyers."),
  ("Can I follow up with people who abandon checkout?", "Yes. With a two-step order form, contacts are saved after the first step, so you can send automatic reminders to those who don't complete payment."),
 ],
 related_ind=["ecommerce-brands", "course-creators", "coaches-consultants", "photographers", "car-detailing", "yoga-pilates-studios"],
 sources=[],
),
dict(
 slug="what-is-a-crm", cat="CRM",
 title="What is a CRM? A plain-English guide for small business owners",
 kw="What Is a CRM? A Plain-English Guide for Small Businesses",
 desc="A CRM keeps every customer, conversation and deal in one place and automates follow-up. Here's what a CRM does, what to look for and how to choose one.",
 read=8,
 short="A CRM (customer relationship management) system is one place that stores every contact, conversation, appointment and deal, so nothing falls through the cracks. A modern small business CRM also automates follow-up: it texts and emails leads, reminds customers about appointments, moves deals through a sales pipeline and asks for reviews. Look for unlimited contacts, built-in SMS and email, booking, payments and automations, so you're not paying for five separate tools.",
 sections=[
  ("What a CRM actually does", """
<ul>
<li><b>Contacts:</b> one record for each person with their details, history, tags and notes.</li>
<li><b>Conversations:</b> texts, emails, calls and social messages in one inbox.</li>
<li><b>Pipelines:</b> every deal or job tracked by stage, from new lead to won.</li>
<li><b>Tasks and reminders</b> for your team.</li>
<li><b>Automations</b> that send messages and update records for you.</li>
<li><b>Reports</b> on leads, sales and where they came from.</li>
</ul>"""),
  ("Signs you need one", """
<ul>
<li>Leads come from many places and some never get a reply.</li>
<li>You rely on memory, sticky notes or spreadsheets to follow up.</li>
<li>Your team doesn't know who spoke to which customer.</li>
<li>You pay for separate tools for email, texting, booking and invoicing.</li>
</ul>"""),
  ("What to look for in a small business CRM", """
<ul>
<li><b>Pricing that doesn't punish growth.</b> Many CRMs charge per contact or per user; unlimited is better.</li>
<li><b>Built-in texting and email,</b> including two-way SMS.</li>
<li><b>Booking and reminders</b> connected to the contact record.</li>
<li><b>Payments and invoices.</b></li>
<li><b>Automation</b> you can set up without a developer.</li>
<li><b>Funnels and forms</b> that feed leads straight in.</li>
<li><b>Help setting it up,</b> because an empty CRM doesn't help anyone.</li>
</ul>"""),
  ("All-in-one vs a stack of tools", """
<p>Many businesses glue together a CRM, an email tool, a texting tool, a scheduler and a funnel builder. Each one has its own bill and login, and leads slip through the gaps between them. An all-in-one system keeps everything connected. See the <a href="/#all-in-one">tools Oceanic Funnels OS replaces</a> and what they'd cost separately.</p>"""),
  ("Oceanic Funnels OS as your CRM", """
<p>Oceanic Funnels OS includes the CRM, pipelines, unified inbox, email, two-way SMS, AI agents, calendars, payments, reviews and unlimited funnels, with unlimited contacts and users from $67 a month. On Growth, our team sets it up for you in the first week. See how it works for <a href="/industries/">your industry</a>.</p>"""),
 ],
 faqs=[
  ("What does CRM stand for?", "Customer relationship management. It's the system a business uses to keep track of contacts, conversations, deals and follow-up."),
  ("Is a CRM worth it for a small business?", "If you're losing leads, following up inconsistently or paying for several separate tools, a CRM usually pays for itself by recovering just a few sales a month."),
  ("What's the difference between a CRM and a spreadsheet?", "A spreadsheet stores data. A CRM also holds the conversations, sends messages, books appointments, tracks deals and automates follow-up."),
 ],
 related_ind=["home-services", "real-estate", "coaches-consultants", "law-firms", "insurance-agencies", "accountants-cpas"],
 sources=[],
),
]
