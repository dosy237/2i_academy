# Génère les pages statiques du site Academy 21 University (en-tête/pied communs).
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def ic(path, extra=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"{extra}>{path}</svg>'

I = {
 "arrow": ic('<path d="M5 12h14M13 6l6 6-6 6"/>'),
 "download": ic('<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>'),
 "compass": ic('<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>'),
 "scale": ic('<path d="M12 4v16M7 20h10M5 8h14M5 8l-2.5 6a3 3 0 0 0 5 0zM19 8l-2.5 6a3 3 0 0 0 5 0z"/>'),
 "users": ic('<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.6"/><path d="M16 14.2c2.8.2 5 2.6 5 5.8"/>'),
 "refresh": ic('<path d="M20 11a8 8 0 0 0-14.5-4.5L4 8M4 4v4h4M4 13a8 8 0 0 0 14.5 4.5L20 16M20 20v-4h-4"/>'),
 "globe": ic('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>'),
 "shield": ic('<path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/>'),
 "chart": ic('<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'),
 "cart": ic('<path d="M3 4h2.5l2.2 11h10.6L21 7H6.4"/><circle cx="9" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/>'),
 "leader": ic('<circle cx="12" cy="7" r="3.5"/><path d="M5 21v-1a7 7 0 0 1 14 0v1"/><path d="M12 14l1.4 2.6L12 21l-1.4-4.4z"/>'),
 "cpu": ic('<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9.5 9.5h5v5h-5zM9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>'),
 "building": ic('<path d="M4 21V5l8-3 8 3v16M2 21h20M9 21v-5h6v5M8 8h.01M12 8h.01M16 8h.01M8 12h.01M12 12h.01M16 12h.01"/>'),
 "monitor": ic('<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>'),
 "layers": ic('<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>'),
 "clock": ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "award": ic('<circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/>'),
 "info": ic('<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5h.01"/>'),
 "mail": ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'),
 "phone": ic('<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>'),
 "pin": ic('<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'),
 "target": ic('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>'),
 "bulb": ic('<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>'),
 "mic": ic('<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>'),
 "briefcase": ic('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>'),
 "calendar": ic('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'),
 "spark": ic('<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>'),
 "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.2c0-1.3 0-2.9-1.8-2.9s-2 1.4-2 2.8V21h-4z"/></svg>',
 "facebook": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v7h4v-7h3l.5-4h-3.5V8.8c0-.5.3-.8.5-.8z"/></svg>',
 "instagram": ic('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>'),
 "youtube": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M22 8.2a3 3 0 0 0-2.1-2.1C18 5.6 12 5.6 12 5.6s-6 0-7.9.5A3 3 0 0 0 2 8.2 31 31 0 0 0 1.6 12 31 31 0 0 0 2 15.8a3 3 0 0 0 2.1 2.1c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1c.4-1.2.4-3.8.4-3.8s0-2.6-.4-3.8zM10 15V9l5.2 3z"/></svg>',
}

def ring(cls="deco", a="#da0612", b="#fccd01", uid="r"):
    """Arcs reprenant l'anneau du logo (rouge + jaune), décoratifs."""
    return f'''<svg class="{cls}" viewBox="0 0 200 200" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="{uid}a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{a}" stop-opacity=".25"/></linearGradient>
    <linearGradient id="{uid}b" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{b}"/><stop offset="1" stop-color="{b}" stop-opacity=".2"/></linearGradient>
  </defs>
  <path d="M150 30 A86 86 0 1 0 170 150" fill="none" stroke="url(#{uid}a)" stroke-width="14" stroke-linecap="round"/>
  <path d="M60 45 A64 64 0 0 1 160 120" fill="none" stroke="url(#{uid}b)" stroke-width="10" stroke-linecap="round"/>
</svg>'''

NAV = [("index.html","Accueil"),("formations.html","Formations"),("admissions.html","Admissions"),("charte.html","Charte graphique"),("contact.html","Contact")]
PROG_NAV = {"bachelor.html","mastere.html","executive-mba.html","ia-marketing-reseau.html"}

def header(active):
    items=[]
    for href,label in NAV:
        cur = ' aria-current="page"' if (href==active or (href=="formations.html" and active in PROG_NAV)) else ""
        items.append(f'<li><a class="nav__link" href="{href}"{cur}>{label}</a></li>')
    return f'''<a class="skip-link" href="#contenu">Aller au contenu principal</a>
<div class="topbar on-dark">
  <div class="container">
    <p class="mb-0">Candidatures ouvertes — rentrée prochaine</p>
    <ul>
      <li><a href="tel:+33000000000">+33 (0)0 00 00 00 00</a></li>
      <li><a href="mailto:admissions@a21-university.example">admissions@a21-university.example</a></li>
    </ul>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html">
      <img src="assets/img/logo-a21-university.png" width="320" height="326" alt="Academy 21 University — accueil">
      <span class="brand__name" aria-hidden="true">Academy Twenty One<span>University</span></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">
      <span class="nav-toggle__bars" aria-hidden="true"><span></span></span> Menu
    </button>
    <nav class="nav" id="main-nav" aria-label="Navigation principale">
      <ul class="nav__list">
        {"".join(items)}
      </ul>
      <div class="nav__cta"><a class="btn btn--primary btn--sm" href="contact.html?programme=candidature">Candidater</a></div>
    </nav>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer on-dark">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo-a21-university-light.png" width="320" height="326" alt="Academy 21 University">
        <p class="motto">Apprendre. Diriger. Transformer.</p>
        <p class="small">Une offre cohérente du Bac+3 à l'Executive Education, centrée sur le management, l'entrepreneuriat et le leadership.</p>
        <div class="socials">
          <a href="#" aria-label="LinkedIn (lien à compléter)">{I["linkedin"]}</a>
          <a href="#" aria-label="Facebook (lien à compléter)">{I["facebook"]}</a>
          <a href="#" aria-label="Instagram (lien à compléter)">{I["instagram"]}</a>
          <a href="#" aria-label="YouTube (lien à compléter)">{I["youtube"]}</a>
        </div>
      </div>
      <nav aria-labelledby="f-formations">
        <h2 id="f-formations">Formations</h2>
        <ul>
          <li><a href="bachelor.html">Bachelor Management (Bac+3)</a></li>
          <li><a href="mastere.html">Mastère Stratégie &amp; Leadership (Bac+5)</a></li>
          <li><a href="executive-mba.html">Executive MBA</a></li>
          <li><a href="ia-marketing-reseau.html">IA &amp; Marketing de réseau</a></li>
        </ul>
      </nav>
      <nav aria-labelledby="f-ecole">
        <h2 id="f-ecole">L'école</h2>
        <ul>
          <li><a href="formations.html">Toutes les formations</a></li>
          <li><a href="admissions.html">Admissions</a></li>
          <li><a href="admissions.html#faq">Questions fréquentes</a></li>
          <li><a href="contact.html">Nous contacter</a></li>
        </ul>
      </nav>
      <div>
        <h2>Contact</h2>
        <ul>
          <li>Adresse du campus — à compléter</li>
          <li><a href="tel:+33000000000">+33 (0)0 00 00 00 00</a></li>
          <li><a href="mailto:admissions@a21-university.example">admissions@a21-university.example</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="mb-0">© <span id="year">2026</span> Academy Twenty One University. Tous droits réservés.</p>
      <ul>
        <li><a href="#">Mentions légales</a></li>
        <li><a href="#">Politique de confidentialité</a></li>
        <li><a href="#">Accessibilité : partiellement conforme</a></li>
        <li><a href="#">Plan du site</a></li>
      </ul>
    </div>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>'''

def page(fname, title, desc, body, active=None):
    html = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#172033">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Plus+Jakarta+Sans:wght@600;700;800&amp;family=Source+Serif+4:ital,wght@1,400;1,600&amp;display=swap">
<link rel="stylesheet" href="assets/css/styles.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
{header(active or fname)}
<main id="contenu" tabindex="-1">
{body}
</main>
{FOOTER}
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w").write(html)

def cta_band(title, text, prog=None):
    q = f"?programme={prog}" if prog else "?programme=candidature"
    return f'''<section class="section--tight" aria-labelledby="cta-title">
  <div class="container">
    <div class="cta-band on-dark">
      {ring("deco", uid="cta")}
      <div>
        <h2 id="cta-title">{title}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--accent" href="contact.html{q}">Déposer ma candidature {I["arrow"]}</a>
        <a class="btn btn--ghost-light" href="contact.html?programme=information">Être rappelé·e</a>
      </div>
    </div>
  </div>
</section>'''

def program_card(href, typ, title, text, level_big, level_small, tags, grad, a, b, uid, level, modes, extra_cls=""):
    tg = "".join(f'<li class="tag{(" "+c) if c else ""}">{t}</li>' for t,c in tags)
    return f'''<article class="program-card reveal{extra_cls}" data-program data-level="{level}" data-modes="{modes}">
  <div class="program-card__media" style="background:{grad}">
    {ring("deco", a, b, uid)}
    <p class="program-card__level mb-0"><b>{level_big}</b><small>{level_small}</small></p>
  </div>
  <div class="program-card__body">
    <p class="program-card__type">{typ}</p>
    <h3><a href="{href}">{title}</a></h3>
    <p>{text}</p>
    <ul class="program-card__meta" aria-label="Informations clés">{tg}</ul>
    <span class="program-card__more link-arrow" aria-hidden="true">Découvrir la formation {I["arrow"]}</span>
  </div>
</article>'''

CARDS = dict(
 bachelor=lambda: program_card("bachelor.html","Bachelor","Management Stratégique &amp; Opérationnel",
   "Devenir manager d'un centre de profit : piloter la performance, développer l'activité, manager les équipes.",
   "Bac+3","Niveau 6",[("420 h",""),("RNCP38666","tag--rncp"),("Hybride","")],
   "linear-gradient(150deg,#2a1a22,#172033 70%)","#da0612","#fccd01","cb","bac3","presentiel distanciel hybride"),
 mastere=lambda: program_card("mastere.html","Mastère","Stratégie, Leadership &amp; Transformation des Organisations",
   "Former les décideurs capables de penser la stratégie, conduire le changement et transformer durablement les organisations.",
   "Bac+5","Niveau 7 · 2 ans",[("900 h",""),("RNCP39994*","tag--rncp"),("Alternance possible","")],
   "linear-gradient(150deg,#16324a,#172033 70%)","#2f86ab","#a7dd63","cm","bac5","presentiel distanciel hybride"),
 emba=lambda: program_card("executive-mba.html","Executive Education","Executive MBA Gouvernance, Leadership &amp; Transformation",
   "Le programme de haute direction pour dirigeants, entrepreneurs et membres de CODIR. Think. Decide. Lead. Transform.",
   "EMBA","12 mois · Executive",[("360 h + projet",""),("7 ans d'expérience","tag--exec"),("Hybride","")],
   "linear-gradient(150deg,#3a2f1c,#172033 70%)","#fccd01","#da0612","ce","executive","presentiel distanciel hybride"),
 ia=lambda: program_card("ia-marketing-reseau.html","Formation courte","IA appliquée au Marketing de Réseau",
   "Transformer la prospection, la communication et le développement du réseau par l'intelligence artificielle.",
   "20 h","5 séances · à distance",[("Distanciel synchrone",""),("8 à 15 participants",""),("Attestation","")],
   "linear-gradient(150deg,#1f3a2a,#172033 70%)","#a7dd63","#2f86ab","ci","courte","distanciel"),
)

def facts(rows, prog, brochure=True):
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k,v in rows)
    b = f'<a class="btn btn--ghost btn--sm" href="contact.html?programme=brochure">{I["download"]} Brochure</a>' if brochure else ""
    return f'''<section class="facts" aria-labelledby="facts-title">
  <h2 id="facts-title">L'essentiel</h2>
  <dl>{dl}</dl>
  <div class="btn-row">
    <a class="btn btn--primary btn--sm" href="contact.html?programme={prog}">Candidater</a>
    {b}
  </div>
</section>'''

