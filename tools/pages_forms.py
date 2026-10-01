# Admissions, candidature en ligne, contact et confirmation.
from components import I, P, PROGRAMS, CONTACT_EMAIL, ring, page, cta_band, simple_hero, table, notice


def field(id_, label, kind="text", required=False, hint=None, attrs="", autocomplete=None, span=False):
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    r = " required" if required else ""
    desc = []
    h = ""
    if hint:
        h = f'<p class="hint" id="{id_}-hint">{hint}</p>'
        desc.append(f"{id_}-hint")
    desc.append(f"{id_}-error")
    ac = f' autocomplete="{autocomplete}"' if autocomplete else ""
    if kind == "textarea":
        ctrl = f'<textarea id="{id_}" name="{id_}"{r} aria-describedby="{" ".join(desc)}"{attrs}></textarea>'
    else:
        ctrl = f'<input id="{id_}" name="{id_}" type="{kind}"{ac}{r} aria-describedby="{" ".join(desc)}"{attrs}>'
    style = ' style="grid-column:1/-1"' if span else ""
    return f'<div class="field"{style}><label for="{id_}">{label}{req}</label>{h}{ctrl}<p class="field__error" id="{id_}-error"></p></div>'


def select(id_, label, options, required=False, hint=None, attrs=""):
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    r = " required" if required else ""
    opts = '<option value="">— Sélectionner —</option>'
    for o in options:
        if isinstance(o, tuple) and isinstance(o[1], list):
            opts += f'<optgroup label="{o[0]}">' + "".join(f'<option value="{v}">{l}</option>' for v, l in o[1]) + "</optgroup>"
        else:
            opts += f'<option value="{o[0]}">{o[1]}</option>'
    h = f'<p class="hint" id="{id_}-hint">{hint}</p>' if hint else ""
    d = (f"{id_}-hint " if hint else "") + f"{id_}-error"
    return f'<div class="field"><label for="{id_}">{label}{req}</label>{h}<select id="{id_}" name="{id_}"{r} aria-describedby="{d}"{attrs}>{opts}</select><p class="field__error" id="{id_}-error"></p></div>'


def choices(name, legend, items, required=False, inline=False, hint=None):
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    h = f'<p class="hint" id="{name}-hint">{hint}</p>' if hint else ""
    out = ""
    for i, it in enumerate(items):
        v, t = it[0], it[1]
        d = f'<span class="choice__desc">{it[2]}</span>' if len(it) > 2 and it[2] else ""
        r = " required" if (required and i == 0) else ""
        out += (f'<div class="choice"><input type="radio" id="{name}-{v}" name="{name}" value="{v}"{r}>'
                f'<label for="{name}-{v}"><span class="choice__dot" aria-hidden="true"></span><span><span class="choice__title">{t}</span>{d}</span></label></div>')
    wrap = "choice-inline" if inline else "choice-grid"
    return (f'<div class="field" data-group="{name}"><fieldset aria-describedby="{(name + "-hint ") if hint else ""}{name}-error"><legend>{legend}{req}</legend>{h}'
            f'<div class="{wrap}">{out}</div></fieldset><p class="field__error" id="{name}-error"></p></div>')


def consent(id_, text, required=True):
    return (f'<div class="field"><div class="checkbox"><input id="{id_}" name="{id_}" type="checkbox" value="oui"{" required" if required else ""} aria-describedby="{id_}-error">'
            f'<label for="{id_}">{text}</label></div><p class="field__error" id="{id_}-error"></p></div>')


EMAIL_ATTRS = ' data-required="Veuillez indiquer votre adresse e-mail." data-format="Le format de l&#39;adresse e-mail n&#39;est pas valide (exemple : nom@domaine.fr)." maxlength="160"'
TEL_PATTERN = ' pattern="[0-9 +().\\-]{8,20}" inputmode="tel"'
TEL_FORMAT = ' data-format="Le numéro doit contenir entre 8 et 20 chiffres (exemple : 06 12 34 56 78)."'

