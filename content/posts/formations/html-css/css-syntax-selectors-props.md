---
title: "Syntaxe CSS 3, sélecteurs et propriétés usuelles"
date: 2024-05-12T21:00:00+01:00
tags: ["CSS 3"]
categories: ["Formation"]
menu:
  sidebar:
    name: CSS - Syntaxe, sélecteurs, propriétés
    identifier: css-syntax-selectors-props
    parent: html-css
    weight: 50
---

## Syntaxe de CSS 3

Une **feuille de style** CSS 3 se compose d'un ensemble de **blocs**.
Ces blocs sont introduits par un **sélecteur** qui précise à quels éléments HTML il s'applique, puis d'une ou plusieurs **déclarations**.
Une déclaration est une **propriété** choisie parmi celles de la norme CSS 3, suivie d'une **valeur** :
```css
selecteur-1 {
    propriete-1: valeur;
    propriete-2: valeur;
}

selecteur-2 {
    propriete-3: valeur;
}
```

De manière générale, CSS fonctionne avec une notion d'**héritage** : si un élément est inclus dans un autre, il hérite de toutes les règles de style qui l'affecte.

### Liaison entre un style CSS et un document HTML

La façon la plus commune de lier une feuille de style CSS avec un document HTML est de l'enregistrer sous la forme d'un fichier texte avec l'extension `.css`, puis de le lier au document HTML grâce à une balise `<link>`.

Il est également possible d'écrire la feuille de style CSS directement dans le document HTML au moyen d'une balise `<style>`  incluse dans le `<head>`. Cette pratique est cependant à éviter, en particulier pour un site multi-pages, car elle ne permet pas de mutualiser les règles de style entre plusieurs pages, et oblige à faire des duplications.

Enfin, les éléments HTML admettent un attribut `style=` qui permet de préciser directement des déclarations pour un élément. Cette pratique est également déconseillée, car il est souvent possible d'obtenir le même résultat grâce à la diversité des sélecteurs HTML disponibles.

## Sélecteurs

Les sélecteurs introduisent les blocs d'instructions CSS. Ils permettent de préciser à quels éléments HTML d'une page les déclarations du bloc doivent s'appliquer.
Il est possible d'utiliser plusieurs sélecteurs sur un même bloc en les séparant par des virgules (`,`).

### Sélecteur universel

Le sélecteur `*` permet d'appliquer un bloc à l'ensemble des éléments d'une page HTML. 

### Balises HTML

Les sélecteurs les plus simples reprennent le nom des balises HTML. Ils permettent d'appliquer un bloc à tous les éléments HTML définis par cette balise.

#### Exemple

```css
a {
    text-decoration: none;
}
```

Ce bloc CSS s'applique à tous les liens d'une page (balise `<a>`), et permet d'éviter leur affichage souligné.

### Identifiants et classes

Tous les éléments HTML peuvent être associés à un identifiant grâce à un attribut `id=` et à une ou plusieurs classes grâce à l'attribut `class=`.

Un identifiant doit être unique à l'échelle d'un document HTML, alors qu'une classe peut être attribuée à plusieurs éléments. Pour donner plusieurs classes à un même élément, il convient de les séparer par un espace.

Ces identifiants et classes peuvent ensuite être utilisés comme des sélecteurs CSS, en les préfixant d'un dièse (`#`) pour les identifiants, et d'un point (`.`) pour les classes :

```css
#identifiant {
    ...
}

.classe {
    ...
}
```

Il est possible de combiner une balise HTML et un identifiant ou une classe :

```css
a.non-souligne {
    text-decoration: none;
}
```

Dans cet exemple, seules les balises `<a>` ayant un attribut `class="non-souligne"` se veront privés de leur trait de soulignement.

### Pseudo-classes

Les pseudo-classes ne sont pas définies par un attribut `class=`, mais sont générées dynamiquement et automatiquement. Elles sont utilisables en tant que sélecteur CSS en les préfixant par deux-points (`:`).
Parmi les pseudo-classes usuelles, on trouve :

- `:first-child` : premier élément enfant d'un conteneur parent.
- `:nth-child(n)` : n-ième élément enfant d'un conteneur parent.
- `:last-child` : dernier élément enfant d'un conteneur parent.
- `:not(selecteur)` : tous les éléments qui ne sont pas compatibles avec le sélecteur indiqué.
- `:link` : liens hypertextes non visités.
- `:visited` : liens hypertextes déjà visités.
- `:hover` : élément actuellement survolé par le curseur.
- `:active` : élement actuellement actif (cliqué).