def subnav(items):
    li="".join(f'<li><a href="#{i}">{l}</a></li>' for i,l in items)
    return f'<nav class="subnav" aria-label="Sommaire de la fiche"><div class="container"><ul>{li}</ul></div></nav>'

def crumbs(name):
    return f'''<nav class="breadcrumb" aria-label="Fil d'Ariane"><ol>
  <li><a href="index.html">Accueil</a></li><li><a href="formations.html">Formations</a></li><li><span aria-current="page">{name}</span></li>
</ol></nav>'''

def notice(html, kind=""):
    icon = I["info"]
    return f'<div class="notice{(" notice--"+kind) if kind else ""}" role="note">{icon}<div>{html}</div></div>'

def table(caption, head, rows, foot=None, vol_col=1):
    V = ' class="vol"'
    th = "".join(f'<th scope="col"{V if i==vol_col else ""}>{h}</th>' for i,h in enumerate(head))
    body=""
    for r in rows:
        cells=f'<th scope="row">{r[0]}</th>'+"".join(f'<td{V if i+1==vol_col else ""}>{c}</td>' for i,c in enumerate(r[1:]))
        body+=f"<tr>{cells}</tr>"
    ft=""
    if foot:
        ft="<tfoot><tr>"+f'<th scope="row">{foot[0]}</th>'+"".join(f'<td{V if i+1==vol_col else ""}>{c}</td>' for i,c in enumerate(foot[1:]))+"</tr></tfoot>"
    return f'''<div class="table-wrap" role="region" aria-label="{caption}" tabindex="0">
<table class="data-table"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}</tbody>{ft}</table></div>'''

def aside(prog, name, extra=""):
    return f'''<aside aria-label="Candidature et contact">
  <div class="aside-card aside-card--navy on-dark">
    <h2>Prêt·e à candidater ?</h2>
    <p class="small">Admission sur dossier et entretien. Un conseiller vous accompagne à chaque étape.</p>
    <a class="btn btn--accent" href="contact.html?programme={prog}">Candidater au {name}</a>
    <a class="btn btn--ghost-light" href="contact.html?programme=brochure">{I["download"]} Recevoir la brochure</a>
  </div>
  <div class="aside-card">
    <h2>Une question ?</h2>
    <p class="small mb-0">Notre équipe admissions vous répond du lundi au vendredi.</p>
    <p class="small mb-0 mt-2"><a href="tel:+33000000000">+33 (0)0 00 00 00 00</a><br><a href="mailto:admissions@a21-university.example">admissions@a21-university.example</a></p>
  </div>
  {extra}
</aside>'''

# =====================================================================
# ACCUEIL
# =====================================================================
home = f'''
<section class="hero on-dark" aria-labelledby="hero-title">
  <div class="container">
    <div>
      <p class="eyebrow">Management · Entrepreneuriat · Leadership</p>
      <h1 id="hero-title">Former ceux qui <em>dirigeront demain.</em></h1>
      <p class="lead">Du Bachelor Bac+3 à l'Executive MBA, Academy Twenty One University forme des managers, des leaders et des dirigeants capables de décider, de mobiliser et de transformer les organisations.</p>
      <div class="btn-row">
        <a class="btn btn--accent" href="formations.html">Découvrir nos formations {I["arrow"]}</a>
        <a class="btn btn--ghost-light" href="admissions.html">Comment candidater ?</a>
      </div>
      <ul class="hero__proof" aria-label="Chiffres clés">
        <li><strong>Bac+3 → Executive</strong><span>une filière complète</span></li>
        <li><strong>3 modalités</strong><span>présentiel, distanciel, hybride</span></li>
        <li><strong>2 référentiels RNCP</strong><span>niveaux 6 et 7</span></li>
      </ul>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <svg class="hero-visual__ring" viewBox="0 0 200 200">
        <defs>
          <linearGradient id="hr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#da0612"/><stop offset="1" stop-color="#7a0a10"/></linearGradient>
          <linearGradient id="hy" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fccd01"/><stop offset="1" stop-color="#fccd01" stop-opacity=".1"/></linearGradient>
        </defs>
        <path d="M169 42 A90 90 0 1 0 158 169" fill="none" stroke="url(#hr)" stroke-width="5" stroke-linecap="round"/>
        <path d="M17 52 A96 96 0 0 1 193 125" fill="none" stroke="url(#hy)" stroke-width="3" stroke-linecap="round"/>
      </svg>
      <div class="hero-visual__disc">
        <img class="emblem" src="assets/img/emblem-21.png" alt="" width="256" height="256">
      </div>
      <div class="float-card float-card--a">
        <span class="float-card__icon" style="background:#eef8e2;color:#3f6e12">{I["award"]}</span>
        <span><strong>RNCP38666</strong>Titre pro. niveau 6</span>
      </div>
      <div class="float-card float-card--b">
        <span class="float-card__icon" style="background:#fff6cc;color:#5f4a00">{I["layers"]}</span>
        <span><strong>Hybride</strong>Sur site ou à distance</span>
      </div>
      <div class="float-card float-card--c">
        <span class="float-card__icon" style="background:#fbecec;color:#b71c1c">{I["leader"]}</span>
        <span><strong>Leadership</strong>la signature de nos parcours</span>
      </div>
    </div>
  </div>
  <svg class="wave" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path fill="currentColor" d="M0 60c240-50 480-60 720-30s480 40 720-10v70H0z"/></svg>
</section>

<section class="finder" aria-labelledby="finder-title">
  <div class="container">
    <div class="finder__panel">
      <h2 class="finder__title" id="finder-title">Trouver ma formation<span>selon mon niveau et mon projet</span></h2>
      <ul class="pill-nav">
        <li><a href="bachelor.html">Bachelor<span>Bac+3 · Niveau 6</span></a></li>
        <li><a href="mastere.html">Mastère<span>Bac+5 · Niveau 7</span></a></li>
        <li><a href="executive-mba.html">Executive MBA<span>Dirigeants · 12 mois</span></a></li>
        <li><a href="ia-marketing-reseau.html">Formation IA<span>20 h · à distance</span></a></li>
        <li><a href="contact.html?programme=information">Être conseillé·e<span>Entretien d'orientation</span></a></li>
      </ul>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="ambition-title">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Notre ambition</p>
      <h2 id="ambition-title">Une école qui associe exigence, terrain et responsabilité</h2>
      <p class="lead">Academy Twenty One University construit une offre cohérente centrée sur le management, l'entrepreneuriat et le leadership, avec une signature professionnalisante, internationale et connectée aux transformations des organisations.</p>
      <ul class="check-list">
        <li><strong>Une pédagogie par la décision :</strong> chaque séquence conduit à une production concrète — diagnostic, budget, feuille de route.</li>
        <li><strong>Des parcours qui se prolongent :</strong> du pilotage d'une activité à la responsabilité globale du dirigeant.</li>
        <li><strong>Une organisation compatible avec la vie active :</strong> présentiel, distanciel synchrone ou hybride.</li>
      </ul>
      <a class="link-arrow" href="formations.html">Comparer les formations {I["arrow"]}</a>
    </div>
    <div class="visual-panel reveal">
      <ul class="stats" style="grid-template-columns:repeat(2,1fr);width:100%">
        <li><strong>420 h</strong><span>Bachelor Management Stratégique &amp; Opérationnel</span></li>
        <li><strong>900 h</strong><span>Mastère sur 2 ans, M1 + M2</span></li>
        <li><strong>360 h</strong><span>Executive MBA + Executive Impact Project</span></li>
        <li><strong>20 h</strong><span>Formation courte IA, 5 séances</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--navy on-dark" aria-labelledby="filiere-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">La filière Management &amp; Leadership</p>
      <h2 id="filiere-title">Quatre niveaux de responsabilité, un même fil rouge</h2>
      <p class="lead">Chaque programme prépare à un palier de décision. Vous entrez au niveau qui correspond à votre parcours et à votre expérience.</p>
    </div>
    <ol class="pathway reveal">
      <li><span class="pathway__dot">Bac+3</span><div><span class="pathway__level">Bachelor</span><span class="pathway__role">Manager</span><p>Piloter une activité, une équipe et la performance opérationnelle.</p></div></li>
      <li><span class="pathway__dot">Bac+5</span><div><span class="pathway__level">Mastère · Niveau 7</span><span class="pathway__role">Strategic Leader</span><p>Concevoir et conduire la transformation d'une organisation.</p></div></li>
      <li><span class="pathway__dot">MBA</span><div><span class="pathway__level">MBA · Niveau 7</span><span class="pathway__role">Business Leader</span><p>Élargir sa maîtrise de la stratégie, de la finance et du développement.</p></div></li>
      <li><span class="pathway__dot">EMBA</span><div><span class="pathway__level">Executive MBA</span><span class="pathway__role">Executive Leader</span><p>Gouverner, arbitrer, transformer et assumer la responsabilité globale.</p></div></li>
    </ol>
  </div>
</section>

<section class="section" aria-labelledby="prog-title">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Nos formations</p>
      <h2 id="prog-title">Choisissez le programme qui correspond à votre trajectoire</h2>
    </div>
    <div class="grid grid--4">
      {CARDS["bachelor"]()}{CARDS["mastere"]()}{CARDS["emba"]()}{CARDS["ia"]()}
    </div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="peda-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="motto">Apprendre. Diriger. Transformer.</p>
      <h2 id="peda-title">Une pédagogie de grande école, orientée décision</h2>
      <p class="lead">Les situations professionnelles plutôt que l'accumulation de cours théoriques.</p>
    </div>
    <div class="grid grid--3">
      <article class="card reveal"><span class="icon-badge">{I["target"]}</span><h3>Apprendre en décidant</h3><p>Études de cas, business games et simulations de comité de direction : vous analysez, arbitrez et défendez vos choix.</p></article>
      <article class="card reveal"><span class="icon-badge icon-badge--blue">{I["briefcase"]}</span><h3>Produire des livrables réels</h3><p>Diagnostic, tableau de bord, budget, plan commercial, feuille de route : chaque séquence débouche sur une production exploitable.</p></article>
      <article class="card reveal"><span class="icon-badge icon-badge--green">{I["mic"]}</span><h3>Rencontrer ceux qui dirigent</h3><p>Conférences de dirigeants, entrepreneurs, consultants et experts, peer learning et coaching individuel.</p></article>
    </div>
    <ul class="chips mt-2 reveal" aria-label="Formats pédagogiques" style="justify-content:center">
      <li>Cas d'entreprise</li><li>Business games</li><li>Simulations managériales</li><li>Missions de conseil</li><li>Ateliers Excel &amp; KPI</li><li>Data &amp; IA appliquées</li><li>Grand Oral</li><li>Board Presentation</li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="mod-title">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Modalités</p>
      <h2 id="mod-title">Se former sans mettre sa vie professionnelle entre parenthèses</h2>
    </div>
    <div class="grid grid--3">
      <article class="card card--surface reveal"><span class="icon-badge">{I["building"]}</span><h3>Présentiel</h3><p>Cours, ateliers, études de cas, simulations, travaux de groupe, soutenances et accompagnement sur site.</p></article>
      <article class="card card--surface reveal"><span class="icon-badge icon-badge--blue">{I["monitor"]}</span><h3>Distanciel synchrone</h3><p>Classes virtuelles en direct, ressources numériques, travaux dirigés et activités collaboratives en ligne.</p></article>
      <article class="card card--surface reveal"><span class="icon-badge icon-badge--yellow">{I["layers"]}</span><h3>Hybride</h3><p>Une organisation combinant les deux modalités. Le calendrier et la répartition des séquences sont communiqués à chaque session.</p></article>
    </div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="adm-title">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Admissions</p>
      <h2 id="adm-title">Une admission sélective, un accompagnement personnalisé</h2>
    </div>
    <ol class="steps reveal">
      <li><h3>Dossier de candidature</h3><p>Parcours académique, expérience professionnelle et projet.</p></li>
      <li><h3>Étude du dossier</h3><p>Analyse de vos acquis et de la cohérence de votre projet.</p></li>
      <li><h3>Entretien</h3><p>Entretien de positionnement, ou entretien Executive pour l'EMBA.</p></li>
      <li><h3>Décision</h3><p>Décision de la commission d'admission et inscription.</p></li>
    </ol>
    <p class="mt-2"><a class="link-arrow" href="admissions.html">Conditions d'accès détaillées {I["arrow"]}</a></p>
  </div>
</section>

{cta_band("Votre prochaine responsabilité commence ici", "Échangez avec un conseiller pour identifier le programme adapté à votre niveau, votre expérience et votre ambition.")}
'''
page("index.html","Academy 21 University — Former ceux qui dirigeront demain",
     "Academy Twenty One University : Bachelor, Mastère, Executive MBA et formations courtes en management, entrepreneuriat et leadership.", home)

