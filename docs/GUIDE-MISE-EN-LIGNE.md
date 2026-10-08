# Mise en ligne chez Hostinger — guide pas à pas

Ordre conseillé (chaque étape dépend de la précédente) :

1. Compte Hostinger → 2. Abonnement + nom de domaine → 3. Adresses e-mail → 4. Comptes Stripe et Flutterwave →
5. Déploiement du site → 6. Variables d'environnement → 7. Domaine + SSL → 8. Tests → 9. Passage en réel.

Comptez une demi-journée, plus les délais de validation de Stripe et Flutterwave (quelques jours).

---

## 1. Créer le compte Hostinger (avec votre adresse personnelle)

C'est normal de commencer avec votre adresse : les adresses de l'école n'existent pas encore.
Elles seront créées à l'étape 3, et vous pourrez ensuite ajouter un accès ou changer l'adresse du compte.

1. Allez sur <https://www.hostinger.fr> → **Se connecter** → **Créer un compte**.
2. Activez la **double authentification** : avatar en haut à droite → **Profil → Sécurité** (ce compte contrôlera le site, les e-mails et le domaine : il doit être bien protégé).

## 2. Acheter l'hébergement et le nom de domaine

**Offre à choisir : « Business » (hébergement web).** C'est la moins chère qui accepte Node.js, indispensable pour les
formulaires, les e-mails et le paiement. L'offre « Premium » / « Single » ne suffit pas.

1. <https://www.hostinger.fr/hebergement-web> → offre **Business** → **Ajouter au panier**.
2. Durée : la plus longue que vous acceptez (12, 24 ou 48 mois). Le prix mensuel affiché est un prix de lancement :
   **regardez le prix de renouvellement** indiqué en petit.
3. **Nom de domaine retenu : `a21businessschool.com`** (offert la première année avec le pack de 48 mois).
   Saisissez-le dans « Sécurisez votre nom de domaine » pendant la commande. Facultatif : réservez aussi
   `a21businessschool.fr` pour protéger le nom (il redirigera vers le .com).
4. Cochez la **protection WHOIS** (gratuite : votre nom et votre adresse ne sont pas publiés).
5. Payez, puis suivez l'assistant : quand il propose de créer un site WordPress ou avec un constructeur, **passez cette étape**.

## 3. Créer les adresses e-mail de l'école

1. hPanel → **E-mails** → choisissez le domaine → **Créer un compte e-mail**.
2. Créez par exemple (5 à 6 boîtes) :

| Adresse | Rôle |
|---|---|
| `noreply@a21businessschool.com` | **envoie** les e-mails du site (accusés de réception, liens de paiement, reçus) |
| `admissions@a21businessschool.com` | **reçoit** les candidatures et les confirmations de paiement |
| `contact@a21businessschool.com` | adresse affichée sur le site |
| `direction@`, `pedagogie@`, `comptabilite@`… | selon vos besoins |

3. Notez chaque mot de passe dans un gestionnaire de mots de passe.
4. Lisez vos e-mails sur <https://mail.hostinger.com> (ou ajoutez-les sur votre téléphone : Hostinger affiche les réglages).
5. **Anti-spam** : hPanel → **Domaines → DNS / Serveurs de noms**. Vérifiez qu'il existe des lignes **SPF** et **DKIM**
   (Hostinger les ajoute en principe automatiquement). Ajoutez une ligne **DMARC** si elle manque :
   type `TXT`, nom `_dmarc`, valeur `v=DMARC1; p=none; rua=mailto:admissions@a21businessschool.com`.
   Sans elles, les e-mails du site risquent d'arriver en spam.

**Envoyez-moi l'adresse à afficher sur le site** (par exemple `contact@…`) : je la remplace dans toutes les pages.

## 4. Créer les comptes de paiement (avec une adresse de l'école)

### 4a. Stripe — carte bancaire (entité France)

1. <https://dashboard.stripe.com/register> avec `admissions@a21businessschool.com` (ou `comptabilite@`).
2. Restez d'abord en **mode test** (interrupteur « Mode test » en haut du tableau de bord).
3. **Clé secrète** : **Développeurs → Clés API → Clé secrète → Révéler** → elle commence par `sk_test_…`.
   Ne la partagez jamais (ni par e-mail, ni dans un message) : elle se colle uniquement dans Hostinger (étape 6).
