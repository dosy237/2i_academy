# Référencement naturel : titres, descriptions, balises de partage et données structurées (schema.org).
import html as _html
import json
import re

SITE_URL = "https://a21businessschool.com"
BRAND = "A21 University"
OG_IMAGE = f"{SITE_URL}/assets/img/og-academy21.jpg"

# Titre (≈ 60 caractères max., affiché en entier par Google) et description (≈ 140-160 caractères).
META = {
    "index.html": ("Academy 21 University : école de management et leadership",
                   "Bachelor Bac+3, Mastère Bac+5, Executive MBA et formation IA, en présentiel, à distance ou en hybride. École de management et de leadership, Paris et Cameroun."),
    "ecole.html": (f"L'école : mission, fondateur et valeurs | {BRAND}",
                   "Découvrez Academy Twenty One University : sa mission, son fondateur le Dr Raoul Ruben NJIONOU, ses valeurs et son ambition d'école de management internationale."),
    "international.html": (f"Ouverture internationale et réseau mondial | {BRAND}",
                           "Une école ouverte sur le monde : réseau international, approche interculturelle et partenariats pour former des managers capables d'agir partout."),
    "formations.html": (f"Formations : Bachelor, Mastère, Executive MBA | {BRAND}",
                        "Comparez nos formations en management et leadership : Bachelor Bac+3 (RNCP), Mastère Bac+5, Executive MBA et formation IA, en présentiel ou à distance."),
    "bachelor.html": (f"Bachelor Management Bac+3 (RNCP) | {BRAND}",
                      "Bachelor Management Stratégique & Opérationnel : 420 h en un an, titre RNCP38666 niveau 6, en présentiel, à distance ou hybride. Devenez manager."),
    "mastere.html": (f"Mastère Stratégie & Leadership Bac+5 | {BRAND}",
                     "Mastère Bac+5 en 2 ans (900 h) : stratégie, leadership et transformation des organisations. Alternance possible, entrée en M1 ou directement en M2."),
    "executive-mba.html": (f"Executive MBA Gouvernance & Leadership | {BRAND}",
                           "Executive MBA de 12 mois pour dirigeants et cadres : 360 h de séminaires, Executive Impact Project et Board Presentation. Présentiel, distanciel ou hybride."),
    "ia-marketing-reseau.html": (f"Formation IA et marketing de réseau (20 h) | {BRAND}",
                                 "Formation de 20 heures à distance pour intégrer l'intelligence artificielle au marketing de réseau, sans prérequis technique. Attestation de formation."),
    "pedagogie.html": (f"Pédagogie et modalités d'études | {BRAND}",
                       "Une pédagogie orientée décision : cas réels, projets, simulations. Étudiez en présentiel, en distanciel synchrone ou en hybride, en initial ou en continu."),
    "entreprises.html": (f"Entreprises et partenariats | {BRAND}",
                         "Recrutez nos talents, accueillez des alternants, formez vos managers ou construisez un partenariat avec Academy Twenty One University."),
    "admissions.html": (f"Admissions : conditions, étapes et FAQ | {BRAND}",
                        "Admission sur dossier et entretien : conditions d'accès par programme, étapes, frais d'étude de dossier, certifications RNCP et questions fréquentes."),
    "candidature.html": (f"Candidater en ligne | {BRAND}",
                         "Déposez votre candidature en ligne en 5 étapes, sans frais : Bachelor, Mastère, Executive MBA ou formation IA. Votre brouillon est enregistré automatiquement."),
    "contact.html": (f"Contact | {BRAND}",
                     "Une question sur nos programmes, l'admission ou un partenariat ? Écrivez-nous ou appelez le 07 51 36 09 44 : notre équipe vous répond personnellement."),
    "brochures.html": (f"Brochures des formations (PDF) | {BRAND}",
                       "Téléchargez les brochures PDF du Bachelor, du Mastère, de l'Executive MBA et de la formation IA, ainsi que la présentation institutionnelle de l'école."),
    "mentions-legales.html": (f"Mentions légales | {BRAND}", "Mentions légales du site Academy Twenty One University : éditeur, siège social, hébergeur et propriété intellectuelle."),
    "confidentialite.html": (f"Politique de confidentialité | {BRAND}", "Comment Academy Twenty One University collecte, utilise et protège vos données personnelles, et comment exercer vos droits (RGPD)."),
    "accessibilite.html": (f"Accessibilité | {BRAND}", "Déclaration d'accessibilité du site Academy Twenty One University (RGAA 4.1) et moyens de nous signaler une difficulté."),
    "plan-du-site.html": (f"Plan du site | {BRAND}", "Toutes les pages du site Academy Twenty One University : formations, admissions, école, international, entreprises et informations légales."),
}