# =====================================================================
# FORMATIONS (catalogue)
# =====================================================================
def seg(name, opts):
    out=[]
    for i,(v,l) in enumerate(opts):
        chk=" checked" if i==0 else ""
        out.append(f'<input type="radio" id="{name}-{v}" name="{name}" value="{v}"{chk}><label for="{name}-{v}">{l}</label>')
    return "".join(out)

formations = f'''
<section class="page-hero page-hero--simple on-dark" aria-labelledby="page-title">
  {ring("deco", uid="ph")}
  <div class="container">
    <div>
      <nav class="breadcrumb" aria-label="Fil d'Ariane"><ol><li><a href="index.html">Accueil</a></li><li><span aria-current="page">Formations</span></li></ol></nav>
      <h1 id="page-title">Nos formations</h1>
      <p class="lead">Du pilotage d'une activité à la responsabilité globale du dirigeant : quatre programmes pour progresser à chaque étape de votre trajectoire.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0" aria-labelledby="cat-title">
  <div class="container">
    <h2 id="cat-title" class="visually-hidden">Catalogue filtrable</h2>
    <form class="filters" data-filters style="margin-top:-3rem;position:relative" aria-label="Filtrer les formations">
      <fieldset><legend>Niveau</legend><div class="seg">{seg("niveau",[("all","Tous"),("bac3","Bac+3"),("bac5","Bac+5"),("executive","Executive"),("courte","Formation courte")])}</div></fieldset>
      <fieldset><legend>Modalité</legend><div class="seg">{seg("modalite",[("all","Toutes"),("presentiel","Présentiel"),("distanciel","Distanciel"),("hybride","Hybride")])}</div></fieldset>
    </form>
    <p class="results-count" id="results-count" role="status" aria-live="polite"></p>
    <div class="grid grid--2">
      {CARDS["bachelor"]()}{CARDS["mastere"]()}{CARDS["emba"]()}{CARDS["ia"]()}
    </div>
  </div>
</section>
<section class="section section--surface" aria-labelledby="cmp-title">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Comparatif</p>
      <h2 id="cmp-title">Quel programme pour quel profil ?</h2>
    </div>
    {table("Comparatif des formations Academy 21 University",
      ["Formation","Niveau","Durée / volume","Public &amp; accès","Reconnaissance"],
      [["<a href='bachelor.html'>Bachelor Management Stratégique &amp; Opérationnel</a>","Bac+3 · Niveau 6","420 h","Bac+2, ou 5 ans d'expérience significative","Prépare au Titre professionnel RNCP38666"],
       ["<a href='mastere.html'>Mastère Stratégie, Leadership &amp; Transformation</a>","Bac+5 · Niveau 7","2 ans · 900 h","Bac+3, ou Bac+2 + 3 ans en management","Conçu en cohérence avec le RNCP39994*"],
       ["<a href='executive-mba.html'>Executive MBA Gouvernance, Leadership &amp; Transformation</a>","Executive","12 mois · 360 h + projet","Dirigeants, 7 ans d'expérience minimum","Diplôme d'établissement"],
       ["<a href='ia-marketing-reseau.html'>IA appliquée au Marketing de Réseau</a>","Formation courte","20 h · 5 séances","Professionnels du marketing de réseau","Attestation de formation"]], vol_col=None)}
    <p class="small text-muted mt-2">* La présentation effective à la certification suppose le cadre conventionnel et l'inscription auprès du certificateur.</p>
  </div>
</section>
{cta_band("Vous hésitez entre deux programmes ?", "Un entretien d'orientation gratuit permet de valider votre niveau d'entrée et le format le plus adapté.")}
'''
page("formations.html","Formations — Academy 21 University","Catalogue des formations Academy 21 University : Bachelor, Mastère, Executive MBA, formation IA.", formations)

# =====================================================================
# BACHELOR
# =====================================================================
bach_rows = [
 ["Stratégie, veille &amp; diagnostic d'activité","35 h","Marché, concurrence, tendances, zone de chalandise, diagnostic stratégique, RSE et orientations de développement."],
 ["Marketing &amp; développement commercial","35 h","Segmentation, positionnement, offre, prix, plan d'action commercial, fidélisation, omnicanalité."],
 ["Achats, stocks &amp; chaîne d'approvisionnement","42 h","Prévisions, commandes, fournisseurs, stocks, inventaires, rotation, démarque, continuité des flux."],
 ["Expérience client &amp; performance commerciale","35 h","Parcours client, qualité de service, merchandising, opérations commerciales, accessibilité, réclamations."],
 ["Finance &amp; pilotage de la rentabilité","49 h","CA, marges, charges, budgets, seuil de rentabilité, prévisionnels, tableaux de bord, analyse des écarts."],
 ["Leadership &amp; management opérationnel","42 h","Organisation, objectifs, délégation, animation, motivation, cohésion, gestion des situations sensibles."],
 ["Ressources humaines &amp; droit social","35 h","Recrutement, intégration, plannings, entretiens, compétences, réglementation, inclusion et handicap."],
 ["Management de projet &amp; conduite du changement","35 h","Cadrage, planification, ressources, risques, gouvernance, communication et mobilisation des équipes."],
 ["Digital, data &amp; intelligence artificielle","28 h","CRM, e-commerce, data, KPI digitaux, IA générative, automatisation, RGPD et aide à la décision."],
 ["Communication professionnelle &amp; négociation","28 h","Réunions, reporting, présentation de résultats, argumentation, négociation, communication managériale."],
 ["Management responsable, qualité &amp; prévention","21 h","RSE, sécurité, prévention, qualité, éthique, accessibilité et amélioration continue."],
 ["Projet professionnel &amp; préparation certification","35 h","Dossier professionnel, études de cas, productions, soutenances, simulations et préparation au jury."],
]
bachelor = f'''
<section class="page-hero on-dark" aria-labelledby="page-title">
  {ring("deco", uid="ph")}
  <div class="container">
    <div>
      {crumbs("Bachelor")}
      <span class="kicker">Bachelor · Bac+3</span>
      <h1 id="page-title">Management Stratégique &amp; Opérationnel</h1>
      <p class="subtitle">Piloter la performance • Développer l'activité • Manager les équipes</p>
      <p class="lead">Une formation pour devenir manager d'un centre de profit : prendre la responsabilité d'une activité commerciale, en développer la performance et animer les équipes qui la font vivre.</p>
    </div>
    {facts([("Niveau de sortie","Bac+3 — Niveau 6"),("Durée","420 h de formation"),("Certification","Titre professionnel — RNCP38666"),("Modalités","Présentiel • Distanciel • Hybride"),("Admission","Bac+2, ou 5 ans d'expérience significative")],"bachelor")}
  </div>
</section>
{subnav([("apercu","Aperçu"),("admission","Admission"),("dimensions","Les 4 dimensions"),("programme","Programme"),("competences","Compétences"),("certification","Certification"),("debouches","Débouchés")])}
<div class="section">
  <div class="container layout-aside">
    <div>
      <section class="content-block" id="apercu" aria-labelledby="t-apercu">
        <p class="eyebrow">Aperçu</p>
        <h2 id="t-apercu">Vision stratégique et maîtrise du terrain</h2>
        <p>Le parcours associe commerce, finance, management, ressources humaines, expérience client, approvisionnements, digital et conduite de projet.</p>
        <p>Au-delà des connaissances de gestion, la formation place l'apprenant dans une <strong>posture de décideur</strong> : analyser une situation, fixer des priorités, construire des prévisionnels, arbitrer, mobiliser une équipe, suivre les résultats et mettre en œuvre les actions correctives nécessaires.</p>
        <div class="grid grid--2 mt-2">
          <div class="card card--surface"><span class="icon-badge">{I["building"]}</span><h3>Présentiel</h3><p>Cours, ateliers, études de cas, simulations managériales, travaux en groupe, soutenances et accompagnement pédagogique sur site.</p></div>
          <div class="card card--surface"><span class="icon-badge icon-badge--blue">{I["monitor"]}</span><h3>Distanciel</h3><p>Classes virtuelles synchrones, ressources numériques, travaux dirigés à distance, accompagnement et activités collaboratives en ligne.</p></div>
        </div>
        <p class="small text-muted mt-2">Le parcours peut être suivi en présentiel, en distanciel ou selon une organisation hybride. Le calendrier et la répartition des séquences sont communiqués à chaque session.</p>
      </section>

      <section class="content-block" id="admission" aria-labelledby="t-admission">
        <p class="eyebrow">Conditions d'accès</p>
        <h2 id="t-admission">Deux voies d'accès</h2>
        <p>L'admission est prononcée après étude du dossier et entretien de positionnement, pour tenir compte aussi bien du parcours académique que de l'expérience professionnelle.</p>
        <div class="grid grid--2">
          <div class="card"><span class="icon-badge">{I["award"]}</span><h3>Accès sur diplôme</h3><p>Être titulaire d'un diplôme ou titre de niveau 5 (Bac+2) ou justifier d'un niveau de formation jugé compatible avec les exigences du parcours.</p><p class="small text-muted">Admission soumise à l'examen du dossier et à un entretien évaluant le projet professionnel, les acquis et la capacité à suivre une formation de niveau 6.</p></div>
          <div class="card"><span class="icon-badge icon-badge--yellow">{I["briefcase"]}</span><h3>Accès sur expérience</h3><p>Justifier d'au moins 5 années d'expérience professionnelle significative, prioritairement dans le commerce, la vente, le management, la gestion d'activité, l'entrepreneuriat ou la conduite d'équipe/projet.</p><p class="small text-muted">Expérience appréciée de façon individualisée lors de l'étude du dossier et de l'entretien.</p></div>
        </div>
        <div class="mt-2">{notice("<p><strong>Important :</strong> la condition de 5 années d'expérience est une condition d'admission définie par Academy 21 University pour les candidats ne disposant pas du niveau académique attendu ; elle ne constitue pas une exigence réglementaire propre au RNCP38666.</p>")}</div>
      </section>

      <section class="content-block" id="dimensions" aria-labelledby="t-dim">
        <p class="eyebrow">Architecture</p>
        <h2 id="t-dim">Les 4 dimensions du Bachelor</h2>
        <div class="grid grid--2">
          <article class="card"><span class="num">01</span><h3>Stratégie &amp; Développement</h3><p>Comprendre son marché, analyser la concurrence, contribuer aux orientations stratégiques, construire un plan de développement et transformer une ambition en plan d'action.</p></article>
          <article class="card"><span class="num">02</span><h3>Performance &amp; Pilotage</h3><p>Maîtriser les indicateurs économiques, construire budgets et prévisionnels, suivre marges et rentabilité, analyser les écarts et décider des actions correctives.</p></article>
          <article class="card"><span class="num">03</span><h3>Commerce &amp; Expérience client</h3><p>Piloter l'offre, les approvisionnements et l'activité commerciale, améliorer le parcours client, développer l'omnicanalité et renforcer la fidélisation.</p></article>
          <article class="card"><span class="num">04</span><h3>Leadership &amp; Management</h3><p>Recruter, intégrer, organiser l'activité, développer les compétences, animer les équipes, conduire les projets et créer une performance collective durable.</p></article>
        </div>
      </section>

      <section class="content-block" id="programme" aria-labelledby="t-prog">
        <p class="eyebrow">Programme</p>
        <h2 id="t-prog">420 heures d'enseignements</h2>
        {table("Programme du Bachelor — 420 heures",["Enseignement","Volume","Contenu"],bach_rows,["Total","420 h",""])}
      </section>

      <section class="content-block" id="competences" aria-labelledby="t-comp">
        <p class="eyebrow">Compétences</p>
        <h2 id="t-comp">Des compétences directement mobilisables</h2>
        <ul class="check-list">
          <li>Piloter l'activité commerciale et sécuriser les approvisionnements.</li>
          <li>Construire et faire évoluer une offre adaptée au marché et aux attentes clients.</li>
          <li>Concevoir une expérience client performante, inclusive et fidélisante.</li>
          <li>Contribuer aux orientations stratégiques et les traduire en actions opérationnelles.</li>
          <li>Élaborer et présenter budgets, prévisionnels et tableaux de bord.</li>
          <li>Analyser la performance économique et décider des actions correctives.</li>
          <li>Piloter le recrutement, l'intégration et le développement des collaborateurs.</li>
          <li>Organiser le travail, manager la performance et renforcer la cohésion des équipes.</li>
          <li>Conduire des projets et mobiliser les équipes autour du changement.</li>
        </ul>
        <h3>Une pédagogie professionnalisante</h3>
        <p>Chaque séquence conduit à une production : diagnostic, tableau de bord, budget, plan commercial, planning, dossier de recrutement, analyse de performance, support de réunion, plan d'action ou projet de transformation.</p>
        <ul class="chips" aria-label="Formats pédagogiques"><li>Cas d'entreprise</li><li>Business games</li><li>Simulations managériales</li><li>Ateliers Excel &amp; KPI</li><li>Jeux de rôle</li><li>Projet fil rouge</li><li>Soutenances professionnelles</li></ul>
      </section>

      <section class="content-block" id="certification" aria-labelledby="t-cert">
        <p class="eyebrow">Certification professionnelle préparée</p>
        <h2 id="t-cert">Titre professionnel Responsable d'établissement marchand</h2>
        <p>Le parcours prépare à l'ensemble des compétences du Titre professionnel <strong>Responsable d'établissement marchand</strong>, enregistré au RNCP sous le numéro <strong>RNCP38666</strong>, certification de niveau 6 délivrée par le ministère chargé de l'Emploi. Le niveau 6 correspond au niveau communément présenté comme Bac+3 / Bac+4 ; Academy 21 University positionne ce parcours comme un Bachelor Bac+3.</p>
        <ul class="bloc-list">
          <li><b>BLOC 1</b><span><strong>Activité commerciale</strong>Approvisionnements, offre et expérience client</span></li>
          <li><b>BLOC 2</b><span><strong>Orientations stratégiques</strong>Prévisionnels et performance économique</span></li>
          <li><b>BLOC 3</b><span><strong>Management</strong>Recrutement, intégration, management des équipes et conduite de projets</span></li>
        </ul>
        <h3 class="mt-2">Évaluation &amp; préparation au jury</h3>
        <p>L'évaluation est progressive : études de cas, travaux chiffrés, mises en situation, projets et soutenances. La préparation finale reproduit les exigences de la certification : étude de cas sur poste informatique, présentation et argumentation des travaux, productions professionnelles, puis entraînement à l'entretien final.</p>
        {notice("<p>Une période en entreprise d'au moins <strong>350 heures</strong> est requise pour le candidat présenté au titre après un parcours de formation ; pour l'alternant, cette période est intégrée au temps de travail en entreprise.</p>","info")}
      </section>

      <section class="content-block" id="debouches" aria-labelledby="t-deb">
        <p class="eyebrow">Débouchés</p>
        <h2 id="t-deb">Les métiers visés</h2>
        <ul class="chips"><li>Manager de centre de profit</li><li>Responsable de point de vente</li><li>Responsable de boutique</li><li>Responsable de département</li><li>Responsable commercial</li><li>Responsable e-commerce</li><li>Directeur adjoint</li><li>Directeur de magasin</li><li>Responsable de succursale</li><li>Entrepreneur / gestionnaire d'activité</li></ul>
        <p class="mt-2">Et après ? Poursuivez avec le <a href="mastere.html">Mastère Stratégie, Leadership &amp; Transformation des Organisations</a> pour passer du pilotage d'une activité à la conduite d'une transformation.</p>
        <div class="mt-2">{notice("<p>Parcours préparant au Titre professionnel Responsable d'établissement marchand — RNCP38666 — niveau 6. En partenariat avec <strong>GREEN UP ACADEMY</strong>, partenaire habilité pour la préparation et la présentation à la certification.</p>")}</div>
      </section>
    </div>
    {aside("bachelor","Bachelor")}
  </div>
</div>
{cta_band("Devenez manager d'un centre de profit", "Admission sur dossier et entretien de positionnement. Parlons de votre projet.", "bachelor")}
'''
page("bachelor.html","Bachelor Management Stratégique & Opérationnel (Bac+3) — Academy 21 University",
     "Bachelor Bac+3 niveau 6 préparant au Titre professionnel RNCP38666 : piloter la performance, développer l'activité, manager les équipes.", bachelor)

