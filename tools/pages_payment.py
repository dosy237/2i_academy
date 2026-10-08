# Paiement des frais d'étude de dossier : espace de paiement, confirmation, espace école.
from components import hero_minimal, I, PROGRAMS, CONTACT_EMAIL, ring, page, notice
from pages_forms import field, select

FEE_EUR = "50,00&nbsp;€"
FEE_FCFA = "32&nbsp;800&nbsp;FCFA"

TRUST = f'''<ul class="pay-trust" aria-label="Garanties">
  <li>{I["lock"]}<span><strong>Paiement chiffré</strong>Pages sécurisées de nos prestataires agréés.</span></li>
  <li>{I["shield"]}<span><strong>Données protégées</strong>L'école n'a jamais accès à vos coordonnées bancaires.</span></li>
  <li>{I["mail"]}<span><strong>Reçu par e-mail</strong>Un justificatif vous est envoyé dès la confirmation.</span></li>
</ul>'''


def build_paiement():
    body = f'''
{hero_minimal([("admissions.html", "Admissions"), ("paiement.html", "Paiement")], "Frais d'étude <span class='serif'>de dossier</span>",
  "Votre espace de paiement personnel et sécurisé.")}
<section class="section section--flush-top" aria-label="Paiement">
  <div class="container">
    <noscript>{notice(f"<p><strong>JavaScript est nécessaire pour accéder au paiement en ligne.</strong> Activez-le, ou écrivez-nous à <a href='mailto:{CONTACT_EMAIL}'>{CONTACT_EMAIL}</a> pour régler vos frais autrement.</p>", "info")}</noscript>
    <div class="pay" data-pay>
      <div class="pay-state js-only" data-pay-state="loading" role="status">
        <span class="spinner spinner--dark" aria-hidden="true"></span> Chargement de votre dossier…
      </div>

      <div class="pay-state pay-state--error" data-pay-state="error" hidden>
        <div class="pay-state__icon">{I["info"]}</div>
        <h2 data-pay-error-title tabindex="-1">Ce lien de paiement n'est pas valide</h2>
        <p data-pay-error-text>Vérifiez que vous avez copié le lien complet reçu par e-mail.</p>
        <div class="btn-row" style="justify-content:center">
          <a class="btn btn--primary" href="mailto:{CONTACT_EMAIL}?subject=Frais%20d%27%C3%A9tude%20de%20dossier">{I["mail"]} Écrire au service admissions</a>
          <a class="btn btn--ghost" href="admissions.html">Retour aux admissions</a>
        </div>
      </div>

      <div class="pay-grid" data-pay-state="ready" hidden>
        <aside class="pay-summary on-dark" aria-labelledby="sum-title">
          {ring("deco", uid="pay")}
          <p class="eyebrow">Votre dossier</p>
          <h2 id="sum-title" class="visually-hidden">Récapitulatif</h2>
          <dl class="pay-summary__list">
            <div><dt>Référence</dt><dd data-f="ref"></dd></div>
            <div><dt>Candidat·e</dt><dd data-f="name"></dd></div>
            <div><dt>Programme</dt><dd data-f="programme"></dd></div>
          </dl>
          <div class="pay-summary__amount">
            <span>Frais d'étude de dossier</span>
            <strong data-f="eur">{FEE_EUR}</strong>
            <span class="pay-summary__fx">soit <b data-f="fcfa">{FEE_FCFA}</b> en Mobile Money</span>
          </div>
          <p class="pay-summary__note">Taux fixe et garanti : 1&nbsp;€ = 655,957&nbsp;FCFA (XAF et XOF). Lien valable jusqu'au <span data-f="expires"></span>.</p>
        </aside>

        <div class="pay-main">
          <div data-pay-cancel hidden>{notice("<p><strong>Paiement interrompu.</strong> Aucun montant n'a été débité. Vous pouvez réessayer ci-dessous.</p>", "info")}</div>
          <h2 id="methods-title" tabindex="-1">Choisissez votre moyen de paiement</h2>
          <div class="pay-methods" role="list" aria-labelledby="methods-title">
            <article class="pay-method" role="listitem" data-method="card">
              <div class="pay-method__head">
                <span class="pay-method__icon pay-method__icon--card">{I["card"]}</span>
                <div><h3>Carte bancaire</h3><p class="pay-method__brands">Visa · Mastercard · CB</p></div>
                <strong class="pay-method__amount" data-f="eur">{FEE_EUR}</strong>
              </div>
              <p class="small text-muted">Paiement en euros sur la page sécurisée de Stripe. Votre banque peut vous demander une validation.</p>
              <button type="button" class="btn btn--primary btn--block" data-pay-go="card">{I["lock"]} <span>Payer <span data-f="eur">{FEE_EUR}</span> par carte</span></button>
              <p class="pay-method__off" data-off hidden>Ce moyen de paiement n'est pas encore activé. <a href="mailto:{CONTACT_EMAIL}">Contactez-nous</a>.</p>
            </article>
            <article class="pay-method" role="listitem" data-method="mobile">
              <div class="pay-method__head">
                <span class="pay-method__icon pay-method__icon--mobile">{I["phone"]}</span>
                <div><h3>Mobile Money</h3><p class="pay-method__brands">Orange Money · MTN MoMo</p></div>
                <strong class="pay-method__amount" data-f="fcfa">{FEE_FCFA}</strong>
              </div>
              <p class="small text-muted">Montant converti en francs CFA au taux fixe. Vous validez le paiement sur votre téléphone, sur la page sécurisée de notre prestataire.</p>
              <fieldset class="pay-zones" data-zones hidden><legend>Votre zone</legend><div class="pay-zones__list" data-zones-list></div></fieldset>
              <button type="button" class="btn btn--navy btn--block" data-pay-go="mobile">{I["phone"]} <span>Payer <span data-f="fcfa">{FEE_FCFA}</span></span></button>
              <p class="pay-method__off" data-off hidden>Ce moyen de paiement n'est pas encore activé. <a href="mailto:{CONTACT_EMAIL}">Contactez-nous</a>.</p>
            </article>
          </div>
          <div class="form-status" data-pay-status role="status" aria-live="polite"></div>
          {TRUST}
        </div>
      </div>
    </div>
  </div>
</section>
'''
    page("paiement.html", "Paiement des frais d'étude — Academy 21 University",
         "Espace de paiement sécurisé des frais d'étude de dossier : carte bancaire, Orange Money, MTN Mobile Money.", body, noindex=True)


