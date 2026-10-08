/*
 * Notch Pay (Orange Money, MTN MoMo — Cameroun) :
 *  - GET  : retour du candidat après paiement (?reference=…) → page de confirmation ;
 *  - POST : webhook (Notch Pay → Paramètres → Webhooks), signé dans l'en-tête « x-notch-signature »
 *    (HMAC-SHA256 du corps brut avec NOTCHPAY_WEBHOOK_HASH). Le statut est toujours relu chez Notch Pay
 *    avant l'envoi des e-mails.
 */
const crypto = require("crypto");
const pay = require("./_lib/pay");

const clean = (v) => String(v || "").replace(/[^A-Za-z0-9._-]/g, "").slice(0, 80);

function signatureOk(req) {
  const secret = process.env.NOTCHPAY_WEBHOOK_HASH;
  const got = String(req.headers["x-notch-signature"] || req.headers["x-notchpay-signature"] || "");
  if (!secret || !got) return false;
  const raw = typeof req.rawBody === "string" ? req.rawBody : JSON.stringify(req.body || {});
  const expected = crypto.createHmac("sha256", secret).update(raw).digest("hex");
  const a = Buffer.from(expected), b = Buffer.from(got.toLowerCase());
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

module.exports = async function handler(req, res) {
  const q = new URL(req.url, "http://x").searchParams;

  if (req.method !== "POST") {
    // Notch Pay renvoie sa propre référence (« reference ») : c'est elle qui sert à relire le statut.
    const id = clean(q.get("reference") || q.get("notchpay_trxref") || q.get("trxref"));
    res.statusCode = 303;
    res.setHeader("Location", `/paiement-confirmation.html?m=mobile${id ? `&id=${encodeURIComponent(id)}` : ""}`);
    return res.end();
  }

  if (!pay.notchpayReady() || !signatureOk(req)) {
    res.statusCode = 401;
    return res.end("unauthorized");
  }
  let evt = req.body;
  if (typeof evt === "string") { try { evt = JSON.parse(evt); } catch (e) { evt = {}; } }
  const data = (evt && evt.data) || {};
  const id = clean(data.reference || (data.transaction && data.transaction.reference));
  if (!id || !/payment\.(complete|completed|success)/.test(String(evt.event || evt.type || "payment.complete"))) {
    res.statusCode = 200;
    return res.end("ignored");
  }
  try {
    const st = await pay.notchpayStatus(id);
    if (st.status === "paid") await pay.notifyPaid(st);
    res.statusCode = 200;
    return res.end("ok");
  } catch (err) {
    console.error("[notchpay]", err && err.message);
    res.statusCode = 500; // Notch Pay renouvellera l'appel
    return res.end("error");
  }
};
