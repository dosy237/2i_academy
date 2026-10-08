# Fiches programme : Bachelor, Mastère, Executive MBA, formation IA (contenus issus des brochures).
from components import BROCHURES, pdf_size, facts_strip, NETWORK_SVG, photo_style, I, ring, page, cta_band, facts, subnav, crumbs, notice, table, aside_program, related


AMB = {"bachelor": "green", "mastere": "red", "executive-mba": "gold", "ia-marketing-reseau": "blue"}

# Bandeau de faits : l'essentiel, en valeurs courtes (le détail est dans la page)
STRIP = {
    "bachelor": [("Niveau", "Bac+3 · Niveau 6"), ("Volume", "420 h"), ("Certification", "RNCP38666"), ("Modalités", "Présentiel · Distanciel · Hybride"), ("Admission", "Bac+2 ou 5 ans d'expérience")],
    "mastere": [("Niveau", "Bac+5 · Niveau 7"), ("Durée", "2 ans · 900 h"), ("Référentiel", "RNCP39994*"), ("Rythme", "Initial, continu ou alternance"), ("Admission", "Bac+3, ou Bac+2 + 3 ans")],
    "executive-mba": [("Public", "Dirigeants &amp; CODIR"), ("Durée", "12 mois"), ("Volume", "360 h + Impact Project"), ("Rythme", "Blocs, week-ends, séminaires"), ("Expérience", "7 ans minimum")],
    "ia-marketing-reseau": [("Format", "Distanciel synchrone"), ("Durée", "20 h · 5 séances"), ("Groupe", "8 à 15 participants"), ("Prérequis", "Aucun en IA"), ("Validation", "Attestation")],
}


def hero(key, kicker, title, subtitle, chips, facts_rows, deco=None, extra="", photo=None):
    """En-tête des fiches : photo fondue à droite (ou illustration), puis bandeau de faits."""
    pdf = BROCHURES[key][0]
    level = kicker.split(" · ")[0]
    rest = " · ".join(kicker.split(" · ")[1:])
    ch = "".join(f'<li class="glass-chip">{I[i]}{t}</li>' for i, t in chips)
    if photo:
        media = f'<div class="hero-program__photo" aria-hidden="true"{photo_style(photo)}></div>'
    else:
        media = f'<div class="hero-program__visual" aria-hidden="true">{NETWORK_SVG}</div>'
    return f'''<section class="hero-program on-dark amb-{AMB[key]}" aria-labelledby="page-title">
  {media}
  <div class="container hero-program__inner">
    <div class="hero-program__text">
      {crumbs([("formations.html", "Formations"), ("", level)])}
      <ul class="hero-badges"><li class="level-tag">{level}</li>{f'<li class="glass-chip">{rest}</li>' if rest else ""}</ul>
      <h1 id="page-title">{title}</h1>
      <p class="subtitle">{subtitle}</p>
      {extra}
      <div class="btn-row">
        <a class="btn btn--accent" href="candidature.html?programme={key}">Candidater {I["arrow"]}</a>
        <a class="btn btn--glass" href="{pdf}" download>{I["download"]} Brochure <span class="visually-hidden">({pdf_size(key)})</span></a>
      </div>
    </div>
  </div>
</section>
{facts_strip(STRIP.get(key, facts_rows))}'''


def dims_cards(items, navy=False):
    cls = "card card--navy on-dark" if navy else "card card--hover"
    out = ""
    for i, (t, d, ico, c) in enumerate(items):
        badge = "icon-badge--navy" if navy else c
        out += f'<article class="{cls}"><span class="icon-badge {badge}">{I[ico]}</span><span class="num">0{i + 1}</span><h3>{t}</h3><p>{d}</p></article>'
    return out


def unfold_program(groups, label):
    """Cartes dépliables : une par année ou par bloc ; au clic, les enseignements avec leur volume et leur contenu."""
    out = ""
    for g in groups:
        kicker, title, hours, intro, modules = g
        items = "".join(
            f'<li><div class="unfold__mod"><strong>{m[0]}</strong><span class="unfold__h">{m[1]}</span></div>'
            + (f'<p>{m[2]}</p>' if len(m) > 2 and m[2] else "") + "</li>" for m in modules)
        out += (f'<details class="unfold"><summary><span class="unfold__kicker">{kicker}</span>'
                f'<span class="unfold__title">{title}</span><span class="unfold__meta"><b>{hours}</b> · {len(modules)} enseignement{"s" if len(modules) > 1 else ""}</span>'
                f'<span class="unfold__intro">{intro}</span><span class="unfold__cta" aria-hidden="true">Voir les enseignements</span></summary>'
                f'<ul class="unfold__list" aria-label="{label} — {kicker}">{items}</ul></details>')
    return f'<div class="unfold-grid">{out}</div>'


def unfold_outcomes(groups):
    """Débouchés : une carte par famille de métiers ; au clic, les compétences mobilisées pour ces métiers."""
    out = ""
    for title, jobs, skills in groups:
        chips = "".join(f"<li>{j}</li>" for j in jobs)
        sk = "".join(f"<li>{k}</li>" for k in skills)
        out += (f'<details class="unfold unfold--jobs"><summary><span class="unfold__title">{title}</span>'
                f'<ul class="chips chips--sm" aria-label="Métiers">{chips}</ul>'
                f'<span class="unfold__cta" aria-hidden="true">Compétences associées</span></summary>'
                f'<div class="unfold__body"><p class="unfold__label">Compétences mobilisées</p><ul class="check-list">{sk}</ul></div></details>')
    return f'<div class="unfold-grid unfold-grid--jobs">{out}</div>'


