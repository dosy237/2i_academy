# Pages institutionnelles : accueil, école, pédagogie, entreprises, formations, brochures.
from components import (ring4, hero_light, hero_editorial, hero_visual, hero_minimal, photo_img, GLOBE_SVG, founder_block, photo_style, I, P, PROGRAMS, BROCHURES, CONTACT_EMAIL, ring, page, cta_band, program_card,
                        simple_hero, table, notice, pdf_size)


def build_index():
    pathway = f'''<ol class="pathway reveal">
  <li><span class="pathway__dot">Bac+3</span><a class="pathway__card" href="bachelor.html"><span class="pathway__level">Bachelor</span><span class="pathway__role">Manager</span><p>Piloter une activité, une équipe et la performance opérationnelle.</p></a></li>
  <li><span class="pathway__dot">Bac+5</span><a class="pathway__card" href="mastere.html"><span class="pathway__level">Mastère · Niveau 7</span><span class="pathway__role">Strategic Leader</span><p>Concevoir et conduire la transformation d'une organisation.</p></a></li>
  <li><span class="pathway__dot">MBA</span><div class="pathway__card"><span class="pathway__level">MBA · Niveau 7</span><span class="pathway__role">Business Leader</span><p>Élargir sa maîtrise de la stratégie, de la finance et du développement.</p><span class="pathway__soon">Programme en préparation</span></div></li>
  <li><span class="pathway__dot">EMBA</span><a class="pathway__card" href="executive-mba.html"><span class="pathway__level">Executive MBA</span><span class="pathway__role">Executive Leader</span><p>Gouverner, arbitrer, transformer et assumer la responsabilité globale.</p></a></li>
</ol>'''

    deliverables = [
        ("presentation", "", "Board papers &amp; Executive Impact Project", "Un document de direction exploitable — diagnostic, scénarios, arbitrages, plan de mise en œuvre — défendu devant un Board.", "Executive MBA"),
        ("compass", "icon-badge--blue", "Diagnostics stratégiques", "Marché, concurrence, organisation, puis orientations argumentées.", "Bachelor · Mastère"),
        ("chart", "", "Tableaux de bord &amp; budgets", "Prévisionnels, écarts, KPI.", "Bachelor"),
        ("briefcase", "icon-badge--yellow", "Missions de conseil", "Consulting Projects et Grand Oral.", "Mastère"),
        ("cpu", "icon-badge--green", "Workflow IA personnel", "Prompts, personas, scripts et tableau de KPI.", "Formation IA"),
        ("users", "icon-badge--blue", "Plans de management", "Recrutement, intégration, conduite du changement.", "Bachelor · Mastère"),
    ]
    deliv = ""
    for n, (i, c, t, d, tag) in enumerate(deliverables):
        if n == 0:
            deliv += (f'<article class="card card--feature on-dark">{ring4("ring4", "bf")}<span class="icon-badge icon-badge--navy">{I[i]}</span>'
                      f'<span class="num">{tag}</span><h3>{t}</h3><p>{d}</p></article>')
        else:
            deliv += f'<article class="card card--hover"><span class="icon-badge {c}">{I[i]}</span><span class="num">{tag}</span><h3>{t}</h3><p>{d}</p></article>'
    faq = [("Puis-je candidater sans Bac+2 ?", "Oui pour le Bachelor : à défaut du niveau 5, vous pouvez justifier d'au moins 5 années d'expérience professionnelle significative, appréciées lors de l'étude du dossier et de l'entretien."),
           ("Les formations sont-elles accessibles à distance ?", "Le Bachelor, le Mastère et l'Executive MBA se suivent en présentiel, en distanciel synchrone ou en hybride. La formation IA &amp; Marketing de réseau se déroule entièrement à distance, en classe virtuelle."),
           ("Le Mastère est-il possible en alternance ?", "Oui, lorsque le cadre conventionnel le permet. Il peut aussi être suivi en formation initiale ou en formation continue.")]
    faq_html = "".join(f'<details><summary>{q}</summary><div class="accordion__body"><p>{a}</p></div></details>' for q, a in faq)

    body = f'''
<section class="hero on-dark" aria-labelledby="hero-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container">
    <div>
      <p class="eyebrow">Academy Twenty One University</p>
      <h1 id="hero-title">Former ceux qui <span class="serif">dirigeront</span> demain.</h1>
      <p class="lead">Du Bachelor à l'Executive MBA : des managers, des leaders et des dirigeants qui décident et transforment.</p>
      <div class="btn-row">
        <a class="btn btn--accent" href="formations.html">Découvrir nos formations {I["arrow"]}</a>
        <a class="btn btn--glass" href="candidature.html">Candidater en ligne</a>
      </div>
      <ul class="hero__stats" aria-label="Chiffres clés">
        <li><strong>4 programmes</strong><span>du Bachelor à l'Executive MBA</span></li>
        <li><strong>3 modalités</strong><span>présentiel, distanciel, hybride</span></li>
        <li><strong>Niveaux 6 &amp; 7</strong><span>référentiels RNCP</span></li>
      </ul>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <div class="hero-visual__halo"></div>
      {ring4("ring4 hero-visual__ring", "hq")}
      <div class="hero-visual__disc"></div>
      <div class="float-card float-card--a"><span class="float-card__icon" style="background:#eef8e2;color:#3f6e12">{I["award"]}</span><span><strong>RNCP38666</strong>Titre pro. niveau 6</span></div>
      <div class="float-card float-card--b"><span class="float-card__icon" style="background:#fff6cc;color:#5f4a00">{I["layers"]}</span><span><strong>Hybride</strong>Sur site ou à distance</span></div>
      <div class="float-card float-card--c"><span class="float-card__icon" style="background:#fbecec;color:#b71c1c">{I["leader"]}</span><span><strong>Leadership</strong>la signature de nos parcours</span></div>
    </div>
  </div>
  <svg class="wave" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path fill="currentColor" d="M0 60c240-50 480-60 720-30s480 40 720-10v70H0z"/></svg>
</section>

<section class="finder" aria-labelledby="finder-title">
  <div class="container">
    <div class="finder__panel">
      <div class="finder__head"><h2 class="finder__title" id="finder-title">Trouver ma formation</h2><p>Choisissez selon votre niveau et votre expérience.</p></div>
      <ul class="pill-nav">
        <li><a href="bachelor.html">Bachelor<span>Bac+3 · Niveau 6</span></a></li>
        <li><a href="mastere.html">Mastère<span>Bac+5 · Niveau 7</span></a></li>
        <li><a href="executive-mba.html">Executive MBA<span>Dirigeants · 12 mois</span></a></li>
        <li><a href="ia-marketing-reseau.html">Formation IA<span>20 h · à distance</span></a></li>
      </ul>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="ambition-title">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Notre ambition</p>
      <h2 id="ambition-title">Une école qui associe exigence, terrain et responsabilité</h2>
      <p class="lead">Une offre cohérente centrée sur le management, l'entrepreneuriat et le leadership, avec une signature professionnalisante, internationale et connectée aux transformations des organisations.</p>
      <ul class="check-list">
        <li><strong>Une pédagogie par la décision :</strong> chaque séquence conduit à une production concrète — diagnostic, budget, feuille de route.</li>
        <li><strong>Des parcours qui se prolongent :</strong> du pilotage d'une activité à la responsabilité globale du dirigeant.</li>
        <li><strong>Une organisation compatible avec la vie active :</strong> présentiel, distanciel synchrone ou hybride.</li>
      </ul>
      <div class="btn-row"><a class="btn btn--navy" href="ecole.html">Découvrir l'école {I["arrow"]}</a><a class="link-arrow" href="formations.html">Comparer les formations {I["arrow"]}</a></div>
    </div>
    <div class="photo-card reveal"{photo_style("bibliotheque")}>
      <span class="glass-chip photo-card__tag">{I["layers"]} Présentiel · Distanciel · Hybride</span>
      <div class="photo-card__glass">
        <div><strong>420 h</strong><span>Bachelor</span></div>
        <div><strong>900 h</strong><span>Mastère, 2 ans</span></div>
        <div><strong>360 h</strong><span>Executive MBA</span></div>
        <div><strong>20 h</strong><span>Formation IA</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--surface" aria-label="Le fondateur">
  <div class="container">
    {founder_block("h2")}
  </div>
</section>

<section class="section section--navy on-dark" aria-labelledby="filiere-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container" style="position:relative">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">La filière Management &amp; Leadership</p>
      <h2 id="filiere-title">Quatre niveaux de responsabilité, un même fil rouge</h2>
      <p class="lead">Chaque programme prépare à un palier de décision. Vous entrez au niveau qui correspond à votre parcours et à votre expérience.</p>
    </div>
    {pathway}
  </div>
</section>

<section class="section" aria-labelledby="prog-title">
  <div class="container">
    <div class="section-head section-head--row reveal">
      <div><p class="eyebrow">Nos formations</p><h2 id="prog-title">Choisissez le programme qui correspond à votre trajectoire</h2></div>
      <a class="link-arrow" href="formations.html">Voir le comparatif {I["arrow"]}</a>
    </div>
    <div class="grid grid--4 reveal-stagger">{"".join(program_card(p["key"]) for p in PROGRAMS)}</div>
  </div>
</section>

<section class="section section--mesh" aria-labelledby="deliv-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="motto">Apprendre. Diriger. Transformer.</p>
      <h2 id="deliv-title">Des livrables concrets, pas seulement des <span class="serif">copies</span></h2>
      <p class="lead">Chaque module débouche sur une production réutilisable dans votre organisation.</p>
    </div>
    <div class="bento reveal-stagger">{deliv}</div>
    <div class="center-row mt-2"><a class="btn btn--ghost" href="pedagogie.html">Notre pédagogie en détail {I["arrow"]}</a></div>
  </div>
</section>

<section class="section" aria-labelledby="mod-title">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Modalités</p>
      <h2 id="mod-title">Se former sans mettre sa vie professionnelle entre <span class="serif">parenthèses</span></h2>
    </div>
    <div class="spectrum reveal">
      <p class="spectrum__ends" aria-hidden="true"><span>Sur site</span><span>À distance</span></p>
      <div class="spectrum__bar" aria-hidden="true"><span style="left:16.6%"></span><span style="left:50%"></span><span style="left:83.4%"></span></div>
      <div class="grid grid--3 reveal-stagger">
        <article class="card card--hover"><span class="icon-badge">{I["building"]}</span><h3>Présentiel</h3><p>Cours, ateliers, études de cas, simulations et soutenances sur site.</p></article>
        <article class="card card--hover"><span class="icon-badge icon-badge--yellow">{I["layers"]}</span><h3>Hybride</h3><p>Les deux modalités combinées, selon le calendrier de chaque session.</p></article>
        <article class="card card--hover"><span class="icon-badge icon-badge--blue">{I["monitor"]}</span><h3>Distanciel synchrone</h3><p>Classes virtuelles en direct et activités collaboratives en ligne.</p></article>
      </div>
    </div>
  </div>
</section>

<section class="section section--navy on-dark" aria-labelledby="world-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container split" style="position:relative">
    <div class="reveal">
      <p class="eyebrow" lang="en">Global engagement</p>
      <h2 id="world-title" lang="en">The world is our <span class="serif">campus.</span></h2>
      <p class="lead">Une communauté Academy Twenty One présente sur 5 continents et dans plus de 75 pays*, une ambition Erasmus+ et un réseau de leaders pour faire du monde un espace d'apprentissage.</p>
      <a class="btn btn--accent" href="international.html">Notre ouverture internationale {I["arrow"]}</a>
      <p class="small mt-1 mb-0">* Présence revendiquée par la communauté Academy Twenty One.</p>
    </div>
    <ul class="stats reveal">
      <li><strong>5</strong><span>continents</span></li>
      <li><strong>75+</strong><span>pays</span></li>
      <li><strong>8</strong><span>formats d'expérience internationale</span></li>
      <li><strong>1</strong><span>réseau mondial : A21 Global Network</span></li>
    </ul>
  </div>
</section>

<section class="section section--surface" aria-labelledby="ent-title">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Entreprises &amp; organisations</p>
      <h2 id="ent-title">Faites grandir vos managers et vos dirigeants</h2>
      <p class="lead">Alternance, formation continue, Executive Education ou session IA pour vos équipes : construisons le dispositif adapté à vos enjeux.</p>
      <div class="btn-row"><a class="btn btn--navy" href="entreprises.html">Espace entreprises {I["arrow"]}</a><a class="link-arrow" href="contact.html?objet=entreprise">Nous écrire {I["arrow"]}</a></div>
    </div>
    <div class="grid grid--2 reveal-stagger">
      <div class="card card--glass"><span class="icon-badge icon-badge--blue">{I["graduation"]}</span><h3>Alternance</h3><p class="small">Mastère en alternance lorsque le cadre conventionnel le permet.</p></div>
      <div class="card card--glass"><span class="icon-badge">{I["leader"]}</span><h3>Dirigeants</h3><p class="small">Executive MBA et Executive Impact Project sur un enjeu réel.</p></div>
      <div class="card card--glass"><span class="icon-badge icon-badge--yellow">{I["users"]}</span><h3>Managers</h3><p class="small">Bachelor et Mastère en formation continue.</p></div>
      <div class="card card--glass"><span class="icon-badge icon-badge--green">{I["cpu"]}</span><h3>IA appliquée</h3><p class="small">20 h pour intégrer l'IA à la prospection et au développement.</p></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="adm-title">
  <div class="container">
    <div class="section-head section-head--row reveal">
      <div><p class="eyebrow">Admissions</p><h2 id="adm-title">Une admission sélective, un accompagnement personnalisé</h2></div>
      <a class="link-arrow" href="admissions.html">Conditions d'accès détaillées {I["arrow"]}</a>
    </div>
    <ol class="steps reveal-stagger">
      <li><h3>Candidature en ligne</h3><p>Formulaire guidé en 5 étapes, brouillon enregistré automatiquement.</p></li>
      <li><h3>Étude du dossier</h3><p>Analyse de vos acquis académiques et professionnels.</p></li>
      <li><h3>Entretien</h3><p>Entretien de positionnement, ou entretien Executive pour l'EMBA.</p></li>
      <li><h3>Décision</h3><p>Décision de la commission d'admission et inscription.</p></li>
    </ol>
    <div class="split split--top mt-3">
      <div class="reveal"><h3>Questions fréquentes</h3><p class="text-muted">Les réponses aux questions les plus posées par les candidats.</p><a class="link-arrow" href="admissions.html#faq">Toutes les questions {I["arrow"]}</a></div>
      <div class="accordion reveal">{faq_html}</div>
    </div>
  </div>
</section>

{cta_band("Votre prochaine responsabilité commence ici", "Choisissez le programme adapté à votre niveau, votre expérience et votre ambition, puis déposez votre candidature en ligne.", secondary=f'<a class="btn btn--glass" href="brochures.html">{I["download"]} Brochures</a>')}
'''
    page("index.html", "Academy 21 University — Former ceux qui dirigeront demain",
         "Academy Twenty One University : Bachelor, Mastère, Executive MBA et formation IA en management, entrepreneuriat et leadership.", body)


