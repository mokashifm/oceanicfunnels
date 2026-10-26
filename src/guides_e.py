"""Guides part E: getting paid, contracts, courses, communities, affiliates and webinars."""

G_E = [
dict(
 slug="estimates-invoices-text-to-pay", cat="Ecommerce and payments",
 title="Estimates, invoices and text-to-pay: get paid faster",
 kw="Estimates, Invoices and Text-to-Pay: How to Get Paid Faster",
 desc="Send estimates customers can accept online, turn them into invoices, and collect payment by text with a secure pay link.",
 read=7,
 short="To get paid faster, send estimates customers can accept online, turn accepted estimates into invoices, and let customers pay by card from a link sent by text. In Oceanic Funnels OS, estimates and invoices live under Payments → Invoices & Estimates, payment links under Payments → Payment Links, and text-to-pay is sent straight from a conversation using the $ icon. You need a connected payment provider, such as Stripe.",
 sections=[
  ("Estimates customers can accept online", """
<ol class="nf-steps-list">
<li>Go to <b>Payments → Invoices &amp; Estimates</b> and open <b>Estimates</b>.</li>
<li>Click <b>New</b>, add your business and customer details, estimate number and expiry date.</li>
<li>Add products or services and send by email or SMS.</li>
<li>The customer accepts or declines online, and can add notes. If they confirm by phone, mark it accepted yourself.</li>
<li>Once accepted, create the invoice from the estimate in one click.</li>
</ol>
<p>The estimates dashboard shows totals by status (draft, sent, accepted, declined, invoiced), so you can see what's waiting.</p>"""),
  ("Invoices", """
<ol class="nf-steps-list">
<li>Go to <b>Payments → Invoices</b> and click <b>New</b>.</li>
<li>Add the customer, invoice number, issue date and due date.</li>
<li>Add line items from your products, plus taxes and any discount.</li>
<li>Send by email or text. Track status and payments in the invoices list and under <b>Payments → Transactions</b>.</li>
</ol>
<p>Recurring invoices are available for retainers and monthly services.</p>"""),
  ("Text-to-pay", """
<p>Open the customer's conversation, choose SMS, click the <b>$</b> icon, pick the product and amount, and send. The customer gets a secure checkout link and pays by card from their phone. It's ideal for paying at the end of a job.</p>"""),
  ("Payment links", """
<p>Create a reusable link under <b>Payments → Payment Links</b> for a product, and share it anywhere: messages, emails, social bios, QR codes. No website needed.</p>"""),
  ("Automate the follow-up", """
<p>Use workflows to remind customers about unpaid invoices and open estimates, and to send a <a href="/guides/get-more-google-reviews/">review request</a> once payment is received.</p>"""),
 ],
 faqs=[
  ("What do I need to take card payments?", "A connected payment provider, such as Stripe. Text-to-pay also needs an active phone number."),
  ("Can customers accept estimates online?", "Yes. Customers can accept or decline estimates online, and accepted estimates can be turned into invoices."),
  ("Can I send recurring invoices?", "Yes. Recurring invoices are available for retainers and monthly services."),
 ],
 related_ind=["home-services", "plumbers", "electricians", "contractors-remodelers", "auto-repair-shops", "cleaning-services"],
 sources=[],
),
dict(
 slug="contracts-e-signature", cat="Ecommerce and payments",
 title="How to send contracts for e-signature (and get paid when they sign)",
 kw="Send Contracts for E-Signature and Get Paid When They Sign",
 desc="Create contract templates, send documents for e-signature, add multiple signers, collect payment at signing and automate follow-up.",
 read=6,
 short="With Documents & Contracts in Oceanic Funnels OS (Payments → Documents & Contracts), you create a document or reusable template, add signature, initials, date and text fields, assign each field to a signer, and send it by email or a shareable link. You can add products to collect a one-time or recurring payment at signing. Track every document as draft, waiting for others or completed, and trigger workflows when it's viewed or signed.",
 sections=[
  ("What you can send", """
<ul>
<li>Service agreements and engagement letters.</li>
<li>Proposals with pricing and a sign-and-pay option.</li>
<li>Waivers, consent forms and policies.</li>
<li>Change orders and statements of work.</li>
</ul>"""),
  ("Create and send a contract", """
<ol class="nf-steps-list">
<li>Go to <b>Payments → Documents &amp; Contracts</b>.</li>
<li>Create a document from scratch or a template. Reuse blocks from the content library.</li>
<li>Add fields: signature, initials, date, text and checkboxes. Set <b>To be signed by</b> for each field.</li>
<li>Add text, images, video, tables or a product list. Add a payment to collect at signing if needed.</li>
<li>For several signers, add recipients and choose sequential or simultaneous signing.</li>
<li>Send by email or share via link. Set an expiry date if the offer is time-limited.</li>
</ol>"""),
  ("Track and follow up", """
<p>The dashboard shows Draft, Waiting for others, Completed and Payments tabs. Resend to remind signers, and use workflow triggers for created, sent, viewed and signed documents, for example to start onboarding the moment a contract is signed.</p>"""),
  ("Turn your contract into a template", """
<p>Save a finished contract as a template, so next time you only change the client details. Editing a template doesn't change documents already sent.</p>"""),
 ],
 faqs=[
  ("Can more than one person sign?", "Yes. Add multiple recipients, assign fields to each and choose whether they sign in order or at the same time."),
  ("Can I collect payment when the contract is signed?", "Yes. Add one-time or recurring payments to the document and collect at signing."),
  ("Can contracts be sent automatically?", "Yes. Workflows can send document templates automatically, for example when a deal moves to Won."),
 ],
 related_ind=["contractors-remodelers", "law-firms", "event-venues-wedding-vendors", "photographers", "property-management", "accountants-cpas"],
 sources=[],
),
dict(
 slug="create-and-sell-an-online-course", cat="Courses and communities",
 title="How to create and sell an online course (without a separate course platform)",
 kw="How to Create and Sell an Online Course Without a Course Platform",
 desc="Build your course with modules and lessons, set up drip content, create offers and pricing, and sell with a funnel, all in one system.",
 read=8,
 short="To create and sell an online course in Oceanic Funnels OS, go to Sites → Memberships, create a product (your course), add categories (modules) and lessons with video, text and downloads, and set drip schedules if you want lessons to unlock over time. Then create an offer with a one-time or subscription price, connect it to a checkout in a funnel, and buyers get access automatically in your branded membership portal. Communities can be added for student discussion.",
 sections=[
  ("Plan your course", """
<ul>
<li><b>One clear outcome:</b> what students can do by the end.</li>
<li><b>Modules</b> for each stage of the journey.</li>
<li><b>Short lessons,</b> 5 to 15 minutes each, with a task or download.</li>
</ul>"""),
  ("Build it", """
<ol class="nf-steps-list">
<li>Go to <b>Sites → Memberships</b> and open <b>Products</b>. Create a new product from a template, with a name, thumbnail and description.</li>
<li>Add categories (modules) and drag them into order.</li>
<li>Add lessons with video, text and files.</li>
<li>Set each lesson's visibility, drip schedule, comments and SEO details.</li>
<li>Brand the membership portal with your logo, colours and domain.</li>
</ol>"""),
  ("Price and sell it", """
<ol class="nf-steps-list">
<li>Under <b>Offers</b>, create an offer containing one or more products.</li>
<li>Choose a one-time price or a subscription, with currency and billing cycle.</li>
<li>Connect the offer to an order form in a <a href="/guides/how-to-build-a-sales-funnel/">sales funnel</a>, with an optional <a href="/guides/order-bumps-and-upsells/">order bump</a>.</li>
<li>Buyers get access automatically, and you can manage, adjust or revoke access under <b>Members</b>.</li>
</ol>"""),
  ("Launch and grow", """
<ul>
<li>Build an email list with a free lesson or <a href="/guides/run-a-webinar/">webinar</a> before launch.</li>
<li>Add a <a href="/guides/paid-online-community/">community</a> so students learn together.</li>
<li>Run an <a href="/guides/affiliate-referral-program/">affiliate program</a> to have students promote it.</li>
</ul>"""),
 ],
 faqs=[
  ("Can lessons unlock over time?", "Yes. Use drip schedules to control when lessons become available after someone joins."),
  ("Can I sell a subscription membership?", "Yes. Offers can be one-time purchases or recurring subscriptions."),
  ("Is course hosting included?", "Yes. Courses, memberships and communities are included on every plan."),
 ],
 related_ind=["course-creators", "coaches-consultants", "personal-trainers", "yoga-pilates-studios", "tutoring-learning-centers", "lash-brow-nail-studios"],
 sources=[],
),
dict(
 slug="paid-online-community", cat="Courses and communities",
 title="How to build a paid online community: a Skool alternative inside your CRM",
 kw="Build a Paid Online Community: A Skool Alternative in Your CRM",
 desc="Create a free or paid online community with groups, channels, events, courses and leaderboards, connected to your CRM and payments.",
 read=7,
 short="An online community gives your customers, students or members a place to talk, learn and stay engaged. In Oceanic Funnels OS, communities include groups, channels, posts, events with reminders, courses inside the group, and gamification with levels, a leaderboard and rewards. You can run free or paid groups, invite members with roles, and connect everything to your CRM and automations, so it works like Skool but lives next to your funnels, email and payments.",
 sections=[
  ("Why build your community here", """
<ul>
<li>Members, payments, courses and email in one system.</li>
<li>Automations can welcome new members, reward activity and win back quiet ones.</li>
<li>Your own branding and domain.</li>
<li>Unlimited contacts, so you aren't charged more as you grow.</li>
</ul>"""),
  ("Set up your community", """
<ol class="nf-steps-list">
<li>Open <b>Communities</b> and create a new community. Connect a custom domain in the community settings.</li>
<li>In <b>Groups</b>, click <b>Create Group</b>, add a name, description and privacy (public or private), and assign moderators.</li>
<li>Add channels with <b>+ Add Channel</b>, such as Announcements, Wins and Questions.</li>
<li>In <b>Learning</b>, click <b>+ Add Course</b> to attach a course, visible to everyone, certain levels, or unlocked by time or milestones.</li>
<li>In <b>Events</b>, create one-time or recurring sessions with a meeting link and reminders.</li>
<li>Invite members from <b>Members</b> and set roles: Admin, Contributor or Member.</li>
</ol>"""),
  ("Make it paid", """
<p>Connect a paid membership offer so people pay to join, monthly or one-time. Combine with a <a href="/guides/how-to-build-a-sales-funnel/">sales page funnel</a> and checkout.</p>"""),
  ("Keep members engaged", """
<ul>
<li><b>Gamification:</b> members earn points for posts, comments and likes, and level up on the leaderboard.</li>
<li><b>Rewards:</b> unlock courses, discounts or roles at certain levels.</li>
<li><b>Weekly rhythm:</b> one live call, one challenge and one win thread every week.</li>
</ul>"""),
 ],
 faqs=[
  ("Can I charge for my community?", "Yes. Connect paid membership plans so members pay to join."),
  ("Can I add courses inside the community?", "Yes. Attach courses in the Learning tab and choose who can see them."),
  ("Does it have a leaderboard?", "Yes. Members earn points for activity, level up on a leaderboard and can unlock rewards."),
 ],
 related_ind=["course-creators", "coaches-consultants", "personal-trainers", "churches", "soccer-clubs-academies", "nonprofits"],
 sources=[],
),
dict(
 slug="affiliate-referral-program", cat="Marketing",
 title="How to run an affiliate or referral program that tracks every sale",
 kw="Run an Affiliate or Referral Program That Tracks Every Sale",
 desc="Set up an affiliate program with pay-per-lead or pay-per-sale commissions, tracking links, an affiliate portal and payouts.",
 read=6,
 short="An affiliate program pays partners or customers for the leads and sales they send you. With the affiliate manager in Oceanic Funnels OS, you create a campaign, choose pay-per-lead or pay-per-sale commissions (flat, percentage or recurring), and enrol affiliates, who each get tracking links and an affiliate portal showing their leads, customers, commissions and payouts. You approve commissions and pay through PayPal or manually.",
 sections=[
  ("Affiliate vs referral program", """
<ul>
<li><b>Affiliates:</b> partners, influencers or other businesses who promote you to their audience.</li>
<li><b>Referrals:</b> happy customers who send friends.</li>
</ul>
<p>The same system handles both; only the reward changes.</p>"""),
  ("Choose your commission model", """
<ul>
<li><b>Pay per lead:</b> reward form submissions, surveys or bookings. Good for service businesses.</li>
<li><b>Pay per sale:</b> a flat amount or a percentage of the sale.</li>
<li><b>Recurring:</b> a share of every subscription payment. Good for memberships and courses.</li>
</ul>"""),
  ("Set it up", """
<ol class="nf-steps-list">
<li>Create a campaign and choose its source: the funnel, form, calendar or product it tracks.</li>
<li>Set the commission model and amounts.</li>
<li>Enrol affiliates. Each gets campaign-specific tracking links.</li>
<li>Affiliates log in to their portal to get links and see leads, customers, commissions and payouts.</li>
<li>Review and approve commissions, then pay through PayPal automatically or manually by bank transfer or another method.</li>
</ol>"""),
  ("Tips", """
<ul>
<li>Make the reward easy to understand.</li>
<li>Give affiliates ready-made posts, emails and images.</li>
<li>Ask happy customers right after a great result, the same moment you'd <a href="/guides/get-more-google-reviews/">ask for a review</a>.</li>
</ul>"""),
 ],
 faqs=[
  ("Can I pay affiliates per lead instead of per sale?", "Yes. Pay-per-lead commissions reward eligible form submissions, surveys or bookings."),
  ("Do affiliates get their own dashboard?", "Yes. The affiliate portal shows their links, leads, customers, commissions and payouts."),
  ("How are affiliates paid?", "You approve commissions, then pay automatically through PayPal or manually by bank transfer or another method."),
 ],
 related_ind=["course-creators", "coaches-consultants", "ecommerce-brands", "solar-installers", "gyms-fitness-studios", "real-estate"],
 sources=[],
),
dict(
 slug="run-a-webinar", cat="Sales funnels",
 title="How to run a webinar that sells: live and on-demand webinar funnels",
 kw="How to Run a Webinar That Sells: Live and On-Demand Funnels",
 desc="Set up a live or on-demand webinar funnel with registration, reminders and follow-up, so more people attend and buy.",
 read=7,
 short="A webinar funnel has three parts: a registration page, reminders that get people to show up, and follow-up that turns attendees into customers. In Oceanic Funnels OS, go to Sites → Webinars → New Webinar Funnel and choose a live webinar (set date and time) or an on-demand webinar (a pre-recorded video people watch any time). Registrations go into your CRM, and automations send confirmations, reminders and follow-ups.",
 sections=[
  ("Live or on-demand?", """
<ul>
<li><b>Live:</b> attendees join at a set time. Great for launches, Q&amp;A and workshops. Stream through Zoom, YouTube Live or another link.</li>
<li><b>On-demand:</b> a recorded webinar people watch after registering. Great for evergreen lead generation that runs every day.</li>
</ul>"""),
  ("Set it up", """
<ol class="nf-steps-list">
<li>Go to <b>Sites → Webinars</b> and click <b>New Webinar Funnel</b>.</li>
<li>Choose <b>Live Webinar</b> (name, timezone, date and time) or <b>On-Demand Webinar</b> (name and video).</li>
<li>Connect a registration form. Every registrant becomes a contact.</li>
<li>Customise the registration, confirmation and broadcast pages.</li>
<li>Set reminders by email and SMS, commonly 24 hours, 1 hour and 10 minutes before.</li>
<li>Build the follow-up: replay, offer and a booking link.</li>
</ol>"""),
  ("Structure a webinar that converts", """
<ol>
<li>Promise one specific outcome in the title.</li>
<li>Teach something genuinely useful for 30 to 40 minutes.</li>
<li>Show proof: results, examples, case studies.</li>
<li>Make one clear offer with a deadline.</li>
<li>Answer questions live.</li>
</ol>"""),
  ("Follow up", """
<p>Send the replay and offer to everyone, then a short sequence over the next few days. Tag attendees and non-attendees separately so each gets the right message.</p>"""),
 ],
 faqs=[
  ("Can I run an automated webinar?", "Yes. On-demand webinars play a pre-recorded video that people watch any time after registering."),
  ("Can I stream with Zoom or YouTube?", "Yes. Live webinars can use a streaming link from Zoom, YouTube Live or other platforms."),
  ("Do registrants go into my CRM?", "Yes. Every registration creates a contact and can start a workflow for reminders and follow-up."),
 ],
 related_ind=["coaches-consultants", "course-creators", "financial-advisors", "real-estate", "mortgage-brokers", "solar-installers"],
 sources=[],
),
]
