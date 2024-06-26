---
title: "Gérer un dépôt Git"
description: Créer un dépôt, écrire des commits, gérer des multiples branches, consulter et manipuler l'historique
date: 2023-04-16T19:00:00+01:00
tags: ["Git"]
categories: ["Formation"]
mermaid: true
menu:
  sidebar:
    name: Gérer un dépôt Git
    identifier: repo-management
    parent: git
    weight: 30
---

## Dépôt local

Un **dépôt** (ou "repository" en anglais) est l'endroit où Git stocke l'historique des versions d'un projet de développement.
Il existe deux types de dépôts dans Git :
  - Un **dépôt local** est une copie du dépôt sur l'ordinateur local d'un développeur
  - Un **dépôt distant** est un dépôt hébergé sur un serveur distant, accessible via Internet.

### Créer un dépôt local

Pour créer un dépôt local avec Git, il suffit de se positionner en ligne de commandes (via `cd`) dans un dossier à transformer en dépôt et d'utiliser la commande :
  ```bash
  git init
  ```
Ceci va créer un sous-dossier `.git` (caché sous UNIX, pour le voir : `ls -la`) qui sert notamment à stocker l'historique. Il n'est pas utile d'y accéder en utilisation courante.

Il est possible de consulter l'état d'un dépôt grâce à la commande :
  ```bash
  git status
  ```
- Pour un dépôt nouvellement créé dans un dossier vide, elle doit proposer la sortie suivante :
  ```console
  On branch main

  No commits yet

  nothing to commit (create/copy files and use "git add" to track)
  ```


## Manipulation des fichiers

Avec Git, un fichier peut être présent dans 3 zones distinctes :
  - le répertoire de travail
  - l'index
  - le dépôt

`git status` permet de connaître l'état de chaque fichier

### Répertoire de travail

Le **répertoire de travail** correspond au contenu du dossier sur l'ordinateur du développeur.
Par défaut, aucun fichier n'est suivi par Git. Par exemple, après la création d'un fichier `exemple.txt`, la commande `git status` donne la sortie suivante :
  ```console
  On branch main
  
    No commits yet
  
    Untracked files:
    (use "git add <file>..." to include in what will be committed)
    exemple.txt
  
    nothing added to commit but untracked files present (use "git add" to track)
  ```

{{< mermaid align="left" >}}
    classDiagram
      direction RL
      Index..Répertoire
      Dépôt..Index
      class Répertoire{        +exemple.txt a4d584      }
      class Index{      }
      class Dépôt{      }
{{< /mermaid >}}

### Index

Pour demander à Git de commencer à suivre un fichier, il faut l'ajouter à l'**index**.
L'index est une zone tampon entre le répertoire de travail et le dépôt qui rassemble l'ensemble des modifications prêtes à être ajoutées à un commit.

Concrètement, on indexe un fichier avec la commande suivante :
  ```bash
  git add <fichier>
  ```
  - On peut utiliser un `.` à la place du nom du fichier pour demander à Git d'indexer tout le répertoire de travail.

Une fois un fichier indexé, il est prêt à être inclus à un commit. La sortie de `git status` reflète cette évolution :
  ```console
  On branch main

  No commits yet
  
  Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
  new file:   exemple.txt
  ```

Il est possible de désindexer un fichier sans le supprimer avec la commande :
  ```bash
  git rm --cached <fichier>
  ```
  - L'option `-f` peut être utilisée à la place de `--cached` pour supprimer totalement le fichier.

Un fichier indexé devient également suivi par Git, ce qui revient à dire que son hash est recalculé à chaque modification du répertoire de travail.
S'il est à nouveau modifié alors qu'il est toujours dans l'index, Git détectera cette modification :
  ```console
On branch main

  No commits yet
  
  Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
  new file:   exemple.txt
  
  Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
  modified:   exemple.txt
  ```

{{< mermaid align="left" >}}
    classDiagram
      direction RL
      Index<|--Répertoire : git add
      Dépôt..Index
      class Répertoire{
        +exemple.txt a4d584
      }
      class Index{
        +exemple.txt a4d584
      }
      class Dépôt{
      }
{{< /mermaid >}}

