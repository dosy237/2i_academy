# Pages légales, plan du site et page 404.
from components import CONTACT_PHONE, CONTACT_TEL, LEGAL_NAME, SIREN, hero_light, hero_editorial, hero_visual, hero_minimal, photo_img, GLOBE_SVG, I, PROGRAMS, CONTACT_EMAIL, SCHOOL, page, simple_hero, notice

TODO = '<span class="todo">à compléter</span>'


def build_mentions():
    body = f'''
{hero_minimal([("mentions-legales.html", "Mentions légales")], "Mentions légales", "Éditeur et hébergeur du site, conformément à la loi n° 2004-575 du 21 juin 2004.")}
<section class="section"><div class="container prose">
  <h2>Éditeur du site</h2>
  <p><strong>{LEGAL_NAME}</strong> (Academy Twenty One University — Academy 21 University)<br>
  Nom commercial : A21<br>
  SIREN : {SIREN} — inscrite au Registre national des entreprises<br>
  Capital social : 2 000 €<br>
  Forme juridique : {TODO}<br>
  Siège social : {TODO}<br>
  Numéro de déclaration d'activité de formation : {TODO}<br>
  E-mail : <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a><br>
  Téléphone : <a href="tel:{CONTACT_TEL}">{CONTACT_PHONE}</a></p>
  <p>Directeur de la publication : Dr Raoul Ruben NJIONOU, fondateur.</p>
  <h2>Hébergement</h2>
  <p>Hostinger International Ltd., 61 Lordou Vironos Street, 6023 Larnaca, Chypre — <a href="https://www.hostinger.fr" rel="noopener">hostinger.fr</a>.</p>
  <h2>Propriété intellectuelle</h2>
  <p>L'ensemble des contenus du site (textes, logo, éléments graphiques, brochures) est la propriété d'{SCHOOL}, sauf mention contraire. Toute reproduction, représentation ou adaptation, totale ou partielle, sans autorisation écrite préalable est interdite.</p>
  <h2>Certifications</h2>
  <p>Les informations relatives aux certifications professionnelles (RNCP38666, RNCP39994) sont présentées conformément aux habilitations effectivement détenues et précisent le certificateur et le cadre applicable. Le détail figure sur la page <a href="admissions.html#certifications">Admissions</a>.</p>
  <h2>Crédits</h2>
  <p>Polices de caractères : Montserrat et Inter, distribuées sous licence SIL Open Font License et hébergées sur ce site.</p>
  <h2>Données personnelles</h2>
  <p>Le traitement des données collectées via les formulaires est décrit dans la <a href="confidentialite.html">politique de confidentialité</a>.</p>
</div></section>'''
    page("mentions-legales.html", "Mentions légales — Academy 21 University", "Mentions légales du site Academy Twenty One University.", body)


