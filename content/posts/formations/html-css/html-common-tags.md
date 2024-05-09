---
title: "Principales balises HTML 5"
date: 2024-05-09T21:15:00+01:00
tags: ["HTML 5"]
categories: ["Formation"]
menu:
  sidebar:
    name: HTML - Principales balises
    identifier: html-common-tags
    parent: html-css
    weight: 30
---

Le principe de HTML 5 est de proposer un ensemble normé d'éléments représentés par des balises XML, dont les règles d'interprétation sont censées être implémentées de manière homogène entre tous les clients HTML (et notamment, les navigateurs).

La version actuellement en vigueur du standard HTML 5 est [publiquement consultable](https://html.spec.whatwg.org/). Néanmoins, il n'est pas utile dans un cadre général de connaître toutes les balises, certains étant beaucoup plus usuelles que d'autres.

## Typologie des éléments HTML

Les éléments HTML 5 se décomposent en 2 grandes familles : les éléments de type **bloc**, et les éléments **en ligne** (*inline*) :

- Les éléments **bloc** délimitent des sections de la page. Par défaut, ils occupent toute la largeur de la page et se succèdent verticalement, dans l'ordre où ils sont décrits dans le document HTML, et sont séparés par un retour à la ligne.
- Les éléments **en ligne** s'inscrivent dans la continuité du flux de la page. Par défaut, ils occupent la taille minimale nécessaire à leur affichage, et ne provoquent aucun retour à la ligne.

{{< alert type="warning" >}} Les éléments en ligne peuvent être imbriqués, mais ne peuvent en aucun cas contenir d'élément bloc. {{< /alert >}}
En revanche, des éléments blocs peuvent être imbriqués entre eux et contenir des éléments en ligne.

## Élements usuels de type bloc

### Titres et intertitres

Les balises `<h1>` a `<h6>` permettent de définir jusqu'à 6 niveaux de titres et inter-titres au sein d'une page web.

### Paragraphes

Un paragraphe standard, contenant du texte et autres éléments, est délimité par une balise `<p>`. Il existe cependant d'autres types de paragraphes :

- `<pre>` : texte préformaté, permettant de préserver les retours à la ligne et les espaces tels que définis dans le texte.
- `<blockquote>` : citation d'une autre source, ou d'une autre page web (pouvant être précisée par un attribute `cite=`). Généralement mis en retrait dans l'affichage par défaut des navigateurs.
- `<address>` : paragraphe dédié à des informations de contact ou à une adresse postale.

### Listes

Toutes les balises liées aux listes sont des balises de type bloc.
Il existe trois types de listes :

- Liste ordonnée : il s'agit d'une liste dont tous les éléments sont numérotés. Elle s'initialise par une balise `<ol>` (*ordered list*). Cette numérotation peut être personnalisée de plusieurs manières grâce à des attributs :
  - `start=` permet de définir la 1ʳᵉ valeur de la liste.
  - `type=` permet de préciser le type de numérotation à utiliser, les types possibles étant `1`, `A`, `a`, `I` et `i`.
  - `reversed` permet de retourner l'ordre de numérotation (qui est croissant par défaut)
- Liste à puces : dans cette liste, chaque élément est précédé par une puce (par défaut, un point épais), sans qu'il n'y ait nécessairement d'ordre. Ce type de liste se déclare avec une balise `<ul>` (*unordered list*)

Chaque ligne à l'intérieur de ces deux types de liste se définit par une balise `<li>` (*list item*). L'attribut `value=` permet de donner une valeur spécifique à une ligne dans une liste ordonnée.

#### Exemple
```html
<ol type="I">
  <li>Élément I</li>
  <li>Élement II</li>
  <li value="V">Élément V</li>
</ol>
```

- Liste de définitions : cette liste permet de définir un glossaire, ou plus généralement une liste d'éléments associés à leur définition. Elle s'initialise avec la balise `<dl>` (*description list*). Chaque élément est ensuite introduit par une balise `<dt>` (*description term*), puis sa définition est précisée grâce à une balise `<dd>` (*description term description*).

#### Exemple
```html
<dl>
  <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
    <dd>Cascading Style Sheets</dd>
</dl>
```

### Élements sémantiques et élément neutre

Les éléments sémantiques (présentés dans le chapitre précédent) sont des éléments de type bloc : `<main>`, `<section>`, `<article>`, `<aside>`, `<nav>`, `<menu>`, `<header>`, `<footer>`

Enfin, HTML 5 propose un élément neutre de type bloc : `<div>`. Il est très utile pour pouvoir délimiter des blocs qui n'ont pas de sens sémantique, mais auxquels doivent s'appliquer des règles différentes de mise en forme. Dans l'idéal, il convient de n'utiliser `div` que lorsqu'il n'existe pas de balise permettant de décrire correctement le sens d'un bloc.

{{< alert type="info" >}} Les tableaux et formulaires, qui sont également des balises de type bloc, sont traités dans un chapitre dédié. {{< /alert >}}

## Éléments usuels de type en ligne

### Emphases

- L'emphase faible se déclare au moyen d'une balise `<em>`. Par défaut, cette emphase est représentée par l'italique.
- L'emphase forte se déclare au moyen d'une balise `<strong>`. Par défaut, cette emphase est représentée par la mise en gras.

À noter que ces balises ont avant tout un sens sémantique, car le comportement de mise en italique ou en gras peut être modifié par la feuille de style.
Il existe également des balises `<i>` et `<b>` permettant de demander une mise en italique ou en gras (*bold*), sans sens sémantique.

### Exposants et indices

- Un exposant (caractères occupant uniquement la moitié supérieure de la ligne de texte) est déclaré par la balise `<sup>` (*superscript*).
- Un indice (caractères occupant uniquement la moitié inférieure de la ligne de texte) est déclaré par la balise `<sub>` (*subscript*).

### Liens hypertextes

Un lien hypertexte est délimité au moyen d'une balise `<a>`.

L'attribut `href=` permet de définir la cible du lien, qu'il s'agisse d'une autre page web, ou d'un autre emplacement de la même page. Il est obligatoire.

Pour cibler un élément de la même page (une ancre), cet élément doit avoir un attribut `id=`, ayant pour valeur un nom qui doit être unique. Ce nom est ensuite utilisé dans l'attribut `href`, précédé d'un dièse (`# `).

#### Exemple
```html
<section id="partie-1"></section>
<section id="partie-2">
  <p>Voir la <a href="#partie-1">première partie</a> pour en savoir plus.</p>
</section>
```

D'autres attributs peuvent églement être précisés, notamment pour améliorer l'accessibilité des liens :

- `title=` permet de donner un titre au lien, qui sera généralement affiché sous forme d'infobulle
- `accesskey=` permet d'associer un lien à un raccourci clavier de la forme Alt+`accesskey`, sous réserve que cette combinaison ne soit pas déjà utilisée par le navigateur.
- `target=` permet de préciser comment le navigateur doit ouvrir le lien. Les valeurs les plus usuelles sont `_self` pour une ouverture dans le même onglet et `_blank` pour une ouverture dans un nouvel onglet.

### Images

L'insertion d'une image s'effectue au moyen de la balise `<img>`. Cette balise a deux attributs obligatoires :

- `src=` pour renseigner la source de l'image à afficher. Le support des différents formats d'image dépend des navigateurs, mais en général, les formats JPEG, PNG et GIF sont supportés.
Les images devant être chargées pour permettre l'affichage de la page, il est déterminant de minimiser le poids des fichiers.
- `alt=` permet de fournir une description de l'image, à destination des publics utilisant des outils d'accessibilité tels que des lecteurs d'écran. Il doit rester vide pour une image purement décorative, n'ayant aucun sens sémantique.

Comme pour les liens, l'attribut `title=` permet d'ajouter un titre, affiché sous forme d'infobulle.

### Élément neutre

A l'instar des éléments de type bloc, les éléments de type en ligne admettent un élément neutre, permettant d'effectuer des mises en forme particulières, indépendamment de toute notion sémantique. Il s'agit de l'élément `<span>`.