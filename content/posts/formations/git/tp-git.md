---
title: "Travaux pratiques : une calculatrice Java sous Git"
description: "Huit exercices pour pratiquer Git et GitLab sur un mini-projet : commits, branches, conflits, merge requests, rebase, tickets et wiki."
date: 2026-10-28T12:00:00+01:00
lastmod: 2026-10-28T12:00:00+01:00
tags: ["Git", "GitLab", "Exercices"]
categories: ["Formation"]
menu:
  sidebar:
    name: "Travaux pratiques"
    identifier: tp-git
    parent: git
    weight: 65
---

Ces travaux pratiques vous font pratiquer Git et GitLab à travers un mini-projet : une calculatrice en Java, qui évolue au fil des exercices. Vous n'avez pas besoin de compiler le code Java : l'objectif est de manipuler Git, pas d'apprendre Java.

## Avant de commencer

### Objectifs pédagogiques

- Maîtriser les commandes Git essentielles (`init`, `add`, `commit`, `push`, `pull`).
- Gérer des branches et résoudre des conflits de fusion.
- Travailler en équipe avec GitLab : merge requests, tickets, jalons, wiki.
- Utiliser des techniques avancées : `rebase`, `stash`, `cherry-pick`, `revert`.

### Matériel et organisation

- Git installé (voir [Premiers pas]({{< relref "first-steps" >}})) et un terminal Unix : sous Windows, Git Bash.
- Un compte gratuit sur [gitlab.com](https://gitlab.com/), avec une [clé SSH]({{< relref "software-forge" >}}) configurée.
- Un éditeur de texte (Visual Studio Code, Notepad++, IntelliJ…).
- Environ 6 heures en tout : 2 heures de lecture des pages de cours et 3 h 30 d'exercices, hors pauses.

Le TP est organisé en quatre blocs progressifs :

| Bloc | Thématique | Exercices |
|---|---|---|
| Bloc 1 | Fondamentaux Git | 1 et 2 |
| Bloc 2 | Branches et collaboration | 3, 4 et 5 |
| Bloc 3 | Techniques avancées | 6 et 7 |
| Bloc 4 | Outils GitLab | 8 |

{{< alert type="pair" >}}
Plusieurs exercices proposent une variante à deux, pour simuler un vrai travail d'équipe. Si vous travaillez seul, vous pouvez simuler un second développeur avec un deuxième clone du dépôt dans un autre dossier (c'est précisément ce que propose l'exercice 7).
{{< /alert >}}

{{< alert type="warning" >}}
Dans tous les exercices, les commandes sont à saisir dans un interpréteur de commandes de type Unix, comme Git Bash sous Windows.
{{< /alert >}}

## Bloc 1 : Fondamentaux Git

**Durée indicative des exercices : 45 min.** Cours associé : [Introduction]({{< relref "introduction" >}}), [Premiers pas]({{< relref "first-steps" >}}), [Gérer un dépôt Git]({{< relref "repo-management" >}}) (dépôt local, historique, tags) et [Travailler avec GitLab]({{< relref "software-forge" >}}) (clés SSH, dépôt distant).

{{< alert type="tip" >}}
Pour ne pas vous perdre entre les trois zones de Git, pensez à la photographie : `git add` prépare le cadrage (on choisit ce qui entrera dans l'image), `git commit` prend la photo, et `git push` la publie. Si vous voulez vous le représenter, dessinez sur une feuille : répertoire de travail → index → dépôt.
{{< /alert >}}

{{< alert type="pitfall" >}}
- Oubli de `git add` avant `git commit` : rien n'est commité.
- Fichiers `.class` ou `.jar` commités : c'est à cela que sert le `.gitignore`.
- SSH non configuré : prévoyez une dizaine de minutes pour le mettre en place (voir [Travailler avec GitLab]({{< relref "software-forge" >}})).
- Dépôt créé avec une branche `master` : renommez-la avec `git branch -m main`, ou configurez une fois pour toutes `git config --global init.defaultBranch main`.
{{< /alert >}}


### Exercice 1 : Premiers pas avec Git (30 min)
#### Objectifs

- Initialiser un dépôt Git local
- Créer une première classe Java simple
- Effectuer votre premier commit
- Créer un dépôt distant sur GitLab et pusher le code

#### Commandes à maîtriser

`git init` : Initialise un nouveau dépôt Git dans le répertoire courant

`git add` : Ajoute des fichiers à l'index (zone de staging)

`git commit` : Enregistre les modifications de l'index dans l'historique

`git status` : Affiche l'état actuel du dépôt

`git remote` : Gère les connexions aux dépôts distants

`git push` : Envoie les commits locaux vers un dépôt distant

`git tag` : Crée une étiquette pour marquer une version spécifique

#### À faire
**Étape 1 — Initialiser le projet**

Créez un nouveau répertoire pour votre projet :

```bash
mkdir calculator-project
cd calculator-project
git init
```

**Étape 2 — Créer la structure du projet**

Créez la structure de dossiers Java :

```bash
mkdir -p src
```

**Étape 3 — Créer la première classe Calculator.java**

Créez le fichier src/Calculator.java avec le code suivant :

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public int subtract(int a, int b) {
        return a - b;
    }
}
```

**Étape 4 — Créer un fichier .gitignore**

Créez un fichier .gitignore pour ignorer les fichiers compilés :

```text
*.class
*.jar
out/
target/
```

**Étape 5 — Créer un README**

Créez un fichier README.md :

```markdown
# Projet Calculatrice

Mini-projet Java pour apprendre Git.

## Fonctionnalités
- Addition
- Soustraction
```

**Étape 6 — Premier commit**

Ajoutez tous les fichiers à l'index et faites votre premier commit :

```bash
git add .
git status  # Vérifiez que tous les fichiers sont bien indexés
git commit -m "Initial commit: Calculator avec add et subtract"
```

**Étape 7 — Créer un tag v1.0**

Marquez cette première version :

```bash
git tag -a v1.0 -m "Version 1.0 - Operations de base"
git tag  # Listez les tags pour vérifier
```

**Étape 8 — Créer le dépôt sur GitLab**

- **a.** Connectez-vous à [gitlab.com](https://gitlab.com/)

- **b.** Cliquez sur 'New project' > 'Create blank project'

- **c.** Nom : calculator-project

- **d.** Visibilité : Privé ou Public

- **e.** **Ne cochez PAS** 'Initialize repository with a README'

- **f.** Cliquez sur 'Create project'

**Étape 9 — Lier et pusher vers GitLab**

GitLab affiche les commandes à exécuter. Utilisez celles-ci :

```bash
git remote add origin git@gitlab.com:<votre-identifiant>/calculator-project.git
git branch -m main  # Renomme la branche master en main (inutile si init.defaultBranch est déjà configuré)
git push -u origin main --tags
```

{{< alert type="check" >}}
Sur GitLab, vous devriez voir vos fichiers, votre commit et le tag.
{{< /alert >}}

{{< alert type="pair" >}}
L'un crée le dépôt, l'autre vérifie qu'il peut le voir en lecture seule (ajoutez-le comme Guest pour l'instant).
{{< /alert >}}

### Exercice 2 : Historique et navigation (15 min)
#### Objectifs

- Consulter l'historique des commits de différentes manières
- Utiliser git blame pour tracer l'origine d'une ligne de code
- Comprendre l'importance des messages de commit

#### Commandes à maîtriser

`git log` : Affiche l'historique complet des commits

`git log --oneline` : Version condensée (1 ligne par commit)

`git log --graph` : Affiche un graphique ASCII de l'historique

`git log --stat` : Montre les statistiques de chaque commit

`git blame <fichier>` : Affiche l'auteur de chaque ligne d'un fichier

`git last-modified` : Affiche le dernier commit ayant modifié chaque fichier (Git ≥ 2.52)

#### À faire
**Étape 1 — Ajouter une méthode multiply**

Modifiez src/Calculator.java pour ajouter la multiplication :

```java
public int multiply(int a, int b) {
    return a * b;
}
```

```bash
git add src/Calculator.java
git commit -m "feat: ajout de la multiplication"
```

**Étape 2 — Mettre à jour le README**

Ajoutez la ligne '- Multiplication' dans la section Fonctionnalités :

```bash
git add README.md
git commit -m "docs: mise à jour README avec multiplication"
```

**Étape 3 — Explorer l'historique**

Testez différentes commandes pour visualiser l'historique :

```bash
git log
```

→ Affiche tous les détails (auteur, date, message complet)

```bash
git log --oneline
```

→ Format compact, idéal pour un aperçu rapide

```bash
git log --oneline --graph
```

→ Affiche la structure des branches (utile plus tard)

```bash
git log --stat
```

→ Montre quels fichiers ont été modifiés et combien de lignes

**Étape 4 — Utiliser git blame**

Découvrez qui a écrit chaque ligne du fichier Calculator.java :

```bash
git blame src/Calculator.java
```

Chaque ligne est annotée avec : le hash du commit, l'auteur, la date, et le contenu de la ligne.

**Étape 5 — Utiliser git last-modified (si votre Git est en version 2.52 ou plus)**

Identifiez en une seule commande le dernier commit ayant modifié chaque fichier du projet :

```bash
git last-modified
```

**Étape 6 — Filtrer l'historique**

Expérimentez avec des filtres :

```bash
git log -n 2  # Affiche seulement les 2 derniers commits
git log --author="Votre Nom"  # Vos commits uniquement
git log -- src/Calculator.java  # Commits ayant modifié ce fichier
```

**Étape 7 — Pusher les modifications**

```bash
git push origin main
```

{{< alert type="check" >}}
Sur GitLab, vérifiez que vos 2 nouveaux commits apparaissent dans l'historique du projet.
{{< /alert >}}

{{< alert type="pair" >}}
Chaque personne fait des modifications différentes (l'un ajoute multiply, l'autre ajoute divide). Utilisez git blame pour identifier qui a écrit quoi.
{{< /alert >}}

## Bloc 2 : Branches et collaboration

**Durée indicative des exercices : 1 h 15.** Cours associé : [Gérer un dépôt Git]({{< relref "repo-management" >}}) (branches, fusion, conflits) et [Travailler avec GitLab]({{< relref "software-forge" >}}) (branches protégées, merge requests).

{{< alert type="tip" >}}
L'exercice 3 est simple et rapide. L'exercice 4 est **le moment clé** du TP : prenez le temps de bien lire les marqueurs de conflit. Si vous vous retrouvez bloqué dans une fusion, `git merge --abort` annule tout et permet de recommencer proprement.
{{< /alert >}}

{{< alert type="pitfall" >}}
- Oubli de `git switch` avant de commencer : les commits partent sur la mauvaise branche. Vérifiez toujours la branche active avec `git branch` ou `git status`.
- Marqueurs de conflit laissés dans le code : le commit contiendrait des lignes `<<<<<<< HEAD`.
- Push après la résolution d'un conflit, sans `git add` : l'erreur persiste, car Git considère le fichier toujours en conflit.
{{< /alert >}}


### Exercice 3 : Branches sans conflit (15 min)
#### Objectifs

- Créer et utiliser des branches pour isoler des développements
- Fusionner une branche sans conflit (fast-forward)
- Comprendre l'intérêt du développement en branches parallèles

#### Commandes à maîtriser

`git branch <nom>` : Crée une nouvelle branche

`git branch` : Liste toutes les branches (* = branche active)

`git switch <nom>` : Change de branche active

`git merge <branche>` : Fusionne une branche dans la branche courante

`git branch -d <nom>` : Supprime une branche fusionnée

#### À faire
**Étape 1 — Créer une branche pour la division**

```bash
git branch feature/division
git branch  # Vérifiez que la branche est créée
git switch feature/division
```

**Étape 2 — Implémenter la division dans la branche**

Créez un nouveau fichier src/AdvancedCalculator.java :

```java
public class AdvancedCalculator extends Calculator {
    public double divide(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Division par zéro");
        }
        return (double) a / b;
    }
}
```

```bash
git add src/AdvancedCalculator.java
git commit -m "feat: ajout division avec gestion erreur"
```

**Étape 3 — Mettre à jour le README dans la branche**

Ajoutez '- Division (avec protection division par zéro)' dans README.md :

```bash
git add README.md
git commit -m "docs: ajout division dans README"
```

**Étape 4 — Fusionner la branche dans main**

```bash
git switch main
git merge feature/division
```

→ Git va faire un 'fast-forward' car main n'a pas changé depuis la création de la branche.

**Étape 5 — Vérifier et nettoyer**

```bash
git log --oneline --graph  # Visualisez l'historique
git branch -d feature/division  # Supprimez la branche devenue inutile
git push origin main
```

{{< alert type="check" >}}
Les deux nouveaux commits de la branche doivent apparaître dans l'historique de main.
{{< /alert >}}

{{< alert type="pair" >}}
Chaque personne crée sa propre branche avec une fonctionnalité différente (par exemple, division vs modulo), puis chacun fusionne sa branche dans main à tour de rôle.
{{< /alert >}}

### Exercice 4 : Gestion des conflits (30 min)
#### Objectifs

- Provoquer intentionnellement un conflit de fusion
- Comprendre les marqueurs de conflit de Git
- Résoudre manuellement un conflit
- Finaliser une fusion après résolution

#### Comprendre les conflits

Un conflit survient quand deux branches modifient les mêmes lignes d’un fichier. Git affiche alors des marqueurs pour indiquer les versions en conflit :

```text
<<<<<<< HEAD
Votre version (branche courante)
=======
Version de la branche à fusionner
>>>>>>> nom-de-la-branche
```

#### À faire
**Étape 1 — Créer deux branches qui vont entrer en conflit**

```bash
git branch feature/formatting-style1
git branch feature/formatting-style2
```

**Étape 2 — Modifier Calculator.java dans la première branche**

```bash
git switch feature/formatting-style1
```

Modifiez la méthode add() avec ce style :

```java
public int add(int a, int b)
{
    return a + b;  // Style 1: accolade seule
}
```

```bash
git add src/Calculator.java
git commit -m "refactor: style1 pour add()"
```

**Étape 3 — Modifier la même méthode dans la seconde branche**

```bash
git switch feature/formatting-style2
```

Modifiez la méthode add() avec ce style différent :

```java
public int add(int a, int b) {  // Style 2: accolade sur la ligne
    return a + b;
}
```

```bash
git add src/Calculator.java
git commit -m "refactor: style2 pour add()"
```

**Étape 4 — Fusionner la première branche sans problème**

```bash
git switch main
git merge feature/formatting-style1  # Fusion OK
```

**Étape 5 — Tenter de fusionner la seconde branche → CONFLIT !**

```bash
git merge feature/formatting-style2
```

→ Git vous avertit du conflit. Le fichier Calculator.java contient maintenant les marqueurs de conflit.

**Étape 6 — Examiner le conflit**

```bash
git status  # Montre les fichiers en conflit
```

Ouvrez src/Calculator.java. Vous verrez :

```text
<<<<<<< HEAD
public int add(int a, int b)
{
    return a + b;  // Style 1
}
=======
public int add(int a, int b) {  // Style 2
    return a + b;
}
>>>>>>> feature/formatting-style2
```

**Étape 7 — Résoudre le conflit**

Choisissez un style (ou créez-en un troisième !). Par exemple, gardons style 2 :

```java
public int add(int a, int b) {
    return a + b;
}
```

{{< alert type="warning" >}}
Supprimez tous les marqueurs (`<<<<<<<`, `=======`, `>>>>>>>`).
{{< /alert >}}

**Étape 8 — Finaliser la fusion**

```bash
git add src/Calculator.java  # Marque le conflit comme résolu
git commit  # Vim s'ouvre pour le message de merge
```

{{< alert type="tip" >}}
Dans Vim,
{{< /alert >}}

- **1.** Appuyez sur 'i' pour éditer si nécessaire

- **2.** Appuyez sur 'Esc' puis tapez ':wq' et Entrée

**Étape 9 — Nettoyer et pusher**

```bash
git branch -d feature/formatting-style1
git branch -d feature/formatting-style2
git push origin main
```

{{< alert type="check" >}}
git log --oneline --graph doit montrer un commit de merge avec deux parents.
{{< /alert >}}

{{< alert type="pair" >}}
Chaque personne modifie la même méthode différemment dans sa branche. La première fusion passe, la seconde crée un conflit. Discutez ensemble de la meilleure résolution.
{{< /alert >}}

### Exercice 5 : Merge Requests sur GitLab (30 min)
#### Objectifs

- Protéger la branche principale
- Créer une merge request sur GitLab
- Faire une revue de code et laisser des commentaires
- Valider et fusionner via l'interface web

#### Concept : Merge Request

Une Merge Request (MR) est une demande pour fusionner une branche dans une autre. Elle permet de faire une revue de code avant la fusion, ce qui améliore la qualité et favorise le partage de connaissances dans l'équipe.

#### À faire
**Étape 1 — Protéger la branche main sur GitLab**

- **a.** Allez dans votre projet GitLab

- **b.** Settings > Repository > Protected branches

- **c.** Branch : main

- **d.** Allowed to merge : Maintainers

- **e.** Allowed to push : No one

- **f.** Cliquez sur 'Protect'

**Étape 2 — Créer une branche feature/power**

```bash
git switch -c feature/power  # Crée et active la branche
```

**Étape 3 — Implémenter la fonction puissance**

Ajoutez dans src/AdvancedCalculator.java :

```java
public double power(int base, int exponent) {
    return Math.pow(base, exponent);
}
```

```bash
git add src/AdvancedCalculator.java
git commit -m "feat: ajout fonction puissance"
```

**Étape 4 — Pusher la branche**

```bash
git push -u origin feature/power
```

**Étape 5 — Créer une Merge Request sur GitLab**

- **a.** GitLab affiche un bouton 'Create merge request' après le push

- **b.** Ou : Code > Merge requests > New merge request

- **c.** Source : feature/power, Target : main

- **d.** Titre : 'feat: Ajout fonction puissance'

- **e.** Description : Décrivez ce que fait la fonction

- **f.** Cochez 'Delete source branch when merge request is accepted'

- **g.** Cliquez sur 'Create merge request'

**Étape 6 — Faire une revue de code**

- **a.** Onglet 'Changes' : voir les modifications ligne par ligne

- **b.** Cliquez sur une ligne pour laisser un commentaire

- **c.** Exemple : 'Penser à gérer les exposants négatifs ?'

- **d.** Onglet 'Overview' : ajouter un commentaire général

**Étape 7 — Approuver et fusionner**

- **a.** Bouton 'Approve' (si vous avez les droits)

- **b.** Bouton 'Merge' (plusieurs options possibles)

- **c.** Choisissez 'Merge commit' (conserve l'historique complet)

- **d.** Confirmez

**Étape 8 — Mettre à jour votre dépôt local**

```bash
git switch main
git pull --prune # Récupérer les dernières modifications et mettre à jour les références
git branch -d feature/power 
```

{{< alert type="check" >}}
La branche feature/power a été supprimée automatiquement sur GitLab et manuellement en local (avec git branch -d).
{{< /alert >}}

{{< alert type="pair" >}}
La personne A crée une MR, la personne B fait la revue de code et laisse des commentaires. A répond aux commentaires et corrige si nécessaire, puis B valide et merge.
{{< /alert >}}

## Bloc 3 : Techniques avancées

**Durée indicative des exercices : 1 h 15.** Cours associé : [Gérer un dépôt Git]({{< relref "repo-management" >}}) (stash, cherry-pick, rebase, revert) et [Flux de travail usuels]({{< relref "workflows" >}}).

{{< alert type="tip" >}}
Pour retenir `git stash`, pensez à un tiroir où l'on range temporairement ses affaires en cours. Prenez aussi le temps de comparer l'historique obtenu par un rebase et celui qu'aurait donné un merge. L'exercice 6 est découpé en quatre parties : n'hésitez pas à faire une pause entre elles.
{{< /alert >}}

{{< alert type="pitfall" >}}
- Force push après un rebase : utilisez toujours `--force-with-lease`, jamais `--force`.
- Rebase sur une branche partagée : danger, cela réécrit un historique que d'autres ont déjà récupéré.
- Stash oublié : `git stash list` permet de retrouver ce qui a été mis de côté.
{{< /alert >}}


### Exercice 6 : Manipulation de l’historique (45 min)
#### Objectifs

- Mettre de côté des modifications avec stash
- Linéariser l'historique avec rebase
- Récupérer un commit spécifique avec cherry-pick
- Annuler un commit avec revert

#### Commandes à maîtriser

`git stash` : Met de côté les modifications en cours

`git stash pop` : Réapplique les dernières modifications mises de côté

`git rebase <branche>` : Réécrit l'historique en appliquant les commits au sommet d'une autre branche

`git cherry-pick <commit>` : Applique un commit spécifique sur la branche courante

`git revert <commit>` : Crée un nouveau commit qui annule les modifications d'un commit

#### À faire
##### Partie A : git stash

**Étape 1 — Commencer une modification**

Modifiez src/Calculator.java en ajoutant un commentaire :

```java
// TODO: Ajouter validation des entrées
public int add(int a, int b) {
```

**Étape 2 — Mettre de côté avec stash**

Vous devez travailler sur quelque chose d'urgent :

```bash
git stash -m "WIP: validation des entrées"
git status  # Le fichier redevient propre
```

**Étape 3 — Faire une correction urgente**

Ajoutez une méthode dans AdvancedCalculator.java :

```java
public int modulo(int a, int b) {
    return a % b;
}
```

```bash
git add src/AdvancedCalculator.java
git commit -m "feat: ajout modulo"
```

**Étape 4 — Récupérer le travail en cours**

```bash
git stash list  # Voir les stash disponibles
git stash pop  # Réapplique les modifications
```

##### Partie B : git rebase

**Étape 1 — Créer une branche avec plusieurs commits**

```bash
git switch -c feature/square-root
```

Ajoutez dans AdvancedCalculator.java :

```java
public double squareRoot(int n) {
    return Math.sqrt(n);
}
```

```bash
git add src/AdvancedCalculator.java
git commit -m "feat: ajout racine carrée"
```

Mettez à jour le README :

```bash
git add README.md
git commit -m "docs: ajout racine carrée"
```

**Étape 2 — Simuler un avancement de main**

```bash
git switch main
```

Ajoutez un commentaire au début de Calculator.java :

```java
// Calculatrice de base - Version 1.5
```

```bash
git add src/Calculator.java
git commit -m "docs: mise à jour version"
```

**Étape 3 — Rebaser la branche feature**

```bash
git switch feature/square-root
git rebase main
```

→ Les commits de feature/square-root sont maintenant au-dessus de main

```bash
git log --oneline --graph  # Visualisez l'historique linéaire
```

**Étape 4 — Fusionner la branche**

```bash
git switch main
git merge feature/square-root  # Fast-forward grâce au rebase
```

##### Partie C : git cherry-pick

**Étape 1 — Créer une branche expérimentale avec un commit intéressant**

```bash
git switch -c feature/absolute  # Crée et active la branche
```

Ajoutez une méthode `absolute` dans `src/Calculator.java`, puis commitez :

```java
public int absolute(int n) {
    return Math.abs(n);
}
```

```bash
git add src/Calculator.java
git commit -m "feat: ajout absolute() pour valeur absolue"
```

**Étape 2 — Ajouter d'autres commits non désirés dans la branche expérimentale**

```bash
echo "// Code expérimental à ne pas intégrer" >> src/Calculator.java
git add src/Calculator.java
git commit -m "WIP: code expérimental instable"
```

**Étape 3 — Récupérer uniquement le commit de la méthode `absolute` avec cherry-pick**

```bash
git log --oneline  # Repérez l'identifiant du commit « ajout absolute() »
git switch main
git cherry-pick <identifiant-commit-absolute>
```

→ Le commit avec la méthode `absolute` est maintenant dans `main`, sans avoir récupéré le code expérimental instable.

##### Partie D : git revert

**Étape 1 — Créer un commit à annuler**

Ajoutez une méthode buguée dans `src/Calculator.java`, puis commitez :

```java
public int buggyMethod(int a) {
    return a / 0;  // Bug volontaire !
}
```

```bash
git add src/Calculator.java
git commit -m "feat: méthode expérimentale"
```

**Étape 2 — Annuler le commit avec revert**

```bash
git revert HEAD  # Annule le dernier commit
```

→ Un nouveau commit est créé qui supprime la méthode buguée.

```bash
git log --oneline  # Les deux commits sont visibles dans l'historique
```

{{< alert type="check" >}}
Vous devez avoir un historique linéaire avec le revert visible.
{{< /alert >}}

{{< alert type="pair" >}}
Personne A crée une branche avec 2 commits. Personne B fait un commit sur main entre-temps. A rebase sa branche. Observez ensemble la différence entre rebase et merge.
{{< /alert >}}

### Exercice 7 : Workflow d’équipe réel (30 min)
#### Objectifs

- Simuler un développement en équipe sur le même projet
- Gérer les synchronisations avec pull --rebase
- Lier des commits à des tickets GitLab
- Pratiquer le workflow complet : ticket → branche → MR → merge

#### Configuration

Cet exercice nécessite de travailler en binôme. Si vous êtes seul, simulez deux développeurs en utilisant deux clones du dépôt dans des dossiers différents.

#### À faire
**Étape 1 — Créer deux tickets sur GitLab**

- **a.** Ticket #1 : 'Ajouter validation min/max pour les opérations'

- **b.** Ticket #2 : 'Ajouter méthode negate()'

- **c.** Assignez chaque ticket à un développeur différent

**Étape 2 — Dev A : Implémenter le ticket #1**

```bash
git switch -c feature/1-validation
```

Créez src/Validator.java :

```java
public class Validator {
    public static boolean isInRange(int value, int min, int max) {
        return value >= min && value <= max;
    }
}
```

```bash
git add src/Validator.java
git commit -m "feat: validation min/max (closes #1)"
git push -u origin feature/1-validation
```

**Étape 3 — Dev B : Implémenter le ticket #2 en parallèle**

```bash
git switch -c feature/2-negate
```

Ajoutez dans AdvancedCalculator.java :

```java
public int negate(int n) {
    return -1 * n;
}
```

```bash
git add src/AdvancedCalculator.java
git commit -m "feat: negate (closes #2)"
git push -u origin feature/2-negate
```

**Étape 4 — Dev A : Créer une MR et la faire valider**

- **a.** Créez une MR depuis feature/1-validation vers main

- **b.** Dev B fait la revue et approuve

- **c.** Dev A merge la MR

**Étape 5 — Dev B : Synchroniser avec main avant de créer sa MR**

```bash
git switch feature/2-negate
git fetch origin  # Récupère les dernières modifications
git rebase origin/main  # Rebase sur le main à jour
```

→ Les commits de Dev B sont maintenant au-dessus de ceux de Dev A

**Étape 6 — Dev B : Créer sa MR et la faire valider**

```bash
git push --force-with-lease origin feature/2-negate
```

- **a.** Créez une MR depuis feature/2-negate vers main

- **b.** Dev A fait la revue et approuve

- **c.** Dev B merge la MR

**Étape 7 — Les deux devs : Synchroniser en local**

```bash
git switch main
git pull --rebase origin main
```

**Étape 8 — Vérifier la fermeture automatique des tickets**

Sur GitLab, les tickets #1 et #2 doivent être automatiquement fermés car les messages de commit contiennent le mot-clé closes suivi du numéro de ticket. Une simple mention (#1) crée un lien vers le ticket, mais seuls les mots-clés closes, fixes ou resolves déclenchent la fermeture automatique.

{{< alert type="check" >}}
git log --oneline --graph doit montrer un historique linéaire avec les deux features intégrées dans l'ordre.
{{< /alert >}}

**Bonnes pratiques :**

- Toujours faire git fetch + git rebase origin/main avant de créer une MR
- Référencer les tickets dans les commits (#X) et les fermer avec closes #X
- Utiliser --force-with-lease au lieu de --force (empêche d’écraser par inadvertance le code d’un autre développeur)
- Faire des commits atomiques et des messages descriptifs

## Bloc 4 : Outils GitLab

**Durée indicative des exercices : 15 min.** Cours associé : [Travailler avec GitLab]({{< relref "software-forge" >}}) (rôles, tickets, jalons, wiki) et [Introduction à GitLab CI]({{< relref "gitlab-ci" >}}).

{{< alert type="tip" >}}
Cet exercice est court mais complet, et le moins critique du TP : si vous manquez de temps, vous pouvez le sauter.
{{< /alert >}}


### Exercice 8 : Gestion de projet complète (15 min)
#### Objectifs

- Créer des jalons (milestones) pour structurer le projet
- Gérer les permissions et les rôles d'équipe
- Documenter le projet avec le Wiki
- Avoir une vue d'ensemble des fonctionnalités GitLab

#### À faire
**Étape 1 — Créer un jalon 'Version 2.0'**

- **a.** Plan > Milestones > New milestone

- **b.** Titre : Version 2.0

- **c.** Date d'échéance : 2 semaines à partir d'aujourd'hui

- **d.** Description : Calculatrice scientifique complète

**Étape 2 — Créer des tickets pour Version 2.0**

Créez 3 tickets et associez-les au jalon :

- **a.** 'Ajouter fonction logarithme' - Label: feature

- **b.** 'Ajouter fonction exponentielle' - Label: feature

- **c.** 'Créer tests unitaires' - Label: testing

**Étape 3 — Configurer les permissions**

Si vous travaillez en binôme :

- **a.** Manage > Members

- **b.** Invitez votre binôme avec le rôle 'Developer'

- **c.** Expliquez les différences entre Guest, Reporter, Developer, Maintainer

**Étape 4 — Créer la documentation dans le Wiki**

- **a.** Plan > Wiki > Create your first page

- **b.** Titre : Documentation API

- **c.** Contenu (exemple) :

```markdown
# API Calculatrice

## Calculator
- `add(int a, int b)` : Addition de deux nombres
- `subtract(int a, int b)` : Soustraction
- `multiply(int a, int b)` : Multiplication

## AdvancedCalculator
- `divide(int a, int b)` : Division (gère division par zéro)
- `power(int base, int exp)` : Puissance
- `squareRoot(int n)` : Racine carrée
- `absolute(int n)` : Valeur absolue
- `negate(int n)` : Opposé
```

**Étape 5 — Explorer les autres fonctionnalités GitLab**

- **a.** Analyze > Repository analytics : graphiques d'activité

- **b.** Plan > Boards : visualisation Kanban des tickets

- **c.** Settings > General > Badges : badges de statut pour README

{{< alert type="check" >}}
Votre projet est maintenant structuré avec jalons, tickets, wiki et permissions configurées.
{{< /alert >}}

{{< alert type="pair" >}}
Créez ensemble un board Kanban avec colonnes To Do / In Progress / Review / Done. Déplacez les tickets entre les colonnes au fur et à mesure.
{{< /alert >}}

## Pour aller plus loin

### Défis supplémentaires

Si vous avez terminé tous les exercices, ces idées prolongent le TP :

- le **rebase interactif** (`git rebase -i`) pour réordonner, fusionner ou reformuler des commits ;
- `git bisect` pour retrouver le commit qui a introduit un bug ;
- la commande expérimentale `git history`, disponible depuis Git 2.54 (voir [Quoi de neuf côté Git ?]({{< relref "nouveautes" >}})) ;
- une première chaîne d'intégration continue avec GitLab CI (voir [Introduction à GitLab CI]({{< relref "gitlab-ci" >}})).

### En cas de blocage

| Problème | Solution |
|---|---|
| Git non installé | Installer Git depuis [git-scm.com](https://git-scm.com/) |
| Connexion HTTPS bloquée | Utiliser SSH, en le configurant pendant l'exercice 1 si besoin |
| Fusion en conflit qui n'aboutit pas | `git merge --abort`, puis recommencer calmement |

### Ce que vous avez appris

| Bloc | Compétences acquises |
|---|---|
| Fondamentaux | `init`, `add`, `commit`, `push`, `pull`, `status`, `log`, `blame`, `tag` |
| Branches | `branch`, `switch`, `merge`, résolution de conflits, merge requests |
| Avancé | `stash`, `rebase`, `cherry-pick`, `revert`, workflow d'équipe |
| GitLab | Tickets, jalons, permissions, wiki, merge requests, revue de code |

### Bonnes pratiques à retenir

- Committer souvent, avec des messages clairs et descriptifs.
- Une branche = une fonctionnalité.
- Toujours `pull` avant de `push`.
- Protéger la branche `main` et passer par des merge requests.
- Faire des revues de code constructives.
- Utiliser un `.gitignore` dès le début du projet.
- Lier les commits aux tickets (`#X` dans les messages).

### Ressources

- Documentation officielle de Git : <https://git-scm.com/doc>
- Documentation de GitLab : <https://docs.gitlab.com>
- *Pro Git*, livre gratuit : <https://git-scm.com/book/fr/v2>
- Interfaces graphiques : GitKraken, SourceTree ; extension GitLens pour VS Code.
- Pense-bêtes : [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf), [GitLab Git Cheat Sheet](https://about.gitlab.com/images/press/git-cheat-sheet.pdf).