HONEYPOT = ('<div class="hp" aria-hidden="true"><label for="website">Ne pas remplir ce champ</label>'
            '<input id="website" name="website" type="text" tabindex="-1" autocomplete="off"></div><input type="hidden" name="ts" value="">')

DIPLOMES = [("aucun", "Sans diplôme"), ("bac", "Baccalauréat (niveau 4)"), ("bac2", "Bac+2 (niveau 5)"), ("bac3", "Bac+3 (niveau 6)"),
            ("bac4", "Bac+4"), ("bac5", "Bac+5 et plus (niveau 7)"), ("autre", "Autre / diplôme étranger")]
EXPERIENCE = [("0-2", "Moins de 3 ans"), ("3-4", "3 à 4 ans"), ("5-6", "5 à 6 ans"), ("7-9", "7 à 9 ans"), ("10+", "10 ans et plus")]


def build_admissions():
    faq_groups = [
        ("Conditions d'accès", [
            ("Puis-je intégrer le Bachelor sans Bac+2 ?", "Oui. À défaut du niveau 5, vous pouvez justifier d'au moins 5 années d'expérience professionnelle significative, appréciées individuellement lors de l'étude du dossier et de l'entretien. Cette condition est définie par Academy 21 University ; elle n'est pas une exigence réglementaire propre au RNCP38666."),
            ("Puis-je entrer directement en M2 du Mastère ?", "Oui, après étude individualisée de vos acquis académiques et professionnels et décision de la commission d'admission."),
            ("J'ai un Bac+2 : puis-je intégrer le Mastère ?", "Par dérogation, oui, si vous justifiez d'au moins 3 années d'expérience sur des fonctions managériales, conformément au prérequis dérogatoire du RNCP39994."),
            ("Quel profil pour l'Executive MBA ?", "Au moins 7 années d'expérience professionnelle, dont une expérience significative de management, de direction, d'entrepreneuriat ou de pilotage d'une activité. Le niveau attendu est généralement Bac+4/Bac+5, mais d'autres parcours peuvent être étudiés.")]),
        ("Organisation", [
            ("Les formations sont-elles accessibles à distance ?", "Le Bachelor, le Mastère et l'Executive MBA se suivent en présentiel, en distanciel synchrone ou en hybride. La formation IA &amp; Marketing de réseau est entièrement à distance, en classe virtuelle."),
            ("Le Mastère est-il accessible en alternance ?", "Le rythme peut être initial, en formation continue ou en alternance lorsque le cadre conventionnel le permet."),
            ("Comment se déroule l'entretien ?", "Il permet d'évaluer votre projet professionnel, vos acquis et votre capacité à suivre le programme. Pour l'Executive MBA, il s'agit d'un entretien Executive qui apprécie la maturité de votre projet.")]),
        ("Certifications", [
            ("L'Executive MBA est-il un diplôme RNCP ?", "Non. L'Executive MBA est un diplôme d'établissement d'Academy Twenty One University. La dénomination MBA ne constitue pas, à elle seule, un grade universitaire ni une certification RNCP."),
            ("Que délivre la formation IA ?", "Une attestation de formation, sous réserve de participation et de réalisation des activités prévues.")]),
    ]
    faq_html = ""
    for g, qs in faq_groups:
        faq_html += f'<div class="faq-group"><h3>{g}</h3><div class="accordion">' + "".join(
            f'<details><summary>{q}</summary><div class="accordion__body"><p>{a}</p></div></details>' for q, a in qs) + "</div></div>"
    prog_cards = ""
    access = {"bachelor": "Bac+2, ou 5 ans d'expérience significative", "mastere": "Bac+3 · Bac+2 + 3 ans en management · entrée directe en M2",
              "executive-mba": "7 ans d'expérience dont management significatif", "ia-marketing-reseau": "Activité ou projet en marketing de réseau"}
    for p in PROGRAMS:
        prog_cards += (f'<article class="card card--hover"><span class="mega__icon" style="background:{p["tile"]};margin-bottom:1rem">{p["level_big"]}</span>'
                       f'<h3>{p["short"]}</h3><p class="small text-muted">{access[p["key"]]}</p>'
                       f'<div class="btn-row card__link"><a class="btn btn--primary btn--sm" href="candidature.html?programme={p["key"]}">Candidater <span class="visually-hidden">au programme {p["short"]}</span></a>'
                       f'<a class="link-arrow" href="{p["href"]}">Fiche <span class="visually-hidden">{p["short"]}</span>{I["arrow"]}</a></div></article>')
    ADM_BTNS = f'<div class="btn-row mt-2"><a class="btn btn--accent" href="candidature.html">Commencer ma candidature {I["arrow"]}</a><a class="btn btn--glass" href="#conditions">Conditions d&#39;accès</a></div>'
    body = f'''
{simple_hero([("admissions.html", "Admissions")], "Admissions",
  "Une admission sélective sur dossier et entretien, qui tient compte de votre parcours académique comme de votre expérience professionnelle.", "Rejoindre l'école",
  ADM_BTNS, photo="etudiante")}
<section class="section" aria-labelledby="proc-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Processus</p><h2 id="proc-title">4 étapes pour nous rejoindre</h2></div>
    <ol class="steps reveal-stagger">
      <li><h3>Candidature en ligne</h3><p>Formulaire guidé en 5 étapes. Votre brouillon est enregistré sur votre appareil.</p></li>
      <li><h3>Étude du dossier</h3><p>Analyse de vos acquis académiques et professionnels par l'équipe pédagogique.</p></li>
      <li><h3>Entretien</h3><p>Entretien de positionnement (Bachelor, Mastère) ou entretien Executive (EMBA).</p></li>
      <li><h3>Décision &amp; inscription</h3><p>Décision de la commission d'admission, puis finalisation de votre inscription.</p></li>
    </ol>
  </div>
</section>
<section class="section section--mesh" id="conditions" aria-labelledby="cond-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Conditions d'accès</p><h2 id="cond-title">Les prérequis par programme</h2></div>
    <div class="grid grid--4 reveal-stagger">{prog_cards}</div>
    <div class="mt-3 reveal">{table("Conditions d'accès détaillées", ["Programme", "Accès principal", "Autres voies d'accès", "Sélection"],
      [["<a href='bachelor.html'>Bachelor (Bac+3)</a>", "Niveau 5 (Bac+2) ou niveau jugé compatible", "5 ans d'expérience professionnelle significative", "Dossier + entretien de positionnement"],
       ["<a href='mastere.html'>Mastère (Bac+5)</a>", "Entrée en M1 : niveau 6 (Bac+3) ou équivalent", "Niveau 5 + 3 ans en fonctions managériales ; entrée directe en M2 sur étude", "Dossier + entretien + validation du projet"],
       ["<a href='executive-mba.html'>Executive MBA</a>", "7 ans d'expérience dont management significatif ; Bac+4/5 en général", "Profils différents étudiés selon responsabilités et acquis", "Dossier + entretien Executive"],
       ["<a href='ia-marketing-reseau.html'>IA &amp; Marketing de réseau</a>", "Activité, projet ou expérience en marketing de réseau", "Aucun prérequis technique en IA", "Diagnostic initial"]], vol_col=None)}</div>
  </div>
</section>
<section class="section" aria-labelledby="dos-title">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">Préparer votre dossier</p>
      <h2 id="dos-title">Les éléments à rassembler</h2>
      <p>Le formulaire en ligne vous guide. Préparez ces éléments pour le compléter en une dizaine de minutes ; les justificatifs pourront vous être demandés lors de l'étude du dossier.</p>
      <a class="btn btn--primary" href="candidature.html">Commencer ma candidature {I["arrow"]}</a>
    </div>
    <ul class="check-list reveal">
      <li><strong>Votre CV</strong> à jour (PDF ou Word, 3 Mo maximum).</li>
      <li><strong>Votre dernier diplôme</strong> obtenu et son niveau.</li>
      <li><strong>Votre expérience professionnelle</strong>, en particulier managériale.</li>
      <li><strong>Votre projet professionnel</strong> et vos motivations, en quelques lignes.</li>
      <li><strong>Vos préférences</strong> de modalité (présentiel, distanciel, hybride) et de rythme.</li>
    </ul>
  </div>
</section>
<section class="section section--surface" id="certifications" aria-labelledby="cert-title">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Transparence</p><h2 id="cert-title">Certifications &amp; reconnaissance</h2></div>
    <ul class="bloc-list reveal">
      <li><b>BACHELOR</b><span><strong>Titre professionnel Responsable d'établissement marchand — RNCP38666, niveau 6</strong>Délivré par le ministère chargé de l'Emploi. Préparation et présentation en partenariat avec GREEN UP ACADEMY, partenaire habilité.</span></li>
      <li><b>MASTÈRE</b><span><strong>Programme conçu en cohérence avec le RNCP39994 — Manager des transformations des organisations, niveau 7</strong>Certificateur IRUP, échéance d'enregistrement au 18/12/2027. Présentation à la certification selon le cadre conventionnel et l'inscription auprès du certificateur.</span></li>
      <li><b>EXECUTIVE MBA</b><span><strong>Diplôme d'établissement A21 University</strong>La dénomination MBA ne constitue pas, à elle seule, un grade universitaire ni une certification RNCP.</span></li>
      <li><b>FORMATION IA</b><span><strong>Attestation de formation</strong>Sous réserve de participation et de réalisation des activités prévues.</span></li>
    </ul>
  </div>
</section>
<section class="section" id="faq" aria-labelledby="faq-title">
  <div class="container container--narrow">
    <div class="section-head section-head--center"><p class="eyebrow">FAQ</p><h2 id="faq-title">Questions fréquentes</h2></div>
    {faq_html}
    <p class="text-center mt-2">Vous ne trouvez pas votre réponse ? <a href="contact.html?objet=information">Posez-nous votre question</a>.</p>
  </div>
</section>
{cta_band("Une question sur votre éligibilité ?", "Le formulaire de candidature vous indique déjà la voie d'accès correspondant à votre profil.")}
'''
    page("admissions.html", "Admissions — Academy 21 University", "Processus d'admission, conditions d'accès par programme, certifications et questions fréquentes.", body)


