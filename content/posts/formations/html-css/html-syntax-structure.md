---
title: "Syntaxe HTML 5 et structure sémantique d'une page web"
description: "Syntaxe de HTML 5, squelette d'une page, métadonnées, balises sémantiques, et du SEO au GEO."
date: 2024-05-07T11:30:00+01:00
lastmod: 2026-07-21T12:00:00+02:00
tags: ["HTML"]
categories: ["Formation"]
menu:
  sidebar:
    name: "HTML - Syntaxe & structure"
    identifier: html-syntax-structure
    parent: html-css
    weight: 20
---

## 2.1. Une syntaxe héritée de XML
La syntaxe de HTML 5 est héritée de celle de XML, avec quelques assouplissements. Un document est un **arbre** composé de **nœuds**, définis au moyen de **balises** :

- balise ouvrante : `<noeud>` ;
- balise fermante : `</noeud>` ;
- balise vide (auto-fermante) : `<noeud/>` — en HTML 5, la barre oblique finale est facultative (`<img>` et `<img/>` sont équivalents).

Un nœud texte s'insère entre une balise ouvrante et une balise fermante. Les balises peuvent être complétées d'**attributs**, sous forme de paires clé/valeur, chaque attribut étant unique à l'échelle d'une balise :

```html
<balise attribut="valeur" autre-attribut="autre valeur">contenu</balise>
```

Les commentaires, ignorés par le navigateur, s'écrivent `<!-- commentaire -->`.

{{< alert type="note" >}}
Contrairement à XML strict (et à l'ancien XHTML, abandonné par le W3C en 2009), un document HTML 5 imparfait ne produit pas d'erreur bloquante : le navigateur tente toujours de l'interpréter au mieux. C'est confortable, mais dangereux : deux navigateurs peuvent « réparer » différemment un code invalide. Il faut donc viser un code valide, vérifié avec le validateur du W3C (validator.w3.org).
{{< /alert >}}

## 2.2. Le squelette minimal d'une page
Une page HTML 5 est un fichier texte enregistré avec l'extension `.html`. Le prologue se limite à la déclaration `<!DOCTYPE html>` (seul élément écrit en majuscules par convention), suivie du nœud racine `html` qui contient exactement deux enfants : `head` et `body`.

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Titre de la page</title>
    </head>
    <body>
    </body>
</html>
```

{{< alert type="a11y" >}}
L'attribut `lang="fr"` sur la balise `<html>` est indispensable : c'est lui qui permet aux lecteurs d'écran de choisir la bonne voix de synthèse. Une page en français annoncée en anglais devient incompréhensible. C'est le critère le plus simple — et l'un des plus souvent oubliés — du RGAA.
{{< /alert >}}

## 2.3. Les métadonnées de l'en-tête
L'élément `<head>` contient les métadonnées de la page : elles ne s'affichent pas dans la page mais renseignent le navigateur, les moteurs de recherche et les outils d'assistance.

- `<title>` : titre de la page, affiché dans l'onglet du navigateur et lu en premier par les lecteurs d'écran. Obligatoire, unique, et idéalement descriptif de la page (« Infos pratiques — Visiter Bellerive-sur-Mer » plutôt que « Accueil »).
- `<meta charset="UTF-8">` : encodage des caractères. À placer en tout début de `head`, avant tout texte.
- `<meta name="viewport" content="width=device-width, initial-scale=1">` : indispensable pour l'affichage sur mobile (nous y reviendrons au chapitre 9 sur le responsive). Sans elle, les téléphones affichent la page « dézoomée » comme sur un écran de bureau.
- `<meta name="description" content="…">` : description de la page, souvent reprise par les moteurs de recherche dans leurs résultats.
- `<meta name="author" content="…">` : auteur de la page.
- `<link rel="stylesheet" href="style.css">` : liaison avec une feuille de style CSS ; l'attribut `rel` précise le type de ressource liée, `href` son emplacement.

{{< alert type="note" >}}
La métadonnée `keywords`, que l'on rencontre encore dans d'anciens supports, est ignorée par tous les moteurs de recherche depuis de nombreuses années : inutile de la renseigner.
{{< /alert >}}

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Visiter Bellerive-sur-Mer — Accueil</title>
        <meta name="description" content="Sites incontournables, agenda et infos pratiques.">
        <link rel="stylesheet" href="style.css">
    </head>
    <body></body>
</html>
```

## 2.4. Blocs et éléments en ligne
Les éléments HTML se répartissent, pour l'affichage par défaut, en deux grandes familles :

- les éléments de type **bloc** délimitent des sections : ils occupent par défaut toute la largeur disponible et se succèdent verticalement (`<p>`, `<h1>`, `<div>`, `<section>`…) ;
- les éléments **en ligne** (*inline*) s'inscrivent dans la continuité du texte, sans provoquer de retour à la ligne, et occupent la taille minimale nécessaire (`<a>`, `<strong>`, `<img>`, `<span>`…).

{{< alert type="warning" >}}
Les éléments en ligne peuvent être imbriqués entre eux, mais ne doivent jamais contenir d'élément bloc : pas de `<p>` dans un `<a>` qui serait lui-même dans une phrase. À l'inverse, les blocs peuvent contenir des blocs et des éléments en ligne.
{{< /alert >}}

{{< alert type="note" >}}
Le standard actuel définit en réalité des « catégories de contenu » plus fines (flow content, phrasing content…), mais la distinction bloc / en ligne reste le bon modèle mental pour débuter — d'autant qu'elle correspond aux valeurs `block` et `inline` de la propriété CSS `display`.
{{< /alert >}}

## 2.5. La structure sémantique du corps
HTML 5 a introduit des balises dites **sémantiques** qui décrivent le rôle de chaque grande zone de la page. Elles facilitent l'indexation par les moteurs de recherche, simplifient les feuilles de style, et surtout permettent aux technologies d'assistance de naviguer de zone en zone (« aller au contenu principal », « aller à la navigation »).

| **Balise** | **Sens sémantique** | **Règles d'usage** |
|---|---|---|
| `<header>` | En-tête de la page ou d'un bloc | Peut apparaître plusieurs fois (en-tête de page, d'article…) |
| `<nav>` | Navigation principale | Réservé aux blocs de liens de navigation majeurs |
| `<main>` | Contenu principal | Un seul par page ; ne peut pas être imbriqué dans une autre balise sémantique |
| `<section>` | Division cohérente d'un contenu | Possède en général son propre titre `<h2>`, `<h3>`… |
| `<article>` | Contenu autonome | A du sens indépendamment du reste de la page (article, fiche, billet…) |
| `<aside>` | Contenu complémentaire | Contenu secondaire, non indispensable (encadré, liens connexes…) |
| `<footer>` | Pied de page ou de bloc | Peut apparaître plusieurs fois, comme `<header>` |