def build_pedagogie():
    tabs = [("bachelor", "Bachelor", "Une pédagogie professionnalisante",
             "Le Bachelor privilégie les situations professionnelles plutôt qu'une accumulation de cours théoriques. Chaque séquence conduit à une production : diagnostic, tableau de bord, budget, plan commercial, planning, dossier de recrutement, plan d'action ou projet de transformation.",
             ["Cas d'entreprise", "Business games", "Simulations managériales", "Ateliers Excel &amp; KPI", "Jeux de rôle", "Projet fil rouge", "Soutenances professionnelles"],
             "Évaluation progressive : études de cas, travaux chiffrés, mises en situation, projets et soutenances, puis préparation finale aux exigences de la certification."),
            ("mastere", "Mastère", "Une pédagogie de grande école, orientée décision",
             "Le M1 consolide les fondamentaux du management stratégique ; le M2 place l'apprenant dans une posture de décision, de direction et de conseil.",
             ["Études de cas stratégiques", "Simulations de comité de direction", "Missions de conseil", "Conférences de dirigeants", "Recherche appliquée &amp; prospective", "Data &amp; IA appliquées", "Grand Oral de leadership"],
             "Études de cas, mises en situation professionnelles, rapports d'activité, productions de conseil, présentations orales et soutenances."),
            ("executive-mba", "Executive MBA", "Une expérience Executive, pas une scolarité classique",
             "Chaque module part d'une problématique de direction et conduit à une décision, un arbitrage ou une feuille de route, systématiquement confrontés aux situations réelles des participants.",
             ["Executive Case Method", "Boardroom Simulations", "CEO &amp; Leaders Series", "Peer Learning", "Executive Coaching", "International &amp; Strategic Immersion", "Executive Impact Project"],
             "Notes de décision, board papers, analyses stratégiques, simulations et soutenance finale devant un jury à dominante professionnelle."),
            ("ia-marketing-reseau", "Formation IA", "Apprendre – tester – produire – améliorer",
             "Chaque séquence alterne apports courts, démonstrations guidées, exercices, analyse critique des résultats produits par l'IA et transposition immédiate dans l'activité.",
             ["Démonstrations en direct", "Cas réels", "Ateliers de prompting", "Jeux de rôle", "Production de contenus", "Workflow final"],
             "Diagnostic initial, évaluation formative, projet fil rouge et présentation finale du dispositif produit.")]
    tl = ""
    for i, (k, n, *_r) in enumerate(tabs):
        sel = "true" if i == 0 else "false"
        ti = "" if i == 0 else ' tabindex="-1"'
        tl += f'<button class="tabs__tab" type="button" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{sel}"{ti}>{n}</button>'
    tp = ""
    for i, (k, n, h, txt, chips, ev) in enumerate(tabs):
        ch = "".join(f"<li>{c}</li>" for c in chips)
        tp += f'''<div class="tabs__panel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}" tabindex="0"{"" if i == 0 else " hidden"}>
  <div class="card"><div class="split split--top" style="gap:2rem">
    <div><h3>{h}</h3><p>{txt}</p><ul class="chips">{ch}</ul></div>
    <div class="card card--surface"><span class="num">Évaluation</span><p>{ev}</p><a class="link-arrow" href="{P[k]["href"]}">Voir le programme {I["arrow"]}</a></div>
  </div></div></div>'''
    body = f'''
{hero_light([("pedagogie.html", "Pédagogie")], "Une pédagogie <span class='serif'>orientée décision</span>",
  "Analyser, arbitrer, produire, défendre : chaque séquence part d'une situation réelle.", "Pédagogie &amp; modalités",
  visual=photo_img("projet", "Une équipe d'apprenants aux profils variés travaille ensemble sur un ordinateur", "55% 40%"), amb="green", shape="galet")}

<section class="section" aria-labelledby="pr-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Nos principes</p><h2 id="pr-title">Quatre principes qui guident chaque séquence</h2></div>
    <div class="grid grid--4 reveal-stagger">
      <article class="card card--hover"><span class="icon-badge">{I["target"]}</span><span class="num">01</span><h3>Partir du réel</h3><p>Chaque module part d'une problématique professionnelle concrète.</p></article>
      <article class="card card--hover"><span class="icon-badge icon-badge--blue">{I["file"]}</span><span class="num">02</span><h3>Produire</h3><p>Chaque séquence débouche sur un livrable : diagnostic, budget, plan, feuille de route.</p></article>
      <article class="card card--hover"><span class="icon-badge icon-badge--yellow">{I["presentation"]}</span><span class="num">03</span><h3>Décider &amp; défendre</h3><p>Soutenances, Grand Oral, Board Presentation : vous argumentez vos choix.</p></article>
      <article class="card card--hover"><span class="icon-badge icon-badge--green">{I["users"]}</span><span class="num">04</span><h3>Apprendre des autres</h3><p>Peer learning, conférences de dirigeants, coaching et travaux collectifs.</p></article>
    </div>
  </div>
</section>

<section class="section section--mesh" aria-labelledby="meth-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Méthodes</p><h2 id="meth-title">Les méthodes de chaque programme</h2></div>
    <div data-tabs class="reveal">
      <div class="tabs__list" role="tablist" aria-label="Programmes">{tl}</div>
      {tp}
    </div>
  </div>
</section>

<section class="section section--navy on-dark" aria-labelledby="ia-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container split" style="position:relative">
    <div class="reveal">
      <p class="eyebrow">Data &amp; intelligence artificielle</p>
      <h2 id="ia-title">L'IA au cœur de chaque parcours</h2>
      <p>De l'IA générative au service de la décision jusqu'à la gouvernance technologique : l'intelligence artificielle est enseignée à chaque niveau, comme un levier de management et de transformation.</p>
      <a class="btn btn--accent" href="ia-marketing-reseau.html">Découvrir la formation IA {I["arrow"]}</a>
    </div>
    <ul class="stats reveal">
      <li><strong>28 h</strong><span>Bachelor — Digital, data &amp; intelligence artificielle</span></li>
      <li><strong>80 h</strong><span>Mastère — Transformation digitale (M1) et IA stratégique (M2)</span></li>
      <li><strong>35 h</strong><span>Executive MBA — Transformation, AI &amp; Digital Strategy</span></li>
      <li><strong>20 h</strong><span>Formation courte — IA appliquée au marketing de réseau</span></li>
    </ul>
  </div>
</section>

<section class="section" id="modalites" aria-labelledby="mo-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Modalités</p><h2 id="mo-title">Présentiel, distanciel ou hybride</h2>
      <p class="lead">Le Bachelor, le Mastère et l'Executive MBA peuvent être suivis selon trois modalités. Le calendrier et la répartition des séquences sont communiqués à chaque session.</p></div>
    <div class="grid grid--3 reveal-stagger">
      <article class="card card--hover card--accent-top"><span class="icon-badge">{I["building"]}</span><h3>Présentiel</h3><p>Cours, ateliers, études de cas, simulations managériales, travaux en groupe, soutenances, coaching et Board sessions.</p></article>
      <article class="card card--hover card--accent-top"><span class="icon-badge icon-badge--blue">{I["monitor"]}</span><h3>Distanciel synchrone</h3><p>Classes virtuelles en direct, conférences, ressources numériques, travaux dirigés et activités collaboratives.</p></article>
      <article class="card card--hover card--accent-top"><span class="icon-badge icon-badge--yellow">{I["layers"]}</span><h3>Hybride</h3><p>Une organisation qui combine les deux modalités, pour concilier formation et activité professionnelle.</p></article>
    </div>
    <div class="mt-3 reveal">{table("Rythmes par programme", ["Programme", "Durée", "Rythme", "Expérience professionnelle"],
      [["<a href='bachelor.html'>Bachelor</a>", "420 h", "Présentiel, distanciel ou hybride", "Période en entreprise d'au moins 350 h pour le candidat présenté au titre ; intégrée pour l'alternant"],
       ["<a href='mastere.html'>Mastère</a>", "2 ans · 900 h", "Initial, formation continue ou alternance selon convention", "Alternance, stage long, mission professionnelle ou activité salariée compatible"],
       ["<a href='executive-mba.html'>Executive MBA</a>", "12 mois · 360 h", "Blocs intensifs, week-ends Executive, séminaires et intersessions", "Executive Impact Project sur une problématique réelle de direction"],
       ["<a href='ia-marketing-reseau.html'>Formation IA</a>", "20 h", "5 séances de 4 h en distanciel synchrone", "Transposition immédiate dans votre activité"]], vol_col=None)}</div>
  </div>
</section>
{cta_band("Envie de vivre cette pédagogie ?", "Choisissez votre programme et déposez votre candidature en ligne.")}
'''
    page("pedagogie.html", "Pédagogie & modalités — Academy 21 University", "Méthodes pédagogiques, évaluation et modalités présentiel, distanciel et hybride d'Academy 21 University.", body)


