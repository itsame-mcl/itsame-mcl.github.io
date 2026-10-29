---
title: "Tableaux et formulaires en HTML 5"
description: "Tableaux de données et formulaires accessibles en HTML 5."
date: 2024-05-14T18:00:00+01:00
lastmod: 2026-07-21T12:00:00+02:00
tags: ["HTML"]
categories: ["Formation"]
menu:
  sidebar:
    name: "HTML - Tableaux et formulaires"
    identifier: html-tables-forms
    parent: html-css
    weight: 40
---

Un tableau HTML sert à présenter des **données tabulaires** : des valeurs qui se lisent en croisant lignes et colonnes. Historiquement, les tableaux ont aussi été détournés pour faire de la mise en page ; cette pratique est aujourd'hui à proscrire absolument — c'est le rôle de CSS (Flexbox et Grid, chapitre 8).

## 4.1. Tableau simple
Un tableau est délimité par `<table>`. Chaque ligne est un `<tr>` (*table row*), qui contient des cellules de deux types : `<th>` (*table header*) pour les en-têtes et `<td>` (*table data*) pour les données. Une légende, fortement recommandée, s'ajoute avec `<caption>` en premier enfant de `<table>`.

Sur chaque `<th>`, l'attribut `scope=` précise la portée de l'en-tête : `col` (la colonne entière) ou `row` (la ligne entière).

```html
<table>
    <caption>Heures de travail nécessaires à la production d'une unité</caption>
    <tr>
        <th scope="col">Pays</th>
        <th scope="col">Drap</th>
        <th scope="col">Vin</th>
    </tr>
    <tr>
        <th scope="row">Angleterre</th>
        <td>100</td>
        <td>120</td>
    </tr>
    <tr>
        <th scope="row">Portugal</th>
        <td>90</td>
        <td>80</td>
    </tr>
</table>
```

{{< alert type="a11y" >}}
`<caption>` et `scope=` ne sont pas décoratifs : ce sont eux qui permettent à un lecteur d'écran d'annoncer « Pays : Portugal, Vin : 80 » plutôt qu'une suite de nombres sans contexte. Un tableau de données sans en-têtes correctement reliés est un des manquements les plus fréquents aux critères RGAA.
{{< /alert >}}

