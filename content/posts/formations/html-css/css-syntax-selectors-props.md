---
title: "Syntaxe CSS 3, sélecteurs et propriétés usuelles"
description: "Anatomie d'une feuille de style, sélecteurs, cascade, variables CSS, modèle de boîte, texte et arrière-plans."
date: 2024-05-12T21:00:00+01:00
lastmod: 2026-07-21T12:00:00+02:00
tags: ["CSS"]
categories: ["Formation"]
menu:
  sidebar:
    name: "CSS - Syntaxe, sélecteurs, propriétés"
    identifier: css-syntax-selectors-props
    parent: html-css
    weight: 50
---

## 6.1. Anatomie d'une feuille de style
Une **feuille de style** CSS se compose de **règles**. Chaque règle est introduite par un **sélecteur**, qui désigne les éléments HTML concernés, suivi d'un bloc de **déclarations** entre accolades. Une déclaration associe une **propriété** à une **valeur** et se termine par un point-virgule :

```css
selecteur-1 {
    propriete-1: valeur;
    propriete-2: valeur;
}
 
selecteur-2 {
    propriete-3: valeur;
}
```

Les commentaires s'écrivent `/* commentaire */`. CSS repose sur deux mécanismes fondamentaux : l'**héritage** (un élément hérite de nombreuses propriétés de ses ancêtres, notamment celles liées au texte) et la **cascade** (des règles concurrentes sont départagées selon des critères de priorité, présentés en 6.4).

## 6.2. Lier une feuille de style à un document HTML
- **Fichier externe** (méthode recommandée) : la feuille est enregistrée dans un fichier `.css` et liée dans le `<head>` par `<link rel="stylesheet" href="style.css">`. Elle est ainsi mutualisée entre toutes les pages du site et mise en cache par le navigateur.
- **Balise `&lt;style&gt;`** dans le `<head>` : à réserver aux cas très particuliers (page unique autonome), car elle empêche toute mutualisation.
- **Attribut `style=`** directement sur un élément : à éviter — il mélange contenu et présentation, ne se mutualise pas, et complique la maintenance.

## 6.3. Les sélecteurs
Plusieurs sélecteurs peuvent partager un même bloc en les séparant par des virgules (`h1, h2 { … }`).

### Sélecteurs de base
| **Sélecteur** | **Cible** | **Exemple** |
|---|---|---|
| `*` | Tous les éléments | `* { box-sizing: border-box; }` |
| `balise` | Tous les éléments de ce type | `a { text-decoration: none; }` |
| `.classe` | Éléments portant `class="classe"` | `.important { color: red; }` |
| `#identifiant` | L'élément portant `id="identifiant"` | `#menu { … }` |

Un `id` doit être **unique** dans la page ; une `class` peut être portée par plusieurs éléments, et un élément peut porter plusieurs classes séparées par des espaces (`class="carte nouveaute"`). Balise et classe se combinent : `a.externe` cible les seuls liens portant la classe `externe`.


### Pseudo-classes
Les pseudo-classes, préfixées par deux-points (`:`), ciblent des états ou des positions générés dynamiquement :

- `:hover` : élément survolé par le pointeur ; `:active` : élément en cours de clic ;
- `:focus` : élément qui a le focus (clavier ou clic) ; `:focus-visible` : focus obtenu au clavier — la pseudo-classe à privilégier pour styler le contour de focus ;
- `:link` et `:visited` : liens non visités / visités ;
- `:first-child`, `:last-child`, `:nth-child(n)` : position parmi les enfants d'un parent (`:nth-child(odd)` ou `(even)` pour un élément sur deux, très utilisé pour zébrer les tableaux) ;
- `:not(sélecteur)` : négation ;
- `:required`, `:disabled`, `:checked` : états des contrôles de formulaire.

### Pseudo-éléments
Préfixés par deux fois deux-points (`::`), ils désignent des fragments implicites du document : `::first-letter` (première lettre), `::first-line` (première ligne), `::selection` (texte sélectionné), `::marker` (puce ou numéro de liste), et `::before` / `::after`, qui insèrent un pseudo-élément avant/après le contenu d'un élément (utilisé avec la propriété `content`).

