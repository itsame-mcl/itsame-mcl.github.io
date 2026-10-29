---
title: "Positionnement des éléments en CSS"
description: "Du flux normal aux grilles : position, flottants, Flexbox et CSS Grid."
date: 2024-05-13T12:00:00+01:00
lastmod: 2026-07-21T12:00:00+02:00
tags: ["CSS"]
categories: ["Formation"]
menu:
  sidebar:
    name: "CSS - Positionnement"
    identifier: css-positioning
    parent: html-css
    weight: 60
---

## 8.1. Le flux normal
Par défaut, les éléments se positionnent « dans le flux » : les blocs s'empilent verticalement (leurs marges verticales fusionnant), les éléments en ligne s'enchaînent horizontalement avec renvoi à la ligne automatique. Toute mise en page consiste à organiser des exceptions maîtrisées à ce flux — et les outils modernes pour le faire sont **Flexbox** et **Grid**.

## 8.2. La propriété position
`position` change le mode de positionnement d'un élément ; le décalage se règle ensuite avec `top`, `right`, `bottom` et `left` :

| **Valeur** | **Comportement** |
|---|---|
| `static` | Valeur par défaut : l'élément suit le flux normal, les propriétés de décalage sont ignorées. |
| `relative` | L'élément est décalé par rapport à sa position normale ; l'espace qu'il occupait dans le flux est conservé. |
| `absolute` | L'élément sort du flux et se positionne par rapport à son plus proche ancêtre lui-même positionné (toute valeur autre que `static`). À défaut, il se positionne par rapport à la page. D'où l'idiome classique : `position: relative` (sans décalage) sur le parent de référence. |
| `fixed` | L'élément sort du flux et se positionne par rapport à la fenêtre du navigateur : il ne bouge pas au défilement. |
| `sticky` | Hybride moderne : l'élément défile normalement, puis « se colle » au bord de la fenêtre quand il l'atteint (nécessite un seuil, ex. `top: 0`). Idéal pour un en-tête ou un sommaire qui reste visible. |

En cas de superposition, `z-index` détermine l'ordre d'empilement des éléments positionnés : la valeur la plus élevée s'affiche au-dessus.

{{< alert type="a11y" >}}
Attention à l'ordre de lecture : les positionnements sortent les éléments du flux **visuellement**, mais les lecteurs d'écran et la navigation au clavier suivent l'ordre du **code HTML**. L'ordre visuel doit rester cohérent avec l'ordre du document.
{{< /alert >}}

## 8.3. Flottants et colonnes multiples : l'héritage
La propriété `float` (`left`, `right`, `none`) pousse un élément sur le côté, le texte suivant l'habillant. La propriété `clear` (`left`, `right`, `both`) interrompt cet habillage. Avant Flexbox et Grid, les flottants servaient — par détournement — à construire des mises en page entières ; cet usage est aujourd'hui **obsolète**. `float` conserve un usage légitime et unique : faire habiller une image par du texte, comme dans un journal.

Le module multi-colonnes découpe pour sa part un bloc de texte en colonnes de journal : `column-count` (nombre de colonnes) ou `column-width` (largeur cible), et `column-gap` (gouttière, `1em` par défaut).

## 8.4. Flexbox : aligner sur un axe
Flexbox résout le problème de la répartition d'éléments **le long d'un axe** (horizontal ou vertical) : barres de navigation, groupes de boutons, cartes de même hauteur, centrage. Il suffit de donner `display: flex` à un bloc : il devient **conteneur flex**, et ses enfants directs deviennent des **éléments flex**.

### L'axe principal : flex-direction
La propriété `flex-direction`, posée sur le conteneur, choisit l'axe principal :

- `row` (défaut) : en ligne, dans le sens de lecture ;
- `row-reverse` : en ligne, sens inverse ;
- `column` : en colonne, de haut en bas ;
- `column-reverse` : en colonne, de bas en haut.

{{< alert type="warning" >}}
L'axe **croisé** (ou secondaire) est toujours perpendiculaire à l'axe principal. Toutes les propriétés d'alignement se définissent par rapport à ces axes, pas par rapport à l'horizontale et la verticale : `justify-content` aligne sur l'axe principal, `align-items` sur l'axe croisé — quel que soit `flex-direction`.
{{< /alert >}}

### Passage à la ligne : flex-wrap
Par défaut (`flex-wrap: nowrap`), les éléments se compriment pour tenir sur une seule ligne, quitte à déborder. `flex-wrap: wrap` autorise le passage à la ligne — la base des galeries de cartes qui se réorganisent selon la largeur d'écran.

### Espacement : gap
La propriété `gap` (et ses déclinaisons `row-gap`, `column-gap`) fixe l'espace entre les éléments flex, sans marge parasite en début ni fin de ligne. Elle remplace avantageusement les vieux bricolages à base de `margin` :

```css
nav ul {
    display: flex;
    gap: 1rem;
    list-style: none;
    margin: 0;
    padding: 0;
}
```