# =====================================================================
# MASTÈRE
# =====================================================================
m1=[["Diagnostic stratégique &amp; intelligence économique","50 h"],["Économie, prospective &amp; géopolitique des affaires","35 h"],["Finance d'entreprise &amp; analyse de la performance","55 h"],["Stratégie marketing, développement &amp; expérience client","40 h"],["Management des organisations &amp; design organisationnel","40 h"],["Gestion de projet complexe &amp; méthodes agiles","45 h"],["Leadership, communication &amp; négociation","40 h"],["Transformation digitale, data &amp; intelligence artificielle","45 h"],["Droit des affaires, risques &amp; conformité","30 h"],["Méthodes de recherche &amp; Consulting Project I","40 h"]]
m2=[["Corporate strategy &amp; scénarios de transformation","50 h"],["Pilotage financier, création de valeur &amp; contrôle stratégique","50 h"],["Conduite du changement &amp; sociologie des organisations","45 h"],["Leadership exécutif, gouvernance &amp; prise de décision","45 h"],["Capital humain, compétences &amp; transformation RH","40 h"],["Innovation, entrepreneuriat &amp; nouveaux business models","40 h"],["RSE, transition écologique &amp; performance globale","35 h"],["International business &amp; management interculturel","35 h"],["IA stratégique, automatisation &amp; transformation des métiers","35 h"],["Conseil en organisation &amp; mission de transformation","45 h"],["Mémoire / Consulting Project II &amp; Grand Oral","60 h"]]
dims=[("Stratégie","Diagnostic, prospective, modèles économiques, choix stratégiques et gouvernance.",I["compass"],""),
      ("Transformation","Conduite du changement, transformation digitale, IA, innovation et nouveaux modèles.",I["refresh"],"icon-badge--blue"),
      ("Performance","Finance, contrôle, création de valeur, KPI, performance économique, sociale et RSE.",I["chart"],"icon-badge--yellow"),
      ("Leadership","Posture de dirigeant, négociation, influence, décision, management et conflits.",I["leader"],""),
      ("Capital humain","Compétences, organisation du travail, talents, inclusion, QVCT et culture.",I["users"],"icon-badge--blue"),
      ("Impact","Responsabilité, transition écologique, parties prenantes, éthique et pérennité.",I["globe"],"icon-badge--green")]
