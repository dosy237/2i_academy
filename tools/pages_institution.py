# Pages institutionnelles issues de la présentation institutionnelle et du document Global Engagement :
# L'école (identité, raison d'être, fondateur, valeurs, modèle, expérience, gouvernance, ambition) et International.
from components import hero_light, hero_editorial, hero_visual, hero_minimal, photo_img, GLOBE_SVG, I, BROCHURES, pdf_size, ring, page, cta_band, simple_hero, notice, founder_block


def build_ecole():
    mvap = [("target", "", "Mission", "Former des managers, entrepreneurs et leaders capables de conjuguer maîtrise professionnelle, intelligence stratégique, leadership responsable et capacité de transformation."),
            ("eye", "icon-badge--blue", "Vision", "Faire d'A21 University une institution internationale de référence dans la formation au management et au leadership, reconnue pour la qualité de ses diplômés, l'impact de ses programmes et son ouverture sur le monde."),
            ("rocket", "icon-badge--yellow", "Ambition", "Construire progressivement une business school internationale forte, professionnalisante et sélective dans ses standards, du Bac au Bac+5 et en Executive Education."),
            ("handshake", "icon-badge--green", "Promesse", "Donner à chaque apprenant les savoirs, les méthodes, les expériences et la posture nécessaires pour passer de l'ambition à la responsabilité.")]
    mvap_html = "".join(f'<article class="card card--hover card--accent-top"><span class="icon-badge {c}">{I[i]}</span><h3>{t}</h3><p>{d}</p></article>' for i, c, t, d in mvap)
    values = [("Excellence", "Élever continuellement les standards de travail, de connaissance, de service et de performance."),
              ("Intégrité", "Agir avec cohérence, loyauté, honnêteté intellectuelle et responsabilité."),
              ("Discipline", "Transformer l'ambition en résultats par la constance, la rigueur et le respect des engagements."),
              ("Audace", "Questionner, entreprendre, innover et décider même lorsque l'environnement est incertain."),
              ("Ouverture", "Comprendre les cultures, les marchés, les idées et les différences avant de prétendre exercer une influence."),
              ("Service", "Considérer le leadership comme une responsabilité envers les équipes, les organisations et la société."),
              ("Impact", "Mesurer la réussite à la valeur créée et aux transformations rendues possibles."),
              ("Persévérance", "Construire dans la durée, apprendre des difficultés et ne pas renoncer à l'exigence.")]
    values_html = "".join(f'<article class="card card--hover"><span class="num">0{i + 1}</span><h3>{t}</h3><p class="small mb-0">{d}</p></article>' for i, (t, d) in enumerate(values))
    levels = [("Bachelor · Bac+3", "Manager", "Comprendre l'entreprise, piloter une activité, développer la performance et manager une équipe.", "bachelor.html"),
              ("Mastère · Bac+5", "Strategic Leader", "Définir des orientations, conduire des transformations et piloter la performance globale.", "mastere.html"),
              ("MBA · Niveau 7", "Business Leader", "Renforcer la maîtrise de la stratégie, de la finance, de la croissance et de la direction d'entreprise.", None),
              ("Executive MBA", "Executive Leader", "Gouverner, arbitrer, transformer et exercer la responsabilité globale du dirigeant.", "executive-mba.html"),
              ("Executive Education", "Lifelong Leader", "Actualiser les compétences des cadres et dirigeants tout au long de leur trajectoire professionnelle.", "ia-marketing-reseau.html")]
    lv = ""
    for tag, role, txt, href in levels:
        inner = f'<span class="num">{tag}</span><h3>{role}</h3><p>{txt}</p>'
        if href:
            lv += f'<a class="card card--glass-dark" href="{href}" style="text-decoration:none">{inner}</a>'
        else:
            lv += f'<div class="card card--glass-dark">{inner}<span class="pathway__soon" style="align-self:flex-start">Programme en préparation</span></div>'
    fields = [("Stratégie &amp; Gouvernance", "Diagnostic, prospective, décision, gouvernance, intelligence économique."),
              ("Finance &amp; Performance", "Finance, contrôle, création de valeur, investissement, pilotage et risques."),
              ("Marketing &amp; Développement", "Marketing, vente, marque, expérience client, business development."),
              ("Leadership &amp; Management", "Comportement organisationnel, équipes, influence, négociation, communication."),
              ("Entrepreneuriat &amp; Innovation", "Création, reprise, business models, innovation et venture building."),
              ("Digital, Data &amp; IA", "Transformation numérique, intelligence artificielle, data-driven management."),
              ("RSE &amp; Transitions", "Responsabilité, ESG, transition écologique, éthique et impact."),
              ("International Business", "Géoéconomie, interculturel, marchés internationaux, alliances et expansion.")]
    fields_html = "".join(f'<li><b>{t.upper()}</b><span>{d}</span></li>' for t, d in fields)
    exp = [("leader", "", "Leadership Lab", "Ateliers de posture, prise de parole, négociation, décision et intelligence relationnelle."),
           ("briefcase", "icon-badge--blue", "Career Center", "CV, employabilité, stages, alternance et relations entreprises."),
           ("rocket", "icon-badge--yellow", "Entrepreneurship Hub", "Incubation, mentorat, business plan, pitch, financement et accompagnement des projets."),
           ("globe", "icon-badge--green", "Global Experience", "Mobilités, International Weeks, study trips, équipes multiculturelles et conférences internationales."),
           ("mic", "", "A21 Talks", "Rencontres avec dirigeants, entrepreneurs, intellectuels, experts et personnalités inspirantes."),
           ("users", "icon-badge--blue", "Community &amp; Alumni", "Vie associative, réseau des diplômés, mentorat intergénérationnel et opportunités professionnelles.")]
    exp_html = "".join(f'<article class="card card--hover"><span class="icon-badge {c}">{I[i]}</span><h3>{t}</h3><p>{d}</p></article>' for i, c, t, d in exp)
    roadmap = [("Consolider", "Installer des programmes robustes du Bac au Bac+5, une Executive Education cohérente et des standards de qualité exigeants."),
               ("Internationaliser", "Développer les partenariats académiques, la mobilité, les programmes bilingues, les professeurs invités et le recrutement international."),
               ("Professionnaliser", "Faire de l'employabilité, de l'alternance, de l'entrepreneuriat et des relations entreprises des marqueurs forts de l'école."),
               ("Produire", "Développer études, publications, cas pédagogiques, observatoires et travaux appliqués sur le leadership et les transformations."),
               ("Rayonner", "Créer des événements académiques et économiques, développer une communauté Alumni et faire entendre une voix A21 sur le management contemporain."),
               ("Reconnaître &amp; être reconnu", "Inscrire progressivement l'institution et ses programmes dans les cadres de qualité, de certification et de reconnaissance pertinents, en France et à l'international.")]
    road_html = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in roadmap)

    dl_inst = f'<a class="btn btn--glass" href="{BROCHURES["institution"][0]}" download>{I["download"]} Présentation institutionnelle ({pdf_size("institution")})</a>'
    body = f'''
{hero_editorial([("ecole.html", "L'école")], "Academy Twenty One <span class='serif'>University</span>",
  "Une école de management, de leadership et d'entrepreneuriat, tournée vers le monde et l'entreprise.", '<span lang="en">Institutional profile</span>', "livres",
  '<div class="btn-row">' + dl_inst + f'<a class="btn btn--accent" href="#fondateur">Le fondateur {I["arrow"]}</a></div>', amb="gold")}

<section class="section" aria-labelledby="id-title">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">01 · Notre identité</p>
      <h2 id="id-title">Former celles et ceux appelés à manager, entreprendre, décider et diriger</h2>
      <p class="lead">A21 University est pensée comme un établissement d'enseignement supérieur de plein exercice, construit autour des sciences du management, du leadership, de l'entrepreneuriat et de la transformation des organisations.</p>
      <p>Son projet ne consiste pas à juxtaposer des formations : il vise à bâtir une institution cohérente, dotée d'une culture, d'une pédagogie, d'une communauté et d'une signature académique propres.</p>
      <p class="quote">Former des diplômés capables de comprendre avant de décider, de décider avant d'agir, et d'agir en mesurant les conséquences de leurs choix.</p>
    </div>
    <div class="visual-panel on-dark reveal">
      {ring("deco", uid="ida")}
      <p class="motto">Une histoire qui devient une institution</p>
      <ul class="stats">
        <li><strong>5</strong><span>continents où la communauté Academy Twenty One est présente*</span></li>
        <li><strong>75+</strong><span>pays revendiqués par ses membres*</span></li>
      </ul>
      <p class="small mt-1 mb-0">Academy Twenty One dispose d'un héritage international dans la formation, le développement du leadership et l'accompagnement de communautés professionnelles. A21 University lui donne une traduction académique plus large et structurée.</p>
    </div>
  </div>
</section>

<section class="section section--mesh" aria-labelledby="raison-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">02 · Notre raison d'être</p><h2 id="raison-title">Mission, vision, ambition, promesse</h2></div>
    <div class="mvap reveal-stagger">{mvap_html}</div>
  </div>
</section>

<section class="section" id="fondateur" aria-label="Le fondateur">
  <div class="container">
    {founder_block("h2", "https://academytwentyone.com/", "Découvrir Academy Twenty One", gallery=True)}
  </div>
</section>

<section class="section section--surface" id="valeurs" aria-labelledby="val-title">
  <div class="container">
    <div class="section-head section-head--center reveal"><p class="eyebrow">03 · Notre ADN</p><h2 id="val-title">Nos 8 valeurs</h2>
      <p class="lead">Elles orientent la sélection, la pédagogie, la relation avec les entreprises, le comportement des apprenants et le développement de l'institution.</p></div>
    <div class="values reveal-stagger">{values_html}</div>
  </div>
</section>

<section class="section section--navy on-dark" aria-labelledby="mod-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container" style="position:relative">
    <div class="section-head reveal"><p class="eyebrow">04 · Notre modèle académique</p><h2 id="mod-title">Une progression de responsabilités</h2>
      <p class="lead">Chaque niveau prépare au suivant tout en conservant une valeur professionnelle propre.</p></div>
    <div class="grid grid--3 reveal-stagger">{lv}</div>
  </div>
</section>

<section class="section" aria-labelledby="champs-title">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">Nos grands champs d'enseignement</p>
      <h2 id="champs-title">Huit domaines pour former des décideurs complets</h2>
      <p>Notre modèle associe l'exigence académique à la réalité de l'entreprise, la compétence technique à la qualité du leadership, et l'ambition individuelle à la responsabilité collective.</p>
      <a class="btn btn--navy" href="pedagogie.html">Notre pédagogie : apprendre par la décision {I["arrow"]}</a>
    </div>
    <ul class="bloc-list reveal">{fields_html}</ul>
  </div>
</section>

<section class="section section--mesh" aria-labelledby="exp-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">05 · L'expérience A21 University</p><h2 id="exp-title">Ce qui se passe aussi en dehors du cours</h2>
      <p class="lead">Une expérience que nous construisons pour développer la compétence, la culture générale, la confiance, le réseau professionnel et le sens des responsabilités.</p></div>
    <div class="grid grid--3 reveal-stagger">{exp_html}</div>
  </div>
</section>

<section class="section" aria-labelledby="resp-title">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">06 · Leadership responsable &amp; impact</p>
      <h2 id="resp-title">Former des personnes capables d'assumer davantage de responsabilité</h2>
      <p>Former des leaders ne signifie pas former des individus à exercer davantage de pouvoir. Pour A21 University, le leadership se mesure à la qualité des décisions, à la confiance créée, aux talents développés et à la valeur durable produite.</p>
      <p>La RSE, l'éthique des affaires, la diversité, l'inclusion, la soutenabilité et l'impact traversent progressivement l'ensemble des programmes.</p>
      <h3 class="mt-2">Une institution connectée à l'entreprise</h3>
      <p>Les entreprises participent à la définition des compétences, interviennent dans les enseignements, proposent des cas, accueillent des apprenants, contribuent aux jurys et recrutent les diplômés.</p>
      <a class="link-arrow" href="entreprises.html">Espace entreprises {I["arrow"]}</a>
    </div>
    <div class="reveal">
      <h3>Gouvernance &amp; exigence institutionnelle</h3>
      <ul class="bloc-list">
        <li><b>PRÉSIDENCE</b><span>Porte la vision, l'identité, les orientations stratégiques et le rayonnement de l'institution.</span></li>
        <li><b>DIRECTION</b><span>Conduit le développement académique, la qualité, les programmes, les partenariats et la professionnalisation.</span></li>
        <li><b>ACADEMIC BOARD</b><span>Réunit progressivement enseignants, chercheurs, professionnels et personnalités qualifiées pour garantir la pertinence académique.</span></li>
        <li><b>INTERNATIONAL ADVISORY BOARD</b><span>Accompagne l'ouverture internationale, les partenariats et la lecture des grandes transformations mondiales.</span></li>
        <li><b>CORPORATE COUNCIL</b><span>Fait dialoguer l'école avec les entreprises sur les compétences, les métiers et l'employabilité.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="amb-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">07 · Notre ambition 2030+</p><h2 id="amb-title">Une ambition qui repose sur une trajectoire</h2>
      <p class="lead">Faire émerger A21 University comme une marque académique internationale crédible et reconnue.</p></div>
    <ol class="steps steps--3 reveal-stagger">{road_html}</ol>
  </div>
</section>

<section class="section section--navy on-dark" aria-labelledby="sig-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container container--narrow text-center" style="position:relative">
    <p class="eyebrow" style="justify-content:center">08 · Notre signature</p>
    <h2 id="sig-title">Learn. Lead. Transform.</h2>
    <p class="lead">Des diplômés qui se distinguent moins par ce qu'ils affirment que par ce qu'ils savent faire : analyser avec rigueur, décider avec courage, communiquer avec clarté, agir avec méthode, diriger avec respect et transformer avec responsabilité.</p>
    <p>Une école où l'ambition n'est jamais séparée de l'effort ; où le leadership n'est jamais séparé de l'éthique ; où l'international n'est jamais réduit à un voyage ; où le diplôme n'est jamais considéré comme une fin.</p>
    <p class="quote" style="color:#fff;border-left:0;padding:0;text-align:center">« Former ceux qui dirigeront demain. »</p>
  </div>
</section>

<section class="section" aria-labelledby="eng-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Nos engagements</p><h2 id="eng-title">Exigence, transparence et ouverture</h2></div>
    <div class="grid grid--3 reveal-stagger">
      <article class="card card--hover"><span class="icon-badge">{I["award"]}</span><h3>Transparence sur les certifications</h3><p>Chaque certification est identifiée explicitement : numéro RNCP, certificateur et cadre d'habilitation. Nos diplômes d'établissement sont présentés comme tels.</p><a class="link-arrow card__link" href="admissions.html#certifications">En savoir plus {I["arrow"]}</a></article>
      <article class="card card--hover"><span class="icon-badge icon-badge--blue">{I["handshake"]}</span><h3>Partenaires habilités</h3><p>Le Bachelor est conduit en partenariat avec GREEN UP ACADEMY, partenaire habilité pour la préparation et la présentation au Titre professionnel RNCP38666.</p><a class="link-arrow card__link" href="bachelor.html#certification">Voir le Bachelor {I["arrow"]}</a></article>
      <article class="card card--hover"><span class="icon-badge icon-badge--green">{I["users"]}</span><h3>Inclusion &amp; accessibilité</h3><p>L'inclusion et le handicap font partie de nos enseignements. Toute demande d'aménagement de parcours est étudiée avec attention.</p><a class="link-arrow card__link" href="contact.html?objet=handicap">Nous contacter {I["arrow"]}</a></article>
    </div>
    <div class="mt-3">{notice("<p><strong>* Repères institutionnels.</strong> La présente plateforme s'appuie sur l'héritage public d'Academy Twenty One : présence internationale revendiquée sur cinq continents et plus de 75 pays, culture de formation, de leadership et de développement humain. Les orientations universitaires, la gamme de programmes et les ambitions académiques présentées ici constituent le projet institutionnel d'A21 University.</p>")}</div>
  </div>
</section>
{cta_band("Rejoignez Academy Twenty One University", "Découvrez le programme qui correspond à votre trajectoire et déposez votre candidature en ligne.", secondary=dl_inst)}
'''
    page("ecole.html", "L'école — Academy 21 University", "Identité, mission, fondateur, valeurs, modèle académique et ambition d'Academy Twenty One University.", body)


