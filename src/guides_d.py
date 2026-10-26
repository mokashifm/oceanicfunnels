"""Guides part D: CRM, automation, calendars, marketing and reporting."""

G_D = [
dict(
 slug="workflow-automation", cat="Automation",
 title="Workflow automation for small business: triggers, actions and recipes",
 kw="Workflow Automation for Small Business: Triggers, Actions, Recipes",
 desc="How workflow automation works: triggers, actions, if/else branches and ready-made recipes, plus the first five automations every business should build.",
 read=9,
 short="A workflow is an automated sequence that starts when something happens (a trigger) and then runs steps for you (actions). For example: when a form is submitted, send a text, create an opportunity, assign it to a salesperson and remind them to call. In Oceanic Funnels OS you can build a workflow with AI, start from a ready-made template, or build from scratch: add a trigger, add actions, use if/else branches for different paths, test it with a fresh contact and publish.",
 sections=[
  ("Triggers, actions and branches", """
<ul>
<li><b>Triggers</b> start a workflow: form submitted, appointment booked, tag added, payment received, call status, quiz or survey submitted and many more. A workflow can have several triggers, and filters narrow when they fire.</li>
<li><b>Actions</b> are the steps: send an SMS, email or WhatsApp, update the contact, add a tag, create or move an opportunity, assign a user, create a task, send a review request, wait, and more.</li>
<li><b>If/else branches</b> split contacts into different paths based on conditions, such as whether they booked or which service they chose.</li>
</ul>"""),
  ("Three ways to build", """
<ol>
<li><b>Build with AI:</b> describe what you want in plain English and the builder drafts the workflow.</li>
<li><b>Templates (recipes):</b> pre-built workflows you can use as-is or customise.</li>
<li><b>From scratch:</b> add each trigger and action yourself.</li>
</ol>"""),
  ("The first five workflows every business needs", """
<ol class="nf-steps-list">
<li><b>New lead follow-up:</b> instant text and email, team notification and a follow-up sequence. See <a href="/guides/speed-to-lead/">speed to lead</a>.</li>
<li><b>Missed call text back:</b> covered in <a href="/guides/missed-call-text-back/">this guide</a>.</li>
<li><b>Appointment confirmations and reminders:</b> see <a href="/guides/reduce-appointment-no-shows/">reducing no-shows</a>.</li>
<li><b>Review request after the job or visit:</b> see <a href="/guides/get-more-google-reviews/">getting more reviews</a>.</li>
<li><b>Reactivation:</b> check in with anyone inactive for a set time. See <a href="/guides/database-reactivation/">database reactivation</a>.</li>
</ol>"""),
  ("Testing and troubleshooting", """
<ul>
<li>Test with a fresh contact that hasn't been through the workflow before.</li>
<li>Make sure the test contact meets the trigger conditions and filters.</li>
<li>Check whether the workflow allows contacts to enter more than once if you expect repeats.</li>
<li>Use the execution logs to see which steps ran, were skipped or failed.</li>
</ul>"""),
  ("Keep automations human", """
<p>Write messages the way you'd text a customer yourself, stop sequences when someone replies or books, and always make it easy to reach a person.</p>"""),
 ],
 faqs=[
  ("Do I need technical skills to build workflows?", "No. Workflows use a visual builder, ready-made templates and an AI builder that drafts workflows from a plain-English description."),
  ("Can one workflow have more than one trigger?", "Yes. You can add several triggers to one workflow and use filters to control when each fires."),
  ("Will you build my workflows?", "On Growth, our team installs five core automations in your first week. On Done-For-You, we build your full automated backend."),
 ],
 related_ind=["home-services", "real-estate", "coaches-consultants", "gyms-fitness-studios", "med-spas", "insurance-agencies"],
 sources=[],
),
dict(
 slug="import-contacts-smart-lists", cat="CRM",
 title="How to import your contacts and organise them with smart lists",
 kw="How to Import Contacts (CSV) and Organise Them with Smart Lists",
 desc="Move your customer list into your CRM from a CSV file, map fields, avoid duplicates, then segment contacts with tags and smart lists.",
 read=6,
 short="To import contacts into Oceanic Funnels OS, export them to a single-sheet CSV with a header row, then go to Contacts → Smart Lists → Import Contacts. Map each column to a field, choose whether to update existing contacts or create new ones, add a tag for the import, and optionally add everyone to a workflow or a new smart list. Existing contacts are matched by email first, then phone. Track progress under Bulk Actions.",
 sections=[
  ("Prepare your file", """
<ul>
<li>Save as a <b>.csv</b> with a single sheet.</li>
<li>Keep it under 30MB; split larger files.</li>
<li>Row 1 must be headers, such as First Name, Email, Phone.</li>
<li>Each row needs at least a name, email or phone.</li>
<li>Clean phone numbers: remove spaces, dashes and letters.</li>
<li>Remove duplicates inside the file first.</li>
</ul>"""),
  ("Import step by step", """
<ol class="nf-steps-list">
<li>Go to <b>Contacts → Smart Lists</b> and click <b>Import Contacts</b>. (To import deals too, start from <b>Opportunities → Import</b>.)</li>
<li>Upload your CSV and choose what to import: contacts, opportunities or both.</li>
<li>Map each column to a field. Leave columns unmapped to skip them.</li>
<li>Tick <b>Don't update Empty Values</b> so blank cells don't overwrite existing data.</li>
<li>Choose <b>Update Only</b> or <b>Create &amp; Update</b> for how matches are handled.</li>
<li>Add a tag such as "imported-oct-2026", and optionally add the contacts to a workflow or a new smart list.</li>
<li>Confirm and start the import. Track it under <b>Bulk Actions</b> and download the error log to fix failed rows.</li>
</ol>"""),
  ("Organise with tags and smart lists", """
<p><b>Tags</b> label contacts: customer, lead, VIP, service type, source. <b>Smart lists</b> are saved filters that update automatically, such as "customers who haven't booked in 6 months" or "leads from Facebook this month". Use them to send targeted campaigns and to start <a href="/guides/database-reactivation/">reactivation</a>.</p>"""),
  ("Respect consent", """
<p>Only text or email people who agreed to hear from you, and keep opt-outs from your old system. In the US, texting also requires <a href="/guides/a2p-10dlc-registration/">A2P 10DLC registration</a>.</p>"""),
 ],
 faqs=[
  ("How are duplicate contacts handled?", "Existing contacts are matched by email first, then phone. Choose Update Only or Create & Update to control what happens to matches."),
  ("Can I import deals or opportunities?", "Yes. Import contacts and opportunities together from Opportunities → Import. Each opportunity needs a matching contact and an owner who exists as a user."),
  ("Will you import my contacts for me?", "On Growth and Done-For-You, our team does the import for you."),
 ],
 related_ind=["real-estate", "dental-practices", "gyms-fitness-studios", "insurance-agencies", "accountants-cpas", "nonprofits"],
 sources=[],
),
dict(
 slug="sales-pipeline-management", cat="CRM",
 title="Sales pipeline management: track every deal from new lead to won",
 kw="Sales Pipeline Management: Track Every Deal from Lead to Won",
 desc="How to set up a sales pipeline with stages that match your process, add opportunities automatically and stop deals from slipping through.",
 read=6,
 short="A sales pipeline shows every potential deal (opportunity) as a card in a stage, such as New Lead, Contacted, Booked, Quote Sent and Won. It shows what to do next and how much revenue is in play. In Oceanic Funnels OS, create one under Opportunities → Pipelines → Create New Pipeline, name your stages, then use workflows to create and move opportunities automatically when forms are submitted, calls booked or payments received.",
 sections=[
  ("Design stages that match how you sell", """
<p>Each stage should describe where the customer is, not what you hope will happen. Examples:</p>
<ul>
<li><b>Service business:</b> New Lead → Contacted → Estimate Booked → Estimate Sent → Won → Lost.</li>
<li><b>Coach or consultant:</b> New Lead → Call Booked → No Show → Proposal Sent → Won → Lost.</li>
<li><b>Real estate:</b> New → Contacted → Showing → Offer → Under Contract → Closed.</li>
</ul>"""),
  ("Set it up", """
<ol class="nf-steps-list">
<li>Go to <b>Opportunities → Pipelines</b> and click <b>Create New Pipeline</b>.</li>
<li>Name the pipeline and add your stages, then save.</li>
<li>Add opportunities manually with <b>Add opportunity</b>, in bulk with <b>Import</b>, or automatically with workflows.</li>
<li>Give each opportunity a value so you can see revenue by stage.</li>
</ol>"""),
  ("Automate the pipeline", """
<p>In a workflow, add a trigger such as Form Submitted, Customer Booked Appointment or Payment Received, then the <b>create or update opportunity</b> action with the pipeline, stage, status and value. Turn on <b>Allow Opportunity to Move</b> so the same deal moves forward instead of being duplicated.</p>"""),
  ("Keep it clean", """
<ul>
<li>Every opportunity has an owner and a next step.</li>
<li>Mark deals as lost with a reason, instead of leaving them to rot.</li>
<li>Review the pipeline weekly with your team.</li>
</ul>"""),
 ],
 faqs=[
  ("What is an opportunity?", "An opportunity is a potential deal linked to a contact, with a pipeline stage, status and value."),
  ("Can I have more than one pipeline?", "Yes. Many businesses use separate pipelines, for example for new sales, renewals or different services."),
  ("Can opportunities move automatically?", "Yes. Workflows can create opportunities and move them between stages when contacts book, pay, reply or submit forms."),
 ],
 related_ind=["real-estate", "insurance-agencies", "roofing", "solar-installers", "law-firms", "recruiting-staffing"],
 sources=[],
),
dict(
 slug="online-booking-calendars", cat="Booking",
 title="Online booking calendars: personal, round robin, class and service booking",
 kw="Online Booking Calendar Types: Round Robin, Class and Service",
 desc="Which booking calendar type to use: personal, round robin, collective, class or service menu, and how to set reminders and payments.",
 read=6,
 short="Online booking calendars let customers book themselves into your schedule. Oceanic Funnels OS includes several types: personal calendars for one person, round robin to share bookings across a team, collective for meetings that need several people, class booking for group sessions with limited spots, and service calendars for businesses with service menus, staff, add-ons and staff-specific pricing. Each calendar has its own notifications for confirmations, reminders and follow-ups.",
 sections=[
  ("Which calendar type do you need?", """
<ul>
<li><b>Personal:</b> one person's availability. Consultants, coaches, solo practitioners.</li>
<li><b>Round robin:</b> bookings shared across a team so leads are spread fairly. Sales teams, agents, multi-staff clinics.</li>
<li><b>Collective:</b> only shows times when everyone required is free. Joint consultations.</li>
<li><b>Class:</b> one session, many attendees, limited seats. Fitness classes, workshops, trial sessions.</li>
<li><b>Service menu and service calendars:</b> customers pick a service, add-ons and staff member. Salons, spas, clinics, detailers.</li>
</ul>"""),
  ("Set up for fewer no-shows", """
<p>Every calendar has notifications for booked, rescheduled, cancelled, reminder and follow-up messages by email, SMS and WhatsApp. Our <a href="/guides/reduce-appointment-no-shows/">no-show guide</a> shows the sequence that works.</p>"""),
  ("Take payment or a deposit", """
<p>For high-value or often-missed appointments, take a payment or deposit when the customer books.</p>"""),
  ("Where to put your calendar", """
<ul>
<li>On your website and funnels as an embedded booking widget.</li>
<li>As a link in your instant replies, emails and social bios.</li>
<li>Inside your <a href="/guides/ai-chat-agent-for-business/">AI agent</a>, so it can book during the conversation.</li>
</ul>"""),
 ],
 faqs=[
  ("Can customers reschedule themselves?", "Yes. Confirmation and reminder messages can include links to reschedule or cancel."),
  ("Can I sync with Google or Outlook calendars?", "Yes. Calendar integrations let you connect your existing calendar so bookings respect your real availability."),
  ("Can different staff have different prices?", "Yes. Service calendars support staff-specific pricing, variations and add-ons."),
 ],
 related_ind=["salons-barbershops", "med-spas", "gyms-fitness-studios", "yoga-pilates-studios", "real-estate", "lash-brow-nail-studios"],
 sources=[],
),
dict(
 slug="marketing-reporting-dashboards", cat="Reporting",
 title="Marketing reporting: dashboards that show where your customers come from",
 kw="Marketing Reporting Dashboards: Leads, Calls, Ads and Revenue",
 desc="How to set up dashboards and reports that show leads, calls, ad spend, bookings and revenue, so you know which marketing actually works.",
 read=6,
 short="Good marketing reporting answers three questions: how many leads came in, where they came from, and how many became paying customers. In Oceanic Funnels OS, dashboards show leads, opportunities, appointments, calls and revenue at a glance, and you can add widgets such as Meta ad spend, clicks, CPC and conversions. Custom reports (Reporting → Custom Reports) package these into reports you can send or schedule by email.",
 sections=[
  ("What to track", """
<ul>
<li><b>Leads</b> by source: Google, Facebook, referrals, organic.</li>
<li><b>Speed to lead</b> and response rate.</li>
<li><b>Appointments</b> booked, shown and no-shows.</li>
<li><b>Opportunities</b> and pipeline value by stage.</li>
<li><b>Revenue</b> and cost per customer.</li>
<li><b>Calls</b> by source, with <a href="/guides/call-tracking/">call tracking</a>.</li>
</ul>"""),
  ("Dashboards vs custom reports", """
<p><b>Dashboards</b> are for at-a-glance checks during the day. Add widgets from the dashboard's edit mode, including Meta Ads metrics once your ad account is connected. <b>Custom reports</b> are for packaged insights: go to <b>Reporting → Custom Reports</b>, add widgets, save, then send or schedule them by email.</p>"""),
  ("Make attribution work", """
<ul>
<li>Use UTM parameters on every ad and social link.</li>
<li>Send traffic to forms, funnels and calendars inside the system, so the source is captured on the contact.</li>
<li>Use <a href="/guides/call-tracking/">call tracking numbers</a> for ads and print.</li>
</ul>"""),
  ("Review weekly", """
<p>Look at the same few numbers every week: leads, booked, shown, won, revenue, cost. When one drops, you know which step to fix.</p>"""),
 ],
 faqs=[
  ("Can I see Facebook ad results in my dashboard?", "Yes. Connect your Meta ad account and add Meta Ads widgets for spend, clicks, conversions, CPC and more."),
  ("Can I email reports automatically?", "Yes. Custom reports can be sent or scheduled by email."),
  ("Does Done-For-You include reporting?", "Growth includes a monthly strategy call and report, and Done-For-You includes everything in Growth."),
 ],
 related_ind=["home-services", "real-estate", "med-spas", "solar-installers", "auto-dealerships", "dental-practices"],
 sources=[],
),
dict(
 slug="call-tracking", cat="Reporting",
 title="Call tracking: see which ads and pages make your phone ring",
 kw="Call Tracking with Number Pools: See Which Ads Make Your Phone Ring",
 desc="How call tracking with number pools and dynamic number insertion shows which ads, keywords and pages drive phone calls.",
 read=6,
 short="Call tracking shows which marketing makes your phone ring. With a number pool, your website swaps in a tracking number for each visitor (dynamic number insertion), so when they call, the call is tied to the ad, keyword or page they came from. In Oceanic Funnels OS, create a pool under Settings → Phone Numbers → Add Number → Add Number Pool, set where calls forward, paste the snippet on your site and see results in Reporting → Call Report.",
 sections=[
  ("Why it matters", """
<p>For many local businesses, most leads call instead of filling in a form. Without call tracking, those leads look like they came from nowhere, and you can't tell which ads are worth paying for.</p>"""),
  ("How number pools work", """
<p>A pool is a set of tracking numbers (at least four). When someone lands on your site from an ad, they see one of the pool numbers. Calls to it forward to your business line, and the system records the source. Google Ads clicks are detected automatically.</p>"""),
  ("Set it up", """
<ol class="nf-steps-list">
<li>Go to <b>Settings → Phone Numbers</b>, open <b>Add Number</b> and choose <b>Add Number Pool</b>.</li>
<li>Choose which visitors to track. All visitors is recommended; paid search only is also available.</li>
<li>Name the pool and set its size. More call volume needs more numbers.</li>
<li>Set the number calls forward to (your business line) and the number shown on your site to be swapped.</li>
<li>Choose local or toll-free numbers, and optionally a whisper message and call recording.</li>
<li>Copy the snippet from the pool's info and paste it into your website or funnel's body tracking code.</li>
<li>Test in a private browser window.</li>
</ol>"""),
  ("Track keywords and multiple ads", """
<p>Add <code>?keyword={keyword}</code> to your ad URLs to record the keyword, and use group IDs to show different pools for different ads or pages. View results in <b>Reporting → Call Report</b>.</p>"""),
  ("Costs", """
<p>Each pool number is billed like a standard phone number, plus call minutes, from your wallet.</p>"""),
 ],
 faqs=[
  ("What is dynamic number insertion?", "It swaps the phone number on your website for a tracking number based on how the visitor arrived, so calls can be tied to the right source."),
  ("Will callers notice?", "No. They see a normal local or toll-free number, and calls forward to your business line."),
  ("What is a whisper message?", "A short message only you hear before the call connects. With a separate pool per campaign, you can use it to name the campaign the caller came from."),
 ],
 related_ind=["home-services", "hvac", "plumbers", "law-firms", "dental-practices", "auto-repair-shops"],
 sources=[],
),
dict(
 slug="email-marketing-campaigns", cat="Marketing",
 title="Email marketing for small business: how to send campaigns people open",
 kw="Email Marketing for Small Business: Send Campaigns People Open",
 desc="How to plan, build, target and schedule email campaigns and newsletters, and keep them out of spam.",
 read=7,
 short="Email campaigns work when they go to people who asked for them, say one useful thing, and arrive from an authenticated domain. In Oceanic Funnels OS, verify a sending domain first, then go to Marketing → Email → Campaigns, build your email from a template, preview on desktop and mobile, pick recipients with smart lists or segments, and send now, schedule, or send in batches to pace large lists.",
 sections=[
  ("Set up your sending domain first", """
<p>You need a verified sending domain before sending campaigns. Follow our <a href="/guides/email-deliverability-spf-dkim-dmarc/">email deliverability guide</a> for SPF, DKIM and DMARC.</p>"""),
  ("What to send", """
<ul>
<li><b>Newsletters:</b> tips, news and one call to action, monthly or fortnightly.</li>
<li><b>Offers:</b> seasonal promotions to the right segment, not everyone.</li>
<li><b>Announcements:</b> new services, new locations, events.</li>
<li><b>Content:</b> your latest blog post or guide.</li>
</ul>"""),
  ("Build and send", """
<ol class="nf-steps-list">
<li>Go to <b>Marketing → Email → Campaigns</b> and create a campaign.</li>
<li>Choose a template or build your own: content, images and links.</li>
<li>Preview on desktop and mobile and send yourself a test.</li>
<li>Choose recipients using smart lists or segments, and add tags, link tracking and UTM tracking in Additional Settings.</li>
<li>Send now, schedule for a set time (you can reschedule until an hour before), or use batch sending for large lists.</li>
</ol>"""),
  ("Write emails people open", """
<ul>
<li>Short, specific subject lines. Avoid all caps and spammy words.</li>
<li>Write like a person, from a person.</li>
<li>One main link or button.</li>
<li>Mobile-friendly layout with readable text.</li>
</ul>"""),
  ("Automated emails vs campaigns", """
<p>Campaigns are one-off sends. For follow-up that runs on its own, like welcome series and nurture sequences, use <a href="/guides/workflow-automation/">workflows</a>.</p>"""),
 ],
 faqs=[
  ("Do I need a sending domain?", "Yes. A verified sending domain is required before sending campaigns, and it's essential for deliverability."),
  ("Can I schedule email campaigns?", "Yes. Schedule for a future date and time, or use batch sending to pace large sends."),
  ("How much does email cost?", "Email sending is pay-as-you-go from your wallet, with no per-contact pricing. Contacts are unlimited on every plan."),
 ],
 related_ind=["ecommerce-brands", "course-creators", "restaurants", "financial-advisors", "nonprofits", "churches"],
 sources=[],
),
dict(
 slug="social-media-scheduling", cat="Marketing",
 title="How to schedule social media posts for every platform from one place",
 kw="Schedule Social Media Posts from One Place: Social Planner Guide",
 desc="Plan and schedule posts for Facebook, Instagram, LinkedIn, TikTok, Google Business Profile and more from one social planner.",
 read=5,
 short="A social planner lets you write, schedule and publish posts to all your social accounts from one place. In Oceanic Funnels OS, go to Marketing → Social Planner, connect your accounts (Facebook pages and groups, Instagram, LinkedIn, TikTok, X and Google Business Profile), create a post, choose the accounts and schedule it. Posts can also be uploaded in bulk or sent for approval before they go live.",
 sections=[
  ("Why schedule instead of posting live", """
<ul>
<li>Batch a month of content in one sitting.</li>
<li>Post consistently, even when you're busy.</li>
<li>Keep every channel up to date, including your Google Business Profile.</li>
</ul>"""),
  ("Set it up", """
<ol class="nf-steps-list">
<li>Go to <b>Marketing → Social Planner</b>.</li>
<li>Connect your social accounts.</li>
<li>Create a post: write the text, add images or video, and choose the accounts.</li>
<li>Schedule a date and time, or post now.</li>
<li>For client or manager sign-off, use <b>Send Post for Approval</b>.</li>
</ol>"""),
  ("A simple weekly content plan", """
<ul>
<li><b>Monday:</b> a tip or how-to.</li>
<li><b>Wednesday:</b> a customer result or review (with permission).</li>
<li><b>Friday:</b> behind the scenes or your team.</li>
<li><b>Monthly:</b> an offer or event.</li>
</ul>
<p>Repurpose your <a href="/guides/start-a-business-blog/">blog posts</a> and guides into short posts with a link back.</p>"""),
  ("Turn followers into leads", """
<p>Point your bio link to a funnel or booking page, and let an <a href="/guides/ai-chat-agent-for-business/">AI agent</a> reply to Facebook and Instagram DMs so no message waits.</p>"""),
 ],
 faqs=[
  ("Which platforms can I post to?", "Facebook pages and groups, Instagram, LinkedIn, TikTok, X and Google Business Profile."),
  ("Can posts be approved before they publish?", "Yes. Use Send Post for Approval so the owner or a manager signs off first."),
  ("Can I upload posts in bulk?", "Yes. Posts can be bulk uploaded to plan a month at a time."),
 ],
 related_ind=["restaurants", "salons-barbershops", "gyms-fitness-studios", "real-estate", "photographers", "churches"],
 sources=[],
),
]