dimcards="".join(f'<article class="card"><span class="icon-badge {c}">{ico}</span><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></article>' for i,(t,d,ico,c) in enumerate(dims))
mastere = f'''
<section class="page-hero on-dark" aria-labelledby="page-title">
  {ring("deco","#2f86ab","#a7dd63","ph")}
  <div class="container">
    <div>
      {crumbs("Mastère")}
      <span class="kicker">Mastère · Bac+5 · Niveau 7</span>
      <h1 id="page-title">Stratégie, Leadership &amp; Transformation des Organisations</h1>
      <p class="subtitle">Former les décideurs capables de penser la stratégie, conduire le changement et transformer durablement les organisations.</p>
      <p class="motto" style="color:var(--logo-yellow)">Apprendre. Diriger. Transformer.</p>
    </div>
    {facts([("Niveau de sortie","Bac+5 • Niveau 7"),("Durée","2 ans • M1 + M2"),("Volume indicatif","900 h"),("Modalités","Présentiel • Distanciel • Hybride"),("Rythme","Initial • Formation continue • Alternance selon convention"),("Référentiel","RNCP39994 • Manager des transformations des organisations*")],"mastere")}
  </div>
</section>
{subnav([("apercu","Aperçu"),("dimensions","Les 6 dimensions"),("admission","Admission"),("programme","Programme"),("rncp","Référentiel RNCP"),("pedagogie","Pédagogie"),("debouches","Débouchés")])}
<div class="section">
  <div class="container layout-aside">
    <div>
      <section class="content-block" id="apercu" aria-labelledby="t-apercu">
        <p class="eyebrow">Aperçu</p>
        <h2 id="t-apercu">Un Mastère pour prendre des responsabilités de direction</h2>
        <p>Dans la continuité du <a href="bachelor.html">Bachelor Management Stratégique &amp; Opérationnel</a>, ce Mastère prépare des profils capables de passer du pilotage d'une activité à la conduite globale d'une transformation.</p>
        <p>Le programme vise une posture de cadre, manager senior, consultant ou dirigeant : analyser une organisation et son environnement, formuler des orientations stratégiques, conduire des projets complexes, mobiliser les équipes, piloter la performance économique et sociale.</p>
        <p class="quote">« Le leadership constitue la signature du parcours : décider dans l'incertitude, donner du sens, créer l'adhésion, arbitrer, développer les compétences et assumer la responsabilité des résultats. »</p>
      </section>

      <section class="content-block" id="dimensions" aria-labelledby="t-dim">
        <p class="eyebrow">Architecture</p>
        <h2 id="t-dim">Les 6 dimensions du programme</h2>
        <div class="grid grid--3">{dimcards}</div>
      </section>

      <section class="content-block" id="admission" aria-labelledby="t-adm">
        <p class="eyebrow">Conditions d'accès</p>
        <h2 id="t-adm">Trois voies d'admission</h2>
        <ul class="bloc-list">
          <li><b>ENTRÉE EN M1</b><span><strong>Niveau 6 (Bac+3) ou équivalent</strong>Admission sur dossier, entretien et validation du projet professionnel.</span></li>
          <li><b>DÉROGATOIRE</b><span><strong>Niveau 5 (Bac+2) + 3 ans en management</strong>Au moins 3 années d'expérience sur des fonctions managériales, conformément au prérequis dérogatoire du RNCP de référence.</span></li>
          <li><b>ENTRÉE EN M2</b><span><strong>Entrée directe</strong>Étude individualisée des acquis académiques et professionnels et décision de la commission d'admission.</span></li>
        </ul>
      </section>

      <section class="content-block" id="programme" aria-labelledby="t-prog">
        <p class="eyebrow">Architecture pédagogique</p>
        <h2 id="t-prog">900 heures sur deux ans</h2>
        <p>Le M1 consolide les fondamentaux du management stratégique et prépare au pilotage des transformations. Le M2 place l'apprenant dans une posture de décision, de direction et de conseil.</p>
        <div data-tabs>
          <div class="tabs__list" role="tablist" aria-label="Années du Mastère">
            <button class="tabs__tab" role="tab" id="tab-m1" aria-controls="panel-m1" aria-selected="true">M1 · 420 h</button>
            <button class="tabs__tab" role="tab" id="tab-m2" aria-controls="panel-m2" aria-selected="false" tabindex="-1">M2 · 480 h</button>
          </div>
          <div class="tabs__panel" role="tabpanel" id="panel-m1" aria-labelledby="tab-m1" tabindex="0">
            {table("M1 — Construire la vision et maîtriser les leviers de pilotage",["Enseignement","Volume"],m1,["Total M1","420 h"])}
          </div>
          <div class="tabs__panel" role="tabpanel" id="panel-m2" aria-labelledby="tab-m2" tabindex="0" hidden>
            {table("M2 — Diriger la transformation et créer de la valeur durable",["Enseignement","Volume"],m2,["Total M2","480 h"])}
          </div>
        </div>
      </section>

      <section class="content-block" id="rncp" aria-labelledby="t-rncp">
        <p class="eyebrow">Alignement RNCP niveau 7</p>
        <h2 id="t-rncp">Les 4 blocs du RNCP39994</h2>
        <p>Le programme couvre les quatre blocs du RNCP39994 « Manager des transformations des organisations » : stratégie, conduite du changement, démarche compétences et performance économique et sociale.</p>
        <ul class="bloc-list">
          <li><b>RNCP39994BC01</b><span><strong>Orienter la stratégie de l'entreprise</strong>Diagnostic • orientations stratégiques • risques • actions de transformation</span></li>
          <li><b>RNCP39994BC02</b><span><strong>Conduire le changement</strong>Ressources • planification • projet • mobilisation • leadership • tensions</span></li>
          <li><b>RNCP39994BC03</b><span><strong>Piloter la démarche compétences</strong>Diagnostic compétences • métiers • talents • RH • inclusion</span></li>
          <li><b>RNCP39994BC04</b><span><strong>Piloter la performance économique et sociale</strong>Finance • KPI • client • RSE • veille • amélioration continue</span></li>
        </ul>
      </section>

      <section class="content-block" id="pedagogie" aria-labelledby="t-peda">
        <p class="eyebrow">Pédagogie</p>
        <h2 id="t-peda">Une pédagogie de grande école, orientée décision</h2>
        <ul class="check-list">
          <li>Études de cas stratégiques et cas réels d'entreprise.</li>
          <li>Business games et simulations de comité de direction.</li>
          <li>Missions de conseil et projets de transformation.</li>
          <li>Conférences de dirigeants, entrepreneurs, consultants et experts.</li>
          <li>Recherche appliquée, veille et prospective.</li>
          <li>Data et intelligence artificielle appliquées au management.</li>
          <li>Grand Oral de leadership et soutenance d'un mémoire / consulting project.</li>
        </ul>
        <div class="grid grid--2">
          <div class="card card--surface"><h3>Évaluation</h3><p>Études de cas, mises en situation professionnelles, rapports d'activité, productions de conseil, présentations orales et soutenances. L'évaluation privilégie la capacité à analyser, décider, argumenter et mettre en œuvre.</p></div>
          <div class="card card--surface"><h3>Expérience professionnelle</h3><p>Le parcours s'articule à une expérience significative : alternance lorsque le cadre conventionnel le permet, stage long, mission professionnelle ou activité salariée compatible.</p></div>
        </div>
      </section>

      <section class="content-block" id="debouches" aria-labelledby="t-deb">
        <p class="eyebrow">Débouchés &amp; trajectoires</p>
        <h2 id="t-deb">Quatre trajectoires</h2>
        <div class="grid grid--2">
          <article class="card"><span class="icon-badge">{I["building"]}</span><h3>Direction</h3><p>Directeur d'unité • Directeur de BU • Directeur adjoint • Responsable transformation</p></article>
          <article class="card"><span class="icon-badge icon-badge--blue">{I["chart"]}</span><h3>Management</h3><p>Manager d'activité • Manager de projet • Responsable performance • Responsable développement</p></article>
          <article class="card"><span class="icon-badge icon-badge--yellow">{I["bulb"]}</span><h3>Conseil</h3><p>Consultant en management • Consultant en organisation • Consultant transformation</p></article>
          <article class="card"><span class="icon-badge icon-badge--green">{I["spark"]}</span><h3>Entrepreneuriat</h3><p>Créateur / repreneur d'entreprise • Entrepreneur • Développeur de nouveaux projets</p></article>
        </div>
        <div class="mt-2">{notice("<p><strong>Note réglementaire.</strong> RNCP39994 « Manager des transformations des organisations », niveau 7, certificateur IRUP, échéance d'enregistrement au 18/12/2027. Le référentiel prévoit un accès avec un niveau 6 ou, par dérogation, un niveau 5 assorti d'au moins trois années d'expérience sur des fonctions managériales. L'obtention de la certification suppose la validation des quatre blocs et l'inscription auprès du certificateur.</p><p>* Programme pédagogique conçu en cohérence avec le RNCP39994 ; il ne vaut pas, à lui seul, habilitation du certificateur.</p>")}</div>
      </section>
    </div>
    {aside("mastere","Mastère")}
  </div>
</div>
{cta_band("Prenez la direction de la transformation", "Entrée en M1 ou directement en M2 selon votre parcours : la commission étudie chaque dossier individuellement.", "mastere")}
'''
page("mastere.html","Mastère Stratégie, Leadership & Transformation des Organisations (Bac+5) — Academy 21 University",
     "Mastère Bac+5 niveau 7 en 2 ans, 900 h, conçu en cohérence avec le RNCP39994 Manager des transformations des organisations.", mastere)

# =====================================================================
# EXECUTIVE MBA
# =====================================================================
emba_rows=[["Strategic Foresight &amp; CEO Agenda","30 h","Prospective, signaux faibles, scénarios, vision, agenda stratégique du dirigeant."],
 ["Corporate Strategy &amp; Business Portfolio","35 h","Stratégie corporate, portefeuille, avantage concurrentiel, diversification, alliances."],
 ["Finance, Capital Allocation &amp; Value Creation","35 h","Cash, rentabilité, valorisation, financement, allocation du capital, décisions d'investissement."],
 ["Corporate Governance &amp; Board Dynamics","25 h","Gouvernance, conseil, délégation, contrôle, parties prenantes, responsabilité du dirigeant."],
 ["Executive Leadership &amp; Power","35 h","Pouvoir, influence, autorité, décision, conflits, courage managérial et posture."],
 ["People, Culture &amp; Succession","25 h","Culture, équipe dirigeante, talents clés, succession, transformation managériale."],
 ["Transformation, AI &amp; Digital Strategy","35 h","IA, digital, automatisation, data, transformation des métiers et gouvernance technologique."],
 ["Growth, International &amp; Strategic Partnerships","30 h","Croissance, internationalisation, alliances, négociation et développement d'écosystèmes."],
 ["Crisis, Risk &amp; Reputation","25 h","Risques, crise, continuité, communication sensible, réputation et décision sous pression."],
 ["Sustainable Business &amp; Impact","20 h","ESG, transition, impact, modèle responsable et création de valeur durable."],
 ["Executive Negotiation &amp; Public Leadership","20 h","Négociation de haut niveau, communication de dirigeant, influence institutionnelle."],
 ["Executive Impact Project &amp; Board Presentation","45 h","Problématique réelle, diagnostic, arbitrages, feuille de route et présentation devant un Board."]]
resp=[("Donner le cap","Vision, prospective, stratégie, gouvernance et priorités.",I["compass"]),("Arbitrer","Finance, capital, risques, portefeuille d'investissements et création de valeur.",I["scale"]),
      ("Mobiliser","Leadership, culture, influence, talent, succession et engagement.",I["users"]),("Transformer","Innovation, changement, IA, digital, nouveaux modèles et organisation.",I["refresh"]),
      ("Développer","Croissance, alliances, international, réputation et écosystèmes.",I["globe"]),("Assumer","Éthique, responsabilité, crise, parties prenantes et impact.",I["shield"])]
