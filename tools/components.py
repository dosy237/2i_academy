# Composants partagés du site Academy 21 University (en-tête, pied, icônes, blocs).
import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# --- Coordonnées : à modifier ici, elles sont reprises sur tout le site ---
CONTACT_EMAIL = "admissions@academy21france.fr"
SCHOOL = "Academy Twenty One University"

BROCHURES = {
    "bachelor": ("assets/docs/brochure-bachelor-management-a21.pdf", "Bachelor Management Stratégique & Opérationnel"),
    "mastere": ("assets/docs/brochure-mastere-strategie-leadership-a21.pdf", "Mastère Stratégie, Leadership & Transformation des Organisations"),
    "executive-mba": ("assets/docs/brochure-executive-mba-a21.pdf", "Executive MBA Gouvernance, Leadership & Transformation"),
    "ia-marketing-reseau": ("assets/docs/fiche-ia-marketing-reseau-a21.pdf", "IA appliquée au Marketing de Réseau"),
    "institution": ("assets/docs/presentation-institutionnelle-a21-university.pdf", "Présentation institutionnelle — Institutional Profile"),
    "international": ("assets/docs/ouverture-internationale-a21-university.pdf", "Ouverture internationale — Global Engagement"),
}

def pdf_size(key):
    path = os.path.join(ROOT, BROCHURES[key][0])
    kb = os.path.getsize(path) / 1024
    return f"PDF, {round(kb)} Ko"

