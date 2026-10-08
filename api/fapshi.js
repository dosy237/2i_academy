/*
 * Fapshi (MTN MoMo, Orange Money — Cameroun) :
 *  - GET  : retour du candidat après paiement (?ext=… ajouté par le site, ?transId=… s'il est fourni) → confirmation ;
 *  - POST : webhook facultatif (Fapshi → Paramètres → Webhook). Le statut est toujours relu chez Fapshi
 *    avant l'envoi des e-mails ; activer FAPSHI_WEBHOOK=1 une fois le webhook configuré.
 */
const pay = require("./_lib/pay");

const clean = (v) => String(v || "").replace(/[^A-Za-z0-9_-]/g, "").slice(0, 80);

module.exports = async function handler(req, res) {
  const q = new URL(req.url, "http://x").searchParams;

  if (req.method !== "POST") {
    let id = clean(q.get("transId") || q.get("transid"));
    if (!id && pay.fapshiReady()) {
      try { id = clean(await pay.fapshiFindTransId(clean(q.get("ext")))); } catch (e) { console.error("[fapshi] retour", e && e.message); }
    }
    res.statusCode = 303;
    res.setHeader("Location", `/paiement-confirmation.html?m=mobile${id ? `&id=${encodeURIComponent(id)}` : ""}`);
    return res.end();
  }

  let evt = req.body;
  if (typeof evt === "string") { try { evt = JSON.parse(evt); } catch (e) { evt = {}; } }
  const id = clean(evt && (evt.transId || (evt.data && evt.data.transId)));
  if (!pay.fapshiReady() || process.env.FAPSHI_WEBHOOK !== "1" || !id) { res.statusCode = 200; return res.end("ignored"); }
  try {
    const st = await pay.fapshiStatus(id); // statut relu chez Fapshi : un faux appel ne peut rien valider
    if (st.status === "paid") await pay.notifyPaid(st);
    res.statusCode = 200;
    return res.end("ok");
  } catch (err) {
    console.error("[fapshi]", err && err.message);
    res.statusCode = 500;
    return res.end("error");
  }
};