def build_paiement_confirmation():
    body = f'''
<section class="page-hero page-hero--simple on-dark" aria-labelledby="page-title">
  <div class="grid-texture" aria-hidden="true"></div>
  {ring("deco", uid="pc")}
  <div class="container text-center"><div data-paid-box>
    <div class="success-mark" data-paid-mark hidden>{I["check"]}</div>
    <div class="pay-wait js-only" data-paid-wait aria-hidden="true"><span class="spinner"></span></div>
    <h1 id="page-title" data-paid-title tabindex="-1">Vérification de votre paiement…</h1>
    <p class="lead" style="margin-inline:auto" data-paid-lead>Nous interrogeons notre prestataire de paiement. Merci de patienter quelques secondes.</p>
    <noscript><p class="lead" style="margin-inline:auto">Le reçu de votre paiement vous est envoyé par e-mail dès sa confirmation.</p></noscript>
  </div></div>
</section>
<section class="section" aria-labelledby="det-title">
  <div class="container container--narrow">
    <div class="recap pay-receipt" data-paid-details hidden>
      <h2 id="det-title">Détail du paiement</h2>
      <dl>
        <dt>Référence du dossier</dt><dd data-p="ref"></dd>
        <dt>Candidat·e</dt><dd data-p="name"></dd>
        <dt>Montant</dt><dd data-p="amount"></dd>
        <dt>Moyen de paiement</dt><dd data-p="provider"></dd>
        <dt>N° de transaction</dt><dd data-p="transaction"></dd>
      </dl>
    </div>
    <div class="btn-row mt-3" style="justify-content:center">
      <a class="btn btn--navy" href="index.html">Retour à l'accueil</a>
      <a class="btn btn--ghost" href="mailto:{CONTACT_EMAIL}">{I["mail"]} Une question ? Écrivez-nous</a>
    </div>
  </div>
</section>
'''
    page("paiement-confirmation.html", "Confirmation de paiement — Academy 21 University",
         "Confirmation du paiement des frais d'étude de dossier.", body, noindex=True)