### Dépôt

À partir du moment où un fichier est présent dans au moins un commit, il est alors enregistré dans le dépôt.

Un **commit** représente une version spécifique d'un projet à un moment donné. **C'est l'unité de base de l'historique d'un dépôt.**
Il contient une copie des fichiers du projet, ainsi qu'un message décrivant les modifications apportées depuis la version précédente.

Un commit est identifié par un **hash** (SHA-1) calculé par Git sur la base du hash de l'ensemble des fichiers du projet.
On l'abrège souvent à ses premiers caractères (par exemple, `1d0703d3`).

Un commit est composé de l'ensemble des fichiers du dernier commit de la branche actuelle (HEAD) auxquels sont appliquées les modifications de l'index.
Pour effectuer un commit, on utilise la commande suivante :
  ```bash
git commit -m "Message de commit"
  ```

Une fois qu'un commit est réalisé, il devient le nouveau commit de référence (HEAD) à partir duquel Git vérifie si un fichier a été modifié.

Quand une modification a été incluse dans un commit, elle sort de l'index, comme en témoigne la sortie de `git status` :
  ```console
  On branch main
  nothing to commit, working tree clean
  ```

{{< mermaid align="left" >}}
    classDiagram
      direction RL
      Index..Répertoire
      Dépôt<|--Index : git commit
      class Répertoire{
        +exemple.txt a4d584
      }
      class Index{
      }
      class Dépôt{
        +exemple.txt a4d584
      }
{{< /mermaid >}}

#### Messages de commit

Le message de commit sera lisible par tous les développeurs du projet et sera retranscrit dans l'historique, d'où l'importance qu'il retrace fidèlement le contenu du commit. 
Il est donc crucial que les modifications apportées par un commit forment un ensemble cohérent. Il vaut souvent mieux séparer un gros commit difficile à résumer en plusieurs petits commits.

En utilisant la syntaxe `git commit -m`, la longueur du message est limitée à 49 caractères.

#### Modifier le dernier commit

Il est possible de corriger un oubli sur le dernier commit ou de modifier son message avec l'option `--amend` :
  ```bash
  git commit --amend -m "Nouveau message de commit"
  ```
  - Pour ne pas modifier le message de commit, il faut ajouter l'option `--no-edit` à la place de `-m`.

Les modifications actuellement contenues dans l'index seront alors fusionnées avec celles du dernier commit, ce qui va créer un nouveau commit qui remplace l'ancien.

### Autres manipulations sur les fichiers

Git propose des commandes permettant de retranscrire d'autres manipulations usuelles sur les fichiers :
  - Déplacer ou renommer un fichier :
    ```bash
    git mv <ancien_nom> <nouveau_nom>
    ```
  - Supprimer un fichier :
    ```bash
    git rm <fichier_a_supprimer>
    ```

Ces modifications seront ajoutées à l'index et devront être commitées pour être retranscrites dans le dépôt.

### Ignorer des fichiers

Il est également possible de demander à Git d'ignorer de manière permanente des fichiers :

Pour cela, il faut créer à la racine du dépôt un fichier nommé `.gitignore` (sans extension), qui continent la liste des fichiers et dossiers à ignorer.
Le fichier `.gitignore` doit être commité pour être pris en compte.

