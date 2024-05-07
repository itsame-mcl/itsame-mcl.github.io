---
title: "Syntaxe HTML 5 et structure sémantique d'une page web"
date: 2024-05-07T11:30:00+01:00
tags: ["HTML 5"]
categories: ["Formation"]
menu:
  sidebar:
    name: HTML - Syntaxe & Stucture
    identifier: html-syntax-structure
    parent: html-css
    weight: 20
---

## Syntaxe de HTML 5

La syntaxe de HTML 5 est basée sur celle de XML, mais admet quelques simplifications.
Une version stricte, nommée XHTML, a existé en parallèle de HTML 4, avant d'être abandonnée par le W3C le 2 juillet 2009.

### Éléments de XML

Un document XML est un fichier texte structuré. Ce document est un **arbre**, composé de **nœuds**.

Il est introduit par un **prologue**, précisant des informations techniques telles que la version de la norme XML ou l'encodage utilisé.

Un arbre contient un unique nœud principal, nommé *nœud document* (ou racine).
Il contient ensuite un ou plusieurs *nœuds élément*, pouvant eux-mêmes contenir d'autres *nœuds élément* ou des *nœuds texte*.

Le nom du nœud document et des nœuds élément est libre, mais ne peut pas contenir d'espace où l'un des caractères suivants : ``!"#$%&'()*+,/;<=>?@[\]^`{|}~``. Il ne peut pas non plus commencer par un chiffre, un tiret (`-`) ou un point.

Les nœuds sont définis au moyen de **balises**, qui peuvent être de trois types :

- Balise ouvrante : `<noeud>`
- Balise fermante : `</noeud>`
- Balise vide : `<noeud/>`

Un nœud texte s'insère entre une balise ouvrante et une balise fermante. Une balise ouvrante doit obligatoirement être suivie d'une balise fermante du même nom. Une balise vide ne peut pas contenir de nœud texte.

Toutes les balises peuvent être complétées d'un ou plusieurs **attributs**, sous forme de combinaison clé/valeur : `<balise attribut="valeur" autre-attribut='autre-valeur'>`. Chaque attribut est unique à l'échelle d'une balise.

Le respect strict des normes de syntaxe est obligatoire en XML. Un document non conforme générera des erreurs bloquantes dans les traitements automatisés.

#### Exemple de document XML valide

```xml
<?xml version="1.0" encoding="UTF-8"?>
<document><!-- nœud document -->
    <element titre="1er élément">
        <enfant>Nœud texte</enfant>
        <enfant>
            <vide attribut1="valeur" attribut2="valeur" />
        </enfant>
    </element>
    <element titre="2ème élément">Nœud texte</element>
</document>
```

### Simplifications en HTML 5

Par rapport à la norme XML stricte, HTML 5 introduit quelques simplifications :

- Le prologue se limite à une unique ligne `<!DOCTYPE html>`
Cette balise est la seule à avoir un nom en majuscule, toutes les autres sont en minuscule.
- Une balise ouvrante peut rester vide, et la balise fermante devient alors facultative.
Les balises vides peuvent donc être remplacées par des balises ouvrantes, rendant le `/` facultatif.
- Dans le cas où un document HTML 5 n'est pas parfaitement valide, la plupart des navigateurs vont quand même tenter de l'interpréter au mieux, au lieu de produire une erreur.

## Structure de base d'une page HTML 5

Une page HTML 5 est un document XML, enregistré sous la forme d'un fichier à l'extension `.html` (ou `.htm`), dont le nœud document s'appelle `html`, et contenant 2 enfants nommés `head` et `body`. Le document HTML 5 minimal est donc le suivant :

```html
<!DOCTYPE html>
<html>
    <head></head>
    <body></body>
</html>
```

### Métadonnées de l'en-tête

L'élément `<head>` représente *l'en-tête* du document HTML. Ses enfants permettent de préciser des métadonnées telles que le titre, l'auteur, la description, l'encodage.
C'est également dans le `<head>` que sont déclarés des liens vers des fichiers supplémentaires nécessaires au bon affichage de la page : feuille de style CSS, scripts JavaScript...

Le titre de la page web, tel qu'affiché dans les onglets des navigateurs web, est défini par un nœud texte à l'intérieur d'une paire de balises `<title>`.

