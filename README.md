# Academy 21 University — site web

Site statique (HTML/CSS/JS sans dépendance) + une fonction serverless Vercel pour recevoir les candidatures.
Contenus issus des brochures officielles (Bachelor, Mastère, Executive MBA, formation IA).

## Pages (20)

Accueil · L'école (identité, fondateur, valeurs, ambition 2030+) · International (Global Network, Erasmus+) · Formations (catalogue filtrable) · 4 fiches programme · Pédagogie & modalités · Entreprises ·
Admissions (+ FAQ, certifications) · **Candidature en ligne** (5 étapes) · Contact · Brochures (PDF) · Merci ·
Mentions légales · Confidentialité · Accessibilité · Plan du site · 404.

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

Plus tard, avec un nom de domaine vérifié (ex. `admissions@academy21france.fr`), le site peut aussi envoyer via
[Resend](https://resend.com) : `RESEND_API_KEY`, `MAIL_FROM`, `ADMISSIONS_EMAIL`, `SEND_CONFIRMATION=1`.
`WEBHOOK_URL` (facultatif) envoie aussi chaque candidature en JSON (Google Sheets, Make, Zapier…).
Tant que rien n'est configuré, le site propose au visiteur l'envoi par e-mail et le téléchargement de son récapitulatif.

## Modifier le site

Les pages sont générées par `tools/` (en-tête, pied et composants communs) :

```bash
python3 tools/build_pages.py     # régénère les 20 pages
python3 -m http.server           # aperçu sur http://localhost:8000 (sans l'API)
```

- Coordonnées : `CONTACT_EMAIL` dans `tools/components.py`.
- Photos : `assets/img/photos/` (dictionnaire `PHOTOS` dans `tools/components.py`) ; photos du fondateur : `dr-raoul-njionou-1/2/3.jpg`.
- Polices : Montserrat (titres, harmonisée avec le site Academy21), Inter (texte), Source Serif 4 (citations).
- Styles : `assets/css/styles.css` · Interactions : `assets/js/main.js`.
- En-têtes : un gabarit par type de page (`hero_light`, `hero_editorial`, `hero_visual`, `hero_minimal`, en-tête des fiches) et une ambiance de couleur par page (`amb-red|gold|green|blue`) dans `tools/components.py`.

## Accessibilité & qualité

RGAA 4.1 / WCAG 2.2 AA visés : lien d'évitement, navigation clavier, focus visible, contrastes vérifiés, cibles ≥ 44 px,
formulaires avec erreurs liées et récapitulatif, `prefers-reduced-motion`, fonctionnement sans JavaScript.
Polices auto-hébergées (aucun service tiers, aucun cookie).

## À compléter

Mentions légales (raison sociale, siège, SIRET, n° de déclaration d'activité, directeur de publication),
adresse postale, confirmation de l'adresse `admissions@academy21france.fr`.
