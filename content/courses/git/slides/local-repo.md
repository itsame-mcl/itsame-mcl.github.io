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

- La commande `git status` permet de consulter l'état d'un dépôt.
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

## États d'un fichier

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

### Index

- Pour demander à Git de suivre un fichier, il faut l'ajouter à l'**index**.
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

### Dépôt

- À partir du moment où un fichier est présent dans au moins un commit, il est alors enregistré dans le dépôt.
- Un commit est composé de l'ensemble des fichiers du dernier commit (HEAD) auxquels sont appliquées les modifications de l'index.
- Pour effectuer un commit, on utilise la commande suivante :
    ```bash
  git commit -m "Message de commit"
    ```

---

- Une fois qu'un commit est réalisé, il devient le nouveau commit de référence (HEAD) à partir duquel Git vérifie si un fichier a été modifié.
- Quand une modification a été incluse dans un commit, elle sort de l'index.

{{% /section %}}