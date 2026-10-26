"""Privacy Policy and Terms of Service content (HTML fragments).

These are a starting draft, not legal advice: have a lawyer review them.
"""

EFFECTIVE = "October 26, 2026"
ENTITY = "Oceanic Funnels"
ADDRESS = "Bahawalpur, Pakistan"
LAW = "Pakistan"
EMAIL = "hello@oceanicfunnels.com"

PRIVACY = [
("Who we are", f"""
<p>This Privacy Policy explains how {ENTITY} ("Oceanic Funnels", "we", "us") collects, uses and protects personal information when you visit oceanicfunnels.com, contact us, or use Oceanic Funnels OS and our done-for-you services (together, the "Services").</p>
<p>You can reach us at <b>{EMAIL}</b>. We are based in {ADDRESS}.</p>"""),

("Information we collect", """
<ul>
<li><b>Information you give us:</b> your name, email, phone number, business name, website, billing details and anything you send us in forms, chats, calls or emails.</li>
<li><b>Account information:</b> login details, plan, settings and the people you add as team members.</li>
<li><b>Payment information:</b> payments are handled by our payment processor. We receive confirmation of payment and limited card details (such as the last four digits and expiry date), not your full card number.</li>
<li><b>Usage information:</b> pages visited, features used, device and browser type, IP address, and approximate location, collected through server logs and cookies.</li>
<li><b>Communications:</b> records of support conversations and the messages you send to us by email, SMS or chat.</li>
</ul>"""),

("Information you store in Oceanic Funnels OS", """
<p>When you use Oceanic Funnels OS, you may upload or collect information about your own leads and customers ("Customer Data"), such as contacts, messages, bookings and payments. You control that data and decide how it is used. We process Customer Data only to provide the Services to you, on your instructions.</p>
<p>You are responsible for having a lawful basis and the required consent to collect and contact the people in your account, including consent for marketing emails, text messages and calls under laws such as the TCPA, CAN-SPAM, CASL and GDPR.</p>"""),

("How we use information", """
<ul>
<li>To provide, set up, maintain and support the Services, including done-for-you builds.</li>
<li>To process payments, manage subscriptions and send receipts and account notices.</li>
<li>To respond to questions and provide customer support.</li>
<li>To send product updates and marketing about our own Services, which you can opt out of at any time.</li>
<li>To keep the Services secure, prevent fraud and abuse, and comply with the law.</li>
<li>To understand how the website and Services are used so we can improve them.</li>
</ul>"""),

("Text messaging (SMS)", """
<p>If you give us your mobile number and agree to receive text messages from Oceanic Funnels, we may send you messages about your account, appointments, support and offers. Message frequency varies. Message and data rates may apply. Reply <b>STOP</b> to opt out or <b>HELP</b> for help at any time.</p>
<p><b>No mobile information will be shared with third parties or affiliates for marketing or promotional purposes.</b> Text messaging opt-in data and consent are not shared with any third parties, except service providers that deliver the messages on our behalf.</p>"""),

("How we share information", """
<p>We do not sell your personal information. We share it only:</p>
<ul>
<li><b>With service providers</b> that help us run the Services, such as hosting and infrastructure, payment processing, email and SMS delivery, telephony, AI features, analytics and customer support tools. They may use the information only to provide services to us.</li>
<li><b>When required by law</b>, or to protect our rights, users or the public.</li>
<li><b>In a business transfer</b>, such as a merger or sale of assets, subject to this policy.</li>
<li><b>With your permission</b>, or at your direction.</li>
</ul>"""),

("AI features", """
<p>Oceanic Funnels OS includes AI agents and AI writing tools. When you use them, the content you provide (for example a conversation the AI agent replies to) is processed by AI service providers to generate a response. We do not use your Customer Data to train our own models.</p>"""),

("Cookies", """
<p>We use cookies and similar technologies to keep you signed in, remember preferences, measure traffic and, where allowed, measure advertising. You can control cookies in your browser settings. Blocking some cookies may stop parts of the Services from working.</p>"""),

("How long we keep information", """
<p>We keep personal information for as long as your account is active and as needed to provide the Services, then for as long as required for legal, tax, accounting and security purposes. When you close your account, you can export your Customer Data first. We delete or anonymise it within a reasonable period after closure unless the law requires us to keep it.</p>"""),

("Security", """
<p>We use reasonable technical and organisational measures to protect personal information, including encryption in transit, access controls and trusted infrastructure providers. No method of transmission or storage is completely secure, so we cannot guarantee absolute security.</p>"""),

("Your rights", """
<p>Depending on where you live, you may have the right to access, correct, delete or export your personal information, to object to or restrict certain processing, and to withdraw consent. California residents may request information about the categories of personal information we collect and how it is used, and we will not discriminate against you for using these rights.</p>
<p>To make a request, email <b>{EMAIL}</b>. If you are a contact of one of our customers, please contact that business directly, since it controls your data; we will help them respond.</p>""".replace("{EMAIL}", EMAIL)),

("International transfers", """
<p>We and our service providers may process information in countries other than yours, including the United States. Where required, we use appropriate safeguards for these transfers.</p>"""),

("Children", """
<p>The Services are for businesses and are not directed to children under 16. We do not knowingly collect personal information from children.</p>"""),

("Changes to this policy", """
<p>We may update this policy from time to time. If we make significant changes, we will post the new version here with a new effective date and, where appropriate, notify you by email or in your account.</p>"""),

("Contact us", f"""
<p>Questions about this policy or your information: email <b>{EMAIL}</b>. {ENTITY}, {ADDRESS}.</p>"""),
]