4. **Webhook** (après l'étape 7, quand le domaine fonctionne) : **Développeurs → Webhooks → Ajouter une destination** →
   URL `https://a21businessschool.com/api/stripe-webhook` → événements `checkout.session.completed` et
   `checkout.session.async_payment_succeeded`.
5. **Activer le compte** pour encaisser réellement : **Paramètres → Activer les paiements** (informations de la société,
   représentant légal, IBAN de l'académie). Stripe vérifie aussi le site : les mentions légales doivent être complètes.

### 4b. Flutterwave — Orange Money et MTN MoMo (entité Cameroun)

1. <https://dashboard.flutterwave.com/signup> avec une adresse de l'école, **pays : Cameroun**, au nom de la structure camerounaise.
2. Fournissez les documents demandés (KYC : registre de commerce, pièce du dirigeant, compte bancaire ou Mobile Money de versement).
3. **Clé secrète** : **Settings → API Keys** (en mode test) → **Secret key** `FLWSECK_TEST-…`.
4. **Webhook** (après l'étape 7) : **Settings → Webhooks** → URL `https://a21businessschool.com/api/flutterwave` →
   **Secret hash** : inventez une phrase secrète (la même que `FLW_WEBHOOK_HASH` à l'étape 6) → **Save**.
5. Demandez par écrit la **commission** appliquée à Orange Money et MTN MoMo au Cameroun.

## 5. Déployer le site sur Hostinger

1. **Préparer GitHub** : le site est sur la branche `claude/2i-academy-design-pages-ru5nhc` du dépôt `dosy237/2i_academy`.
   Le plus propre est de la fusionner dans `main` (je peux préparer la demande de fusion) et de déployer `main`.
2. hPanel → **Sites web → Ajouter un site web** → **Application web Node.js**.
3. **Importer un dépôt Git** → **Connecter GitHub** → autorisez Hostinger sur le dépôt `2i_academy` → **Déployer**.
4. Vérifiez les réglages proposés :

| Réglage | Valeur |
|---|---|
| Branche | `main` (ou la branche du site) |
| Version de Node.js | **20** ou **22** |
| Commande d'installation | `npm install` |
| Commande de build | *(vide — le site n'a pas d'étape de construction)* |
| Fichier d'entrée / commande de démarrage | `server.js` / `npm start` |

5. **Déployer**. Hostinger attribue d'abord une **adresse temporaire** : ouvrez-la, le site doit s'afficher.
6. Ensuite, chaque modification poussée sur la branche est redéployée automatiquement.

## 6. Renseigner les variables d'environnement

Tableau de bord de l'application Node.js → menu de gauche **Variables d'environnement** → **Ajouter une variable**
(une par ligne). Elles restent enregistrées entre les déploiements. Après un ajout ou une modification : **Redéployer**.

| Variable | Valeur | |
|---|---|---|
| `SITE_URL` | `https://a21businessschool.com` | |
| `SMTP_HOST` | `smtp.hostinger.com` | e-mails |
| `SMTP_PORT` | `465` | e-mails |
| `SMTP_USER` | `noreply@a21businessschool.com` | e-mails |
| `SMTP_PASS` | mot de passe de cette boîte | e-mails |
| `MAIL_FROM_NAME` | `Academy 21 University` | e-mails |
| `ADMISSIONS_EMAIL` | `admissions@a21businessschool.com` (plusieurs : séparées par des virgules) | e-mails |
| `COPY_EMAIL` | votre adresse (copie de chaque envoi) | e-mails |
| `PAYMENT_SECRET` | 40 caractères aléatoires (générateur de mots de passe), **ne plus jamais la changer** sinon les liens déjà envoyés deviennent invalides | paiement |
| `ADMIN_KEY` | la clé de l'espace école, 16 caractères ou plus, à ne donner qu'à l'équipe d'admission | paiement |
| `STRIPE_SECRET_KEY` | `sk_test_…` (puis `sk_live_…`) | carte |
| `FLW_SECRET_KEY` | `FLWSECK_TEST-…` (puis la clé réelle) | Mobile Money |
| `FLW_WEBHOOK_HASH` | la phrase secrète saisie dans Flutterwave | Mobile Money |
| `MOBILE_CURRENCIES` | `XAF` (Cameroun) ; `XAF,XOF` si Flutterwave active aussi l'Afrique de l'Ouest | Mobile Money |

## 7. Brancher le nom de domaine et le HTTPS

1. Tableau de bord de l'application → **Domaines** (ou **Connecter un domaine**) → choisissez votre domaine.
   Comme il est acheté chez Hostinger, les réglages DNS se font automatiquement. Prévoyez de quelques minutes à quelques heures.
2. **SSL** : hPanel → **Sécurité → SSL** → installez le certificat gratuit pour `a21businessschool.com` et `www.a21businessschool.com`.
3. Vérifiez : `https://a21businessschool.com` affiche le site avec le cadenas.
4. Retournez à l'étape 4 pour créer les **webhooks** Stripe et Flutterwave avec ce domaine.

## 8. Tester (en mode test : aucun argent réel)

**E-mails**
1. Page **Contact** : envoyez un message → `admissions@` le reçoit, la copie arrive, l'accusé de réception arrive chez l'expéditeur.
2. Page **Candidature** : envoyez une candidature avec un CV → même vérification ; l'e-mail reçu par l'école contient
   le lien « Envoyer au candidat le lien de paiement ».
3. Regardez aussi le dossier **spam**. S'il y en a, revoyez SPF/DKIM/DMARC (étape 3).

**Paiements**
1. `https://a21businessschool.com/espace-ecole.html` → clé `ADMIN_KEY` → votre propre adresse → **Créer et envoyer le lien**.
2. Ouvrez l'e-mail reçu → **Accéder à mon espace de paiement**.
3. **Carte** : numéro `4242 4242 4242 4242`, date future, CVC `123` → page « paiement confirmé » + e-mails à l'école et au candidat.
4. **Mobile Money** : suivez les instructions de test affichées par Flutterwave → même vérification.
5. Contrôlez les paiements dans les tableaux de bord Stripe et Flutterwave (mode test).

## 9. Passer en réel

1. Comptes Stripe et Flutterwave **activés** (documents validés).
2. Remplacez `STRIPE_SECRET_KEY` et `FLW_SECRET_KEY` par les **clés réelles** → **Redéployer**.
3. Recréez les deux **webhooks en mode réel** (ils sont séparés de ceux du mode test).
4. Faites un vrai paiement de contrôle, puis remboursez-le depuis le tableau de bord.
5. Virements vers la banque : Stripe → **Paramètres → Virements** (automatiques, quotidiens) ; Flutterwave → **Settlements**
   (règlement automatique vers le compte de l'académie).

## Avant l'ouverture au public

- [x] Adresse affichée sur le site : admin@academy21france.fr.
- [x] Mentions légales (raison sociale, siège, SIRET, capital, directeur de publication).
- [ ] Phrase sur les frais d'étude de dossier (remboursables ou non) dans les mentions / conditions.
- [ ] Désactiver l'ancien déploiement Vercel une fois le domaine actif (éviter deux copies du site en ligne).

## Ensuite : référencement et accessibilité (prochaine étape de travail)

- Fichiers `robots.txt` et `sitemap.xml`, adresses canoniques, titres et descriptions travaillés page par page.
- Aperçus de partage (Open Graph : Facebook, LinkedIn, WhatsApp) et données structurées Google
  (`EducationalOrganization`, `Course` pour chaque formation, fil d'Ariane, FAQ).
- **Google Search Console** et **Bing Webmaster Tools** : validation du domaine, envoi du plan du site, suivi de l'indexation.
- **Fiche Google Business Profile** pour le Cameroun et pour la France.
- Performance (images optimisées en WebP, poids des pages) : critère de classement Google.
- Contenus : mots-clés recherchés par les candidats (Bachelor management Cameroun, MBA à distance, etc.).
- Audit d'accessibilité **RGAA 4.1** complet, page par page, et déclaration d'accessibilité mise à jour.
