# oceanicfunnels.com

Marketing website for Oceanic Funnels OS.

| Folder | What it is |
|---|---|
| `site/` | The live website. Cloudflare Pages publishes this folder. |
| `src/` | Source: `body.src.html` (page markup + styles), `build.py` (FAQ, schema, links, SEO tags). |
| `brand/` | Logo kit: SVG and PNG logos, app icons, favicon, colours. |

## Change the site
1. Edit `src/body.src.html` or the settings at the top of `src/build.py` (plan checkout links, login URL, prices in the FAQ).
2. `cd src && python3 build.py` rewrites `site/`.
3. Commit and push. Cloudflare Pages deploys automatically in about a minute.

## Cloudflare settings
Deployed as a Cloudflare Worker with static assets (`wrangler.jsonc` points it at `site/`).
- Worker name: `oceanicfunnels` (must match `name` in wrangler.jsonc)
- Build command: *(empty)* · Deploy command: `npx wrangler deploy` · Path: `/`