Il existe des outils en ligne comme [gitignore.io](https://www.toptal.com/developers/gitignore) pour avoir des listes usuelles de fichiers à ignorer selon les types de projets.

## Consulter l'historique d'un dépôt

{{< mermaid align="left" >}}
    gitGraph
      commit id: "3b1d805"
      commit id: "6a2b687"
      commit id: "49eb5d0"
      commit id: "8f7308f"
      commit id: "30d524c" tag: "HEAD"
{{< /mermaid >}}

La commande `git log` permet d'obtenir l'historique complet des commits d'un dépôt, dans l'ordre chronologique inversé :
  ```bash
  git log
  ```
  ```console
  commit 30d524c6603ed1982bdf82eb54d7215a00b22328 (HEAD -> main)
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Fri Apr 14 12:31:00 2023 +0200
  
      Suppression du fichier exemple.txt devenu inutile
  
  commit 8f7308fc1099a44fb25af05c3ee7c6a7ca17f111
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Fri Apr 14 12:30:31 2023 +0200
  
      Correction d'une coquille dans le poème
  
  commit 49eb5d06716e1f0668681b417a884b3d808bacda
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Fri Apr 14 12:30:02 2023 +0200
  
      Le poème est plutôt un haiku
  
  commit 6a2b687e994b4c8341adc6542c313cb860dad452
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Fri Apr 14 12:29:24 2023 +0200
  
      Ajout d'un poème sur l'informatique
  
  commit 3b1d805510f43af8e7b9da97d0bf44dca127a9d1
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Thu Apr 13 16:56:41 2023 +0200
  
      Exemple de commit avec un fichier unique
  ```

- L'option `--oneline` permet d'obtenir un affichage compact, avec une seule ligne par commit :
  ```bash
  git log --oneline
  ```
  ```console
  30d524c (HEAD -> main) Suppression du fichier exemple.txt devenu inutile
  8f7308f Correction d'une coquille dans le poème
  49eb5d0 Le poème est plutôt un haiku
  6a2b687 Ajout d'un poème sur l'informatique
  3b1d805 Exemple de commit avec un fichier unique
  ```

- L'option `--stat` permet de connaître le nombre de modifications effectuées sur chaque fichier :
  ```bash
  git log --stat
  ```
  ```console
  commit 30d524c6603ed1982bdf82eb54d7215a00b22328 (HEAD -> main)
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Fri Apr 14 12:31:00 2023 +0200
  
      Suppression du fichier exemple.txt devenu inutile
  
  exemple.txt | 0
  1 file changed, 0 insertions(+), 0 deletions(-)
  
  commit 8f7308fc1099a44fb25af05c3ee7c6a7ca17f111
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Fri Apr 14 12:30:31 2023 +0200
  
      Correction d'une coquille dans le poème
  
  haiku.txt | 2 +-
  1 file changed, 1 insertion(+), 1 deletion(-)
  
  commit 49eb5d06716e1f0668681b417a884b3d808bacda
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Fri Apr 14 12:30:02 2023 +0200
  
      Le poème est plutôt un haiku
  
  poeme.txt => haiku.txt | 0
  1 file changed, 0 insertions(+), 0 deletions(-)
  
  commit 6a2b687e994b4c8341adc6542c313cb860dad452
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Fri Apr 14 12:29:24 2023 +0200
  
      Ajout d'un poème sur l'informatique
  
  poeme.txt | 3 +++
  1 file changed, 3 insertions(+)
  
  commit 3b1d805510f43af8e7b9da97d0bf44dca127a9d1
  Author: Maxence Collard-Lagalle <maxence@collard-lagalle.me>
  Date:   Thu Apr 13 16:56:41 2023 +0200
  
      Exemple de commit avec un fichier unique
  
  exemple.txt | 0
  1 file changed, 0 insertions(+), 0 deletions(-)
  ```
- Il est possible de combiner les options `--oneline` et `--stat`.

### Filtrer l'historique

`git log` supporte de nombreuses options permettant de filtrer l'historique selon plusieurs critères :
  - `-n <nombre>` : n derniers commits
  - `--before="AAAA-MM-JJ HH:mm"` : commits plus anciens qu'une date
  - `--after="AAAA-MM-JJ HH:mm"` : commits plus récents qu'une date
  - `--author="Nom"` : commits signés par un auteur
  - `-- <fichier>` : commits affectant un fichier

### Rechercher à l'intérieur des commits

L'option `-S` permet de rechercher une chaîne de caractères et d'afficher la liste des commits contenant cette chaîne à l'intérieur des fichiers qu'ils modifient :
  ```bash
  git log -S "Chaîne à rechercher"
  ```
- Il existe également l'option `-G` pour faire une recherche par expression régulière (regex).

### Consulter l'historique détaillé d'un fichier

La commande `git blame` permet de connaître l'historique détaillé d'un fichier en précisant de quel commit viennent chacune de ses lignes dans leur rédaction actuelle :
  ```bash
  git blame <fichier>
  ```
- La sortie de cette commande affiche chaque ligne du fichier dans le terminal, précédé de l'identifiant du commit ayant introduit ou modifié cette ligne, du nom de l'auteur et de la date de ce commit :
  ```bash
  git blame haiku.txt
  ```
  ```console
  6a2b687e poeme.txt (Maxence Collard-Lagalle 2023-04-14 12:29:24 +0200 1) Un clic malencontreux
  8f7308fc haiku.txt (Maxence Collard-Lagalle 2023-04-14 12:30:31 +0200 2) Fichier important supprimé
  6a2b687e poeme.txt (Maxence Collard-Lagalle 2023-04-14 12:29:24 +0200 3) Sauvegarde ? Jamais fait.
  ```

### Comparer deux commits

Grâce à `git diff`, il est possible d'effectuer des comparaisons entre deux états d'un fichier.
  - Si la commande est utilisée sans paramètres, la comparaison s'effectue entre le répertoire de travail et l'index.
  - Il est possible de donner en paramètres un identifiant de commit pour comparer ce commit au répertoire de travail, ou deux identifiants de commit pour les comparer.

Par exemple, il est possible de comparer le commit `49eb5d0` à l'état actuel du dépôt, c'est-à-dire au commit `HEAD`:
  ```bash
  git diff 49eb5d0 HEAD
  ```
  ```diff
  diff --git a/exemple.txt b/exemple.txt
  deleted file mode 100644
  index e69de29..0000000
  diff --git a/haiku.txt b/haiku.txt
  index b3c75e6..2ba1e15 100644
  --- a/haiku.txt
  +++ b/haiku.txt
  @@ -1,3 +1,3 @@
  Un clic malencontreux
  -Fichier portant supprimé
  +Fichier important supprimé
  Sauvegarde ? Jamais fait.
  \ No newline at end of file
  ```

- `git diff` permet également de vérifier les modifications qui seront incluses dans le commit en cours de préparation en comparant l'index et le dernier commit :
  ```bash
  git diff --staged
  ```

### Rechercher un commit défectueux

L'outil `git bisect` permet de retrouver un commit défectueux (par exemple, ayant introduit un bug) par recherche dichotomique :
- Il faut tout d'abord l'initialiser en lui précisant notamment l'identifiant d'un "mauvais commit" (ayant le problème) et d'un "bon commit" (n'ayant pas le problème) :
  ```bash
  git bisect start
  git bisect bad <mauvais commit, vide pour commit actuel>
  git bisect good <bon commit>
  ```
