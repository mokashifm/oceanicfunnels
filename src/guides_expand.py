"""Expansions for the guides that match the Launch ($17) offer. Applied on top of guides_a..e by slug.
Each entry can replace sections (by heading), append sections before the last product section,
add FAQs, and set updated/read/plan. Facts are kept to what the plans actually include."""

UPD = "2026-11-10"

EXPAND = {
# ------------------------------------------------------------------ sales funnel
"how-to-build-a-sales-funnel": dict(
 updated=UPD, read=14, plan="launch",
 insert_after="What a sales funnel is",
 add=[
  ("The 5 most common types of sales funnel", """
<p>Pick the funnel type that matches what you sell. The pages are different, but the logic is the same: one offer, one action, then follow-up.</p>
<div class="nf-tablewrap"><table class="nf-table" style="min-width:0"><thead><tr><th>Funnel type</th><th>Best for</th><th>Pages</th><th>The action</th></tr></thead><tbody>
<tr><td><b>Lead magnet funnel</b></td><td>Building an email list for coaches, creators and service businesses</td><td>Opt-in page, thank-you page</td><td>Download a free guide, checklist or template</td></tr>
<tr><td><b>Low-ticket product funnel</b></td><td>Digital products, guides, templates, small physical products</td><td>Sales page, order form, upsell, thank-you</td><td>Buy a $7 to $47 product</td></tr>
<tr><td><b>Booking funnel</b></td><td>Consultations, estimates, appointments, trial classes</td><td>Landing page, calendar, confirmation</td><td>Book a time</td></tr>
<tr><td><b>Webinar funnel</b></td><td>Courses, programs and higher-priced offers</td><td>Registration, reminder, replay, offer</td><td>Register, attend, then buy</td></tr>
<tr><td><b>Product launch funnel</b></td><td>A new course, product or service</td><td>Waitlist, launch sales page, checkout</td><td>Join the waitlist, then buy on launch day</td></tr>
</tbody></table></div>
<p>If you're starting from zero, the low-ticket product funnel is the simplest to build and the fastest to test: one page, one checkout, and you know within days whether people will pay.</p>"""),
 ],
 insert_before_last=[
  ("Example: a $27 digital guide funnel, page by page", """
<p>Here's a complete funnel for a creator selling a $27 meal-prep guide. Every page has one job.</p>
<ol class="nf-steps-list">
<li><b>Sales page.</b> Headline: "The 30-Day Meal Prep Plan: dinner sorted before Monday starts." Below it: what's inside (42 recipes, 4 shopping lists, printable PDF), who it's for, a short story about why it was made, and one button repeated three times: "Get the guide for $27."</li>
<li><b>Order form.</b> Name, email and card. One order bump: "Add the 15-minute breakfast pack for $9." No menu, no links away.</li>
<li><b>Upsell page.</b> Shown once, after payment: "Get the full year of plans for $47 instead of $97, one click, no card re-entry." A "No thanks" link goes straight to the thank-you page.</li>
<li><b>Thank-you page.</b> Download button, what to do first, and where to get help.</li>
</ol>
<p>If 100 visitors land on the sales page and 3 buy, that's a 3% conversion rate. If one in four buyers adds the $9 bump and one in ten takes the $47 upsell, each buyer is worth more than the $27 sticker price, which is what lets you afford ads.</p>"""),
  ("A landing page template you can copy", """
<p>Use this order from top to bottom. It works for products, services and bookings.</p>
<ol>
<li><b>Headline:</b> the result they get, in their words.</li>
<li><b>Sub-headline:</b> what it is and who it's for, in one sentence.</li>
<li><b>Button:</b> the one action, with the price if it's a product.</li>
<li><b>Picture of the outcome:</b> the product, the finished result, or a short video.</li>
<li><b>The problem:</b> two or three sentences about what's frustrating them now.</li>
<li><b>What's included:</b> a short list, each line a benefit.</li>
<li><b>Proof:</b> genuine reviews, results you can stand behind, or credentials.</li>
<li><b>Price and guarantee:</b> what it costs and what happens if it isn't right for them.</li>
<li><b>FAQ:</b> the five questions people ask before buying.</li>
<li><b>Final button:</b> the same action as the top.</li>
</ol>"""),
  ("Common sales funnel mistakes", """
<ul>
<li><b>Too many choices.</b> Several offers or plans on one page slow people down. Sell one thing per funnel.</li>
<li><b>A menu and links that lead away.</b> Every exit is a lost sale. Remove them from funnel pages.</li>
<li><b>Asking for too much too soon.</b> A cold visitor will download a free guide or buy a small product long before they book a $3,000 call.</li>
<li><b>No follow-up.</b> Most people don't buy on the first visit. Without email or SMS follow-up, they're gone.</li>
<li><b>Not tracking each step.</b> Install your ad pixel and analytics before sending traffic, so you know where people drop off.</li>
<li><b>Changing everything at once.</b> Test one change at a time so you know what made the difference.</li>
</ul>"""),
  ("Sales funnel checklist", """
<ul class="nf-check">
<li>One offer and one audience, written down in a sentence.</li>
<li>Landing page with a clear headline, one action and a mobile-friendly layout.</li>
<li>Form, calendar or checkout tested end to end with a real test purchase or booking.</li>
<li>Thank-you page that tells people what happens next.</li>
<li>Payment provider connected and tested.</li>
<li>Ad pixel and analytics installed, with key events firing.</li>
<li>Follow-up set up for people who don't buy straight away.</li>
<li>A weekly check of the conversion rate at each step.</li>
</ul>"""),
 ],
 replace={
  "Building funnels in Oceanic Funnels OS": ("Building funnels in Oceanic Funnels OS", """
<p>Every plan includes unlimited funnels and websites with a drag-and-drop builder, order forms, checkout and payments. The <b>Launch plan ($17/month)</b> covers steps 1 to 3 of this guide: your landing page, order form, checkout and thank-you page. For step 4, the <b>Growth plan ($97/month)</b> adds the CRM and pipelines, lead forms, calendars, email and SMS follow-up and automations. On Scale, a dedicated builder helps you build and grow it. See <a href="/#pricing">all plans</a>.</p>"""),
 },
 faqs_add=[
  ("Do I need a website to have a sales funnel?", "No. A funnel can live on its own domain or subdomain. Many businesses start with a funnel for one offer and add a full website later."),
  ("How long does it take to build a sales funnel?", "A simple one-offer funnel with a sales page, checkout and thank-you page can be built in an afternoon from a template. More complex funnels with webinars or multiple upsells take longer."),
  ("Can I sell digital products with a funnel?", "Yes. Guides, templates, printables and other downloads are some of the easiest things to sell with a funnel, because there's nothing to ship."),
  ("How much does it cost to build a sales funnel?", "The software can start from $17 a month on our Launch plan. Your other costs are your domain, payment-processing fees and any ads you run."),
 ],
),

# ------------------------------------------------------------------ order bumps
"order-bumps-and-upsells": dict(
 updated=UPD, read=12, plan="launch",
 replace={
  "Setting it up in Oceanic Funnels OS": ("Setting it up in Oceanic Funnels OS", """
<ol class="nf-steps-list">
<li>Add your products to the funnel step's products, and mark the add-on as a <b>Bump Product</b>.</li>
<li>Open the order form on the page, go to its advanced settings and open <b>Order bump options</b>.</li>
<li>Turn on <b>Order Bump</b>, choose the bump product and save.</li>
<li>Add an upsell step after the checkout step in the funnel for your one-click offer.</li>
<li>Run a test purchase and check the bump, the upsell and the thank-you page all work.</li>
</ol>
<p>Funnel checkouts with two-step order forms, order bumps and one-click upsells are included on every plan, starting with Launch at $17 a month. Automatic email and SMS follow-up for abandoned checkouts is included from Growth. On Scale, your builder helps you set up the checkout and follow-up.</p>"""),
  "Two-step order forms": ("Two-step order forms", """
<p>A two-step order form asks for contact details first, then payment. Because the contact is saved after step one, you can follow up with anyone who doesn't finish checkout. That follow-up by email and SMS is included from the Growth plan.</p>"""),
 },
 insert_before_last=[
  ("Order bump and upsell examples by business", """
<div class="nf-tablewrap"><table class="nf-table" style="min-width:0"><thead><tr><th>Business</th><th>Main product</th><th>Order bump</th><th>Upsell</th></tr></thead><tbody>
<tr><td>Recipe creator</td><td>Meal-prep guide, $27</td><td>Breakfast recipe pack, $9</td><td>12-month plan bundle, $47</td></tr>
<tr><td>Teacher</td><td>Worksheet kit, $19</td><td>Answer-key video walkthroughs, $7</td><td>Full-year curriculum bundle, $59</td></tr>
<tr><td>Coach</td><td>Starter workbook, $17</td><td>Goal-setting templates, $7</td><td>Group coaching seat, $197</td></tr>
<tr><td>Skincare brand</td><td>Cleanser, $28</td><td>Travel-size moisturiser, $9</td><td>3-month routine bundle, $79</td></tr>
<tr><td>Ceramics shop</td><td>Mug, $32</td><td>Gift wrap and card, $5</td><td>Matching set of 4, $99</td></tr>
</tbody></table></div>
<p>The pattern: the bump makes the main purchase better right now, and the upsell is the bigger version of what they just bought.</p>"""),
  ("How to price bumps and upsells", """
<ul>
<li><b>Order bump:</b> usually 10% to 40% of the main product price. Low enough that ticking the box needs no thinking.</li>
<li><b>Upsell:</b> can be higher than the main product, as long as it's clearly the next step. Offer a real saving or bonus for taking it now.</li>
<li><b>Downsell:</b> a smaller or split-payment version of the upsell for people who said no.</li>
</ul>
<p>Only use "this page only" pricing if it's true. If the price is available later anyway, say so, or don't use the claim at all.</p>"""),
  ("Upsell page copy template", """
<ol>
<li><b>Confirm the order:</b> "You're in. Your order is confirmed." This calms the buyer and stops them worrying about the payment.</li>
<li><b>Name the next step:</b> "Most people who get the guide also want the full year of plans."</li>
<li><b>Show what they get:</b> three to five short lines.</li>
<li><b>The offer:</b> the price, what they save, and that it's one click with no card re-entry.</li>
<li><b>Two buttons:</b> "Yes, add it to my order" and a plain "No thanks, take me to my download."</li>
</ol>"""),
  ("What to measure", """
<ul>
<li><b>Bump take rate:</b> the share of buyers who tick the bump. 15% to 35% is a common range.</li>
<li><b>Upsell take rate:</b> the share who accept the upsell. Often 5% to 20%.</li>
<li><b>Average order value:</b> total revenue divided by orders. This is the number bumps and upsells exist to raise.</li>
</ul>
<p>These ranges vary a lot by offer and audience, so treat them as a starting point and measure your own.</p>"""),
  ("Common mistakes to avoid", """
<ul>
<li><b>An unrelated bump.</b> A random add-on feels like a trick. It should make the main purchase better.</li>
<li><b>A bump that costs more than the main product.</b> That's an upsell, and it belongs after payment.</li>
<li><b>A chain of upsells.</b> One upsell and one downsell is plenty for most funnels.</li>
<li><b>Fake urgency.</b> "Only today" when it isn't true damages trust and can break advertising rules.</li>
<li><b>Hiding the "No thanks" link.</b> Make it easy to decline. People who feel tricked ask for refunds.</li>
</ul>"""),
 ],
 faqs_add=[
  ("Do order bumps annoy customers?", "Not when they're small, relevant and clearly optional. One bump on the order form is normal. Several bumps stacked up starts to feel like clutter."),
  ("Should every funnel have an upsell?", "Only if you have a natural next step. A forced upsell that doesn't fit hurts trust more than it adds revenue."),
  ("Can I use order bumps on a $17 product?", "Yes. Low-priced products are where bumps help most, because a $7 or $9 add-on can raise the order value by a third or more."),
 ],
),

# ------------------------------------------------------------------ website
"build-a-business-website": dict(
 updated=UPD, read=12, plan="launch",
 insert_after="Website or funnel?",
 add=[
  ("The pages every small business website needs", """
<div class="nf-tablewrap"><table class="nf-table" style="min-width:0"><thead><tr><th>Page</th><th>Its job</th><th>Must include</th></tr></thead><tbody>
<tr><td><b>Home</b></td><td>Say what you do and send people to the next step</td><td>Headline, who it's for, main button, proof</td></tr>
<tr><td><b>Services or products</b></td><td>Help people choose</td><td>What's included, prices or "from" prices, button on each</td></tr>
<tr><td><b>About</b></td><td>Build trust</td><td>Who you are, why you do it, photo of you or your team</td></tr>
<tr><td><b>Contact</b></td><td>Make it easy to reach you</td><td>Phone, email, form or booking, opening hours, location if you have one</td></tr>
<tr><td><b>FAQ</b></td><td>Answer objections before they stop a sale</td><td>Price, timing, what happens next, refunds</td></tr>
<tr><td><b>Privacy policy and terms</b></td><td>Stay compliant</td><td>How you use data and the rules of buying from you</td></tr>
</tbody></table></div>
<p>Start with these six. Add a blog and individual service pages later, as you learn what people search for.</p>"""),
  ("Homepage structure, top to bottom", """
<ol>
<li><b>Headline and sub-headline:</b> what you do and who you do it for.</li>
<li><b>Main button:</b> buy, book, call or get a quote.</li>
<li><b>Picture of your work or product.</b></li>
<li><b>Three reasons to choose you</b>, each one a benefit, not a feature.</li>
<li><b>Your services or best products</b> with links.</li>
<li><b>Proof:</b> genuine reviews, photos, results or credentials.</li>
<li><b>How it works:</b> three steps from first contact to result.</li>
<li><b>FAQ</b> and a final button.</li>
</ol>"""),
 ],
 insert_before_last=[
  ("Writing website copy that turns visitors into customers", """
<ul>
<li><b>Lead with the result.</b> "Spotless homes, every two weeks" beats "Professional cleaning solutions."</li>
<li><b>Use their words.</b> Write the way your customers describe their problem, not the way your industry does.</li>
<li><b>Be specific.</b> Prices, timeframes and numbers are more convincing than adjectives.</li>
<li><b>One idea per section</b>, with a short heading people can scan.</li>
<li><b>Repeat the main button</b> after every two or three sections.</li>
</ul>"""),
  ("Domains, simply explained", """
<p>Your domain is your address, such as <i>yourbusiness.com</i>. Buy it from any domain registrar; it usually costs around $10 to $20 a year. You can use the main domain for your website and a subdomain, such as <i>shop.yourbusiness.com</i>, for a funnel or store. Keep the domain registered in your own name so you always own it.</p>"""),
  ("Website launch checklist", """
<ul class="nf-check">
<li>Every page has a unique title and meta description.</li>
<li>Domain connected and the padlock (https) showing.</li>
<li>Every button and link tested on a phone and a computer.</li>
<li>Contact form, booking or checkout tested with a real test.</li>
<li>Privacy policy and terms pages published.</li>
<li>Analytics and your ad pixel installed.</li>
<li>Site submitted to Google Search Console with your sitemap.</li>
</ul>"""),
  ("What it costs to build a business website", """
<p>On Oceanic Funnels, unlimited websites and funnels are included on every plan, starting with Launch at $17 a month, which also includes an online store, checkout and payments. Your other costs are the domain and payment-processing fees if you sell online. Lead forms, booking calendars, live chat and email or SMS follow-up are included from the Growth plan at $97 a month. See <a href="/#pricing">all plans</a>.</p>"""),
  ("Common website mistakes", """
<ul>
<li><b>A vague headline</b> that doesn't say what you do in the first few seconds.</li>
<li><b>Too many buttons</b> pointing to different actions on the same screen.</li>
<li><b>No prices at all.</b> Even "from" prices help people decide whether to contact you.</li>
<li><b>Slow pages</b> from huge images. Compress photos before you upload them.</li>
<li><b>Out-of-date details:</b> old opening hours, phone numbers or offers.</li>
</ul>"""),
 ],
 faqs_add=[
  ("How long does it take to build a business website?", "With a template, a simple five or six page site can be ready in a day or two. Most of the time goes into writing the words and gathering photos."),
  ("Website or sales funnel: which should I build first?", "If you sell one main product or offer, start with a funnel and add a website later. If people need to browse several services before contacting you, start with the website."),
  ("Can I sell products on my website?", "Yes. You can add an online store with products, a cart and checkout to your website on every plan."),
 ],
),

# ------------------------------------------------------------------ online store
"set-up-an-online-store": dict(
 updated=UPD, read=12, plan="launch", append_mode=True,
 insert_after="Before you start",
 add=[
  ("Store or product funnel?", """
<div class="nf-tablewrap"><table class="nf-table" style="min-width:0"><thead><tr><th></th><th>Online store</th><th>Product funnel</th></tr></thead><tbody>
<tr><td>Best for</td><td>Several products people browse and compare</td><td>One hero product or offer</td></tr>
<tr><td>How people buy</td><td>Browse, add to cart, check out</td><td>Read one page, buy in one step</td></tr>
<tr><td>Extras</td><td>Collections, cart, coupons, shipping zones</td><td>Order bumps and one-click upsells</td></tr>
<tr><td>Works well with ads?</td><td>Yes, for catalogue and collection ads</td><td>Yes, usually the higher conversion rate for one product</td></tr>
</tbody></table></div>
<p>You don't have to choose: many sellers run a store for the full range and a funnel for their bestseller.</p>"""),
 ],
 insert_before_last=[
  ("Writing product pages that sell", """
<ul>
<li><b>Photos first:</b> at least three, including the product in use and a close-up. Use the same background across products.</li>
<li><b>A one-line promise</b> under the name: what it does for the buyer.</li>
<li><b>Short description:</b> three to five lines covering what it is, who it's for and why it's different.</li>
<li><b>Details:</b> size, materials, what's in the box, delivery time.</li>
<li><b>Genuine reviews</b> once you have them.</li>
<li><b>Clear price and one "Add to cart" button.</b></li>
</ul>"""),
  ("Pricing, coupons and free shipping", """
<ul>
<li><b>Price from your costs up:</b> product, packaging, shipping, payment fees and the cost of getting a customer.</li>
<li><b>Free shipping over a threshold</b> set a little above your average order encourages bigger baskets.</li>
<li><b>Use coupons on purpose:</b> a first-order code for email sign-ups, or a code for a launch, rather than permanent discounts.</li>
</ul>"""),
  ("A checkout that doesn't lose sales", """
<ul>
<li>Ask only for what you need to fulfil the order.</li>
<li>Show the full price, including shipping, before the payment step. Surprise costs are a top reason people abandon checkout.</li>
<li>Offer the payment methods your customers expect through your payment provider.</li>
<li>Show your returns policy and a contact option near the payment button.</li>
<li>Test the checkout on a phone, where most shoppers buy.</li>
</ul>"""),
  ("Store launch checklist", """
<ul class="nf-check">
<li>Payment provider connected and a real test order completed.</li>
<li>Every product has photos, description, price and Include in Online Store switched on.</li>
<li>Shipping zones and rates cover every place you sell to, including a default zone.</li>
<li>Returns, shipping, privacy and terms pages published.</li>
<li>Order confirmation tested.</li>
<li>Analytics and your ad pixel installed, with purchase tracking tested.</li>
</ul>"""),
  ("How to get your first sales", """
<ol>
<li><b>Start with people who know you.</b> Email your contacts and post to your own social accounts with a launch offer, such as free shipping for the first week.</li>
<li><b>Ask your first buyers for reviews</b> and photos, then add the genuine ones to your product pages.</li>
<li><b>Post the product in use,</b> not just the product. Short videos of how it's made or used work especially well.</li>
<li><b>Run small ads only after tracking works.</b> Install your ad pixel, test a purchase, then start with a small daily budget on your best product.</li>
<li><b>Bring back people who almost bought.</b> Reminders to visitors who added to cart but didn't check out are often the cheapest sales you'll get.</li>
</ol>"""),
  ("Common online store mistakes", """
<ul>
<li><b>Too many products at launch.</b> Start with your best few and add more once they sell.</li>
<li><b>Poor or inconsistent photos.</b> They're the first thing shoppers judge.</li>
<li><b>Hidden shipping costs</b> that only appear at the last step.</li>
<li><b>No returns policy</b> or contact details, which makes a new store look risky.</li>
<li><b>Never testing on a phone</b>, where most people shop.</li>
</ul>"""),
 ],
 replace={
  "Step 5: Market to your buyers": ("Step 5: Market to your buyers", """
<p>Every order creates a contact, so your buyers are saved in one place. On the Growth plan you can then send follow-up emails and texts, ask for reviews, recover <a href="/guides/order-bumps-and-upsells/">abandoned checkouts</a> and run campaigns. For a single hero product, a product funnel with order bumps and upsells often converts better than a store page.</p>"""),
 },
 faqs_add=[
  ("Which plan includes the online store?", "The online store, checkout and payments are included on every plan, starting with Launch at $17 a month. Email and SMS marketing to your buyers is included from Growth."),
  ("Can I sell digital products in my store?", "Yes. You can sell digital products as well as physical ones."),
  ("Do I need my own domain for my store?", "It's strongly recommended. A store on your own domain looks more trustworthy and keeps your brand in one place."),
 ],
),

# ------------------------------------------------------------------ online course
"create-and-sell-an-online-course": dict(
 updated=UPD, read=13,
 plan_box=("Sell it with a funnel, host it on Growth",
           "Launch ($17/month) covers the sales page, checkout and payments. Course hosting, member areas and drip lessons are included from Growth ($97/month).",
           "/#pricing", "See the plans"),
 insert_after="Plan your course",
 add=[
  ("Validate the idea before you build it", """
<p>The most expensive course is the one nobody buys. Before recording a single lesson:</p>
<ol>
<li><b>Write the promise in one sentence:</b> "In 4 weeks, you'll be able to..."</li>
<li><b>Ask your audience</b> what they struggle with most, in their own words.</li>
<li><b>Pre-sell it:</b> build a simple sales page with a launch price and see if people buy before it exists. If they do, record it. If they don't, you've saved weeks.</li>
<li><b>Start with a smaller product,</b> such as a guide or workshop, to learn what your audience will pay for.</li>
</ol>"""),
  ("How to price an online course", """
<div class="nf-tablewrap"><table class="nf-table" style="min-width:0"><thead><tr><th>Format</th><th>Typical price range</th><th>Best for</th></tr></thead><tbody>
<tr><td>Mini course or workshop</td><td>$19 to $99</td><td>One specific skill, new audiences</td></tr>
<tr><td>Signature course</td><td>$197 to $997</td><td>A full transformation, an established audience</td></tr>
<tr><td>Course with coaching or community</td><td>$500 and up</td><td>Results that need support and accountability</td></tr>
<tr><td>Membership</td><td>$19 to $99 a month</td><td>Ongoing content, templates and community</td></tr>
</tbody></table></div>
<p>These are common ranges, not rules. Price on the value of the outcome and your audience's ability to pay, and test.</p>"""),
 ],
 insert_before_last=[
  ("Your course sales page structure", """
<ol>
<li><b>Headline:</b> the outcome and the timeframe.</li>
<li><b>Who it's for, and who it isn't for.</b></li>
<li><b>The problem</b> and why other approaches haven't worked.</li>
<li><b>The modules:</b> one line each, written as results.</li>
<li><b>About you:</b> why you're the right person to teach it.</li>
<li><b>Proof:</b> genuine student results once you have them.</li>
<li><b>Price, bonuses and your guarantee.</b></li>
<li><b>FAQ</b> and a final button.</li>
</ol>"""),
  ("A simple 4-week launch plan", """
<div class="nf-tablewrap"><table class="nf-table" style="min-width:0"><thead><tr><th>Week</th><th>Focus</th><th>What to do</th></tr></thead><tbody>
<tr><td>1</td><td>Warm up</td><td>Share tips from the course topic and invite people to a free waitlist or lesson</td></tr>
<tr><td>2</td><td>Teach</td><td>Run a free workshop or <a href="/guides/run-a-webinar/">webinar</a> that solves one small problem</td></tr>
<tr><td>3</td><td>Open</td><td>Open the doors with a launch price or bonus that genuinely ends</td></tr>
<tr><td>4</td><td>Close</td><td>Answer questions, share the deadline, and close the offer when you said you would</td></tr>
</tbody></table></div>"""),
  ("What you need to sell a course", """
<p>You need a sales page, a checkout, a place to host lessons, and email to deliver and follow up. In Oceanic Funnels, the sales funnel and checkout are included from Launch ($17/month). Course hosting with modules, lessons and drip schedules, member areas, communities and email follow-up are included from Growth ($97/month), all in one system. See <a href="/#pricing">all plans</a>.</p>"""),
  ("Recording your lessons without a studio", """
<ul>
<li><b>Camera:</b> a recent phone on a stand, at eye level, facing a window for soft light.</li>
<li><b>Sound matters more than video.</b> A clip-on microphone costs little and makes the biggest difference.</li>
<li><b>Screen lessons:</b> record your screen with a voice-over for software, slides or worked examples.</li>
<li><b>Keep it short:</b> one idea per lesson, 5 to 15 minutes, with one task at the end.</li>
<li><b>Batch it:</b> record a whole module in one session so the look and sound stay consistent.</li>
</ul>"""),
  ("Keeping students engaged to the end", """
<ul>
<li>Give a quick win in the first lesson, so students feel progress straight away.</li>
<li>End every lesson with one small action.</li>
<li>Use drip schedules or weekly releases to keep a steady pace.</li>
<li>Add a <a href="/guides/paid-online-community/">community</a> or live Q&amp;A so students can ask questions.</li>
<li>Send short check-in emails when someone hasn't logged in for a while.</li>
</ul>
<p>Students who finish get results, and students who get results buy your next course and recommend you.</p>"""),
 ],
 faqs_add=[
  ("How long should an online course be?", "As short as it can be while delivering the promise. Many successful courses are 1 to 3 hours of video split into short lessons."),
  ("Can I pre-sell a course before it's finished?", "Yes, and it's a smart way to validate the idea. Be clear about the start date and what buyers get, and refund anyone if you decide not to deliver."),
  ("Which plan do I need to host a course?", "Course hosting, memberships and communities are included on Growth, AI Pro and Scale. Launch covers the sales page and checkout."),
 ],
),
}


def apply(guides):
    by = {g["slug"]: g for g in guides}
    for slug, x in EXPAND.items():
        g = by[slug]
        secs = list(g["sections"])
        if "replace" in x:
            secs = [x["replace"].get(h, (h, c)) for h, c in secs]
        if "add" in x:
            i = [h for h, _ in secs].index(x["insert_after"]) + 1
            secs = secs[:i] + x["add"] + secs[i:]
        if "insert_before_last" in x:
            if x.get("append_mode"): secs = secs + x["insert_before_last"]
            else: secs = secs[:-1] + x["insert_before_last"] + secs[-1:]
        g["sections"] = secs
        g["faqs"] = list(g["faqs"]) + x.get("faqs_add", [])
        for k in ("updated", "read", "plan", "plan_box"):
            if k in x: g[k] = x[k]
    return guides
