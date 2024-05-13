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

## Flux de positionnement

### Positionnement dans le flux

Par défaut, le positionnement des objets s'effectue de manière dite statique, ou dans le flux.
Cela implique que :

- les éléments en ligne s'enchaînent à la suite, autant que possible sur la même ligne.
- les éléments de type bloc se positionnent les uns en dessous des autres, les marges externes supérieures et inférieures étant fusionnées.

Par défaut, les éléments ont pour hauteur celle de tous les éléments dans le flux qu'ils contiennent, et 0 si ils sont vides ou ne contiennent que des éléments hors du flux.
La largeur par défaut des élements dépend de leur type : pour les éléments de type bloc, il s'agit de celle de le élément parent, alors que pour les éléments en ligne, il s'agit de celle de leur contenu.

### Positionnement hors du flux

Seuls les éléments de type bloc ou de type en ligne dimensionnables peuvent recevoir un autre type de dimensionnement, hors du flux. La propriété CSS `position` permet de choisir le type de positionnement :

- `relative` : l'élément est positionné relativement à sa position dans le flux
- `absolute` : l'élément est positionné relativement à la position de son élément parent.
Ce positionnement ne fonctionne que si l'élement parent est lui même hors du flux; si ce n'est pas le cas, une solution simple consiste à positionner le parent en relatif avec un décalage nul. 
- `fixed` : l'élément est positionné relativement à l'écran. Ainsi, il ne bouge pas au défilement.

Le décalage est ensuite à régler à l'aide d'une combinaison des propritétés `left`, `right`, `top`et `bottom` qui permettent respectivement de décaler par rapport au côté gauche, droite, supérieur et inférieur.

Il est possible que ce type de positionnement engendre des superpositions. La propriété `z-index` permet de déterminer l'ordre des blocs dans cet empilement, le bloc ayant la valeur de `z-index` la plus élevée étant affiché au dessus des autres.

## Flottants et colonnes multiples

### Flottants
Le positionnement flottant permet de placer un élément le plus à gauche ou à droite possible de la page, tout en préservant son emplacement vertical dans le flux.

La propriété CSS concernée est `float`. Elle peut prendre pour valeur `left` pour un flottant à gauche, `right` pour un flottant à droite et `none` pour empêcher le flottement.

Il est aussi possible de préciser avec la propriété `clear` qu'un bloc doit interrompre les flottants, quitte à créer un espace vertical vierge. Elle peut prendre pour valeurs `left` pour interrompre les flottants à gauche, `right` pour ceux à droite et `both` pour interrompre tous les flottants.

### Colonnes multiples

CSS permet de diviser un bloc en colonnes multiples, en spécifiant un nombre de colonnes avec `column-count`, et/ou la largeur de chaque colonne avec `column-width`.

Par défaut, les colonnes sont espacées par une gouttière de largeur `1em`. Il est possible de fixer une autre largeur avec `column-gap`

## Nouvelles techniques de positionnement

### Flexbox

Le système de *flexbox* a été introduit dans la norme CSS 3 dans le but de simplifier la mise en page en permettant le positionnement des blocs selon un axe horizontal ou vertical.

Pour initialiser une flexbox, il suffit de donner la valeur `flex` à la propriété `display` d'un bloc, qui devient alors un conteneur flex (*flex container*). Tous ses blocs enfants directs deviennent ainsi des éléments flex (*flex items*).

#### Axe principal

L'axe principal d'une flexbox est l'axe selon lequel les éléments flex sont disposés.
Il est fixé au niveau du conteneur flex par la propriété `flex-direction` et peut prendre pour valeur :
- `row` pour une disposition selon l'axe horizontal (en ligne) dans le sens de lecture
- `reverse-row` pour une disposition selon l'axe horizontal (en ligne) dans le sens inverse du sens de lecture
- `column` pour une disposition selon l'axe vertical (en colonne) dans le sens de lecture
- `reverse-column`  pour une disposition selon l'axe vertical (en colonne) dans le sens inverse du sens de lecture

#### Débordement

Par défaut, s'il n'est pas possible de faire tenir tous les éléments flex le long de l'axe principal, les éléments supplémentaires débordent du conteneur flex.
Il est possible de modifier ce comportement pour faire un renvoi à la ligne ou à la colonne suivante en fixant la propriété `flex-wrap` à la valeur `wrap` dans le conteneur.

#### Dimensionnement des éléments flex

La propriété `flex` permet de paramétrer la dimension des éléments flex. Elle prend généralement une ou deux valeurs.

