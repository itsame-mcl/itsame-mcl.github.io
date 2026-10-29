---
title: HTML 5 & CSS 3
description: "Les fondamentaux du développement web : HTML 5, CSS 3, Flexbox, Grid, responsive design et accessibilité numérique."
lastmod: 2026-07-21T12:00:00+02:00
menu:
  sidebar:
    name: HTML 5 & CSS 3
    identifier: html-css
    parent: formations
    weight: 200
---

Cette formation présente les fondamentaux du développement web : structurer une page avec HTML 5, la mettre en forme avec CSS 3 et la rendre accessible à tous. Conçue pour deux journées de formation en présentiel, elle se lit aussi bien d'une traite que chapitre par chapitre. L'accessibilité numérique en est le fil rouge : elle est abordée à chaque étape plutôt que reléguée à la fin.

## Objectifs pédagogiques

À l'issue de cette formation, vous serez capable de :

- écrire une page web valide et bien structurée en HTML 5, en utilisant les balises sémantiques appropriées ;
- construire des tableaux de données et des formulaires accessibles ;
- mettre en forme une page à l'aide de CSS 3 : sélecteurs, modèle de boîte, texte, couleurs et arrière-plans ;
- réaliser des mises en page modernes avec Flexbox et CSS Grid, sans recourir aux techniques obsolètes ;
- adapter une page à toutes les tailles d'écran (responsive design) ;
- appliquer les bonnes pratiques d'accessibilité numérique (WCAG 2.2 / RGAA) à chaque étape du développement.

## Public et prérequis

Cette formation s'adresse à des développeurs débutants ou à des profils techniques n'ayant jamais (ou peu) pratiqué le développement web front-end. Aucune connaissance préalable de HTML ou de CSS n'est requise. Une familiarité avec la manipulation de fichiers et l'utilisation d'un éditeur de texte est suffisante.

## Matériel et environnement

- Un éditeur de code : Visual Studio Code (recommandé, avec l'extension Live Server), ou tout éditeur de texte.
- Un navigateur récent (Firefox ou Chrome/Edge) avec ses outils de développement (touche F12).
- Aucun serveur ni installation particulière : un fichier `.html` s'ouvre directement dans le navigateur.
- Sites de référence à garder ouverts : MDN Web Docs (developer.mozilla.org, en français) et le validateur du W3C (validator.w3.org).

{{< alert type="info" >}}
Ce support a été révisé en juillet 2026 : accessibilité (WCAG 2.2, RGAA), Flexbox, CSS Grid, variables CSS et responsive design y occupent désormais une place centrale.
{{< /alert >}}

## Mettre en pratique

Chaque chapitre se termine par les exercices à réaliser. Ils sont regroupés en deux pages de travaux pratiques, corrigés à l'appui : le [TP HTML]({{< relref "tp-html" >}}) (exercices 1 à 7) et le [TP CSS]({{< relref "tp-css" >}}) (exercices 8 à 14). Le fil rouge est la construction du mini-site touristique d'une ville de votre choix.

### Si le temps vous manque

Vous pouvez d'abord sauter les exercices bonus, puis traiter l'exercice 5 (tableau complexe) en lisant simplement son corrigé, puis l'exercice 12 (gabarit de page) de la même façon. En revanche, ne sautez jamais l'exercice 6 (le formulaire), les exercices 10 et 11 (Flexbox et Grid), l'exercice 13 (responsive) ni le test final au clavier : ils portent les objectifs centraux de la formation.

### Pour consolider

Une fois la formation terminée, vous pouvez prolonger le mini-site en plusieurs pages, puis vous relire une semaine plus tard avec une vingtaine de questions sur les pièges rencontrés (`alt` vide ou absent, spécificité, axes de Flexbox…). Pour la suite, notamment JavaScript, les parcours de [web.dev/learn](https://web.dev/learn) sont un bon point de départ.

## Ce qui a changé depuis la première version

Ces pages ont été révisées en juillet 2026. Si vous avez consulté la première version (2024), voici les principales corrections techniques apportées :

- **Flexbox** : les valeurs de `flex-direction` sont `row-reverse` et `column-reverse` ; `gap` est désormais utilisable en Flexbox.
- **`box-sizing`** : seules les valeurs `content-box` et `border-box` existent, `padding-box` ayant été retirée de la spécification.
- **Arrière-plans** : la propriété s'écrit `background-attachment`, de valeur par défaut `scroll` ; `background-size` a été ajoutée.
- **Unités** : `rem` et `em` sont définies par rapport à la **taille de police** (de la racine pour `rem`, de l'élément pour `em`).
- **Position** : ajout de `position: sticky` et précision sur `position: absolute` (relatif au plus proche ancêtre positionné).
- **Tableaux** : l'élément est `<thead>` ; `rowspan` et `colspan` sont des attributs HTML, non des propriétés CSS.
- **Formulaires** : ajout de `<select>`, de `autocomplete` (critère WCAG 2.2) et de mises en garde sur `placeholder`.
- **Métadonnées** : ajout de la balise `viewport`, indispensable ; la métadonnée `keywords` est obsolète.
- **Liens** : `accesskey` et `title` ne sont plus présentés comme des bonnes pratiques d'accessibilité.
- **Référentiels** : HTML est un standard vivant maintenu par le WHATWG ; l'accessibilité est alignée sur WCAG 2.2 et le RGAA 4.1.2.