Les pseudo-classes peuvent également être utilisées en combinaison avec une balise HTML, un identifiant ou une classe.

### Pseudo-éléments

Les pseudo-éléments sont également générés de manière dynamique, et permettent de manipuler des éléments qui existent de manière implicite dans le document HTML. Ils se préfixent par deux deux-points (`::`).
Moins nombreux que les pseudo-classes, les 6 plus usuels sont :

- `::first-letter` : premier caractère d'un élément.
- `::first-line` : première ligne d'un élément.
- `::selection` : texte surligné/sélectionné par l'utilisateur.
- `::marker` : puces d'une liste non ordonnée.
- `::before` : S'utilise en combinaison avec un autre sélecteur et représente un pseudo-élément s'insérant juste avant.
- `::after` : S'utilise en combinaison avec un autre sélecteur et représente un pseudo-élément s'insérant juste après.

### Inclusion et juxtaposition

Il est également possible de construire des sélecteurs s'attachant aux relations d'inclusion ou de juxtaposition entre deux éléments.

- `element1 element2` permet de sélectionner tous les `element2` qui sont un enfant d'un `element1`, quel que soit le nombre d'éléments intermédiaires imbriqués.
- `element1 > element2` permet de sélectionner tous les `element2` qui sont des enfants directs d'un `element1`, sans aucun autre élément intermédiaire imbriqué.
- `element1 + element2` permet de sélectionner tous les `element2` qui sont directement juxtaposés à un `element1`.
Concrètement, cela signifie que la balise ouvrante de `element2` suit immédiatement la balise fermante de `element1`.

### Priorité entre les sélecteurs

Il existe plusieurs logiques de priorité entre les sélecteurs : d'une part, si deux blocs portent sur le même sélecteur et spécifient une valeur différente pour la même propriété, celui qui est décrit en second dans l'ordre de la feuille de style prime sur celui qui est écrit en premier.
De plus, un sélecteur portant sur un identifiant primera sur un autre portant sur une classe, qui primera lui-même sur un sélecteur simple.

Il est cependant possible de rendre une propriété prioritaire sur toutes les autres en y ajoutant `!important` après sa valeur, par exemple `text-decoration: none !important;`

## Propriétés usuelles

Il existe actuellement 520 propriétés CSS différentes, mais certaines sont plus usuelles que d'autres.

{{< alert type="info" >}} Les propriétés relatives au positionnement des blocs feront l'objet d'un chapitre spécifique. {{< /alert >}}

### Dimensions, bordures et marges

CSS est construit autour d'un modèle de "boîtes", qui définit la dimension totale d'un élément HTML. Cette boîte se compose de 4 éléments concentriques : le contenu, le padding (littéralement "rembourrage"), la bordure et la marge.

Plusieurs unités peuvent être utilisées pour définir ces dimensions. Les valeurs peuvent être entières ou décimales, le séparateur décimal étant le point (`.`).
Les unités les plus usuelles sont :

- `rem` : hauteur d'un caractère majuscule dans le nœud racine de la page (par défaut, 16 pixels)
- `em` : hauteur d'un caractère majuscule dans l'élément parent
- `px` : pixel
- `%` : taille relative soit à celle de l'élément parent (pour les éléments bloc), soit à la relation d'équivalence 1`em` = 100 % (pour les éléments en ligne)
- `vw` :  1 % de la largeur de la fenêtre du navigateur de l'utilisateur
- `vh` : 1 % de la hauteur de la fenêtre du navigateur de l'utilisateur
- `cm`, `mm` : centimètres et millimètres, utiles notamment pour des pages ayant vocation à être imprimées

#### Contenu

Le contenu étant au cœur de la boîte, sa dimension se définie simplement à partir de sa hauteur et de sa largeur :

- `width` : largeur du contenu
- `height` : hauteur du contenu

La valeur `auto` permet de conserver la valeur automatiquement calculée par défaut. Pour les éléments en ligne, seuls ceux dits dimensionnables (tels que `<img>`) peuvent avoir des valeurs fixées pour `width`et `height`.

#### Padding (marge interne)

La marge interne (padding) est la 2ᵉ couche du modèle de boîte. Par défaut, sa valeur est nulle. Les propriétés qui permettent de la définir sont les suivantes :

- `padding-top` : Marge interne supérieure
- `padding-bottom` Marge interne inférieure
- `padding-left` : Marge interne gauche
- `padding-right` : Marge interne droite

#### Bordure

Les bordures sont la 3ᵉ couche du modèle de boîte. Par défaut, les bordures sont désactivées et de taille nulle. Il convient donc de préciser à la fois la taille et le style des bordures. Ainsi, la valeur des propriétés liées aux bordures se décompose en 3 parties : dimension, style et couleur.