def build_espace_ecole():
    prog_opts = [(p["key"], f'{p["short"]} — {p["title"]}') for p in PROGRAMS] + [("indecis", "Programme à confirmer")]
    body = f'''
{hero_minimal([("espace-ecole.html", "Espace école")], "Espace <span class='serif'>école</span>",
  "Après l'étude d'un dossier recevable : envoyer au candidat son lien de paiement des frais d'étude.")}
<section class="section section--flush-top" aria-labelledby="link-title">
  <div class="container layout-aside">
    <div class="wizard__panel">
      <h2 id="link-title">Demander les frais d'étude</h2>
      <p class="text-muted">Réservé à l'équipe d'admission. Les champs marqués d'un astérisque (<span class="req">*</span>) sont obligatoires.</p>
      <form class="form" id="fee-form" action="/api/payment" method="post" novalidate>
        <input type="hidden" name="action" value="link">
        <div class="error-summary" tabindex="-1" role="alert" data-error-summary hidden><h3>Erreurs</h3><ul></ul></div>
        {field("key", "Clé d'accès de l'école", "password", True, "La clé définie dans Vercel (variable ADMIN_KEY).", ' data-required="Veuillez saisir la clé d&#39;accès." autocomplete="current-password"')}
        <div class="field"><label for="email">E-mail du ou des candidats <span class="req" aria-hidden="true">*</span></label>
          <p class="hint" id="email-hint">Plusieurs candidats : collez leurs adresses séparées par des virgules. Chacun reçoit son propre e-mail et son propre lien.</p>
          <textarea id="email" name="email" rows="2" required data-emails inputmode="email" autocomplete="off" spellcheck="false" aria-describedby="email-hint email-error" data-required="Veuillez indiquer au moins une adresse e-mail."></textarea>
          <p class="field__error" id="email-error"></p></div>
        <div class="notice notice--info" data-batch-note role="status" hidden>{I["info"]}<div><p data-batch-text></p></div></div>
        <div class="form__row">
          {select("programme", "Programme", prog_opts, required=True, attrs=' data-required="Veuillez sélectionner le programme."')}
          <div data-single>{field("ref", "Référence du dossier", required=True, hint="Exemple : A21-261008-K4P2", attrs=' data-required="Veuillez indiquer la référence du dossier." maxlength="40" autocapitalize="characters"')}</div>
        </div>
        <div class="form__row" data-single>
          {field("prenom", "Prénom du candidat", required=True, attrs=' data-required="Veuillez indiquer le prénom." maxlength="80"')}
          {field("nom", "Nom du candidat", required=True, attrs=' data-required="Veuillez indiquer le nom." maxlength="80"')}
        </div>
        <div class="form__row">
          {field("amount", "Montant (€)", "text", True, "Converti automatiquement en FCFA pour le Mobile Money.", ' value="50" inputmode="decimal" pattern="[0-9]{1,4}([.,][0-9]{1,2})?" data-required="Veuillez indiquer le montant." data-format="Montant attendu : un nombre, par exemple 50."')}
          {field("days", "Validité du lien (jours)", "text", True, "Entre 1 et 90 jours.", ' value="30" inputmode="numeric" pattern="[1-9][0-9]?" data-required="Veuillez indiquer la durée de validité." data-format="Un nombre de jours entre 1 et 90."')}
        </div>
        <div class="field"><label for="message">Message personnel</label>
          <p class="hint" id="message-hint">Facultatif — ajouté à l'e-mail, par exemple pour annoncer l'entretien.</p>
          <textarea id="message" name="message" maxlength="1200" aria-describedby="message-hint message-error"></textarea>
          <p class="field__error" id="message-error"></p></div>
        <div class="field"><div class="checkbox"><input id="send" name="send" type="checkbox" value="1" checked>
          <label for="send">Envoyer l'e-mail au candidat (copie à l'école)</label></div></div>
        <div class="form-status" data-status role="status" aria-live="polite"></div>
        <div><button class="btn btn--primary" type="submit" data-submit>{I["send"]} Créer et envoyer le lien</button></div>
      </form>
      <div class="pay-link" data-link-box hidden>
        <label for="pay-link-out">Lien de paiement du candidat</label>
        <div class="pay-link__row"><input id="pay-link-out" type="text" readonly>
          <button type="button" class="btn btn--ghost btn--sm" data-copy>{I["copy"]} Copier</button></div>
      </div>
      <div class="pay-link" data-batch-box hidden>
        <h3 class="pay-link__title">Liens créés</h3>
        <table class="pay-batch"><caption class="visually-hidden">Liens de paiement par candidat</caption>
          <thead><tr><th scope="col">E-mail</th><th scope="col">Référence</th><th scope="col">Statut</th><th scope="col">Lien</th></tr></thead><tbody data-batch-rows></tbody></table>
      </div>
    </div>
    <aside aria-label="Fonctionnement">
      <div class="aside-card">
        <h2>Comment ça marche</h2>
        <ol class="mini-steps">
          <li>Le candidat dépose sa candidature : <strong>rien n'est payé</strong> à ce stade.</li>
          <li>Dossier recevable : vous envoyez ici le lien (ou depuis le bouton présent dans l'e-mail de candidature, qui pré-remplit ce formulaire). Plusieurs candidats d'un même programme : séparez leurs adresses par des virgules.</li>
          <li>Le candidat paie par carte ou Mobile Money. L'école et le candidat reçoivent la confirmation par e-mail.</li>
        </ol>
      </div>
      <div class="aside-card aside-card--navy on-dark mt-2">
        <h2>{I["key"]} Accès protégé</h2>
        <p class="small">La clé n'est jamais enregistrée sur le site. Ne la partagez qu'avec l'équipe d'admission.</p>
      </div>
    </aside>
  </div>
</section>
'''
    page("espace-ecole.html", "Espace école — Academy 21 University", "Espace réservé à l'équipe d'admission.", body, noindex=True)