TERMS = [
("Agreement", f"""
<p>These Terms of Service ("Terms") are an agreement between you and {ENTITY} ("Oceanic Funnels", "we", "us") and govern your use of oceanicfunnels.com, Oceanic Funnels OS (the "Platform") and our done-for-you services (together, the "Services"). By creating an account, paying for a plan or using the Services, you agree to these Terms. If you use the Services for a business, you confirm you can accept these Terms on its behalf.</p>"""),

("Your account", """
<ul>
<li>You must give accurate information and keep your login details secure. You are responsible for everything that happens under your account, including the actions of team members you invite.</li>
<li>You must be at least 18 years old and use the Services for business purposes.</li>
<li>Tell us right away at hello@oceanicfunnels.com if you think your account has been accessed without permission.</li>
</ul>"""),

("Plans, billing and renewal", """
<ul>
<li><b>Subscriptions:</b> plans are billed monthly in advance and renew automatically each month until cancelled.</li>
<li><b>Prices:</b> current prices are shown on our website. We may change prices with at least 30 days' notice. Changes apply from your next billing period.</li>
<li><b>Founding member pricing:</b> if you join under a founding member offer, you keep the price you signed up at for as long as your subscription stays active and in good standing on the same plan. The offer ends if you cancel, downgrade or your account is suspended for non-payment.</li>
<li><b>Taxes:</b> prices exclude taxes unless stated. You are responsible for applicable taxes.</li>
<li><b>Failed payments:</b> if a payment fails, we may retry it and may suspend the Services until the balance is paid.</li>
</ul>"""),

("Usage charges and add-ons", """
<ul>
<li>Email, SMS, phone calls, WhatsApp messages and AI agent usage are charged on a pay-as-you-go basis from your account wallet at the rates shown in your account. AI chat replies are billed by the tokens used and voice calls by the minute.</li>
<li>You authorise us to recharge your wallet automatically when it falls below the threshold you set.</li>
<li>Add-ons (such as WhatsApp messaging or AI Agent Unlimited) are billed monthly in addition to your plan, and third-party fees (such as WhatsApp's per-message fees and carrier fees) may apply.</li>
<li>Usage charges and wallet balances are non-refundable except where required by law.</li>
</ul>"""),

("Done-for-you services", """
<ul>
<li><b>Growth plan:</b> includes setup of your account in the first week, five core automations, one AI chat agent, a niche template, and five edit requests each month.</li>
<li><b>Done-For-You plan:</b> includes a custom sales funnel and automated backend built by our team, plus ten edit requests or one new page each month.</li>
<li><b>Extra funnels:</b> funnels built by our team beyond your plan are $297 one time per funnel. You can build unlimited funnels yourself on every plan.</li>
<li>Monthly edit requests and pages do not roll over to the next month.</li>
<li><b>Your part:</b> you agree to provide the content, logins, brand assets and approvals we need, on time. Timelines, including our "live in 14 days" target, start once we have what we need, and are extended by any delays on your side. If we miss the 14-day launch target for reasons within our control, your next month's Done-For-You fee is waived.</li>
<li>You are responsible for reviewing and approving everything we build before it goes live, including claims in your copy and compliance with laws that apply to your business.</li>
</ul>"""),

("Cancellation and refunds", """
<ul>
<li>You can cancel any time from your account or by emailing hello@oceanicfunnels.com. Cancellation takes effect at the end of your current billing period, and you keep access until then.</li>
<li><b>30-day money-back guarantee:</b> if you cancel the OS or Growth plan within 30 days of your first payment for your first subscription, we will refund that first subscription payment. This does not cover usage charges, add-ons, third-party fees or one-time build fees.</li>
<li>The 30-day money-back guarantee does not apply to the Done-For-You plan, because our team starts building your funnel and backend right away.</li>
<li>Except as stated above or required by law, payments are non-refundable.</li>
</ul>"""),

("Acceptable use", """
<p>You agree not to use the Services to:</p>
<ul>
<li>Send messages, emails or calls to people who have not given the consent required by law, or ignore opt-out requests.</li>
<li>Send spam, phishing, or deceptive or misleading content, or impersonate anyone.</li>
<li>Promote illegal products or services, or content that is hateful, harassing, sexually explicit, or that infringes someone else's rights.</li>
<li>Upload malware, attack, overload or try to gain unauthorised access to the Services or other systems.</li>
<li>Resell, sublicense or provide the Platform to third parties as your own software product without our written agreement.</li>
</ul>
<p>To send text messages in the United States, you must complete carrier registration (A2P 10DLC) and follow carrier rules. We may pause messaging, suspend or terminate accounts that break these rules or put the Services, our providers or other customers at risk.</p>"""),

("Your content and data", """
<p>You own the content and Customer Data you put into the Services. You give us permission to host, copy, process and display it only as needed to provide and support the Services. You are responsible for your content and for having the rights and consents to use it. You can export your data while your account is active. See our <a href="/privacy/">Privacy Policy</a> for how we handle personal information.</p>"""),

("Our property", """
<p>The Services, including the Platform, our software, templates, designs and brand, belong to us or our licensors. We give you a limited, non-exclusive, non-transferable right to use the Services during your subscription, for your own business. Funnels and pages we build for you are yours to use once paid for, but templates and components we reuse across customers remain ours.</p>"""),

("Third-party services", """
<p>The Services rely on and connect to third-party services, such as payment processors, messaging carriers, email providers, AI providers, ad platforms and app integrations. Your use of those services may be subject to their own terms and fees. We are not responsible for third-party services and their availability.</p>"""),

("No guaranteed results", """
<p>We build tools and funnels designed to help you get and convert customers, but results depend on your offer, market, traffic and many other factors outside our control. <b>We do not guarantee any specific revenue, leads, sales or rankings.</b> Examples, results and figures shown on our website are illustrations or past results of specific customers and are not promises of what you will achieve.</p>"""),

("Availability and changes", """
<p>We aim to keep the Services available and reliable, but they may be interrupted for maintenance, updates or reasons outside our control. We may add, change or remove features over time. If we remove a core feature of your plan, we will tell you in advance.</p>"""),

("Disclaimers", """
<p>Except as expressly stated in these Terms, the Services are provided "as is" and "as available", without warranties of any kind, whether express or implied, including warranties of merchantability, fitness for a particular purpose and non-infringement, to the fullest extent permitted by law.</p>"""),

("Limitation of liability", """
<p>To the fullest extent permitted by law, we are not liable for any indirect, incidental, special, consequential or punitive damages, or for lost profits, revenue, data or business opportunities. Our total liability for any claim relating to the Services is limited to the amount you paid us in the 3 months before the event giving rise to the claim.</p>"""),

("Indemnity", """
<p>You agree to defend and compensate us for claims, losses and costs (including reasonable legal fees) that arise from your content, your messages to your contacts, your use of the Services in breach of these Terms, or your breach of any law.</p>"""),

("Suspension and termination", """
<p>We may suspend or terminate your access if you breach these Terms, fail to pay, or use the Services in a way that creates legal or security risk. Where reasonable, we will give you notice and a chance to fix the problem first. After termination, you may request an export of your data within 30 days.</p>"""),

("Governing law and disputes", f"""
<p>These Terms are governed by the laws of {LAW}, without regard to conflict-of-law rules. Before starting any formal dispute, you agree to contact us at hello@oceanicfunnels.com so we can try to resolve it informally within 30 days.</p>"""),

("Changes to these Terms", """
<p>We may update these Terms from time to time. If changes are significant, we will notify you by email or in your account at least 15 days before they take effect. Continuing to use the Services after that means you accept the updated Terms.</p>"""),

("Contact", f"""
<p>{ENTITY}, {ADDRESS}. Email: <b>{EMAIL}</b>.</p>"""),
]
