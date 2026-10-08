/*
 * Academy 21 University — paiement des frais d'étude de dossier.
 *
 *  POST action=link    (espace école, protégé par ADMIN_KEY) : crée le lien signé et l'envoie au candidat.
 *  GET  action=session&t=…   : récapitulatif du dossier à régler (page paiement.html).
 *  POST action=card|mobile   : ouvre le paiement Stripe (carte) ou CinetPay (Orange Money, MTN MoMo).
 *  GET  action=status&m=card|mobile&id=…   : statut relu chez le prestataire (page de confirmation).
 *
 * Variables (Vercel > Settings > Environment Variables) — voir README :
 *  PAYMENT_SECRET, ADMIN_KEY, FEE_EUR (défaut 50), STRIPE_SECRET_KEY, CINETPAY_APIKEY, CINETPAY_SITE_ID,
 *  CINETPAY_CURRENCIES (défaut "XAF,XOF"), SITE_URL (facultatif), + variables d'e-mail de api/submit.js.
 */
const crypto = require("crypto");
const { esc, sendMail, layout, button, siteUrl, schoolInboxes, copyInboxes, mailConfigured } = require("./_lib/mail");
const pay = require("./_lib/pay");

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const clean = (v, max = 200) => (typeof v === "string" ? v.trim().slice(0, max) : typeof v === "number" ? String(v) : "");

function parseBody(req) {
  const b = req.body;
  if (!b) return {};
  if (typeof b === "string") {
    try { return JSON.parse(b); } catch (e) { return Object.fromEntries(new URLSearchParams(b)); }
  }
  return b;
}
const isFormPost = (req) => String(req.headers["content-type"] || "").includes("application/x-www-form-urlencoded");

function json(res, status, body) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.end(JSON.stringify(body));
}
function redirect(res, url) {
  res.statusCode = 303;
  res.setHeader("Location", url);
  res.end();
}

function adminOk(key) {
  const expected = process.env.ADMIN_KEY || "";
  if (expected.length < 12) return null; // non configuré
  const a = crypto.createHash("sha256").update(String(key || "")).digest();
  const b = crypto.createHash("sha256").update(expected).digest();
  return crypto.timingSafeEqual(a, b);
}

async function createLink(req, res, body) {
  const ok = adminOk(body.key);
  if (ok === null || !process.env.PAYMENT_SECRET) return json(res, 503, { ok: false, error: "not_configured" });
  if (!ok) { await new Promise((r) => setTimeout(r, 600)); return json(res, 401, { ok: false, error: "key" }); }

  const c = {
    ref: clean(body.ref, 40).toUpperCase().replace(/[^A-Z0-9-]/g, ""),
    prenom: clean(body.prenom, 80), nom: clean(body.nom, 80), email: clean(body.email, 160),
    programme: clean(body.programme, 40), amount: Number(String(body.amount || pay.feeEur()).replace(",", ".")),
  };
  const days = Math.min(90, Math.max(1, parseInt(body.days, 10) || 30));
  const fields = [];
  if (!c.ref) fields.push("Référence");
  if (!c.prenom) fields.push("Prénom");
  if (!c.nom) fields.push("Nom");
  if (!EMAIL_RE.test(c.email)) fields.push("E-mail");
  if (!pay.PROGRAMMES[c.programme]) fields.push("Programme");
  if (!(c.amount >= 1 && c.amount <= 5000)) fields.push("Montant");
  if (fields.length) return json(res, 400, { ok: false, error: "validation", fields });
  c.amount = Math.round(c.amount * 100) / 100;

  const token = pay.createToken(c, days);
  const link = `${siteUrl(req)}/paiement.html?t=${encodeURIComponent(token)}`;
  const s = pay.summary(pay.readToken(token));
  const until = new Date(s.expires).toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Paris" });

  let sent = false;
  if ((body.send === "1" || body.send === true) && mailConfigured()) {
    const note = clean(body.message, 1200);
    const html = layout("Votre dossier a été étudié", `<p>Bonjour ${esc(c.prenom)},</p>
<p>Votre dossier de candidature <strong>${esc(c.ref)}</strong> (${esc(s.programme)}) a été étudié par notre équipe.
Pour poursuivre votre admission, nous vous invitons à régler les frais d'étude de dossier.</p>
${note ? `<p style="padding:12px 16px;background:#f5f7fa;border-radius:8px;white-space:pre-wrap">${esc(note)}</p>` : ""}
<p style="font-size:17px"><strong>${esc(s.labelEur)}</strong> <span style="color:#535c6e">· soit ${esc(s.labelFcfa)} en Mobile Money</span></p>
${button(link, "Accéder à mon espace de paiement")}
<p style="font-size:13px;color:#535c6e">Carte bancaire, Orange Money ou MTN Mobile Money. Paiement sécurisé par nos prestataires : l'école n'a jamais accès à vos données bancaires.
Lien personnel, valable jusqu'au ${esc(until)}. Si le bouton ne fonctionne pas, copiez cette adresse : ${esc(link)}</p>`);
    const text = `Bonjour ${c.prenom},\n\nVotre dossier ${c.ref} (${s.programme}) a été étudié. Pour poursuivre votre admission, merci de régler les frais d'étude de dossier : ${s.labelEur} (soit ${s.labelFcfa} en Mobile Money).\n\n${note ? note + "\n\n" : ""}Votre espace de paiement : ${link}\nLien valable jusqu'au ${until}.\n\nAcademy Twenty One University`;
    try {
      await sendMail({ to: [c.email], cc: [...schoolInboxes(), ...copyInboxes()], replyTo: schoolInboxes()[0],
        subject: `Academy 21 University — frais d'étude de dossier (${c.ref})`, html, text });
      sent = true;
    } catch (e) {
      console.error("[paiement] envoi du lien", e && e.message);
      return json(res, 502, { ok: false, error: "delivery", link });
    }
  }
  return json(res, 200, { ok: true, sent, link, expires: s.expires, labelEur: s.labelEur, labelFcfa: s.labelFcfa });
}

