/*
 * Academy 21 University — serveur Node.js (hébergement Hostinger « Node.js web app », VPS, ou tout serveur Node 20+).
 * Sert les pages du site et les fonctions de api/ (les mêmes que sur Vercel), sans dépendance supplémentaire.
 *
 *   npm install && npm start        (port : variable PORT, 3000 par défaut)
 *
 * Les variables (SMTP_USER, ADMIN_KEY, STRIPE_SECRET_KEY…) se renseignent dans le panneau de l'hébergeur ;
 * en local, un fichier .env à la racine est aussi lu (il ne doit jamais être publié).
 */
const http = require("http");
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const ROOT = __dirname;
loadDotEnv(path.join(ROOT, ".env"));

const PORT = Number(process.env.PORT || 3000);
const MAX_BODY = 6 * 1024 * 1024; // CV jusqu'à 3 Mo, encodé en base64
const API = new Set(["submit", "payment", "fapshi", "notchpay", "cinetpay", "flutterwave", "stripe-webhook"]);

const TYPES = {
  ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg", ".webp": "image/webp", ".ico": "image/x-icon", ".woff2": "font/woff2", ".pdf": "application/pdf",
  ".txt": "text/plain; charset=utf-8", ".xml": "application/xml; charset=utf-8", ".webmanifest": "application/manifest+json",
};

const SECURITY = {
  "X-Content-Type-Options": "nosniff",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "X-Frame-Options": "SAMEORIGIN",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
};

function loadDotEnv(file) {
  let txt;
  try { txt = fs.readFileSync(file, "utf8"); } catch (e) { return; }
  txt.split(/\r?\n/).forEach((line) => {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/i);
    if (!m || line.trim().startsWith("#") || process.env[m[1]] !== undefined) return;
    process.env[m[1]] = m[2].replace(/^(["'])(.*)\1$/, "$2");
  });
}

/* Seuls les fichiers publics sont servis : pages HTML à la racine et dossier assets/. */
function publicFile(urlPath) {
  let p;
  try { p = decodeURIComponent(urlPath); } catch (e) { return null; }
  if (p === "/") p = "/index.html";
  if (p.includes("\0")) return null;
  const file = path.normalize(path.join(ROOT, p));
  if (!file.startsWith(ROOT + path.sep)) return null;
  const rel = path.relative(ROOT, file).split(path.sep);
  const ok = (rel.length === 1 && /\.(html|txt|xml|ico|webmanifest)$/.test(rel[0])) || rel[0] === "assets";
  return ok ? file : null;
}

const COMPRESSIBLE = new Set([".html", ".css", ".js", ".json", ".svg", ".txt", ".xml", ".webmanifest"]);

/* Balises de vérification des moteurs de recherche, réglables sans toucher au code (variables d'environnement). */
function verificationTags() {
  const tags = [];
  const g = String(process.env.GOOGLE_SITE_VERIFICATION || "").trim().replace(/[^A-Za-z0-9_-]/g, "");
  const b = String(process.env.BING_SITE_VERIFICATION || "").trim().replace(/[^A-Za-z0-9_-]/g, "");
  if (g) tags.push(`<meta name="google-site-verification" content="${g}">`);
  if (b) tags.push(`<meta name="msvalidate.01" content="${b}">`);
  return tags.join("\n");
}

function sendFile(req, res, file, status) {
  fs.stat(file, (err, st) => {
    if (err || !st.isFile()) return notFound(req, res);
    const ext = path.extname(file).toLowerCase();
    res.statusCode = status || 200;
    res.setHeader("Content-Type", TYPES[ext] || "application/octet-stream");
    res.setHeader("Last-Modified", st.mtime.toUTCString());
    if (file.includes(`${path.sep}assets${path.sep}fonts${path.sep}`)) res.setHeader("Cache-Control", "public, max-age=31536000, immutable");
    else if (ext === ".html") res.setHeader("Cache-Control", "no-cache");
    else if (file.includes(`${path.sep}assets${path.sep}`)) res.setHeader("Cache-Control", "public, max-age=604800");
    else res.setHeader("Cache-Control", "public, max-age=86400");

    // Fichiers volumineux non textuels (images, PDF, polices) : envoi direct.
    if (!COMPRESSIBLE.has(ext)) {
      res.setHeader("Content-Length", st.size);
      if (req.method === "HEAD") return res.end();
      return fs.createReadStream(file).pipe(res);
    }
    // Textes : vérification moteurs (pages HTML) et compression gzip/brotli (pages plus rapides).
    fs.readFile(file, (e, buf) => {
      if (e) return notFound(req, res);
      let body = buf;
      if (ext === ".html") {
        const tags = verificationTags();
        if (tags) body = Buffer.from(buf.toString("utf8").replace("<head>", `<head>\n${tags}`), "utf8");
      }
      const accept = String(req.headers["accept-encoding"] || "");
      res.setHeader("Vary", "Accept-Encoding");
      let out = body;
      if (/\bbr\b/.test(accept)) { out = zlib.brotliCompressSync(body); res.setHeader("Content-Encoding", "br"); }
      else if (/\bgzip\b/.test(accept)) { out = zlib.gzipSync(body); res.setHeader("Content-Encoding", "gzip"); }
      res.setHeader("Content-Length", out.length);
      if (req.method === "HEAD") return res.end();
      res.end(out);
    });
  });
}

function notFound(req, res) {
  const page = path.join(ROOT, "404.html");
  if (fs.existsSync(page)) return sendFile(req, res, page, 404);
  res.statusCode = 404;
  res.end("Page introuvable");
}

/* Corps de requête lu comme sur Vercel : JSON ou formulaire → objet, sinon texte. */
function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    req.on("data", (c) => {
      size += c.length;
      if (size <= MAX_BODY) chunks.push(c);
    });
    req.on("end", () => {
      if (size > MAX_BODY) return reject(Object.assign(new Error("trop volumineux"), { status: 413 }));
      const raw = Buffer.concat(chunks).toString("utf8");
      req.rawBody = raw; // conservé pour vérifier la signature des webhooks
      const type = String(req.headers["content-type"] || "");
      if (!raw) return resolve(undefined);
      if (type.includes("application/json")) { try { return resolve(JSON.parse(raw)); } catch (e) { return resolve(raw); } }
      if (type.includes("application/x-www-form-urlencoded")) return resolve(Object.fromEntries(new URLSearchParams(raw)));
      resolve(raw);
    });
    req.on("error", reject);
  });
}

