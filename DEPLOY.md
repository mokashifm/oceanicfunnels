# Deploy oceanicfunnels.com on Cloudflare Pages (free)

The live website is the `site/` folder of this repo. Cloudflare Pages publishes it on every push.

## 1. Put the domain on Cloudflare (once, about 10 minutes)
1. Create a free account at cloudflare.com → **Add a domain** → `oceanicfunnels.com` → choose the **Free** plan.
2. Cloudflare scans your current DNS records. Keep any email (MX/TXT) records it finds.
3. Cloudflare shows you **2 nameservers**. In GoDaddy → My Products → oceanicfunnels.com → **DNS → Nameservers → Change → "I'll use my own nameservers"** → paste both → Save.
4. Wait for the "Your domain is active" email (usually under an hour, can take up to 24h).

## 2. Connect this GitHub repo (once, 2 minutes)
1. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git**.
2. Connect GitHub, pick **mokashifm/oceanicfunnels**.
3. Build settings: Framework preset **None**, Build command **empty**, Build output directory **`site`** → **Save and Deploy**.
4. You get a preview link like `oceanicfunnels.pages.dev`. Open it and check it.

## 3. Connect your domain
1. In the project → **Custom domains → Set up a domain** → add `www.oceanicfunnels.com`, then add `oceanicfunnels.com` too.
2. Cloudflare creates the DNS records automatically (because the domain is on Cloudflare).
3. Make one the main address: **Rules → Redirect Rules → Create** → "Redirect from root to WWW" template (the canonical tag and sitemap use `https://www.oceanicfunnels.com`).

## 4. Point the app subdomain at your white-label app
1. In your white-label platform, add the custom domain `app.oceanicfunnels.com` for the agency/app login. It gives you a CNAME target.
2. Cloudflare → **DNS → Add record** → Type `CNAME`, Name `app`, Target = what the platform gave you → **Proxy status: DNS only (grey cloud)** → Save.
3. Do the same for any other platform subdomains it asks for (e.g. checkout or link domains), always **DNS only**.

## 5. Updating the site later
Every push to the `main` branch of this repo deploys automatically. Every deploy is kept, so you can roll back in one click under **Deployments**.

## 6. Before you share the link
- Replace the plan button links (`plan1`, `plan2`, `plan3` in src/build.py) with your checkout / order form links, then rebuild and push. Right now they scroll to the pricing section.
- "Log in" points to `https://app.oceanicfunnels.com`. Change `login` in src/build.py if your app lives elsewhere.
- "Talk to our team" points to the CTA section. Set `book_url` to your calendar link.

## 7. After it's live (SEO)
1. **Google Search Console** → Add property → Domain `oceanicfunnels.com` → verify with the TXT record (add it in Cloudflare DNS) → submit `https://www.oceanicfunnels.com/sitemap.xml` → URL Inspection → Request indexing for the homepage.
2. **Bing Webmaster Tools** → import from Google Search Console (Bing's index feeds ChatGPT search).
3. Test the share card: paste the link into a WhatsApp chat or LinkedIn post; you should see the "Stop fishing for customers. Build the net." image.
4. Run **PageSpeed Insights** on the homepage; aim for 90+ on mobile.

## What's in this folder
| File | Purpose |
|---|---|
| index.html | The homepage, with title, description, social tags and schema built in |
| 404.html | "This fish got away" page for broken links |
| robots.txt | Allows Google and AI crawlers (GPTBot, ClaudeBot, PerplexityBot) |
| sitemap.xml | Tells search engines what to index |
| _headers | Security headers and long caching for images |
| favicon.ico, icon.svg, icon-192.png, icon-512.png, apple-touch-icon.png | Browser tab and phone home-screen icons |
| og-image.png | The image shown when the link is shared on social media or in chats |