def build_entreprises():
    body = f'''
{hero_light([("entreprises.html", "Entreprises")], "Faites grandir vos <span class='serif'>managers</span> et vos dirigeants",
  "Alternance, formation continue, Executive Education ou IA : un dispositif adapté à vos enjeux.", "Entreprises &amp; organisations",
  f'<div class="btn-row"><a class="btn btn--primary" href="contact.html?objet=entreprise">Échanger avec nous {I["arrow"]}</a><a class="btn btn--ghost" href="brochures.html">{I["download"]} Brochures</a></div>',
  visual=photo_img("echange", "Une équipe internationale échange autour d'un ordinateur", "50% 40%"), amb="gold", shape="arche")}

<section class="section" aria-labelledby="off-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Nos solutions</p><h2 id="off-title">Quatre façons de travailler ensemble</h2></div>
    <div class="grid grid--2 reveal-stagger">
      <article class="card card--hover"><span class="icon-badge icon-badge--blue">{I["graduation"]}</span><h3>Recruter un alternant</h3><p>Le Mastère Stratégie, Leadership &amp; Transformation peut être suivi en alternance lorsque le cadre conventionnel le permet. Pour l'alternant du Bachelor, la période en entreprise est intégrée au temps de travail.</p><a class="link-arrow card__link" href="mastere.html">Le Mastère {I["arrow"]}</a></article>
      <article class="card card--hover"><span class="icon-badge icon-badge--yellow">{I["users"]}</span><h3>Former vos managers</h3><p>Bachelor (Bac+3) pour les managers de centre de profit, Mastère (Bac+5) pour les cadres qui conduisent la transformation — en formation continue, à distance ou en hybride.</p><a class="link-arrow card__link" href="formations.html">Comparer les formations {I["arrow"]}</a></article>
      <article class="card card--hover"><span class="icon-badge">{I["leader"]}</span><h3>Accompagner vos dirigeants</h3><p>L'Executive MBA s'adresse aux dirigeants, membres de CODIR et cadres supérieurs. Organisation compatible avec la vie d'un dirigeant : blocs intensifs, week-ends et séminaires.</p><a class="link-arrow card__link" href="executive-mba.html">L'Executive MBA {I["arrow"]}</a></article>
      <article class="card card--hover"><span class="icon-badge icon-badge--green">{I["cpu"]}</span><h3>Intégrer l'IA dans vos équipes</h3><p>20 heures en distanciel synchrone, en groupe de 8 à 15 participants, pour intégrer l'IA à la prospection, la communication et le pilotage commercial.</p><a class="link-arrow card__link" href="ia-marketing-reseau.html">La formation IA {I["arrow"]}</a></article>
    </div>
  </div>
</section>

<section class="section section--navy on-dark" aria-labelledby="val-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container" style="position:relative">
    <div class="section-head reveal"><p class="eyebrow">Ce que votre organisation y gagne</p><h2 id="val-title">Des travaux directement exploitables</h2>
      <p class="lead">Nos apprenants travaillent sur des problématiques réelles : leurs productions servent votre organisation pendant la formation.</p></div>
    <div class="grid grid--3 reveal-stagger">
      <article class="card card--glass-dark"><span class="icon-badge icon-badge--navy">{I["presentation"]}</span><h3>Executive Impact Project</h3><p>Diagnostic, options, scénarios, arbitrages, impacts financiers et humains, risques, gouvernance et plan de mise en œuvre — défendus devant un Board.</p></article>
      <article class="card card--glass-dark"><span class="icon-badge icon-badge--navy">{I["briefcase"]}</span><h3>Mission de transformation</h3><p>En M2 du Mastère : conseil en organisation, mission de transformation et Consulting Project II.</p></article>
      <article class="card card--glass-dark"><span class="icon-badge icon-badge--navy">{I["chart"]}</span><h3>Pilotage opérationnel</h3><p>Au Bachelor : budgets, tableaux de bord, plans commerciaux et plans d'action sur votre activité.</p></article>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="how-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Démarche</p><h2 id="how-title">Comment nous travaillons avec vous</h2></div>
    <ol class="steps reveal-stagger">
      <li><h3>Premier échange</h3><p>Vos enjeux, les profils concernés et votre calendrier.</p></li>
      <li><h3>Proposition</h3><p>Programme, modalité et rythme adaptés à votre organisation.</p></li>
      <li><h3>Admission</h3><p>Étude des dossiers et entretiens des collaborateurs.</p></li>
      <li><h3>Suivi</h3><p>Un interlocuteur dédié tout au long du parcours.</p></li>
    </ol>
  </div>
</section>
{cta_band("Parlons de vos besoins", "Décrivez-nous votre projet : nous revenons vers vous avec une proposition adaptée.",
  secondary=f'<a class="btn btn--glass" href="mailto:{CONTACT_EMAIL}">{I["mail"]} Écrire un e-mail</a>').replace('href="candidature.html"', 'href="contact.html?objet=entreprise"').replace("Déposer ma candidature", "Contacter l'équipe")}
'''
    page("entreprises.html", "Entreprises — Academy 21 University", "Alternance, formation continue, Executive Education et formation IA pour les entreprises et organisations.", body)


