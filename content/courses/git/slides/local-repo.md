---
weight: 30
hideCard: true
---
{{% section %}}

# Gérer un dépôt local
Créer un dépôt, écrire des commits, gérer des multiples branches, consulter et manipuler l'historique

---

## Qu'est-ce qu'un dépôt ?

- Un **dépôt** (ou "repository" en anglais) est l'endroit où Git stocke l'historique des versions d'un projet de développement.
- Il existe deux types de dépôts dans Git :
  - Un **dépôt local** est une copie du dépôt sur l'ordinateur local d'un développeur
  - Un **dépôt distant** est un dépôt hébergé sur un serveur distant, accessible via Internet.

---

## Créer un dépôt local

- Pour créer un dépôt local avec Git, il suffit de se positionner en ligne de commandes (via `cd`) dans un dossier à transformer en dépôt et d'utiliser la commande :
  ```bash
  git init
  ```
  - Ceci va créer un sous-dossier .git (caché sous UNIX, pour le voir : `ls -la`) qui sert notamment à stocker l'historique.
    - Il n'est pas utile d'y accéder en utilisation courante.

---

- Il est possible de consulter l'état d'un dépôt grâce à la commande :
  ```bash
  git status
  ```
  - Pour un dépôt nouvellement créé dans un dossier vide, elle doit proposer la sortie suivante :
      ```console
      On branch main
    
      No commits yet
    
      nothing to commit (create/copy files and use "git add" to track)
      ```

---

## Qu'est-ce qu'un commit ?

- Un **commit** représente une version spécifique d'un projet à un moment donné. **C'est l'unité de base de l'historique d'un dépôt.**
  - Il contient une copie des fichiers du projet, ainsi qu'un message décrivant les modifications apportées depuis la version précédente.
- Un commit est identifié par un **hash** (SHA-1) calculé par Git sur la base du hash de l'ensemble des fichiers du projet.
  - On l'abrège souvent à ses premiers caractères (par exemple, `1d0703d3`).

---

## Manipulation des fichiers

- Avec Git, un fichier peut être présent dans 3 zones distinctes :
  - le répertoire de travail
  - l'index
  - le dépôt
- `git status` permet de connaître l'état de chaque fichier

---

### Répertoire de travail

- Le **répertoire de travail** correspond au contenu du dossier sur l'ordinateur du développeur.
  - Par défaut, aucun fichier n'est suivi par Git. Par exemple, après la création d'un fichier `exemple.txt`, la commande `git status` donne la sortie suivante :
    ```console
    On branch main
    
      No commits yet
    
      Untracked files:
      (use "git add <file>..." to include in what will be committed)
      exemple.txt
    
      nothing added to commit but untracked files present (use "git add" to track)
      ```

---

<div class="mermaid">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
    classDiagram
      direction RL
      Index..Répertoire
      Dépôt..Index
      class Répertoire{
        +exemple.txt a4d584
      }
      class Index{
      }
      class Dépôt{
      }
  </pre>
</div>

---

### Index

- Pour demander à Git de commencer à suivre un fichier, il faut l'ajouter à l'**index**.
- L'index est une zone tampon entre le répertoire de travail et le dépôt qui rassemble l'ensemble des modifications prêtes à être ajoutées à un commit.
- Concrètement, on indexe un fichier avec la commande suivante :
    ```bash
    git add <fichier>
    ```
  - On peut utiliser un `.` à la place du nom du fichier pour demander à Git d'indexer tout le répertoire de travail.

---

- Une fois un fichier indexé, il est prêt à être inclus à un commit. La sortie de `git status` reflète cette évolution :
    ```console
    On branch main

    No commits yet
    
    Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
    new file:   exemple.txt
    ```
- Il est possible de désindexer un fichier sans le supprimer avec la commande :
    ```bash
    git rm --cached <fichier>
    ```
    - L'option `-f` peut être utilisée à la place de `--cached` pour supprimer totalement le fichier.

---

- Un fichier indexé devient également suivi par Git, ce qui revient à dire que son hash est recalculé à chaque modification du répertoire de travail.
- S'il est à nouveau modifié alors qu'il est toujours dans l'index, Git détectera cette modification :
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

---

<div class="mermaid">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
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
  </pre>
</div>

---

### Dépôt

- À partir du moment où un fichier est présent dans au moins un commit, il est alors enregistré dans le dépôt.
- Un commit est composé de l'ensemble des fichiers du dernier commit de la branche actuelle (HEAD) auxquels sont appliquées les modifications de l'index.
- Pour effectuer un commit, on utilise la commande suivante :
    ```bash
  git commit -m "Message de commit"
    ```

---

