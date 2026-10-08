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

/* ------------------------------------------------------------------
   Gabarit des e-mails : en-tête logo, photo, filet 4 couleurs, carte, pied de page.
   Tables et styles en ligne pour Gmail, Outlook et les messageries mobiles ;
   lisible même si les images sont bloquées (textes alternatifs et fonds de couleur).
------------------------------------------------------------------ */
const FONT = "'Inter','Segoe UI',Helvetica,Arial,sans-serif";
const DISPLAY = "'Montserrat','Segoe UI',Helvetica,Arial,sans-serif";
const C = { navy: "#172033", ink: "#1f2937", muted: "#5b6475", line: "#e4e8ef", bg: "#f2f4f8", red: "#c8102e" };
const CONTACT = { email: "contact@a21businessschool.com", phone: "07 51 36 09 44", tel: "+33751360944",
  address: "7 boulevard Suchet, 75016 Paris" };

const publicBase = (base) => String(base || process.env.SITE_URL || "").replace(/\/+$/, "");

/* layout(titre, contenu, { eyebrow, preheader, hero, base, footerNote })
   hero : true pour les e-mails envoyés aux candidats (photo), false pour les notifications internes. */
function layout(title, inner, opts) {
  const o = Object.assign({ hero: true, eyebrow: "", preheader: "", footerNote: "" }, opts || {});
  const base = publicBase(o.base);
  const logo = base ? `<img src="${esc(base)}/assets/img/email/logo-21.png" width="42" height="35" alt="A21" style="display:block;border:0;height:35px;width:auto">` : "";
  const hero = o.hero && base
    ? `<tr><td style="padding:0;background:${C.navy}"><img src="${esc(base)}/assets/img/email/banner.jpg" width="600" alt="Étudiantes et étudiants d'Academy Twenty One University" style="display:block;width:100%;max-width:600px;height:auto;border:0;color:#ffffff;font:14px ${FONT}"></td></tr>`
    : "";
  const rule = `<tr><td style="padding:0;font-size:0;line-height:0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td height="4" style="background:#da0612;font-size:0;line-height:0">&nbsp;</td><td height="4" style="background:#fccd01;font-size:0;line-height:0">&nbsp;</td>
<td height="4" style="background:#a7dd63;font-size:0;line-height:0">&nbsp;</td><td height="4" style="background:#2f86ab;font-size:0;line-height:0">&nbsp;</td></tr></table></td></tr>`;
  const site = base ? `<a href="${esc(base)}" style="color:${C.muted};text-decoration:underline">${esc(base.replace(/^https?:\/\//, ""))}</a> · ` : "";
  return `<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>${esc(title)}</title></head>
<body style="margin:0;padding:0;background:${C.bg};-webkit-text-size-adjust:100%">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:${C.bg}">${esc(o.preheader || title)}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:${C.bg}"><tr><td align="center" style="padding:28px 12px">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px">
<tr><td style="padding:0 4px 18px"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
${logo ? `<td style="padding-right:12px;vertical-align:middle">${logo}</td>` : ""}
<td style="vertical-align:middle;font:800 16px/1.15 ${DISPLAY};color:${C.navy}">Academy Twenty One<br><span style="font:600 10px ${FONT};letter-spacing:3px;color:${C.muted};text-transform:uppercase">University</span></td>
</tr></table></td></tr>
<tr><td style="background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 8px 24px rgba(23,32,51,.08)">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
${hero}${rule}
<tr><td style="padding:34px 36px 8px">
${o.eyebrow ? `<p style="margin:0 0 10px;font:800 11px ${DISPLAY};letter-spacing:2px;text-transform:uppercase;color:${C.red}">${esc(o.eyebrow)}</p>` : ""}
<h1 style="margin:0 0 18px;font:800 24px/1.25 ${DISPLAY};color:${C.navy}">${esc(title)}</h1>
</td></tr>
<tr><td style="padding:0 36px 34px;font:15px/1.65 ${FONT};color:${C.ink}">${inner}</td></tr>
</table></td></tr>
<tr><td style="padding:24px 8px 8px;font:12px/1.7 ${FONT};color:${C.muted};text-align:center">
<p style="margin:0 0 6px;font:800 11px ${DISPLAY};letter-spacing:3px;text-transform:uppercase;color:${C.navy}">Learn. Lead. Transform.</p>
<p style="margin:0">Academy Twenty One University · ${CONTACT.address}</p>
<p style="margin:0">${site}<a href="mailto:${CONTACT.email}" style="color:${C.muted};text-decoration:underline">${CONTACT.email}</a> · <a href="tel:${CONTACT.tel}" style="color:${C.muted};text-decoration:none">${CONTACT.phone}</a></p>
${o.footerNote ? `<p style="margin:10px 0 0;font-size:11px;color:#8a92a3">${o.footerNote}</p>` : ""}
</td></tr>
</table></td></tr></table></body></html>`;
}

/* Bouton compatible Outlook (table + fond de couleur). */
function button(href, label) {
  return `<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:26px 0"><tr>
<td style="background:${C.red};border-radius:999px"><a href="${esc(href)}" style="display:inline-block;padding:15px 30px;font:700 15px ${DISPLAY};color:#ffffff;text-decoration:none;border-radius:999px">${esc(label)}</a></td></tr></table>`;
}

/* Tableau « libellé / valeur » aéré. */
function details(rows) {
  const r = rows.filter((x) => x[1] !== undefined && x[1] !== null && String(x[1]).trim() !== "");
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:18px 0;border:1px solid ${C.line};border-radius:12px;border-collapse:separate;overflow:hidden">
${r.map((x, i) => `<tr><td style="padding:11px 16px;${i ? `border-top:1px solid ${C.line};` : ""}background:#f7f8fb;width:38%;vertical-align:top;font:600 13px ${FONT};color:${C.muted}">${esc(x[0])}</td>
<td style="padding:11px 16px;${i ? `border-top:1px solid ${C.line};` : ""}vertical-align:top;font:14px/1.55 ${FONT};color:${C.ink};white-space:pre-wrap">${esc(x[1])}</td></tr>`).join("")}</table>`;
}

/* Encadré doux (message personnel, information importante). */
function callout(html) {
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:18px 0"><tr>
<td style="border-left:4px solid #fccd01;background:#fffbea;border-radius:8px;padding:14px 18px;font:14px/1.6 ${FONT};color:#3d3220">${html}</td></tr></table>`;
}

function signature() {
  return `<p style="margin:26px 0 0">Bien cordialement,<br><strong style="color:${C.navy}">L'équipe Academy Twenty One University</strong></p>`;
}

/* URL publique du site : SITE_URL, sinon l'hôte de la requête. */
function siteUrl(req) {
  if (process.env.SITE_URL) return process.env.SITE_URL.replace(/\/+$/, "");
  const h = (req && req.headers) || {};
  const host = String(h["x-forwarded-host"] || h.host || "localhost").split(",")[0].trim();
  const proto = String(h["x-forwarded-proto"] || (host.startsWith("localhost") ? "http" : "https")).split(",")[0].trim();
  return `${proto}://${host}`;
}

module.exports = { esc, list, smtpConfigured, mailConfigured, schoolInboxes, copyInboxes, sendMail, layout, button, details, callout, signature, siteUrl };