- Git va alors sélectionner un commit situé entre ces deux bornes et remettre le répertoire de travail à l'état de ce commit :
  ```console
  Bisecting: X revisions left to test after this (roughly Y steps)
  ```
- Après avoir vérifié manuellement si le bug est toujours présent, il faut indiquer à Git le résultat de cette vérification avec l'une de ces commandes :
  - `git bisect good` si le bug est absent
  - `git bisect bad` si le bug est présent

- Lorsque Git a réussi à repérer le commit ayant introduit le bug, il indique son identifiant dans la sortie du terminal, ainsi que les détails du commit :
  ```console
  8f7308fc1099a44fb25af05c3ee7c6a7ca17f111 is the first bad commit
  commit 8f7308fc1099a44fb25af05c3ee7c6a7ca17f111
  ...
  ```
- Pour sortir du mode de recherche et revenir à l'état initial du répertoire de travail, il faut réinitialiser git bisect via :
  ```bash
  git bisect reset
  ```

### Annuler un commit

Git propose un mécanisme de `revert` permettant d'annuler les modifications d'un commit. Il consiste à écrire un nouveau commit qui continent l'inverse des modifications du commit original. Ce mécanisme s'utilise avec la commande suivante :
  ```bash
  git revert <commit_a_annuler>
  ```
  - Ce nouveau commit s'inscrit dans l'historique au moment où il est créé, comme n'importe quel autre commit.

### Revenir à un état antérieur de l'historique

