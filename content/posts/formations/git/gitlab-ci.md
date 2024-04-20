---
title: "Introduction à GitLab CI"
date: 2023-04-16T19:00:00+01:00
tags: ["GitLab"]
categories: ["Formation"]
mermaid: true
menu:
  sidebar:
    name: Introduction à GitLab CI
    identifier: gitlab-ci
    parent: git
    weight: 60
---

L'intégration continue (*Continuous Integration, CI*) est une pratique de développement logiciel qui consiste à tester et à construire automatiquement un projet chaque fois qu'un développeur soumet un changement dans le code source.
Cette pratique vise à détecter rapidement les erreurs de code et à garantir que le code est fonctionnel et prêt à être déployé.

Un **pipeline** d'intégration continue est un processus automatisé qui permet de construire, tester et déployer un projet.
Il s'agit d'une série d'étapes configurées pour être exécutées automatiquement par un `runner` lorsque des événements surviennent un dépôt (comme un commit).

## GitLab CI/CD

GitLab CI/CD est l'outil permettant de configurer des pipelines d'intégration continue dans un projet géré sur GitLab.

Il s'appuie sur les runners [GitLab Runner](https://docs.gitlab.com/runner/) qui sont une technologie open source pouvant être déployée sur sa propre installation.

## Configurer un pipeline GitLab CI/CD

La configuration d'un pipeline GitLab CI/CD repose sur la rédaction d'un fichier de configuration nommé "manifeste".

