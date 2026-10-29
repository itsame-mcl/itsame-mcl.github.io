---
title: "Le web, les standards et l'accessibilité"
description: "Les trois langages du web, les organismes de normalisation et les référentiels d'accessibilité (WCAG, RGAA)."
date: 2026-07-21T12:00:00+02:00
lastmod: 2026-07-21T12:00:00+02:00
tags: ["HTML", "CSS", "Accessibilité"]
categories: ["Formation"]
menu:
  sidebar:
    name: "Web, standards et accessibilité"
    identifier: web-standards-accessibility
    parent: html-css
    weight: 10
---

## 1.1. Trois langages complémentaires
Une page web moderne repose sur trois langages aux rôles bien distincts :

- **HTML** (HyperText Markup Language) décrit le **contenu** et sa **structure** : titres, paragraphes, images, liens, tableaux, formulaires…
- **CSS** (Cascading Style Sheets) décrit la **présentation** : couleurs, polices, dimensions, positionnement des éléments.
- **JavaScript** apporte l'**interactivité** : réaction aux actions de l'utilisateur, modification dynamique de la page. Il n'est pas traité dans cette formation.

Cette séparation des responsabilités est un principe fondamental : un document HTML doit rester compréhensible et utilisable même sans CSS ni JavaScript. C'est aussi la base de l'accessibilité et du référencement.

## 1.2. Qui définit les standards ?
Le **W3C** (World Wide Web Consortium) et le **WHATWG** (Web Hypertext Application Technology Working Group) sont les deux organismes qui normalisent les technologies du web.

- Depuis 2019, la spécification HTML est maintenue exclusivement par le WHATWG sous la forme d'un **standard vivant** (HTML Living Standard, consultable sur html.spec.whatwg.org) : il n'y aura pas de « HTML 6 », le standard évolue en continu. « HTML 5 » reste le nom d'usage.
- **CSS** n'est plus un bloc monolithique : depuis « CSS 3 », la spécification est découpée en **modules** (sélecteurs, flexbox, grid, media queries…) qui évoluent chacun à leur rythme. « CSS 3 » reste, là aussi, le nom d'usage courant.

{{< alert type="note" >}}
Conséquence pratique : la bonne référence au quotidien n'est pas la spécification elle-même, mais **MDN Web Docs**, qui documente chaque balise et chaque propriété avec son état de compatibilité. Le site caniuse.com permet de vérifier le support d'une fonctionnalité par les navigateurs.
{{< /alert >}}

## 1.3. L'accessibilité numérique : un fil rouge, pas une option
L'accessibilité numérique consiste à rendre les contenus et services web utilisables par tous, y compris les personnes en situation de handicap : déficiences visuelles (cécité, malvoyance, daltonisme), auditives, motrices (navigation au clavier seul) ou cognitives. Elle bénéficie en réalité à tous les utilisateurs : navigation au clavier, sous-titres, contrastes lisibles en plein soleil, pages plus rapides.

### Les référentiels
- **WCAG** (Web Content Accessibility Guidelines) : le référentiel international du W3C. La version en vigueur est **WCAG 2.2** (recommandation depuis octobre 2023), organisée autour de 4 principes : perceptible, utilisable, compréhensible, robuste. Trois niveaux de conformité existent : A, AA (le niveau généralement exigé) et AAA.
- **RGAA** (Référentiel Général d'Amélioration de l'Accessibilité) : la déclinaison française, obligatoire pour les services publics et les grandes entreprises. La version en vigueur est le **RGAA 4.1.2** (106 critères) ; une version 5, alignée sur WCAG 2.2, est annoncée pour fin 2026.
- En Europe, l'**European Accessibility Act** (directive 2019/882, applicable depuis juin 2025) étend les obligations d'accessibilité à de nombreux services privés (e-commerce, banque, transport…).

{{< alert type="a11y" >}}
Tout au long de ce support, les encadrés verts comme celui-ci signalent les bonnes pratiques d'accessibilité liées au point de cours. L'accessibilité ne s'ajoute pas à la fin d'un projet : elle se construit à chaque ligne de code.
{{< /alert >}}

### Quatre réflexes à acquérir dès aujourd'hui
- Utiliser les balises pour leur **sens**, pas pour leur apparence (la mise en forme relève de CSS).
- Toujours fournir une **alternative textuelle** aux contenus non textuels (images, icônes).
- Veiller à ce que tout soit utilisable **au clavier seul**.
- Garantir des **contrastes** suffisants entre texte et fond.

{{< alert type="try" >}}
Une démonstration vaut tous les discours : écoutez une trentaine de secondes d'une page mal structurée (sans titres, sans repères de navigation, images sans alternative) avec un lecteur d'écran comme NVDA, gratuit sous Windows. L'effet est saisissant.
{{< /alert >}}
