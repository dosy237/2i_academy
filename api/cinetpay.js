/*
 * CinetPay (Orange Money, MTN MoMo) :
 *  - notification serveur à serveur (notify_url) : le statut est relu chez CinetPay avant tout envoi d'e-mail ;
 *  - retour du candidat (return_url, ?retour=1) : redirection vers la page de confirmation.
 */
const pay = require("./_lib/pay");

function parseBody(req) {
  const b = req.body;
  if (!b) return {};
  if (typeof b === "string") {
    try { return JSON.parse(b); } catch (e) { return Object.fromEntries(new URLSearchParams(b)); }
  }
  return b;
}

module.exports = async function handler(req, res) {
  const q = new URL(req.url, "http://x").searchParams;
  const body = req.method === "POST" ? parseBody(req) : {};
  const id = String(body.cpm_trans_id || body.transaction_id || q.get("transaction_id") || "").replace(/[^A-Za-z0-9-]/g, "").slice(0, 64);

  if (q.get("retour")) {
    res.statusCode = 303;
    res.setHeader("Location", `/paiement-confirmation.html?m=mobile${id ? `&id=${encodeURIComponent(id)}` : ""}`);
    return res.end();
  }

  // CinetPay vérifie la disponibilité de l'URL par un GET : on répond simplement 200.
  if (req.method !== "POST" || !id || !pay.cinetpayReady()) { res.statusCode = 200; return res.end("OK"); }

  try {
    const st = await pay.cinetpayStatus(id);
    if (st.status === "paid") await pay.notifyPaid(st);
    res.statusCode = 200;
    return res.end("OK");
  } catch (err) {
    console.error("[cinetpay]", err && err.message);
    res.statusCode = 500; // CinetPay renouvellera la notification
    return res.end("ERREUR");
  }
};
