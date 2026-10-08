/*
 * Paiement des frais d'étude de dossier : lien signé, Stripe (carte), CinetPay (Orange Money, MTN MoMo).
 * Aucune base de données : le lien envoyé au candidat contient sa référence, signée (HMAC) avec PAYMENT_SECRET.
 */
const crypto = require("crypto");
const { esc, sendMail, layout, schoolInboxes, copyInboxes, mailConfigured } = require("./mail");

const PROGRAMMES = {
  "bachelor": "Bachelor Management Stratégique & Opérationnel",
  "mastere": "Mastère Stratégie, Leadership & Transformation des Organisations",
  "executive-mba": "Executive MBA Gouvernance, Leadership & Transformation",
  "ia-marketing-reseau": "IA appliquée au Marketing de Réseau",
  "indecis": "Programme à confirmer",
};

/* Parité fixe et garantie du franc CFA (XAF et XOF) : 1 € = 655,957 FCFA. */
const EUR_TO_FCFA = 655.957;
const feeEur = () => {
  const n = Number(process.env.FEE_EUR || 50);
  return Number.isFinite(n) && n > 0 && n <= 5000 ? Math.round(n * 100) / 100 : 50;
};
/* CinetPay exige un montant multiple de 5 : arrondi au multiple de 5 supérieur. */
const toFcfa = (eur) => Math.ceil((eur * EUR_TO_FCFA) / 5) * 5;
const fmtEur = (n) => new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR" }).format(n);
const fmtFcfa = (n) => `${new Intl.NumberFormat("fr-FR").format(n)} FCFA`;

const ZONES = { XAF: "Afrique centrale (XAF)", XOF: "Afrique de l'Ouest (XOF)" };

const stripeReady = () => Boolean(process.env.STRIPE_SECRET_KEY);
const cinetpayReady = () => Boolean(process.env.CINETPAY_APIKEY && process.env.CINETPAY_SITE_ID);
const zonesAvailable = () => {
  const z = String(process.env.CINETPAY_CURRENCIES || "XAF,XOF").split(",").map((x) => x.trim().toUpperCase()).filter((x) => ZONES[x]);
  return z.length ? z : ["XAF"];
};

/* ---------------------------------------------------------------- Lien signé */
const b64u = (buf) => Buffer.from(buf).toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const unb64u = (s) => Buffer.from(String(s).replace(/-/g, "+").replace(/_/g, "/"), "base64");

function secret() {
  const s = process.env.PAYMENT_SECRET;
  if (!s || s.length < 16) throw Object.assign(new Error("PAYMENT_SECRET manquant (16 caractères minimum)"), { code: "not_configured" });
  return s;
}
const sign = (body) => b64u(crypto.createHmac("sha256", secret()).update(body).digest());

function createToken(c, days) {
  const now = Math.floor(Date.now() / 1000);
  const payload = { r: c.ref, f: c.prenom, l: c.nom, e: c.email, p: c.programme, a: c.amount || feeEur(), i: now, x: now + (days || 30) * 86400 };
  const body = b64u(JSON.stringify(payload));
  return `${body}.${sign(body)}`;
}

/* Renvoie le dossier { ref, prenom, nom, email, programme, amount, expires } ou lève une erreur codée. */
function readToken(token) {
  const [body, mac] = String(token || "").split(".");
  if (!body || !mac) throw Object.assign(new Error("lien incomplet"), { code: "invalid" });
  const expected = Buffer.from(sign(body));
  const got = Buffer.from(mac);
  if (expected.length !== got.length || !crypto.timingSafeEqual(expected, got)) throw Object.assign(new Error("signature"), { code: "invalid" });
  let p;
  try { p = JSON.parse(unb64u(body).toString("utf8")); } catch (e) { throw Object.assign(new Error("lecture"), { code: "invalid" }); }
  if (!p.x || p.x < Date.now() / 1000) throw Object.assign(new Error("expiré"), { code: "expired" });
  return { ref: p.r, prenom: p.f, nom: p.l, email: p.e, programme: p.p, amount: Number(p.a) || feeEur(), expires: p.x };
}

function summary(c) {
  return {
    ref: c.ref, prenom: c.prenom, nom: c.nom, email: c.email,
    programme: PROGRAMMES[c.programme] || c.programme || "",
    amountEur: c.amount, amountFcfa: toFcfa(c.amount),
    labelEur: fmtEur(c.amount), labelFcfa: fmtFcfa(toFcfa(c.amount)),
    rate: EUR_TO_FCFA, expires: new Date(c.expires * 1000).toISOString(),
    methods: { card: stripeReady(), mobile: cinetpayReady() }, zones: zonesAvailable().map((code) => ({ code, label: ZONES[code] })),
  };
}