const server = http.createServer(async (req, res) => {
  Object.entries(SECURITY).forEach(([k, v]) => res.setHeader(k, v));
  const url = new URL(req.url, "http://localhost");

  const api = url.pathname.match(/^\/api\/([a-z-]+)\/?$/);
  if (api) {
    if (!API.has(api[1])) return notFound(req, res);
    try {
      if (req.method === "POST" || req.method === "PUT") req.body = await readBody(req);
      await require(`./api/${api[1]}.js`)(req, res);
    } catch (err) {
      console.error(`[api/${api[1]}]`, err && err.message);
      if (!res.headersSent) {
        res.statusCode = err.status || 500;
        res.setHeader("Content-Type", "application/json; charset=utf-8");
        res.end(JSON.stringify({ ok: false, error: err.status === 413 ? "too_large" : "server" }));
      }
    }
    return;
  }

  if (req.method !== "GET" && req.method !== "HEAD") {
    res.statusCode = 405;
    res.setHeader("Allow", "GET, HEAD");
    return res.end();
  }
  // Une seule adresse par page (référencement) : /index.html → /
  if (url.pathname === "/index.html") {
    res.statusCode = 301;
    res.setHeader("Location", "/" + (url.search || ""));
    return res.end();
  }
  const file = publicFile(url.pathname);
  return file ? sendFile(req, res, file) : notFound(req, res);
});

server.listen(PORT, () => console.log(`Academy 21 University — http://localhost:${PORT}`));