### Combinateurs
| **Écriture** | **Signification** |
|---|---|
| `A B` | Tout `B` descendant (à n'importe quelle profondeur) d'un `A` |
| `A > B` | Tout `B` enfant **direct** d'un `A` |
| `A + B` | Tout `B` frère **immédiatement** suivant d'un `A` |
| `A ~ B` | Tout `B` frère suivant (pas nécessairement immédiat) d'un `A` |

## 6.4. Cascade, spécificité et !important
Quand plusieurs règles fixent la même propriété sur le même élément, le navigateur les départage ainsi :

- **Spécificité** du sélecteur, par ordre décroissant : styles en ligne (`style=`), puis identifiants (`#`), puis classes / pseudo-classes / attributs, puis balises et pseudo-éléments. Un sélecteur composé cumule les niveaux de ses composants : `nav a.actif` (1 balise + 1 balise + 1 classe) l'emporte sur `nav a`.
- **Ordre d'apparition** : à spécificité égale, la dernière règle déclarée l'emporte.

Le suffixe `!important` (`text-decoration: none !important;`) court-circuite toute la cascade. Il doit rester exceptionnel : chaque `!important` rend la feuille de style plus difficile à maintenir, car il ne peut être surchargé que par… un autre `!important`.

{{< alert type="tip" >}}
Pour retenir l'ordre de priorité, une analogie : un sélecteur de balise est comme un prénom (beaucoup de personnes le portent), une classe comme un nom de famille (déjà plus précis), et un identifiant comme un numéro de sécurité sociale (il ne désigne qu'une seule personne). Plus c'est précis, plus ça l'emporte.
{{< /alert >}}

