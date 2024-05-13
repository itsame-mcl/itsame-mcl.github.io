---
title: "Positionnement des éléments en CSS"
date: 2024-05-13T12:00:00+01:00
tags: ["CSS 3"]
categories: ["Formation"]
menu:
  sidebar:
    name: CSS - Positionnement
    identifier: css-positioning
    parent: html-css
    weight: 60
---

## Principes du positionnement en CSS

Par défaut, le positionnement des objets s'effectue de manière dite statique, ou dans le flux.
Cela implique que :

- les éléments en ligne s'enchaînent à la suite, autant que possible sur la même ligne.
- les éléments de type bloc se positionnent les uns en dessous des autres, les marges externes supérieures et inférieures étant fusionnées.

Par défaut, les éléments ont pour hauteur celle de tous les éléments dans le flux qu'ils contiennent, et 0 si ils sont vides ou ne contiennent que des éléments hors du flux.
La largeur par défaut des élements dépend de leur type : pour les éléments de type bloc, il s'agit de celle de le élément parent, alors que pour les éléments en ligne, il s'agit de celle de leur contenu.

Seuls les éléments de type bloc ou de type en ligne dimensionnables peuvent recevoir un autre type de dimensionnement, hors du flux.