def ic(path, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{path}</svg>')

I = {
 "arrow": ic('<path d="M5 12h14M13 6l6 6-6 6"/>', "i-arrow"),
 "arrow-up": ic('<path d="M12 19V5M6 11l6-6 6 6"/>'),
 "arrow-left": ic('<path d="M19 12H5M11 6l-6 6 6 6"/>'),
 "chev": ic('<path d="M6 9l6 6 6-6"/>', "chev"),
 "download": ic('<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>'),
 "compass": ic('<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>'),
 "scale": ic('<path d="M12 4v16M7 20h10M5 8h14M5 8l-2.5 6a3 3 0 0 0 5 0zM19 8l-2.5 6a3 3 0 0 0 5 0z"/>'),
 "users": ic('<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.6"/><path d="M16 14.2c2.8.2 5 2.6 5 5.8"/>'),
 "refresh": ic('<path d="M20 11a8 8 0 0 0-14.5-4.5L4 8M4 4v4h4M4 13a8 8 0 0 0 14.5 4.5L20 16M20 20v-4h-4"/>'),
 "globe": ic('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>'),
 "shield": ic('<path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/>'),
 "chart": ic('<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'),
 "leader": ic('<circle cx="12" cy="7" r="3.5"/><path d="M5 21v-1a7 7 0 0 1 14 0v1"/><path d="M12 14l1.4 2.6L12 21l-1.4-4.4z"/>'),
 "cpu": ic('<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9.5 9.5h5v5h-5zM9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>'),
 "building": ic('<path d="M4 21V5l8-3 8 3v16M2 21h20M9 21v-5h6v5M8 8h.01M12 8h.01M16 8h.01M8 12h.01M12 12h.01M16 12h.01"/>'),
 "monitor": ic('<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>'),
 "layers": ic('<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>'),
 "clock": ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "award": ic('<circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/>'),
 "info": ic('<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5h.01"/>'),
 "mail": ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'),
 "target": ic('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>'),
 "bulb": ic('<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>'),
 "mic": ic('<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>'),
 "briefcase": ic('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>'),
 "calendar": ic('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'),
 "spark": ic('<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>'),
 "file": ic('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>'),
 "check": ic('<path d="M5 12.5l4.5 4.5L19 7.5"/>'),
 "send": ic('<path d="M21 3L10 14M21 3l-7 18-4-7-7-4z"/>'),
 "save": ic('<path d="M5 3h11l3 3v13a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2z"/><path d="M8 3v5h7M8 21v-7h8v7"/>'),
 "handshake": ic('<path d="M3 12l4-4 5 2 5-2 4 4-7 7a2 2 0 0 1-2.8 0z"/><path d="M8.5 13.5l2 2M11 11l3 3"/>'),
 "rocket": ic('<path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2M9 15l-3-3c1-4 4-8 9-9 1 5-1 8-5 12l-1 0z"/><circle cx="15" cy="9" r="1.5"/>'),
 "graduation": ic('<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5M22 9v6"/>'),
 "presentation": ic('<path d="M3 4h18M5 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4M12 15v4M8 21l4-2 4 2"/><path d="M9 11l2-2 2 2 3-3"/>'),
 "message": ic('<path d="M4 5h16v11H8l-4 4z"/><path d="M8 9h8M8 12h5"/>'),
 "card": ic('<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6.5 15h4"/>'),
 "phone": ic('<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.5h3"/>'),
 "key": ic('<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16.5 6.5l2.5 2.5M14 9l2 2"/>'),
 "copy": ic('<rect x="8.5" y="8.5" width="12" height="12" rx="2"/><path d="M15.5 8.5V5.5a2 2 0 0 0-2-2h-8a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h3"/>'),
 "lock": ic('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'),
 "eye": ic('<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>'),
 "map": ic('<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>'),
}

def ring(cls="deco", a="#da0612", b="#fccd01", uid="r"):
    """Arcs décoratifs reprenant l'anneau du logo."""
    return f'''<svg class="{cls}" viewBox="0 0 200 200" aria-hidden="true" focusable="false"><defs>
<linearGradient id="{uid}a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{a}" stop-opacity=".2"/></linearGradient>
<linearGradient id="{uid}b" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{b}"/><stop offset="1" stop-color="{b}" stop-opacity=".15"/></linearGradient></defs>
<path d="M150 30 A86 86 0 1 0 170 150" fill="none" stroke="url(#{uid}a)" stroke-width="14" stroke-linecap="round"/>
<path d="M60 45 A64 64 0 0 1 160 120" fill="none" stroke="url(#{uid}b)" stroke-width="10" stroke-linecap="round"/></svg>'''

# --- Programmes : données communes (menu, cartes, liens) ---
PROGRAMS = [
    dict(key="bachelor", href="bachelor.html", short="Bachelor", type="Bachelor",
         title="Management Stratégique &amp; Opérationnel", level_big="Bac+3", level_small="Niveau 6",
         text="Devenir manager d'un centre de profit : piloter la performance, développer l'activité, manager les équipes.",
         tags=[("420 h", ""), ("RNCP38666", "tag--rncp"), ("Hybride", "")],
         grad="linear-gradient(150deg,#3a1820,#172033 70%)", a="#da0612", b="#fccd01",
         level="bac3", modes="presentiel distanciel hybride", tile="#b71c1c",
         mega="Bac+3 · Niveau 6 · 420 h — titre RNCP38666"),
    dict(key="mastere", href="mastere.html", short="Mastère", type="Mastère",
         title="Stratégie, Leadership &amp; Transformation des Organisations", level_big="Bac+5", level_small="Niveau 7 · 2 ans",
         text="Former les décideurs capables de penser la stratégie, conduire le changement et transformer durablement les organisations.",
         tags=[("900 h", ""), ("RNCP39994*", "tag--rncp"), ("Alternance possible", "")],
         grad="linear-gradient(150deg,#123651,#172033 70%)", a="#2f86ab", b="#a7dd63",
         level="bac5", modes="presentiel distanciel hybride", tile="#1e6a8a",
         mega="Bac+5 · Niveau 7 · 2 ans — RNCP39994"),
    dict(key="executive-mba", href="executive-mba.html", short="Executive MBA", type="Executive Education",
         title="Executive MBA Gouvernance, Leadership &amp; Transformation", level_big="EMBA", level_small="12 mois · Executive",
         text="Le programme de haute direction pour dirigeants, entrepreneurs et membres de CODIR.",
         tags=[("360 h + projet", ""), ("7 ans d'expérience", "tag--exec"), ("Hybride", "")],
         grad="linear-gradient(150deg,#3d311a,#172033 70%)", a="#fccd01", b="#da0612",
         level="executive", modes="presentiel distanciel hybride", tile="#7a5f2c",
         mega="Dirigeants · 12 mois · 360 h + Impact Project"),
    dict(key="ia-marketing-reseau", href="ia-marketing-reseau.html", short="Formation IA", type="Formation courte",
         title="IA appliquée au Marketing de Réseau", level_big="20 h", level_small="5 séances · à distance",
         text="Transformer la prospection, la communication et le développement du réseau par l'intelligence artificielle.",
         tags=[("Distanciel synchrone", ""), ("8 à 15 participants", ""), ("Attestation", "")],
         grad="linear-gradient(150deg,#1d3d28,#172033 70%)", a="#a7dd63", b="#2f86ab",
         level="courte", modes="distanciel", tile="#3f6e12",
         mega="20 h · 5 séances · distanciel synchrone"),
]
P = {p["key"]: p for p in PROGRAMS}

NAV = [("ecole.html", "L'école"), ("formations.html", "Formations"), ("pedagogie.html", "Pédagogie"),
       ("international.html", "International"), ("admissions.html", "Admissions"), ("entreprises.html", "Entreprises"),
       ("contact.html", "Contact")]
PROGRAM_FILES = {p["href"] for p in PROGRAMS}

def mega_menu():
    items = "".join(
        f'<a href="{p["href"]}"><span class="mega__icon" style="background:{p["tile"]}">{p["level_big"]}</span>'
        f'<span><span class="mega__title">{p["short"]} — {p["title"]}</span><span class="mega__desc">{p["mega"]}</span></span></a>'
        for p in PROGRAMS)
    return (f'<div class="mega" id="mega-formations" hidden>{items}'
            f'<div class="mega__foot"><a class="link-arrow" href="formations.html">Comparer toutes les formations {I["arrow"]}</a>'
            f'<a class="link-arrow" href="brochures.html">Télécharger les brochures {I["download"]}</a></div></div>')

def header(active):
    items = []
    for href, label in NAV:
        if href == "formations.html":
            cur = " is-current" if (active == href or active in PROGRAM_FILES) else ""
            items.append(
                f'<li class="nav__item"><a class="nav__link nojs-only{cur}" href="formations.html">Formations</a>'
                f'<button class="nav__link js-only{cur}" type="button" aria-expanded="false" aria-controls="mega-formations" data-dropdown>'
                f'Formations {I["chev"]}</button>{mega_menu()}</li>')
        else:
            cur = ' aria-current="page"' if href == active else ""
            items.append(f'<li class="nav__item"><a class="nav__link" href="{href}"{cur}>{label}</a></li>')
    return f'''<a class="skip-link" href="#contenu">Aller au contenu principal</a>
<div class="topbar on-dark">
  <div class="container">
    <p>Candidatures ouvertes — Bachelor, Mastère, Executive MBA et formation IA</p>
    <ul>
      <li><a href="brochures.html">Brochures</a></li>
      <li><a href="entreprises.html">Espace entreprises</a></li>
      <li><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
    </ul>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html">
      <img class="brand__mark" src="assets/img/emblem-21-header.png" width="154" height="128" alt="">
      <span class="brand__name">Academy Twenty One<span>University</span><span class="visually-hidden"> — retour à l'accueil</span></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">
      <span class="nav-toggle__bars" aria-hidden="true"><span></span></span> Menu
    </button>
    <nav class="nav" id="main-nav" aria-label="Navigation principale">
      <ul class="nav__list">{"".join(items)}</ul>
      <div class="nav__cta"><a class="btn btn--primary btn--sm" href="candidature.html">Candidater {I["arrow"]}</a></div>
    </nav>
  </div>
</header>'''

def footer():
    progs = "".join(f'<li><a href="{p["href"]}">{p["short"]} — {p["level_big"]}</a></li>' for p in PROGRAMS)
    return f'''<footer class="site-footer on-dark">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo-a21-university-light.png" width="320" height="326" alt="Academy 21 University">
        <p class="motto">Learn. Lead. Transform.</p>
        <p class="small">Une école de management, d'entrepreneuriat et de leadership — du Bachelor à l'Executive Education, en présentiel, à distance ou en hybride.</p>
      </div>
      <nav aria-labelledby="f-formations">
        <h2 id="f-formations">Formations</h2>
        <ul>{progs}<li><a href="formations.html">Toutes les formations</a></li></ul>
      </nav>
      <nav aria-labelledby="f-ecole">
        <h2 id="f-ecole">L'école</h2>
        <ul>
          <li><a href="ecole.html">Notre ambition</a></li>
          <li><a href="ecole.html#fondateur">Le fondateur</a></li>
          <li><a href="pedagogie.html">Pédagogie &amp; modalités</a></li>
          <li><a href="international.html">International</a></li>
          <li><a href="entreprises.html">Entreprises</a></li>
          <li><a href="brochures.html">Brochures</a></li>
        </ul>
      </nav>
      <nav aria-labelledby="f-candidats">
        <h2 id="f-candidats">Candidats</h2>
        <ul>
          <li><a href="admissions.html">Admissions</a></li>
          <li><a href="candidature.html">Candidater en ligne</a></li>
          <li><a href="admissions.html#faq">Questions fréquentes</a></li>
          <li><a href="contact.html">Nous contacter</a></li>
          <li><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
        </ul>
      </nav>
    </div>
    <div class="footer-bottom">
      <p>© <span data-year>2026</span> {SCHOOL}. Tous droits réservés.</p>
      <ul>
        <li><a href="mentions-legales.html">Mentions légales</a></li>
        <li><a href="confidentialite.html">Confidentialité</a></li>
        <li><a href="accessibilite.html">Accessibilité : partiellement conforme</a></li>
        <li><a href="plan-du-site.html">Plan du site</a></li>
      </ul>
    </div>
  </div>
</footer>
<button class="to-top" type="button" aria-label="Revenir en haut de la page">{I["arrow-up"]}</button>
<script src="assets/js/main.js" defer></script>'''

# Pas de pictogrammes décoratifs dans les cartes (demande de l'école) : on retire les pastilles d'icônes.
_DECO_ICON = re.compile(r'<span class="(?:icon-badge|float-card__icon)[^"]*"[^>]*>\s*<svg.*?</svg>\s*</span>', re.S)


def page(fname, title, desc, body, active=None, noindex=False):
    body = _DECO_ICON.sub("", body)
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    html = f'''<!doctype html>
<html lang="fr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{robots}
<meta name="theme-color" content="#172033">
<meta name="a21-contact" content="{CONTACT_EMAIL}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/logo-a21-university.png">
<meta property="og:locale" content="fr_FR">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/montserrat-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">
<script>document.documentElement.className=document.documentElement.className.replace("no-js","js");</script>
</head>
<body>
{header(active or fname)}
<main id="contenu" tabindex="-1">
{body}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(html)

# --- Blocs réutilisables ---
def cta_band(title, text, prog=None, secondary=None):
    q = f"?programme={prog}" if prog else ""
    sec = secondary or ('<a class="btn btn--glass" href="contact.html">Poser une question</a>')
    return f'''<section class="section--tight" aria-labelledby="cta-title">
  <div class="container">
    <div class="cta-band on-dark reveal">
      {ring("deco", uid="cta")}
      <div><h2 id="cta-title">{title}</h2><p>{text}</p></div>
      <div class="btn-row"><a class="btn btn--accent" href="candidature.html{q}">Déposer ma candidature {I["arrow"]}</a>{sec}</div>
    </div>
  </div>
</section>'''

def program_card(key, heading="h3"):
    p = P[key]
    tg = "".join(f'<li class="tag{(" " + c) if c else ""}">{t}</li>' for t, c in p["tags"])
    return f'''<article class="program-card" data-program data-level="{p["level"]}" data-modes="{p["modes"]}">
  <div class="program-card__media" style="background:{p["grad"]}">
    {ring("deco", p["a"], p["b"], "c" + p["key"][:3])}
    <p class="program-card__level"><b>{p["level_big"]}</b><small>{p["level_small"]}</small></p>
  </div>
  <div class="program-card__body">
    <p class="program-card__type">{p["type"]}</p>
    <{heading}><a href="{p["href"]}">{p["title"]}</a></{heading}>
    <p>{p["text"]}</p>
    <ul class="program-card__meta" aria-label="Informations clés">{tg}</ul>
    <span class="program-card__more link-arrow" aria-hidden="true">Découvrir la formation {I["arrow"]}</span>
  </div>
</article>'''

def facts(rows, key):
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    pdf = BROCHURES[key][0]
    return f'''<section class="facts" aria-labelledby="facts-title">
  <h2 id="facts-title">{I["info"]} L'essentiel</h2>
  <dl>{dl}</dl>
  <div class="btn-row">
    <a class="btn btn--primary btn--sm" href="candidature.html?programme={key}">Candidater {I["arrow"]}</a>
    <a class="btn btn--ghost btn--sm" href="{pdf}" download>{I["download"]} Brochure <span class="visually-hidden">({pdf_size(key)})</span></a>
  </div>
</section>'''

def subnav(items, key):
    li = "".join(f'<li><a href="#{i}">{l}</a></li>' for i, l in items)
    return (f'<nav class="subnav" aria-label="Sommaire de la page"><div class="container"><ul>{li}</ul>'
            f'<a class="btn btn--primary btn--sm subnav__cta" href="candidature.html?programme={key}">Candidater</a></div></nav>')

def crumbs(items):
    out = '<li><a href="index.html">Accueil</a></li>'
    for href, label in items[:-1]:
        out += f'<li><a href="{href}">{label}</a></li>'
    out += f'<li><span aria-current="page">{items[-1][1]}</span></li>'
    return f'<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>{out}</ol></nav>'

def notice(html, kind=""):
    k = f" notice--{kind}" if kind else ""
    icon = I["check"] if kind == "success" else I["info"]
    return f'<div class="notice{k}" role="note">{icon}<div>{html}</div></div>'

def table(caption, head, rows, foot=None, vol_col=1):
    V = ' class="vol"'
    th = "".join(f'<th scope="col"{V if i == vol_col else ""}>{h}</th>' for i, h in enumerate(head))
    body = ""
    for r in rows:
        body += "<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(
            f'<td{V if i + 1 == vol_col else ""}>{c}</td>' for i, c in enumerate(r[1:])) + "</tr>"
    ft = ""
    if foot:
        ft = "<tfoot><tr>" + f'<th scope="row">{foot[0]}</th>' + "".join(
            f'<td{V if i + 1 == vol_col else ""}>{c}</td>' for i, c in enumerate(foot[1:])) + "</tr></tfoot>"
    plain = caption.replace("&amp;", "&")
    return (f'<div class="table-wrap" role="region" aria-label="{plain}" tabindex="0"><table class="data-table">'
            f'<caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}</tbody>{ft}</table></div>')

def aside_program(key, name):
    pdf = BROCHURES[key][0]
    return f'''<aside aria-label="Candidature et documentation">
  <div class="aside-card aside-card--navy on-dark">
    <h2>Prêt·e à candidater ?</h2>
    <p class="small">Admission sur dossier et entretien. Le formulaire en ligne prend une dizaine de minutes et votre brouillon est enregistré automatiquement.</p>
    <a class="btn btn--accent" href="candidature.html?programme={key}">Candidater au {name} {I["arrow"]}</a>
    <a class="btn btn--glass" href="{pdf}" download>{I["download"]} Brochure ({pdf_size(key)})</a>
  </div>
  <div class="aside-card">
    <h2>Une question ?</h2>
    <ul class="aside-list">
      <li>{I["message"]}<span><a href="contact.html?objet=information&amp;programme={key}">Écrire à l'équipe admissions</a></span></li>
      <li>{I["mail"]}<span><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></span></li>
      <li>{I["info"]}<span><a href="admissions.html#faq">Questions fréquentes</a></span></li>
    </ul>
  </div>
</aside>'''

def related(keys, title="Poursuivre votre réflexion"):
    cards = "".join(program_card(k) for k in keys)
    cols = "grid--3" if len(keys) == 3 else "grid--2"
    return f'''<section class="section section--surface" aria-labelledby="rel-title">
  <div class="container">
    <div class="section-head section-head--row reveal"><div><p class="eyebrow">Autres programmes</p><h2 id="rel-title">{title}</h2></div>
    <a class="link-arrow" href="formations.html">Toutes les formations {I["arrow"]}</a></div>
    <div class="grid {cols} reveal-stagger">{cards}</div>
  </div>
</section>'''

PHOTOS = {
    "bibliotheque": "/assets/img/photos/campus-bibliotheque.jpg",
    "livres": "/assets/img/photos/etudiants-livres.jpg",
    "projet": "/assets/img/photos/equipe-projet.jpg",
    "echange": "/assets/img/photos/equipe-echange.jpg",
    "reussite": "/assets/img/photos/reussite.jpg",
    "leadership": "/assets/img/photos/leadership-entreprise.jpg",
}

def photo_style(key):
    return f' style="--photo:url({PHOTOS[key]})"' if key else ""

def simple_hero(crumb_items, title, lead, eyebrow=None, extra="", uid="ph", photo=None):
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    cls = " page-hero--photo" if photo else ""
    return f'''<section class="page-hero page-hero--simple{cls} on-dark" aria-labelledby="page-title"{photo_style(photo)}>
  <div class="grid-texture" aria-hidden="true"></div>
  {ring("deco", uid=uid)}
  <div class="container"><div>
    {crumbs(crumb_items)}
    {eb}<h1 id="page-title">{title}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div></div>
</section>'''


# --- Fondateur : Dr Raoul Ruben NJIONOU ---
# Déposez les photos dans assets/img/photos/ sous ces noms : elles sont prises en compte automatiquement.
FOUNDER_ALTS = ["Portrait du Dr Raoul Ruben NJIONOU, fondateur d'Academy Twenty One", 'Le Dr Raoul Ruben NJIONOU anime une séance devant les membres de la communauté', "Le Dr Raoul Ruben NJIONOU s'exprime sur scène lors d'un événement Academy Twenty One"]
FOUNDER_PHOTOS = ["dr-raoul-njionou-1.jpg", "dr-raoul-njionou-2.jpg", "dr-raoul-njionou-3.jpg"]

def founder_photos():
    return [f"/assets/img/photos/{f}" for f in FOUNDER_PHOTOS if os.path.exists(os.path.join(ROOT, "assets/img/photos", f))]

FOUNDER_TEXT = ("Fondateur, Chairman &amp; CEO d'A21. Avec près de 15 ans d'expérience dans le Marketing de Réseau "
                "et plus de 20 ans dans le monde des affaires, il a su se faire une place au sommet. "
                "Leader d'impact reconnu sur 5 continents.")

def founder_block(heading="h2", more_href="ecole.html#fondateur", more_label="En savoir plus", gallery=False, hid="founder-title"):
    photos = founder_photos()
    portrait_style = f' style="--photo:url({photos[0]})"' if photos else ""
    gal = ""
    if gallery and len(photos) > 1:
        gal = '<div class="founder__gallery">' + "".join(
            f'<div style="--photo:url({ph})">{zoom_btn(ph, FOUNDER_ALTS[n + 1], "fondateur")}</div>' for n, ph in enumerate(photos[1:])) + "</div>"
    ext = ' rel="noopener" target="_blank"' if more_href.startswith("http") else ""
    sr = '<span class="visually-hidden"> (nouvel onglet)</span>' if ext else ""
    label = ""
    full = " founder--full" if gal else ""
    return f'''<article class="founder{full} reveal" aria-labelledby="{hid}">
  <div class="founder__portrait"{portrait_style}><span aria-hidden="true">RRN</span>{zoom_btn(photos[0], FOUNDER_ALTS[0], "fondateur") if photos else ""}</div>
  <div>
    <p class="eyebrow">Le fondateur</p>
    <{heading} id="{hid}">Dr. Raoul Ruben NJIONOU</{heading}>
    <p class="founder__text">{FOUNDER_TEXT}</p>
    <a class="link-arrow" href="{more_href}"{ext}>{more_label}{sr} {I["arrow"]}</a>
    {gal}
  </div>
</article>'''


# =====================================================================
# Ambiances et en-têtes de page variés (une mise en page par type de page)
# =====================================================================

def ring4(cls="ring4", uid="q"):
    """Anneau aux quatre couleurs du logo : rouge, jaune, vert, bleu."""
    return f'''<svg class="{cls}" viewBox="0 0 240 240" aria-hidden="true" focusable="false">
<circle cx="120" cy="120" r="104" fill="none" stroke="currentColor" stroke-opacity=".12" stroke-width="1"/>
<path d="M120 16 A104 104 0 0 1 224 120" fill="none" stroke="#da0612" stroke-width="7" stroke-linecap="round"/>
<path d="M224 120 A104 104 0 0 1 120 224" fill="none" stroke="#fccd01" stroke-width="7" stroke-linecap="round" stroke-dasharray="150 400"/>
<path d="M120 224 A104 104 0 0 1 16 120" fill="none" stroke="#a7dd63" stroke-width="7" stroke-linecap="round" stroke-dasharray="120 400"/>
<path d="M16 120 A104 104 0 0 1 120 16" fill="none" stroke="#2f86ab" stroke-width="7" stroke-linecap="round" stroke-dasharray="90 400"/>
<circle cx="120" cy="120" r="80" fill="none" stroke="currentColor" stroke-opacity=".08" stroke-width="1" stroke-dasharray="2 6"/>
</svg>'''


def _crumbs_light(items):
    return crumbs(items).replace('class="breadcrumb"', 'class="breadcrumb breadcrumb--light"')


def hero_light(crumb_items, title, lead, eyebrow=None, extra="", visual="", amb="red", shape="galet"):
    """En-tête clair et compact (pages de service) ; visuel facultatif à droite."""
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    vis = f'<div class="hero-light__visual hero-light__visual--{shape}">{visual}</div>' if visual else ""
    cols = " hero-light--split" if visual else ""
    return f'''<section class="hero-light{cols} amb-{amb}" aria-labelledby="page-title">
  {ring4("ring4 hero-light__ring", "hl")}
  <div class="container hero-light__inner">
    <div class="hero-light__text">
      {_crumbs_light(crumb_items)}
      {eb}<h1 id="page-title">{title}</h1>
      <p class="lead">{lead}</p>
      {extra}
    </div>
    {vis}
  </div>
</section>'''


def zoom_btn(src, alt, group=""):
    """Bouton transparent posé sur une image : ouvre la visionneuse (assets/js/main.js)."""
    g = f' data-zoom-group="{group}"' if group else ""
    return (f'<button type="button" class="zoom-btn" data-zoom="{src}" data-zoom-alt="{alt}"{g} '
            f'aria-label="Agrandir la photo : {alt}"><span class="zoom-btn__chip" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            f'<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2M11 8.5v5M8.5 11h5"/></svg></span></button>')


def photo_img(key, alt, pos="center"):
    return f'<img src="{PHOTOS[key]}" alt="{alt}" loading="eager" style="object-position:{pos}">{zoom_btn(PHOTOS[key], alt)}'


def hero_editorial(crumb_items, title, lead, eyebrow, photo, extra="", amb="gold"):
    """Grande photo pleine largeur, texte ancré en bas : page vitrine."""
    return f'''<section class="hero-editorial on-dark amb-{amb}" aria-labelledby="page-title"{photo_style(photo)}>
  <div class="container hero-editorial__inner">
    {crumbs(crumb_items)}
    <p class="eyebrow">{eyebrow}</p>
    <h1 id="page-title">{title}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div>
  {ring4("ring4 hero-editorial__ring", "he")}
</section>'''


def hero_visual(crumb_items, title, lead, eyebrow, visual, extra="", amb="blue"):
    """En-tête sombre en deux colonnes avec une illustration (international, IA)."""
    return f'''<section class="hero-visual-page on-dark amb-{amb}" aria-labelledby="page-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container hero-visual-page__inner">
    <div>
      {crumbs(crumb_items)}
      <p class="eyebrow">{eyebrow}</p>
      <h1 id="page-title">{title}</h1>
      <p class="lead">{lead}</p>
      {extra}
    </div>
    <figure class="hero-visual-page__figure" aria-hidden="true">{visual}</figure>
  </div>
</section>'''


def hero_minimal(crumb_items, title, lead):
    """Pages de texte (légal, plan du site) : pas de bannière, un simple titre."""
    return f'''<header class="hero-minimal" aria-labelledby="page-title">
  <div class="container">
    {_crumbs_light(crumb_items)}
    <h1 id="page-title">{title}</h1>
    <p class="lead">{lead}</p>
    <span class="rule4" aria-hidden="true"></span>
  </div>
</header>'''


def facts_strip(rows, label="L'essentiel"):
    """Bandeau de faits en verre, qui chevauche le bas de l'en-tête des fiches programme."""
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    return f'''<section class="facts-strip" aria-label="{label}">
  <div class="container"><dl>{dl}</dl></div>
</section>'''


GLOBE_SVG = '''<svg viewBox="0 0 520 520" fill="none">
<defs><radialGradient id="glb" cx="40%" cy="35%" r="65%"><stop offset="0" stop-color="#2f86ab" stop-opacity=".55"/><stop offset="1" stop-color="#172033" stop-opacity="0"/></radialGradient></defs>
<circle cx="260" cy="260" r="200" fill="url(#glb)"/>
<g stroke="#7cc3e0" stroke-opacity=".45" stroke-width="1.2">
<circle cx="260" cy="260" r="200"/><ellipse cx="260" cy="260" rx="200" ry="66"/><ellipse cx="260" cy="260" rx="200" ry="134"/>
<ellipse cx="260" cy="260" rx="66" ry="200"/><ellipse cx="260" cy="260" rx="134" ry="200"/><path d="M60 260h400M260 60v400"/></g>
<g stroke="#fccd01" stroke-width="2" stroke-dasharray="3 7" stroke-linecap="round"><path d="M150 200 Q 240 110 350 170"/><path d="M180 330 Q 280 400 380 300"/><path d="M350 170 Q 420 230 380 300"/></g>
<g><circle cx="150" cy="200" r="9" fill="#da0612"/><circle cx="350" cy="170" r="9" fill="#fccd01"/><circle cx="380" cy="300" r="9" fill="#a7dd63"/><circle cx="180" cy="330" r="9" fill="#2f86ab"/>
<circle cx="150" cy="200" r="20" stroke="#da0612" stroke-opacity=".4"/><circle cx="350" cy="170" r="20" stroke="#fccd01" stroke-opacity=".4"/><circle cx="380" cy="300" r="20" stroke="#a7dd63" stroke-opacity=".4"/><circle cx="180" cy="330" r="20" stroke="#2f86ab" stroke-opacity=".4"/></g>
<path d="M260 30 A230 230 0 0 1 490 260" stroke="#da0612" stroke-width="5" stroke-linecap="round"/>
<path d="M490 260 A230 230 0 0 1 260 490" stroke="#fccd01" stroke-width="5" stroke-linecap="round" stroke-dasharray="200 600"/>
<path d="M260 490 A230 230 0 0 1 30 260" stroke="#a7dd63" stroke-width="5" stroke-linecap="round" stroke-dasharray="160 600"/>
<path d="M30 260 A230 230 0 0 1 260 30" stroke="#2f86ab" stroke-width="5" stroke-linecap="round" stroke-dasharray="120 600"/>
</svg>'''

NETWORK_SVG = '''<svg viewBox="0 0 520 520" fill="none">
<g stroke="#7cc3e0" stroke-opacity=".35" stroke-width="1.3">
<path d="M260 260L110 140M260 260L410 120M260 260L440 300M260 260L330 440M260 260L120 380M260 260L70 260"/>
<path d="M110 140L410 120M410 120L440 300M440 300L330 440M330 440L120 380M120 380L70 260M70 260L110 140" stroke-dasharray="4 8"/></g>
<g fill="#172033" stroke-width="2.5">
<circle cx="110" cy="140" r="22" stroke="#2f86ab"/><circle cx="410" cy="120" r="18" stroke="#a7dd63"/><circle cx="440" cy="300" r="24" stroke="#fccd01"/>
<circle cx="330" cy="440" r="18" stroke="#da0612"/><circle cx="120" cy="380" r="20" stroke="#a7dd63"/><circle cx="70" cy="260" r="14" stroke="#2f86ab"/></g>
<g stroke="#fff" stroke-opacity=".85" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M101 140h18M110 131v18"/><path d="M402 120l6 6 10-12"/><path d="M430 300h20M440 290l10 10-10 10"/><path d="M322 440h16"/><path d="M112 380a8 8 0 1 0 16 0a8 8 0 1 0-16 0"/></g>
<circle cx="260" cy="260" r="92" fill="#fff"/><circle cx="260" cy="260" r="108" stroke="#fccd01" stroke-width="3" stroke-dasharray="6 10"/>
<g stroke="#172033" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><circle cx="260" cy="236" r="26"/><path d="M212 318c8-28 28-42 48-42s40 14 48 42"/></g>
<circle cx="260" cy="260" r="150" stroke="#2f86ab" stroke-opacity=".25"/>
</svg>'''