## 6.5. Les variables CSS (propriétés personnalisées)
CSS permet de définir ses propres variables, dites **propriétés personnalisées**. Déclarées sur la pseudo-classe `:root` (l'élément `<html>`), elles sont utilisables partout via la fonction `var()` :

```css
:root {
    --couleur-principale: #1f4e79;
    --espacement: 1.5rem;
}
 
h1 {
    color: var(--couleur-principale);
    margin-bottom: var(--espacement);
}
```

Les variables centralisent la charte graphique (couleurs, espacements, polices) : une modification en un seul point se propage à tout le site. Elles sont aujourd'hui supportées par tous les navigateurs et constituent une bonne pratique standard.

## 7.1. Les unités de mesure
Les valeurs numériques utilisent le point (`.`) comme séparateur décimal. Unités les plus usuelles :

| **Unité** | **Signification** |
|---|---|
| `px` | Pixel CSS. Unité absolue de référence à l'écran. |
| `rem` | Taille de police de l'élément racine `<html>` (16 px par défaut). L'unité à privilégier pour les tailles de texte et les espacements. |
| `em` | Taille de police de l'élément courant (héritée du parent). Attention aux effets de composition en cas d'imbrication. |
| `%` | Pourcentage d'une valeur de référence, en général la dimension correspondante de l'élément parent. |
| `vw` / `vh` | 1 % de la largeur / hauteur de la fenêtre du navigateur (viewport). |
| `fr` | Fraction de l'espace disponible — spécifique aux grilles CSS (chapitre 8). |
| `cm`, `mm` | Unités physiques, utiles pour les feuilles de style d'impression. |

{{< alert type="a11y" >}}
Définir les tailles de texte en `rem` plutôt qu'en `px` respecte le réglage de taille de police choisi par l'utilisateur dans son navigateur — un besoin réel pour les personnes malvoyantes. C'est l'une des raisons pour lesquelles `rem` est devenu l'unité de référence.
{{< /alert >}}

## 7.2. Le modèle de boîte
Chaque élément HTML est rendu comme une **boîte** composée de quatre couches concentriques : le **contenu**, le **padding** (marge interne), la **bordure** et la **marge externe**.

### Contenu
`width` et `height` fixent les dimensions du contenu. La valeur `auto` (par défaut) laisse le navigateur calculer : pour un bloc, la largeur disponible du parent et la hauteur du contenu. Les propriétés `min-width`, `max-width`, `min-height` et `max-height` bornent ces dimensions — `max-width` est très utilisée en responsive.

Seuls les éléments de type bloc et les éléments en ligne « dimensionnables » (comme `<img>`, ou tout élément passé en `display: inline-block`) acceptent `width` et `height`.

### Padding, bordure, marge
Chaque couche se règle côté par côté (`padding-top`, `border-left`, `margin-bottom`…) ou via des raccourcis acceptant de 1 à 4 valeurs :

- **1 valeur** : les quatre côtés ;
- **2 valeurs** : haut/bas, puis gauche/droite ;
- **3 valeurs** : haut, gauche/droite, bas ;
- **4 valeurs** : haut, droite, bas, gauche (sens horaire).

Pour les bordures, il faut préciser dimension, style et couleur. Le raccourci `border` regroupe les trois : `border: 1px solid #1f4e79;`. Les styles usuels sont `solid` (trait plein), `double`, `dotted` (points) et `dashed` (tirets). La propriété `border-radius` arrondit les angles (`border-radius: 8px;`).

{{< alert type="note" >}}
Les marges externes verticales de deux blocs qui se suivent **fusionnent** (margin collapsing) : entre un paragraphe avec `margin-bottom: 20px` et le suivant avec `margin-top: 10px`, l'espace est de 20 px, pas 30. Ce comportement disparaît dans les conteneurs Flexbox et Grid.
{{< /alert >}}

### box-sizing : redéfinir ce que mesurent width et height
Par défaut (`box-sizing: content-box`), `width` ne mesure que le contenu : une boîte de `width: 300px` avec `padding: 20px` et une bordure de 2 px occupe en réalité 344 px. La valeur `border-box` fait englober padding et bordure dans `width`/`height`, ce qui simplifie énormément les calculs de mise en page. La règle suivante est devenue un standard de facto en début de feuille de style :

```css
* {
    box-sizing: border-box;
}
```

{{< alert type="warning" >}}
Une valeur `padding-box` a existé dans d'anciennes versions de la spécification, mais elle a été **retirée** : seules `content-box` et `border-box` sont valides aujourd'hui.
{{< /alert >}}

### Dépassement : overflow
Quand un contenu ne tient pas dans une boîte aux dimensions fixées, `overflow` règle le comportement : `visible` (défaut, le contenu déborde), `hidden` (masqué), `scroll` (barres de défilement permanentes) ou `auto` (barres uniquement si nécessaire).

### Mode d'affichage : display
`display` modifie le comportement d'un élément : `block`, `inline`, `inline-block` (en ligne mais dimensionnable), `none` (retiré de l'affichage **et** de l'arbre d'accessibilité), et les valeurs `flex` et `grid` présentées au chapitre 8.

## 7.3. Mise en forme du texte
### Police de caractères
`font-family` accepte une liste de polices par ordre de préférence, terminée par une famille générique (`serif`, `sans-serif`, `monospace`) : le navigateur utilise la première police disponible sur la machine de l'utilisateur.

```css
body {
    font-family: "Segoe UI", Roboto, Arial, sans-serif;
}
```

Pour utiliser une police non installée chez l'utilisateur, on la fournit avec un bloc `@font-face`. Le format **WOFF2**, compressé et universellement supporté, est aujourd'hui le seul nécessaire :

```css
@font-face {
    font-family: "MaPolice";
    src: local("MaPolice"),
         url("mapolice.woff2") format("woff2");
    font-display: swap;
}
```

La ligne `local()` évite un téléchargement si la police est déjà installée ; `font-display: swap` affiche le texte avec une police de substitution pendant le chargement plutôt qu'un texte invisible.

### Taille, interligne, alignement
- `font-size` : taille de police, de préférence en `rem`.
- `line-height` : interligne. La bonne pratique est une valeur **sans unité**, multiplicateur de la taille de police (`line-height: 1.5`). Les WCAG recommandent au moins 1,5 pour les paragraphes.
- `text-align` : `left`, `right`, `center`, `justify`. La justification est déconseillée à l'écran : les « rivières » d'espaces gênent les lecteurs dyslexiques.
- `text-indent` : retrait de première ligne.

