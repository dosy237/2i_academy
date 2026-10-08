/*
 * Flutterwave (Orange Money, MTN MoMo) :
 *  - GET  : retour du candidat après paiement (?tx_ref=…) → page de confirmation ;
 *  - POST : webhook (Flutterwave → Paramètres → Webhooks), authentifié par l'en-tête « verif-hash » = FLW_WEBHOOK_HASH.
 *    Le statut est toujours relu chez Flutterwave avant l'envoi des e-mails.
 */
const crypto = require("crypto");
const pay = require("./_lib/pay");

const same = (a, b) => {
  const x = crypto.createHash("sha256").update(String(a || "")).digest();
  const y = crypto.createHash("sha256").update(String(b || "")).digest();
  return crypto.timingSafeEqual(x, y);
};

module.exports = async function handler(req, res) {
  const q = new URL(req.url, "http://x").searchParams;

  if (req.method !== "POST") {
    const id = String(q.get("tx_ref") || "").replace(/[^A-Za-z0-9-]/g, "").slice(0, 64);
    res.statusCode = 303;
    res.setHeader("Location", `/paiement-confirmation.html?m=mobile${id ? `&id=${encodeURIComponent(id)}` : ""}`);
    return res.end();
  }

  const secret = process.env.FLW_WEBHOOK_HASH;
  if (!secret || !pay.flutterwaveReady() || !same(req.headers["verif-hash"], secret)) {
    res.statusCode = 401;
    return res.end("unauthorized");
  }
  let evt = req.body;
  if (typeof evt === "string") { try { evt = JSON.parse(evt); } catch (e) { evt = {}; } }
  const data = (evt && evt.data) || {};
  const id = String(data.tx_ref || evt.txRef || "").replace(/[^A-Za-z0-9-]/g, "").slice(0, 64);
  if (!id) { res.statusCode = 200; return res.end("ignored"); }
  try {
    const st = await pay.flutterwaveStatus(id);
    if (st.status === "paid") await pay.notifyPaid(st);
    res.statusCode = 200;
    return res.end("ok");
  } catch (err) {
    console.error("[flutterwave]", err && err.message);
    res.statusCode = 500; // Flutterwave renouvellera l'appel
    return res.end("error");
  }
};