respcards="".join(f'<article class="card card--navy"><span class="icon-badge icon-badge--navy">{ico}</span><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></article>' for i,(t,d,ico) in enumerate(resp))
emba = f'''
<section class="page-hero on-dark" aria-labelledby="page-title">
  {ring("deco","#fccd01","#da0612","ph")}
  <div class="container">
    <div>
      {crumbs("Executive MBA")}
      <span class="kicker">Executive MBA · Executive Education</span>
      <h1 id="page-title">Gouvernance, Leadership &amp; Transformation</h1>
      <p class="subtitle">Le programme de haute direction d'Academy Twenty One University.</p>
      <p class="motto" style="color:var(--logo-yellow)">Think. Decide. Lead. Transform.</p>
    </div>
    {facts([("Positionnement","Programme Executive de haute direction"),("Public","Dirigeants • Entrepreneurs • Cadres supérieurs • Membres de CODIR"),("Durée","12 mois"),("Volume indicatif","360 h + Executive Impact Project"),("Organisation","Blocs intensifs • Week-ends Executive • Séminaires"),("Modalités","Présentiel • Distanciel synchrone • Hybride"),("Expérience","7 ans minimum, dont responsabilités managériales significatives")],"executive-mba")}
  </div>
</section>
{subnav([("apercu","Aperçu"),("public","Public &amp; admission"),("responsabilites","Les 6 responsabilités"),("programme","Programme"),("experience","Expérience Executive"),("organisation","Organisation"),("certification","Reconnaissance")])}
<div class="section">
  <div class="container layout-aside">
    <div>
      <section class="content-block" id="apercu" aria-labelledby="t-apercu">
        <p class="eyebrow eyebrow--gold">Le programme de ceux qui portent la responsabilité finale</p>
        <h2 id="t-apercu">Prendre de la hauteur, arbitrer, assumer</h2>
        <p>L'Executive MBA est conçu pour des professionnels qui ne découvrent plus le management : ils l'exercent déjà. Leur enjeu est de prendre de la hauteur, arbitrer entre des intérêts contradictoires, engager des ressources, conduire des transformations et assumer la responsabilité globale de la décision.</p>
        <p>Programme le plus senior de la filière Management &amp; Leadership, il concentre l'apprentissage sur les questions auxquelles un dirigeant est réellement confronté :</p>
        <p class="quote">« Où aller, pourquoi, avec quelles ressources, avec quelles équipes, à quel risque, et comment créer durablement de la valeur ? »</p>
      </section>

      <section class="content-block" id="public" aria-labelledby="t-public">
        <p class="eyebrow">Public</p>
        <h2 id="t-public">À qui s'adresse l'Executive MBA ?</h2>
        <div class="grid grid--2">
          <article class="card"><span class="icon-badge">{I["leader"]}</span><h3>Dirigeants</h3><p>Présidents, directeurs généraux, directeurs adjoints, dirigeants de PME/ETI, responsables de filiales ou d'unités.</p></article>
          <article class="card"><span class="icon-badge icon-badge--blue">{I["briefcase"]}</span><h3>Cadres supérieurs</h3><p>Membres ou futurs membres de comités de direction souhaitant passer d'une expertise fonctionnelle à une vision globale.</p></article>
          <article class="card"><span class="icon-badge icon-badge--yellow">{I["spark"]}</span><h3>Entrepreneurs</h3><p>Fondateurs et repreneurs confrontés aux enjeux de structuration, gouvernance, croissance, financement et changement d'échelle.</p></article>
          <article class="card"><span class="icon-badge icon-badge--green">{I["users"]}</span><h3>Leaders d'organisations</h3><p>Responsables de réseaux, institutions ou communautés ayant une responsabilité importante de mobilisation, de développement et de gouvernance.</p></article>
        </div>
        <h3 class="mt-2">Admission sélective</h3>
        <p>Le programme privilégie les candidats justifiant d'au moins <strong>7 années d'expérience professionnelle</strong>, dont une expérience significative de management, de direction, d'entrepreneuriat ou de pilotage d'une activité. Admission sur dossier, <strong>entretien Executive</strong> et appréciation de la maturité du projet professionnel.</p>
        <p>Le niveau académique attendu est généralement Bac+4/Bac+5 ou équivalent. Des profils au parcours académique différent peuvent être étudiés lorsque l'expérience, le niveau de responsabilité et les acquis professionnels le justifient.</p>
      </section>
    </div>
    {aside("executive-mba","Executive MBA")}
  </div>
</div>
<section class="section section--navy on-dark" id="responsabilites" aria-labelledby="t-resp">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Architecture du leadership</p>
      <h2 id="t-resp">Les 6 responsabilités du dirigeant</h2>
    </div>
    <div class="grid grid--3">{respcards}</div>
  </div>
</section>
<div class="section">
  <div class="container" style="max-width:960px">
    <section class="content-block" id="programme" aria-labelledby="t-prog">
      <p class="eyebrow">Architecture du programme</p>
      <h2 id="t-prog">360 heures de séminaires de haute intensité</h2>
      <p>Chaque module part d'une problématique de direction et conduit à une décision, un arbitrage ou une feuille de route. Les apports conceptuels sont systématiquement confrontés aux situations réelles des participants.</p>
      {table("Modules de l'Executive MBA",["Module","Vol.","Focus Executive"],emba_rows,["Total","360 h",""])}
    </section>

    <section class="content-block" id="experience" aria-labelledby="t-exp">
      <p class="eyebrow">Pédagogie</p>
      <h2 id="t-exp">Une expérience Executive, pas une scolarité classique</h2>
      <div class="grid grid--2">
        <div class="card card--surface"><h3>Executive Case Method</h3><p>Analyse de situations complexes et défense d'une décision devant les pairs.</p></div>
        <div class="card card--surface"><h3>Boardroom Simulations</h3><p>Conseil d'administration, comité de direction, crise, investissement et transformation.</p></div>
        <div class="card card--surface"><h3>CEO &amp; Leaders Series</h3><p>Rencontres avec dirigeants, entrepreneurs, investisseurs, experts et personnalités qualifiées.</p></div>
        <div class="card card--surface"><h3>Peer Learning</h3><p>Capitalisation structurée sur l'expérience professionnelle des participants.</p></div>
        <div class="card card--surface"><h3>Executive Coaching</h3><p>Travail individuel sur la posture, les priorités, les angles morts et la trajectoire de leadership.</p></div>
        <div class="card card--surface"><h3>International &amp; Strategic Immersion</h3><p>Séminaire ou étude comparative d'écosystèmes économiques et managériaux.</p></div>
      </div>
      <div class="split mt-2" style="align-items:start">
        <div>
          <h3>Executive Impact Project</h3>
          <p>Chaque participant travaille sur une problématique stratégique liée à son entreprise, son organisation ou son projet entrepreneurial. Pas un mémoire théorique, mais un <strong>document de direction exploitable</strong> : diagnostic, options, scénarios, arbitrages, impacts financiers et humains, risques, gouvernance et plan de mise en œuvre.</p>
          <p>Le programme se conclut par une <strong>Board Presentation</strong> : le participant défend son projet comme devant un conseil d'administration, des investisseurs ou un comité exécutif.</p>
        </div>
        <div>
          <h3>Évaluation</h3>
          <p>L'évaluation porte sur la qualité du raisonnement stratégique, la capacité d'arbitrage, la pertinence des recommandations, la maîtrise des données financières et opérationnelles, la posture de leadership et la capacité à défendre une décision.</p>
          <ul class="chips" aria-label="Productions évaluées"><li>Notes de décision</li><li>Board papers</li><li>Analyses stratégiques</li><li>Simulations</li><li>Soutenance finale</li></ul>
        </div>
      </div>
    </section>

    <section class="content-block" id="organisation" aria-labelledby="t-org">
      <p class="eyebrow">Organisation</p>
      <h2 id="t-org">Compatible avec la vie d'un dirigeant</h2>
      <ul class="bloc-list">
        <li><b>FORMAT</b><span>12 mois, avec possibilité d'aménagement selon la cohorte.</span></li>
        <li><b>RYTHME</b><span>Blocs Executive concentrés, week-ends et séminaires périodiques.</span></li>
        <li><b>PRÉSENTIEL</b><span>Séminaires, simulations, rencontres, coaching et Board sessions.</span></li>
        <li><b>DISTANCIEL</b><span>Classes synchrones, conférences, coaching et travaux de groupe.</span></li>
        <li><b>INTERSESSION</b><span>Lectures, diagnostics, travaux appliqués et avancement de l'Executive Impact Project.</span></li>
      </ul>
    </section>

    <section class="content-block" id="certification" aria-labelledby="t-cert">
      <p class="eyebrow">Certification &amp; reconnaissance</p>
      <h2 id="t-cert">Un diplôme d'établissement A21 University</h2>
      <p>L'Executive MBA complète l'architecture de formation sans se confondre avec le <a href="mastere.html">Mastère</a> : le Mastère forme au niveau Bac+5 des managers capables de conduire la transformation ; l'Executive MBA s'adresse à des professionnels déjà expérimentés et travaille la responsabilité globale du dirigeant.</p>
      <p>Il peut être articulé, selon les partenariats et habilitations conclus par l'établissement, à des certifications professionnelles adaptées.</p>
      {notice("<p><strong>Note.</strong> La dénomination « Executive MBA » désigne ici le programme d'établissement d'Academy Twenty One University. Elle ne constitue pas en elle-même un grade universitaire, un diplôme national ou une certification RNCP. Les éventuelles certifications professionnelles associées font l'objet d'une information distincte et conforme aux habilitations effectivement détenues.</p>")}
    </section>
  </div>
</div>
{cta_band("Rejoignez la prochaine cohorte Executive", "Admission sur dossier et entretien Executive. Échangeons sur votre projet de direction.", "executive-mba")}
'''
page("executive-mba.html","Executive MBA Gouvernance, Leadership & Transformation — Academy 21 University",
     "Executive MBA de 12 mois pour dirigeants, entrepreneurs et cadres supérieurs : 360 h, Executive Impact Project et Board Presentation.", emba)

# =====================================================================
# IA & MARKETING DE RÉSEAU
# =====================================================================
ia_rows=[["01 · Fondamentaux de l'IA &amp; marketing de réseau","3 h","IA générative, cas d'usage, prompting, fiabilité, limites, confidentialité et bonnes pratiques.","Créer une bibliothèque de prompts adaptée à son activité."],
 ["02 · Prospection augmentée par l'IA","5 h","Personas, segmentation, ciblage, messages d'approche, qualification, personnalisation et scénarios de relance.","Construire une mini-campagne de prospection multicanale."],
 ["03 · Communication &amp; Personal Branding","4 h","Positionnement, storytelling, ligne éditoriale, posts, scripts vidéo, calendrier de contenus et cohérence de marque.","Produire un calendrier éditorial et des contenus prêts à publier."],
 ["04 · Conversion, recrutement &amp; développement du réseau","4 h","Argumentaires, découverte des besoins, objections, relances, recrutement, onboarding et duplication.","Élaborer un kit de conversation et d'intégration."],
 ["05 · Automatisation &amp; pilotage de la performance","4 h","Workflows, organisation, tableaux de suivi, KPI, analyse des résultats et amélioration continue.","Concevoir son système personnel de prospection et de suivi assisté par IA."]]
ia = f'''
<section class="page-hero on-dark" aria-labelledby="page-title">
  {ring("deco","#a7dd63","#2f86ab","ph")}
  <div class="container">
    <div>
      {crumbs("IA &amp; Marketing de réseau")}
      <span class="kicker">Formation courte · Fiche prospective</span>
      <h1 id="page-title">Intelligence artificielle appliquée au marketing de réseau</h1>
      <p class="subtitle">Transformer la prospection, la communication et le développement du réseau par l'IA.</p>
    </div>
    {facts([("Format","Distanciel synchrone"),("Durée","20 heures"),("Rythme","5 séances de 4 h"),("Effectif conseillé","8 à 15 participants"),("Validation","Attestation de formation")],"ia-marketing-reseau")}
  </div>
</section>
{subnav([("finalite","Finalité"),("public","Public &amp; prérequis"),("objectifs","Objectifs"),("programme","Programme"),("approche","Approche"),("evaluation","Évaluation"),("livrables","Livrables")])}
<div class="section">
  <div class="container layout-aside">
    <div>
      <section class="content-block" id="finalite" aria-labelledby="t-fin">
        <p class="eyebrow">Finalité et positionnement</p>
        <h2 id="t-fin">Une formation directement orientée métier</h2>
        <p>Permettre aux professionnels du marketing de réseau d'intégrer l'intelligence artificielle dans leurs pratiques quotidiennes afin de gagner en efficacité, en régularité et en qualité relationnelle, <strong>sans déshumaniser la relation commerciale</strong>. Mises en situation, cas concrets et livrables immédiatement réutilisables.</p>
      </section>
      <section class="content-block" id="public" aria-labelledby="t-pub">
        <p class="eyebrow">Public cible et prérequis</p>
        <h2 id="t-pub">Pour qui ?</h2>
        <div class="grid grid--2">
          <div class="card"><span class="icon-badge icon-badge--green">{I["users"]}</span><h3>Public cible</h3><ul class="mb-0"><li>Marketeurs de réseau</li><li>Leaders et animateurs d'équipe</li><li>Entrepreneurs et indépendants</li><li>Professionnels de la vente relationnelle</li><li>Responsables de développement de réseau</li></ul></div>
          <div class="card"><span class="icon-badge icon-badge--blue">{I["monitor"]}</span><h3>Prérequis</h3><ul class="mb-0"><li>Maîtriser les usages numériques courants</li><li>Disposer d'un ordinateur connecté</li><li>Avoir une activité, un projet ou une expérience en marketing de réseau</li><li>Aucun prérequis technique en IA ou en programmation</li></ul></div>
        </div>
      </section>
      <section class="content-block" id="objectifs" aria-labelledby="t-obj">
        <p class="eyebrow">Objectifs pédagogiques</p>
        <h2 id="t-obj">Ce que vous saurez faire</h2>
        <ul class="check-list">
          <li>Comprendre les principes essentiels de l'IA générative, ses possibilités et ses limites.</li>
          <li>Maîtriser l'art du prompt pour obtenir des productions pertinentes, contextualisées et exploitables.</li>
          <li>Structurer une prospection assistée par l'IA : ciblage, personas, qualification et personnalisation.</li>
          <li>Créer plus efficacement des contenus et développer un personal branding cohérent.</li>
          <li>Améliorer les scripts de prise de contact, de présentation, de relance et de traitement des objections.</li>
          <li>Concevoir des processus de recrutement, d'onboarding et de duplication plus structurés.</li>
          <li>Mettre en place des workflows simples d'automatisation et des indicateurs de pilotage.</li>
          <li>Adopter un usage responsable de l'IA respectueux des données, de l'éthique et de la relation humaine.</li>
        </ul>
      </section>
      <section class="content-block" id="programme" aria-labelledby="t-prog">
        <p class="eyebrow">Architecture pédagogique</p>
        <h2 id="t-prog">5 modules · 20 heures</h2>
        {table("Modules de la formation IA &amp; Marketing de réseau",["Module","Durée","Contenus clés","Atelier / livrable"],ia_rows,["Total","20 h","",""])}
      </section>
      <section class="content-block" id="approche" aria-labelledby="t-app">
        <p class="eyebrow">Approche</p>
        <h2 id="t-app">Apprendre – tester – produire – améliorer</h2>
        <p>Chaque séquence alterne apports courts, démonstrations guidées, exercices individuels ou collectifs, analyse critique des résultats produits par l'IA et transposition immédiate dans l'activité.</p>
        <ul class="chips" aria-label="Formats pédagogiques"><li>Démonstrations en direct</li><li>Cas réels</li><li>Ateliers de prompting</li><li>Jeux de rôle &amp; objections</li><li>Production de contenus</li><li>Workflow final</li></ul>
        <h3 class="mt-2">Outils mobilisables</h3>
        <p>Assistants d'IA générative, outils de création de contenus, solutions de présentation et de productivité, tableurs et outils de suivi. La pédagogie reste centrée sur des méthodes transférables plutôt que sur la dépendance à une plateforme unique.</p>
      </section>
      <section class="content-block" id="evaluation" aria-labelledby="t-eval">
        <p class="eyebrow">Évaluation et validation</p>
        <h2 id="t-eval">Un suivi du début à la fin</h2>
        <ul class="bloc-list">
          <li><b>DIAGNOSTIC</b><span>Positionnement sur les usages de l'IA et les pratiques de prospection.</span></li>
          <li><b>FORMATIVE</b><span>Exercices, prompts, mises en situation et corrections au fil des modules.</span></li>
          <li><b>FIL ROUGE</b><span>Construction progressive d'un système de prospection et de développement de réseau assisté par IA.</span></li>
          <li><b>FINALE</b><span>Présentation du dispositif produit, justification des choix et démonstration d'un workflow.</span></li>
          <li><b>VALIDATION</b><span>Attestation de formation, sous réserve de participation et de réalisation des activités prévues.</span></li>
        </ul>
      </section>
      <section class="content-block" id="livrables" aria-labelledby="t-liv">
        <p class="eyebrow">Livrables</p>
        <h2 id="t-liv">Vous repartez avec votre système</h2>
        <ul class="chips"><li>Bibliothèque de prompts</li><li>Fiches personas</li><li>Scripts de prospection et de relance</li><li>Matrice de traitement des objections</li><li>Calendrier éditorial</li><li>Kit d'onboarding</li><li>Tableau de KPI</li><li>Workflow personnel de prospection IA</li><li>Plan d'action post-formation</li></ul>
        <div class="card card--navy mt-2 on-dark"><p class="eyebrow">Promesse pédagogique</p><p class="mb-0" style="font-size:1.1rem;color:#fff">À la fin de la formation, chaque participant repart avec un système concret et personnalisable pour intégrer l'IA à son activité de marketing de réseau — de la prospection au pilotage de la performance.</p></div>
      </section>
    </div>
    {aside("ia-marketing-reseau","programme IA")}
  </div>
</div>
{cta_band("Intégrez l'IA à votre activité dès la prochaine session", "5 séances de 4 h à distance, en petit groupe de 8 à 15 participants.", "ia-marketing-reseau")}
'''
page("ia-marketing-reseau.html","Formation IA appliquée au Marketing de Réseau — Academy 21 University",
     "Formation courte de 20 h à distance : intégrer l'IA générative à la prospection, la communication et le développement du réseau.", ia)

