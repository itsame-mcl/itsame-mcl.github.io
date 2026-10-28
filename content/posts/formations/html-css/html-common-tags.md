---
title: "Principales balises HTML 5"
description: "Titres, paragraphes, listes, liens, images, audio, vidéo et éléments neutres."
date: 2024-05-09T21:15:00+01:00
lastmod: 2026-07-21T12:00:00+02:00
tags: ["HTML"]
categories: ["Formation"]
menu:
  sidebar:
    name: "HTML - Principales balises"
    identifier: html-common-tags
    parent: html-css
    weight: 30
---

Le standard définit plus d'une centaine de balises, mais un petit sous-ensemble couvre l'immense majorité des besoins. Ce chapitre présente les balises usuelles, en dehors des tableaux et formulaires qui font l'objet des chapitres 4 et 5.

## 3.1. Titres et hiérarchie
Les balises `<h1>` à `<h6>` définissent six niveaux de titres. Elles structurent le document comme le ferait le plan d'un rapport :

- une page contient en principe **un seul `&lt;h1&gt;`**, qui annonce son sujet principal ;
- les niveaux s'enchaînent **sans saut** : un `<h3>` ne doit apparaître que sous un `<h2>` ;
- on ne choisit jamais un niveau de titre pour sa taille d'affichage — c'est le rôle de CSS.

{{< alert type="a11y" >}}
La hiérarchie des titres est le second mode de navigation des lecteurs d'écran (touche H pour sauter de titre en titre). Un plan de titres incohérent rend la page très difficile à explorer. Les outils de développement des navigateurs et l'extension HeadingsMap permettent de visualiser ce plan.
{{< /alert >}}

## 3.2. Paragraphes
- `<p>` : paragraphe standard.
- `<pre>` : texte préformaté, qui préserve espaces et retours à la ligne (utile pour du code).
- `<blockquote>` : citation longue, avec un attribut facultatif `cite=` indiquant l'URL de la source.
- `<address>` : informations de contact de l'auteur de la page ou de l'article.

## 3.3. Listes
Trois types de listes existent, toutes de type bloc :

### Liste ordonnée : &lt;ol&gt;
Chaque élément, défini par `<li>` (*list item*), est numéroté. Trois attributs personnalisent la numérotation : `start=` (première valeur), `type=` (style de numérotation : `1`, `A`, `a`, `I`, `i`) et `reversed` (ordre décroissant). L'attribut `value=` sur un `<li>` force une valeur particulière.

```html
<ol type="I">
    <li>Élément I</li>
    <li>Élément II</li>
    <li value="5">Élément V</li>
</ol>
```

### Liste non ordonnée : &lt;ul&gt;
Chaque élément `<li>` est précédé d'une puce. C'est la liste à utiliser dès qu'il n'y a pas d'ordre significatif — c'est aussi la structure standard d'un menu de navigation :

```html
<nav>
    <ul>
        <li><a href="index.html">Accueil</a></li>
        <li><a href="decouvrir.html">Découvrir la ville</a></li>
        <li><a href="contact.html">Contact</a></li>
    </ul>
</nav>
```

### Liste de descriptions : &lt;dl&gt;
Elle associe des termes (`<dt>`, *description term*) et leurs définitions (`<dd>`, *description details*). Idéale pour un glossaire ou une liste de caractéristiques :

```html
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
    <dt>CSS</dt>
    <dd>Cascading Style Sheets</dd>
</dl>
```