##### Cas d'une valeur unique
- Si la valeur est sans unité, elle agit comme un facteur de proportion entre les éléments flex (`flex-grow`) : si `flex` a la même valeur pour les éléments, alors ils se partagent équitablement l'axe principal. Sinon, ils se le partagent proportionnellement à la valeur de la propriété.
- Si la valeur est avec unité, elle représente la taille minimale de l'élément le long de l'axe principal (`flex-basis`).

##### Cas d'une valeur double
- La valeur avec unité représente la taille minimale de l'élément. Si une fois tous les éléments positionnés, il reste de l'espace disponible sur l'axe principal, il est partagé proportionnellement à la valeur sans unité.

#### Alignement

Il est également possible de paramétrer dans le conteneur flex l'alignement des éléments flex le long de l'axe principal ou de l'axe perpendiculaire (à l'axe principal).

##### Selon l'axe principal
L'alignement le long de l'axe principal s'effectue grâce à la propriété `justify-content`.
Les principales valeurs sont :
- `flex-start` : alignement depuis l'origine de l'axe principal
- `flex-end` : alignement depuis la fin de l'axe principal
- `center` : alignement autour du centre de l'axe principal
- `space-between` : alignement tout au long de l'axe principal, avec des espaces égaux entre chaque élément
- `space-around` : alignement tout au long de l'axe principal, avec des espaces égaux entre chaque élément et des demi-espaces au niveau des extrémités de l'axe
- `space-evenly` : alignement tout au long de l'axe principal, avec des espaces égaux entre chaque élément et aux extrémités de l'axe

##### Selon l'axe perpendiculaire (axe croisé)
L'alignement le long de l'axe perpendiculaire s'effectue grâce à la propriété `align-items`.
Il peut prendre les valeurs `flex-start`, `flex-end` et `center` avec un comportement similaire à celui de ces valeurs pour l'axe principal.
Sinon, l'alignement par défaut correspond à la valeur `stretch`, qui correspond à un étirement des éléments flex sur toute la longueur de l'axe perpendiculaire.
Enfin, la valeur `baseline` permet de positionner les éléments afin d'aligner la première ligne de texte de chaque élément le long de l'axe perpendiculaire.

Il est possible de modifier l'alignement selon l'axe perpendiculaire d'un élément flex en particulier en donnant à une valeur à sa propriété `align-self`. Les valeurs possibles sont les mêmes que pour `align-items`.

### Grilles

Les grilles CSS sont une autre solution moderne de positionnement.
Il s'agit d'une normalisation d'une pratique qui était déjà utilisée grâce à des frameworks CSS tels que [Bootstrap](https://getbootstrap.com/) qui proposait une grille à 12 colonnes.

Comme pour les flexbox, une grille s'initialise en donnant la valeur `grid` à la propriété `display` d'un élément, qui devient un conteneur de grille. Ses enfants directs sont des éléments de grille.

#### Colonnes de la grille

Par défaut, la trame de la grille se compose d'une seule colonne. Elle ne représente donc pas de différence avec le flux normal.

Pour spécifier le nombre de colonnes de la grille, il faut utiliser la propriété `grid-template-columns`. Elle prend en valeur une liste de dimensions, représentant la largeur de chaque colonne.
Ces dimensions peuvent utiliser les unités habituelles, mais aussi l'unité `fr`, qui représente une fraction de la largeur totale de la grille (sur le principe des dimensions sans unités de flexbox).

La largeur de la gouttière entre les colonnes de la grille se fixe avec la propriété `gap`.

#### Lignes de la grille

Par défaut, chaque ligne de la grille à la hauteur de son contenu. Il peut être utile de fixer une hauteur constante avec la propriété `grid-auto-rows`.
La valeur de cette propriété peut être fixée de manière à donner une hauteur minimale tout en gardant la flexibilité de s'adapter à un contenu plus haut grâce à la fonction `minmax`. Ainsi, `minmax(valeur, auto)` donne `valeur` comme minimum.

#### Positionnement des éléments

Les éléments de la grille peuvent être positionnés grâce aux propriétés `grid-column` pour les colonnes et `grid-row` pour les lignes.

Si un élément tient dans une seule ligne ou une seule colonne, il suffit de préciser le numéro de cette dernière en valeur, la numérotation commençant à 1.
Si l'élément s'étend sur plusieurs lignes ou colonnes, la valeur de la propriété devient `début / fin`.

La valeur de fin est à entendre comme le début de la colonne ou ligne suivante, ainsi, pour recouvrir 2 colonnes, on considère que l'élément va du début de la colonne 1 au début de la colonne 3, d'où la notation `1 / 3`;
