/*
 * Webhook Stripe (facultatif mais recommandé) : garantit l'e-mail de confirmation même si le candidat
 * ferme la page avant son retour sur le site. Seul l'identifiant de session est lu dans l'événement :
 * le statut est ensuite relu directement chez Stripe avec la clé secrète, ce qui écarte tout faux appel.
 * Événements à cocher : checkout.session.completed, checkout.session.async_payment_succeeded.
 */
const pay = require("./_lib/pay");

module.exports = async function handler(req, res) {
  if (req.method !== "POST") { res.statusCode = 405; res.setHeader("Allow", "POST"); return res.end(); }
  let evt = req.body;
  if (typeof evt === "string") { try { evt = JSON.parse(evt); } catch (e) { evt = {}; } }
  const obj = evt && evt.data && evt.data.object;
  const wanted = ["checkout.session.completed", "checkout.session.async_payment_succeeded"];
  if (!pay.stripeReady() || !obj || !wanted.includes(evt.type) || !/^cs_/.test(obj.id || "")) {
    res.statusCode = 200;
    return res.end("ignored");
  }
  try {
    await pay.stripeNotifyOnce(await pay.stripeStatus(obj.id));
    res.statusCode = 200;
    return res.end("ok");
  } catch (err) {
    console.error("[stripe-webhook]", err && err.message);
    res.statusCode = 500; // Stripe réessaiera
    return res.end("error");
  }
};
