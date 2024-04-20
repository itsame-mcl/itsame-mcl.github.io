---
title: "Introduction"
date: 2023-04-16T19:00:00+01:00
tags: ["Git", "GitLab"]
categories: ["Formation"]
menu:
  sidebar:
    name: Introduction
    identifier: introduction
    parent: git
    weight: 10
---

[Git](https://git-scm.com/) a été créé par Linus Torvalds, le créateur du système d'exploitation Linux, en 2005.
Il a été conçu pour être un VCS décentralisé, capable de gérer efficacement les grands projets open source tels que le développement du noyau Linux.
Git a rapidement gagné en popularité auprès de la communauté du développement de logiciels en raison de sa rapidité, de sa facilité d'utilisation et de sa flexibilité.

Git, en tant que VCS décentralisé (ou distribué), permet à chaque développeur de disposer d'une copie complète de l'historique des modifications et du code source sur leur ordinateur. 
Ils peuvent dont travailler en mode déconnecté (sans accès à Internet ou à un serveur centralisé) et ont accès à toutes les versions du code source.
Cela signifie qu'**il n'y a pas de point unique de défaillance**, car le référentiel de code est distribué sur plusieurs machines.

[GitLab](https://about.gitlab.com/) est une plateforme web open source de gestion de projets de développement de logiciels qui utilise Git pour la gestion de versions de code source.
GitLab fournit des fonctionnalités de collaboration supplémentaires telles que des tableaux de bord de suivi de projets, des outils de gestion de bugs ou bien encore des outils d'intégration continue.
Il fournit également des fonctionnalités de gestion d'équipe telles que la gestion des utilisateurs, des permissions et des groupes de projets.

## Pourquoi utiliser un système de gestion de versions ?

- Un **système de gestion de versions (VCS)** est un outil permettant de suivre les 
modifications apportées au code source d'un projet au fil du temps.

- Son utilisation permet de :
  - travailler ensemble sur un même code source
  - conserver l'historique des modifications apportées
  - revenir à des versions précédentes
  - résoudre les conflits entre les modifications apportées par différents développeurs

## Quels sont les avantages ?

- **Sécurité**
  - **Sauvegarde automatique** : les développeurs n'ont pas besoin de se rappeler de faire des sauvegardes régulières de leur code, car le VCS s'en charge automatiquement.
  - **Facilité de récupération** : si un développeur supprime accidentellement un fichier important ou introduit une erreur dans le code, il peut facilement revenir à une version précédente du code grâce à l'historique des modifications stocké dans le VCS.
- **Travail en équipe**
  - **Collaboration efficace** : chaque développeur peut travailler sur sa propre branche de code et fusionner ses modifications avec la branche principale une fois qu'il est satisfait de son travail.
  - **Gestion des conflits** : si deux développeurs ont modifié le même fichier de code, le VCS les alertera et les aidera à résoudre le conflit en fusionnant les modifications de manière appropriée.
- **Documentation**
  - **Historique des modifications** : les développeurs peuvent facilement accéder à des versions antérieures du code et voir qui a effectué quelles modifications, quand et pourquoi.
  - **Commentaires** : lorsqu'un développeur effectue des modifications avec un VCS, il peut ajouter un message pour décrire les modifications apportées au code.