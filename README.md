# Academy 21 University — site web

Site statique (HTML/CSS/JS sans dépendance) + une fonction serverless Vercel pour recevoir les candidatures.
Contenus issus des brochures officielles (Bachelor, Mastère, Executive MBA, formation IA).

## Pages (23)

Accueil · L'école (identité, fondateur, valeurs, ambition 2030+) · International (Global Network, Erasmus+) · Formations (catalogue filtrable) · 4 fiches programme · Pédagogie & modalités · Entreprises ·
Admissions (+ FAQ, certifications) · **Candidature en ligne** (5 étapes) · Contact · Brochures (PDF) · Merci ·
Mentions légales · Confidentialité · Accessibilité · Plan du site · 404.
Paiement (non référencées) : Espace de paiement · Confirmation de paiement · Espace école.

## Activer l'envoi des e-mails (10 minutes)

Les formulaires envoient vers `/api/submit` (`api/submit.js`). Les e-mails partent **de votre boîte Gmail**,
avec **« Academy 21 University »** comme nom d'expéditeur.

À chaque candidature :
- l'école reçoit la candidature (avec le CV en pièce jointe) ; « Répondre » écrit directement au candidat ;
- vous recevez une copie (et l'e-mail reste aussi dans vos « Messages envoyés ») ;
- le candidat reçoit un accusé de réception avec sa référence (`A21-AAMMJJ-XXXX`).

1. Sur le compte Google qui enverra les e-mails : activer la **validation en deux étapes**
   (myaccount.google.com → Sécurité), puis créer un **mot de passe d'application**
   (myaccount.google.com/apppasswords) : 16 caractères.
2. Dans Vercel → **Settings → Environment Variables** :

| Variable | Valeur |
|---|---|
| `SMTP_USER` | votre adresse Gmail (l'expéditeur) |
| `SMTP_PASS` | le mot de passe d'application (16 caractères) — jamais votre mot de passe Gmail |
| `ADMISSIONS_EMAIL` | l'adresse de l'école qui reçoit les candidatures (plusieurs : séparées par des virgules) |
| `COPY_EMAIL` *(facultatif)* | qui reçoit la copie ; par défaut `SMTP_USER` (vous) |
| `MAIL_FROM_NAME` *(facultatif)* | nom affiché ; par défaut « Academy 21 University » |
| `SEND_CONFIRMATION` *(facultatif)* | `0` pour ne pas envoyer l'accusé de réception au candidat |

3. **Redeploy**. Limite Gmail : environ 500 e-mails par jour.

Plus tard, avec un nom de domaine vérifié (ex. `admissions@a21businessschool.com`), le site peut aussi envoyer via
[Resend](https://resend.com) : `RESEND_API_KEY`, `MAIL_FROM`, `ADMISSIONS_EMAIL`, `SEND_CONFIRMATION=1`.
`WEBHOOK_URL` (facultatif) envoie aussi chaque candidature en JSON (Google Sheets, Make, Zapier…).
Tant que rien n'est configuré, le site propose au visiteur l'envoi par e-mail et le téléchargement de son récapitulatif.

## Frais d'étude de dossier (paiement en ligne)

Le candidat ne paie rien en déposant sa candidature. Après l'étude d'un dossier recevable :

1. L'école ouvre **/espace-ecole.html** (lien direct et pré-rempli dans chaque e-mail de candidature),
   saisit sa clé d'accès et clique sur « Créer et envoyer le lien ».
   Plusieurs candidats d'un même programme : coller leurs adresses séparées par des virgules ; chacun reçoit son propre
   e-mail et son propre lien (référence attribuée automatiquement), et l'école reçoit un récapitulatif (50 adresses maximum par envoi).
2. Le candidat reçoit un e-mail avec son **lien personnel** (signé, valable 30 jours par défaut) vers
   **/paiement.html** : récapitulatif du dossier, 50 € par carte bancaire, ou 32 800 FCFA par Orange Money / MTN MoMo
   (taux fixe 1 € = 655,957 FCFA, arrondi au multiple de 5 exigé par CinetPay).
3. Une fois le paiement confirmé par le prestataire, l'école (avec copie) et le candidat reçoivent un e-mail de confirmation.

Aucune base de données : la référence du dossier voyage dans le lien, protégé par une signature.

### Comptes à créer (au nom de l'école, avec la même adresse e-mail)

| Service | Rôle | Coût |
|---|---|---|
| [Stripe](https://dashboard.stripe.com/register) | Carte bancaire (Visa, Mastercard, CB) | Pas d'abonnement ; commission par paiement (environ 1,5 % + 0,25 € pour une carte européenne, davantage pour une carte hors Europe) |
| [Flutterwave](https://flutterwave.com) *(recommandé pour le Cameroun)* | Orange Money, MTN MoMo (XAF Cameroun, XOF Afrique de l'Ouest) | Pas d'abonnement ; commission par paiement (à confirmer à l'inscription) |
| [CinetPay](https://cinetpay.com) *(alternative)* | Orange Money, MTN MoMo (XAF, XOF) | Pas d'abonnement ; commission par paiement (de l'ordre de 3 %) |

Tarifs indicatifs : à vérifier sur le site de chaque prestataire au moment de l'inscription. Les deux services demandent des
justificatifs de l'école (statuts, identité du représentant, coordonnées bancaires) avant de verser les fonds.

### Variables Vercel du paiement

| Variable | Valeur |
|---|---|
| `PAYMENT_SECRET` | une longue phrase secrète aléatoire (32 caractères ou plus) ; sert à signer les liens |
| `ADMIN_KEY` | la clé d'accès de l'espace école (12 caractères minimum), à ne partager qu'avec l'équipe d'admission |
| `STRIPE_SECRET_KEY` | Stripe → Développeurs → Clés API → clé secrète (`sk_test_…` pour tester, `sk_live_…` en production) |
| `FLW_SECRET_KEY` | Flutterwave → Settings → API Keys → clé secrète (`FLWSECK_TEST-…` pour tester) |
| `FLW_WEBHOOK_HASH` | une phrase secrète de votre choix, recopiée dans Flutterwave → Settings → Webhooks (« Secret hash ») |
| `CINETPAY_APIKEY`, `CINETPAY_SITE_ID` | seulement si vous choisissez CinetPay (CinetPay → Intégrations) |
| `MOBILE_PROVIDER` *(facultatif)* | `flutterwave` ou `cinetpay` si les deux sont configurés (Flutterwave par défaut) |
| `MOBILE_CURRENCIES` *(facultatif)* | `XAF,XOF` par défaut ; `XAF` seul pour ne proposer que l'Afrique centrale |
| `FEE_EUR` *(facultatif)* | montant en euros, `50` par défaut |
| `SITE_URL` *(facultatif)* | adresse publique du site, ex. `https://www.academy21.com` (sinon déduite automatiquement) |

Webhook Stripe (recommandé, garantit l'e-mail même si le candidat ferme la page) : Stripe → Développeurs → Webhooks →
ajouter l'URL `https://a21businessschool.com/api/stripe-webhook` avec les événements `checkout.session.completed` et
`checkout.session.async_payment_succeeded`. Webhook Flutterwave : `https://a21businessschool.com/api/flutterwave` (avec le même
« Secret hash » que `FLW_WEBHOOK_HASH`). CinetPay utilise automatiquement `https://a21businessschool.com/api/cinetpay`.
Tant qu'un moyen de paiement n'est pas configuré, la page l'affiche comme « pas encore activé ».

## Héberger chez Hostinger (au lieu de Vercel)

Guide complet, pas à pas (comptes, domaine, e-mails, paiements, tests) : [docs/GUIDE-MISE-EN-LIGNE.md](docs/GUIDE-MISE-EN-LIGNE.md).

Le site fonctionne à l'identique avec `server.js` (Node.js 20 ou plus, aucune autre dépendance que nodemailer).

1. Offre Hostinger compatible **Node.js** : *Business* ou *Cloud* (l'hébergement de base ne fait pas tourner Node.js).
2. hPanel → **Sites web → Ajouter → Application web Node.js** : importer le dépôt GitHub (ou l'archive du site),
   commande d'installation `npm install`, commande de démarrage `npm start`, version de Node 20 ou 22.
3. Dans **Variables d'environnement** de l'application : les mêmes variables que ci-dessus (e-mails, paiement), plus
   `SITE_URL=https://www.a21businessschool.com`.
4. Rattacher le nom de domaine à l'application, puis activer le certificat SSL (gratuit).
5. Mettre à jour les adresses de webhook chez Stripe et Flutterwave avec le nouveau domaine.

**E-mails avec une boîte Hostinger** (à la place de Gmail) :

| Variable | Valeur |
|---|---|
| `SMTP_HOST` | `smtp.hostinger.com` |
| `SMTP_PORT` | `465` |
| `SMTP_USER` | l'adresse qui envoie, ex. `noreply@a21businessschool.com` |
| `SMTP_PASS` | le mot de passe de cette boîte |
| `ADMISSIONS_EMAIL` | la ou les boîtes de l'école qui reçoivent (séparées par des virgules) |
| `COPY_EMAIL` | qui reçoit une copie |

Pensez à changer l'adresse affichée sur le site (`CONTACT_EMAIL` dans `tools/components.py`) puis à régénérer les pages.

## Modifier le site

Les pages sont générées par `tools/` (en-tête, pied et composants communs) :

```bash
python3 tools/build_pages.py     # régénère les 23 pages
python3 -m http.server           # aperçu sur http://localhost:8000 (sans l'API)
```

- Coordonnées : `CONTACT_EMAIL` dans `tools/components.py`.
- Photos : `assets/img/photos/` (dictionnaire `PHOTOS` dans `tools/components.py`) ; photos du fondateur : `dr-raoul-njionou-1/2/3.jpg`.
- Polices : Montserrat (titres, harmonisée avec le site Academy21), Inter (texte). Mots mis en valeur : classe `.serif` (encadré, sans italique).
- Styles : `assets/css/styles.css` · Interactions : `assets/js/main.js`.
- En-têtes : un gabarit par type de page (`hero_light`, `hero_editorial`, `hero_visual`, `hero_minimal`, en-tête des fiches) et une ambiance de couleur par page (`amb-red|gold|green|blue`) dans `tools/components.py`.

## Accessibilité & qualité

RGAA 4.1 / WCAG 2.2 AA visés : lien d'évitement, navigation clavier, focus visible, contrastes vérifiés, cibles ≥ 44 px,
formulaires avec erreurs liées et récapitulatif, `prefers-reduced-motion`, fonctionnement sans JavaScript.
Polices auto-hébergées (aucun service tiers, aucun cookie).

## Coordonnées et informations légales

ACADEMY TWENTY ONE (A21) — 7 boulevard Suchet, 75016 Paris — SIRET 927 784 314 00019 — capital 2 000 €.
Contact : `contact@a21businessschool.com` · 07 51 36 09 44 (constantes dans `tools/components.py` et `tools/pages_legal.py`).