def build_bachelor():
    rows = [
        ["Stratégie, veille &amp; diagnostic d'activité", "35 h", "Marché, concurrence, tendances, zone de chalandise, diagnostic stratégique, RSE et orientations de développement."],
        ["Marketing &amp; développement commercial", "35 h", "Segmentation, positionnement, offre, prix, plan d'action commercial, fidélisation, omnicanalité."],
        ["Achats, stocks &amp; chaîne d'approvisionnement", "42 h", "Prévisions, commandes, fournisseurs, stocks, inventaires, rotation, démarque, continuité des flux."],
        ["Expérience client &amp; performance commerciale", "35 h", "Parcours client, qualité de service, merchandising, opérations commerciales, accessibilité, réclamations."],
        ["Finance &amp; pilotage de la rentabilité", "49 h", "CA, marges, charges, budgets, seuil de rentabilité, prévisionnels, tableaux de bord, analyse des écarts."],
        ["Leadership &amp; management opérationnel", "42 h", "Organisation, objectifs, délégation, animation, motivation, cohésion, gestion des situations sensibles."],
        ["Ressources humaines &amp; droit social", "35 h", "Recrutement, intégration, plannings, entretiens, compétences, réglementation, inclusion et handicap."],
        ["Management de projet &amp; conduite du changement", "35 h", "Cadrage, planification, ressources, risques, gouvernance, communication et mobilisation des équipes."],
        ["Digital, data &amp; intelligence artificielle", "28 h", "CRM, e-commerce, data, KPI digitaux, IA générative, automatisation, RGPD et aide à la décision."],
        ["Communication professionnelle &amp; négociation", "28 h", "Réunions, reporting, présentation de résultats, argumentation, négociation, communication managériale."],
        ["Management responsable, qualité &amp; prévention", "21 h", "RSE, sécurité, prévention, qualité, éthique, accessibilité et amélioration continue."],
        ["Projet professionnel &amp; préparation certification", "35 h", "Dossier professionnel, études de cas, productions, soutenances, simulations et préparation au jury."],
    ]
    dims = [("Stratégie &amp; Développement", "Comprendre son marché, analyser la concurrence, contribuer aux orientations stratégiques et transformer une ambition en plan d'action.", "compass", ""),
            ("Performance &amp; Pilotage", "Maîtriser les indicateurs économiques, construire budgets et prévisionnels, suivre marges et rentabilité, décider des actions correctives.", "chart", "icon-badge--blue"),
            ("Commerce &amp; Expérience client", "Piloter l'offre, les approvisionnements et l'activité commerciale, améliorer le parcours client, développer l'omnicanalité.", "target", "icon-badge--yellow"),
            ("Leadership &amp; Management", "Recruter, intégrer, organiser, développer les compétences, animer les équipes et conduire les projets.", "users", "icon-badge--green")]
    body = f'''
{hero("bachelor", "Bachelor · Bac+3", "Management Stratégique &amp; <span class='serif'>Opérationnel</span>", "Piloter la performance • Développer l'activité • Manager les équipes",
  [("award", "Titre RNCP38666"), ("clock", "420 h"), ("layers", "Présentiel · Distanciel · Hybride")],
  [("Niveau de sortie", "Bac+3 — Niveau 6"), ("Durée", "420 h de formation"), ("Certification", "Titre professionnel — RNCP38666"), ("Modalités", "Présentiel • Distanciel • Hybride"), ("Admission", "Bac+2, ou 5 ans d'expérience significative")], photo="livres")}
{subnav([("apercu", "Aperçu"), ("admission", "Admission"), ("dimensions", "Les 4 dimensions"), ("programme", "Programme"), ("debouches", "Débouchés"), ("pedagogie", "Pédagogie"), ("certification", "Certification")], "bachelor")}
<div class="section">
  <div class="container layout-aside">
    <div>
      <section class="content-block" id="apercu" aria-labelledby="t-apercu">
        <p class="eyebrow">Aperçu</p>
        <h2 id="t-apercu">Une formation pour devenir manager d'un centre de profit</h2>
        <p class="lead">Prendre la responsabilité d'une activité commerciale, en développer la performance et animer les équipes qui la font vivre.</p>
        <p>Le parcours associe vision stratégique et maîtrise du terrain : commerce, finance, management, ressources humaines, expérience client, approvisionnements, digital et conduite de projet.</p>
        <p>Au-delà des connaissances de gestion, la formation place l'apprenant dans une <strong>posture de décideur</strong> : analyser une situation, fixer des priorités, construire des prévisionnels, arbitrer, mobiliser une équipe, suivre les résultats et mettre en œuvre les actions correctives nécessaires.</p>
        <div class="grid grid--2 mt-2">
          <div class="card card--surface"><span class="icon-badge">{I["building"]}</span><h3>Présentiel</h3><p>Cours, ateliers, études de cas, simulations managériales, travaux en groupe, soutenances et accompagnement pédagogique sur site.</p></div>
          <div class="card card--surface"><span class="icon-badge icon-badge--blue">{I["monitor"]}</span><h3>Distanciel</h3><p>Classes virtuelles synchrones, ressources numériques, travaux dirigés à distance et activités collaboratives en ligne.</p></div>
        </div>
        <p class="small text-muted mt-1">Le parcours peut aussi être suivi selon une organisation hybride. Le calendrier et la répartition des séquences sont communiqués à chaque session.</p>
      </section>
      <section class="content-block" id="admission" aria-labelledby="t-admission">
        <p class="eyebrow">Conditions d'accès</p>
        <h2 id="t-admission">Deux voies d'accès</h2>
        <p>L'admission est prononcée après étude du dossier et entretien de positionnement, pour tenir compte du parcours académique comme de l'expérience professionnelle.</p>
        <div class="grid grid--2">
          <div class="card card--hover"><span class="icon-badge">{I["graduation"]}</span><h3>Accès sur diplôme</h3><p>Diplôme ou titre de niveau 5 (Bac+2), ou niveau de formation jugé compatible avec les exigences du parcours.</p><p class="small text-muted">Dossier et entretien évaluant le projet professionnel, les acquis et la capacité à suivre une formation de niveau 6.</p></div>
          <div class="card card--hover"><span class="icon-badge icon-badge--yellow">{I["briefcase"]}</span><h3>Accès sur expérience</h3><p>Au moins 5 années d'expérience professionnelle significative, prioritairement en commerce, vente, management, gestion d'activité, entrepreneuriat ou conduite d'équipe/projet.</p><p class="small text-muted">Expérience appréciée de façon individualisée lors du dossier et de l'entretien.</p></div>
        </div>
        <div class="mt-2">{notice("<p><strong>Important :</strong> la condition de 5 années d'expérience est une condition d'admission définie par Academy 21 University pour les candidats ne disposant pas du niveau académique attendu ; elle ne constitue pas une exigence réglementaire propre au RNCP38666.</p>")}</div>
      </section>
      <section class="content-block" id="dimensions" aria-labelledby="t-dim">
        <p class="eyebrow">Architecture</p>
        <h2 id="t-dim">Les 4 dimensions du Bachelor</h2>
        <div class="grid grid--2 reveal-stagger">{dims_cards(dims)}</div>
      </section>
      <section class="content-block" id="programme" aria-labelledby="t-prog">
        <p class="eyebrow">Programme · une année</p>
        <h2 id="t-prog">420 heures d'enseignements</h2>
        <p>Le Bachelor se suit sur <strong>une année</strong>, après un Bac+2 ou une expérience significative. Cliquez sur la carte pour afficher les enseignements, leur volume et leur contenu.</p>
        {unfold_program([("Année unique · Bac+3", "Les enseignements du Bachelor", "420 h", "Commerce, finance, management, ressources humaines, expérience client, approvisionnements, digital et conduite de projet.", rows)], "Enseignements du Bachelor")}
        <details class="table-toggle"><summary>Voir le programme complet sous forme de tableau</summary>
        {table("Programme du Bachelor — 420 heures", ["Enseignement", "Volume", "Contenu"], rows, ["Total", "420 h", ""])}</details>
        <p class="program-sign">Programme conçu par l'équipe pédagogique d'Academy 21 University.</p>
      </section>
      <section class="content-block" id="debouches" aria-labelledby="t-deb">
        <p class="eyebrow">Débouchés</p>
        <h2 id="t-deb">Les métiers visés</h2>
        <p>Cliquez sur la carte pour voir les compétences que le Bachelor vous permet de mobiliser.</p>
        {unfold_outcomes([("Métiers visés et compétences",
           ["Manager de centre de profit", "Responsable de point de vente", "Responsable de boutique", "Responsable de département", "Responsable commercial", "Responsable e-commerce", "Directeur adjoint", "Directeur de magasin", "Responsable de succursale", "Entrepreneur / gestionnaire d'activité"],
           ["Piloter l'activité commerciale et sécuriser les approvisionnements.", "Construire et faire évoluer une offre adaptée au marché.", "Concevoir une expérience client performante, inclusive et fidélisante.", "Traduire les orientations stratégiques en actions opérationnelles.", "Élaborer et présenter budgets, prévisionnels et tableaux de bord.", "Analyser la performance économique et décider des actions correctives.", "Piloter le recrutement, l'intégration et le développement des collaborateurs.", "Organiser le travail, manager la performance et renforcer la cohésion.", "Conduire des projets et mobiliser les équipes autour du changement."])])}
        <div class="card card--surface mt-2"><h3>Et après ?</h3><p>Poursuivez avec le Mastère Stratégie, Leadership &amp; Transformation des Organisations pour passer du pilotage d'une activité à la conduite d'une transformation.</p><a class="link-arrow" href="mastere.html">Découvrir le Mastère {I["arrow"]}</a></div>
      </section>
      <section class="content-block" id="pedagogie" aria-labelledby="t-peda">
        <p class="eyebrow">Pédagogie</p>
        <h2 id="t-peda">Une pédagogie professionnalisante</h2>
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
        {notice("<p>Une période en entreprise d'au moins <strong>350 heures</strong> est requise pour le candidat présenté au titre après un parcours de formation ; pour l'alternant, cette période est intégrée au temps de travail en entreprise.</p>", "info")}
        <div class="mt-2">{notice("<p>Parcours préparant au Titre professionnel Responsable d'établissement marchand — RNCP38666 — niveau 6. En partenariat avec <strong>GREEN UP ACADEMY</strong>, partenaire habilité pour la préparation et la présentation à la certification.</p>")}</div>
      </section>
    </div>
    {aside_program("bachelor", "Bachelor")}
  </div>
</div>
{related(["mastere", "executive-mba", "ia-marketing-reseau"])}
{cta_band("Devenez manager d'un centre de profit", "Admission sur dossier et entretien de positionnement. Parlons de votre projet.", "bachelor")}
'''
    page("bachelor.html", "Bachelor Management Stratégique & Opérationnel (Bac+3) — Academy 21 University",
         "Bachelor Bac+3 niveau 6 préparant au Titre professionnel RNCP38666 : piloter la performance, développer l'activité, manager les équipes.", body)


