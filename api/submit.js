/*
 * Academy 21 University — réception des candidatures et des demandes de contact.
 * Fonction serverless Vercel (Node.js).
 *
 * DEUX FAÇONS D'ENVOYER LES E-MAILS (Vercel > Settings > Environment Variables) :
 *
 * A. Depuis votre boîte Gmail (recommandé, aucun nom de domaine requis)
 *    SMTP_USER         Votre adresse Gmail, ex. prenom.nom@gmail.com : les e-mails partent de cette boîte.
 *    SMTP_PASS         Le « mot de passe d'application » Google (16 caractères), PAS votre mot de passe Gmail.
 *    MAIL_FROM_NAME    Facultatif. Nom affiché comme expéditeur. Défaut : « Academy 21 University ».
 *    ADMISSIONS_EMAIL  Adresse de l'école qui reçoit chaque candidature (plusieurs : séparées par des virgules).
 *    COPY_EMAIL        Facultatif. Qui reçoit une copie de chaque candidature. Défaut : SMTP_USER (vous).
 *    SEND_CONFIRMATION Facultatif. "0" pour NE PAS envoyer d'accusé de réception au candidat (envoyé par défaut).
 *    SMTP_HOST / SMTP_PORT / SMTP_SECURE  Facultatifs. Défaut : smtp.gmail.com / 465 / true (autre messagerie possible).
 *
 * B. Via Resend (https://resend.com), si vous disposez d'un nom de domaine vérifié
 *    RESEND_API_KEY, ADMISSIONS_EMAIL, MAIL_FROM ("Academy 21 University <admissions@votre-domaine.fr>"),
 *    SEND_CONFIRMATION="1" pour l'accusé de réception.
 *
 * WEBHOOK_URL (facultatif, avec A ou B) : reçoit chaque envoi en JSON (Google Sheets via Apps Script, Make, Zapier…).
 *
 * Si rien n'est configuré, la fonction répond 503 et le site propose au visiteur l'envoi par e-mail.
 */

const PROGRAMMES = {
  "bachelor": "Bachelor Management Stratégique & Opérationnel",
  "mastere": "Mastère Stratégie, Leadership & Transformation des Organisations",
  "executive-mba": "Executive MBA Gouvernance, Leadership & Transformation",
  "ia-marketing-reseau": "IA appliquée au Marketing de Réseau",
  "indecis": "Pas encore décidé",
};

const LABELS = {
  candidature: [
    ["programme", "Programme"], ["entree", "Année d'entrée"], ["modalite", "Modalité"], ["rythme", "Rythme"],
    ["civilite", "Civilité"], ["prenom", "Prénom"], ["nom", "Nom"], ["email", "E-mail"], ["telephone", "Téléphone"],
    ["ville", "Ville"], ["pays", "Pays"], ["diplome", "Dernier diplôme"], ["diplome_intitule", "Intitulé du diplôme"],
    ["situation", "Situation"], ["experience", "Expérience professionnelle"], ["experience_management", "Expérience managériale"],
    ["poste", "Poste"], ["entreprise", "Entreprise"], ["source", "Connaissance de l'école"], ["motivation", "Projet & motivations"],
  ],
  contact: [
    ["objet", "Objet"], ["programme", "Programme"], ["prenom", "Prénom"], ["nom", "Nom"], ["email", "E-mail"],
    ["telephone", "Téléphone"], ["organisation", "Organisation"], ["message", "Message"],
  ],
};