def seg(name, opts):
    return "".join(f'<input type="radio" id="{name}-{v}" name="{name}" value="{v}"{" checked" if i == 0 else ""}><label for="{name}-{v}">{l}</label>'
                   for i, (v, l) in enumerate(opts))


def build_formations():
    body = f'''
{hero_light([("formations.html", "Formations")], "Nos <span class='serif'>formations</span>",
  "Quatre programmes, du pilotage d'une activité à la direction générale.", "Catalogue", amb="red")}
<section class="section section--flush-top" aria-labelledby="cat-title">
  <div class="container">
    <h2 id="cat-title" class="visually-hidden">Catalogue filtrable</h2>
    <form class="filters" data-filters aria-label="Filtrer les formations">
      <fieldset><legend>Niveau</legend><div class="seg">{seg("niveau", [("all", "Tous"), ("bac3", "Bac+3"), ("bac5", "Bac+5"), ("executive", "Executive"), ("courte", "Formation courte")])}</div></fieldset>
      <fieldset><legend>Modalité</legend><div class="seg">{seg("modalite", [("all", "Toutes"), ("presentiel", "Présentiel"), ("distanciel", "Distanciel"), ("hybride", "Hybride")])}</div></fieldset>
    </form>
    <p class="results-count" id="results-count" role="status" aria-live="polite"></p>
    <div class="grid grid--2">{"".join(program_card(p["key"], "h3") for p in PROGRAMS)}</div>
  </div>
</section>
<section class="section section--surface" aria-labelledby="cmp-title">
  <div class="container">
    <div class="section-head section-head--row reveal"><div><p class="eyebrow">Comparatif</p><h2 id="cmp-title">Quel programme pour quel profil ?</h2></div>
      <a class="link-arrow" href="brochures.html">Toutes les brochures {I["download"]}</a></div>
    <div class="reveal">{table("Comparatif des formations Academy 21 University",
      ["Formation", "Niveau", "Durée / volume", "Public &amp; accès", "Reconnaissance"],
      [["<a href='bachelor.html'>Bachelor Management Stratégique &amp; Opérationnel</a>", "Bac+3 · Niveau 6", "420 h", "Bac+2, ou 5 ans d'expérience significative", "Prépare au Titre professionnel RNCP38666"],
       ["<a href='mastere.html'>Mastère Stratégie, Leadership &amp; Transformation</a>", "Bac+5 · Niveau 7", "2 ans · 900 h", "Bac+3, ou Bac+2 + 3 ans en management", "Conçu en cohérence avec le RNCP39994*"],
       ["<a href='executive-mba.html'>Executive MBA Gouvernance, Leadership &amp; Transformation</a>", "Executive", "12 mois · 360 h + projet", "Dirigeants, 7 ans d'expérience minimum", "Diplôme d'établissement"],
       ["<a href='ia-marketing-reseau.html'>IA appliquée au Marketing de Réseau</a>", "Formation courte", "20 h · 5 séances", "Professionnels du marketing de réseau", "Attestation de formation"]], vol_col=None)}</div>
    <p class="small text-muted mt-1">* La présentation effective à la certification suppose le cadre conventionnel et l'inscription auprès du certificateur.</p>
  </div>
</section>
{cta_band("Vous hésitez entre deux programmes ?", "Le formulaire de candidature vous indique la voie d'accès correspondant à votre profil. Une question ? Écrivez-nous.")}
'''
    page("formations.html", "Formations — Academy 21 University", "Catalogue des formations Academy 21 University : Bachelor, Mastère, Executive MBA, formation IA.", body)