## 4.2. En-tête, corps et pied de tableau
Comme la page elle-même, un tableau peut être structuré en trois zones : `<thead>` (lignes d'en-tête), `<tbody>` (corps) et `<tfoot>` (ligne de synthèse : totaux, moyennes…). Cette structure clarifie le code et permet, en CSS, de styler chaque zone séparément.

```html
<table>
    <caption>Fréquentation mensuelle</caption>
    <thead>
        <tr>
            <th scope="col">Mois</th>
            <th scope="col">Visiteurs</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">Janvier</th>
            <td>1 240</td>
        </tr>
        <tr>
            <th scope="row">Février</th>
            <td>1 105</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th scope="row">Total</th>
            <td>2 345</td>
        </tr>
    </tfoot>
</table>
```

## 4.3. Tableaux complexes
Un tableau est dit **complexe** dès qu'une cellule s'étend sur plusieurs lignes ou colonnes, au moyen des attributs `rowspan=` et `colspan=`.

Ces fusions perturbent la lecture automatique : le simple `scope=` ne suffit plus à relier chaque donnée à ses en-têtes. La solution : donner un identifiant (`id=`) à chaque `<th>`, puis lister explicitement dans chaque `<td>` les identifiants de ses en-têtes via l'attribut `headers=`.

```html
<table>
    <caption>Chiffre d'affaires semestriel</caption>
    <thead>
        <tr>
            <th id="entreprise" rowspan="2">Entreprise</th>
            <th id="ca" colspan="2">Chiffre d'affaires</th>
        </tr>
        <tr>
            <th id="semestre-1" headers="ca">1er semestre</th>
            <th id="semestre-2" headers="ca">2e semestre</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th id="societe-1" headers="entreprise">Société 1</th>
            <td headers="societe-1 semestre-1">10</td>
            <td headers="societe-1 semestre-2">20</td>
        </tr>
        <tr>
            <th id="societe-2" headers="entreprise">Société 2</th>
            <td headers="societe-2 semestre-1">30</td>
            <td headers="societe-2 semestre-2">40</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th id="total" headers="entreprise">Total</th>
            <td headers="total semestre-1">40</td>
            <td headers="total semestre-2">60</td>
        </tr>
    </tfoot>
</table>
```


Un formulaire permet à l'utilisateur de saisir des données et de les envoyer au serveur. Il est délimité par la balise de type bloc `<form>` et contient des **contrôles** : champs de saisie, listes, cases à cocher, boutons…

## 5.1. Le contrôle universel : &lt;input&gt;
La plupart des contrôles se déclarent avec la balise vide `<input>`. Deux attributs sont essentiels : `name=`, le nom sous lequel la donnée sera transmise au serveur, et `type=`, qui détermine la nature du contrôle :

| **Type** | **Description** |
|---|---|
| `text` | Champ de texte libre sur une ligne |
| `number` | Valeur numérique (avec attributs `min=`, `max=`, `step=`) |
| `email` | Adresse électronique (validation automatique du format) |
| `tel` | Numéro de téléphone (affiche le clavier numérique sur mobile) |
| `url` | Adresse web (validation automatique du format) |
| `password` | Mot de passe (saisie masquée) |
| `checkbox` | Case à cocher (choix multiples) |
| `radio` | Bouton radio (choix unique parmi les `input` partageant le même `name=`) |
| `date` / `time` | Sélecteur de date / d'heure |
| `color` | Sélecteur de couleur |
| `file` | Sélecteur de fichier à téléverser |
| `hidden` | Valeur transmise sans être affichée |

L'attribut `value=` fixe une valeur initiale. Pour les cases à cocher et boutons radio, l'attribut `checked` présélectionne le contrôle.

{{< alert type="note" >}}
Utiliser le bon `type=` n'est pas cosmétique : le navigateur adapte le clavier virtuel sur mobile (clavier numérique pour `tel`, arobase pour `email`) et effectue une première validation gratuite du format saisi.
{{< /alert >}}

## 5.2. Listes déroulantes : &lt;select&gt;
Une liste déroulante se construit avec `<select>` (qui porte le `name=`) et des `<option>` :

```html
<label for="visite">Visite guidée souhaitée</label>
<select name="visite" id="visite">
    <option value="">— Choisir une visite —</option>
    <option value="vieux-port">Le vieux port</option>
    <option value="citadelle" selected>La citadelle</option>
</select>
```

L'attribut `selected` présélectionne une option ; `<optgroup label="…">` permet de regrouper des options sous un intitulé commun.

## 5.3. Zones de texte multilignes : &lt;textarea&gt;
Pour une saisie libre sur plusieurs lignes, `<textarea>` s'utilise avec une balise ouvrante et une balise fermante. `rows=` et `cols=` suggèrent ses dimensions initiales, `maxlength=` limite la longueur du texte.

## 5.4. Boutons
Un bouton se définit avec `<button>`, dont le nœud texte constitue le libellé. Son attribut `type=` prend trois valeurs :

- `submit` (valeur par défaut) : déclenche l'envoi du formulaire ;
- `reset` : réinitialise tous les contrôles à leur valeur initiale (à utiliser avec prudence : un clic malheureux efface toute la saisie) ;
- `button` : sans effet propre, pour un comportement défini en JavaScript.

## 5.5. Libellés et regroupements : la clé de l'accessibilité
**Chaque contrôle doit avoir un libellé**, déclaré avec `<label>`. Deux écritures sont possibles :

```html
<!-- Liaison explicite par for/id (recommandée) -->
<label for="courriel">Adresse électronique</label>
<input type="email" name="courriel" id="courriel">
 
<!-- Liaison par imbrication -->
<label>
    Adresse électronique
    <input type="email" name="courriel">
</label>
```

Les contrôles apparentés — typiquement une série de boutons radio — se regroupent dans un `<fieldset>`, dont le premier enfant `<legend>` donne l'intitulé du groupe :

```html
<fieldset>
    <legend>Formule d'abonnement</legend>
    <label><input type="radio" name="formule" value="simple" checked> Simple</label>
    <label><input type="radio" name="formule" value="famille"> Famille</label>
</fieldset>
```

{{< alert type="a11y" >}}
Le `<label>` est le critère d'accessibilité n° 1 des formulaires : sans lui, un lecteur d'écran annonce « édition, vide » sans dire ce qu'il faut saisir. Il agrandit aussi la zone cliquable (cliquer sur le libellé active le champ). L'attribut `placeholder=` (texte grisé dans le champ) **ne remplace jamais un label** : il disparaît dès la saisie et son contraste est insuffisant. Enfin, l'attribut `autocomplete=` (`name`, `email`, `tel`…) permet aux navigateurs et aides techniques de pré-remplir les champs — c'est un critère WCAG 2.2.
{{< /alert >}}

## 5.6. Validation et envoi des données
L'attribut `required`, ajouté à un contrôle, le rend obligatoire : le navigateur bloque l'envoi et signale le champ s'il est vide. Les attributs `min=`, `max=`, `maxlength=` et `pattern=` (expression régulière) complètent cette validation native, qui reste une aide à la saisie : le serveur doit toujours revalider les données.

L'envoi est piloté par deux attributs de `<form>` :

- `action=` : URL destinataire des données (facultatif si c'est la page courante) ;
- `method=` : `get` transmet les valeurs dans l'URL (`?nom=valeur&autre=valeur`), adapté aux recherches et filtres ; `post` les transmet dans le corps de la requête HTTP, obligatoire dès que les données sont sensibles ou modifient un état côté serveur.

```html
<form action="/inscription" method="post">
    <label for="nom">Nom</label>
    <input type="text" name="nom" id="nom" autocomplete="family-name" required>
 
    <label for="courriel">Adresse électronique</label>
    <input type="email" name="courriel" id="courriel" autocomplete="email" required>
 
    <button type="submit">S'inscrire</button>
</form>
```

{{< alert type="practice" >}}
Les exercices 4 à 7 du [TP HTML]({{< relref "tp-html" >}}) portent sur les tableaux simples et complexes, le formulaire de contact et un premier audit d'accessibilité.
{{< /alert >}}