const VALUES = {
  entree: { m1: "Entrée en M1", m2: "Entrée directe en M2" },
  modalite: { presentiel: "Présentiel", distanciel: "Distanciel synchrone", hybride: "Hybride", indifferent: "Pas de préférence" },
  rythme: { initial: "Formation initiale", continue: "Formation continue", alternance: "Alternance", indifferent: "À définir" },
  civilite: { madame: "Madame", monsieur: "Monsieur", nr: "Non précisée" },
  diplome: { aucun: "Sans diplôme", bac: "Baccalauréat", bac2: "Bac+2", bac3: "Bac+3", bac4: "Bac+4", bac5: "Bac+5 et plus", autre: "Autre / étranger" },
  situation: { etudiant: "Étudiant·e", salarie: "Salarié·e", manager: "Manager / cadre", dirigeant: "Dirigeant·e", entrepreneur: "Entrepreneur·e / indépendant·e", recherche: "En recherche d'emploi", autre: "Autre" },
  experience: { "0-2": "Moins de 3 ans", "3-4": "3 à 4 ans", "5-6": "5 à 6 ans", "7-9": "7 à 9 ans", "10+": "10 ans et plus" },
  experience_management: { aucune: "Aucune", moins3: "Moins de 3 ans", "3plus": "3 ans et plus" },
  objet: { information: "Demande d'information", entreprise: "Entreprise / partenariat", rappel: "Être rappelé·e", handicap: "Aménagement / handicap", autre: "Autre" },
  source: { recherche: "Moteur de recherche", reseaux: "Réseaux sociaux", recommandation: "Recommandation", entreprise: "Entreprise", salon: "Salon / événement", autre: "Autre" },
  programme: PROGRAMMES,
};

const REQUIRED = {
  candidature: ["programme", "modalite", "prenom", "nom", "email", "telephone", "ville", "pays", "diplome", "situation", "experience", "experience_management", "motivation", "exactitude", "consentement"],
  contact: ["objet", "prenom", "nom", "email", "message", "consentement"],
};

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const CV_MAX = 3 * 1024 * 1024;
const CV_EXT = /\.(pdf|docx?)$/i;

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const clean = (v, max = 3000) => (typeof v === "string" ? v.trim().slice(0, max) : "");
const label = (field, value) => (VALUES[field] && VALUES[field][value]) || value;

function reference() {
  const d = new Date();
  const ymd = d.toISOString().slice(2, 10).replace(/-/g, "");
  const rnd = Math.random().toString(36).slice(2, 6).toUpperCase();
  return `A21-${ymd}-${rnd}`;
}

function parseBody(req) {
  const b = req.body;
  if (!b) return {};
  if (typeof b === "string") {
    try { return JSON.parse(b); } catch (e) { return Object.fromEntries(new URLSearchParams(b)); }
  }
  return b;
}

function isFormPost(req) {
  return String(req.headers["content-type"] || "").includes("application/x-www-form-urlencoded");
}

function reply(req, res, status, json) {
  if (isFormPost(req)) {
    // Envoi sans JavaScript : redirection vers une page lisible.
    const type = json.type || "contact";
    const target = json.ok
      ? `/merci.html?type=${encodeURIComponent(type)}&ref=${encodeURIComponent(json.ref || "")}`
      : `/${type === "candidature" ? "candidature" : "contact"}.html?erreur=${encodeURIComponent(json.error || "envoi")}`;
    res.statusCode = 303;
    res.setHeader("Location", target);
    return res.end();
  }
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  return res.end(JSON.stringify(json));
}

function buildEmail(type, data, ref) {
  const rows = LABELS[type]
    .filter(([k]) => data[k])
    .map(([k, l]) => `<tr><th align="left" style="padding:8px 12px;background:#f5f7fa;border-bottom:1px solid #e1e5ec;width:220px;font:600 14px Arial;color:#172033;vertical-align:top">${esc(l)}</th>`
      + `<td style="padding:8px 12px;border-bottom:1px solid #e1e5ec;font:14px Arial;color:#2c3445;white-space:pre-wrap">${esc(label(k, data[k]))}</td></tr>`)
    .join("");
  const title = type === "candidature"
    ? `Nouvelle candidature — ${label("programme", data.programme)}`
    : `Nouvelle demande — ${label("objet", data.objet)}`;
  const html = `<div style="font-family:Arial,sans-serif;max-width:720px;margin:auto">
<div style="background:#172033;color:#fff;padding:20px 24px;border-radius:12px 12px 0 0"><div style="font-size:12px;letter-spacing:2px;color:#fccd01;text-transform:uppercase">Academy 21 University</div>
<div style="font-size:20px;font-weight:bold;margin-top:6px">${esc(title)}</div><div style="font-size:13px;color:#c3cad6;margin-top:4px">Référence ${esc(ref)} · ${new Date().toLocaleString("fr-FR", { timeZone: "Europe/Paris" })}</div></div>
<table style="width:100%;border-collapse:collapse;border:1px solid #e1e5ec">${rows}</table>
<p style="font:13px Arial;color:#535c6e">Répondez directement à cet e-mail pour écrire à ${esc(data.prenom)} ${esc(data.nom)}.</p></div>`;
  const text = `${title}\nRéférence : ${ref}\n\n` + LABELS[type].filter(([k]) => data[k]).map(([k, l]) => `${l} : ${label(k, data[k])}`).join("\n");
  return { subject: `${title} — ${data.prenom} ${data.nom} (${ref})`, html, text };
}

