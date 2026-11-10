// Oceanic Funnels site worker: serves the static site and forwards website pixel events
// to the Meta Conversions API (server side) at POST /api/e.
// Secret required (set in Cloudflare, never in code): META_CAPI_TOKEN
// Optional variable for testing in Events Manager: META_TEST_CODE
const PIXEL_ID = "2113854352568666";
const ALLOWED = new Set(["PageView", "ViewContent", "InitiateCheckout", "Lead", "Contact"]);
const GRAPH = "https://graph.facebook.com/v21.0/";

function cookie(h, name) {
  const m = (h || "").match(new RegExp("(?:^|;\\s*)" + name + "=([^;]+)"));
  return m ? decodeURIComponent(m[1]) : undefined;
}

async function handle(req, env, ctx) {
  const origin = req.headers.get("Origin") || "";
  if (origin && !/^https:\/\/(www\.)?oceanicfunnels\.com$/.test(origin)) return new Response(null, { status: 403 });
  let b;
  try { b = JSON.parse(await req.text()); } catch { return new Response(null, { status: 400 }); }
  if (!b || b.p !== PIXEL_ID || !ALLOWED.has(b.e) || typeof b.id !== "string" || b.id.length > 64) return new Response(null, { status: 204 });
  if (!env.META_CAPI_TOKEN) return new Response(null, { status: 204 });

  const ck = req.headers.get("Cookie");
  let url = typeof b.u === "string" ? b.u.slice(0, 1000) : "https://oceanicfunnels.com/";
  let fbc = cookie(ck, "_fbc");
  if (!fbc) { try { const id = new URL(url).searchParams.get("fbclid"); if (id) fbc = "fb.1." + Date.now() + "." + id; } catch {} }
  const user_data = {
    client_ip_address: req.headers.get("CF-Connecting-IP") || undefined,
    client_user_agent: req.headers.get("User-Agent") || undefined,
    fbp: cookie(ck, "_fbp"),
    fbc,
  };
  const custom_data = {};
  if (b.d && typeof b.d === "object") for (const k of ["content_name", "value", "currency"]) if (b.d[k] !== undefined) custom_data[k] = String(b.d[k]).slice(0, 200);
  const payload = {
    data: [{ event_name: b.e, event_time: Math.floor(Date.now() / 1000), event_id: b.id, event_source_url: url,
             action_source: "website", user_data, custom_data }],
  };
  if (env.META_TEST_CODE) payload.test_event_code = env.META_TEST_CODE;
  ctx.waitUntil(fetch(GRAPH + PIXEL_ID + "/events?access_token=" + encodeURIComponent(env.META_CAPI_TOKEN), {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload),
  }).catch(() => {}));
  return new Response(null, { status: 204 });
}

export default {
  async fetch(req, env, ctx) {
    const u = new URL(req.url);
    if (u.pathname === "/api/e") {
      if (req.method === "POST") return handle(req, env, ctx);
      return new Response(null, { status: 405 });
    }
    return env.ASSETS.fetch(req);
  },
};
