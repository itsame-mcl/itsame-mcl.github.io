---
title: "Flux de travail usuels"
description: "GitFlow, OneFlow, GitLab Flow"
date: 2023-04-16T19:00:00+01:00
tags: ["Git"]
categories: ["Formation"]
mermaid: true
menu:
  sidebar:
    name: Flux de travail usuels
    identifier: workflows
    parent: git
    weight: 50
---

Un flux de travail (en anglais, *workflow*) est une façon standardisée d'organiser les branches d'un projet Git.
Leur utilisation permet de bénéficier de méthodes éprouvées pour s'adapter à des modes usuels d'organisation et d'outils spécifiquement conçus pour leur prise en charge.

## GitFlow

GitFlow est un flux de travail qui a été proposé par [Vincent Driessen](https://nvie.com/posts/a-successful-git-branching-model/) en 2010.
Son objectif est de permettre en parallèle la maintenance d'une version de production et l'élaboration d'une version de développement.

GitFlow s'appuie sur 5 familles de branches :
  - `main` : branche principale et permanente, chaque version de main est vouée à être mise en production
  - `develop` : branche permanente, soutenant la version de développement
  - `feature` : branches éphémères tirées de `develop`, dédiées au développement d'une fonctionnalité
  - `release` : branches éphémères tirées de `develop`, servant aux ultimes correctifs avant mise en production
  - `hotfix` : branches éphémères tirées de `main`, permettant la correction de bugs en production

### Exemple

{{< mermaid align="left" >}}
    gitGraph
        commit tag: "v1.0.0"
        branch develop order: 3
        branch feature/US1 order: 4
        commit
        commit
        checkout main
        branch hotfix/1.0.1 order: 1
        commit
        checkout main
        merge hotfix/1.0.1 tag: "v1.0.1"
        checkout develop
        merge hotfix/1.0.1
        branch feature/US2 order: 5
        commit
        commit
        checkout feature/US1
        commit
        checkout develop
        merge feature/US1
        branch release/1.1.0 order: 2
        commit
        commit
        checkout main
        merge release/1.1.0 tag: "v1.1.0"
        checkout develop
        merge release/1.1.0
        checkout feature/US2
        commit
{{< /mermaid >}}

### Utilisation de l'extension GitFlow

Les installations de Git pour Windows depuis la version 2.6.4 incluent directement une extension permettant une prise en charge simplifiée de GitFlow.
  - Pour macOS et Linux, un paquet nommé `git-flow` est généralement disponible pour installer cette extension.

L'extension se manipule ensuite en ligne de commandes au travers de l'instruction `git flow`


#### Initialisation

L'initialisation de GitFlow s'effectue en utilisant la sous-commande `init` de `git flow` :
  ```bash
  git flow init
  ```

Git demande alors des informations sur les noms à utiliser pour les différentes branches et les tags de version :
  ```console
  Which branch should be used for bringing forth production releases?
  Branch name for production releases: [main]
  Branch name for "next release" development: [develop]
  How to name your supporting branch prefixes?
  Feature branches? [feature/]
  Release branches? [release/]
  Hotfix branches? [hotfix/]
  Version tag prefix? [] v
  ```

#### Développer une fonctionnalité

Pour démarrer une branche de fonctionnalité, il suffit d'utiliser l'instruction `feature start` :
  ```bash
  git flow feature start <nom_de_la_fonction>
  ```
  - Git va alors automatiquement créer une branche à partir de `develop` et l'activer.

Il est ensuite possible de publier cette branche sur un dépôt distant :
  ```bash
  git flow feature publish <nom_de_la_fonction>
  ```

Il est également possible de récupérer une branche de fonctionnalité à partir d'un dépôt distant :
  ```bash
  git flow feature pull origin <nom_de_la_fonction>
  ```

Enfin, une fois le développement d'une fonctionnalité terminée, il est nécessaire de la clôturer :
  ```bash
  git flow feature finish <nom_de_la_fonction>
  ```
  - Cette commande fusionne la branche de fonctionnalité dans `develop`, supprime la branche devenue inutile et réactive `develop`.

#### Réaliser une version de production ou un correctif

Les mêmes commandes que pour les fonctionnalités peuvent s'utiliser pour les versions de production ou les correctifs, en remplaçant le mot-clé `feature` par `release` ou `hotfix` :
  ```bash
  git flow release start <numero_de_version> <commit_de_depart>
  ```
  - Le numéro de version saisi sera ensuite apposé comme un tag lors de la fusion dans `main`.
  - Il est possible de faire partir une `release` (resp., `hotfix`) de n'importe quel commit de `develop` (resp., `main`).

## OneFlow

OneFlow est une évolution de GitFlow proposée par [Adam Ruka](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow) en 2017.
Son objectif est de proposer un historique plus clair et lisible sur le long terme en ne se basant que sur une branche perpétuelle.

Utiliser OneFlow de manière efficace implique de manipuler les tags et les `squash` ou les `rebase`.

OneFlow s'appuie sur une branche principale : `main` qui sert de branche de développement
On dérive de cette branche trois types de branches éphémères :
  - `feature` pour les fonctionnalités
  - `release` pour les mises en production
  - `hotfix` pour les correctifs sur la production

Les branches `release` et `hotfix` s'achèvent par un tag qui permet d'identifier leur dernier commit comme étant prêt à être mis en production.

### Exemple

{{< mermaid align="left" >}}
    gitGraph
        commit tag: "v1.0.0"
        branch hotfix/1.0.1 order: 1
        branch feature/US1 order: 3
        commit
        commit
        checkout main
        checkout hotfix/1.0.1
        commit
        checkout main
        merge hotfix/1.0.1 tag: "v1.0.1"
        branch feature/US2 order: 4
        commit
        commit
        checkout feature/US1
        commit
        checkout main
        merge feature/US1
        branch release/1.1.0 order: 2
        commit
        commit
        checkout main
        merge release/1.1.0 tag: "v1.1.0"
        checkout feature/US2
        commit
{{< /mermaid >}}

Pour améliorer encore la lisibilité de l'historique, il est conseillé de rebase les branches de fonctionnalité sur la dernière version étiquetée de `main` avant de les fusionner :

{{< mermaid align="left" >}}
    gitGraph
        commit tag: "v1.0.0"
        branch hotfix/1.0.1 order: 1
        checkout main
        checkout hotfix/1.0.1
        commit
        checkout main
        merge hotfix/1.0.1 tag: "v1.0.1"
        branch feature/US1 order: 3
        commit
        commit
        commit
        checkout main
        merge feature/US1
        branch release/1.1.0 order: 2
        commit
        commit
        checkout main
        merge release/1.1.0 tag: "v1.1.0"
        branch feature/US2 order: 4
        commit
        commit
        commit
        checkout main
        merge feature/US2
{{< /mermaid >}}

## GitLab Flow

GitLab Flow est une autre approche alternative à GitFlow qui a été proposé par les équipes de développement de [GitLab](https://about.gitlab.com/topics/version-control/what-is-gitlab-flow/) en 2016.

Son approche combine celle des branches de fonctionnalité avec une prise en charge de multiples environnements de déploiement.
Elle est donc plus particulière adaptée aux grandes organisations qui ont un système informatique complexe.

Dans GitLab Flow, `main` est une branche perpétuelle qui sert au développement. On en découle des branches de fonctionnalités éphémères.
Il existe également autant de branches permanentes que d'environnements de déploiement. Les fonctionnalités et les correctifs se déplacent entre les branches par fusion.

### Exemple

{{< mermaid align="left" >}}
    gitGraph
        commit
        branch qualification order: 3
        commit
        checkout main
        branch production order: 5
        commit tag: "v1.0.0"
        checkout main
        branch feature/US1 order: 1
        commit
        commit
        checkout production
        branch hotfix/1.0.1 order: 4
        checkout hotfix/1.0.1
        commit
        commit
        commit
        checkout production
        merge hotfix/1.0.1 tag: "v1.0.1"
        checkout qualification
        merge hotfix/1.0.1
        checkout main
        merge qualification
        branch feature/US2 order: 2
        commit
        commit
        checkout feature/US1
        commit
        checkout main
        merge feature/US1
        checkout qualification
        merge main
        checkout production
        merge qualification tag: "v1.1.0"
        checkout feature/US2
        commit
        checkout main
        merge feature/US2
        checkout qualification
        merge main
{{< /mermaid >}}

Le GitLab Flow permet de maintenir plusieurs versions de recette et de production en parallèle, et de maîtriser les fonctionnalités proposées.
Mais il demande de faire preuve de vigilance dans les opérations de fusion pour s'assurer qu'un correctif fait à un endroit a bien été répercuté partout où il devait l'être.

La lisibilité de l'historique peut également être améliorée en utilisant des `rebase`.

## Remarques

Il existe bien d'autres flux de travail pour Git et aucun n'a vocation à être une solution universelle qui s'adapte à tous les environnements.

Il est même tout à fait possible de concevoir un flux "sur mesure" pour répondre à un besoin spécifique. 
Le plus important est surtout que toute l'équipe qui travaille sur un projet ait connaissance du flux en vigueur et l'applique.
