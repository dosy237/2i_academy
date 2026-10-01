# Academy 21 University — site web

Site statique (HTML/CSS/JS sans dépendance) + une fonction serverless Vercel pour recevoir les candidatures.
Contenus issus des brochures officielles (Bachelor, Mastère, Executive MBA, formation IA).

## Pages (19)

Accueil · L'école · Formations (catalogue filtrable) · 4 fiches programme · Pédagogie & modalités · Entreprises ·
Admissions (+ FAQ, certifications) · **Candidature en ligne** (5 étapes) · Contact · Brochures (PDF) · Merci ·
Mentions légales · Confidentialité · Accessibilité · Plan du site · 404.

## Activer la réception des candidatures (5 minutes)

Les formulaires envoient vers `/api/submit` (`api/submit.js`). Dans Vercel → **Settings → Environment Variables** :

| Variable | Valeur |
|---|---|
| `RESEND_API_KEY` | clé API gratuite créée sur [resend.com](https://resend.com) |
| `ADMISSIONS_EMAIL` | adresse qui reçoit les candidatures (pour l'adresse d'expédition de test de Resend : l'e-mail du compte Resend) |
| `MAIL_FROM` *(facultatif)* | expéditeur sur un domaine vérifié dans Resend |
| `SEND_CONFIRMATION` *(facultatif)* | `1` pour envoyer un accusé de réception au candidat (nécessite `MAIL_FROM`) |
| `WEBHOOK_URL` *(facultatif)* | reçoit chaque envoi en JSON (Google Sheets, Make, Zapier…) |

Puis **Redeploy**. Chaque candidature arrive par e-mail avec une référence (`A21-AAMMJJ-XXXX`) et le CV en pièce jointe.
Tant que rien n'est configuré, le site propose automatiquement au visiteur l'envoi par e-mail et le téléchargement de son récapitulatif.

## Modifier le site

Les pages sont générées par `tools/` (en-tête, pied et composants communs) :

```bash
python3 tools/build_pages.py     # régénère les 19 pages
python3 -m http.server           # aperçu sur http://localhost:8000 (sans l'API)
```

- Coordonnées : `CONTACT_EMAIL` dans `tools/components.py`.
- Photos : `assets/img/photos/` (dictionnaire `PHOTOS` dans `tools/components.py`).
- Styles : `assets/css/styles.css` · Interactions : `assets/js/main.js`.

## Accessibilité & qualité

RGAA 4.1 / WCAG 2.2 AA visés : lien d'évitement, navigation clavier, focus visible, contrastes vérifiés, cibles ≥ 44 px,
formulaires avec erreurs liées et récapitulatif, `prefers-reduced-motion`, fonctionnement sans JavaScript.
Polices auto-hébergées (aucun service tiers, aucun cookie).

## À compléter

Mentions légales (raison sociale, siège, SIRET, n° de déclaration d'activité, directeur de publication),
adresse postale, confirmation de l'adresse `admissions@academy21france.fr`.