/* ---------------------------------------------------------------- Stripe (REST, sans dépendance) */
function form(obj, prefix, out) {
  out = out || new URLSearchParams();
  Object.keys(obj).forEach((k) => {
    const key = prefix ? `${prefix}[${k}]` : k;
    const v = obj[k];
    if (v === undefined || v === null) return;
    if (typeof v === "object") form(v, key, out); else out.append(key, String(v));
  });
  return out;
}

async function stripe(path, params, method) {
  const r = await fetch(`https://api.stripe.com/v1/${path}`, {
    method: method || (params ? "POST" : "GET"),
    headers: { Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`, "Content-Type": "application/x-www-form-urlencoded" },
    body: params ? form(params).toString() : undefined,
  });
  const json = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(`Stripe ${r.status}: ${(json.error && json.error.message) || "erreur"}`);
  return json;
}

async function stripeCheckout(c, token, base) {
  const meta = { ref: c.ref, prenom: c.prenom, nom: c.nom, email: c.email, programme: c.programme };
  const s = await stripe("checkout/sessions", {
    mode: "payment",
    locale: "fr",
    customer_email: c.email,
    client_reference_id: c.ref,
    line_items: { 0: { quantity: 1, price_data: { currency: "eur", unit_amount: Math.round(c.amount * 100),
      product_data: { name: "Frais d'étude de dossier", description: `${PROGRAMMES[c.programme] || "Candidature"} — référence ${c.ref}` } } } },
    metadata: meta,
    payment_intent_data: { metadata: meta, description: `Frais d'étude de dossier ${c.ref}` },
    success_url: `${base}/paiement-confirmation.html?m=card&id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${base}/paiement.html?t=${encodeURIComponent(token)}&annule=1`,
  });
  return s.url;
}

/* Statut fiable : relu directement chez Stripe (jamais depuis le navigateur). */
async function stripeStatus(id) {
  if (!/^cs_[A-Za-z0-9_]+$/.test(id)) throw Object.assign(new Error("identifiant"), { code: "invalid" });
  const s = await stripe(`checkout/sessions/${id}?expand[]=payment_intent`);
  const m = s.metadata || {};
  const status = s.payment_status === "paid" ? "paid" : s.status === "expired" ? "failed" : "pending";
  return {
    status, method: "card", provider: "Stripe", ref: m.ref, prenom: m.prenom, nom: m.nom, email: m.email || s.customer_email,
    programme: m.programme, amount: fmtEur((s.amount_total || 0) / 100), transaction: (s.payment_intent && s.payment_intent.id) || s.id,
    _pi: s.payment_intent && typeof s.payment_intent === "object" ? s.payment_intent : null,
  };
}

/* Notifie une seule fois : la marque « a21_notified » est posée sur le paiement Stripe. */
async function stripeNotifyOnce(st) {
  if (st.status !== "paid" || !st._pi) return;
  if (st._pi.metadata && st._pi.metadata.a21_notified) return;
  await stripe(`payment_intents/${st._pi.id}`, { metadata: { a21_notified: new Date().toISOString() } });
  await notifyPaid(st);
}

/* ---------------------------------------------------------------- CinetPay (Mobile Money) */
const CINETPAY = "https://api-checkout.cinetpay.com/v2";

async function cinetpay(path, payload) {
  const r = await fetch(`${CINETPAY}/${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ apikey: process.env.CINETPAY_APIKEY, site_id: process.env.CINETPAY_SITE_ID, ...payload }),
  });
  return r.json().catch(() => ({}));
}

async function cinetpayCheckout(c, currency, base) {
  const zones = zonesAvailable();
  const cur = zones.includes(currency) ? currency : zones[0];
  const transaction_id = `${String(c.ref).replace(/[^A-Za-z0-9-]/g, "")}-${crypto.randomBytes(3).toString("hex").toUpperCase()}`;
  const j = await cinetpay("payment", {
    transaction_id,
    amount: toFcfa(c.amount),
    currency: cur,
    channels: "MOBILE_MONEY",
    lang: "fr",
    description: `Frais etude de dossier ${c.ref}`.replace(/[^A-Za-z0-9 -]/g, ""),
    customer_name: c.nom || "Candidat", customer_surname: c.prenom || "A21", customer_email: c.email,
    notify_url: `${base}/api/cinetpay`,
    return_url: `${base}/api/cinetpay?retour=1`,
    metadata: JSON.stringify({ ref: c.ref, prenom: c.prenom, nom: c.nom, email: c.email, programme: c.programme }),
  });
  if (String(j.code) !== "201" || !j.data || !j.data.payment_url) throw new Error(`CinetPay ${j.code}: ${j.message || j.description || "erreur"}`);
  return j.data.payment_url;
}

async function cinetpayStatus(id) {
  if (!/^[A-Za-z0-9-]{6,64}$/.test(id)) throw Object.assign(new Error("identifiant"), { code: "invalid" });
  const j = await cinetpay("payment/check", { transaction_id: id });
  const d = j.data || {};
  let m = {};
  try { m = typeof d.metadata === "string" ? JSON.parse(d.metadata) : d.metadata || {}; } catch (e) { m = {}; }
  const s = String(d.status || "").toUpperCase();
  const status = s === "ACCEPTED" ? "paid" : s === "REFUSED" || s === "CANCELED" ? "failed" : "pending";
  return {
    status, method: "mobile", provider: `CinetPay${d.payment_method ? ` · ${d.payment_method}` : ""}`,
    ref: m.ref, prenom: m.prenom, nom: m.nom, email: m.email, programme: m.programme,
    amount: d.amount ? `${new Intl.NumberFormat("fr-FR").format(Number(d.amount))} ${d.currency === "XOF" || d.currency === "XAF" ? "FCFA" : d.currency || ""}`.trim() : "",
    transaction: id,
  };
}

/* ---------------------------------------------------------------- E-mails de paiement */
function paidRows(st) {
  const rows = [["Référence du dossier", st.ref], ["Candidat·e", `${st.prenom || ""} ${st.nom || ""}`.trim() || st.email], ["E-mail", st.email],
    ["Programme", PROGRAMMES[st.programme] || st.programme], ["Montant", st.amount], ["Moyen de paiement", st.method === "card" ? "Carte bancaire (Stripe)" : `Mobile Money (${st.provider})`],
    ["N° de transaction", st.transaction], ["Date", new Date().toLocaleString("fr-FR", { timeZone: "Europe/Paris" })]];
  return `<table style="width:100%;border-collapse:collapse;margin:12px 0">${rows.filter((r) => r[1]).map((r) =>
    `<tr><th align="left" style="padding:7px 10px;background:#f5f7fa;border-bottom:1px solid #e1e5ec;font-size:14px;width:190px">${esc(r[0])}</th><td style="padding:7px 10px;border-bottom:1px solid #e1e5ec;font-size:14px">${esc(r[1])}</td></tr>`).join("")}</table>`;
}

async function notifyPaid(st) {
  if (!mailConfigured()) { console.warn("[paiement] reçu mais e-mails non configurés", st.ref, st.transaction); return; }
  const school = schoolInboxes();
  const rows = paidRows(st);
  const jobs = [sendMail({
    to: school, cc: copyInboxes(), replyTo: st.email,
    subject: `Frais d'étude réglés — ${`${st.prenom || ""} ${st.nom || ""}`.trim() || st.email} (${st.ref})`,
    html: layout("Frais d'étude de dossier réglés", `<p>Le paiement suivant vient d'être confirmé par ${esc(st.provider)}.</p>${rows}`),
    text: `Frais d'étude réglés — ${st.ref} — ${st.amount} — ${st.transaction}`,
  })];
  if (st.email) {
    jobs.push(sendMail({
      to: [st.email], replyTo: school[0],
      subject: `Academy 21 University — paiement reçu (${st.ref})`,
      html: layout("Votre paiement a bien été reçu", `<p>Bonjour${st.prenom ? " " + esc(st.prenom) : ""},</p><p>Nous confirmons la réception de vos frais d'étude de dossier. Conservez cet e-mail comme justificatif.</p>${rows}<p>Notre équipe vous recontacte pour la suite de votre admission.</p>`),
      text: `Bonjour${st.prenom ? " " + st.prenom : ""},\n\nNous confirmons la réception de vos frais d'étude de dossier (${st.amount}).\nRéférence : ${st.ref}\nTransaction : ${st.transaction}\n\nAcademy Twenty One University`,
    }).catch((e) => console.error("[paiement] reçu candidat", e && e.message)));
  }
  await Promise.all(jobs);
}

module.exports = {
  PROGRAMMES, EUR_TO_FCFA, feeEur, toFcfa, fmtEur, fmtFcfa, ZONES,
  stripeReady, cinetpayReady, createToken, readToken, summary,
  stripeCheckout, stripeStatus, stripeNotifyOnce, cinetpayCheckout, cinetpayStatus, notifyPaid,
};