`git reset` permet de ramener un dépôt à un état antérieur en supprimant tous les commits réalisés après un commit donné :
  ```bash
  git reset <dernier_commit_a_conserver>
  ```
  - Avec `--soft`, le répertoire de travail est remis à l'état du commit ciblé et les modifications réalisées depuis sont remises dans l'index.
  - Sans option, les modifications restent dans le répertoire de travail, mais pas dans l'index.
  - `--hard` réinitialise **définitivement** le répertoire de travail et l'index.

### Supprimer totalement un fichier de l'historique

Dans le cas où un fichier a été commité **par erreur**, il est possible de demander à Git de réécrire son historique en le filtrant pour supprimer totalement ce fichier :
  ```bash
  git filter-branch --index-filter \
  'git rm -rf --cached --ignore-unmatch <chemin_vers_le_fichier>' HEAD
  ```
- Sur un système avec Python>=3.5 installé, l'extension [git filter-repo](https://github.com/newren/git-filter-repo) fournit une commande simplifiée :
  ```bash
  git filter-repo --invert-paths --path <chemin_vers_le_fichier>
  ```

## Tags

Les tags sont un moyen simple d'associer une étiquette (généralement, un numéro de version) à un commit.
Une fois qu'ils sont positionnés, les tags peuvent être utilisés à la place des identifiants de commits dans presque toutes les commandes de Git.

### Ajouter un tag

Ajouter un tag s'effectue avec la commande :
  ```bash
  git tag <nom_du_tag> <commit>
  ```
  - Si aucun identifiant de commit n'est précisé, le tag s'appliquera au dernier commit (HEAD).
  - Il est possible d'ajouter des informations détaillées à un tag (par exemple, un changelog) en ajoutant l'option `-a`.

### Manipuler les tags

Git peut fournir la liste des tags d'un dépôt :
  ```bash
  git tag --list
  ```

Il est également possible d'afficher les détails d'un tag, notamment sa date et son auteur :
  ```bash
  git tag show <nom_du_tag>
  ```

Enfin, il est possible de supprimer un tag :
  ```bash
  git tag -d <nom_du_tag>
  ```

## Utiliser plusieurs branches

Avec celle de commit, la notion de branche et l'un des concepts clés de Git. 
La maîtriser permet de considérablement simplifier le travail collaboratif.

Une branche est un **enchaînement de commits parallèle** à la version principale du projet.
Par convention, la version principale est la branche `main` (anciennement `master`).

Techniquement, une branche est un tag dynamique qui se déplace automatiquement sur le dernier commit en date de sa lignée.

`HEAD` est le tag du dernier commit de la branche actuellement active.
{{< mermaid align="left" >}}
    gitGraph
      commit
      commit
      branch feature
      commit
      commit
      checkout main
      commit tag: "main"
      checkout feature
      commit tag: "feature, HEAD"
{{< /mermaid >}}
  - Sur cet exemple, `feature` est la branche active.


### Lister les branches d'un dépôt

Pour lister les branches d'un dépôt, la commande à utiliser est `git branch` :
  ```bash
  git branch
  ```
  ```console
  * feature
    main
  ```
  - La branche actuellement active est signalée par l'astérisque (`*`)
  - L'option `-v` permet d'afficher en plus l'identifiant et le message du dernier commit de chaque branche

### Créer une branche

La création de branche s'effectue également grâce à `git branch` :
  ```bash
  git branch <nom_de_la_branche> <commit_initial>
  ```
  - Si aucun commit initial n'est précisé, `HEAD` sera le point de départ de la nouvelle branche.

Le nom d'une branche :
  - ne peut contenir que des caractères ASCII
  - ne doit pas commencer par un tiret
  - ne doit pas contenir deux points consécutifs
  - ne doit pas se terminer par un slash, mais peut en contenir pour créer une hiérarchie

### Changer de branche

`git switch` permet de changer la branche active :
  ```bash
  git switch <branche_a_activer>
  ```
  - Pour les versions de Git antérieures à 2.23.0, la commande était `git checkout <branche>`
  - Tous les nouveaux commits seront affiliés à la branche activée