def build_candidature():
    progs = [("bachelor", "Bachelor Management Stratégique &amp; Opérationnel", "Bac+3 · Niveau 6 · 420 h"),
             ("mastere", "Mastère Stratégie, Leadership &amp; Transformation", "Bac+5 · Niveau 7 · 2 ans"),
             ("executive-mba", "Executive MBA Gouvernance, Leadership &amp; Transformation", "12 mois · 7 ans d'expérience"),
             ("ia-marketing-reseau", "IA appliquée au Marketing de Réseau", "20 h · distanciel synchrone")]
    steps = ["Programme", "Identité", "Parcours", "Projet", "Envoi"]
    stepper = ""
    for i, s in enumerate(steps):
        cur = ' aria-current="step"' if i == 0 else ""
        stepper += f'<li data-step-indicator="{i}"{cur}><span class="n" aria-hidden="true">{i + 1}</span><span class="label">{s}</span></li>'

    def nav(i):
        prev = f'<button class="btn btn--ghost" type="button" data-prev>{I["arrow-left"]} Précédent</button>' if i > 0 else '<span class="spacer"></span>'
        return (f'<div class="wizard__nav">{prev}<p class="draft-note" data-draft-note hidden>{I["save"]} Brouillon enregistré sur cet appareil</p>'
                f'<button class="btn btn--primary" type="button" data-next>Continuer {I["arrow"]}</button>'
                f'<button class="btn btn--primary" type="submit" data-submit>{I["send"]} Envoyer ma candidature</button></div>')

    s1 = f'''<section class="wizard-step is-active" data-step="0" aria-labelledby="st0">
  <h2 id="st0" tabindex="-1">À quel programme candidatez-vous ?</h2>
  <p class="hint">Étape 1 sur 5 — Choisissez votre programme et vos préférences d'organisation.</p>
  <div class="form">
    {choices("programme", "Programme", progs, required=True)}
    <div data-show-if="programme=mastere" hidden>{choices("entree", "Année d'entrée souhaitée", [("m1", "Entrée en M1"), ("m2", "Entrée directe en M2", "Sur étude individualisée")], required=True, inline=True)}</div>
    <div class="form__row">
      {select("modalite", "Modalité souhaitée", [("presentiel", "Présentiel"), ("distanciel", "Distanciel synchrone"), ("hybride", "Hybride"), ("indifferent", "Pas de préférence")], required=True)}
      {select("rythme", "Rythme souhaité", [("initial", "Formation initiale"), ("continue", "Formation continue (en poste)"), ("alternance", "Alternance (selon convention)"), ("indifferent", "À définir ensemble")], hint="L'alternance concerne le Mastère, selon le cadre conventionnel.")}
    </div>
  </div>
  {nav(0)}
</section>'''
    s2 = f'''<section class="wizard-step" data-step="1" aria-labelledby="st1">
  <h2 id="st1" tabindex="-1">Vos coordonnées</h2>
  <p class="hint">Étape 2 sur 5 — Nous les utilisons uniquement pour traiter votre candidature.</p>
  <div class="form">
    {select("civilite", "Civilité", [("madame", "Madame"), ("monsieur", "Monsieur"), ("nr", "Je préfère ne pas répondre")])}
    <div class="form__row">
      {field("prenom", "Prénom", required=True, autocomplete="given-name", attrs=' data-required="Veuillez indiquer votre prénom." maxlength="80"')}
      {field("nom", "Nom", required=True, autocomplete="family-name", attrs=' data-required="Veuillez indiquer votre nom." maxlength="80"')}
    </div>
    <div class="form__row">
      {field("email", "Adresse e-mail", "email", True, "Format attendu : nom@domaine.fr", EMAIL_ATTRS, "email")}
      {field("telephone", "Téléphone", "tel", True, "Exemple : 06 12 34 56 78 ou +33 6 12 34 56 78", TEL_PATTERN + ' data-required="Veuillez indiquer votre numéro de téléphone."' + TEL_FORMAT, "tel")}
    </div>
    <div class="form__row">
      {field("ville", "Ville de résidence", required=True, autocomplete="address-level2", attrs=' data-required="Veuillez indiquer votre ville." maxlength="80"')}
      {field("pays", "Pays", required=True, autocomplete="country-name", attrs=' value="France" data-required="Veuillez indiquer votre pays." maxlength="80"')}
    </div>
  </div>
  {nav(1)}
</section>'''
    s3 = f'''<section class="wizard-step" data-step="2" aria-labelledby="st2">
  <h2 id="st2" tabindex="-1">Votre parcours</h2>
  <p class="hint">Étape 3 sur 5 — Ces informations permettent d'identifier votre voie d'accès.</p>
  <div class="form">
    <div class="form__row">
      {select("diplome", "Dernier diplôme obtenu", DIPLOMES, required=True, attrs=' data-required="Veuillez indiquer votre dernier diplôme."')}
      {field("diplome_intitule", "Intitulé du diplôme", hint="Exemple : BTS MCO, Licence Gestion…", attrs=' maxlength="160"')}
    </div>
    <div class="form__row">
      {select("situation", "Situation actuelle", [("etudiant", "Étudiant·e"), ("salarie", "Salarié·e"), ("manager", "Manager / cadre"), ("dirigeant", "Dirigeant·e"), ("entrepreneur", "Entrepreneur·e / indépendant·e"), ("recherche", "En recherche d'emploi"), ("autre", "Autre")], required=True, attrs=' data-required="Veuillez indiquer votre situation actuelle."')}
      {select("experience", "Expérience professionnelle", EXPERIENCE, required=True, attrs=' data-required="Veuillez indiquer votre expérience professionnelle."')}
    </div>
    <div class="form__row">
      {select("experience_management", "Dont expérience managériale", [("aucune", "Aucune"), ("moins3", "Moins de 3 ans"), ("3plus", "3 ans et plus")], required=True, attrs=' data-required="Veuillez indiquer votre expérience managériale."')}
      {field("poste", "Poste actuel ou dernier poste", autocomplete="organization-title", attrs=' maxlength="160"')}
    </div>
    {field("entreprise", "Entreprise ou organisation", autocomplete="organization", attrs=' maxlength="160"')}
    <div class="eligibility" data-eligibility aria-live="polite"></div>
  </div>
  {nav(2)}
</section>'''
    s4 = f'''<section class="wizard-step" data-step="3" aria-labelledby="st3">
  <h2 id="st3" tabindex="-1">Votre projet</h2>
  <p class="hint">Étape 4 sur 5 — Quelques lignes suffisent : nous approfondirons lors de l'entretien.</p>
  <div class="form">
    <div class="field"><label for="motivation">Votre projet professionnel et vos motivations <span class="req" aria-hidden="true">*</span></label>
      <p class="hint" id="motivation-hint">Entre 80 et 3 000 caractères. Pourquoi ce programme, et qu'en attendez-vous ?</p>
      <textarea id="motivation" name="motivation" required minlength="80" maxlength="3000" aria-describedby="motivation-hint motivation-count motivation-error" data-required="Veuillez présenter votre projet en quelques lignes." data-format="Votre texte doit contenir au moins 80 caractères."></textarea>
      <p class="field__counter" id="motivation-count" data-counter-for="motivation" aria-live="polite">0 / 3 000 caractères</p>
      <p class="field__error" id="motivation-error"></p></div>
    <div class="field"><label for="cv">Votre CV</label>
      <p class="hint" id="cv-hint">Facultatif — PDF ou Word, 3 Mo maximum. Vous pourrez aussi le transmettre plus tard.</p>
      <input id="cv" name="cv" type="file" accept=".pdf,.doc,.docx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document" aria-describedby="cv-hint cv-error">
      <p class="field__error" id="cv-error"></p></div>
    {select("source", "Comment avez-vous connu l'école ?", [("recherche", "Moteur de recherche"), ("reseaux", "Réseaux sociaux"), ("recommandation", "Recommandation"), ("entreprise", "Mon entreprise"), ("salon", "Salon / événement"), ("autre", "Autre")])}
  </div>
  {nav(3)}
</section>'''
    s5 = f'''<section class="wizard-step is-last" data-step="4" aria-labelledby="st4">
  <h2 id="st4" tabindex="-1">Vérifiez et envoyez</h2>
  <p class="hint">Étape 5 sur 5 — Relisez vos informations avant l'envoi.</p>
  <div class="recap" data-recap></div>
  <div class="form mt-2">
    {consent("exactitude", "Je certifie l'exactitude des informations transmises.")}
    {consent("consentement", "J'accepte que mes données soient utilisées par Academy Twenty One University pour traiter ma candidature, conformément à la <a href='confidentialite.html'>politique de confidentialité</a>.")}
    <div class="form-status" data-status role="status" aria-live="polite"></div>
  </div>
  {nav(4)}
</section>'''
    body = f'''
{simple_hero([("admissions.html", "Admissions"), ("candidature.html", "Candidature")], "Candidater en ligne",
  "Cinq étapes, une dizaine de minutes. Votre brouillon est enregistré sur votre appareil : vous pouvez reprendre plus tard.", "Admissions")}
<section class="section section--flush-top" aria-label="Formulaire de candidature">
  <div class="container" style="margin-top:-3.5rem;position:relative;z-index:2">
    <form class="wizard" id="candidature-form" data-wizard data-submit-form action="/api/submit" method="post" novalidate>
      <input type="hidden" name="type" value="candidature">
      {HONEYPOT}
      <aside class="stepper on-dark" aria-label="Progression">
        <h2>Votre candidature</h2>
        <ol>{stepper}</ol>
        <div class="stepper__progress" aria-hidden="true"><span data-progress></span></div>
        <p class="stepper__note">Les champs marqués d'un astérisque (<span aria-hidden="true">*</span>) sont obligatoires.</p>
      </aside>
      <div class="wizard__panel">
        <div class="error-summary" tabindex="-1" role="alert" data-error-summary hidden><h3>Erreurs</h3><ul></ul></div>
        {s1}{s2}{s3}{s4}{s5}
      </div>
    </form>
  </div>
</section>
'''
    page("candidature.html", "Candidater en ligne — Academy 21 University", "Formulaire de candidature en ligne aux programmes d'Academy Twenty One University.", body)