def build_international():
    network = [("globe", "", "Une communauté mondiale", "L'héritage A21 offre des relais humains, culturels et professionnels dans de nombreuses régions du monde."),
               ("leader", "icon-badge--blue", "Des leaders &amp; entrepreneurs", "Le réseau réunit des profils issus de l'entrepreneuriat, du management, de la formation et du leadership."),
               ("map", "icon-badge--yellow", "Des écosystèmes locaux", "Chaque communauté peut devenir un point d'entrée pour comprendre un marché, une culture et des pratiques professionnelles."),
               ("users", "icon-badge--green", "Une capacité de mobilisation", "Conférences, mentorat, visites d'entreprises, projets, accueils professionnels et événements internationaux."),
               ("graduation", "", "Une future communauté Alumni", "Relier les diplômés au réseau mondial existant et construire un réseau Alumni international.")]
    net_html = "".join(f'<article class="card card--hover"><span class="icon-badge {c}">{I[i]}</span><h3>{t}</h3><p>{d}</p></article>' for i, c, t, d in network)
    zones = [("Europe · Erasmus+", "Mobilités académiques, stages, mobilités des personnels, coopérations interinstitutionnelles et programmes intensifs."),
             ("Afrique", "Partenariats universitaires, mobilité encadrée, projets entrepreneuriaux, études de marchés, conférences et talents."),
             ("Amériques", "Business immersion, entrepreneuriat, innovation, dirigeants invités et coopération professionnelle."),
             ("Asie &amp; Moyen-Orient", "International business, innovation, digital, supply chains, intercultural management et partenariats."),
             ("Réseau global A21", "Mentorat, conférences, relais locaux, rencontres de leaders, projets transfrontaliers et communauté.")]
    zones_html = "".join(f'<li><b>{t.upper()}</b><span>{d}</span></li>' for t, d in zones)
    formats = [("Semester / Study abroad", "Période d'études chez un partenaire, avec reconnaissance des acquis selon les accords applicables."),
               ("Global internship", "Stage ou mission professionnelle à l'étranger, dans une entreprise ou organisation partenaire."),
               ("International Week", "Semaine intensive réunissant enseignants, dirigeants et apprenants de plusieurs pays autour d'un thème commun."),
               ("Global Business Challenge", "Équipes multiculturelles travaillant sur un problème réel d'entreprise et présentant leurs recommandations."),
               ("Study trip", "Immersion courte dans un écosystème économique : entreprises, institutions, incubateurs et universités."),
               ("Virtual exchange", "Cours partagés, projets collaboratifs et classes internationales à distance."),
               ("Visiting professors", "Enseignements et masterclasses assurés par des professeurs et professionnels internationaux."),
               ("Global mentoring", "Mise en relation avec des dirigeants, entrepreneurs ou Alumni du réseau international.")]
    stamp_icons = ["graduation", "briefcase", "calendar", "target", "map", "monitor", "mic", "users"]
    stamp_colors = ["#2f86ab", "#b71c1c", "#3f6e12", "#7a5f2c"]
    formats_html = "".join(
        f'<li class="stamp"><span class="stamp__seal" aria-hidden="true" style="--c:{stamp_colors[n % 4]};--r:{(-8, 5, -3, 7)[n % 4]}deg">{I[stamp_icons[n]]}</span>'
        f'<h3 lang="en">{t}</h3><p>{d}</p></li>' for n, (t, d) in enumerate(formats))
    principles = [("Qualité", "Chaque mobilité répond à des objectifs pédagogiques ou professionnels identifiés."), ("Équité", "Les dispositifs tendent à rendre l'international accessible à des profils divers."),
                  ("Reconnaissance", "Les acquis réalisés chez un partenaire sont encadrés et reconnus selon les conventions applicables."), ("Sécurité", "Évaluation des destinations, information, assurance, contacts d'urgence et suivi des participants."),
                  ("Inclusion", "Attention portée aux besoins particuliers et aux obstacles économiques, sociaux ou liés au handicap."), ("Durabilité", "Pratiques de mobilité plus responsables et intégration des enjeux environnementaux.")]
    pr_html = "".join(f'<article class="card card--glass-dark"><h3>{t}</h3><p>{d}</p></article>' for t, d in principles)
    phases = [("Structurer", "Coordination internationale, politique de mobilité, cartographie du réseau, processus qualité et partenaires prioritaires."),
              ("Europe", "Préparer la démarche ECHE/Erasmus+, signer des accords académiques et développer les premières mobilités encadrées."),
              ("Global Network", "Déployer A21 Global Ambassadors, International Weeks, Visiting Faculty, Global Mentoring et stages internationaux."),
              ("Programmes", "Développer Global Tracks, cours bilingues, programmes conjoints et coopérations pédagogiques transnationales."),
              ("Rayonnement", "Créer un Global Leadership Summit, développer la marque A21 University à l'international et consolider le réseau Alumni."),
              ("Excellence", "Évaluer l'impact, renforcer les standards de qualité et inscrire la stratégie internationale dans les référentiels pertinents.")]
    ph_html = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in phases)
    dl_int = f'<a class="btn btn--glass" href="{BROCHURES["international"][0]}" download>{I["download"]} Document Global Engagement ({pdf_size("international")})</a>'
    body = f'''
{hero_visual([("international.html", "International")], "Une université ouverte sur le <span class='serif'>monde</span>",
  '<span lang="en">From a global community to a global university.</span> Faire du monde un espace d’apprentissage et d’opportunités.', '<span lang="en">Global engagement</span>', GLOBE_SVG,
  f'<ul class="hero-badges"><li class="glass-chip">{I["globe"]}5 continents · 75+ pays*</li><li class="glass-chip">{I["map"]}Ambition Erasmus+</li></ul><div class="btn-row">' + dl_int + '</div>', amb="blue")}

<section class="section" aria-labelledby="coeur-title">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">01 · L'international au cœur du projet</p>
      <h2 id="coeur-title">Une composante de l'expérience académique, pas une option</h2>
      <p class="lead">Apprendre à travailler avec d'autres cultures, comprendre les marchés internationaux, maîtriser les codes professionnels globaux et construire un réseau au-delà des frontières.</p>
      <p>Qu'un apprenant A21 puisse étudier ici tout en étant exposé au monde : travailler avec des pairs d'autres pays, rencontrer des dirigeants internationaux, réaliser une mobilité, développer un projet transfrontalier et rejoindre une communauté Alumni réellement globale.</p>
    </div>
    <div class="visual-panel on-dark reveal">
      {ring("deco", uid="int")}
      <p class="motto">Global mindset. Local impact. Responsible leadership.</p>
      <ul class="stats">
        <li><strong>5</strong><span>continents où la communauté A21 est présente*</span></li>
        <li><strong>75+</strong><span>pays revendiqués par ses membres*</span></li>
        <li><strong>2</strong><span>cercles : l'Europe avec Erasmus+, le monde avec le réseau A21</span></li>
        <li><strong>8</strong><span>formats d'expérience internationale</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--mesh" aria-labelledby="net-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">02 · A21 Global Network</p><h2 id="net-title">Notre avantage distinctif</h2></div>
    <div class="grid grid--3 reveal-stagger">{net_html}</div>
  </div>
</section>

<section class="section" id="erasmus" aria-labelledby="eras-title">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">03 · Notre stratégie Erasmus+</p>
      <h2 id="eras-title">L'Europe, premier espace structuré de mobilité</h2>
      <p>L'ambition est d'engager l'établissement dans la démarche permettant de participer pleinement au programme Erasmus+ pour l'enseignement supérieur. La Charte Erasmus pour l'enseignement supérieur (ECHE) en constitue le préalable.</p>
      <ul class="check-list">
        <li>Préparer une Erasmus Policy Statement cohérente avec la stratégie internationale.</li>
        <li>Structurer reconnaissance académique, sélection, accompagnement et suivi des mobilités.</li>
        <li>Identifier des partenaires européens et conclure des accords interinstitutionnels.</li>
        <li>Développer la mobilité d'études et de stages des apprenants.</li>
        <li>Encourager la mobilité d'enseignement et de formation des personnels.</li>
        <li>Participer à terme à des Blended Intensive Programmes et projets de coopération.</li>
      </ul>
      {notice("<p><strong>Transparence.</strong> A21 University inscrit l'obtention de la Charte ECHE dans sa feuille de route institutionnelle ; elle ne la détient pas à ce jour. Toute communication distingue l'ambition Erasmus+ d'une participation ou d'une charte effectivement obtenue.</p>")}
    </div>
    <div class="reveal">
      <h3>04 · Erasmus+… et au-delà de l'Europe</h3>
      <p>Deux cercles complémentaires : un espace européen structuré par Erasmus+ et un espace mondial structuré par les partenariats académiques et le réseau A21.</p>
      <figure class="venn mb-2" role="img" aria-label="Deux cercles qui se recoupent : l'Europe avec Erasmus+, et le monde avec le réseau A21 ; l'apprenant A21 se trouve à leur intersection.">
        <svg viewBox="0 0 460 260" aria-hidden="true">
          <circle cx="165" cy="130" r="110" fill="#2f86ab" fill-opacity=".14" stroke="#2f86ab" stroke-width="2"/>
          <circle cx="295" cy="130" r="110" fill="#fccd01" fill-opacity=".18" stroke="#7a5f2c" stroke-width="2" stroke-dasharray="6 6"/>
          <text x="110" y="125" text-anchor="middle" fill="#1e6a8a" font-size="17">Europe</text>
          <text x="110" y="148" text-anchor="middle" fill="#1e6a8a" font-size="13" font-weight="600">Erasmus+</text>
          <text x="352" y="125" text-anchor="middle" fill="#5f4a20" font-size="17">Monde</text>
          <text x="352" y="148" text-anchor="middle" fill="#5f4a20" font-size="13" font-weight="600">Réseau A21</text>
          <circle cx="230" cy="130" r="30" fill="#172033"/>
          <text x="230" y="127" text-anchor="middle" fill="#fff" font-size="11">A21</text>
          <text x="230" y="142" text-anchor="middle" fill="#fff" font-size="9" font-weight="600">apprenant</text>
        </svg>
      </figure>
      <ul class="bloc-list">{zones_html}</ul>
    </div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="xp-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">05 · Pour chaque apprenant</p><h2 id="xp-title">Une expérience internationale, physique ou intégrée au cursus</h2></div>
    <ul class="stamps reveal-stagger">{formats_html}</ul>
  </div>
</section>

<section class="section" aria-labelledby="prog-int-title">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">06 · Internationaliser les programmes</p>
      <h2 id="prog-int-title">Des cursus préparés aux environnements multiculturels</h2>
      <ul class="check-list">
        <li>Modules enseignés en anglais et offre bilingue français-anglais, progressivement.</li>
        <li>International Business, management interculturel, géoéconomie et négociation internationale.</li>
        <li>Cas d'entreprises provenant de plusieurs continents.</li>
        <li>Équipes projet multiculturelles, y compris à distance.</li>
        <li>Dirigeants et experts du réseau international associés aux jurys et masterclasses.</li>
        <li>Parcours ou certificats « Global Track » dans les Bachelor, Mastère, MBA et Executive MBA.</li>
      </ul>
    </div>
    <div class="reveal">
      <p class="eyebrow">07 · International Faculty &amp; Visiting Leaders</p>
      <ul class="bloc-list">
        <li><b>VISITING PROFESSOR</b><span>Intervention académique intensive, séminaire, cours spécialisé ou contribution à un projet.</span></li>
        <li><b>EXECUTIVE IN RESIDENCE</b><span>Dirigeant accueilli pour partager son expérience, conseiller des projets et dialoguer avec les apprenants.</span></li>
        <li><b>GLOBAL SPEAKER</b><span>Personnalité internationale invitée dans le cadre des A21 Talks.</span></li>
        <li><b>INTERNATIONAL JURY</b><span>Évaluation de projets, business challenges, mémoires et soutenances.</span></li>
        <li><b>MENTOR</b><span>Accompagnement d'un étudiant, entrepreneur ou jeune diplômé.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--navy on-dark" aria-labelledby="mob-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container" style="position:relative">
    <div class="section-head reveal"><p class="eyebrow">09 · Une politique de mobilité responsable</p><h2 id="mob-title">La mobilité ne se réduit jamais au déplacement</h2>
      <p class="lead">Préparée, accompagnée et reconnue : transparence de la sélection, préparation linguistique et interculturelle, conventions, reconnaissance des acquis, accompagnement et suivi au retour.</p></div>
    <div class="grid grid--3 reveal-stagger">{pr_html}</div>
  </div>
</section>

<section class="section" aria-labelledby="road-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">10 · Feuille de route internationale</p><h2 id="road-title">Six phases pour devenir une université globale</h2></div>
    <ol class="steps steps--3 reveal-stagger">{ph_html}</ol>
    <div class="card card--navy on-dark mt-3 text-center"><p class="motto" style="margin-inline:auto">The world is our campus.</p>
      <p class="mb-0" style="color:#fff;font-size:1.1rem">Faire converger trois forces : la mobilité académique européenne, les partenariats internationaux et la puissance relationnelle du réseau mondial Academy Twenty One.</p></div>
    <div class="mt-2">{notice("<p>* Présence revendiquée par la communauté Academy Twenty One. La Charte Erasmus pour l'enseignement supérieur (ECHE) est un préalable pour participer aux mobilités Erasmus+ ; Erasmus+ prévoit aussi, sous conditions, des mobilités impliquant des pays tiers non associés au programme.</p>")}</div>
  </div>
</section>
{cta_band("Vivez une formation ouverte sur le monde", "Déposez votre candidature et rejoignez une communauté présente sur cinq continents.", secondary=dl_int)}
'''
    page("international.html", "International — Academy 21 University", "Ouverture internationale d'A21 University : A21 Global Network, stratégie Erasmus+, mobilités et expériences internationales.", body)