Par convention, le manifeste se nomme `.gitlab-ci.yml` et doit être placé à la racine du dépôt.
Le manifeste est écrit en [YAML](https://www.redhat.com/fr/topics/automation/what-is-yaml), un langage de sérialisation de données généralement utilisé pour écrire des fichiers de configuration.

### Exemple de syntaxe YAML

```yaml
# Commentaire
cle: valeur
parent:
  enfant: valeur
liste:
  - option 1
  - option 2
niveau1:
  niveau2:
    niveau3a: valeur a
    niveau3b: |
      1 choix 1
      2 choix 2
    niveau3c:
      - liste
```

### Jobs

Un pipeline GitLab CI/CD est composé de `jobs`, qui sont un ensemble d'instructions de ligne de commande (un script) qui doivent être exécutées par le runner :
  ```yaml
  nom-du-job:
    script: 
      - commande 1
      - commande 2
  ```
Par défaut, tous les jobs définis dans le manifeste s'exécutent simultanément.

### Images

Les runners GitLab reposent sur une technologie de conteneurisation compatible avec Docker.

Il est donc possible de demander à un job de s'exécuter à partir d'une image Docker, pour éviter d'avoir à configurer à la main un environnement :
  ```yaml
  build:
    image: maven/3-eclipse-temurin-21 # Maven 3 + Java 21
    script: 
      - mvn package
  ```

### Étapes

Il est possible de regrouper des jobs par étapes, nommées `stages` qui s'exécuteront de manière séquencée.
  - Tous les jobs d'une même étape s'exécutent simultanément, puis GitLab passe aux jobs de l'étape suivante.

Le manifeste doit donc contenir une déclaration des étapes du pipeline, puis chaque job doit être rattaché à une étape.

```yaml
stages:
  - build
  - test

build:
  image: maven/3-eclipse-temurin-21
  stage: build
  script:
    - mvn package
  
unit-test:
  image: maven/3-eclipse-temurin-21
  stage: test
  script:
    - mvn test
```

### Règles de lancement conditionnel

Par défaut, GitLab CI/CD exécute le pipeline à chaque fois qu'un commit est envoyé.

Il est possible de fixer des conditions pour modifier ce comportement, par exemple pour n'exécuter certaines étapes que dans certaines branches.
Le mot-clé `rules` permet de fixer ces règles de lancement conditionnel pour un job.

Au sein du bloc `rules`, il est possible de fixer une ou plusieurs conditions avec `if`.
Il faut et il suffit qu'une des conditions soit respectée pour qu'un job puisse être exécuté.

Plusieurs variables usuelles sont disponibles pour rédiger ces conditions :
  - `$CI_COMMIT_BRANCH` : branche du commit
  - `$CI_COMMIT_TAG` : tags du commit
  - `$CI_COMMIT_TITLE` : message du commit

```yaml
deploy:
  image: maven/3-eclipse-temurin-21
  script: 
    - mvn deploy
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
    - if: $CI_COMMIT_TITLE =~ /Deploy.*/
```
- Dans cet exemple, le job `deploy` ne s'exécutera que si le pipeline est déclenché depuis la branche `main` ou si le message de commit débute par "Deploy".

### Modes d'exécution

Les modes d'exécution sont une autre façon de conditionner le lancement d'un job.

Par défaut, les jobs d'une étape ne se lancent que si tous les jobs de l'étape précédente se sont terminés avec succès. L'option `when` permet de modifier ce comportement.
  - `when` peut être combiné avec `rules` pour créer des scénarios d'exécution complexes.

Plusieurs modes d'exécution sont disponibles :
  - `on_success` : seulement si tous les jobs de l'étape précédente réussissent (mode par défaut)
  - `on_failure` : seulement si au moins un job de l'étape précédente a échoué
  - `always` : toujours exécuter ce job
  - `never` : ne jamais exécuter ce job (utile en combinaison avec `rules`)
  - `manual` : ne pas exécuter automatiquement ce job, mais permettre de le lancer manuellement

Il est également possible de rendre l'échec d'un job non bloquant avec `allow-failure: true`

```yaml
deploy:
  image: maven/3-eclipse-temurin-21
  script: 
    - mvn deploy
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
    - if: $CI_COMMIT_TITLE =~ /Deploy.*/
      when: manual
```
- Désormais, le job `deploy` ne se lancera plus automatiquement si le commit commence par "Deploy", mais une option permettant de le lancer manuellement sera proposée à la place.

### Cache

Le cache permet de sauvegarder des fichiers/dossiers d'un runner et de les partager tout au long du pipeline.
Il est détruit une fois le pipeline terminé.

L'utilisation du cache permet par exemple d'éviter de rebuild plusieurs fois un même projet entre les différentes étapes du pipeline.

Un bloc `cache` doit préciser les fichiers et dossiers concernés dans le sous-bloc `paths`.
Par défaut, le job commencera par récupérer les fichiers du cache au début de son exécution, et écrira les modifications à la fin.
Ce comportement peut être modifié avec l'option `policy` :
  - `pull` : récupérer le cache, mais ne pas écrire les modifications
  - `push` : ne pas récupérer le cache, mais écrire les modifications

```yaml
stages:
  - build
  - verify

build:
  image: maven/3-eclipse-temurin-21
  stage: build
  script:
    - mvn package
  cache:
    paths:
      - target
    policy: push
```
- À l'issue de l'exécution de l'étape build, le dossier `target` sera mis en cache pour être réutilisé à l'étape `verify`.

### Artefacts

Les artefacts ont un fonctionnement proche du cache, à ceci près qu'ils sont préservés à l'issue du pipeline.
Ils peuvent donc être réutilisés dans un autre pipeline, publiés ou bien encore téléchargés.

Les artefacts se configurent grâce à un bloc `artifacts` qui se décompose en plusieurs sous-blocs :
  - `paths` permet de définir les fichiers et dossiers du runner à rendre disponibles
  - `name` définit le nom de l'archive zip qui contiendra l'artefact
  - `expire_in` fixe la durée de vie de l'artefact. Par défaut, cette durée s'exprime en secondes, mais il est possible de préciser une autre unité.

```yaml
stages:
  - build
  - verify

build:
  image: maven/3-eclipse-temurin-21
  stage: build
  script:
    - mvn package
  artifacts:
    paths:
      - target
    name: build
    expire_in: 1 week
```
- Ce job rendra le dossier `target` disponible au téléchargement dans un fichier nommé `build.zip`. Ce fichier sera conservé par GitLab pendant 1 semaine.

## Superviser un pipeline GitLab

Dès qu'un pipeline est configuré sur un dépôt GitLab, une icône apparaît en regard de chaque commit.
Cette icône indique le résultat du pipeline :
  - Une coche verte indique un pipeline réussi
  - Un point d'exclamation jaune indique une réussite avec des avertissements
  - Une croix rouge signale un pipeline en échec
  - Un rond bleu signifie que le pipeline est en cours d'exécution
  - Une flèche grise invite à exécuter une étape en mode manuel

### Détails d'un pipeline

{{< img src="/images/posts/formations/git/gitlab-ci/pipeline.png" title="Détail d'un pipeline GitLab" >}}

En cliquant sur l'icône, on peut accéder à l'interface détaillée du pipeline :
- Chaque colonne correspond à une étape
- Chaque pastille correspond à un job, avec son résultat d'exécution

### Détails d'un job

{{< img src="/images/posts/formations/git/gitlab-ci/job.png" title="Détail d'un job GitLab" >}}

GitLab permet d'accéder aux détails d'exécution d'un job, et notamment aux logs du runner.
  - Cette interface permet également de télécharger les artefacts.