### Graisse, style, décorations, casse
- `font-weight` : graisse, de `100` à `900` ou par mots-clés (`normal`, `bold`).
- `font-style` : `normal` ou `italic`.
- `text-decoration` : `none`, `underline`, `line-through`.
- `text-transform` : `lowercase`, `uppercase`, `capitalize` — la mise en capitales se fait en CSS, pas en tapant le texte en majuscules dans le HTML (les lecteurs d'écran risqueraient d'épeler les sigles).

{{< alert type="a11y" >}}
Ne jamais supprimer le soulignement des liens (`text-decoration: none`) sans fournir un autre indice visuel que la couleur seule : environ 8 % des hommes sont daltoniens et ne distingueront pas un lien bleu d'un texte noir. Le critère WCAG « Utilisation de la couleur » impose un second indicateur (soulignement, graisse, icône…).
{{< /alert >}}

### Couleurs
La propriété `color` (couleur du texte) accepte plusieurs notations :

- un **nom de couleur** parmi les 140 noms normalisés : `red`, `steelblue`… ;
- une valeur **hexadécimale** : `#rrggbb`, ou `#rrggbbaa` avec transparence ;
- les fonctions `rgb()` et `hsl()`. La syntaxe moderne sépare les composantes par des espaces et introduit la transparence par une barre oblique : `rgb(31 78 121)`, `rgb(31 78 121 / 0.5)`, `hsl(210 60% 30%)`. Les anciennes écritures `rgb(31, 78, 121)` et les fonctions `rgba()`/`hsla()` restent valides.

{{< alert type="a11y" >}}
Le **contraste** entre texte et fond est mesurable : les WCAG exigent un ratio d'au moins **4,5:1** pour le texte courant et 3:1 pour les grands textes (niveau AA). Des outils gratuits le vérifient en deux clics : le « Contrast Checker » de WebAIM, ou directement l'inspecteur des navigateurs (le sélecteur de couleur affiche le ratio).
{{< /alert >}}

## 7.4. Arrière-plans
`background-color` fixe une couleur de fond. Pour une image de fond :

- `background-image: url(chemin/vers/image);`
- `background-repeat` : `repeat` (défaut), `repeat-x`, `repeat-y`, `no-repeat` ;
- `background-position` : position de l'image (`center`, `top right`, valeurs numériques…) ;
- `background-size` : `cover` (couvre toute la boîte, quitte à rogner) ou `contain` (entièrement visible) ;
- `background-attachment` : `scroll` (défaut, l'image défile avec la page), `fixed` (fixe par rapport à la fenêtre), `local` (défile avec le contenu de l'élément).

Les propriétés d'arrière-plan ne sont pas héritées par les éléments enfants. `background-image` accepte aussi des dégradés générés par le navigateur : `background-image: linear-gradient(#1f4e79, #2e74b5);`.

{{< alert type="a11y" >}}
Une image de fond CSS est invisible pour les lecteurs d'écran et n'accepte pas d'attribut `alt`. Règle simple : une image **porteuse d'information** passe par `<img>` avec son `alt` ; une image **décorative** peut passer par `background-image`. Et tout texte posé sur une image doit conserver un contraste suffisant, par exemple via un voile semi-transparent.
{{< /alert >}}

## 7.5. Personnalisation des listes
- `list-style-type` : style de puce ou de numérotation (`disc`, `square`, `decimal`, ou tout caractère avec `list-style-type: "▶"`) ;
- `list-style-position` : puces à l'intérieur (`inside`) ou à l'extérieur (`outside`, défaut) de la boîte de la liste ;
- `list-style-image: url(…)` : image en guise de puce ;
- `list-style: none` supprime puces et numéros — l'usage standard pour les menus de navigation construits sur `<ul>`.

{{< alert type="practice" >}}
Les exercices 8 et 9 du [TP CSS]({{< relref "tp-css" >}}) font poser une charte graphique avec variables, puis travailler le modèle de boîte.
{{< /alert >}}