La balise `<menu>` existe également ; elle représente sémantiquement une liste d'actions (barre d'outils) et se comporte comme une liste `<ul>`. Son usage reste rare : dans la pratique, la navigation d'un site se construit avec `<nav>` contenant une liste de liens.

```html
<body>
    <header>
        <nav>…menu principal…</nav>
    </header>
    <main>
        <article>
            <header>…titre et chapeau…</header>
            <section>…première partie…</section>
            <section>…seconde partie…</section>
            <footer>…auteur, date…</footer>
        </article>
        <aside>…encadré complémentaire…</aside>
    </main>
    <footer>…mentions légales…</footer>
</body>
```

{{< alert type="a11y" >}}
Ces balises créent des « points de repère » (landmarks) que les utilisateurs de lecteurs d'écran utilisent pour se déplacer directement de zone en zone, sans écouter toute la page. Une page correctement structurée en `header`/`nav`/`main`/`footer` est déjà un grand pas vers la conformité RGAA.
{{< /alert >}}

## 2.6. Du SEO au GEO : la sémantique à l'ère des IA génératives
Le **SEO** (Search Engine Optimization) désigne l'optimisation d'une page pour les moteurs de recherche classiques. Un nouveau sigle s'y ajoute depuis quelques années : le **GEO** (Generative Engine Optimization), l'optimisation pour les moteurs de réponse à base d'IA générative — assistants conversationnels, résumés générés en tête des résultats de recherche, agents qui lisent le web pour le compte d'un utilisateur.

Ces systèmes ne se contentent plus de classer des liens : ils **lisent** les pages, en **extraient** des passages, et les **citent** dans leurs réponses. Une part croissante des visiteurs découvre ainsi un contenu sans jamais afficher la page. Cela concerne directement le développeur front-end : c'est la qualité du HTML qui détermine ce qu'une machine peut extraire de la page.

### Ce qui aide un moteur génératif à comprendre une page
- **Une structure sémantique propre** : les balises de zone (`<main>`, `<article>`, `<nav>`…) et une hiérarchie de titres cohérente permettent d'identifier le contenu principal, de le découper en passages autonomes et d'écarter les menus et pieds de page.
- **Des contenus autoportants** : des titres explicites, des paragraphes qui ont du sens isolément, des listes et tableaux correctement balisés (une donnée dans un vrai `<table>` avec `caption` et en-têtes est exploitable ; la même donnée dans un dessin ou un `<div>` stylé ne l'est pas).
- **Des métadonnées soignées** : un `<title>` descriptif, une meta `description` fidèle, l'attribut `lang`, des dates explicites (`<time datetime=…>`).
- **Les données structurées** (vocabulaire Schema.org, généralement en JSON-LD dans le `<head>`) : elles décrivent formellement le contenu (un lieu, un événement, des horaires…). Utiles de longue date pour les résultats enrichis des moteurs classiques, elles sont hors du périmètre de cette formation, mais sachez qu'elles existent.

{{< alert type="warning" >}}
Le GEO est un domaine **jeune et instable** : les préconisations changent au rythme des outils d'IA, et le marketing y produit beaucoup de « recettes magiques » non vérifiées. Exemple emblématique : le fichier `llms.txt`, proposé pour guider les IA, n'est à ce jour reconnu par aucun grand acteur — et Google indique explicitement qu'aucun balisage « spécial IA » n'est requis, les bonnes pratiques web classiques restant la référence. Méfiance, donc, envers toute technique présentée comme indispensable.
{{< /alert >}}

{{< alert type="note" >}}
La bonne nouvelle à retenir — et le message de ce chapitre : ce qui sert les utilisateurs sert aussi les machines. Un HTML sémantique, accessible et bien structuré est lisible par un humain, un lecteur d'écran, un robot d'indexation **et** une IA générative. Il n'y a pas quatre optimisations concurrentes, il y a un seul travail bien fait — et c'est la responsabilité du développeur front-end.
{{< /alert >}}

{{< alert type="practice" >}}
Les exercices 1 et 2 du [TP HTML]({{< relref "tp-html" >}}) font construire le squelette d'une page, puis sa structure sémantique.
{{< /alert >}}