Changer de branche :
  - Modifie le répertoire de travail et l'index
  - Préserve les modifications en cours
  - Déplace l'étiquette `HEAD`

### Mettre de côté les modifications en cours

Il peut arriver que l'on souhaite temporairement mettre de côté des modifications en cours, par exemple pour travailler en urgence sur un problème.

Git rend cela possible grâce à la commande :
  ```bash
  git stash
  ```
  - Cette commande stocke temporairement les modifications du répertoire de travail et de l'index, et remet le répertoire de travail à l'état du dernier commit de la branche.
  - L'option `--include-untracked` permet d'également inclure les fichiers non suivis par Git.

Pour réappliquer dans la branche active les dernières modifications mises de côté, la commande est :
  ```bash
  git stash pop
  ```
Il est également possible de supprimer des modifications sans les appliquer :
  ```bash
  git stash drop
  ```
Enfin, il est possible d'accumuler plusieurs stashes, qui peuvent être listés :
  ```bash
  git stash list
  ```

### Fusionner deux branches

Fusionner des branches permet d'intégrer des modifications faites sur une branche dans une autre.
C'est une opération cruciale, car elle permet par exemple d'intégrer à une version des productions des fonctionnalités développées en parallèle.

La fusion doit être initiée en ayant activé la branche cible (celle qui doit recevoir les modifications)
La fusion s'effectue avec la commande `git merge`, en précisant la branche source des modifications :
  ```bash
  git merge <branche_source>
  ```

{{< mermaid align="left" >}}
  gitGraph
    commit
    commit id: "1-8a4f40a"
    branch feature
    commit
    commit
    checkout main
    commit
    checkout feature
    commit tag: "feature"
    checkout main
    merge feature id: "6-1a59d24" tag: "main, HEAD"
{{< /mermaid >}}

- Git recherche l'ancêtre commun des branches à fusionner (ici, `1-8a4f40a`) et y injecte les modifications issues de chaque branche, pour créer un nouveau commit dans la branche active, dit commit de merge.
  - Ici, le commit de merge a l'identifiant `6-1a59d24`.

{{< mermaid align="left" >}}
  classDiagram
    direction LR
    Commit1..Commit4
    Commit1..Commit5
    Commit4..Commit6
    Commit5..Commit6
    class Commit1 {
      fichier1.txt 41ad58
      fichier2.txt 1efc25
      fichier3.txt 690a41
    }
    class Commit4 {
      fichier1.txt 914da0
      fichier2.txt 1efc25
      fichier3.txt 690a41
    }
    class Commit5 {
      fichier1.txt 41ad58
      fichier2.txt ea451d
      fichier3.txt 690a41
    }
    class Commit6 {
      fichier1.txt 914da0
      fichier2.txt ea451d
      fichier3.txt 690a41
    }
{{< /mermaid >}}

#### Fusion Fast-Forward

Si le commit de merge calculé par Git est égal au dernier commit de la branche source (il a le même hash), alors Git évite de créer un doublon.
À la place, il procède à une fusion *fast-forward* en déplaçant l'étiquette de la branche cible sur le commit de la branche source.

{{< mermaid align="left" >}}
    gitGraph
      commit
      commit
      branch feature
      commit
      commit
      checkout main
      merge feature tag: "main, feature, HEAD"
{{< /mermaid >}}

#### Conflits de fusion

Un conflit de fusion survient si la même zone d'un même fichier a été modifiée entre l'ancêtre commun d'une part et les branches source et cible simultanément d'autre part.
  - Une zone d'un fichier correspond généralement à une ligne et son voisinage immédiat.

Dans ce cas, Git suspend la fusion et le développeur doit trancher manuellement le conflit en indiquant quelle version conserver.
- Git signale l'échec de la fusion automatique et les conflits dans la sortie de la commande `git merge` :
  ```console
  Auto-merging sonnet.txt
  CONFLICT (add/add): Merge conflict in sonnet.txt
  Automatic merge failed; fix conflicts and then commit the result.
  ```
