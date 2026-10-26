"""Guides part C: websites, SEO, content, store and lead capture. Menu paths checked against the product's help docs (Oct 2026)."""

G_C = [
dict(
 slug="build-a-business-website", cat="Websites and SEO",
 title="How to build a business website and connect your domain",
 kw="How to Build a Business Website and Connect Your Domain",
 desc="Build a professional business website from a template, connect your own domain with free SSL, and turn visitors into leads, step by step.",
 read=7,
 short="To build a business website in Oceanic Funnels OS, go to Sites → Websites, click New Website, start from a template or a blank page, and edit each page in the drag-and-drop builder. Then connect your domain from the website's Settings tab (automatically with supported providers, or by adding DNS records), assign it to the site and publish. SSL is set up automatically once the domain is verified. Forms, calendars and chat on the site feed straight into your CRM.",
 sections=[
  ("Website or funnel?", """
<p>Use a <b>website</b> when you need several pages people browse: home, services, about, contact, blog. Use a <a href="/guides/how-to-build-a-sales-funnel/">funnel</a> when you want visitors to take one action, such as booking a call or buying. Most businesses use both, and both are unlimited on every Oceanic Funnels plan.</p>"""),
  ("Step by step: create, customise, connect, publish", """
<ol class="nf-steps-list">
<li>Go to <b>Sites → Websites</b> and click <b>New Website</b>. Choose <b>From Templates</b> or <b>From Blank</b>, name the site and click <b>Create</b>.</li>
<li>Edit each page's text, images, colours, navigation, buttons and forms in the builder. Check the mobile layout and preview as a visitor.</li>
<li>Add each page's title and meta description for search engines, then click <b>Save</b>. Saving doesn't change the live site yet.</li>
<li>Open the website's <b>Settings</b> tab, click <b>Connect Domain</b> and enter your domain or subdomain. Connect automatically by authorising a supported domain provider, or manually by adding the DNS records shown. DNS changes can take up to 24 hours.</li>
<li>In the same <b>Settings</b> tab, select the connected domain from the Domain dropdown and save.</li>
<li>Back in the builder, preview, save and click <b>Publish</b> on every page that should be live.</li>
</ol>
<p>SSL (the padlock and https) is set up automatically once your domain's DNS records are verified. If you use Cloudflare, set the A or CNAME record to DNS only.</p>"""),
  ("What every business website needs", """
<ul>
<li><b>A clear headline</b> that says what you do and who for, above the fold.</li>
<li><b>One main call to action</b> repeated down the page: book, call or get a quote.</li>
<li><b>Proof:</b> reviews, photos of your work, results.</li>
<li><b>Contact options</b>: phone, form, booking calendar and <a href="/guides/website-live-chat-widget/">live chat</a>.</li>
<li><b>Fast loading and mobile-first design</b>, since most visitors arrive on a phone.</li>
</ul>"""),
  ("Test before you share it", """
<p>Submit a test form, book a test appointment and run a test checkout if you sell online. Make sure each one creates the contact, notification or order you expect in your CRM.</p>"""),
  ("Next: get found on Google", """
<p>Once the site is live, work through our <a href="/guides/website-seo-checklist/">website SEO checklist</a> and start a <a href="/guides/start-a-business-blog/">blog</a> that answers your customers' questions.</p>"""),
 ],
 faqs=[
  ("Can I use my own domain?", "Yes. Connect your domain from the website's Settings tab, automatically with supported providers or by adding DNS records manually. SSL is added automatically."),
  ("Do I need a developer?", "No. Websites are built with a drag-and-drop builder and templates. On the Done-For-You plan our team builds your sales funnel for you, and an extra funnel can be built for you by our team for $297."),
  ("How many websites can I build?", "Unlimited websites and funnels are included on every plan."),
 ],
 related_ind=["home-services", "law-firms", "dental-practices", "restaurants", "contractors-remodelers", "photographers"],
 sources=[],
),
dict(
 slug="website-seo-checklist", cat="Websites and SEO",
 title="Website SEO checklist: the settings that help you rank on Google",
 kw="Website SEO Checklist: Settings That Help You Rank on Google",
 desc="A practical website SEO checklist: page titles, meta descriptions, social images, canonical links, XML sitemap, redirects, schema markup and content.",
 read=8,
 short="The on-site SEO basics are: a unique title and meta description on every page, one clear H1, a social sharing image, canonical links to avoid duplicates, an XML sitemap submitted to Google Search Console, 301 redirects for old URLs, schema markup that describes your business, fast mobile pages, and helpful content that answers real questions. In Oceanic Funnels OS, page SEO lives under each page's Settings → SEO Meta Data, the sitemap and robots.txt under Settings → Domains, and redirects under Settings → URL Redirects.",
 sections=[
  ("1. Titles and meta descriptions", """
<p>Every page needs a unique title (around 50 to 60 characters) with the main phrase people search, and a meta description (around 150 to 160 characters) that makes them want to click. In the page or funnel step editor, open <b>Settings → SEO Meta Data</b>.</p>"""),
  ("2. One clear H1 and helpful headings", """
<p>Use one H1 per page that matches the search intent, then H2s for each section. Write headings people would actually search, like "How much does a roof inspection cost?"</p>"""),
  ("3. Social image", """
<p>Add a <b>Social Image</b> (1200 × 630 pixels) in the same SEO Meta Data panel, so links shared on Facebook, LinkedIn and WhatsApp look professional.</p>"""),
  ("4. Canonical links", """
<p>If similar content lives at more than one URL, set the <b>Canonical Link</b> at the bottom of the SEO Meta Data panel so Google knows which version to rank. Blog posts have their own canonical setting under <b>Sites → Blogs</b>.</p>"""),
  ("5. XML sitemap and robots.txt", """
<p>Generate your <b>XML Sitemap</b> and manage <b>robots.txt</b> under <b>Settings → Domains</b>, from the Manage menu next to your domain. Then submit the sitemap in Google Search Console and Bing Webmaster Tools.</p>"""),
  ("6. Redirects", """
<p>When you change a URL or move from an old website, add 301 redirects under <b>Settings → URL Redirects</b> so you keep the rankings and links the old pages earned.</p>"""),
  ("7. Schema markup", """
<p>Schema markup tells search engines and AI assistants exactly what your business is: name, address, services, reviews, FAQs. The website builder includes a <b>Schema Markup</b> option under SEO &amp; AEO Optimization, with manual and AI-assisted modes.</p>"""),
  ("8. Speed and mobile", """
<ul>
<li>Compress images before uploading.</li>
<li>Avoid heavy scripts and too many third-party widgets.</li>
<li>Check every page on a phone.</li>
</ul>"""),
  ("9. Content that answers questions", """
<p>Settings get you eligible to rank; content is what ranks. Create a page for each service and location you serve, and a <a href="/guides/start-a-business-blog/">blog</a> that answers your customers' questions. Answer the question in the first paragraph, which helps with Google's AI answers and assistants like ChatGPT.</p>"""),
  ("10. Off-site signals", """
<ul>
<li>A complete Google Business Profile.</li>
<li>Consistent business details across directories (see <a href="/guides/business-listings-management/">business listings</a>).</li>
<li>A steady flow of <a href="/guides/get-more-google-reviews/">Google reviews</a>.</li>
<li>Links from local partners, associations and press.</li>
</ul>"""),
 ],
 faqs=[
  ("How long does SEO take?", "It varies, but new pages and new domains commonly take a few months to rank for competitive terms. Long, specific searches usually rank sooner."),
  ("Do I need to submit my sitemap?", "Google can find pages on its own, but submitting your XML sitemap in Google Search Console and Bing Webmaster Tools helps new pages get discovered faster."),
  ("What is AEO?", "Answer engine optimisation means structuring content so AI assistants and Google's AI answers can quote it: direct answers, clear headings, FAQs and schema markup."),
 ],
 related_ind=["home-services", "dental-practices", "law-firms", "real-estate", "roofing", "med-spas"],
 sources=[],
),
dict(
 slug="start-a-business-blog", cat="Websites and SEO",
 title="How to start a business blog that brings in leads",
 kw="How to Start a Business Blog That Brings In Leads",
 desc="How to set up a business blog, what to write about, how to structure posts for Google and AI search, and how to turn readers into leads.",
 read=7,
 short="A business blog brings in leads when each post answers a question your customers search for, then invites them to take the next step. In Oceanic Funnels OS, create a blog under Sites → Blogs, add posts with a title, slug, category, author, SEO description and cover image, and publish, schedule or save as draft. Add the blog to your website with the Blog Post List element and link every post to a relevant service page or booking form.",
 sections=[
  ("What to write about", """
<ul>
<li><b>Questions customers ask you every week.</b> Each one is a post.</li>
<li><b>Costs and prices:</b> "How much does a kitchen remodel cost in 2026?"</li>
<li><b>Comparisons:</b> "Veneers vs bonding: which is right for you?"</li>
<li><b>How-tos and checklists</b> related to your service.</li>
<li><b>Local topics</b> for the areas you serve.</li>
</ul>"""),
  ("How to set up your blog", """
<ol class="nf-steps-list">
<li>Go to <b>Sites → Blogs</b> and create a new blog from scratch or a template.</li>
<li>Set the site title, slug and description, and connect your domain now or later in Blog Settings.</li>
<li>Add a post: write it, or import from a URL or CSV file.</li>
<li>Set the URL slug, category, author, SEO title, description and a cover image with alt text.</li>
<li>Publish now, schedule for later or save as a draft.</li>
<li>Add the <b>Blog Post List</b> element to a page on your website to show your posts.</li>
</ol>"""),
  ("How to structure a post for Google and AI search", """
<ul>
<li>Answer the question in the first two or three sentences.</li>
<li>Use clear H2 headings that match related questions.</li>
<li>Add a short FAQ at the end.</li>
<li>Use real examples, prices and steps from your experience.</li>
<li>Link to the relevant service page and to other posts.</li>
</ul>"""),
  ("Turn readers into leads", """
<p>Every post should end with a clear next step: book a call, get a quote, download a checklist. A free resource in exchange for an email adds the reader to your CRM, where an automated email sequence can follow up.</p>"""),
  ("How often to post", """
<p>Consistency beats volume. One genuinely useful post a week, kept up for six months, builds far more search traffic than ten thin posts in one week.</p>"""),
 ],
 faqs=[
  ("Can I schedule blog posts?", "Yes. Posts can be published immediately, scheduled for a future time or kept as drafts."),
  ("Can I import existing blog posts?", "Yes. Posts can be imported from a URL or a CSV file."),
  ("Does the blog use my own domain?", "Yes. Connect your domain in Blog Settings, or show posts on your website with the Blog Post List element."),
 ],
 related_ind=["coaches-consultants", "law-firms", "financial-advisors", "real-estate", "dental-practices", "course-creators"],
 sources=[],
),
dict(
 slug="wordpress-migration", cat="Websites and SEO",
 title="WordPress hosting and migration: move your WordPress site without rebuilding it",
 kw="WordPress Hosting & Migration: Move Your Site Without Rebuilding",
 desc="Keep your WordPress website and move it to Oceanic Funnels hosting next to your CRM, funnels and automations. Here's how the migration works.",
 read=6,
 short="If your business website runs on WordPress, you don't have to rebuild it. Oceanic Funnels can host your WordPress site alongside your CRM, funnels and automations. Our team migrates it with a migration plugin: you install the plugin on your current site and generate a secure, time-limited access link, and we move the site for you. Larger sites typically take one to three business days. WordPress hosting is an add-on; ask our team for pricing.",
 sections=[
  ("Why move WordPress next to your CRM", """
<ul>
<li>One login and one support team for your site, funnels and CRM.</li>
<li>Forms, chat and booking on your WordPress site connect to your contacts and automations.</li>
<li>No more chasing a separate host, plugins for every feature and a developer for every fix.</li>
</ul>"""),
  ("How the migration works", """
<ol class="nf-steps-list">
<li>Tell our team which site you want moved.</li>
<li>In your WordPress admin, go to <b>Plugins → Add Plugin → Upload Plugin</b>, upload the migration plugin we send you, then install and activate it.</li>
<li>Open the plugin from the sidebar and click <b>Generate secure access link</b>. Choose how long it stays active, from 24 hours to 7 days.</li>
<li>Send us the link. Your WordPress password is never shared.</li>
<li>We migrate the site. Larger sites usually take one to three business days.</li>
<li>Review the migrated site, then we point your domain to it.</li>
</ol>
<p>You can revoke or regenerate the access link at any time, and it expires automatically when its timer runs out.</p>"""),
  ("Before you migrate", """
<ul>
<li>Make sure you have administrator access to the current WordPress site.</li>
<li>Take a backup with your current host.</li>
<li>List any custom code or unusual plugins so we can check them.</li>
<li>Plan the domain switch for a quiet time.</li>
</ul>"""),
  ("Or rebuild in the website builder", """
<p>If your WordPress site is small or outdated, rebuilding it in the <a href="/guides/build-a-business-website/">website builder</a> can be simpler: no plugins to update, built-in forms and chat, and unlimited sites on every plan. Keep the same URLs or add <a href="/guides/website-seo-checklist/">301 redirects</a> so you don't lose rankings.</p>"""),
 ],
 faqs=[
  ("Do I have to share my WordPress password?", "No. The migration uses a secure, time-limited access link generated by the plugin. You can revoke it at any time."),
  ("How long does a WordPress migration take?", "Most migrations finish within one to three business days, depending on the size of the site."),
  ("Is WordPress hosting included in my plan?", "WordPress hosting is an add-on. Ask our team for pricing for your site."),
 ],
 related_ind=["law-firms", "dental-practices", "contractors-remodelers", "accountants-cpas", "nonprofits", "churches"],
 sources=[],
),
dict(
 slug="business-listings-management", cat="Websites and SEO",
 title="Business listings: keep your name, address and phone consistent everywhere",
 kw="Business Listings Management: Keep NAP Consistent for Local SEO",
 desc="Why consistent business listings matter for local SEO, which directories count, and how listings management updates them from one place.",
 read=6,
 short="Business listings are your company's profiles on directories, maps and apps such as Google, Bing, Apple Maps and Facebook. Search engines trust businesses whose name, address and phone number (NAP) match everywhere. Listings management publishes your details to a network of directories from one place and keeps them in sync. In Oceanic Funnels OS, listings management is an add-on powered by the major listing networks; ask our team for pricing.",
 sections=[
  ("Why consistent listings matter", """
<p>When your business details differ across sites, an old address on one directory, a different phone number on another, search engines and customers can't be sure which is right. Consistent details support local search rankings, and accurate hours and phone numbers stop customers calling a wrong number or turning up when you're closed.</p>"""),
  ("What to keep consistent", """
<ul>
<li>Business name, exactly the same everywhere.</li>
<li>Address, in the same format.</li>
<li>Main phone number.</li>
<li>Website URL.</li>
<li>Opening hours, including holidays.</li>
<li>Categories, description and photos.</li>
</ul>"""),
  ("How listings management works", """
<ol>
<li>You enter your business details once.</li>
<li>They're published to the directories in the network, including major ones like Bing and Apple Maps.</li>
<li>When something changes, you update it once and the change syncs to the network.</li>
<li>If an update is slow to appear, a force sync can prioritise it.</li>
</ol>"""),
  ("Do these first, for free", """
<ul>
<li>Claim and complete your Google Business Profile.</li>
<li>Claim your Bing Places and Apple Business Connect profiles.</li>
<li>Make sure your website shows the same name, address and phone in the footer.</li>
</ul>"""),
 ],
 faqs=[
  ("What is NAP?", "NAP stands for name, address and phone number. Keeping it identical across the web helps search engines trust your business information."),
  ("Is listings management included?", "Listings management is an add-on. Ask our team for pricing."),
  ("Do I still need a Google Business Profile?", "Yes. Your Google Business Profile is the most important listing for local search. Claim it, complete it and keep getting reviews."),
 ],
 related_ind=["home-services", "dental-practices", "restaurants", "auto-repair-shops", "salons-barbershops", "law-firms"],
 sources=[],
),
dict(
 slug="set-up-an-online-store", cat="Ecommerce and payments",
 title="How to set up an online store: products, shipping and checkout",
 kw="How to Set Up an Online Store: Products, Shipping and Checkout",
 desc="Set up an online store with products, variants, shipping zones, coupons and checkout, connected to your CRM, email and SMS marketing.",
 read=8,
 short="To set up an online store in Oceanic Funnels OS, connect a payment provider, create products under Payments → Products and switch on Include in Online Store, add store elements such as Featured Products, Collections and Cart to your website, then set shipping zones and rates under Payments → Settings → Shipping & Delivery. Orders appear under Payments → Orders, and every buyer becomes a contact you can follow up with by email and SMS.",
 sections=[
  ("Before you start", """
<ul>
<li>Connect a payment provider, such as Stripe, so you can take card payments.</li>
<li>Have product photos, descriptions, prices and variants (sizes, colours) ready.</li>
<li>Decide where you ship and how much it costs.</li>
</ul>"""),
  ("Step 1: Create your products", """
<ol class="nf-steps-list">
<li>Go to <b>Payments → Products</b> and create a product.</li>
<li>Add the name, description, media, price and any variants.</li>
<li>Switch on <b>Include in Online Store</b> and save. Products without this setting won't show in your store.</li>
</ol>"""),
  ("Step 2: Add the store to your website", """
<p>Go to <b>Sites → Stores</b> to start the guided setup, or add store elements to your website in the builder: <b>Featured Products</b>, <b>Collections List</b> and <b>Cart</b>. The cart lets shoppers adjust items, and checkout collects their details, shipping choice, coupon codes and payment.</p>"""),
  ("Step 3: Set up shipping", """
<ol class="nf-steps-list">
<li>Go to <b>Payments → Settings → Shipping &amp; Delivery</b>.</li>
<li>Create a shipping zone, name it and choose the countries and states it covers.</li>
<li>Add rates: flat rates, or rates based on order value or weight, such as free shipping over a set amount.</li>
<li>Add a default zone for everywhere else, so no customer sees "no shipping available".</li>
</ol>
<p>At checkout, the cheapest option shows first and free shipping is selected by default when available. You can also offer pickup in store.</p>"""),
  ("Step 4: Fulfil orders", """
<p>Orders appear under <b>Payments → Orders</b>. When you ship, add the tracking number, carrier and tracking link so the customer is kept informed.</p>"""),
  ("Step 5: Market to your buyers", """
<p>Because every order creates a contact, you can send follow-up emails and texts, ask for reviews, recover <a href="/guides/order-bumps-and-upsells/">abandoned checkouts</a> and run campaigns. For single hero products, a product funnel with order bumps and upsells often converts better than a store page.</p>"""),
 ],
 faqs=[
  ("Can I offer free shipping over a certain amount?", "Yes. Shipping rates can be based on order value or weight, so you can set free shipping above a threshold and a standard rate below it."),
  ("Can customers pick up in store?", "Yes. With pickup in store, the shipping section is hidden at checkout and the pickup location is used instead."),
  ("Why isn't my product showing in the store?", "Check that Include in Online Store is switched on for the product."),
 ],
 related_ind=["ecommerce-brands", "restaurants", "soccer-clubs-academies", "gyms-fitness-studios", "salons-barbershops", "photographers"],
 sources=[],
),
dict(
 slug="website-live-chat-widget", cat="Websites and SEO",
 title="How to add live chat to your website and answer every visitor",
 kw="Add Live Chat to Your Website: Setup Guide",
 desc="Add a live chat widget to your website or funnel so visitors can message you, your team or an AI agent, with every chat landing in one inbox.",
 read=5,
 short="A live chat widget lets website visitors message you without leaving the page. In Oceanic Funnels OS, create one under Sites → Chat Widget: choose Live Chat (or SMS/email chat, WhatsApp, or the all-in-one widget), match it to your brand and save. Then select it in your website or funnel settings, or paste the embed code into your site. Every chat lands in your Conversations inbox, where your team or an AI agent can reply.",
 sections=[
  ("Which chat widget to choose", """
<ul>
<li><b>Live chat:</b> real-time chat on the page.</li>
<li><b>SMS / email chat:</b> visitors leave their details and the conversation continues by text or email, even after they leave the site.</li>
<li><b>WhatsApp:</b> visitors start a WhatsApp conversation with your business.</li>
<li><b>All-in-one:</b> lets visitors pick their preferred channel.</li>
</ul>"""),
  ("How to set it up", """
<ol class="nf-steps-list">
<li>Go to <b>Sites → Chat Widget</b> and click <b>New</b>.</li>
<li>Choose the widget type, customise the colours, greeting and icon to match your brand, then save.</li>
<li>On sites built in Oceanic Funnels OS, open the website or funnel <b>Settings</b> and select the widget in the Chat Widget section.</li>
<li>On other sites, click <b>Get Code</b>, copy the code and paste it into your site's tracking code area.</li>
</ol>"""),
  ("Answer chats 24/7 with an AI agent", """
<p>Connect an <a href="/guides/ai-chat-agent-for-business/">AI chat agent</a> to the widget so visitors get instant answers and can book appointments outside business hours, with your team taking over when needed.</p>"""),
  ("Tips", """
<ul>
<li>Use a friendly greeting that invites a question, like "Need a quote? Ask us anything."</li>
<li>Reply fast during business hours; slow live chat is worse than no chat.</li>
<li>Collect a phone number or email early so you can follow up if they leave.</li>
</ul>"""),
 ],
 faqs=[
  ("Where do chat messages go?", "All chats land in the Conversations inbox, next to SMS, email and social messages."),
  ("Can I add the chat widget to a WordPress site?", "Yes. Copy the widget's embed code and add it to your site's header or footer code."),
  ("Can an AI agent answer website chats?", "Yes. An AI chat agent can reply to website chats, answer questions and book appointments."),
 ],
 related_ind=["med-spas", "law-firms", "home-services", "real-estate", "coaches-consultants", "vacation-rentals"],
 sources=[],
),
dict(
 slug="lead-capture-forms-surveys", cat="Lead capture",
 title="Lead capture forms and surveys: build forms that convert and route leads",
 kw="Lead Capture Forms and Surveys That Convert",
 desc="How to build lead capture forms and multi-step surveys, which fields to ask for, and how to route every submission into your CRM and follow-up.",
 read=6,
 short="A lead capture form collects a visitor's details in exchange for something they want: a quote, a consultation, a guide. Ask for as little as you need, usually name, email and phone, and use a multi-step survey when you need more information, because each step feels small. In Oceanic Funnels OS, build forms under Sites → Forms and surveys under Sites → Surveys, add them to any page, and trigger an automation on every submission.",
 sections=[
  ("Form or survey?", """
<ul>
<li><b>Form:</b> all fields on one screen. Best for short requests like contact, callback or download.</li>
<li><b>Survey:</b> one question per step. Best for quotes and qualification, because each step feels quick and you can branch based on answers.</li>
<li><b>Quiz:</b> scored questions with personalised results. See our <a href="/guides/lead-generation-quiz/">quiz guide</a>.</li>
</ul>"""),
  ("Which fields to ask for", """
<ul>
<li>Name, email and phone for most leads.</li>
<li>One or two qualifying questions, such as service needed, budget range or timeline.</li>
<li>An SMS consent checkbox, unchecked by default, if you'll text them. See <a href="/guides/a2p-10dlc-registration/">A2P 10DLC</a>.</li>
</ul>
<p>Every extra field lowers the completion rate, so cut anything you don't use.</p>"""),
  ("Route every submission", """
<p>Each submission creates or updates a contact. Use the <b>Form Submitted</b> or <b>Survey Submitted</b> workflow trigger to send an <a href="/guides/speed-to-lead/">instant reply</a>, tag the lead, create an opportunity in your <a href="/guides/sales-pipeline-management/">pipeline</a> and alert your team.</p>"""),
  ("Where to put your forms", """
<ul>
<li>On landing pages and funnels, above the fold and again further down.</li>
<li>On service pages and blog posts.</li>
<li>As a popup for exit intent or a free resource.</li>
<li>Embedded on other websites with the embed code.</li>
</ul>"""),
 ],
 faqs=[
  ("How many fields should a form have?", "As few as possible. Name, email and phone plus one qualifying question works for most businesses. Use a multi-step survey if you need more."),
  ("Can I embed forms on another website?", "Yes. Forms and surveys can be embedded on any website with the embed code, or shared as a direct link."),
  ("Can a form submission start an automation?", "Yes. Use the Form Submitted or Survey Submitted trigger to send replies, tag leads, create opportunities and notify your team."),
 ],
 related_ind=["home-services", "solar-installers", "insurance-agencies", "law-firms", "roofing", "mortgage-brokers"],
 sources=[],
),
dict(
 slug="lead-generation-quiz", cat="Lead capture",
 title="How to build a lead generation quiz that qualifies your leads",
 kw="How to Build a Lead Generation Quiz That Qualifies Leads",
 desc="Quizzes turn curious visitors into qualified leads. Here's how to build a scored quiz with personalised results and automatic follow-up.",
 read=7,
 short="A lead generation quiz asks visitors a few engaging questions, scores their answers and shows a personalised result, in exchange for their contact details. It qualifies leads automatically because the answers tell you what they need. In Oceanic Funnels OS, build one under Sites → Quizzes: add questions, assign points or categories to answers, design the results page by score tier, save the score to the contact, and use the Quiz Submitted trigger to start follow-up.",
 sections=[
  ("Why quizzes work", """
<p>People enjoy learning something about themselves or their situation. A quiz like "What's your home's solar savings score?" or "Which treatment is right for your skin?" feels like help, not a sales form, and the answers qualify the lead before you ever speak to them.</p>"""),
  ("Plan your quiz", """
<ol>
<li><b>Pick the outcome categories,</b> such as Beginner, Intermediate and Advanced, or three product recommendations.</li>
<li><b>Write 5 to 8 questions</b> that sort people into those categories.</li>
<li><b>Decide what each result recommends</b>, with a clear next step: book, buy or download.</li>
</ol>"""),
  ("Build it step by step", """
<ol class="nf-steps-list">
<li>Go to <b>Sites → Quizzes</b> and click <b>Add Quiz</b>. Start from scratch or a template.</li>
<li>Add questions: single or multiple choice, yes/no, rating, short answer and more.</li>
<li>Assign points or categories to each answer. Use <b>Jump To</b> logic to skip irrelevant questions.</li>
<li>Add contact fields (name, email, phone) before the results.</li>
<li>Design the results page: score tiers, ranges, text and a call-to-action button, under <b>Settings → Edit Results Page</b>.</li>
<li>Set notifications and an autoresponder that can include the results.</li>
<li>Click <b>Integrate</b> to embed the quiz on a page or share the direct link.</li>
</ol>"""),
  ("Follow up based on the result", """
<p>Save scores, tiers and categories to contact fields, then use the <b>Quiz Submitted</b> workflow trigger to send each result group a different follow-up sequence. High scores get a booking invitation; lower scores get nurture content.</p>"""),
 ],
 faqs=[
  ("How many questions should a quiz have?", "Five to eight is a good range: enough to be useful, short enough that people finish."),
  ("Can quiz results be saved to the contact?", "Yes. Scores, tiers and category results can be saved to contact fields and used in automations."),
  ("Can I schedule a quiz to open and close?", "Yes. You can set open and close dates and times, with a custom message for visitors outside that window."),
 ],
 related_ind=["solar-installers", "weight-loss-clinics", "med-spas", "coaches-consultants", "financial-advisors", "course-creators"],
 sources=[],
),
]
