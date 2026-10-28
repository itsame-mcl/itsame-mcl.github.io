---
title: "Responsive design : s'adapter à tous les écrans"
description: "Meta viewport, dimensions fluides et media queries."
date: 2026-07-21T12:00:00+02:00
lastmod: 2026-07-21T12:00:00+02:00
tags: ["CSS"]
categories: ["Formation"]
menu:
  sidebar:
    name: "CSS - Responsive design"
    identifier: css-responsive
    parent: html-css
    weight: 70
---

## 9.1. Le principe
Plus de la moitié du trafic web mondial provient des téléphones. Le **responsive design** consiste à concevoir une page unique dont la mise en page s'adapte à la largeur de l'écran, plutôt que des sites séparés par appareil. Trois ingrédients : la balise meta viewport, des dimensions fluides, et les media queries.

## 9.2. La balise meta viewport
Sans instruction contraire, un navigateur mobile affiche la page comme sur un écran de bureau de ~980 px, puis dézoome. La balise suivante, à placer dans le `<head>` de **toutes** les pages, désactive ce comportement :

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

{{< alert type="warning" >}}
Ne jamais y ajouter `user-scalable=no` ou `maximum-scale=1` : empêcher le zoom viole les WCAG — les personnes malvoyantes en dépendent.
{{< /alert >}}

## 9.3. Dimensions fluides
Les largeurs fixes en pixels sont l'ennemi du responsive. Les bons réflexes :

- largeurs en `%`, `fr` ou via `flex`, plutôt qu'en `px` ;
- `max-width` plutôt que `width` : `main { max-width: 70rem; margin: 0 auto; }` centre le contenu et le limite sur grand écran sans le contraindre sur petit ;
- images fluides avec la règle devenue standard : `img { max-width: 100%; height: auto; }` ;
- grilles auto-adaptatives : `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));` crée autant de colonnes d'au moins 250 px que la largeur le permet — souvent sans aucune media query.

## 9.4. Les media queries
Une **media query** applique un groupe de règles sous condition, notamment de largeur de fenêtre :

```css
/* Styles de base : mobile d'abord */
nav ul {
    display: flex;
    flex-direction: column;
}
 
/* À partir de 768 px de large */
@media (min-width: 768px) {
    nav ul {
        flex-direction: row;
        gap: 2rem;
    }
}
```

L'approche recommandée est **mobile first** : les styles de base ciblent les petits écrans (mise en page en une colonne, naturellement produite par le flux), et les media queries `min-width` enrichissent progressivement la mise en page à mesure que l'écran s'élargit. Les seuils (breakpoints) usuels se situent autour de 600–768 px (tablette) et 1024–1200 px (bureau), mais doivent être choisis en fonction du contenu, pas d'appareils particuliers.

Les media queries permettent aussi de cibler l'impression (`@media print`) ou des préférences de l'utilisateur (voir chapitre 10).

{{< alert type="practice" >}}
L'exercice 13 du [TP CSS]({{< relref "tp-css" >}}) fait passer le site en responsive, selon la démarche mobile first.
{{< /alert >}}