- La commande `git status` précise également qu'une fusion est en cours et la liste des fichiers en conflit :
  ```console
  On branch main
  You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)
  
  Unmerged paths:
  (use "git add <file>..." to mark resolution)
  both added:      sonnet.txt
  
  no changes added to commit (use "git add" and/or "git commit -a")
  ```

#### Résoudre les conflits de fusion

Pour résoudre les conflits, le développeur doit ouvrir dans un éditeur de texte les fichiers concernés.
Git a inséré dans le fichier des informations sur les modifications effectuées dans les branches source et cible sous le format suivant :
  ```text
  <<<<<<< HEAD
  Version de la branche cible
  =======
  Version de la branche source
  >>>>>>> source
  ```
  - Si une zone est vide, c'est qu'elle n'existe pas dans la branche concernée.

Il est possible, et souvent utile, d'afficher également des informations sur le contenu de l'ancêtre commun via une option de configuration de Git :
  ```bash
  git config --global merge.conflictstyle diff3
  ```
  - Dans ce cas, les informations sur les modifications adopteront la présentation suivante :
  ```text
  <<<<<<< HEAD
  Version de la branche cible
  ||||||| merged common ancestor
  Version de l'ancêtre commun
  =======
  Version de la branche source
  >>>>>>> source
  ```

Une fois le fichier ouvert dans l'éditeur de texte, il est possible de reprendre à l'identique l'une des versions proposées, ou d'en écrire une nouvelle.

Lorsque tous les conflits d'un fichier sont résolus (il n'y a plus de marqueurs ajoutés par Git), le fichier doit être indexé (`git add`)

Après la résolution du dernier fichier, l'index peut finalement être commité (`git commit`), ce qui permettra de finaliser le commit de merge et la fusion des branches.

##### Exemple

- Fichier `sonnet.txt` avant résolution des conflits :
```text
<<<<<<< HEAD
=======
Quand l'écran s'allume, je tape sur mon clavier,
Et je me sens l'âme d'un héros bien armé,
Mais parfois c'est la guerre, les bugs sont aguerris,
Et je dois me résoudre à un peu de répit.

>>>>>>> alt-sonnet
Sur mon écran s'affichent des pixels brillants,
Des octets bien alignés, des programmes ardents,
Des virus dévastateurs, des spams envahissants,
Des câbles emmêlés, des bugs persistants.

<<<<<<< HEAD
Je pianote sur mon clavier, tel un virtuose,
Je créé des dossiers, des fichiers grandioses,
Je navigue sur le web, je me sens comme un rose,
Mais parfois je m'emmêle, je suis un peu névrose.

Je rêve de machines, de logiciels parfaits,
De claviers qui répondent à mes moindres souhaits,
De souris magiques qui font tout à ma place.
=======
Je rêve de machines, de logiciels parfaits,
D'ordinateurs qui pensent, qui lisent dans mes traits,
De robots programmés, qui m'apportent le café.
>>>>>>> alt-sonnet

Mais en attendant, je m'en remets à mon ordinateur,
Avec ses programmes parfois un peu farfelus,
Et je souris, car je sais qu'il est mon sauveur.
```

- Fichier `sonnet.txt` après résolution des conflits :
```text
Quand l'écran s'allume, je tape sur mon clavier,
Et je me sens l'âme d'un héros bien armé,
Mais parfois c'est la guerre, les bugs sont aguerris,
Et je dois me résoudre à un peu de répit.

Je pianote sur mon clavier, tel un virtuose,
Je créé des dossiers, des fichiers grandioses,
Je navigue sur le web, je me sens comme un rose,
Mais parfois je m'emmêle, je suis un peu névrose.

Je rêve de machines, de logiciels parfaits,
D'ordinateurs qui pensent, qui lisent dans mes traits,
De robots programmés, qui m'apportent le café.

Mais en attendant, je m'en remets à mon ordinateur,
Avec ses programmes parfois un peu farfelus,
Et je souris, car je sais qu'il est mon sauveur.
```

Le premier conflit a été résolu en conservant la version de `alt-sonnet` et le second par une ré-écriture mélangeant les deux versions et supprimant un texte commun

- La commande `git status` permet de confirmer que la fusion est terminée après commit des modifications :
  ```console
  On branch main
  nothing to commit, working tree clean
  ```