def build_brochures():
    cards = ""
    for p in PROGRAMS:
        k = p["key"]
        pdf, name = BROCHURES[k]
        cards += f'''<article class="card card--hover doc-card">
  <div class="doc-card__thumb" aria-hidden="true">PDF</div>
  <div>
    <p class="program-card__type">{p["type"]} · {p["level_big"]}</p>
    <h3 style="font-size:1.15rem">{name}</h3>
    <p class="doc-card__meta">{pdf_size(k)} · Programme, admission, modalités, débouchés</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--sm" href="{pdf}" download>{I["download"]} Télécharger <span class="visually-hidden">la brochure {name}</span></a>
      <a class="btn btn--ghost btn--sm" href="{p["href"]}">Voir la fiche <span class="visually-hidden">{name}</span></a>
    </div>
  </div>
</article>'''
    inst = ""
    for k, desc, href, label in [("institution", "Identité, mission, valeurs, modèle académique, gouvernance, ambition 2030+", "ecole.html", "Voir L'école"),
                                 ("international", "A21 Global Network, stratégie Erasmus+, mobilités, feuille de route internationale", "international.html", "Voir International")]:
        pdf, name = BROCHURES[k]
        inst += f'''<article class="card card--hover doc-card">
  <div class="doc-card__thumb" aria-hidden="true">PDF</div>
  <div>
    <p class="program-card__type">A21 University · Institution</p>
    <h3 style="font-size:1.15rem">{name}</h3>
    <p class="doc-card__meta">{pdf_size(k)} · {desc}</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--sm" href="{pdf}" download>{I["download"]} Télécharger <span class="visually-hidden">{name}</span></a>
      <a class="btn btn--ghost btn--sm" href="{href}">{label}</a>
    </div>
  </div>
</article>'''
    body = f'''
{hero_light([("brochures.html", "Brochures")], "Brochures &amp; <span class='serif'>documentation</span>",
  "Programmes, présentation institutionnelle et ouverture internationale, en PDF.", "Documentation", amb="blue")}
<section class="section" aria-labelledby="doc-prog-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Programmes</p><h2 id="doc-prog-title">Brochures des formations</h2></div>
    <div class="grid grid--2 reveal-stagger">{cards}</div>
    <div class="section-head reveal mt-3"><p class="eyebrow">Institution</p><h2 id="doc-inst-title">Documents institutionnels</h2></div>
    <div class="grid grid--2 reveal-stagger" aria-labelledby="doc-inst-title">{inst}</div>
    <div class="mt-3 reveal">{notice("<p>Les brochures sont au format PDF. Si vous avez besoin d'un document dans un autre format accessible, <a href='contact.html?objet=information'>écrivez-nous</a> : nous vous l'adresserons.</p>", "info")}</div>
  </div>
</section>
{cta_band("Votre choix est fait ?", "Déposez votre candidature en ligne : le formulaire prend une dizaine de minutes.")}
'''
    page("brochures.html", "Brochures — Academy 21 University", "Téléchargez les brochures PDF du Bachelor, du Mastère, de l'Executive MBA et de la formation IA.", body)