# =====================================================================
# ADMISSIONS
# =====================================================================
faq=[("Puis-je intégrer le Bachelor sans Bac+2 ?","Oui. À défaut du niveau 5, vous pouvez justifier d'au moins 5 années d'expérience professionnelle significative, appréciée individuellement lors de l'étude du dossier et de l'entretien."),
 ("Puis-je entrer directement en M2 du Mastère ?","Oui, après étude individualisée de vos acquis académiques et professionnels et décision de la commission d'admission."),
 ("Le Mastère est-il accessible en alternance ?","Le rythme peut être initial, en formation continue ou en alternance lorsque le cadre conventionnel le permet. Une expérience significative en organisation (stage long, mission, activité salariée) est attendue."),
 ("L'Executive MBA est-il un diplôme RNCP ?","Non. L'Executive MBA est un diplôme d'établissement d'Academy Twenty One University. La dénomination MBA ne constitue pas, à elle seule, un grade universitaire ni une certification RNCP."),
 ("Les formations sont-elles accessibles à distance ?","Oui : le Bachelor, le Mastère et l'Executive MBA se suivent en présentiel, en distanciel synchrone ou en hybride. La formation IA &amp; Marketing de réseau est 100 % en distanciel synchrone."),
 ("Les formations sont-elles accessibles aux personnes en situation de handicap ?","Contactez notre référent handicap avant votre candidature afin d'étudier les aménagements possibles (rythme, supports, modalités d'évaluation).")]
faq_html="".join(f'<details><summary>{q}</summary><div class="accordion__body"><p class="mb-0">{a}</p></div></details>' for q,a in faq)
admissions=f'''
<section class="page-hero page-hero--simple on-dark" aria-labelledby="page-title">
  {ring("deco", uid="ph")}
  <div class="container"><div>
    <nav class="breadcrumb" aria-label="Fil d'Ariane"><ol><li><a href="index.html">Accueil</a></li><li><span aria-current="page">Admissions</span></li></ol></nav>
    <h1 id="page-title">Admissions</h1>
    <p class="lead">Une admission sélective sur dossier et entretien, qui tient compte de votre parcours académique comme de votre expérience professionnelle.</p>
    <div class="btn-row"><a class="btn btn--accent" href="contact.html?programme=candidature">Commencer ma candidature {I["arrow"]}</a></div>
  </div></div>
</section>
<section class="section" aria-labelledby="proc-title">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Processus</p><h2 id="proc-title">4 étapes pour nous rejoindre</h2></div>
    <ol class="steps">
      <li><h3>Dossier de candidature</h3><p>Formulaire en ligne, CV, diplômes et présentation de votre projet professionnel.</p></li>
      <li><h3>Étude du dossier</h3><p>Analyse de vos acquis académiques et professionnels par l'équipe pédagogique.</p></li>
      <li><h3>Entretien</h3><p>Entretien de positionnement (Bachelor, Mastère) ou entretien Executive (EMBA).</p></li>
      <li><h3>Décision &amp; inscription</h3><p>Décision de la commission d'admission, puis finalisation de votre inscription.</p></li>
    </ol>
  </div>
</section>
<section class="section section--surface" aria-labelledby="cond-title">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Conditions d'accès</p><h2 id="cond-title">Les prérequis par programme</h2></div>
    {table("Conditions d'accès par programme",["Programme","Accès principal","Autres voies d'accès","Sélection"],
      [["<a href='bachelor.html'>Bachelor (Bac+3)</a>","Niveau 5 (Bac+2) ou niveau jugé compatible","5 ans d'expérience professionnelle significative","Dossier + entretien de positionnement"],
       ["<a href='mastere.html'>Mastère (Bac+5)</a>","Entrée en M1 : niveau 6 (Bac+3) ou équivalent","Niveau 5 + 3 ans en fonctions managériales ; entrée directe en M2 sur étude","Dossier + entretien + validation du projet"],
       ["<a href='executive-mba.html'>Executive MBA</a>","7 ans d'expérience dont management significatif ; Bac+4/5 en général","Profils différents étudiés selon responsabilités et acquis","Dossier + entretien Executive"],
       ["<a href='ia-marketing-reseau.html'>IA &amp; Marketing de réseau</a>","Activité ou projet en marketing de réseau","Aucun prérequis technique en IA","Diagnostic initial"]], vol_col=None)}
  </div>
</section>
<section class="section" id="faq" aria-labelledby="faq-title">
  <div class="container" style="max-width:860px">
    <div class="section-head section-head--center"><p class="eyebrow">FAQ</p><h2 id="faq-title">Questions fréquentes</h2></div>
    <div class="accordion">{faq_html}</div>
  </div>
</section>
{cta_band("Une question sur votre éligibilité ?", "Nos conseillers étudient votre situation et vous orientent vers le bon niveau d'entrée.")}
'''
page("admissions.html","Admissions — Academy 21 University","Conditions d'accès, processus d'admission et questions fréquentes des formations Academy 21 University.", admissions)

# =====================================================================
# CONTACT
# =====================================================================
contact=f'''
<section class="page-hero page-hero--simple on-dark" aria-labelledby="page-title">
  {ring("deco", uid="ph")}
  <div class="container"><div>
    <nav class="breadcrumb" aria-label="Fil d'Ariane"><ol><li><a href="index.html">Accueil</a></li><li><span aria-current="page">Contact</span></li></ol></nav>
    <h1 id="page-title">Candidater ou nous contacter</h1>
    <p class="lead">Demande de brochure, entretien d'orientation ou candidature : un conseiller d'admission vous répond sous 48 h ouvrées.</p>
  </div></div>
</section>
<section class="section" aria-labelledby="form-title">
  <div class="container layout-aside">
    <div>
      <h2 id="form-title">Votre demande</h2>
      <p class="text-muted">Les champs marqués d'un astérisque (<span class="req" style="color:var(--red)">*</span>) sont obligatoires.</p>
      <form class="form" data-validate action="#" method="post">
        <div class="error-summary" tabindex="-1" role="alert" hidden><h2>Erreurs</h2><ul></ul></div>
        <div class="field">
          <label for="programme">Objet de votre demande <span class="req" aria-hidden="true">*</span></label>
          <select id="programme" name="programme" required aria-describedby="programme-error" data-required="Veuillez sélectionner l'objet de votre demande.">
            <option value="">— Sélectionner —</option>
            <optgroup label="Candidater à une formation">
              <option value="bachelor">Bachelor Management Stratégique &amp; Opérationnel</option>
              <option value="mastere">Mastère Stratégie, Leadership &amp; Transformation</option>
              <option value="executive-mba">Executive MBA Gouvernance, Leadership &amp; Transformation</option>
              <option value="ia-marketing-reseau">IA appliquée au Marketing de Réseau</option>
              <option value="candidature">Je ne sais pas encore</option>
            </optgroup>
            <optgroup label="Autre demande">
              <option value="brochure">Recevoir une brochure</option>
              <option value="information">Être rappelé·e par un conseiller</option>
            </optgroup>
          </select>
          <p class="field__error" id="programme-error" aria-live="polite"></p>
        </div>
        <div class="form__row">
          <div class="field">
            <label for="prenom">Prénom <span class="req" aria-hidden="true">*</span></label>
            <input id="prenom" name="prenom" type="text" autocomplete="given-name" required aria-describedby="prenom-error" data-required="Veuillez indiquer votre prénom.">
            <p class="field__error" id="prenom-error" aria-live="polite"></p>
          </div>
          <div class="field">
            <label for="nom">Nom <span class="req" aria-hidden="true">*</span></label>
            <input id="nom" name="nom" type="text" autocomplete="family-name" required aria-describedby="nom-error" data-required="Veuillez indiquer votre nom.">
            <p class="field__error" id="nom-error" aria-live="polite"></p>
          </div>
        </div>
        <div class="form__row">
          <div class="field">
            <label for="email">Adresse e-mail <span class="req" aria-hidden="true">*</span></label>
            <p class="hint" id="email-hint">Format attendu : nom@domaine.fr</p>
            <input id="email" name="email" type="email" autocomplete="email" required aria-describedby="email-hint email-error" data-required="Veuillez indiquer votre adresse e-mail." data-format="Le format de l'adresse e-mail n'est pas valide (exemple : nom@domaine.fr).">
            <p class="field__error" id="email-error" aria-live="polite"></p>
          </div>
          <div class="field">
            <label for="tel">Téléphone</label>
            <p class="hint" id="tel-hint">Facultatif — exemple : 06 12 34 56 78</p>
            <input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" pattern="[0-9 +().-]{{8,20}}" aria-describedby="tel-hint tel-error" data-format="Le numéro doit contenir entre 8 et 20 chiffres (exemple : 06 12 34 56 78).">
            <p class="field__error" id="tel-error" aria-live="polite"></p>
          </div>
        </div>
        <div class="form__row">
          <div class="field">
            <label for="niveau">Dernier diplôme obtenu</label>
            <select id="niveau" name="niveau" aria-describedby="niveau-error">
              <option value="">— Sélectionner —</option><option>Baccalauréat</option><option>Bac+2 (niveau 5)</option><option>Bac+3 (niveau 6)</option><option>Bac+4</option><option>Bac+5 et plus (niveau 7)</option><option>Autre</option>
            </select>
            <p class="field__error" id="niveau-error" aria-live="polite"></p>
          </div>
          <div class="field">
            <label for="experience">Années d'expérience professionnelle</label>
            <select id="experience" name="experience" aria-describedby="experience-error">
              <option value="">— Sélectionner —</option><option>Moins de 3 ans</option><option>3 à 5 ans</option><option>5 à 7 ans</option><option>Plus de 7 ans</option>
            </select>
            <p class="field__error" id="experience-error" aria-live="polite"></p>
          </div>
        </div>
        <div class="field">
          <label for="message">Votre message</label>
          <textarea id="message" name="message" aria-describedby="message-error"></textarea>
          <p class="field__error" id="message-error" aria-live="polite"></p>
        </div>
        <div class="field">
          <div class="checkbox">
            <input id="rgpd" name="rgpd" type="checkbox" required data-label="Consentement" aria-describedby="rgpd-error">
            <label for="rgpd" style="font-weight:500">J'accepte que mes données soient utilisées pour traiter ma demande, conformément à la <a href="#">politique de confidentialité</a>. <span class="req" aria-hidden="true">*</span></label>
          </div>
          <p class="field__error" id="rgpd-error" aria-live="polite"></p>
        </div>
        <div class="form-status" role="status" aria-live="polite"></div>
        <div><button class="btn btn--primary" type="submit">Envoyer ma demande {I["arrow"]}</button></div>
      </form>
    </div>
    <aside aria-label="Coordonnées">
      <div class="aside-card aside-card--navy on-dark">
        <h2>Coordonnées</h2>
        <ul class="check-list mb-0" style="gap:1rem">
          <li><strong style="color:#fff">Adresse</strong><br>Adresse du campus — à compléter</li>
          <li><strong style="color:#fff">Téléphone</strong><br><a href="tel:+33000000000" style="color:#fff">+33 (0)0 00 00 00 00</a></li>
          <li><strong style="color:#fff">E-mail</strong><br><a href="mailto:admissions@a21-university.example" style="color:#fff">admissions@a21-university.example</a></li>
          <li><strong style="color:#fff">Horaires</strong><br>Du lundi au vendredi, 9 h – 18 h</li>
        </ul>
      </div>
      <div class="aside-card">
        <h2>Référent handicap</h2>
        <p class="small mb-0">Pour toute demande d'aménagement, précisez-le dans votre message : notre référent vous contactera.</p>
      </div>
    </aside>
  </div>
</section>
'''
page("contact.html","Contact & candidature — Academy 21 University","Contactez Academy 21 University : candidature, brochure, entretien d'orientation.", contact)