def build_confidentialite():
    toc = ["Responsable du traitement", "Données collectées", "Finalités et bases légales", "Destinataires", "Durées de conservation", "Stockage local et cookies", "Vos droits"]
    toc_html = "".join(f'<li><a href="#c{i}">{t}</a></li>' for i, t in enumerate(toc))
    body = f'''
{hero_minimal([("confidentialite.html", "Confidentialité")], "Politique de confidentialité", "Comment nous collectons, utilisons et protégeons vos données (RGPD).")}
<section class="section"><div class="container layout-aside">
  <div class="prose">
    <h2 id="c0">Responsable du traitement</h2>
    <p>{SCHOOL}, joignable à l'adresse <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> ou au <a href="tel:{CONTACT_TEL}">{CONTACT_PHONE}</a>. Adresse postale : {TODO}.</p>
    <h2 id="c1">Données collectées</h2>
    <p>Nous collectons uniquement les données que vous saisissez dans nos formulaires :</p>
    <ul>
      <li><strong>Formulaire de candidature :</strong> programme et préférences, civilité (facultative), nom, prénom, adresse e-mail, téléphone, ville, pays, diplôme, situation et expérience professionnelles, poste et entreprise (facultatifs), projet professionnel, CV (facultatif), source de connaissance de l'école (facultative).</li>
      <li><strong>Formulaire de contact :</strong> objet, programme concerné, nom, prénom, adresse e-mail, téléphone (facultatif), organisation (facultative) et message.</li>
    </ul>
    <h2 id="c2">Finalités et bases légales</h2>
    <ul>
      <li>Étude de votre candidature et organisation de l'admission — mesures précontractuelles prises à votre demande (article 6.1.b du RGPD).</li>
      <li>Réponse à vos demandes d'information — votre consentement (article 6.1.a), que vous pouvez retirer à tout moment.</li>
      <li>Sécurité du site et prévention des envois abusifs — intérêt légitime (article 6.1.f).</li>
    </ul>
    <h2 id="c3">Destinataires</h2>
    <p>Vos données sont destinées exclusivement à l'équipe admissions et pédagogique d'{SCHOOL}. Elles transitent par notre hébergeur (Vercel Inc.) et par notre prestataire d'envoi d'e-mails, liés par des engagements de confidentialité. Elles ne sont jamais vendues ni cédées.</p>
    <h2 id="c4">Durées de conservation</h2>
    <ul>
      <li>Candidatures non suivies d'une inscription : 2 ans à compter du dernier contact.</li>
      <li>Demandes d'information : 3 ans à compter du dernier contact.</li>
      <li>Candidatures suivies d'une inscription : intégrées au dossier de l'apprenant pour la durée légale applicable.</li>
    </ul>
    <h2 id="c5">Stockage local et cookies</h2>
    <p>Ce site ne dépose <strong>aucun cookie publicitaire ni de mesure d'audience</strong>. Les polices de caractères sont hébergées sur nos serveurs : aucune donnée n'est transmise à un service tiers lors de votre visite.</p>
    <p>Pour vous éviter de perdre votre saisie, le formulaire de candidature enregistre un brouillon <strong>uniquement sur votre appareil</strong> (stockage local du navigateur). Ce brouillon n'est jamais transmis sans votre action ; il est effacé après l'envoi et vous pouvez le supprimer à tout moment en vidant les données du site dans votre navigateur.</p>
    <h2 id="c6">Vos droits</h2>
    <p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité de vos données, ainsi que du droit de retirer votre consentement. Pour les exercer, écrivez à <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>
    <p>Si vous estimez que vos droits ne sont pas respectés, vous pouvez adresser une réclamation à la CNIL (<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
  </div>
  <aside aria-label="Sommaire"><nav class="toc" aria-labelledby="toc-title"><h2 id="toc-title">Sommaire</h2><ol>{toc_html}</ol></nav></aside>
</div></section>'''
    page("confidentialite.html", "Politique de confidentialité — Academy 21 University", "Politique de confidentialité et protection des données personnelles d'Academy Twenty One University.", body)


