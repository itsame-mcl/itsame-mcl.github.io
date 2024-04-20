---
title: "Premiers pas"
description: "Installation et configuration de Git"
date: 2023-04-16T19:00:00+01:00
tags: ["Git"]
categories: ["Formation"]
mermaid: true
menu:
  sidebar:
    name: Premiers pas
    identifier: first-steps
    parent: git
    weight: 20
---

## Installation de Git

### Linux

Git est généralement installé directement dans la plupart des distributions Linux.
Sinon, il est installable dans un terminal au travers du gestionnaire de paquets de la distribution :
  - Debian : `sudo apt install git-all`
  - Fedora : `sudo dnf install git-all`

### macOS

Sur macOS Mavericks (10.9) ou ultérieur, Git est fourni au travers des Xcode Command Line Tools. 
Il suffit d'essayer de lancer Git dans un terminal via une commande comme `git --version` pour que macOS propose de l'installer avec d'autres outils de développement. 
Sinon, il est possible d'utiliser [Homebrew](https://brew.sh/) via `brew install git` ou de [télécharger l'installateur](https://git-scm.com/download/mac).

### Windows

Sur Windows, l'installation de Git est possible grâce au projet [Git for Windows](https://gitforwindows.org/) qui fournit Git avec un émulateur de ligne de commande Bash.
Une façon simple de l'installer de manière automatisée est d'utiliser [Scoop](https://scoop.sh/) pour installer Git avec la commande `scoop install git`.

Sinon, il est possible de [télécharger l'installateur via le site officiel](https://git-scm.com/download/win) ou avec WinGet.
Certains écrans demandent une attention particulière :

#### Choix de l'éditeur de texte par défaut

{{< img src="/images/posts/formations/git/first-steps/text_editor.png" title="Choosing the default editor used by Git" >}}

- Vim est un bon choix pour des utilisateurs habitués à utiliser des programmes en ligne de commande.
- Sinon, il vaut mieux utiliser un éditeur avec une interface graphique comme Notepad++ ou VS Code.

#### Nom de la branche initiale dans les nouveaux dépôts

{{< img src="/images/posts/formations/git/first-steps/branch_name.png" title="Adjusting the name of the initial branch in new repositories" >}}

Il est désormais recommandé pour travailler avec des outils tiers de sélectionner l'option *Override the default branch name for new repositories* et de choisir `main` comme nom par défaut.

#### Inscription de Git dans les variables d'environnement

{{< img src="/images/posts/formations/git/first-steps/path.png" title="Adjusting your PATH environment" >}}

- *Git from the command line and also from 3rd-party software* permet d'utiliser Git avec d'autres logiciels installés sur l'ordinateur, notamment des IDE.
- *Use Git and optional Unix tools from the Command Prompt* donne accès à des commandes Unix dans la ligne de commande Windows.

#### Choix de l'exécutable SSH

{{< img src="/images/posts/formations/git/first-steps/ssh.png" title="Choosing the SSH executable" >}}

Depuis Windows 10, un client SSH est directement intégré à Windows. Il est donc possible de l'utiliser en choisissant *Use external OpenSSH* pour mutualiser les configurations.

#### Choix du magasin de certificats HTTPS

{{< img src="/images/posts/formations/git/first-steps/ca_cert.png" title="Choosing HTTPS transport backend" >}}

L'option *Use the native Windows Secure Channel library* permet de bénéficier des certificats de sécurité déployés dans un cadre professionnel via un domaine Active Directory. 

#### Conversion des fins de ligne

{{< img src="/images/posts/formations/git/first-steps/crlf.png" title="Configuring the line ending conventions" >}}

À configurer en fonction des habitudes de l'équipe :
  - *Checkout Windows-style, commit Unix-style line endings* est recommandé sous Windows pour un projet multi-plateformes.
  - *Checkout as-is, commit Unix-style line endings* peut s'utiliser si toute l'équipe travaille avec des logiciels adaptés au monde Unix.

#### Comportement par défaut du pull

{{< img src="/images/posts/formations/git/first-steps/pull.png" title="Choose the default behavior of git pull" >}}

À configurer en fonction des habitudes de l'équipe. En l'absence de préférence, l'option *Default (fast-forward or merge)* est plus simple à appréhender dans un premier temps. 

## Configuration de Git

### Niveaux de configuration

{{< mermaid align="left" >}}
    flowchart TD
      subgraph system
        subgraph global
          subgraph local
            node[Configuration]
          end
        end
      end
{{< /mermaid >}}

- De manière générale, la configuration se définit à l'échelle de l'utilisateur, donc au niveau `global`.
- Le niveau `local` peut également être utilisé pour des paramètres spécifiques à un projet.

### Configuration minimale

La configuration de Git s'effectue en ligne de commandes (CLI) dans un terminal.
Il faut au minimum configurer un nom d'auteur et une adresse e-mail :
```bash
git config --global user.name "Prénom Nom"
git config --global user.email "utilisateur@domaine.tld"
```
Dans un cadre professionnel, la configuration d'un proxy peut également être nécessaire :
```bash
 git config --global http.proxy "http://proxy.domaine.tld:port"
 git config --global https.proxy "http://proxy.domaine.tld:port"
 git config --global no.proxy "exception1,exception2,localhost"
```

### Consulter la configuration active

La commande `git config` permet également de connaître la valeur actuelle d'un paramètre. 
Il est même possible de consulter toute la configuration actuellement active grâce à la commande suivante :
  ```bash
  git config --list
  ```
L'option `--show-origin` permet d'indiquer en plus si une configuration vient du niveau `system`, `global` ou `local`. 

## Obtenir de l'aide

Git propose une aide intégrée (en anglais) sur son fonctionnement et la syntaxe de ses commandes. Cette aide est accessible via la commande :
  ```bash
  git help <commande>
  ```
En cas d'utilisation de `git help` sans préciser de nom de commande, Git écrira dans le terminal une liste des commandes les plus usuelles.