# =====================================================================
# CHARTE GRAPHIQUE
# =====================================================================
sw=[("Navy institutionnel","#172033","Fonds, en-têtes de tableaux, texte titre","--navy"),
    ("Navy profond","#0c1220","Pied de page, barre supérieure","--navy-950"),
    ("Rouge Academy","#b71c1c","Boutons principaux, liens, surtitres","--red"),
    ("Or Executive","#9a7b3f","Surtitres Executive (grand texte), filets","--gold"),
    ("Rouge logo","#da0612","Anneau du logo — décoratif uniquement","--logo-red"),
    ("Jaune logo","#fccd01","Boutons sur fond navy, accents","--logo-yellow"),
    ("Vert logo","#a7dd63","Accents, badges certification","--logo-green"),
    ("Bleu logo","#2f86ab","Anneau de focus clavier, accents","--logo-blue"),
    ("Gris texte","#535c6e","Texte secondaire","--muted"),
    ("Surface","#f4f6f8","Fonds de sections alternées","--surface")]
swh="".join(f'<li class="swatch"><div class="swatch__chip" style="background:{h}"></div><div class="swatch__info"><strong>{n}</strong><code>{h} · var({v})</code><br>{u}</div></li>' for n,h,u,v in sw)
charte=f'''
<section class="page-hero page-hero--simple on-dark" aria-labelledby="page-title">
  {ring("deco", uid="ph")}
  <div class="container"><div>
    <nav class="breadcrumb" aria-label="Fil d'Ariane"><ol><li><a href="index.html">Accueil</a></li><li><span aria-current="page">Charte graphique</span></li></ol></nav>
    <h1 id="page-title">Charte graphique &amp; design system</h1>
    <p class="lead">Logo, couleurs, typographies et composants du site Academy 21 University. Toutes les combinaisons de couleurs de texte respectent le niveau AA des WCAG 2.2 / RGAA 4.1.</p>
  </div></div>
</section>
<div class="section"><div class="container">
  <section class="content-block" aria-labelledby="c-logo">
    <p class="eyebrow">01 · Logo</p>
    <h2 id="c-logo">Le logo Academy 21 University</h2>
    <p>Logo extrait des brochures officielles. Il est utilisé sans déformation ni recoloration de l'emblème. La version « fond sombre » ne modifie que le texte (ACADEMY, UNIVERSITY, ™) passé en blanc.</p>
    <div class="grid grid--3">
      <div class="visual-panel" style="min-height:260px;background:#fff"><img src="assets/img/logo-a21-university.png" alt="Logo Academy 21 University, version couleur sur fond clair" width="320" height="326" style="height:200px;width:auto"></div>
      <div class="visual-panel visual-panel--navy" style="min-height:260px"><img src="assets/img/logo-a21-university-light.png" alt="Logo Academy 21 University, version pour fond sombre" width="320" height="326" style="height:200px;width:auto"></div>
      <div class="visual-panel" style="min-height:260px"><img src="assets/img/emblem-21.png" alt="Emblème 21 seul, utilisé pour l'icône du site" width="256" height="256" style="height:160px;width:auto"></div>
    </div>
    <ul class="check-list mt-2">
      <li>Zone de protection minimale : la hauteur de la lettre « A » du mot ACADEMY tout autour du logo.</li>
      <li>Taille minimale : 48 px de hauteur à l'écran (en-tête : 62 px).</li>
      <li>Ne pas étirer, incliner, ombrer ni placer l'emblème couleur sur une photo chargée.</li>
    </ul>
  </section>
  <section class="content-block" aria-labelledby="c-col">
    <p class="eyebrow">02 · Couleurs</p>
    <h2 id="c-col">Palette</h2>
    <p>Deux familles : les couleurs <strong>institutionnelles</strong> (navy, rouge, or) prélevées sur les brochures, et les couleurs <strong>du logo</strong> (rouge, jaune, vert, bleu) réservées aux accents et aux éléments décoratifs.</p>
    <ul class="swatches">{swh}</ul>
    <h3 class="mt-2">Contrastes vérifiés</h3>
    {table("Ratios de contraste des combinaisons de texte",["Combinaison","Ratio","Usage autorisé"],
      [["Blanc sur Rouge Academy #b71c1c","6,6 : 1","Tout texte (AA)"],["Rouge Academy sur blanc","6,6 : 1","Tout texte (AA)"],["Navy #172033 sur blanc","16,3 : 1","Tout texte (AAA)"],["Gris texte #535c6e sur blanc","6,7 : 1","Tout texte (AA)"],
       ["Navy sur Jaune logo #fccd01","10,8 : 1","Tout texte (AAA)"],["Jaune logo sur Navy","10,8 : 1","Tout texte (AAA)"],["#c3cad6 sur Navy","9,9 : 1","Texte courant sur fond sombre"],["Or #9a7b3f sur blanc","4,0 : 1","Grand texte uniquement (≥ 24 px)"],["Or foncé #7a5f2c sur blanc","6,0 : 1","Tout texte (AA)"]], vol_col=None)}
  </section>
  <section class="content-block" aria-labelledby="c-type">
    <p class="eyebrow">03 · Typographie</p>
    <h2 id="c-type">Trois voix complémentaires</h2>
    <div class="type-sample"><p class="small text-muted mb-0">Titres — Plus Jakarta Sans 700/800</p><p style="font-family:var(--font-display);font-weight:800;font-size:2.4rem;color:var(--ink);line-height:1.1;margin:.3rem 0">Former ceux qui dirigeront demain</p><p class="small text-muted mb-0">Géométrique et affirmée, elle fait écho aux capitales du logotype ACADEMY.</p></div>
    <div class="type-sample"><p class="small text-muted mb-0">Texte courant — Inter 400/600</p><p style="margin:.3rem 0">Le programme ne cherche pas à accumuler des enseignements. Il concentre l'apprentissage sur les questions auxquelles un dirigeant est réellement confronté.</p><p class="small text-muted mb-0">Excellente lisibilité à l'écran, chiffres tabulaires pour les volumes horaires.</p></div>
    <div class="type-sample"><p class="small text-muted mb-0">Citations &amp; sous-titres — Source Serif 4 italique</p><p class="quote" style="margin:.3rem 0">Piloter la performance • Développer l'activité • Manager les équipes</p><p class="small text-muted mb-0">Reprend la touche « grande école » des sous-titres en italique des brochures.</p></div>
  </section>
  <section class="content-block" aria-labelledby="c-comp">
    <p class="eyebrow">04 · Composants</p>
    <h2 id="c-comp">Boutons, étiquettes, notes</h2>
    <div class="btn-row mb-2"><a class="btn btn--primary" href="#c-comp">Bouton principal</a><a class="btn btn--ghost" href="#c-comp">Bouton secondaire</a><a class="btn btn--navy" href="#c-comp">Bouton navy</a></div>
    <div class="card card--navy on-dark mb-2"><div class="btn-row"><a class="btn btn--accent" href="#c-comp">Bouton sur fond sombre</a><a class="btn btn--ghost-light" href="#c-comp">Secondaire sur fond sombre</a></div></div>
    <ul class="chips mb-2" style="gap:.5rem"><li class="tag">420 h</li><li class="tag tag--rncp">RNCP38666</li><li class="tag tag--exec">Executive</li></ul>
    {notice("<p>Les notes réglementaires (RNCP, certificateur, dénomination MBA) utilisent toujours ce composant afin de rester visibles et fidèles aux documents officiels.</p>")}
  </section>
  <section class="content-block" aria-labelledby="c-a11y">
    <p class="eyebrow">05 · Accessibilité</p>
    <h2 id="c-a11y">Engagements RGAA / WCAG 2.2 AA</h2>
    <div class="grid grid--2">
      <ul class="check-list mb-0"><li>Lien d'évitement « Aller au contenu » et repères ARIA (header, nav, main, footer).</li><li>Focus clavier visible sur tous les éléments (double anneau blanc + bleu).</li><li>Cibles cliquables d'au moins 44 × 44 px.</li><li>Hiérarchie de titres cohérente, un seul H1 par page.</li></ul>
      <ul class="check-list mb-0"><li>Tableaux avec légende et en-têtes associés.</li><li>Formulaire : étiquettes visibles, aides, messages d'erreur liés et récapitulatif focalisable.</li><li>Animations désactivées si « réduire les animations » est activé.</li><li>Contenu utilisable sans JavaScript et zoom jusqu'à 200 % sans perte.</li></ul>
    </div>
  </section>
</div></div>
'''
page("charte.html","Charte graphique — Academy 21 University","Charte graphique et design system du site Academy 21 University : logo, couleurs, typographies, composants, accessibilité.", charte)
print("ok")
