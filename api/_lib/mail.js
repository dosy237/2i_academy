/*
 * Envoi des e-mails, commun à toutes les fonctions (Gmail/SMTP ou Resend).
 * Les fichiers de api/_lib ne sont pas exposés comme routes par Vercel.
 */

const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const list = (v) => String(v || "").split(",").map((x) => x.trim()).filter(Boolean);

function smtpConfigured() {
  return Boolean(process.env.SMTP_USER && process.env.SMTP_PASS);
}

function mailConfigured() {
  return (smtpConfigured() || Boolean(process.env.RESEND_API_KEY)) && list(process.env.ADMISSIONS_EMAIL).length > 0;
}

/* Boîtes de l'école (destinataires) et copie (par défaut, l'adresse qui envoie). */
function schoolInboxes() {
  return list(process.env.ADMISSIONS_EMAIL);
}
function copyInboxes() {
  const school = schoolInboxes().map((x) => x.toLowerCase());
  return list(process.env.COPY_EMAIL || (smtpConfigured() ? process.env.SMTP_USER : ""))
    .filter((c) => !school.includes(c.toLowerCase()));
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

/* Gabarit commun : bandeau marine, titre, contenu, signature. */
function layout(title, inner) {
  return `<div style="font-family:Arial,sans-serif;max-width:620px;margin:auto;color:#2c3445">
<div style="background:#172033;color:#fff;padding:20px 24px;border-radius:12px 12px 0 0"><div style="font-size:12px;letter-spacing:2px;color:#fccd01;text-transform:uppercase">Academy 21 University</div>
<div style="font-size:20px;font-weight:bold;margin-top:6px">${esc(title)}</div></div>
<div style="border:1px solid #e1e5ec;border-top:0;border-radius:0 0 12px 12px;padding:20px 24px;font-size:15px;line-height:1.6">${inner}
<p style="color:#535c6e;margin-top:24px">Academy Twenty One University<br>Learn. Lead. Transform.</p></div></div>`;
}

function button(href, label) {
  return `<p style="margin:24px 0"><a href="${esc(href)}" style="display:inline-block;background:#c8102e;color:#fff;text-decoration:none;font-weight:bold;padding:14px 26px;border-radius:999px">${esc(label)}</a></p>`;
}

/* URL publique du site : SITE_URL, sinon l'hôte de la requête. */
function siteUrl(req) {
  if (process.env.SITE_URL) return process.env.SITE_URL.replace(/\/+$/, "");
  const h = (req && req.headers) || {};
  const host = String(h["x-forwarded-host"] || h.host || "localhost").split(",")[0].trim();
  const proto = String(h["x-forwarded-proto"] || (host.startsWith("localhost") ? "http" : "https")).split(",")[0].trim();
  return `${proto}://${host}`;
}

module.exports = { esc, list, smtpConfigured, mailConfigured, schoolInboxes, copyInboxes, sendMail, layout, button, siteUrl };
