"""AI-for-business series, batch 1: 30 days x 2 posts (Facebook + Instagram).
(kicker, image headline, caption, hashtags). Order = day 1 AM, day 1 PM, day 2 AM, ...
Stats used (verified Oct 2026):
- QuickBooks/Intuit 2026 AI Impact Report (May 12, 2026): 34,000+ SMB owners in US, Canada, UK, Australia;
  ~7 in 10 use AI regularly; US 77% (up from 48% in July 2024); US 78% say productivity improved; US 43% say revenue increased.
- Goldman Sachs 10,000 Small Businesses survey (Mar 17, 2026, n=1,256, US): 76% use AI; only 14% fully integrate it
  into core operations; 49% cite lack of technical expertise; 48% difficulty choosing tools.
- BrightLocal Local Consumer Review Survey 2026 (Mar 10, 2026, 1,002 US adults): 45% use AI tools for local business
  recommendations (up from 6%); ChatGPT 31%, Google AI Mode 23%; 97% of AI users sometimes double-check AI picks against real reviews.
"""

POSTS = [
# Day 1
("AI for business", "7 in 10 small businesses now use AI regularly.",
"A 2026 QuickBooks study of more than 34,000 small and midsize business owners in the US, UK, Canada and Australia found roughly 7 in 10 now use AI regularly.\n\nIn the US, that's 77%, up from 48% in mid-2024.\n\nThe question is no longer whether your competitors use AI. It's whether they use it to answer customers faster than you do.\n\nSource: QuickBooks 2026 AI Impact Report.",
"#ai #smallbusiness #artificialintelligence #businessgrowth"),
("AI search", "Your customers are asking ChatGPT who to call.",
"In BrightLocal's 2026 survey of US consumers, 45% said they now use AI tools to find local business recommendations. A year earlier it was 6%.\n\nChatGPT and Google's AI Mode were the most used.\n\nIf an AI tool can't find clear, consistent information about your business, it can't recommend you.\n\nSource: BrightLocal Local Consumer Review Survey 2026.",
"#aisearch #chatgpt #localbusiness #localseo"),
# Day 2
("Prompt of the day", "Turn one customer question into a week of content.",
"Try this prompt in ChatGPT, Claude or Gemini:\n\n\"I run a [type of business] in [city]. A customer asked: '[their question]'. Write a short, friendly answer I can post on social media, a longer version for my website FAQ, and a 3-line version for a text reply.\"\n\nOne real question. Three ready-to-use answers. Always read and edit before you post.",
"#aiprompts #chatgpt #contentmarketing #smallbusiness"),
("AI agents", "A chatbot answers questions. An AI agent gets things done.",
"Old chatbots followed a script and got stuck the moment a customer went off it.\n\nAn AI agent understands the question, looks up your services and prices, asks a follow-up, and books the appointment into your calendar. When it hits something it shouldn't handle, it passes the conversation to a person.\n\nThat's the difference between deflecting customers and serving them.",
"#aiagents #ai #customerservice #automation"),
# Day 3
("AI reality check", "76% use AI. Only 14% have built it into how they run the business.",
"Goldman Sachs surveyed 1,256 US small business owners in early 2026. 76% use AI, but only 14% have fully integrated it into their core operations.\n\nMost businesses use AI like a search engine: ask a question, copy the answer.\n\nThe real gains come when AI is wired into the work itself: answering leads, booking appointments, following up, sending reminders.\n\nSource: Goldman Sachs 10,000 Small Businesses survey, March 2026.",
"#ai #smallbusiness #digitaltransformation #automation"),
("AI search", "How to check whether AI recommends your business.",
"Open ChatGPT or Google's AI Mode and ask the questions your customers ask:\n\n\"Best [your service] near [your area]\"\n\"Who does [service] open on Saturdays in [city]?\"\n\nNote who gets mentioned, and which websites and reviews the answer is based on. If you're missing, that tells you exactly where to show up next.\n\nRepeat it every month. The answers change.",
"#aisearch #localseo #chatgpt #smallbusiness"),
# Day 4
("AI voice", "AI can now answer your phone and book the appointment.",
"An AI voice agent picks up when you can't, in a natural voice, answers common questions about your services, hours and prices, and books the caller into your calendar.\n\nIt doesn't replace your team. It catches the calls your team can't take: during busy hours, after closing time and at weekends.\n\nEvery missed call is a customer someone else will serve.",
"#voiceai #aireceptionist #smallbusiness #customerservice"),
("Prompt of the day", "Ask AI to find the holes in your website.",
"Paste your homepage text into an AI tool and ask:\n\n\"You're a busy customer looking for [your service]. Read this page. What questions do you still have? What would stop you from booking? What's confusing?\"\n\nYou'll get an honest outside view in seconds. Fix the top three things it finds.",
"#aiprompts #website #conversion #smallbusiness"),
# Day 5
("AI myth", "\"AI is only for big companies.\"",
"The opposite is true. Big companies have staff to answer every enquiry. Small businesses don't.\n\nThat's exactly where AI helps most: replying to leads at night, sending reminders, writing first drafts, summarising messages, answering the same ten questions every day.\n\nYou don't need a tech team. You need the right system set up once.",
"#ai #smallbusiness #entrepreneur #automation"),
("AI search", "AI tools trust businesses with clear, consistent information.",
"When AI answers \"who's the best [service] near me\", it pulls from your Google Business Profile, your reviews, your website and other sites that mention you.\n\nThree things to check today:\n1. Name, address, phone and hours are identical everywhere\n2. Your website answers common questions in plain words\n3. You're getting fresh reviews every month\n\nThe clearer your information, the easier you are to recommend.",
"#aisearch #localseo #googlebusinessprofile #smallbusiness"),
# Day 6
("Prompt of the day", "Let AI write the follow-up you keep forgetting to send.",
"Prompt:\n\n\"Write a short, friendly follow-up text to a customer who asked about [service] 3 days ago but didn't book. Mention [one benefit]. End with a simple question. Under 300 characters. No pressure.\"\n\nBetter still: set it up as an automation so it sends itself to every lead who goes quiet.",
"#aiprompts #followup #sales #smallbusiness"),
("AI for business", "Where small businesses actually use AI first.",
"QuickBooks' 2026 research found businesses usually start with AI in admin, customer communication and scheduling, and use it least where human judgement matters most.\n\nThat's the right order. Let AI handle the repetitive, time-sensitive work, like replies, reminders, booking and summaries, and keep people on the work that needs care and judgement.\n\nSource: QuickBooks 2026 AI Impact Report.",
"#ai #smallbusiness #productivity #automation"),
# Day 7
("AI safety", "Three rules before you let AI talk to your customers.",
"1. Give it your real information: services, prices, hours, policies. AI guesses when it doesn't know.\n2. Tell it what not to answer, such as medical, legal or financial specifics, and to hand those to a person.\n3. Review conversations every week and fix anything it got wrong.\n\nSet up properly, an AI agent is fast and consistent. Set up lazily, it's a liability.",
"#aisafety #aiagents #customerservice #smallbusiness"),
("AI agents", "What an AI agent can do while you sleep.",
"- Reply to website chat, Facebook, Instagram and text messages in seconds\n- Answer questions about services, prices and opening hours\n- Ask qualifying questions\n- Book appointments into your calendar\n- Send the booking confirmation\n- Flag anything urgent for your team in the morning\n\nYou wake up to booked appointments, not a pile of unread messages.",
"#aiagents #automation #smallbusiness #leadgeneration"),
# Day 8
("AI reality check", "The biggest barrier to AI isn't cost. It's know-how.",
"In Goldman Sachs' 2026 survey of US small business owners, 49% of AI users said lack of technical expertise was a barrier, and 48% struggled to choose the right tools.\n\nMost owners don't need another tool to learn. They need a system that's already set up for how their business works.\n\nSource: Goldman Sachs 10,000 Small Businesses survey, March 2026.",
"#ai #smallbusiness #aitools #businessowner"),
("Prompt of the day", "Turn your reviews into marketing in two minutes.",
"Copy your last 20 reviews into an AI tool and ask:\n\n\"What do customers praise most? List the top 5 themes, with a short quote for each. Then suggest 3 headlines for my website based on what customers actually say.\"\n\nYour customers have already written your best marketing. AI just helps you find it.",
"#aiprompts #reviews #marketing #smallbusiness"),
# Day 9
("AI search", "Reviews matter more in the AI era, not less.",
"BrightLocal found that 97% of people who use AI for local recommendations sometimes double-check the AI's picks against real reviews.\n\nAI might put you on the shortlist. Your reviews decide whether you get the call.\n\nAsk every happy customer, every time, automatically.\n\nSource: BrightLocal Local Consumer Review Survey 2026.",
"#reviews #aisearch #localbusiness #reputation"),
("AI voice", "After-hours calls don't have to go to voicemail anymore.",
"Most people won't leave a voicemail for a business they've never used. They hang up and call the next one.\n\nAn AI voice agent can answer after hours, handle the common questions and book a time, then send your team a summary of the call.\n\nAnd if you'd rather not use AI on the phone, missed call text back is the simplest fix: an instant text the moment a call goes unanswered.",
"#voiceai #missedcalls #smallbusiness #customerservice"),
# Day 10
("AI myth", "\"Customers hate talking to AI.\"",
"Customers hate waiting, being ignored and getting useless answers.\n\nAn AI that answers instantly, gets the facts right and books them in is a better experience than a voicemail box or a reply two days later.\n\nWhat customers don't like is being trapped. Always give them an easy way to reach a person.",
"#ai #customerexperience #aiagents #smallbusiness"),
("Prompt of the day", "Plan a month of posts in ten minutes.",
"Prompt:\n\n\"I run a [business] for [type of customer]. Give me 20 social media post ideas based on the questions customers ask before buying, common mistakes they make, and quick tips. For each, write a one-line hook.\"\n\nPick the best ten, add your own photos and voice, and schedule them in one sitting.",
"#aiprompts #socialmediamarketing #contentplanning #smallbusiness"),
# Day 11
("AI for business", "AI won't replace your team. It replaces the waiting.",
"In Goldman Sachs' 2026 survey, 87% of small business owners using AI said it augments their workforce rather than replacing employees.\n\nThe best use of AI is taking the repetitive, time-sensitive tasks off your team's plate, so the first reply goes out in seconds and your people spend their time on customers who are ready to buy.\n\nSource: Goldman Sachs 10,000 Small Businesses survey, March 2026.",
"#ai #teamwork #smallbusiness #productivity"),
("AI search", "Write your FAQs the way customers ask questions.",
"AI search tools read your website to answer questions about you. The easier your answers are to find, the more likely they get used.\n\nTurn real customer questions into an FAQ page:\n\"How much does [service] cost?\"\n\"Do you work weekends?\"\n\"How long does it take?\"\n\nOne clear question, one clear answer. Plain words, no jargon.",
"#aisearch #seo #faq #smallbusiness"),
# Day 12
("Prompt of the day", "Ask AI to roleplay your toughest customer.",
"Prompt:\n\n\"Act as a customer who is interested in [service] but thinks it's too expensive. I'll reply as the business owner. Push back the way a real customer would.\"\n\nPractise your answers before the real conversation. It's free sales training, any time you want it.",
"#aiprompts #salestraining #sales #smallbusiness"),
("AI agents", "Train your AI agent like a new employee.",
"You wouldn't put a new hire on the front desk without showing them your prices, policies and how you talk to customers.\n\nGive your AI agent the same:\n- Services, prices and hours\n- Answers to your 20 most common questions\n- Your booking rules\n- Your tone of voice\n- What to hand to a person\n\nThe better the training, the better the conversations.",
"#aiagents #ai #customerservice #smallbusiness"),
# Day 13
("AI for business", "Businesses using AI report it's helping revenue, not just time.",
"In QuickBooks' 2026 research, 43% of US small businesses said AI had increased their revenue. Only 2% said it decreased it.\n\nThe revenue gains come from speed: answering leads first, following up consistently and filling the calendar, not from AI writing nicer emails.\n\nSource: QuickBooks 2026 AI Impact Report.",
"#ai #revenue #smallbusiness #businessgrowth"),
("AI safety", "Don't paste customer data into free AI tools.",
"Free AI chat tools are great for drafting and brainstorming. They're not the place for customer names, phone numbers, medical details or payment information.\n\nUse AI inside systems built for business data, and check what each tool does with what you type.\n\nIn Goldman Sachs' 2026 survey, half of small business AI users named data privacy and security as a concern. They're right to.",
"#aisafety #dataprivacy #cybersecurity #smallbusiness"),
# Day 14
("Prompt of the day", "Rewrite your service descriptions in customer language.",
"Prompt:\n\n\"Rewrite this service description so a busy customer understands it in 10 seconds. Lead with the result they get, not the process. Keep it under 60 words. Avoid jargon.\n\n[paste your description]\"\n\nCustomers buy outcomes. AI can help you say it their way.",
"#aiprompts #copywriting #marketing #smallbusiness"),
("AI search", "Google's AI Mode answers questions like a conversation.",
"Instead of typing a few keywords, people can now ask Google full questions and follow-ups: \"Which dentist near me takes new patients and is open Saturday?\" Then: \"Which of those has the best reviews?\"\n\nAI Mode builds one answer from your Business Profile, reviews and website.\n\nKeep your hours, services and photos up to date, and answer common questions on your site.",
"#googleaimode #aisearch #localseo #smallbusiness"),
# Day 15
("AI myth", "\"AI will make all businesses sound the same.\"",
"Only if everyone uses it the same way.\n\nAI writes the first draft. You add the details only you know: the customer story, your opinion, your local knowledge, your photos.\n\nUse AI to save time on the blank page, then make it yours.",
"#ai #contentcreation #branding #smallbusiness"),
("AI voice", "What a good AI receptionist says and what it never says.",
"Should do:\n- Greet callers by your business name\n- Answer hours, location, services and price ranges\n- Book, reschedule and confirm appointments\n- Take a clear message for anything else\n\nShould never do:\n- Give medical, legal or financial advice\n- Promise things your team hasn't approved\n- Keep a caller going round in circles when they ask for a person",
"#aireceptionist #voiceai #customerservice #smallbusiness"),
# Day 16
("Prompt of the day", "Summarise a long customer email in one line.",
"Prompt:\n\n\"Summarise this customer message in one sentence. Then list what they're asking for, how urgent it is, and suggest a polite reply.\n\n[paste message]\"\n\nYou still decide what to send. AI just gets you there faster. Never paste anything sensitive into a tool you don't trust.",
"#aiprompts #productivity #email #smallbusiness"),
("AI agents", "The best AI agents know when to hand over.",
"Good AI customer service isn't about answering everything. It's about answering the easy 80% instantly and passing the rest to a person, with the full conversation attached.\n\nThe customer doesn't repeat themselves. Your team sees exactly what they need. Everyone wins.",
"#aiagents #customerservice #ai #smallbusiness"),
# Day 17
("AI for business", "AI works best on the jobs nobody wants to do.",
"- Replying to the same question for the 50th time\n- Chasing confirmations and no-shows\n- Sending payment reminders\n- Writing the first draft of a post\n- Summarising a long thread\n- Following up with leads who went quiet\n\nHand these to AI and automation. Keep the conversations that build relationships for yourself.",
"#ai #automation #productivity #smallbusiness"),
("AI search", "Is your business invisible to AI?",
"Quick test: ask ChatGPT \"What does [your business name] in [your city] do?\"\n\nIf it gets it wrong, or knows nothing, AI tools don't have enough clear information about you yet.\n\nThe fix: a clear website, a complete Google Business Profile, consistent listings, fresh reviews and mentions on other trusted local sites.",
"#aisearch #chatgpt #localseo #smallbusiness"),
# Day 18
("Prompt of the day", "Create a simple onboarding email sequence with AI.",
"Prompt:\n\n\"Write a 3-email welcome sequence for a new customer of my [business]. Email 1: welcome and what happens next. Email 2 (day 3): a helpful tip. Email 3 (day 7): ask how it's going and invite a review. Friendly, under 120 words each.\"\n\nEdit, add your voice, and load it into an automation once.",
"#aiprompts #emailmarketing #customerexperience #smallbusiness"),
("AI reality check", "AI is only as good as the system around it.",
"An AI that writes a brilliant reply does nothing if the lead sits in an inbox nobody checks.\n\nThe value comes from connecting AI to the rest of your business: your inbox, calendar, CRM, payments and follow-up.\n\nThat's why the businesses getting the most from AI aren't using more tools. They're using fewer, better-connected ones.",
"#ai #crm #automation #smallbusiness"),
# Day 19
("AI myth", "\"Setting up AI takes months.\"",
"Not for the everyday jobs.\n\nAn AI agent for your website and messages, missed call text back, booking with reminders and a follow-up sequence can all be live in days, once your information is ready.\n\nStart with the leak that costs you the most, like slow replies or no-shows, and fix that first.",
"#ai #automation #smallbusiness #getstarted"),
("AI agents", "AI on Instagram DMs: what it should and shouldn't do.",
"Should:\n- Reply within seconds, even at night\n- Answer questions about services and prices\n- Share your booking link and help them pick a time\n- Pass anything sensitive or complicated to a person\n\nShouldn't:\n- Pretend to be a specific person on your team\n- Make promises about results\n- Argue with customers\n\nSet the rules once, and review the conversations weekly.",
"#instagram #aiagents #socialmedia #smallbusiness"),
# Day 20
("Prompt of the day", "Find out why leads aren't booking.",
"Paste 10 lead conversations that didn't book, with personal details removed, and ask:\n\n\"What patterns do you see? Where did these conversations stall? What questions went unanswered? Suggest 3 changes to how we reply.\"\n\nAI is great at spotting patterns you're too close to see.",
"#aiprompts #sales #conversion #smallbusiness"),
("AI for business", "In the US, 78% of small businesses say AI improved productivity.",
"That's up from 46% in mid-2024, according to QuickBooks' 2026 AI Impact Report.\n\nProductivity only matters if the time saved goes somewhere useful. Put it into the customers, the calls and the work that grows the business.\n\nSource: QuickBooks 2026 AI Impact Report.",
"#ai #productivity #smallbusiness #businessgrowth"),
# Day 21
("AI search", "Five things AI tools look at before recommending a local business.",
"1. Your Google Business Profile: hours, services, photos\n2. Your reviews: how many, how recent, what they say\n3. Your website: clear answers to common questions\n4. Consistent name, address and phone across listings\n5. Mentions on other local and industry sites\n\nNone of it is new. AI just makes it matter more.",
"#aisearch #localseo #googlebusinessprofile #smallbusiness"),
("AI voice", "Missed calls are the easiest AI win for most businesses.",
"If you only do one thing with AI this month, make sure no call goes unanswered.\n\nOption 1: an instant text back when you miss a call.\nOption 2: an AI voice agent that answers and books.\n\nBoth run 24/7. Both catch customers who would otherwise call your competitor next.",
"#missedcalls #voiceai #smallbusiness #automation"),
# Day 22
("AI safety", "Watch out for AI voice scams targeting businesses.",
"Scammers can now clone voices from short audio clips. Some businesses have received calls that sound like the owner or a supplier asking for an urgent payment.\n\nSimple protection:\n- Never pay on a phone or voice-note request alone\n- Agree a code word for urgent payment requests\n- Confirm any change of bank details through a known number\n\nAI helps your business. Make sure it can't be used against it.",
"#cybersecurity #aiscams #fraudprevention #smallbusiness"),
("Prompt of the day", "Write a better job ad in five minutes.",
"Prompt:\n\n\"Write a job ad for a [role] at my [business] in [city]. Include what a normal day looks like, who will love this job, who won't, pay range [X], and how to apply. Friendly and honest, under 250 words.\"\n\nHonest ads attract better applicants. AI helps with the first draft; you add the truth.",
"#aiprompts #hiring #recruitment #smallbusiness"),
# Day 23
("AI agents", "One AI agent, every channel.",
"Customers message you wherever is easiest: your website chat, Facebook, Instagram, text, WhatsApp.\n\nOne AI agent trained on your business can answer on all of them, consistently, with every conversation landing in one inbox your team can see.\n\nNo more switching between five apps to find out who's been answered.",
"#aiagents #omnichannel #customerservice #smallbusiness"),
("AI myth", "\"If I use AI, I'll lose the personal touch.\"",
"You lose the personal touch when customers wait two days for a reply, or never hear back at all.\n\nLet AI handle the speed: instant replies, reminders and follow-ups. Then add the personal touch where it counts: the call, the visit, the thank-you, remembering their name.\n\nFast and personal isn't a contradiction.",
"#customerexperience #ai #smallbusiness #service"),
# Day 24
("AI for business", "The AI gap: using it vs building it in.",
"Most small businesses now use AI. Far fewer have built it into how the business runs.\n\nUsing AI: asking ChatGPT to write a post.\nBuilding it in: every new lead gets an instant AI reply, a booking link, reminders and follow-ups, automatically.\n\nThe second one is where the time and revenue gains are.",
"#ai #automation #smallbusiness #businessstrategy"),
("Prompt of the day", "Turn a blog post into a week of social content.",
"Prompt:\n\n\"Turn this article into 5 social media posts: one tip, one myth vs fact, one question for my audience, one short story, and one call to action. Under 120 words each.\n\n[paste article]\"\n\nWrite once, publish five times.",
"#aiprompts #contentrepurposing #socialmedia #smallbusiness"),
# Day 25
("AI search", "Photos help AI and customers understand your business.",
"AI tools and Google use your photos to understand what you do and where you are, and customers use them to decide whether to trust you.\n\nAdd recent, real photos to your website, Google Business Profile and social profiles: your team, your work, your premises.\n\nStock photos don't build trust. Real ones do.",
"#localseo #googlebusinessprofile #aisearch #smallbusiness"),
("AI agents", "What happens when your AI agent doesn't know the answer?",
"It should say so, and get a person involved. Never make something up.\n\nThat's why setup matters:\n- Give it your real information\n- Tell it to admit when it doesn't know\n- Route those conversations to your team\n- Add the missing answer so it knows next time\n\nEvery week, your AI gets a little better.",
"#aiagents #ai #customerservice #smallbusiness"),
# Day 26
("AI reality check", "Don't buy an AI tool until you know its job.",
"QuickBooks found only about 1 in 10 small businesses pay for dedicated AI tools, and the ones that do mostly keep paying. The difference is usually a clear job for the tool from day one.\n\nBefore buying any AI tool, ask: what specific job will it do, who will set it up, and how will we know it's working?\n\nSource: QuickBooks 2026 AI Impact Report.",
"#ai #aitools #smallbusiness #businesstips"),
("Prompt of the day", "Prepare for a sales call in two minutes.",
"Prompt:\n\n\"I'm about to speak to a [type of business] owner about [your service]. List the 5 problems they most likely have, 5 questions I should ask, and 3 objections they might raise, with a calm answer to each.\"\n\nWalk in prepared. Listen more than you talk.",
"#aiprompts #sales #salestips #smallbusiness"),
# Day 27
("AI voice", "AI can take bookings over the phone, in a natural voice.",
"Today's AI voice agents don't sound like the old \"press 1 for sales\" systems. They understand natural speech, ask follow-up questions and book appointments.\n\nThey work best for clear, repeatable calls: bookings, opening hours, prices, directions. Complex or sensitive calls should still reach a person.",
"#voiceai #aireceptionist #smallbusiness #customerservice"),
("AI for business", "Start with one AI job, not ten.",
"Pick the one problem that costs you the most right now:\n\n- Slow replies to new leads\n- Missed calls\n- No-shows\n- Unpaid invoices\n- Forgotten follow-ups\n\nAutomate that first. Measure it for a month. Then add the next one.\n\nSmall, working steps beat a big plan that never gets finished.",
"#ai #automation #smallbusiness #productivity"),
# Day 28
("AI search", "AI tools quote your website. Make it worth quoting.",
"When AI answers a question about your industry or area, it often cites websites that explain things clearly.\n\nWrite short, helpful pages that answer real questions: prices, timelines, what to expect, how to choose.\n\nHelpful content gets found by people and by AI.",
"#contentmarketing #aisearch #seo #smallbusiness"),
("AI myth", "\"AI is too expensive for a small business.\"",
"Many everyday AI features, like chat replies, reminders and drafting, are now built into business software at a small monthly cost, and they work 24/7.\n\nThe real cost to compare isn't the software. It's the leads you lose to slow replies, the no-shows nobody reminded, and the follow-ups that never got sent.",
"#ai #smallbusiness #roi #automation"),
# Day 29
("Prompt of the day", "Write a reply to a bad review without making it worse.",
"Prompt:\n\n\"Write a calm, professional reply to this negative review. Thank them, acknowledge the issue without arguing, briefly explain what we're doing about it, and invite them to contact us directly. Under 80 words.\n\n[paste review]\"\n\nRead it twice before posting. Future customers are reading too.",
"#aiprompts #reviews #reputationmanagement #smallbusiness"),
("AI agents", "Your AI agent can work weekends. Your follow-up should too.",
"A lead that messages on Saturday night and hears nothing until Monday has usually moved on.\n\nAn AI agent answers immediately, books them in, and your follow-up automation keeps them warm until your team is back.\n\nYour business stays open for enquiries even when your doors are closed.",
"#aiagents #weekend #smallbusiness #automation"),
# Day 30
("AI for business", "AI is now everyday business. The difference is how you use it.",
"Across the US, UK, Canada and Australia, most small businesses now use AI regularly.\n\nThe winners won't be the ones with the most AI tools. They'll be the ones who use AI to reply faster, follow up every time, and never miss a customer.\n\nThat's what we build at Oceanic Funnels.",
"#ai #smallbusiness #future #automation"),
("Get started", "Put AI to work in your business this month.",
"An AI agent on your website and social messages. Missed call text back. Booking with reminders. Follow-up that never forgets.\n\nAll in one system that works 24/7, from $67 a month, or built for you by our team.\n\noceanicfunnels.com",
"#oceanicfunnels #aiagents #automation #smallbusiness"),
]

assert len(POSTS) == 60, len(POSTS)
