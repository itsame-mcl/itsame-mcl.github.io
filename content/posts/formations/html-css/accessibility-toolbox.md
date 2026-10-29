---
title: "Accessibilité et CSS : approfondissements et boîte à outils"
description: "Focus visible, préférences des utilisateurs, premiers pas avec ARIA et outils de vérification."
date: 2026-07-21T12:00:00+02:00
lastmod: 2026-07-21T12:00:00+02:00
tags: ["HTML", "CSS", "Accessibilité"]
categories: ["Formation"]
menu:
  sidebar:
    name: "Accessibilité - Boîte à outils"
    identifier: accessibility-toolbox
    parent: html-css
    weight: 80
---

## 10.1. CSS et accessibilité
### Le focus visible
Les utilisateurs au clavier repèrent leur position grâce au **contour de focus** que le navigateur dessine autour de l'élément actif. Le supprimer (`outline: none`) sans le remplacer rend le site inutilisable au clavier. Pour le personnaliser :

```css
a:focus-visible,
button:focus-visible {
    outline: 3px solid #1f4e79;
    outline-offset: 2px;
}
```

### Respecter les préférences de l'utilisateur
Deux media queries adaptent la page aux réglages du système d'exploitation :

```css
/* Réduire les animations pour les personnes sensibles au mouvement */
@media (prefers-reduced-motion: reduce) {
    * {
        animation: none;
        transition: none;
    }
}
 
/* Proposer un thème sombre */
@media (prefers-color-scheme: dark) {
    :root {
        --fond: #1a1a2e;
        --texte: #f0f0f0;
    }
}
```

### Masquer sans exclure
`display: none` et `visibility: hidden` retirent un contenu de l'écran **et** des lecteurs d'écran. Pour un texte destiné aux seuls lecteurs d'écran (préciser le contexte d'un bouton-icône, par exemple), on utilise une classe utilitaire consacrée, dite « sr-only », qui masque visuellement sans retirer de l'arbre d'accessibilité :

```css
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
    border: 0;
}
```

## 10.2. Premiers pas avec ARIA
**WAI-ARIA** est un ensemble d'attributs (`role=`, `aria-label=`, `aria-expanded=`…) qui complètent la sémantique HTML pour les composants dynamiques. La **première règle d'ARIA** est de ne pas en utiliser quand une balise HTML native fait le travail : `<button>` vaut infiniment mieux que `<div role="button">`, car il apporte gratuitement le focus clavier, l'activation par Entrée/Espace et l'annonce correcte. Aux débutants, on retiendra trois usages sûrs :

- `aria-label="…"` : donner un nom accessible à un élément sans texte visible (bouton-icône : `<button aria-label="Rechercher">🔍</button>`) ;
- `aria-current="page"` : signaler la page courante dans un menu de navigation ;
- `role="search"` sur le formulaire de recherche (ou mieux : la balise `<search>`, récemment ajoutée au standard).

{{< alert type="warning" >}}
Un ARIA mal employé est pire que pas d'ARIA du tout : il fait mentir la page aux technologies d'assistance. En cas de doute, s'en tenir au HTML sémantique.
{{< /alert >}}

## 10.3. La boîte à outils de vérification
- **Validation du code** : validator.w3.org (HTML) et jigsaw.w3.org/css-validator (CSS).
- **Audit automatique** : Lighthouse (intégré à Chrome/Edge, onglet « Audits »), extension axe DevTools, ou WAVE (wave.webaim.org). Attention : les outils automatiques ne détectent qu'environ un tiers des problèmes d'accessibilité — ils complètent les tests manuels, ils ne les remplacent pas.
- **Test clavier** : parcourir toute la page à la touche Tab — tout doit être atteignable, dans un ordre logique, avec un focus toujours visible.
- **Contrastes** : WebAIM Contrast Checker, ou l'inspecteur du navigateur.
- **Lecteur d'écran** : NVDA (gratuit, Windows) ou VoiceOver (macOS) pour une écoute réelle de ses pages.
- **Référentiels** : accessibilite.numerique.gouv.fr (RGAA), w3.org/WAI (WCAG, en français partiel).

## 10.4. Pour aller plus loin
- **MDN Web Docs** (developer.mozilla.org/fr) : la référence quotidienne, en français.
- **web.dev/learn** (Google) : parcours « Learn HTML », « Learn CSS », « Learn Accessibility ».
- **CSS-Tricks** : les guides visuels « A Complete Guide to Flexbox » et « A Complete Guide to Grid ».
- **Jeux d'apprentissage** : Flexbox Froggy et Grid Garden pour ancrer les réflexes de manière ludique.
- **caniuse.com** : compatibilité navigateurs de chaque fonctionnalité.
- **SEO et GEO** : la documentation Google Search Central (developers.google.com/search), qui couvre désormais aussi l'optimisation pour les fonctionnalités d'IA générative — la source à consulter avant toute « recette » GEO glanée ailleurs.

{{< alert type="practice" >}}
L'exercice 14 du [TP CSS]({{< relref "tp-css" >}}) clôt la formation par les finitions d'accessibilité et un audit final du site.
{{< /alert >}}