module.exports = async function handler(req, res) {
  const q = new URL(req.url, "http://x").searchParams;
  const body = req.method === "POST" ? parseBody(req) : {};
  const action = clean(body.action || q.get("action"), 20);

  try {
    if (req.method === "GET" && action === "session") {
      if (!process.env.PAYMENT_SECRET) return json(res, 503, { ok: false, error: "not_configured" });
      return json(res, 200, { ok: true, ...pay.summary(pay.readToken(q.get("t"))) });
    }

    if (req.method === "GET" && action === "status") {
      const m = q.get("m") === "mobile" ? "mobile" : "card";
      const id = clean(q.get("id"), 120);
      if (m === "card") {
        if (!pay.stripeReady()) return json(res, 503, { ok: false, error: "not_configured" });
        const st = await pay.stripeStatus(id);
        await pay.stripeNotifyOnce(st).catch((e) => console.error("[paiement] notification", e && e.message));
        delete st._pi;
        return json(res, 200, { ok: true, ...st });
      }
      if (!pay.cinetpayReady()) return json(res, 503, { ok: false, error: "not_configured" });
      return json(res, 200, { ok: true, ...(await pay.cinetpayStatus(id)) });
    }

    if (req.method === "POST" && action === "link") return await createLink(req, res, body);

    if (req.method === "POST" && (action === "card" || action === "mobile")) {
      const c = pay.readToken(body.t);
      const base = siteUrl(req);
      let url;
      if (action === "card") {
        if (!pay.stripeReady()) return json(res, 503, { ok: false, error: "not_configured" });
        url = await pay.stripeCheckout(c, body.t, base);
      } else {
        if (!pay.cinetpayReady()) return json(res, 503, { ok: false, error: "not_configured" });
        url = await pay.cinetpayCheckout(c, clean(body.currency, 3).toUpperCase(), base);
      }
      return isFormPost(req) ? redirect(res, url) : json(res, 200, { ok: true, url });
    }

    res.setHeader("Allow", "GET, POST");
    return json(res, 405, { ok: false, error: "method" });
  } catch (err) {
    if (err && (err.code === "invalid" || err.code === "expired")) return json(res, 400, { ok: false, error: err.code });
    if (err && err.code === "not_configured") return json(res, 503, { ok: false, error: "not_configured" });
    console.error("[paiement]", err && err.message);
    return json(res, 502, { ok: false, error: "provider" });
  }
};