Les autres métadonnées sont définies à l'aide des balises `meta` dont l'attribut `name` indique le nom de la métadonnée et l'attribut `content` précise sa valeur.
Cette règle admet deux exceptions (pour des raisons de compatibilité historique avec d'anciennes versions de HTML) :
- la métadonnée sur la langue de la page web est indiquée sous la forme d'un attribut du nœud document `html` : `<html lang="fr">`
- la métadonnée sur l'encodage de la page web est indiquée par une balise `meta` ayant pour seul attribut `charset`

Enfin, les liens vers d'autres fichiers sont précisés dans des balises `link` dont l'attribut `rel` précise le type de fichier lié et l'attribut `href` son emplacement.

#### Exemple d'en-tête HTML 5 avec métadonnées

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <title>Titre de la page web</title>
        <meta charset="UTF-8">
        <meta name="author" content="Auteur de la page web">
        <meta name="description" content="Description de la page web">
        <meta name="keywords" content="Mot Clé 1, Mot Clé 2, Mot Clé 3">
        <link rel="stylesheet" href="style.css">
    </head>
    <body></body>
</html>
```

### Structure sémantique du corps

L'élément `<body>` représente le *corps* du document web. C'est dans cet élément que s'insère tout le contenu de la page web, au moyen des balises définies dans la norme HTML 5.

L'introduction de HTML 5 s'est accompagnée d'une vaste réflexion autour de la notion de *web sémantique*, dans l'idée de rendre les standards du web davantage porteurs de sens vis à vis du contenu qu'ils décrivent.
L'objectif est de faciliter le travail d'indexation par les moteurs de recherche et les outils d'analyse automatique de documents, ainsi que d'améliorer l'accessibilité numérique en précisant où se trouve le contenu le plus important.

Cette évolution passe par l'introduction de nouvelles balises permettant de subdiviser en **blocs** les pages web, en fonction du contenu de ces blocs. Ces balises sont les suivantes, dans l'ordre où elles apparaissent généralement sur une page web :

| Balise  | Sens sémantique                                | Règles d'usage                                                                                                              |
|:-------:|:-----------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
|  main   | Contenu principal                              | Limité à un par page web, ne peut pas être un enfant d'une autre balise sémantique                                          |
| section | Division cohérente d'un contenu ou de la page  | Peut être parent ou enfant d'autres balises sémantiques au sein de la même page web                                         |
| article | Contenu indépendant                            | Permet de délimiter un contenu ayant du sens indépendamment du reste de la page web                                         |
|  aside  | Contenu indépendant et d'importance secondaire | Peut être utilisé pour préciser qu'un contenu n'est pas directement lié au contenu principal                                |
|   nav   | Menu de navigation                             | Permet de définir un menu principal de navigation, permettant de naviguer entre les contenus et avec d'autres pages du site |
|  menu   | Menu secondaire                                | Définit un menu d'importance secondaire, permettant par exemple d'accéder à des options, mais pas de naviguer sur le site   |
| header  | En-tête de bloc                                | Peut aussi bien être utilisé pour délimiter l'en-tête de la page web que celui d'un bloc sémantique                         |
| footer  | Pied de page de bloc                           | Peut aussi bien être utilisé pour délimiter le pied de page de la page web que celui d'un bloc sémantique                   |

L'usage de ces balises n'est pas obligatoire, mais fortement recommandé pour améliorer les performances en référencement et accessibilité de la page web. Il permet également de simplifier l'écriture des feuilles de style.

#### Exemple de document HTML 5 avec métadonnées et structure sémantique

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <title>Page multi-articles</title>
        <meta charset="UTF-8">
        <meta name="author" content="Auteur de la page web">
        <meta name="description" content="Description de la page web">
        <meta name="keywords" content="HTML5, Sémantique">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <nav></nav>
        </header>
        <main>
            <menu></menu>
            <article>
                <header></header>
                <section></section>
                <section></section>
                <section></section>
                <footer></footer>
            </article>
            <article>
                <section></section>
                <section></section>
            </article>
            <aside>
                <section></section>
                <section></section>
            </aside>
        </main>
        <footer></footer>
    </body>
</html>
```

Dans cet exemple, cette page web en français commence par un en-tête contenant le menu principal de navigation.

Le contenu principal s'ouvre ensuite, et se compose de deux articles indépendants et d'un article complémentaire. Un menu secondaire permet d'accéder à des options supplémentaires.

Le premier article possède lui aussi un en-tête (une introduction), trois sections distinctes (des sous parties) et un pied de page (une conclusion).
Le second article, plus simple, se découpe simplement en deux sections. Enfin, l'article annexe se compose lui aussi de deux sections.

La page se conclut par un pied de page général, situé en dehors du contenu principal.