### Alignement sur l'axe principal : justify-content
- `flex-start` (défaut) : regroupés au début de l'axe ;
- `flex-end` : regroupés à la fin ;
- `center` : centrés ;
- `space-between` : répartis, premier et dernier collés aux extrémités ;
- `space-around` : répartis avec un demi-espace aux extrémités ;
- `space-evenly` : répartis avec des espaces strictement égaux partout.

### Alignement sur l'axe croisé : align-items
`stretch` (défaut : les éléments s'étirent sur toute la hauteur de la ligne — c'est lui qui donne des colonnes de même hauteur « gratuitement »), `flex-start`, `flex-end`, `center`, et `baseline` (alignement sur la ligne de base du texte). Un élément peut déroger à l'alignement commun avec `align-self`.

Le centrage parfait, casse-tête historique de CSS, tient désormais en trois lignes :

```css
.parent {
    display: flex;
    justify-content: center;  /* axe principal */
    align-items: center;      /* axe croisé */
}
```

### Dimensionnement des éléments : la propriété flex
Posée sur les **éléments** flex, la propriété raccourcie `flex` regroupe trois valeurs : `flex-grow` (part de l'espace excédentaire que l'élément peut absorber), `flex-shrink` (sa capacité à rétrécir) et `flex-basis` (sa taille de départ sur l'axe principal). En pratique, trois idiomes couvrent l'essentiel :

- `flex: 1` : tous les éléments qui portent cette valeur se partagent l'espace équitablement (des valeurs différentes créent des proportions : `flex: 2` prend deux fois plus que `flex: 1`) ;
- `flex: 200px` : taille de départ de 200 px, sans absorption de l'espace restant ;
- `flex: 1 200px` : taille de départ de 200 px, puis partage proportionnel de l'espace restant.

## 8.5. Grid : composer en deux dimensions
Là où Flexbox raisonne sur un axe, **CSS Grid** définit une véritable grille en **deux dimensions** — lignes et colonnes — dans laquelle on place les éléments. C'est l'outil des gabarits de page complets, qui normalise ce que des frameworks comme Bootstrap simulaient autrefois avec leurs grilles à 12 colonnes. Un conteneur de grille se déclare avec `display: grid` ; ses enfants directs deviennent des éléments de grille.

### Définir les colonnes et les lignes
`grid-template-columns` définit les colonnes par une liste de largeurs. Outre les unités habituelles, l'unité `fr` représente une fraction de l'espace disponible, et deux fonctions rendent la définition expressive :

- `repeat(n, valeur)` évite les répétitions : `repeat(3, 1fr)` crée trois colonnes égales ;
- `minmax(min, max)` borne une dimension : `minmax(200px, 1fr)`.

```css
.grille {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}
```

Les lignes se créent automatiquement à mesure que les éléments remplissent la grille ; leur hauteur par défaut est celle de leur contenu. `grid-auto-rows` impose une hauteur aux lignes implicites — `grid-auto-rows: minmax(100px, auto)` donnant un minimum de 100 px extensible. `grid-template-rows` définit explicitement les premières lignes. Comme en Flexbox, `gap` règle les gouttières.

### Placer les éléments
Par défaut, les éléments remplissent la grille dans l'ordre du document. Pour placer explicitement un élément, `grid-column` et `grid-row` indiquent les **lignes de séparation** (numérotées à partir de 1) de début et de fin, séparées par une barre oblique. Ainsi, `grid-column: 1 / 3` étend l'élément de la ligne de séparation 1 à la 3, soit sur les colonnes 1 et 2. La syntaxe `span n` (« s'étendre sur n pistes ») est souvent plus lisible : `grid-column: span 2`.

### Nommer les zones : grid-template-areas
Pour un gabarit de page, la propriété `grid-template-areas` permet de « dessiner » la grille en toutes lettres, chaque chaîne représentant une ligne :

```css
body {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-areas:
        "header header"
        "main   aside"
        "footer footer";
    gap: 1rem;
}
 
header { grid-area: header; }
main   { grid-area: main; }
aside  { grid-area: aside; }
footer { grid-area: footer; }
```

Ce gabarit se relit d'un coup d'œil et se réorganise en une seule règle dans une media query (chapitre 9) — c'est la méthode recommandée pour les gabarits de page.

### Flexbox ou Grid ?
| **Choisir Flexbox quand…** | **Choisir Grid quand…** |
|---|---|
| Le contenu s'organise le long d'**un axe** (menu, barre d'outils, rangée de boutons) | La mise en page se pense en **lignes et colonnes** simultanément (gabarit de page, galerie) |
| C'est le **contenu** qui doit dicter la répartition de l'espace | C'est la **structure** qui doit dicter le placement du contenu |
| On aligne ou centre quelques éléments | On veut des zones nommées et un placement explicite |

{{< alert type="note" >}}
Les deux se combinent naturellement : une page en Grid dont chaque zone organise son contenu interne en Flexbox est le schéma le plus courant des sites modernes.
{{< /alert >}}

{{< alert type="practice" >}}
Les exercices 10 à 12 du [TP CSS]({{< relref "tp-css" >}}) portent sur la navigation en Flexbox, une galerie en Grid et le gabarit d'une page.
{{< /alert >}}