Sur le même modèle que la marge interne, les propriétés permettant de fixer les bordures sont `border-top`, `border-bottom`, `border-left` et `border-right`.

Le style de la bordure peut être précisé au moyen de plusieurs valeurs, les plus usuelles étant :

- `solid` : bordure pleine
- `double` : double bordure
- `dotted` : bordure en pointillés à base de points
- `dashed` : bordure en pointillés à base de tirets

#### Marge externe

La marge externe est la 4ᵉ et dernière couche du modèle de boîte. Elle se définit de la même manière que la marge interne, avec les propriétés `margin-top`, `margin-bottom`, `margin-left` et `margin-right`.

#### Raccourcis

Les propriétés sur le padding, la bordure et la marge admettent une version raccourcie, qui sont respectivement `padding`, `border-width` et `margin`. Elles peuvent être suivies de 1 à 4 valeurs permettant de préciser les dimensions :

- **1 valeur** : S'applique uniformément aux 4 côtés de la boîte.
- **2 valeurs** : la première valeur s'applique aux côtés supérieur et inférieur, la seconde aux côtés latéraux.
- **3 valeurs** : la première valeur s'applique au côté supérieur, la deuxième aux côtés latéraux et la troisième au côté inférieur.
- **4 valeurs** : la première valeur s'applique au côté supérieur, la deuxième au côté droit, la troisième au côté inférieur et la quatrième au côté gauche.

Pour les bordures, la propriété `border-width` est à compléter par la propriété `border-style` qui prend également de 1 à 4 valeurs de style. Si l'on souhaite utiliser la même valeur de dimension et de style pour les 4 côtés, il existe aussi la propriété `border`.

#### Box-sizing

La propriété `box-sizing` permet de modifier le comportement du modèle de boîte. Grâce à elle, il est possible de faire en sorte que les propriétés `width` et `height` englobent des couches en plus de celle du contenu principal, ce qui permet de simplifier la mise en page. Elle peut prendre 3 valeurs :

- `content-box` : comportement par défaut, `width` et `height` définissent les dimensions du contenu.
- `padding-box` : `width` et `height` définissent les dimensions du contenu et du padding.
- `border-box` : `width` et `height` définissent les dimensions du contenu, du padding et de la bordure.
Cette valeur est souvent utilisée, car elle permet de n'avoir ensuite à gérer que les marges extérieures.

#### Mode d'affichage

La propriété `display` permet de modifier le comportement d'un élément HTML. Elle est à utiliser avec précaution car elle peut parfois créer des résultats complexes à maintenir, mais permet de donner davantage de souplesse.
Ses principales valeurs sont :

- `block` : l'élément se comporte comme un élément bloc
- `inline` : l'élément se comporte comme un élément en ligne non dimensionnable
- `inline-block` : l'élément se comporte comme un élément en ligne dimensionnable

### Mise en forme du texte

Dans les éléments HTML contenant du texte, il est possible d'utiliser de nombreuses propriétés pour le mettre en forme.

#### Police

La police de caractères est fixée grâce à la propriété `font-family`.
Pour pouvoir être affichée, la police doit être installée sur l'ordinateur du client qui consulte la page web.

Il est donc possible et même recommandé de proposer une liste de plusieurs polices, séparées par une virgule.
Enfin, la liste de polices devrait se terminer par une police générique, proposée sur la plupart des systèmes.
Les plus usuelles sont `serif` (police à empattement, comme Times New Roman), `sans-serif` (police sans empattement, comme Arial) et `monospace` (police à largeur fixe, comme Courier).

Pour pouvoir utiliser des polices moins usuelles, il est également possible de les fournir directement au moyen d'un bloc `@font-face`. Il est nécessaire de disposer de la police dans un ou plusieurs des formats suivants : `woff2` (`.woff2`), `woff` (`.woff`), `opentype` (`.otf`, `.ttf`), `collection` (`.otc`, `.ttc`), `embedded-opentype` (`.eot`) ou `svg` (`.svg`, `.svgz`). 

Le bloc `@font-face` doit se composer de deux déclarations : `font-family` pour indiquer de la police, tel qu'il pourra être ensuite utilisé ailleurs dans la feuille de style, et `src` pour donner le chemin d'accès aux fichiers de la police :

```css
@font-face {
    font-family: "Police";
    src: local("Police"),
         url("police.woff2") format("woff2"),
         url("police.otf") format("opentype"),
         url("police.ttf") format("opentype");
}
```