- Une fois qu'un commit est réalisé, il devient le nouveau commit de référence (HEAD) à partir duquel Git vérifie si un fichier a été modifié.
- Quand une modification a été incluse dans un commit, elle sort de l'index, comme en témoigne la sortie de `git status` :
  ```console
  On branch main
  nothing to commit, working tree clean
  ```

---

<div class="mermaid">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
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
  </pre>
</div>

---

#### Messages de commit

- Le message de commit sera lisible par tous les développeurs du projet et sera retranscrit dans l'historique, d'où l'importance qu'il retrace fidèlement le contenu du commit.
  - Il est donc crucial que les modifications apportées par un commit forment un ensemble cohérent.
- En utilisant la syntaxe `git commit -m`, la longueur du message est limitée à 49 caractères.
  - Il vaut souvent mieux séparer un gros commit difficile à résumer en plusieurs petits commits.
---

#### Modifier le dernier commit

- Il est possible de corriger un oubli sur le dernier commit ou de modifier son message avec l'option `--amend` :
  ```bash
  git commit --amend -m "Nouveau message de commit"
  ```
  - Pour ne pas modifier le message de commit, il faut ajouter l'option `--no-edit` à la place de `-m`.
- Les modifications actuellement contenues dans l'index seront alors fusionnées avec celles du dernier commit, ce qui va créer un nouveau commit qui remplace l'ancien.

---

### Autres manipulations sur les fichiers

- Git propose des commandes permettant de retranscrire d'autres manipulations usuelles sur les fichiers :
  - Déplacer ou renommer un fichier :
    ```bash
    git mv <ancien_nom> <nouveau_nom>
    ```
  - Supprimer un fichier :
    ```bash
    git rm <fichier_a_supprimer>
    ```
- Ces modifications seront ajoutées à l'index et devront être commitées pour être retranscrites dans le dépôt.

---

### Ignorer des fichiers

- Il est également possible de demander à Git d'ignorer de manière permanente des fichiers.
  - Pour cela, il faut créer à la racine du dépôt un fichier nommé `.gitignore` (sans extension), qui continent la liste des fichiers et dossiers à ignorer.
  - Le fichier `.gitignore` doit être commité pour être pris en compte.