# Pages proposées aux moteurs de recherche (sitemap.xml) et importance relative.
SITEMAP = [
    ("index.html", "1.0"), ("formations.html", "0.9"), ("bachelor.html", "0.9"), ("mastere.html", "0.9"),
    ("executive-mba.html", "0.9"), ("ia-marketing-reseau.html", "0.8"), ("admissions.html", "0.9"), ("candidature.html", "0.8"),
    ("ecole.html", "0.7"), ("pedagogie.html", "0.7"), ("international.html", "0.6"), ("entreprises.html", "0.6"),
    ("brochures.html", "0.6"), ("contact.html", "0.6"), ("plan-du-site.html", "0.3"), ("mentions-legales.html", "0.2"),
    ("confidentialite.html", "0.2"), ("accessibilite.html", "0.2"),
]

COURSES = {
    "bachelor.html": dict(name="Bachelor Management Stratégique & Opérationnel",
                          description="Bachelor Bac+3 de 420 heures préparant au Titre professionnel Responsable d'établissement marchand (RNCP38666, niveau 6) : piloter la performance, développer l'activité, manager les équipes.",
                          credential="Titre professionnel RNCP38666 — niveau 6", workload="PT420H"),
    "mastere.html": dict(name="Mastère Stratégie, Leadership & Transformation des Organisations",
                         description="Mastère Bac+5 en deux ans (900 heures) conçu en cohérence avec le RNCP39994 « Manager des transformations des organisations » : stratégie, conduite du changement, performance et leadership.",
                         credential="Mastère Bac+5 — niveau 7", workload="PT900H"),
    "executive-mba.html": dict(name="Executive MBA Gouvernance, Leadership & Transformation",
                               description="Programme Executive de 12 mois pour dirigeants, entrepreneurs et cadres supérieurs : 360 heures de séminaires, Executive Impact Project et Board Presentation.",
                               credential="Diplôme d'établissement Executive MBA", workload="PT360H"),
    "ia-marketing-reseau.html": dict(name="IA appliquée au Marketing de Réseau",
                                     description="Formation de 20 heures en classe virtuelle pour intégrer l'intelligence artificielle aux pratiques du marketing de réseau, sans prérequis technique.",
                                     credential="Attestation de formation", workload="PT20H", modes=["online"]),
}


def page_url(fname):
    f = str(fname or "").lstrip("/")
    return f"{SITE_URL}/" if f in ("", "index.html") else f"{SITE_URL}/{f}"


ORG = {
    "@type": "EducationalOrganization",
    "@id": f"{SITE_URL}/#organisation",
    "name": "Academy Twenty One University",
    "alternateName": ["Academy 21 University", "A21 University", "A21 Business School"],
    "url": f"{SITE_URL}/",
    "logo": f"{SITE_URL}/assets/img/brand/icone-a21-512.png",
    "image": OG_IMAGE,
    "email": "contact@a21businessschool.com",
    "telephone": "+33 7 51 36 09 44",
    "slogan": "Learn. Lead. Transform.",
    "address": {"@type": "PostalAddress", "streetAddress": "7 boulevard Suchet", "postalCode": "75016",
                "addressLocality": "Paris", "addressCountry": "FR"},
    "founder": {"@type": "Person", "name": "Raoul Ruben NJIONOU", "honorificPrefix": "Dr"},
    "sameAs": ["https://www.academytwentyone.com/"],
}


