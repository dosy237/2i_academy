/*
 * Academy 21 University — paiement des frais d'étude de dossier.
 *
 *  POST action=link    (espace école, protégé par ADMIN_KEY) : crée le lien signé et l'envoie au candidat.
 *  GET  action=session&t=…   : récapitulatif du dossier à régler (page paiement.html).
 *  POST action=card|mobile   : ouvre le paiement Stripe (carte) ou CinetPay (Orange Money, MTN MoMo).
 *  GET  action=status&m=card|mobile&id=…   : statut relu chez le prestataire (page de confirmation).
 *
 * Variables (Vercel > Settings > Environment Variables) — voir README :
 *  PAYMENT_SECRET, ADMIN_KEY, FEE_EUR (défaut 50), STRIPE_SECRET_KEY,
 *  Mobile Money : NOTCHPAY_PUBLIC_KEY + NOTCHPAY_WEBHOOK_HASH (Notch Pay), ou Flutterwave / CinetPay,
 *  MOBILE_PROVIDER (facultatif), MOBILE_CURRENCIES (défaut "XAF,XOF"), SITE_URL (facultatif), + variables d'e-mail.
 */
const crypto = require("crypto");
const { esc, sendMail, layout, button, details, callout, signature, siteUrl, schoolInboxes, copyInboxes, mailConfigured } = require("./_lib/mail");
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

const refGen = () => {
  const ymd = new Date().toISOString().slice(2, 10).replace(/-/g, "");
  return `A21-${ymd}-${crypto.randomBytes(3).toString("hex").toUpperCase().slice(0, 4)}`;
};
/* Plusieurs adresses possibles : séparées par des virgules, points-virgules ou retours à la ligne. */
const splitEmails = (v) => [...new Set(String(v || "").split(/[\s,;]+/).map((x) => x.trim().toLowerCase()).filter(Boolean))];
const MAX_BATCH = 50;

function linkEmail(c, s, link, until, note, base) {
  const hello = c.prenom ? `Bonjour ${esc(c.prenom)},` : "Bonjour,";
  const inner = `<p style="margin:0 0 14px">${hello}</p>
<p style="margin:0 0 14px">Votre dossier de candidature <strong>${esc(c.ref)}</strong> a été étudié par notre équipe. Pour poursuivre votre admission, nous vous invitons à régler les frais d'étude de dossier.</p>
${note ? callout(esc(note).replace(/\n/g, "<br>")) : ""}
${details([["Programme", s.programme], ["Frais d'étude de dossier", s.labelEur], ["En Mobile Money", `${s.labelFcfa} (taux fixe 1 € = 655,957 FCFA)`], ["Lien valable jusqu'au", until]])}
${button(link, "Accéder à mon espace de paiement")}
<p style="margin:0;font-size:13px;color:#5b6475">Carte bancaire, Orange Money ou MTN Mobile Money. Le paiement est sécurisé par nos prestataires : l'école n'a jamais accès à vos coordonnées bancaires.</p>
<p style="margin:10px 0 0;font-size:12px;color:#8a92a3;word-break:break-all">Si le bouton ne fonctionne pas, copiez cette adresse dans votre navigateur : ${esc(link)}</p>
${signature()}`;
  const html = layout("Votre dossier a été étudié", inner, { hero: true, eyebrow: "Admissions", base, preheader: `Frais d'étude de dossier : ${s.labelEur} — lien personnel` });
  const text = `${c.prenom ? `Bonjour ${c.prenom},` : "Bonjour,"}\n\nVotre dossier ${c.ref} (${s.programme}) a été étudié. Pour poursuivre votre admission, merci de régler les frais d'étude de dossier : ${s.labelEur} (soit ${s.labelFcfa} en Mobile Money).\n\n${note ? note + "\n\n" : ""}Votre espace de paiement : ${link}\nLien valable jusqu'au ${until}.\n\nL'équipe Academy Twenty One University`;
  return { subject: `Academy 21 University — frais d'étude de dossier (${c.ref})`, html, text };
}