def build_contact():
    objets = [("information", "Demande d'information"), ("orientation", "Entretien d'orientation"), ("entreprise", "Entreprise / partenariat"),
              ("rappel", "Être rappelé·e"), ("handicap", "Aménagement / situation de handicap"), ("autre", "Autre demande")]
    prog_opts = [(p["key"], f'{p["short"]} — {p["title"]}') for p in PROGRAMS] + [("indecis", "Je ne sais pas encore")]
    body = f'''
{simple_hero([("contact.html", "Contact")], "Contactez-nous",
  "Information, orientation, partenariat entreprise ou demande d'aménagement : l'équipe vous répond personnellement.", "Contact",
  f'<div class="btn-row mt-2"><a class="btn btn--accent" href="candidature.html">Vous souhaitez candidater ? {I["arrow"]}</a></div>')}
<section class="section section--flush-top" aria-labelledby="form-title">
  <div class="container layout-aside" style="margin-top:-3.5rem;position:relative;z-index:2">
    <div class="wizard__panel">
      <h2 id="form-title">Votre message</h2>
      <p class="text-muted">Les champs marqués d'un astérisque (<span class="req">*</span>) sont obligatoires.</p>
      <form class="form" id="contact-form" data-validate data-submit-form action="/api/submit" method="post" novalidate>
        <input type="hidden" name="type" value="contact">
        {HONEYPOT}
        <div class="error-summary" tabindex="-1" role="alert" data-error-summary hidden><h3>Erreurs</h3><ul></ul></div>
        <div class="form__row">
          {select("objet", "Objet de votre demande", objets, required=True, attrs=' data-required="Veuillez sélectionner l&#39;objet de votre demande."')}
          {select("programme", "Programme concerné", prog_opts)}
        </div>
        <div class="form__row">
          {field("prenom", "Prénom", required=True, autocomplete="given-name", attrs=' data-required="Veuillez indiquer votre prénom." maxlength="80"')}
          {field("nom", "Nom", required=True, autocomplete="family-name", attrs=' data-required="Veuillez indiquer votre nom." maxlength="80"')}
        </div>
        <div class="form__row">
          {field("email", "Adresse e-mail", "email", True, "Format attendu : nom@domaine.fr", EMAIL_ATTRS, "email")}
          {field("telephone", "Téléphone", "tel", False, "Facultatif — utile si vous souhaitez être rappelé·e", TEL_PATTERN + TEL_FORMAT, "tel")}
        </div>
        <div data-show-if="objet=entreprise" hidden>{field("organisation", "Entreprise ou organisation", autocomplete="organization", attrs=' maxlength="160"')}</div>
        <div class="field"><label for="message">Votre message <span class="req" aria-hidden="true">*</span></label>
          <textarea id="message" name="message" required minlength="10" maxlength="3000" aria-describedby="message-count message-error" data-required="Veuillez écrire votre message." data-format="Votre message doit contenir au moins 10 caractères."></textarea>
          <p class="field__counter" id="message-count" data-counter-for="message" aria-live="polite">0 / 3 000 caractères</p>
          <p class="field__error" id="message-error"></p></div>
        {consent("consentement", "J'accepte que mes données soient utilisées pour répondre à ma demande, conformément à la <a href='confidentialite.html'>politique de confidentialité</a>.")}
        <div class="form-status" data-status role="status" aria-live="polite"></div>
        <div><button class="btn btn--primary" type="submit" data-submit>{I["send"]} Envoyer ma demande</button></div>
      </form>
    </div>
    <aside aria-label="Autres moyens de contact">
      <div class="aside-card aside-card--navy on-dark">
        <h2>Écrivez-nous directement</h2>
        <p class="small">Pour toute question sur les programmes, l'admission ou un partenariat.</p>
        <a class="btn btn--accent" href="mailto:{CONTACT_EMAIL}">{I["mail"]} {CONTACT_EMAIL}</a>
      </div>
      <div class="aside-card">
        <h2>Accès rapides</h2>
        <ul class="aside-list">
          <li>{I["send"]}<span><a href="candidature.html">Déposer une candidature</a></span></li>
          <li>{I["download"]}<span><a href="brochures.html">Télécharger une brochure</a></span></li>
          <li>{I["info"]}<span><a href="admissions.html#faq">Questions fréquentes</a></span></li>
          <li>{I["handshake"]}<span><a href="entreprises.html">Espace entreprises</a></span></li>
        </ul>
      </div>
      <div class="aside-card">
        <h2>Situation de handicap</h2>
        <p class="small mb-0">Choisissez l'objet « Aménagement / situation de handicap » : votre demande sera étudiée avec attention et en toute confidentialité.</p>
      </div>
    </aside>
  </div>
</section>
'''
    page("contact.html", "Contact — Academy 21 University", "Contactez Academy Twenty One University : information, orientation, entreprises, aménagements.", body)


