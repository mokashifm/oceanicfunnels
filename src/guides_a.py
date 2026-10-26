"""Guides part A: lead response and conversations.
Each guide: slug, title (H1), kw (title tag), desc (meta), cat, read (minutes), short (answer-first box),
sections [(h2, html)], faqs [(q, a)], related_ind [industry slugs], sources [(title, url)].
Menu paths are the Oceanic Funnels OS menus. No vendor names.
"""

G_A = [
dict(
 slug="missed-call-text-back", cat="Lead response",
 title="What is missed call text back? How it works and how to set it up",
 kw="Missed Call Text Back: What It Is and How to Set It Up",
 desc="Missed call text back sends an automatic text when you can't answer a call, so the caller doesn't ring your competitor. Here's how it works and how to set it up.",
 read=7,
 short="Missed call text back is an automation that sends a text message to anyone whose call you don't answer, usually within seconds. Instead of hitting voicemail and calling the next business on Google, the caller gets a message like \"Sorry we missed you, how can we help?\" and the conversation continues by text. In Oceanic Funnels OS you turn it on under Settings → Phone System → Voice → Voicemail & Missed Call Text Back.",
 sections=[
  ("Why missed calls cost you customers", """
<p>Most people who call a local business and get voicemail don't leave a message. They hang up and call the next result. If you're a plumber under a sink, a stylist mid-cut or a dentist with a patient, you can't answer every call, and every unanswered call is a customer who may book with someone else.</p>
<p>Missed call text back closes that gap. The caller gets an instant, personal reply, which keeps the conversation with you until you, a team member or an AI agent can pick it up.</p>"""),
  ("How missed call text back works", """
<ol>
<li><b>Someone calls your business number.</b> If nobody answers before the ring timeout, the call counts as missed.</li>
<li><b>An automatic text goes out.</b> The system texts the caller from your business number with the message you wrote.</li>
<li><b>The reply lands in your inbox.</b> When the caller texts back, the conversation appears in your unified inbox next to their contact record.</li>
<li><b>You (or your AI agent) carry on the conversation.</b> Book them, quote them or answer their question by text.</li>
</ol>
<p>A few details matter. Answered calls never trigger a text. Every missed call sends a text, so if someone calls three times in a row they'll get three texts unless you add a rule to limit it. And contacts who have opted out of texts won't receive one.</p>"""),
  ("What to write in your missed call text", """
<p>Keep it short, human and specific to what callers usually want. A good message names your business, apologises for missing them and asks one easy question.</p>
<ul>
<li><b>Home services:</b> "Hi, this is Coastal Plumbing. Sorry we missed your call, we're on a job. What's going on and what's your address? We'll get you booked in."</li>
<li><b>Clinics and spas:</b> "Thanks for calling Bloom Aesthetics! We're with a client right now. Are you looking to book, or do you have a question we can help with?"</li>
<li><b>Coaches and consultants:</b> "Hey, it's Sam from Peak Coaching. Missed your call. Grab a time that suits you here and I'll call you back: [booking link]"</li>
</ul>
<p>Avoid long paragraphs, multiple links or anything that reads like a marketing blast. The goal is a reply.</p>"""),
  ("How to set up missed call text back in Oceanic Funnels OS", """
<ol class="nf-steps-list">
<li>Go to <b>Settings → Phone System</b>, then open the <b>Voice</b> tab.</li>
<li>Open <b>Voicemail &amp; Missed Call Text Back</b> and select <b>Missed Call Text Back</b>.</li>
<li>Tick <b>Enable Missed Call Text Back</b> and click <b>Customize</b>.</li>
<li>Write your message. You can insert fields such as the business name.</li>
<li>Send yourself a test, then click <b>Save</b>.</li>
<li>Set the incoming call timeout in the same Voice area. Around 10 to 20 seconds works for most businesses: long enough to answer, short enough that the text arrives while the caller is still holding their phone.</li>
</ol>
<p>To send texts in the US, your number needs to be registered for business texting (A2P 10DLC for local numbers, or toll-free verification). We cover that in our <a href="/guides/a2p-10dlc-registration/">A2P 10DLC guide</a>. On the Growth and Done-For-You plans, our team sets all of this up for you.</p>"""),
  ("Make it smarter with an AI agent", """
<p>Missed call text back starts the conversation. An <a href="/guides/ai-chat-agent-for-business/">AI chat agent</a> can finish it: answer common questions, collect details and book an appointment straight into your calendar, any time of day. For calls, a <a href="/guides/ai-receptionist/">voice AI receptionist</a> can answer the phone itself.</p>"""),
 ],
 faqs=[
  ("Does missed call text back work on my existing number?", "It works on the business phone numbers inside Oceanic Funnels OS. You can get a new local or toll-free number, or forward your existing line to one, so missed calls on that line trigger the text."),
  ("Will callers get a text every time they call?", "Yes, every missed call triggers a text by default. If you want to limit repeats, you can add a rule in an automation, such as only texting once per day."),
  ("Can missed call text back reply on WhatsApp instead of SMS?", "Missed call text back sends SMS. There is a separate missed-call reply option for WhatsApp if you use the WhatsApp add-on."),
  ("Does it cost extra?", "The feature is included. Each text is billed as normal SMS usage from your wallet."),
 ],
 related_ind=["home-services", "hvac", "plumbers", "salons-barbershops", "dental-practices", "auto-repair-shops"],
 sources=[],
),
dict(
 slug="speed-to-lead", cat="Lead response",
 title="Speed to lead: why replying in minutes wins the sale, and how to automate it",
 kw="Speed to Lead: Why Fast Lead Response Wins (and How to Automate It)",
 desc="Speed to lead is how fast you respond to a new enquiry. Research shows the first business to reply usually wins. Here's how to reply in seconds automatically.",
 read=8,
 short="Speed to lead is the time between a new lead contacting you and your first reply. It matters because interest fades fast and many people contact several businesses at once. A widely cited Harvard Business Review study found companies that contacted leads within an hour were nearly seven times as likely to qualify them as those that waited even an hour longer. The fix is automation: an instant text and email, an AI agent that answers questions, and a booking link, so every lead gets a reply in seconds, day or night.",
 sections=[
  ("What speed to lead means", """
<p>Every enquiry starts a clock. A form fill, a Facebook lead ad, a missed call, an Instagram DM. The person is thinking about their problem right now, and they may have contacted two or three other businesses in the same five minutes. Whoever responds first, with something useful, usually gets the conversation and often the sale.</p>"""),
  ("What the research says", """
<p>In a study published in Harvard Business Review, researchers looked at how quickly companies responded to web leads. Firms that tried to contact a lead within an hour were nearly seven times as likely to qualify that lead as firms that waited even an hour longer, and more than 60 times as likely as firms that waited 24 hours or more. Many companies in the study took far longer than an hour to respond at all.</p>
<p>The exact numbers will vary by industry, but the pattern holds everywhere: the longer a lead waits, the colder it gets.</p>"""),
  ("Why most businesses are slow", """
<ul>
<li><b>Leads arrive when you're busy.</b> On a job, with a client, or after hours.</li>
<li><b>Leads arrive in too many places.</b> Website forms, ad platforms, social DMs, email and calls, each checked separately.</li>
<li><b>No clear owner.</b> Nobody is sure who is meant to follow up, so nobody does.</li>
</ul>"""),
  ("How to automate speed to lead", """
<ol>
<li><b>Bring every lead into one CRM.</b> Forms, funnels, ad leads, calls and social messages all create or update a contact in the same place.</li>
<li><b>Send an instant reply.</b> An automation sends a text and email the moment the lead arrives: who you are, what happens next, and a booking link.</li>
<li><b>Let an AI agent handle the first conversation.</b> It answers common questions, asks your qualifying questions and books the appointment.</li>
<li><b>Alert a human.</b> Your team gets a notification and a task to call hot leads, with the conversation history already on the record.</li>
<li><b>Follow up if there's no reply.</b> A short sequence of texts and emails over the next few days, stopping automatically when they respond or book.</li>
</ol>"""),
  ("Setting it up in Oceanic Funnels OS", """
<p>In Oceanic Funnels OS, this is a workflow triggered by a new form submission, a new lead or an inbound message. It sends your instant reply, assigns the lead to a team member, creates a task and starts the follow-up sequence. Pair it with <a href="/guides/missed-call-text-back/">missed call text back</a> so phone leads get the same instant response, and an <a href="/guides/ai-chat-agent-for-business/">AI chat agent</a> for conversations outside business hours.</p>
<p>On the Growth plan our team installs a speed-to-lead automation as one of your core automations in the first week. On Done-For-You, we build it into your full funnel and backend.</p>"""),
  ("What to measure", """
<ul>
<li><b>Time to first response:</b> aim for under a minute for automated replies and under five minutes for a human follow-up during business hours.</li>
<li><b>Contact rate:</b> the share of new leads who reply or answer.</li>
<li><b>Booking rate:</b> the share of leads who book a call or appointment.</li>
</ul>"""),
 ],
 faqs=[
  ("What is a good speed to lead?", "Automated replies should go out within seconds. For a human follow-up, aim for under five minutes during business hours. The research consistently shows that the first hour matters most."),
  ("Do automated replies feel impersonal?", "Not if they're written well. A short, friendly text that names your business and asks one easy question reads as personal, and it's far better than no reply at all."),
  ("Can an AI agent reply to leads at night?", "Yes. An AI agent can reply on SMS, email, website chat, Facebook, Instagram and WhatsApp, answer questions and book appointments around the clock."),
 ],
 related_ind=["real-estate", "insurance-agencies", "solar-installers", "mortgage-brokers", "roofing", "auto-dealerships"],
 sources=[("The Short Life of Online Sales Leads (Harvard Business Review, 2011)", "https://hbr.org/2011/03/the-short-life-of-online-sales-leads")],
),
dict(
 slug="ai-chat-agent-for-business", cat="AI agents",
 title="How to set up an AI chat agent that answers leads and books appointments",
 kw="AI Chat Agent for Business: Answer Leads and Book Appointments 24/7",
 desc="An AI chat agent replies to leads on your website, SMS, Facebook, Instagram and WhatsApp, answers questions and books appointments. Here's how to set one up.",
 read=8,
 short="An AI chat agent is software that replies to customer messages for you, using your business information. In Oceanic Funnels OS, it can answer on SMS, email, your website chat, Facebook, Instagram and WhatsApp, answer common questions, qualify leads and book, reschedule or cancel appointments in your calendar. You create one under AI Agents → Conversation AI, train it on your business, test it in suggestive mode, then switch it to auto-pilot.",
 sections=[
  ("What an AI chat agent can do for a small business", """
<ul>
<li><b>Reply instantly, day or night.</b> No lead waits until morning.</li>
<li><b>Answer the questions you get every day.</b> Prices, opening hours, services, location, what to bring.</li>
<li><b>Qualify leads.</b> Ask your questions, such as budget, timeline or location, before handing over to a human.</li>
<li><b>Book appointments.</b> Offer times from your calendar and book, reschedule or cancel.</li>
<li><b>Work across channels.</b> SMS, email, website chat, Facebook, Instagram and WhatsApp from one agent.</li>
</ul>"""),
  ("Suggestive mode vs auto-pilot", """
<p>AI agents in Oceanic Funnels OS have three modes:</p>
<ul>
<li><b>Off:</b> the agent doesn't respond.</li>
<li><b>Suggestive:</b> the agent drafts replies for your team to review and send. This is the best way to start, because you can see how it answers before it talks to customers on its own.</li>
<li><b>Auto-pilot:</b> the agent replies automatically.</li>
</ul>
<p>We recommend running in suggestive mode until the agent handles your common questions, unknown questions and bookings the way you want, then switching to auto-pilot.</p>"""),
  ("How to set up your AI chat agent", """
<ol class="nf-steps-list">
<li>Go to <b>AI Agents → Conversation AI</b> and click <b>Create Bot</b>.</li>
<li>Pick a setup method. The guided form is the quickest: choose <b>General Q&amp;A</b> or <b>Appointment Booking</b>, then set a brand voice.</li>
<li>Train the agent on your business: services, prices, policies, opening hours and the questions customers ask most.</li>
<li>Set its goals, such as booking an appointment, and connect the calendar it should book into.</li>
<li>Choose the channels it should answer on.</li>
<li>Test it with real questions in suggestive mode, then switch to auto-pilot.</li>
</ol>
<p>For more complex conversations, a prompt-based or flow-based agent gives you full control over the instructions and branching logic.</p>"""),
  ("Writing good instructions", """
<ul>
<li><b>Be specific about what it can and can't promise.</b> For example: "Never quote a final price; give the starting price and offer a free estimate."</li>
<li><b>Tell it when to hand over.</b> Complaints, urgent issues and anything it isn't sure about should go to a human.</li>
<li><b>Match your tone.</b> Friendly and short works best on SMS and social messages.</li>
<li><b>Keep information current.</b> Update prices and hours whenever they change.</li>
</ul>"""),
  ("What it costs", """
<p>AI usage in Oceanic Funnels OS is pay-as-you-go: chat replies are billed from your wallet based on the tokens they use, so you only pay for the conversations the agent actually has. If you have high volume, the optional AI Agent Unlimited add-on is +$147 a month. See <a href="/#pricing">pricing</a>.</p>"""),
 ],
 faqs=[
  ("Which channels can the AI agent reply on?", "SMS, email, website chat, Facebook, Instagram and WhatsApp. WhatsApp requires the +$19/month WhatsApp add-on plus WhatsApp's own message fees."),
  ("Can the AI agent book appointments?", "Yes. Connect a calendar and the agent can offer available times, book, reschedule and cancel appointments."),
  ("Will it make things up?", "Agents answer from the information and instructions you give them. Testing in suggestive mode and giving clear instructions on when to hand over to a human keeps answers accurate."),
  ("Do you set it up for me?", "On the Growth plan our team sets up and trains one AI chat agent on your business. On Done-For-You we set up both chat and voice AI."),
 ],
 related_ind=["med-spas", "coaches-consultants", "gyms-fitness-studios", "real-estate", "soccer-clubs-academies", "travel-agencies"],
 sources=[],
),
dict(
 slug="ai-receptionist", cat="AI agents",
 title="AI receptionist for small business: how a voice AI agent answers your calls",
 kw="AI Receptionist for Small Business: Voice AI That Answers Calls",
 desc="A voice AI receptionist answers your business calls, answers questions, books appointments and transfers urgent calls. Here's how it works and how to set it up.",
 read=7,
 short="An AI receptionist is a voice AI agent that answers your business phone, talks to callers in natural speech, answers common questions from your knowledge base, books appointments into your calendar, sends texts and transfers calls to a person when needed. In Oceanic Funnels OS you build one under AI Agents → Voice AI, assign it a phone number and choose whether it answers every call, only after hours, or as a backup when nobody picks up.",
 sections=[
  ("What a voice AI agent does", """
<ul>
<li><b>Answers inbound calls</b> with your welcome message and voice.</li>
<li><b>Answers questions</b> using a knowledge base with your services, prices and policies.</li>
<li><b>Collects caller details</b> and saves them to the contact record.</li>
<li><b>Books appointments</b> into a connected calendar.</li>
<li><b>Transfers calls</b> to a person's phone when the caller needs a human.</li>
<li><b>Sends a text</b> during the call, such as a booking link or directions.</li>
<li><b>Logs everything:</b> each call is saved with a recording, transcript and summary.</li>
</ul>"""),
  ("When to use it: always on, after hours or backup", """
<p>You decide when the agent picks up. Common setups:</p>
<ul>
<li><b>After hours only:</b> your team answers during the day, and the AI handles evenings and weekends.</li>
<li><b>Backup:</b> the AI answers only when nobody on the team picks up.</li>
<li><b>Always on:</b> the AI answers every call first and transfers when needed, which suits busy front desks.</li>
</ul>"""),
  ("How to set up a voice AI agent", """
<ol class="nf-steps-list">
<li>Go to <b>AI Agents → Voice AI</b> and click <b>Create Agent</b>.</li>
<li>Name the agent, then choose its voice, language, timezone and welcome message.</li>
<li>Write the prompt: who it is, what your business does, how to handle common requests and when to transfer.</li>
<li>Add a <b>Knowledge Base</b> with your services, prices, hours and FAQs.</li>
<li>Add <b>Actions</b>: appointment booking with your calendar, call transfer to a team member, and send SMS.</li>
<li>Test it with a web call or phone call.</li>
<li>In <b>Deploy</b>, pick the phone number, choose <b>Answer Calls Directly</b> or <b>Use as Backup</b>, and set working hours.</li>
</ol>"""),
  ("Tips for a natural-sounding agent", """
<ul>
<li>Keep the welcome message short: name the business and ask how you can help.</li>
<li>Tell the agent to confirm details back to the caller, such as dates and phone numbers.</li>
<li>Give it a clear rule for emergencies and complaints: transfer straight away.</li>
<li>Review call summaries in the first week and tighten the prompt where callers got stuck.</li>
</ul>"""),
  ("Costs", """
<p>Voice AI in Oceanic Funnels OS is pay-as-you-go, billed by the minute from your wallet. If you take a lot of calls, AI Agent Unlimited (+$147/month) covers unlimited AI replies and voice minutes. On the Done-For-You plan, our team builds and tunes your voice AI agent for you.</p>"""),
 ],
 faqs=[
  ("Can the AI receptionist transfer a call to me?", "Yes. Add a call transfer action with your phone number, and tell the agent when to use it, such as emergencies or when the caller asks for a person."),
  ("Can it book appointments during the call?", "Yes. Connect a calendar and add the appointment booking action, and the agent will offer available times and book the appointment."),
  ("Can I listen to the calls?", "Yes. Each call is logged with a recording, transcript and AI summary, and the summary can also be saved to the contact's notes."),
 ],
 related_ind=["home-services", "hvac", "dental-practices", "law-firms", "chiropractors-physiotherapy", "vacation-rentals"],
 sources=[],
),
dict(
 slug="whatsapp-business-automation", cat="Messaging",
 title="WhatsApp automation for business: what you can automate and what it costs",
 kw="WhatsApp Business Automation: What You Can Automate and Costs",
 desc="How businesses automate WhatsApp: instant replies, reminders, AI agents and broadcasts, plus how WhatsApp's 24-hour window and per-message pricing work.",
 read=8,
 short="With the WhatsApp Business Platform connected to Oceanic Funnels OS, you can reply to WhatsApp messages from the same inbox as SMS, email and social DMs, let an AI agent answer and book appointments, send appointment reminders and follow-ups, and send approved template messages to opted-in contacts. WhatsApp charges per message for templates; replies inside the 24-hour customer service window are free. In Oceanic Funnels OS, WhatsApp is a +$19/month add-on plus WhatsApp's message fees.",
 sections=[
  ("Why WhatsApp matters", """
<p>In much of the world, WhatsApp is how customers prefer to talk to businesses. Parents of a soccer academy, travellers booking a trip, clients of a clinic: many would rather send a WhatsApp than call or email. Bringing WhatsApp into your CRM means those conversations aren't trapped on one staff member's phone.</p>"""),
  ("What you can automate", """
<ul>
<li><b>Instant replies</b> to new messages, with an AI agent that answers questions and books appointments.</li>
<li><b>Appointment notifications:</b> confirmations, reminders and follow-ups from your calendar settings.</li>
<li><b>Workflow messages</b> after forms, purchases or pipeline changes.</li>
<li><b>Broadcasts</b> to opted-in groups, like a team, class or customer segment, using approved templates.</li>
<li><b>Missed call replies</b> by WhatsApp instead of SMS.</li>
</ul>"""),
  ("How WhatsApp's rules and pricing work", """
<p>WhatsApp has its own rules for businesses. The two that matter most:</p>
<ul>
<li><b>The 24-hour customer service window.</b> When a customer messages you, a 24-hour window opens. Inside it you can send normal free-form replies. Outside it, you can only send pre-approved <b>template</b> messages.</li>
<li><b>Per-message pricing.</b> Since July 2025, WhatsApp charges per template message, with prices that depend on the category and the country. Marketing templates are always charged. Utility templates, such as an appointment reminder, are free when sent inside an open customer service window and charged outside it. Free-form replies inside the window are free.</li>
</ul>
<p>There's also a 72-hour free window when someone messages you from a click-to-WhatsApp ad and you reply within 24 hours. Check WhatsApp's current rate card for your country before planning large campaigns.</p>"""),
  ("Getting set up", """
<ol class="nf-steps-list">
<li>Add the WhatsApp add-on to your Oceanic Funnels OS account.</li>
<li>Connect your WhatsApp Business account and phone number through the setup flow. You'll need a Meta business account.</li>
<li>Create and submit your message templates for approval, such as appointment reminders and follow-ups.</li>
<li>Turn on WhatsApp in your calendar notifications, workflows and AI agent channels.</li>
</ol>
<p>On the Growth and Done-For-You plans, our team handles this setup with you.</p>"""),
  ("Best practices", """
<ul>
<li>Only message people who have opted in to WhatsApp messages from you.</li>
<li>Keep templates short and useful. Reminders and updates get far better responses than promotions.</li>
<li>Reply fast while the 24-hour window is open, which is when conversations are free.</li>
<li>Use tags to send broadcasts only to the relevant group.</li>
</ul>"""),
 ],
 faqs=[
  ("How much does WhatsApp cost in Oceanic Funnels OS?", "WhatsApp is a +$19/month add-on, plus WhatsApp's own per-message fees for template messages, which vary by country and message category."),
  ("Can my AI agent reply on WhatsApp?", "Yes. The AI chat agent can answer WhatsApp messages and book appointments, just like on SMS and website chat."),
  ("Can I send appointment reminders on WhatsApp?", "Yes. Turn on WhatsApp in your calendar notifications and choose an approved template for reminders and follow-ups."),
 ],
 related_ind=["soccer-clubs-academies", "travel-agencies", "swim-schools", "martial-arts-dance-studios", "churches", "daycares-preschools"],
 sources=[("Pricing on the WhatsApp Business Platform (Meta for Developers)", "https://developers.facebook.com/docs/whatsapp/pricing")],
),
]