def build_mastere():
    m1 = [["Diagnostic stratégique &amp; intelligence économique", "50 h"], ["Économie, prospective &amp; géopolitique des affaires", "35 h"], ["Finance d'entreprise &amp; analyse de la performance", "55 h"], ["Stratégie marketing, développement &amp; expérience client", "40 h"], ["Management des organisations &amp; design organisationnel", "40 h"], ["Gestion de projet complexe &amp; méthodes agiles", "45 h"], ["Leadership, communication &amp; négociation", "40 h"], ["Transformation digitale, data &amp; intelligence artificielle", "45 h"], ["Droit des affaires, risques &amp; conformité", "30 h"], ["Méthodes de recherche &amp; Consulting Project I", "40 h"]]
    m2 = [["Corporate strategy &amp; scénarios de transformation", "50 h"], ["Pilotage financier, création de valeur &amp; contrôle stratégique", "50 h"], ["Conduite du changement &amp; sociologie des organisations", "45 h"], ["Leadership exécutif, gouvernance &amp; prise de décision", "45 h"], ["Capital humain, compétences &amp; transformation RH", "40 h"], ["Innovation, entrepreneuriat &amp; nouveaux business models", "40 h"], ["RSE, transition écologique &amp; performance globale", "35 h"], ["International business &amp; management interculturel", "35 h"], ["IA stratégique, automatisation &amp; transformation des métiers", "35 h"], ["Conseil en organisation &amp; mission de transformation", "45 h"], ["Mémoire / Consulting Project II &amp; Grand Oral", "60 h"]]
    dims = [("Stratégie", "Diagnostic, prospective, modèles économiques, choix stratégiques et gouvernance.", "compass", ""),
            ("Transformation", "Conduite du changement, transformation digitale, IA, innovation et nouveaux modèles.", "refresh", "icon-badge--blue"),
            ("Performance", "Finance, contrôle, création de valeur, KPI, performance économique, sociale et RSE.", "chart", "icon-badge--yellow"),
            ("Leadership", "Posture de dirigeant, négociation, influence, décision, management et conflits.", "leader", ""),
            ("Capital humain", "Compétences, organisation du travail, talents, inclusion, QVCT et culture.", "users", "icon-badge--blue"),
            ("Impact", "Responsabilité, transition écologique, parties prenantes, éthique et pérennité.", "globe", "icon-badge--green")]
    body = f'''
{hero("mastere", "Mastère · Bac+5 · Niveau 7", "Stratégie, Leadership &amp; <span class='serif'>Transformation</span> des Organisations",
  "Former les décideurs capables de penser la stratégie, conduire le changement et transformer durablement les organisations.",
  [("award", "RNCP39994*"), ("clock", "2 ans · 900 h"), ("graduation", "Alternance possible")],
  [("Niveau de sortie", "Bac+5 • Niveau 7"), ("Durée", "2 ans • M1 + M2"), ("Volume indicatif", "900 h"), ("Modalités", "Présentiel • Distanciel • Hybride"), ("Rythme", "Initial • Formation continue • Alternance selon convention"), ("Référentiel", "RNCP39994 • Manager des transformations des organisations*")],
  ("#2f86ab", "#a7dd63"), '<p class="motto">Apprendre. Diriger. Transformer.</p>', photo="bibliotheque")}
{subnav([("apercu", "Aperçu"), ("dimensions", "Les 6 dimensions"), ("admission", "Admission"), ("programme", "Programme"), ("rncp", "Référentiel RNCP"), ("pedagogie", "Pédagogie"), ("debouches", "Débouchés")], "mastere")}
<div class="section">
  <div class="container layout-aside">
    <div>
      <section class="content-block" id="apercu" aria-labelledby="t-apercu">
        <p class="eyebrow">Aperçu</p>
        <h2 id="t-apercu">Un Mastère pour prendre des responsabilités de direction</h2>
        <p class="lead">Dans la continuité du Bachelor, ce Mastère prépare des profils capables de passer du pilotage d'une activité à la conduite globale d'une transformation.</p>
        <p>Le programme vise une posture de cadre, manager senior, consultant ou dirigeant : analyser une organisation et son environnement, formuler des orientations stratégiques, conduire des projets complexes, mobiliser les équipes, piloter la performance économique et sociale et inscrire l'entreprise dans une dynamique durable d'adaptation.</p>
        <p class="quote">Le leadership constitue la signature du parcours : décider dans l'incertitude, donner du sens, créer l'adhésion, arbitrer, développer les compétences et assumer la responsabilité des résultats.</p>
      </section>
      <section class="content-block" id="dimensions" aria-labelledby="t-dim">
        <p class="eyebrow">Architecture</p>
        <h2 id="t-dim">Les 6 dimensions du programme</h2>
        <div class="grid grid--3 reveal-stagger">{dims_cards(dims)}</div>
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
        <p>Le Mastère se déroule sur <strong>deux années</strong>. Cliquez sur une année pour afficher ses enseignements et leur volume horaire. Entrée directe en M2 possible après étude du dossier.</p>
        {unfold_program([
          ("Année 1 · M1", "Construire la vision et maîtriser les leviers de pilotage", "420 h", "Fondamentaux du management stratégique et préparation au pilotage des transformations.", m1),
          ("Année 2 · M2", "Diriger la transformation et créer de la valeur durable", "480 h", "Posture de décision, de direction et de conseil ; mémoire ou consulting project et Grand Oral.", m2),
        ], "Enseignements du Mastère")}
        <p class="program-sign">Programme conçu par l'équipe pédagogique d'Academy 21 University.</p>
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
        <div class="grid grid--2 reveal-stagger">
          <article class="card card--hover"><h3>Direction</h3><p>Directeur d'unité • Directeur de BU • Directeur adjoint • Responsable transformation</p></article>
          <article class="card card--hover"><h3>Management</h3><p>Manager d'activité • Manager de projet • Responsable performance • Responsable développement</p></article>
          <article class="card card--hover"><h3>Conseil</h3><p>Consultant en management • Consultant en organisation • Consultant transformation</p></article>
          <article class="card card--hover"><h3>Entrepreneuriat</h3><p>Créateur / repreneur d'entreprise • Entrepreneur • Développeur de nouveaux projets</p></article>
        </div>
        <div class="mt-2">{notice("<p><strong>Note réglementaire.</strong> RNCP39994 « Manager des transformations des organisations », niveau 7, certificateur IRUP, échéance d'enregistrement au 18/12/2027. Le référentiel prévoit un accès avec un niveau 6 ou, par dérogation, un niveau 5 assorti d'au moins trois années d'expérience sur des fonctions managériales. L'obtention de la certification suppose la validation des quatre blocs et l'inscription auprès du certificateur.</p><p>* Programme pédagogique conçu en cohérence avec le RNCP39994 ; la présentation effective à la certification suppose le cadre conventionnel et l'inscription auprès du certificateur. Le présent descriptif ne vaut pas, à lui seul, habilitation du certificateur.</p>")}</div>
      </section>
    </div>
    {aside_program("mastere", "Mastère")}
  </div>
</div>
{related(["bachelor", "executive-mba", "ia-marketing-reseau"])}
{cta_band("Prenez la direction de la transformation", "Entrée en M1 ou directement en M2 selon votre parcours : la commission étudie chaque dossier individuellement.", "mastere")}
'''
    page("mastere.html", "Mastère Stratégie, Leadership & Transformation des Organisations (Bac+5) — Academy 21 University",
         "Mastère Bac+5 niveau 7 en 2 ans, 900 h, conçu en cohérence avec le RNCP39994 Manager des transformations des organisations.", body)


