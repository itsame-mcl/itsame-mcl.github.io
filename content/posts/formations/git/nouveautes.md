---
title: "Quoi de neuf côté Git ?"
description: "Les évolutions récentes de Git utiles à connaître, et les changements annoncés pour Git 3.0."
date: 2026-10-28T12:00:00+01:00
lastmod: 2026-10-28T12:00:00+01:00
tags: ["Git"]
categories: ["Formation"]
menu:
  sidebar:
    name: Quoi de neuf côté Git ?
    identifier: nouveautes
    parent: git
    weight: 80
---

Git publie une version environ tous les trimestres. Cette page recense, sans prétendre à l'exhaustivité, les évolutions récentes les plus utiles pour les pratiques décrites dans cette formation. La référence complète reste constituée par les notes de version de chaque publication, disponibles sur le [site officiel de Git](https://git-scm.com/).

{{< alert type="info" >}}
Page rédigée en octobre 2026, alors que la dernière version stable était Git 2.56 (28 septembre 2026). Les versions plus récentes ne sont pas couvertes.
{{< /alert >}}

## Des commandes plus claires

- **Git 2.23 : `git switch` et `git restore`.** Elles remplacent les principaux usages de `git checkout` (changer de branche, créer une branche, restaurer des fichiers). `git checkout` reste valide.
- **Git 2.46 : sous-commandes de `git config`.** `git config list`, `get`, `set` et `unset` offrent une syntaxe plus lisible que les options historiques.
- **Git 2.52 : `git last-modified`.** Cette commande affiche, pour chaque fichier, le dernier commit qui l'a modifié. Une nouvelle commande `git repo` permet par ailleurs de lire des caractéristiques du dépôt.

## Réécrire l'historique plus simplement

La commande expérimentale `git history` propose des réécritures guidées de l'historique récent, sans passer par un rebase interactif :

- Git 2.54 : introduction de la commande, avec `split` pour scinder un commit en deux ;
- Git 2.55 : sous-commande `fixup` ;
- Git 2.56 : sous-commande `drop`, qui retire un commit et rejoue ses descendants sur son parent.

Comme toute réécriture d'historique, ces commandes ne doivent servir que sur des commits non partagés. Leur caractère expérimental signifie que leur syntaxe peut encore évoluer.

## Confort et sécurité au quotidien

- **Hooks définis dans la configuration** (Git 2.54), pouvant être partagés de façon centralisée, puis **exécutés en parallèle** (Git 2.55).
- **Démon `fsmonitor` pour Linux** (Git 2.55), qui accélère les commandes interrogeant l'état du répertoire de travail.
- **`git checkout -m`** crée désormais un stash pour sauvegarder les modifications locales, ce qui permet de résoudre plusieurs fois les conflits (Git 2.55).
- **Séquences de contrôle de terminal** issues des messages d'un dépôt distant largement neutralisées par défaut, à l'exception des couleurs (Git 2.55).
- **Git 2.56 :** `git status` suggère la bonne commande `git pull` quand la branche est en retard ou a divergé ; `git add --resolved` indexe les fichiers dont les conflits sont résolus ; `git branch --delete-merged` supprime les branches locales déjà fusionnées ; `git bisect --reset-when-found` referme automatiquement la recherche.

## Git 3.0 : ce qui est annoncé

Git 3.0 sera la prochaine version « majeure », qui autorise des changements incompatibles. Selon la documentation du projet sur les ruptures prévues (*breaking changes*) :

- les nouveaux dépôts utiliseront **`main`** comme nom de branche initiale par défaut ;
- le **hachage par défaut** des nouveaux dépôts passera de SHA-1 à **SHA-256** ;
- le support du langage **Rust**, optionnel à ce jour, deviendra obligatoire pour compiler Git.

Aucune date de publication n'est annoncée à ce jour. En attendant, il est possible de s'y préparer en configurant `init.defaultBranch main`.