def build_merci():
    body = f'''
<section class="page-hero page-hero--simple on-dark" aria-labelledby="page-title">
  <div class="grid-texture" aria-hidden="true"></div>
  {ring("deco", uid="ph")}
  <div class="container text-center"><div>
    <div class="success-mark">{I["check"]}</div>
    <h1 id="page-title" data-merci-title>Merci, votre demande a bien été envoyée</h1>
    <p class="lead" style="margin-inline:auto" data-merci-lead>Notre équipe l'étudie et revient vers vous par e-mail dans les meilleurs délais.</p>
    <div class="ref-box mt-1" data-ref-box hidden><span>Votre référence</span><strong data-ref></strong></div>
  </div></div>
</section>
<section class="section" aria-labelledby="next-title">
  <div class="container">
    <div class="section-head section-head--center"><p class="eyebrow">Et maintenant ?</p><h2 id="next-title">Les prochaines étapes</h2></div>
    <ol class="steps">
      <li><h3>Accusé de réception</h3><p>Conservez votre référence : elle facilite nos échanges.</p></li>
      <li><h3>Étude du dossier</h3><p>L'équipe pédagogique analyse votre parcours et votre projet.</p></li>
      <li><h3>Entretien</h3><p>Nous vous contactons pour fixer un entretien de positionnement.</p></li>
      <li><h3>Décision</h3><p>La commission d'admission vous communique sa décision.</p></li>
    </ol>
    <div class="btn-row mt-3" style="justify-content:center">
      <a class="btn btn--navy" href="index.html">Retour à l'accueil</a>
      <a class="btn btn--ghost" href="brochures.html">{I["download"]} Télécharger une brochure</a>
      <a class="btn btn--ghost" href="pedagogie.html">Découvrir notre pédagogie</a>
    </div>
  </div>
</section>
'''
    page("merci.html", "Merci — Academy 21 University", "Confirmation de l'envoi de votre demande à Academy Twenty One University.", body, noindex=True)