def build_emba():
    rows = [["Strategic Foresight &amp; CEO Agenda", "30 h", "Prospective, signaux faibles, scénarios, vision, agenda stratégique du dirigeant."],
            ["Corporate Strategy &amp; Business Portfolio", "35 h", "Stratégie corporate, portefeuille, avantage concurrentiel, diversification, alliances."],
            ["Finance, Capital Allocation &amp; Value Creation", "35 h", "Cash, rentabilité, valorisation, financement, allocation du capital, décisions d'investissement."],
            ["Corporate Governance &amp; Board Dynamics", "25 h", "Gouvernance, conseil, délégation, contrôle, parties prenantes, responsabilité du dirigeant."],
            ["Executive Leadership &amp; Power", "35 h", "Pouvoir, influence, autorité, décision, conflits, courage managérial et posture."],
            ["People, Culture &amp; Succession", "25 h", "Culture, équipe dirigeante, talents clés, succession, transformation managériale."],
            ["Transformation, AI &amp; Digital Strategy", "35 h", "IA, digital, automatisation, data, transformation des métiers et gouvernance technologique."],
            ["Growth, International &amp; Strategic Partnerships", "30 h", "Croissance, internationalisation, alliances, négociation et développement d'écosystèmes."],
            ["Crisis, Risk &amp; Reputation", "25 h", "Risques, crise, continuité, communication sensible, réputation et décision sous pression."],
            ["Sustainable Business &amp; Impact", "20 h", "ESG, transition, impact, modèle responsable et création de valeur durable."],
            ["Executive Negotiation &amp; Public Leadership", "20 h", "Négociation de haut niveau, communication de dirigeant, influence institutionnelle."],
            ["Executive Impact Project &amp; Board Presentation", "45 h", "Problématique réelle, diagnostic, arbitrages, feuille de route et présentation devant un Board."]]
    resp = [("Donner le cap", "Vision, prospective, stratégie, gouvernance et priorités.", "compass", ""), ("Arbitrer", "Finance, capital, risques, portefeuille d'investissements et création de valeur.", "scale", ""),
            ("Mobiliser", "Leadership, culture, influence, talent, succession et engagement.", "users", ""), ("Transformer", "Innovation, changement, IA, digital, nouveaux modèles et organisation.", "refresh", ""),
            ("Développer", "Croissance, alliances, international, réputation et écosystèmes.", "globe", ""), ("Assumer", "Éthique, responsabilité, crise, parties prenantes et impact.", "shield", "")]
    exp = [("Executive Case Method", "Analyse de situations complexes et défense d'une décision devant les pairs."), ("Boardroom Simulations", "Conseil d'administration, comité de direction, crise, investissement et transformation."),
           ("CEO &amp; Leaders Series", "Rencontres avec dirigeants, entrepreneurs, investisseurs, experts et personnalités qualifiées."), ("Peer Learning", "Capitalisation structurée sur l'expérience professionnelle des participants."),
           ("Executive Coaching", "Travail individuel sur la posture, les priorités, les angles morts et la trajectoire de leadership."), ("International &amp; Strategic Immersion", "Séminaire ou étude comparative d'écosystèmes économiques et managériaux.")]
    expc = "".join(f'<div class="card card--hover"><span class="num">0{i + 1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(exp))
    body = f'''
{hero("executive-mba", "Executive MBA · Executive Education", "Gouvernance, Leadership &amp; <span class='serif'>Transformation</span>", "Le programme de haute direction d'Academy Twenty One University.",
  [("clock", "12 mois"), ("leader", "7 ans d'expérience minimum"), ("presentation", "Board Presentation")],
  [("Positionnement", "Programme Executive de haute direction"), ("Public", "Dirigeants • Entrepreneurs • Cadres supérieurs • Membres de CODIR"), ("Durée", "12 mois"), ("Volume indicatif", "360 h + Executive Impact Project"), ("Organisation", "Blocs intensifs • Week-ends Executive • Séminaires"), ("Modalités", "Présentiel • Distanciel synchrone • Hybride"), ("Expérience", "7 ans minimum, dont responsabilités managériales significatives")],
  ("#fccd01", "#da0612"), '<p class="motto">Think. Decide. Lead. Transform.</p>', photo="leadership")}
{subnav([("apercu", "Aperçu"), ("public", "Public &amp; admission"), ("responsabilites", "Les 6 responsabilités"), ("programme", "Programme"), ("experience", "Expérience Executive"), ("organisation", "Organisation"), ("certification", "Reconnaissance")], "executive-mba")}
<div class="section">
  <div class="container layout-aside">
    <div>
      <section class="content-block" id="apercu" aria-labelledby="t-apercu">
        <p class="eyebrow eyebrow--gold">Le programme de ceux qui portent la responsabilité finale</p>
        <h2 id="t-apercu">Prendre de la hauteur, arbitrer, assumer</h2>
        <p class="lead">Conçu pour des professionnels qui ne découvrent plus le management : ils l'exercent déjà.</p>
        <p>Leur enjeu n'est plus seulement de maîtriser une fonction, mais de prendre de la hauteur, arbitrer entre des intérêts contradictoires, engager des ressources, conduire des transformations et assumer la responsabilité globale de la décision.</p>
        <p>Programme le plus senior de la filière Management &amp; Leadership, il crée un espace exigeant où dirigeants, entrepreneurs et cadres supérieurs confrontent leurs pratiques, renforcent leur capacité stratégique et travaillent leur posture de leader.</p>
        <p class="quote">Où aller, pourquoi, avec quelles ressources, avec quelles équipes, à quel risque, et comment créer durablement de la valeur ?</p>
      </section>
      <section class="content-block" id="public" aria-labelledby="t-public">
        <p class="eyebrow">Public</p>
        <h2 id="t-public">À qui s'adresse l'Executive MBA ?</h2>
        <div class="grid grid--2 reveal-stagger">
          <article class="card card--hover"><span class="icon-badge">{I["leader"]}</span><h3>Dirigeants</h3><p>Présidents, directeurs généraux, directeurs adjoints, dirigeants de PME/ETI, responsables de filiales ou d'unités.</p></article>
          <article class="card card--hover"><span class="icon-badge icon-badge--blue">{I["briefcase"]}</span><h3>Cadres supérieurs</h3><p>Membres ou futurs membres de comités de direction souhaitant passer d'une expertise fonctionnelle à une vision globale.</p></article>
          <article class="card card--hover"><span class="icon-badge icon-badge--yellow">{I["rocket"]}</span><h3>Entrepreneurs</h3><p>Fondateurs et repreneurs confrontés aux enjeux de structuration, gouvernance, croissance, financement et changement d'échelle.</p></article>
          <article class="card card--hover"><span class="icon-badge icon-badge--green">{I["users"]}</span><h3>Leaders d'organisations</h3><p>Responsables de réseaux, institutions ou communautés ayant une responsabilité importante de mobilisation et de gouvernance.</p></article>
        </div>
        <h3 class="mt-2">Une admission sélective</h3>
        <p>Le programme privilégie les candidats justifiant d'au moins <strong>7 années d'expérience professionnelle</strong>, dont une expérience significative de management, de direction, d'entrepreneuriat ou de pilotage d'une activité. Admission sur dossier, <strong>entretien Executive</strong> et appréciation de la maturité du projet professionnel.</p>
        <p>Le niveau académique attendu est généralement Bac+4/Bac+5 ou équivalent. Des profils au parcours académique différent peuvent être étudiés lorsque l'expérience, le niveau de responsabilité et les acquis professionnels démontrent une capacité à suivre le programme.</p>
      </section>
    </div>
    {aside_program("executive-mba", "Executive MBA")}
  </div>
</div>
<section class="section section--navy on-dark" id="responsabilites" aria-labelledby="t-resp">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container" style="position:relative">
    <div class="section-head reveal"><p class="eyebrow">Architecture du leadership</p><h2 id="t-resp">Les 6 responsabilités du dirigeant</h2></div>
    <div class="grid grid--3 reveal-stagger">{"".join(f'<article class="card card--glass-dark"><span class="icon-badge icon-badge--navy">{I[ico]}</span><span class="num">0{i + 1}</span><h3>{t}</h3><p>{d}</p></article>' for i, (t, d, ico, c) in enumerate(resp))}</div>
  </div>
</section>
<div class="section">
  <div class="container container--narrow">
    <section class="content-block" id="programme" aria-labelledby="t-prog">
      <p class="eyebrow">Architecture du programme</p>
      <h2 id="t-prog">360 heures de séminaires de haute intensité</h2>
      <p>Chaque module part d'une problématique de direction et conduit à une décision, un arbitrage ou une feuille de route. Les apports conceptuels sont systématiquement confrontés aux situations réelles des participants.</p>
      <p>Cliquez sur la carte pour afficher les douze modules, leur volume et leur focus.</p>
      {unfold_program([("12 mois · Executive", "Les modules de l'Executive MBA", "360 h", "Stratégie, finance, gouvernance, leadership, transformation, croissance, risques et impact, jusqu'à la Board Presentation.", rows)], "Modules de l'Executive MBA")}
      <details class="table-toggle"><summary>Voir tous les modules sous forme de tableau</summary>
      {table("Modules de l'Executive MBA", ["Module", "Vol.", "Focus Executive"], rows, ["Total", "360 h", ""])}</details>
        <p class="program-sign">Programme conçu par l'équipe pédagogique d'Academy 21 University.</p>
    </section>
    <section class="content-block" id="experience" aria-labelledby="t-exp">
      <p class="eyebrow">Pédagogie</p>
      <h2 id="t-exp">Une expérience Executive, pas une scolarité classique</h2>
      <div class="grid grid--2 reveal-stagger">{expc}</div>
      <div class="split split--top mt-3">
        <div class="card card--navy on-dark"><span class="icon-badge icon-badge--navy">{I["presentation"]}</span><h3>Executive Impact Project</h3><p>Chaque participant travaille sur une problématique stratégique liée à son entreprise, son organisation ou son projet entrepreneurial. Pas un mémoire théorique, mais un document de direction exploitable : diagnostic, options, scénarios, arbitrages, impacts financiers et humains, risques, gouvernance et plan de mise en œuvre.</p><p>Le programme se conclut par une <strong style="color:#fff">Board Presentation</strong> : le participant défend son projet comme devant un conseil d'administration, des investisseurs ou un comité exécutif.</p></div>
        <div>
          <h3>Évaluation</h3>
          <p>Il n'y a pas de logique d'examen académique traditionnel comme principe central. L'évaluation porte sur la qualité du raisonnement stratégique, la capacité d'arbitrage, la pertinence des recommandations, la maîtrise des données financières et opérationnelles, la posture de leadership et la capacité à défendre une décision.</p>
          <ul class="chips" aria-label="Productions évaluées"><li>Notes de décision</li><li>Board papers</li><li>Analyses stratégiques</li><li>Simulations</li><li>Travaux collectifs</li><li>Soutenance finale</li></ul>
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
      <p>L'Executive MBA complète l'architecture de formation sans se confondre avec le Mastère : le Mastère forme au niveau Bac+5 des managers capables de conduire la transformation ; l'Executive MBA s'adresse à des professionnels déjà expérimentés et travaille la responsabilité globale du dirigeant.</p>
      <p>Il peut être articulé, selon les partenariats et habilitations conclus par l'établissement, à des certifications professionnelles adaptées. Toute communication relative à une certification RNCP identifie explicitement la certification, son certificateur et le cadre d'habilitation applicable.</p>
      {notice("<p><strong>Note.</strong> La dénomination « Executive MBA » désigne ici le programme d'établissement d'Academy Twenty One University. Elle ne constitue pas en elle-même un grade universitaire, un diplôme national ou une certification RNCP. Les éventuelles certifications professionnelles associées font l'objet d'une information distincte et conforme aux habilitations effectivement détenues.</p>")}
    </section>
  </div>
</div>
{related(["mastere", "ia-marketing-reseau"], "Les autres programmes de la filière")}
{cta_band("Rejoignez la prochaine cohorte Executive", "Admission sur dossier et entretien Executive. Échangeons sur votre projet de direction.", "executive-mba")}
'''
    page("executive-mba.html", "Executive MBA Gouvernance, Leadership & Transformation — Academy 21 University",
         "Executive MBA de 12 mois pour dirigeants, entrepreneurs et cadres supérieurs : 360 h, Executive Impact Project et Board Presentation.", body)


def build_ia():
    rows = [["01 · Fondamentaux de l'IA &amp; marketing de réseau", "3 h", "IA générative, cas d'usage, prompting, fiabilité, limites, confidentialité et bonnes pratiques.", "Créer une bibliothèque de prompts adaptée à son activité."],
            ["02 · Prospection augmentée par l'IA", "5 h", "Personas, segmentation, ciblage, messages d'approche, qualification, personnalisation et scénarios de relance.", "Construire une mini-campagne de prospection multicanale."],
            ["03 · Communication &amp; Personal Branding", "4 h", "Positionnement, storytelling, ligne éditoriale, posts, scripts vidéo, calendrier de contenus et cohérence de marque.", "Produire un calendrier éditorial et des contenus prêts à publier."],
            ["04 · Conversion, recrutement &amp; développement du réseau", "4 h", "Argumentaires, découverte des besoins, objections, relances, recrutement, onboarding et duplication.", "Élaborer un kit de conversation et d'intégration."],
            ["05 · Automatisation &amp; pilotage de la performance", "4 h", "Workflows, organisation, tableaux de suivi, KPI, analyse des résultats et amélioration continue.", "Concevoir son système personnel de prospection et de suivi assisté par IA."]]
    body = f'''
{hero("ia-marketing-reseau", "Formation courte · IA appliquée", "Intelligence artificielle appliquée au <span class='serif'>marketing de réseau</span>", "Transformer la prospection, la communication et le développement du réseau par l'IA.",
  [("monitor", "100 % à distance"), ("clock", "20 h · 5 séances"), ("users", "8 à 15 participants")],
  [("Format", "Distanciel synchrone"), ("Durée", "20 heures"), ("Rythme", "5 séances de 4 h"), ("Effectif conseillé", "8 à 15 participants"), ("Prérequis", "Aucun prérequis technique en IA"), ("Validation", "Attestation de formation")],
  ("#a7dd63", "#2f86ab"))}
{subnav([("finalite", "Finalité"), ("public", "Public &amp; prérequis"), ("objectifs", "Objectifs"), ("programme", "Programme"), ("approche", "Approche"), ("evaluation", "Évaluation"), ("livrables", "Livrables")], "ia-marketing-reseau")}
<div class="section">
  <div class="container layout-aside">
    <div>
      <section class="content-block" id="finalite" aria-labelledby="t-fin">
        <p class="eyebrow">Finalité et positionnement</p>
        <h2 id="t-fin">Une formation directement orientée métier</h2>
        <p class="lead">Intégrer l'intelligence artificielle dans vos pratiques quotidiennes pour gagner en efficacité, en régularité et en qualité relationnelle — sans déshumaniser la relation commerciale.</p>
        <p>La formation privilégie les mises en situation, les cas concrets et la production de livrables immédiatement réutilisables.</p>
      </section>
      <section class="content-block" id="public" aria-labelledby="t-pub">
        <p class="eyebrow">Public cible et prérequis</p>
        <h2 id="t-pub">Pour qui ?</h2>
        <div class="grid grid--2">
          <div class="card card--hover"><span class="icon-badge icon-badge--green">{I["users"]}</span><h3>Public cible</h3><ul class="mb-0"><li>Marketeurs de réseau</li><li>Leaders et animateurs d'équipe</li><li>Entrepreneurs et indépendants</li><li>Professionnels de la vente relationnelle</li><li>Responsables de développement de réseau</li></ul></div>
          <div class="card card--hover"><span class="icon-badge icon-badge--blue">{I["monitor"]}</span><h3>Prérequis</h3><ul class="mb-0"><li>Maîtriser les usages numériques courants</li><li>Disposer d'un ordinateur connecté</li><li>Avoir une activité, un projet ou une expérience en marketing de réseau</li><li>Aucun prérequis technique en IA ou en programmation</li></ul></div>
        </div>
      </section>
      <section class="content-block" id="objectifs" aria-labelledby="t-obj">
        <p class="eyebrow">Objectifs pédagogiques</p>
        <h2 id="t-obj">Ce que vous saurez faire</h2>
        <ul class="check-list check-list--cols">
          <li>Comprendre les principes de l'IA générative, ses possibilités et ses limites.</li>
          <li>Maîtriser l'art du prompt pour obtenir des productions exploitables.</li>
          <li>Structurer une prospection assistée par l'IA : ciblage, personas, qualification.</li>
          <li>Créer des contenus et développer un personal branding cohérent.</li>
          <li>Améliorer vos scripts de contact, présentation, relance et objections.</li>
          <li>Concevoir recrutement, onboarding et duplication plus structurés.</li>
          <li>Mettre en place des workflows d'automatisation et des indicateurs.</li>
          <li>Adopter un usage responsable : données, éthique et relation humaine.</li>
        </ul>
      </section>
      <section class="content-block" id="programme" aria-labelledby="t-prog">
        <p class="eyebrow">Architecture pédagogique</p>
        <h2 id="t-prog">5 séances · <span class="serif">20 heures</span></h2>
        <ol class="timeline reveal-stagger">{"".join(f'<li><span class="timeline__dot" aria-hidden="true">{n + 1}</span><div class="timeline__card"><span class="tag">{r[1]}</span><h3>{r[0].split(" · ", 1)[1]}</h3><p>{r[2]}</p><span class="timeline__out">Livrable : {r[3]}</span></div></li>' for n, r in enumerate(rows))}</ol>
      </section>
      <section class="content-block" id="approche" aria-labelledby="t-app">
        <p class="eyebrow">Approche</p>
        <h2 id="t-app">Apprendre – tester – produire – améliorer</h2>
        <p>Chaque séquence alterne apports courts, démonstrations guidées, exercices individuels ou collectifs, analyse critique des résultats produits par l'IA et transposition immédiate dans l'activité professionnelle.</p>
        <ul class="chips" aria-label="Formats pédagogiques"><li>Démonstrations en direct</li><li>Cas réels de marketing de réseau</li><li>Ateliers de prompting</li><li>Jeux de rôle &amp; objections</li><li>Production de contenus</li><li>Workflow final</li></ul>
        <h3 class="mt-2">Outils mobilisables</h3>
        <p>Assistants d'IA générative, outils de création de contenus, solutions de présentation et de productivité, tableurs et outils de suivi. Le choix précis est adapté au niveau des participants ; la pédagogie reste centrée sur des méthodes transférables plutôt que sur une plateforme unique.</p>
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
        <p class="mt-2">À l'issue des 20 heures, le participant est capable de concevoir et piloter un dispositif simple, cohérent et mesurable d'acquisition, de communication et d'animation de réseau assisté par IA, en conservant la maîtrise humaine des décisions, des messages et de la relation.</p>
      </section>
      <section class="content-block" id="livrables" aria-labelledby="t-liv">
        <p class="eyebrow">Livrables</p>
        <h2 id="t-liv">Vous repartez avec votre système</h2>
        <ul class="chips"><li>Bibliothèque de prompts</li><li>Fiches personas</li><li>Scripts de prospection et de relance</li><li>Matrice de traitement des objections</li><li>Calendrier éditorial</li><li>Kit d'onboarding</li><li>Tableau de KPI</li><li>Workflow personnel de prospection IA</li><li>Plan d'action post-formation</li></ul>
        <div class="card card--navy on-dark mt-2"><p class="motto">Promesse pédagogique</p><p class="mb-0" style="font-size:1.1rem;color:#fff">À la fin de la formation, chaque participant repart avec un système concret et personnalisable pour intégrer l'IA à son activité de marketing de réseau — de la prospection au pilotage de la performance.</p></div>
      </section>
    </div>
    {aside_program("ia-marketing-reseau", "programme IA")}
  </div>
</div>
{related(["bachelor", "mastere", "executive-mba"])}
{cta_band("Intégrez l'IA à votre activité dès la prochaine session", "5 séances de 4 h à distance, en petit groupe de 8 à 15 participants.", "ia-marketing-reseau")}
'''
    page("ia-marketing-reseau.html", "Formation IA appliquée au Marketing de Réseau — Academy 21 University",
         "Formation courte de 20 h à distance : intégrer l'IA générative à la prospection, la communication et le développement du réseau.", body)
