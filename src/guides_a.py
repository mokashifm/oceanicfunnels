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
 desc="Missed call text back sends an automatic text when you can't answer a call, so the caller doesn't ring your competitor. How it works and how to set it up.",
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
<p>To send texts in the US, your number needs to be registered for business texting (A2P 10DLC for local numbers, or toll-free verification). We cover that in our <a href="/guides/a2p-10dlc-registration/">A2P 10DLC guide</a>. On the Scale plan, your account manager and builder help you set all of this up.</p>"""),
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
 title="What is speed to lead? Meaning, statistics and software to automate it",
 kw="Speed to Lead: Meaning, Statistics and Software (2026 Guide)",
 desc="Speed to lead is how fast you reply to a new lead. See the HBR and MIT research, what speed to lead software does, and how to reply in seconds.",
 read=13, updated="2026-11-01",
 short="Speed to lead is the time between a new lead contacting you and your first reply. It matters because interest fades fast and many people contact several businesses at once. A widely cited Harvard Business Review study found companies that contacted leads within an hour were nearly seven times as likely to qualify them as those that waited even an hour longer. An earlier MIT and InsideSales study found the odds of reaching a lead dropped 100 times when the first call came at 30 minutes instead of 5. The fix is speed to lead software: an instant text and email, an AI agent that answers questions, and a booking link, so every lead gets a reply in seconds, day or night.",
 sections=[
  ("What speed to lead means", """
<p>Speed to lead (also called lead response time) is the total time it takes a business to contact a prospect after they submit an enquiry, fill out a web form, call or show buying interest. Every enquiry starts a clock. A form fill, a Facebook lead ad, a missed call, an Instagram DM. The person is thinking about their problem right now, and they may have contacted two or three other businesses in the same five minutes. Whoever responds first, with something useful, usually gets the conversation and often the sale.</p>
<p>You'll also see it written as "speed 2 lead" or "speed2lead". It's the same idea: reply first, reply fast.</p>"""),
  ("Speed to lead statistics: what the research says", """
<p><b>Harvard Business Review (2011).</b> In a study published in Harvard Business Review, researchers looked at how quickly companies responded to web leads. Firms that tried to contact a lead within an hour were nearly seven times as likely to qualify that lead as firms that waited even an hour longer, and more than 60 times as likely as firms that waited 24 hours or more. Many companies in the study took far longer than an hour to respond at all.</p>
<p><b>MIT and InsideSales Lead Response Management Study (2007).</b> Using three years of data from six companies, more than 15,000 leads and over 100,000 call attempts, the researchers found:</p>
<ul>
<li>The odds of <b>contacting</b> a lead if called in 5 minutes versus 30 minutes drop <b>100 times</b>.</li>
<li>The odds of <b>qualifying</b> a lead if called in 5 minutes versus 30 minutes drop <b>21 times</b>.</li>
<li>Wednesdays and Thursdays were the best days to make contact, and 4 to 6pm the best time of day.</li>
</ul>
<p>Both studies are more than a decade old and were run on phone and web leads, so treat the exact multiples as a guide rather than a promise. The pattern has held up since: the longer a lead waits, the colder it gets. This is where the popular "5-minute rule" comes from: reply to every new lead within five minutes.</p>"""),
  ("What is speed to lead software?", """
<p>Speed to lead software replies to new leads automatically, the moment they arrive, and makes sure a person follows up fast. Instead of a lead sitting in an inbox until someone checks it, the software sends an instant text and email, alerts your team and starts a follow-up sequence.</p>
<p>Look for these features when you compare speed to lead tools:</p>
<ul>
<li><b>Every lead source in one place:</b> website forms, funnels, Facebook and Instagram lead ads, calls, texts and social DMs.</li>
<li><b>Instant SMS and email replies</b> that go out within seconds, 24/7.</li>
<li><b><a href="/guides/missed-call-text-back/">Missed call text back</a></b>, so phone leads get the same instant reply.</li>
<li><b>An AI agent</b> that answers questions and books appointments outside business hours.</li>
<li><b>Team alerts and lead routing</b> (round robin or by territory), with a task to call.</li>
<li><b>Automatic follow-up</b> that stops when the lead replies or books.</li>
<li><b>Response-time reporting</b>, so you can see how fast each lead got a reply.</li>
</ul>
<p>Many businesses stitch this together from a CRM, a texting tool and a scheduler. Oceanic Funnels OS does all of it in one system.</p>"""),
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
  ("7 ways to improve speed to lead", """
<ol>
<li><b>Automate instant replies.</b> Send a text and email with a booking link the second a form is submitted. No human should be needed for the first reply.</li>
<li><b>Use an AI agent after hours.</b> Evenings and weekends are when many leads arrive and nobody is at a desk. An AI agent can answer questions, qualify and book around the clock.</li>
<li><b>Route leads to the right person automatically.</b> Use round robin or rules by service, location or language, so every lead has an owner the moment it arrives.</li>
<li><b>Cut form friction.</b> Ask only for what you need to reply: name, phone, email and one or two qualifying questions. Shorter forms get more submissions and faster replies.</li>
<li><b>Text back missed calls.</b> Phone leads go cold fastest. <a href="/guides/missed-call-text-back/">Missed call text back</a> replies within seconds when nobody can pick up.</li>
<li><b>Put alerts on your team's phones.</b> A push or SMS alert with the lead's details and a tap-to-call link beats an email that sits unread.</li>
<li><b>Measure it every week.</b> Track average and slowest response times by person and by lead source, and fix the gaps.</li>
</ol>"""),
  ("How to calculate speed to lead", """