## 3.4. Emphases et enrichissements du texte
- `<em>` : emphase (rendue en italique par défaut) — le sens : « ce mot est important dans la phrase ».
- `<strong>` : emphase forte (rendue en gras par défaut) — le sens : « ceci est important dans le document ».
- `<i>` et `<b>` : italique et gras purement visuels, sans valeur sémantique (terme étranger, nom d'œuvre…). À réserver aux cas où `<em>`/`<strong>` seraient trompeurs.
- `<sup>` et `<sub>` : exposant (m`<sup>`2`</sup>`) et indice (H`<sub>`2`</sub>`O).
- `<mark>` : passage surligné (résultat de recherche, par exemple).
- `<time datetime="2026-07-20">` : date ou heure, avec sa valeur normalisée en attribut.

## 3.5. Liens hypertextes
Un lien se déclare avec la balise `<a>` et son attribut obligatoire `href=`, qui désigne la cible : une autre page (`href="contact.html"`, `href="https://exemple.fr"`), une ancre dans la même page (`href="#partie-1"`, pointant vers l'élément portant `id="partie-1"`), une adresse de courriel (`href="mailto:…"`).

```html
<section id="partie-1">…</section>
<section id="partie-2">
    <p>Voir la <a href="#partie-1">première partie</a> pour en savoir plus.</p>
</section>
```

L'attribut `target="_blank"` ouvre le lien dans un nouvel onglet. À utiliser avec parcimonie : il retire à l'utilisateur le contrôle de sa navigation.

{{< alert type="a11y" >}}
L'intitulé du lien doit être explicite **hors contexte** : les utilisateurs de lecteurs d'écran naviguent souvent de lien en lien. « Cliquez ici » ou « En savoir plus » répétés dix fois sont inutilisables ; préférer « Consulter les horaires d'ouverture ». Deux attributs historiques sont par ailleurs à éviter : `accesskey` (raccourcis clavier qui entrent en conflit avec ceux des navigateurs et des lecteurs d'écran) et `title` comme unique porteur d'information (l'infobulle n'est accessible ni au clavier ni au tactile).
{{< /alert >}}

## 3.6. Images
Une image s'insère avec la balise vide `<img>` et deux attributs obligatoires :

- `src=` : chemin du fichier image. Formats universellement supportés : JPEG (photos), PNG (transparence), GIF, SVG (dessins vectoriels, icônes) et **WebP/AVIF**, formats modernes plus légers, aujourd'hui supportés par tous les navigateurs. Le poids des images étant le premier facteur de lenteur d'une page, il doit être minimisé.
- `alt=` : **alternative textuelle**, lue par les lecteurs d'écran et affichée si l'image ne charge pas.

{{< alert type="a11y" >}}
Règle d'or de l'attribut `alt` : décrire la **fonction** de l'image, pas son apparence. Une image porteuse d'information reçoit une description utile (`alt="Plan d'accès : l'office de tourisme est face à la mairie"`) ; une image purement décorative reçoit un `alt` **vide** (`alt=""`) — et non pas d'attribut du tout, ce qui conduirait le lecteur d'écran à lire le nom du fichier.
{{< /alert >}}

Les attributs `width=` et `height=` (en pixels, sans unité) réservent l'espace de l'image avant son chargement et évitent les « sauts » de mise en page. Pour associer une légende visible à une image, on utilise `<figure>` et `<figcaption>` :

```html
<figure>
    <img src="vieux-port.jpg" alt="Le vieux port et ses façades colorées" width="800" height="450">
    <figcaption>Le vieux port, cœur historique de Bellerive-sur-Mer.</figcaption>
</figure>
```

## 3.7. Audio et vidéo
HTML 5 intègre nativement les contenus multimédias, sans greffon externe :

```html
<video src="visite.mp4" controls width="640" height="360">
    Votre navigateur ne prend pas en charge la vidéo.
</video>
 
<audio src="podcast.mp3" controls></audio>
```

L'attribut `controls` affiche les commandes de lecture du navigateur. Le texte placé entre les balises n'est affiché que si le navigateur ne sait pas lire le média.

{{< alert type="a11y" >}}
Une vidéo doit proposer des **sous-titres** (balise `<track kind="subtitles">` pointant vers un fichier `.vtt`) et un contenu audio une **transcription** textuelle. Éviter absolument `autoplay` : un média qui se déclenche seul perturbe fortement les utilisateurs de lecteurs d'écran (et agace tous les autres).
{{< /alert >}}

## 3.8. Les éléments neutres : &lt;div&gt; et &lt;span&gt;
Quand aucune balise sémantique ne convient, deux éléments « neutres » permettent de regrouper du contenu, notamment pour lui appliquer des styles CSS : `<div>` (bloc) et `<span>` (en ligne). Ils n'ont aucun sens propre : la bonne pratique est de n'y recourir **qu'en dernier ressort**, après avoir vérifié qu'aucune balise sémantique ne décrit mieux le contenu.

{{< alert type="practice" >}}
L'exercice 3 du [TP HTML]({{< relref "tp-html" >}}) met en œuvre titres, listes, emphases, images et liens.
{{< /alert >}}