- Il existe des outils en ligne comme [gitignore.io](https://www.toptal.com/developers/gitignore) pour avoir des listes usuelles de fichiers à ignorer selon les types de projets.

---

## Consulter l'historique d'un dépôt

<div class="mermaid">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
    gitGraph
      commit id: "3b1d805"
      commit id: "6a2b687"
      commit id: "49eb5d0"
      commit id: "8f7308f"
      commit id: "30d524c" tag: "HEAD"
  </pre>
</div>

---

- La commande `git log` permet d'obtenir l'historique complet des commits d'un dépôt, dans l'ordre chronologique inversé :
  ```bash
  git log
  ```
  ```console
  commit 30d524c6603ed1982bdf82eb54d7215a00b22328 (HEAD -> main)
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Fri Apr 14 12:31:00 2023 +0200
  
      Suppression du fichier exemple.txt devenu inutile
  
  commit 8f7308fc1099a44fb25af05c3ee7c6a7ca17f111
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Fri Apr 14 12:30:31 2023 +0200
  
      Correction d'une coquille dans le poème
  
  commit 49eb5d06716e1f0668681b417a884b3d808bacda
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Fri Apr 14 12:30:02 2023 +0200
  
      Le poème est plutôt un haiku
  
  commit 6a2b687e994b4c8341adc6542c313cb860dad452
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Fri Apr 14 12:29:24 2023 +0200
  
      Ajout d'un poème sur l'informatique
  
  commit 3b1d805510f43af8e7b9da97d0bf44dca127a9d1
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Thu Apr 13 16:56:41 2023 +0200
  
      Exemple de commit avec un fichier unique
  ```

---

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
  
---

- L'option `--stat` permet de connaître le nombre de modifications effectuées sur chaque fichier :
  ```bash
  git log --stat
  ```
  ```console
  commit 30d524c6603ed1982bdf82eb54d7215a00b22328 (HEAD -> main)
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Fri Apr 14 12:31:00 2023 +0200
  
      Suppression du fichier exemple.txt devenu inutile
  
  exemple.txt | 0
  1 file changed, 0 insertions(+), 0 deletions(-)
  
  commit 8f7308fc1099a44fb25af05c3ee7c6a7ca17f111
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Fri Apr 14 12:30:31 2023 +0200
  
      Correction d'une coquille dans le poème
  
  haiku.txt | 2 +-
  1 file changed, 1 insertion(+), 1 deletion(-)
  
  commit 49eb5d06716e1f0668681b417a884b3d808bacda
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Fri Apr 14 12:30:02 2023 +0200
  
      Le poème est plutôt un haiku
  
  poeme.txt => haiku.txt | 0
  1 file changed, 0 insertions(+), 0 deletions(-)
  
  commit 6a2b687e994b4c8341adc6542c313cb860dad452
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Fri Apr 14 12:29:24 2023 +0200
  
      Ajout d'un poème sur l'informatique
  
  poeme.txt | 3 +++
  1 file changed, 3 insertions(+)
  
  commit 3b1d805510f43af8e7b9da97d0bf44dca127a9d1
  Author: Maxence Lagalle <contact@maxence.lagalle.fr>
  Date:   Thu Apr 13 16:56:41 2023 +0200
  
      Exemple de commit avec un fichier unique
  
  exemple.txt | 0
  1 file changed, 0 insertions(+), 0 deletions(-)
  ```
- Il est possible de combiner les options `--oneline` et `--stat`.

---

### Filtrer l'historique

- `git log` supporte de nombreuses options permettant de filtrer l'historique selon plusieurs critères :
  - `-n <nombre>` : n derniers commits
  - `--before="AAAA-MM-JJ HH:mm"` : commits plus anciens qu'une date
  - `--after="AAAA-MM-JJ HH:mm"` : commits plus récents qu'une date
  - `--author="Nom"` : commits signés par un auteur
  - `-- <fichier>` : commits affectant un fichier

---

### Rechercher à l'intérieur des commits

- L'option `-S` permet de rechercher une chaîne de caractères et d'afficher la liste des commits contenant cette chaîne à l'intérieur des fichiers qu'ils modifient :
  ```bash
  git log -S "Chaîne à rechercher"
  ```
- Il existe également l'option `-G` pour faire une recherche par expression régulière (regex).

---

### Consulter l'historique détaillé d'un fichier

- La commande `git blame` permet de connaître l'historique détaillé d'un fichier en précisant de quel commit viennent chacune de ses lignes dans leur rédaction actuelle :
  ```bash
  git blame <fichier>
  ```
  - La sortie de cette commande affiche chaque ligne du fichier dans le terminal, précédé de l'identifiant du commit ayant introduit ou modifié cette ligne, du nom de l'auteur et de la date de ce commit.

---

- Exemple :
  ```bash
  git blame haiku.txt
  ```
  ```console
  6a2b687e poeme.txt (Maxence Lagalle 2023-04-14 12:29:24 +0200 1) Un clic malencontreux
  8f7308fc haiku.txt (Maxence Lagalle 2023-04-14 12:30:31 +0200 2) Fichier important supprimé
  6a2b687e poeme.txt (Maxence Lagalle 2023-04-14 12:29:24 +0200 3) Sauvegarde ? Jamais fait.
  ```

---

### Comparer deux commits

- Grâce à `git diff`, il est possible d'effectuer des comparaisons entre deux états d'un fichier.
  - Si la commande est utilisée sans paramètres, la comparaison s'effectue entre le répertoire de travail et l'index.
  - Il est possible de donner en paramètres un identifiant de commit pour comparer ce commit au répertoire de travail, ou deux identifiants de commit pour les comparer.

---

- Par exemple, il est possible de comparer le commit `49eb5d0` à l'état actuel du dépôt, c'est-à-dire au commit `HEAD`:
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

---

### Rechercher un commit défectueux

- L'outil `git bisect` permet de retrouver un commit défectueux (par exemple, ayant introduit un bug) par recherche dichotomique.
- Il faut tout d'abord l'initialiser en lui précisant notamment l'identifiant d'un "mauvais commit" (ayant le problème) et d'un "bon commit" (n'ayant pas le problème) :
  ```bash
  git bisect start
  git bisect bad <mauvais commit, vide pour commit actuel>
  git bisect good <bon commit>
  ```

---

- Git va alors sélectionner un commit situé entre ces deux bornes et remettre le répertoire de travail à l'état de ce commit :
  ```console
  Bisecting: X revisions left to test after this (roughly Y steps)
  ```
- Après avoir vérifié manuellement si le bug est toujours présent, il faut indiquer à Git le résultat de cette vérification avec l'une de ces commandes :
  - `git bisect good` si le bug est absent
  - `git bisect bad` si le bug est présent

---

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

---

### Revenir à un état antérieur de l'historique

- Git permet facilement de revenir à un état antérieur, par exemple pour repartir d'une version précédente ou annuler des modifications expérimentales.
- Pour cela, il faut utiliser la commande :
  ```bash
  git reset <commit>
  ```
  - Le répertoire de travail est alors remis à l'état du commit ciblé et les modifications réalisées depuis sont remises dans l'index.
  - L'option `--hard` permet de réinitialiser **définitivement** le répertoire de travail et l'index et supprime les commits devenus obsolètes.
- 

{{% /section %}}