- En cas de difficultés, il est possible d'abandonner une fusion pour la recommencer ultérieurement ou avec d'autres branches :
  ```bash
  git merge --abort
  ```

### Linéariser un historique

Pour des raisons de lisibilité, on peut vouloir rendre aussi linéaire que possible l'historique d'une branche, en particulier de la branche principale.

Git propose des approches permettant de récupérer tout ou partie des modifications d'une autre branche tout en conservant un historique clair.

#### Récupérer un commit : le cherry pick

Git permet de récupérer dans une branche les modifications apportées par un commit réalisé dans une autre branche avec la commande `git cherry-pick` :
  ```bash
  git cherry-pick <identifiant_commit>
  ```
  - En cas de conflit, la même mécanique de résolution des conflits que pour la fusion de branches sera déclenchée 


{{< mermaid align="left" >}}
    gitGraph
      commit
      commit
      branch feature
      commit id: "2-7ed128b" tag: "feature"
      checkout main
      commit
      cherry-pick id: "2-7ed128b"
      commit
      commit tag: "main, HEAD"
{{< /mermaid >}}

- Le commit `2-7ed128b`, initialement présent dans la branche `feature` a été intégré sans fusion à l'historique de la branche `main`.

#### Réécrire une branche dans une autre : le rebase

Le rebase est une autre façon de fusionner deux branches. Au lieu d'écrire un commit de merge, le rebase consiste à intégrer tous les commits de la branche source dans la branche cible.

Une fois positionné dans la branche cible, la commande `git rebase` permet d'effectuer cette opération :
  ```bash
  git rebase <branche_source>
  ```

Les commits de la branche source seront réécrits dans la branche cible dans le même ordre, immédiatement après l'ancêtre commun.

Les conflits devront être résolus après chaque commit, pour permettre à l'opération de continuer :
  - Les fichiers en conflit doivent être ajoutés à l'index avec `git add`
  - Puis, il faut demander à Git de continuer le rebase avec la commande :
    ```bash
    git rebase --continue
    ```

##### Comparaison entre merge et rebase

- Exemple d'historique après un `git merge` :
  {{< mermaid align="left" >}}
      gitGraph
        commit id: "0-71af11d"
        commit id: "1-8a4f40a"
        branch feature
        commit id: "2-9358c74"
        commit id: "3-8151b64"
        checkout main
        commit id: "4-09aa3e3"
        checkout feature
        commit id: "5-af29107" tag: "feature"
        checkout main
        merge feature id: "6-1a59d24"
        commit id: "7-46ccbcb" tag: "main, HEAD"
  {{< /mermaid >}}

  - Le même historique après un `git rebase`:
  {{< mermaid align="left" >}}
      gitGraph
        commit id: "0-71af11d"
        commit id: "1-8a4f40a"
        commit id: "2-9358c74"
        commit id: "3-8151b64"
        commit id: "5-af29107"
        commit id: "4-09aa3e3"
        commit id: "6-1a59d24"
        commit id: "7-46ccbcb" tag: "main, HEAD"
  {{< /mermaid >}}

#### Simplifier l'historique : le squash

Le `squash` permet à Git de rassembler plusieurs commits en un seul au moment d'une fusion, ce qui est une autre façon de linéariser un historique tout en le simplifiant.

La manière la plus simple d'y parvenir est d'ajouter l'option `--squash` à `git merge`: 
  ```bash
  git merge --squash <branche_source>
  ```
  - Cette opération écrit dans l'index la combinaison de tous les commits de la branche source.
  - Il faut ensuite effectuer un commit classique pour terminer la fusion.

### Supprimer une branche

L'option `-d` de `git branch` permet de supprimer une branche :
  ```bash
  git branch -d <branche_a_supprimer>
  ```

La suppression ne doit être effectuée que si la branche est devenue inutile :
  - Parce qu'elle a été fusionnées dans une autre
  - Parce que ses modifications ont été abandonnées (l'option devient alors `-D` par sécurité)

Une fois la branche supprimée, ses commits non fusionnés sont définitivement perdus