La première ligne de `src` permet d'utiliser en priorité une version installée sur l'ordinateur du client si jamais il possède déjà cette police. Cela permet d'éviter des flux réseaux inutiles, car la police doit sinon être téléchargée par le client.

#### Taille et interligne

La taille de la police de caractères est fixée grâce à la propriété `font-size`. Les mêmes unités de mesure que pour le dimensionnement des éléments sont utilisables.

L'interligne est pour sa part fixé par la propriété `line-height`. Outre les unités de mesure habituelles, il est également possible de fixer une valeur sans unité (sur le modèle de celle des traitements de texte), `1` étant l'interligne minimal et `1.15` l'interligne standard.

#### Couleur

La couleur du texte est réglée par la propriété `color`. Elle admet plusieurs types de valeurs :

- un nom de couleur (en anglais), parmi les [140 noms actuellement disponibles](https://www.w3schools.com/colors/colors_names.asp) : `red`, `green`, `blue`...
- une valeur hexadécimale, au format `#aabbcc` (pour les valeurs de rouge, vert et bleu) ou `#aabbccdd` (rouge, vert, bleu, avec la transparence)
- une combinaison de couleurs rouge, vert, bleu avec des valeurs entre 0 et 255 ou en pourcentage : `rgb(rouge, vert, bleu)` ; ou `rgba(rouge, vert, bleu, alpha)` pour rajouter la transparence
- une combinaison teinte, saturation, luminosité : `hsl(teinte, saturation, luminosite)` ; ou `hsla(teinte, saturation, luminosite, alpha)` pour rajouter la transparence

#### Gras, italique, souligné

Trois propriétés permettent de gérer ces différents aspects de l'apparence du texte :

- `font-weight` : permet de modifier l'épaisseur de la police, la valeur `bold` étant la mise en gras.
- `font-style` : permet de modifier le style de la police, la valeur `italic` étant l'italique.
- `text-decoration` : permet d'appliquer des effets au texte, les valeurs usuelles étant `none` pour l'absence d'effet, `underline` pour le souligné ou `line-through` pour le texte barré.

#### Alignement et retrait

L'alignement du texte est paramétré par la propriété `text-align`. Ses valeurs sont semblables à celle d'un traitement de texte :

- `left` : aligné à gauche
- `right` : aligné à droite
- `center` : centré
- `justify` : justifié

Un retrait peut être fixé par la propriété `text-indent`, suivi d'une dimension (positive ou négative).

#### Casse

Il est également possible de modifier la casse d'un texte directement en CSS grâce à la propriété `text-transform`. Trois valeurs sont souvent utilisées : `lowercase` pour mettre le texte en minuscule, `uppercase` pour mettre le texte en majuscule et `capitalize` pour mettre la 1ʳᵉ lettre de chaque mot en majuscule.

### Arrière-plan

Deux approches sont possibles pour donner un arrière-plan à un élément : fixer une couleur de fond grâce à la propriété `background-color`, ou utiliser une image de fond.
Pour cette solution, plusieurs propriétés sont à utiliser :

- `background-image` : permet d'indiquer l'image à utiliser comme arrière-plan, avec une valeur au format `url(chemin/vers/image)`
- `background-repeat` : par défaut, l'image de fond se répète horizontalement et verticalement. Il est possible d'utiliser une répétition uniquement horizontale avec `repeat-x`, uniquement verticale avec `repeat-y` ou de désactiver la répétition avec `no-repeat`.
- `background-position` : permet de fixer la position de l'image de fond par rapport à l'élément auquel la propriété s'applique. La première valeur donne l'alignement horizontal et la seconde l'alignement vertical.
- `background-attachement` : permet de définir si l'image de fond doit défiler en même temps que l'élément auquel elle est liée (`local`), ou si elle doit rester fixe sur la page (`fixed`). 

Les images d'arrière-plan sont souvent utilisées aujourd'hui pour créer des fonds non unis, avec des motifs géométriques répétables.
Contrairement aux autres propriétés CSS, ces propriétés ne sont pas héritées par les éléments enfants.

### Listes

Des propriétés CSS permettent également de personnaliser les listes, notamment non ordonnées :

- `list-style-type` : permet de définir le style de puce. Les valeurs possibles sont `disc` pour des ronds pleins, `square` pour des carrés, ou alors tout caractère unique, y compris un emoji, comme `▶️`.
- `list-style-position` : permet de choisir si les puces sont à l'intérieur (`inside`) ou à l'extérieur (`outside`) de la boîte englobant la liste.
- `list-style-image` : permet d'utiliser une image comme puce, en précisant son url (`url(lien/vers/la/puce`))