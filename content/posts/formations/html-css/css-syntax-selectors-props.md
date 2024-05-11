---
title: "Syntaxe CSS 3, sélecteurs et propriétés usuelles"
date: 2024-05-11T11:30:00+01:00
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

Il existe plusieurs logiques de priorité entre les sélecteurs : d'une part, si deux blocs portent sur le même sélecteur, celui qui est décrit en second dans l'ordre de la feuille de style prime sur celui qui est écrit en premier.
De plus, un sélecteur portant sur un identifiant primera sur un autre portant sur une classe, qui primera lui-même sur un sélecteur simple.

Il est cependant possible de rendre une propriété prioritaire sur toutes les autres en y ajoutant `!important` après sa valeur, par exemple `text-decoration: none !important;`

## Propriétés usuelles