<p><b>Speed to lead = time of first response − time the lead arrived.</b></p>
<p>Example: a form is submitted at 7:42pm and your first text goes out at 7:42pm and 20 seconds. Your speed to lead is 20 seconds. If the first reply is a call at 9:15am the next day, it's 13 hours and 33 minutes.</p>
<p>Report the <b>median</b> as well as the average, because a few leads left overnight can hide behind a good average. Count only real replies: a message that answers the lead or books them, not an internal notification.</p>
<h3>Test your own speed to lead</h3>
<p>Fill out your own website form, send your own Instagram DM, and call your main number after hours. Time how long each takes to get a reply. Most owners are surprised by the result. Then take our free <a href="/tools/speed-to-lead-test/">Speed to Lead Test</a> to score your setup out of 100 and see your top fixes.</p>"""),
  ("Setting it up in Oceanic Funnels OS", """
<p>In Oceanic Funnels OS, this is a workflow triggered by a new form submission, a new lead or an inbound message. It sends your instant reply, assigns the lead to a team member, creates a task and starts the follow-up sequence. Pair it with <a href="/guides/missed-call-text-back/">missed call text back</a> so phone leads get the same instant response, and an <a href="/guides/ai-chat-agent-for-business/">AI chat agent</a> for conversations outside business hours.</p>
<p>Speed-to-lead automations are included from the Growth plan, and AI replies from AI Pro. On Scale, your builder sets them up with you.</p>"""),
  ("What to measure", """
<ul>
<li><b>Time to first response:</b> aim for under a minute for automated replies and under five minutes for a human follow-up during business hours.</li>
<li><b>Contact rate:</b> the share of new leads who reply or answer.</li>
<li><b>Booking rate:</b> the share of leads who book a call or appointment.</li>
</ul>"""),
 ],
 faqs=[
  ("What does speed to lead mean?", "Speed to lead means how quickly you respond to a new lead after they contact you, from the moment they submit a form, call or message, to your first reply. The faster the reply, the better your chance of reaching and converting them."),
  ("Is 'speed 2 lead' the same as speed to lead?", "Yes. 'Speed 2 lead' and 'speed2lead' are other ways of writing speed to lead. They all mean the time it takes to reply to a new lead."),
  ("What is speed to lead software?", "Speed to lead software replies to new leads automatically within seconds by text and email, alerts your team, routes the lead to the right person and keeps following up until they reply or book."),
  ("What is the 5-minute rule for leads?", "The 5-minute rule says you should contact every new lead within five minutes. It comes from lead response research such as the MIT and InsideSales study, which found contact odds dropped 100 times at 30 minutes compared with 5."),
  ("How do you calculate speed to lead?", "Subtract the time the lead arrived from the time of your first real reply. For example, a form submitted at 7:42pm that gets a text at 7:42 and 20 seconds has a speed to lead of 20 seconds. Track the median as well as the average."),
  ("How can I improve speed to lead?", "Automate an instant text and email reply, use an AI agent after hours, route leads to an owner automatically, shorten your forms, text back missed calls, alert your team on their phones, and review response times weekly."),
  ("What is a good speed to lead?", "Automated replies should go out within seconds. For a human follow-up, aim for under five minutes during business hours. The research consistently shows that the first hour matters most."),
  ("Do automated replies feel impersonal?", "Not if they're written well. A short, friendly text that names your business and asks one easy question reads as personal, and it's far better than no reply at all."),
  ("Can an AI agent reply to leads at night?", "Yes. An AI agent can reply on SMS, email, website chat, Facebook, Instagram and WhatsApp, answer questions and book appointments around the clock."),
 ],
 related_ind=["real-estate", "insurance-agencies", "solar-installers", "mortgage-brokers", "roofing", "auto-dealerships"],
 sources=[("The Short Life of Online Sales Leads (Harvard Business Review, 2011)", "https://hbr.org/2011/03/the-short-life-of-online-sales-leads"),
          ("Lead Response Management Study (Elkington and Oldroyd, MIT and InsideSales, 2007)", "https://www.mortech.com/hs-fs/hub/25649/file-13535879-pdf/docs/mit_study.pdf")],
),
dict(
 slug="ai-chat-agent-for-business", cat="AI agents",
 title="How to set up an AI chat agent that answers leads and books appointments",
 kw="AI Chat Agent for Business: Answer Leads and Book 24/7",
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
  ("Do you set it up for me?", "AI agents are included on AI Pro and Scale. On Scale, your account manager and builder help you set up and train your chat and voice AI agents."),
 ],
 related_ind=["med-spas", "coaches-consultants", "gyms-fitness-studios", "real-estate", "soccer-clubs-academies", "travel-agencies"],
 sources=[],
),
dict(
 slug="ai-receptionist", cat="AI agents",
 title="AI receptionist for small business: how a voice AI agent answers your calls",
 kw="AI Receptionist: Voice AI That Answers Your Business Calls",
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
<p>Voice AI in Oceanic Funnels OS is pay-as-you-go, billed by the minute from your wallet. If you take a lot of calls, AI Agent Unlimited (+$147/month) covers unlimited AI replies and voice minutes. Voice AI is included on AI Pro and Scale, and on Scale your builder helps you set up and tune your voice agent.</p>"""),
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
<li>Go to <b>Settings → WhatsApp</b> and choose how to connect: link the WhatsApp Business app you already use (you keep using the app, and can import up to six months of chat history), create a new WhatsApp Business account with a new number, or migrate a number from another WhatsApp provider.</li>
<li>Log in with the Facebook account that manages your business, verify the number with the code sent by SMS or call, and select your Meta business portfolio.</li>
<li>Create and submit your message templates for approval, such as appointment reminders and follow-ups.</li>
<li>Turn on WhatsApp in your calendar notifications, workflows and AI agent channels.</li>
</ol>
<p>On the Scale plan, your account manager and builder help you with this setup.</p>"""),
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