async function createLink(req, res, body) {
  const ok = adminOk(body.key);
  if (ok === null || !process.env.PAYMENT_SECRET) return json(res, 503, { ok: false, error: "not_configured" });
  if (!ok) { await new Promise((r) => setTimeout(r, 600)); return json(res, 401, { ok: false, error: "key" }); }

  const emails = splitEmails(body.email);
  const batch = emails.length > 1;
  const base = {
    ref: clean(body.ref, 40).toUpperCase().replace(/[^A-Z0-9-]/g, ""),
    prenom: batch ? "" : clean(body.prenom, 80), nom: batch ? "" : clean(body.nom, 80),
    programme: clean(body.programme, 40), amount: Number(String(body.amount || pay.feeEur()).replace(",", ".")),
  };
  const days = Math.min(90, Math.max(1, parseInt(body.days, 10) || 30));
  const fields = [];
  if (!batch && !base.ref) fields.push("Référence");
  if (!batch && !base.prenom) fields.push("Prénom");
  if (!batch && !base.nom) fields.push("Nom");
  const bad = emails.filter((e) => !EMAIL_RE.test(e));
  if (!emails.length || bad.length) fields.push(bad.length ? `E-mail (${bad.slice(0, 3).join(", ")})` : "E-mail");
  if (emails.length > MAX_BATCH) fields.push(`E-mail (${MAX_BATCH} adresses maximum par envoi)`);
  if (!pay.PROGRAMMES[base.programme]) fields.push("Programme");
  if (!(base.amount >= 1 && base.amount <= 5000)) fields.push("Montant");
  if (fields.length) return json(res, 400, { ok: false, error: "validation", fields });
  base.amount = Math.round(base.amount * 100) / 100;

  const wantSend = (body.send === "1" || body.send === true) && mailConfigured();
  const note = clean(body.message, 1200);
  const school = schoolInboxes();
  const results = [];
  let s0 = null;
  // Envois un par un : chaque candidat reçoit son propre e-mail et son propre lien (jamais les adresses des autres).
  for (const email of emails) {
    const c = { ...base, email, ref: batch ? refGen() : base.ref };
    const token = pay.createToken(c, days);
    const link = `${siteUrl(req)}/paiement.html?t=${encodeURIComponent(token)}`;
    const s = pay.summary(pay.readToken(token));
    s0 = s0 || s;
    const until = new Date(s.expires).toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Paris" });
    const r = { email, ref: c.ref, link, sent: false };
    if (wantSend) {
      const m = linkEmail(c, s, link, until, note, siteUrl(req));
      try {
        await sendMail({ to: [email], cc: batch ? [] : [...school, ...copyInboxes()], replyTo: school[0], subject: m.subject, html: m.html, text: m.text });
        r.sent = true;
      } catch (e) {
        console.error("[paiement] envoi du lien", email, e && e.message);
        r.error = "delivery";
      }
    }
    results.push(r);
  }

  // Envoi groupé : un seul récapitulatif à l'école plutôt qu'une copie par candidat.
  if (batch && wantSend && results.some((r) => r.sent)) {
    await sendMail({
      to: school, cc: copyInboxes(), subject: `Frais d'étude — ${results.filter((r) => r.sent).length} lien(s) de paiement envoyé(s)`,
      html: layout("Liens de paiement envoyés", `<p style="margin:0">${esc(s0.programme)} · ${esc(s0.labelEur)} (${esc(s0.labelFcfa)})</p>`
        + details(results.map((r) => [r.email, `${r.ref} — ${r.sent ? "envoyé" : "échec de l'envoi"}`])),
        { hero: false, eyebrow: "Espace école", base: siteUrl(req) }),
      text: results.map((r) => `${r.email} — ${r.ref} — ${r.sent ? "envoyé" : "échec"}`).join("\n"),
    }).catch((e) => console.error("[paiement] récapitulatif école", e && e.message));
  }

  const failed = results.filter((r) => r.error).length;
  const out = { ok: failed === 0, sent: results.filter((r) => r.sent).length, results, link: results[0].link,
    expires: s0.expires, labelEur: s0.labelEur, labelFcfa: s0.labelFcfa };
  if (failed) { out.error = "delivery"; out.failed = failed; }
  return json(res, failed === results.length && wantSend ? 502 : 200, out);
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
      if (!pay.mobileReady()) return json(res, 503, { ok: false, error: "not_configured" });
      const st = await pay.mobileStatus(id);
      // Flutterwave sans webhook configuré : la confirmation part depuis la page de retour.
      const prov = pay.mobileProvider();
      const noHook = (prov === "flutterwave" && !process.env.FLW_WEBHOOK_HASH) || (prov === "notchpay" && !process.env.NOTCHPAY_WEBHOOK_HASH);
      if (st.status === "paid" && noHook) {
        await pay.notifyPaid(st).catch((e) => console.error("[paiement] notification", e && e.message));
      }
      return json(res, 200, { ok: true, ...st });
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
        if (!pay.mobileReady()) return json(res, 503, { ok: false, error: "not_configured" });
        url = await pay.mobileCheckout(c, clean(body.currency, 3).toUpperCase(), base);
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