const list = (v) => String(v || "").split(",").map((x) => x.trim()).filter(Boolean);

function smtpConfigured() {
  return Boolean(process.env.SMTP_USER && process.env.SMTP_PASS);
}

let transporter = null;
function smtp() {
  if (!transporter) {
    const nodemailer = require("nodemailer");
    const port = Number(process.env.SMTP_PORT || 465);
    transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST || "smtp.gmail.com",
      port,
      secure: process.env.SMTP_SECURE ? process.env.SMTP_SECURE === "true" : port === 465,
      auth: { user: process.env.SMTP_USER, pass: String(process.env.SMTP_PASS).replace(/\s+/g, "") },
    });
  }
  return transporter;
}

async function sendResend(payload) {
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!r.ok) throw new Error(`Resend ${r.status}: ${await r.text()}`);
}

/* Envoi unique, quel que soit le service : { to, cc, replyTo, subject, html, text, attachments } */
async function sendMail(m) {
  if (smtpConfigured()) {
    const name = (process.env.MAIL_FROM_NAME || "Academy 21 University").replace(/["<>]/g, "");
    await smtp().sendMail({
      from: { name, address: process.env.SMTP_USER },
      to: m.to, cc: m.cc && m.cc.length ? m.cc : undefined, replyTo: m.replyTo,
      subject: m.subject, html: m.html, text: m.text,
      attachments: (m.attachments || []).map((a) => ({ filename: a.filename, content: a.content, encoding: "base64" })),
    });
    return;
  }
  await sendResend({
    from: process.env.MAIL_FROM || "Academy 21 University <onboarding@resend.dev>",
    to: m.to, cc: m.cc && m.cc.length ? m.cc : undefined, reply_to: m.replyTo,
    subject: m.subject, html: m.html, text: m.text,
    attachments: m.attachments && m.attachments.length ? m.attachments : undefined,
  });
}

function confirmation(type, data, ref) {
  const what = type === "candidature" ? "votre candidature" : "votre message";
  const e = type === "candidature" ? "e" : "";
  const text = `Bonjour ${data.prenom},\n\nNous avons bien reçu ${what}, enregistré${e} sous la référence ${ref}.\n` +
    `Notre équipe revient vers vous dans les meilleurs délais.\n\nAcademy Twenty One University\nLearn. Lead. Transform.`;
  const html = `<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;color:#2c3445">
<div style="background:#172033;color:#fff;padding:20px 24px;border-radius:12px 12px 0 0"><div style="font-size:12px;letter-spacing:2px;color:#fccd01;text-transform:uppercase">Academy 21 University</div>
<div style="font-size:20px;font-weight:bold;margin-top:6px">Nous avons bien reçu ${what}</div></div>
<div style="border:1px solid #e1e5ec;border-top:0;border-radius:0 0 12px 12px;padding:20px 24px;font-size:15px;line-height:1.6">
<p>Bonjour ${esc(data.prenom)},</p><p>Nous avons bien reçu ${what}, enregistré${e} sous la référence <strong>${esc(ref)}</strong>.</p>
<p>Notre équipe revient vers vous dans les meilleurs délais.</p><p style="color:#535c6e">Academy Twenty One University<br>Learn. Lead. Transform.</p></div></div>`;
  return { subject: `Academy 21 University — nous avons bien reçu ${what} (${ref})`, text, html };
}

module.exports = async function handler(req, res) {
  if (req.method === "OPTIONS") { res.statusCode = 204; return res.end(); }
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return reply(req, res, 405, { ok: false, error: "method" });
  }

  const body = parseBody(req);
  const type = body.type === "candidature" ? "candidature" : "contact";

  // Anti-spam : champ piège rempli ou envoi trop rapide → on simule un succès sans rien transmettre.
  const elapsed = Number(body.elapsed || 0);
  if (clean(body.website) || (body.elapsed !== undefined && elapsed > 0 && elapsed < 1200)) {
    return reply(req, res, 200, { ok: true, ref: reference(), type });
  }

  const data = {};
  LABELS[type].forEach(([k]) => { data[k] = clean(body[k], k === "motivation" || k === "message" ? 3000 : 200); });
  data.exactitude = clean(body.exactitude);
  data.consentement = clean(body.consentement);

  const missing = REQUIRED[type].filter((k) => !data[k]);
  if (data.email && !EMAIL_RE.test(data.email)) missing.push("email");
  if (type === "candidature" && data.programme && !PROGRAMMES[data.programme]) missing.push("programme");
  if (type === "candidature" && data.motivation && data.motivation.length < 80) missing.push("motivation");
  if (missing.length) {
    const extra = { consentement: "Consentement", exactitude: "Attestation d'exactitude" };
    const names = [...new Set(missing)].map((k) => extra[k] || (LABELS[type].find(([f]) => f === k) || [k, k])[1]);
    return reply(req, res, 400, { ok: false, error: "validation", fields: names, type });
  }

  let attachment = null;
  if (type === "candidature" && body.cv && typeof body.cv === "object" && body.cv.data) {
    const name = clean(body.cv.name, 120).replace(/[^\w.\- ]+/g, "_");
    const size = Math.floor((String(body.cv.data).length * 3) / 4);
    if (!CV_EXT.test(name)) return reply(req, res, 400, { ok: false, error: "validation", fields: ["CV (format)"], type });
    if (size > CV_MAX) return reply(req, res, 413, { ok: false, error: "too_large", type });
    attachment = { filename: name, content: String(body.cv.data) };
  }

  const school = list(process.env.ADMISSIONS_EMAIL);
  const viaSmtp = smtpConfigured();
  const hasMail = (viaSmtp || process.env.RESEND_API_KEY) && school.length > 0;
  const hasHook = process.env.WEBHOOK_URL;
  if (!hasMail && !hasHook) {
    return reply(req, res, 503, { ok: false, error: "not_configured", type });
  }

  const ref = reference();
  const mail = buildEmail(type, data, ref);

  try {
    const jobs = [];
    if (hasMail) {
      // Copie : par défaut, l'adresse Gmail qui envoie (vous), sauf si elle est déjà destinataire.
      const copy = list(process.env.COPY_EMAIL || (viaSmtp ? process.env.SMTP_USER : ""))
        .filter((c) => !school.map((x) => x.toLowerCase()).includes(c.toLowerCase()));
      jobs.push(sendMail({
        to: school, cc: copy, replyTo: data.email,
        subject: mail.subject, html: mail.html, text: mail.text,
        attachments: attachment ? [attachment] : [],
      }));
      const wantsConfirmation = viaSmtp ? process.env.SEND_CONFIRMATION !== "0"
        : process.env.SEND_CONFIRMATION === "1" && Boolean(process.env.MAIL_FROM);
      if (wantsConfirmation) {
        const c = confirmation(type, data, ref);
        jobs.push(sendMail({ to: [data.email], replyTo: school[0], subject: c.subject, html: c.html, text: c.text })
          .catch((e) => console.error("[submit] accusé de réception", e && e.message)));
      }
    }
    if (hasHook) {
      const record = { ref, type, receivedAt: new Date().toISOString(), ...data, cv: attachment ? attachment.filename : "" };
      jobs.push(fetch(process.env.WEBHOOK_URL, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(record) })
        .then((r) => { if (!r.ok) throw new Error(`Webhook ${r.status}`); }));
    }
    await Promise.all(jobs);
    return reply(req, res, 200, { ok: true, ref, type });
  } catch (err) {
    console.error("[submit]", err && err.message);
    return reply(req, res, 502, { ok: false, error: "delivery", type });
  }
};