def _breadcrumbs(body):
    m = re.search(r'<nav class="breadcrumb[^"]*"[^>]*><ol>(.*?)</ol></nav>', body, re.S)
    if not m:
        return None
    items = []
    for href, label in re.findall(r'<a href="([^"]+)">(.*?)</a>', m.group(1)):
        items.append((label, page_url(href)))
    cur = re.search(r'<span aria-current="page">(.*?)</span>', m.group(1))
    if cur:
        items.append((cur.group(1), None))
    out = []
    for i, (label, url) in enumerate(items):
        el = {"@type": "ListItem", "position": i + 1, "name": _html.unescape(re.sub(r"<[^>]+>", "", label))}
        if url:
            el["item"] = url
        out.append(el)
    return {"@type": "BreadcrumbList", "itemListElement": out} if len(out) > 1 else None


def _faq(body):
    qa = re.findall(r'<details><summary>(.*?)</summary><div class="accordion__body">(.*?)</div></details>', body, re.S)
    if not qa:
        return None
    clean = lambda t: _html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t))).strip()
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in qa]}


def structured_data(fname, body, title, desc):
    graph = [ORG]
    if fname == "index.html":
        graph.append({"@type": "WebSite", "@id": f"{SITE_URL}/#site", "url": f"{SITE_URL}/", "name": "Academy Twenty One University",
                      "inLanguage": "fr-FR", "publisher": {"@id": ORG["@id"]}})
    c = COURSES.get(fname)
    if c:
        graph.append({
            "@type": "Course", "name": c["name"], "description": c["description"], "url": page_url(fname), "inLanguage": "fr",
            "provider": {"@id": ORG["@id"]},
            "educationalCredentialAwarded": c["credential"],
            "offers": {"@type": "Offer", "category": "Paid", "url": f"{SITE_URL}/candidature.html"},
            "hasCourseInstance": {"@type": "CourseInstance", "courseMode": c.get("modes", ["onsite", "online", "blended"]),
                                  "courseWorkload": c["workload"]},
        })
    bc = _breadcrumbs(body)
    if bc:
        graph.append(bc)
    if fname == "admissions.html":
        fq = _faq(body)
        if fq:
            graph.append(fq)
    data = {"@context": "https://schema.org", "@graph": graph}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def head_tags(fname, title, desc, noindex):
    url = page_url(fname)
    t = _html.escape(_html.unescape(title), quote=True)
    d = _html.escape(_html.unescape(desc), quote=True)
    tags = [
        f'<link rel="canonical" href="{url}">' if not noindex else "",
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Academy Twenty One University">',
        f'<meta property="og:title" content="{t}">',
        f'<meta property="og:description" content="{d}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{OG_IMAGE}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="Academy Twenty One University — Bachelor, Mastère, Executive MBA et formation IA">',
        '<meta property="og:locale" content="fr_FR">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{t}">',
        f'<meta name="twitter:description" content="{d}">',
        f'<meta name="twitter:image" content="{OG_IMAGE}">',
    ]
    return "\n".join(x for x in tags if x)


def lazy_images(body):
    """Images hors du premier écran : chargement différé (vitesse = critère de classement)."""
    seen = {"n": 0}

    def fix(m):
        tag = m.group(0)
        seen["n"] += 1
        if "loading=" in tag:
            return tag
        if seen["n"] == 1:
            return tag.replace("<img ", '<img fetchpriority="high" ', 1)
        return tag.replace("<img ", '<img loading="lazy" decoding="async" ', 1)

    return re.sub(r"<img\b[^>]*>", fix, body)


def write_robots_and_sitemap(root, today):
    with open(f"{root}/robots.txt", "w") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: " + SITE_URL + "/sitemap.xml\n")
    urls = "".join(f"  <url><loc>{page_url(p)}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>\n" for p, pr in SITEMAP)
    with open(f"{root}/sitemap.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