def build_accessibilite():
    body = f'''
{hero_minimal([("accessibilite.html", "Accessibilité")], "Déclaration d'accessibilité", "Notre engagement pour un site utilisable par toutes et tous.")}
<section class="section"><div class="container prose">
  <h2>État de conformité</h2>
  <p>Le site est <strong>partiellement conforme</strong> avec le Référentiel général d'amélioration de l'accessibilité (RGAA 4.1) et les WCAG 2.2 niveau AA. Aucun audit externe n'a encore été réalisé ; cette déclaration sera mise à jour à l'issue de l'audit.</p>
  <h2>Mesures mises en œuvre</h2>
  <ul>
    <li>Lien d'évitement « Aller au contenu principal » et structure de titres hiérarchisée.</li>
    <li>Navigation complète au clavier, focus visible sur tous les éléments interactifs.</li>
    <li>Contrastes de texte conformes au niveau AA (au moins 4,5:1 pour le texte courant).</li>
    <li>Zones cliquables d'au moins 44 × 44 pixels.</li>
    <li>Formulaires avec étiquettes visibles, aides à la saisie, messages d'erreur explicites et récapitulatif des erreurs.</li>
    <li>Tableaux de données avec légende et en-têtes associés.</li>
    <li>Respect du réglage « réduire les animations » du système.</li>
    <li>Site utilisable sans JavaScript et lisible avec un zoom de 200 %.</li>
  </ul>
  <h2>Contenus non accessibles</h2>
  <p>Les brochures au format PDF ne sont pas encore entièrement balisées pour les technologies d'assistance. Une version accessible peut être obtenue sur simple demande.</p>
  <h2>Retour d'information et contact</h2>
  <p>Si vous ne parvenez pas à accéder à un contenu ou à un service, contactez-nous via le <a href="contact.html?objet=handicap">formulaire de contact</a> ou à <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> : nous vous proposerons une alternative accessible.</p>
  <h2>Voies de recours</h2>
  <p>Si vous constatez un défaut d'accessibilité vous empêchant d'accéder à un contenu, que vous nous l'avez signalé et que vous n'avez pas obtenu de réponse satisfaisante, vous pouvez saisir le Défenseur des droits (<a href="https://www.defenseurdesdroits.fr" rel="noopener">www.defenseurdesdroits.fr</a>).</p>
</div></section>'''
    page("accessibilite.html", "Accessibilité — Academy 21 University", "Déclaration d'accessibilité du site Academy Twenty One University.", body)


def build_plan():
    progs = "".join(f'<li><a href="{p["href"]}">{p["short"]} — {p["title"]}</a></li>' for p in PROGRAMS)
    body = f'''
{hero_minimal([("plan-du-site.html", "Plan du site")], "Plan du site", "Toutes les pages du site.")}
<section class="section"><div class="container sitemap">
  <div class="card"><h2 style="font-size:1.1rem">L'école</h2><ul><li><a href="index.html">Accueil</a></li><li><a href="ecole.html">L'école</a></li><li><a href="ecole.html#fondateur">Le fondateur</a></li><li><a href="pedagogie.html">Pédagogie &amp; modalités</a></li><li><a href="international.html">International</a></li><li><a href="entreprises.html">Entreprises</a></li><li><a href="brochures.html">Brochures</a></li></ul></div>
  <div class="card"><h2 style="font-size:1.1rem">Formations</h2><ul><li><a href="formations.html">Toutes les formations</a></li>{progs}</ul></div>
  <div class="card"><h2 style="font-size:1.1rem">Candidats &amp; informations</h2><ul><li><a href="admissions.html">Admissions</a></li><li><a href="candidature.html">Candidater en ligne</a></li><li><a href="contact.html">Contact</a></li><li><a href="mentions-legales.html">Mentions légales</a></li><li><a href="confidentialite.html">Confidentialité</a></li><li><a href="accessibilite.html">Accessibilité</a></li></ul></div>
</div></section>'''
    page("plan-du-site.html", "Plan du site — Academy 21 University", "Plan du site Academy Twenty One University.", body)


def build_404():
    body = f'''
<section class="page-hero page-hero--simple on-dark" aria-labelledby="page-title">
  <div class="grid-texture" aria-hidden="true"></div>
  <div class="container"><div>
    <p class="eyebrow">Erreur 404</p>
    <h1 id="page-title">Cette page est introuvable</h1>
    <p class="lead">Elle a peut-être été déplacée ou n'existe plus. Voici quelques pistes pour reprendre votre navigation.</p>
    <div class="btn-row mt-2"><a class="btn btn--accent" href="/index.html">Retour à l'accueil {I["arrow"]}</a><a class="btn btn--glass" href="/formations.html">Nos formations</a><a class="btn btn--glass" href="/plan-du-site.html">Plan du site</a></div>
  </div></div>
</section>'''
    page("404.html", "Page introuvable — Academy 21 University", "La page demandée est introuvable.", body, noindex=True)
