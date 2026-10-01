# Academy 21 University — maquettes du site

Site statique (HTML/CSS/JS, sans dépendance) conçu à partir des brochures officielles :
Bachelor, Mastère, Executive MBA et fiche prospective IA & Marketing de réseau.

## Pages

| Fichier | Contenu |
|---|---|
| `index.html` | Accueil : hero, recherche rapide, ambition, filière, programmes, pédagogie, modalités, admissions |
| `formations.html` | Catalogue filtrable (niveau, modalité) + tableau comparatif |
| `bachelor.html` | Bachelor Management Stratégique & Opérationnel — Bac+3, RNCP38666 |
| `mastere.html` | Mastère Stratégie, Leadership & Transformation — Bac+5, RNCP39994 (onglets M1/M2) |
| `executive-mba.html` | Executive MBA Gouvernance, Leadership & Transformation |
| `ia-marketing-reseau.html` | Formation courte IA appliquée au marketing de réseau |
| `admissions.html` | Processus, conditions par programme, FAQ |
| `contact.html` | Formulaire candidature / brochure avec validation accessible |
| `charte.html` | Charte graphique : logo, couleurs, contrastes, typographies, composants |

## Charte

- **Logo** : extrait des brochures (`assets/img/`) — version couleur, version fond sombre, emblème « 21 », favicon.
- **Couleurs** : navy `#172033`, rouge `#B71C1C`, or `#9A7B3F` (brochures) ; rouge `#DA0612`, jaune `#FCCD01`, vert `#A7DD63`, bleu `#2F86AB` (logo).
- **Typographies** (Google Fonts) : Plus Jakarta Sans (titres), Inter (texte), Source Serif 4 italique (sous-titres/citations).

## Accessibilité (RGAA 4.1 / WCAG 2.2 AA)

Lien d'évitement, repères ARIA, focus visible, cibles ≥ 44 px, contrastes vérifiés, tableaux légendés,
onglets au clavier, formulaire avec erreurs liées et récapitulatif, `prefers-reduced-motion`, fonctionnement sans JS.

## Modifier

Les pages sont générées par `tools/build_pages.py` (en-tête et pied communs) :

```bash
python3 tools/build_pages.py
python3 -m http.server   # puis http://localhost:8000
```

## À compléter

Adresse, téléphone, e-mail (`admissions@a21-university.example`), liens réseaux sociaux, mentions légales,
politique de confidentialité, envoi réel du formulaire, photos (le disque du hero accepte une image `.photo`).
