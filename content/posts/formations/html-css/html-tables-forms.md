---
title: "Tableaux et formulaires en HTML 5"
date: 2024-05-14T18:00:00+01:00
tags: ["HTML 5"]
categories: ["Formation"]
menu:
  sidebar:
    name: HTML - Tableaux et formulaires
    identifier: html-tables-forms
    parent: html-css
    weight: 40
---

## Tableaux

En HTML 5, un tableau de données est un élément de type bloc, représenté par une balise `<table>`.
Selon le degré de complexité du tableau, plusieurs autres balises sont à utiliser à l'intérieur de cet élément.

Historiquement, les tableaux étaient également utilisés pour faire de la mise en page, mais cette pratique est très fortement déconseillée depuis, compte tenu des possibilités offertes par CSS.

### Tableau simple

Pour réaliser un tableau simple, chaque ligne du tableau est décrite par un élément `<tr>` (*table row*).
Ces éléments contiennent à leur tour deux types d'éléments : `<th>` (*table head*) pour les cellules d'en-tête, et `<td>` (*table data*) pour les cellules de données.

Pour les éléments `th`, un attribut `scope=` permet de préciser si l'en-tête porte sur la ligne (`row`) ou la colonne (`col`).

Une légende peut être ajoutée au tableau grâce à un élément `<caption>`, en enfant direct de `<table>`.

#### Exemple

```html
<table>
    <caption>Heures de travail nécessaires à la production d’une unité</caption>
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
Ce code donne le tableau ci-dessous :

|    Pays    | Drap | Vin |
|:----------:|:----:|:---:|
| Angleterre | 100  | 120 |
|  Portugal  |  90  | 80  |

*Heures de travail nécessaires à la production d’une unité*

### Tableau avec en-tête et pied de page

À l'instar des blocs sémantiques, il est possible de distinguer 3 zones dans un tableau : l'en-tête, le corps, et le pied de page, grâce aux balises `<thead>`, `<tbody>` et `<tfoot>`.

```html
<table>
    <caption></caption>
    <thad>
        <tr>
            <th></th>
            <th></th>
        </tr>
    </thad>
    <tbody>
        <tr>
            <th></th>
            <td></td>
        </tr>
        <tr>
            <th></th>
            <td></td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th></th>
            <td></td>
        </tr>
    </tfoot>
</table>
```

### Tableau complexe

Un tableau est dit complexe dès lors que des cellules d'en-tête ou de données s'étendent sur plus d'une ligne ou d'une colonne.
Pour étendre une cellule, les propriétés `rowspan` et `colspan` permettent de définir les dimensions d'une cellule.

L'utilisation de tableaux complexes pouvant perturber les outils d'accessibilité numérique, de nouveaux attributs sont à fixer : un identifiant (`id=`) doit être donné à chaque balise `<th>` à la place des attributs `scope`, et une référence à ces identifiants doit être donnée par un attribut `headers=` dans les balises `<td>`.

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
            <th id="semestre-2" headers="ca">2ème semestre</th>
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

## Formulaires

Un formulaire est initialisé en HTML 5 au moyen de la balise de type bloc `<form>`. Elle contient ensuite les différents éléments, appelés contrôles, du formulaire.

### Contrôles de formulaire

La plupart des contrôles de formulaire se déclarent à l'aide d'une balise `<input>`.
L'attribut `name=` permet de préciser le nom du contrôleur, tel qu'il sera utilisé à l'envoi des données, et l'attribut `type=` permet de préciser le type de contrôle. Le tableau ci-dessous donne une liste de valeurs usuelles pour cet argument :

|   Type   | Description                              |
|:--------:|:-----------------------------------------|
|   text   | Champ de texte libre sur une ligne       |
|  number  | Champ de saisie de valeur numérique      |
|  email   | Champ de saisie pour adresse e-mail      |
|   tel    | Champ de saisie pour numéro de téléphone |
| password | Champ de saisie pour mot de passe        |
| checkbox | Case à cocher                            |
|  radio   | Bouton radio                             |
|   date   | Sélecteur de date                        |
|   time   | Sélecteur d'heure                        |
|  color   | Sélecteur de couleur                     |
|   file   | Sélecteur de fichier                     |

Une valeur initiale peut être donnée à ces contrôles avec l'attribut `value=`.

### Boutons

Les boutons se définissent grâce à une balise `<button>`. Cette balise contient un nœud texte qui correspond au libellé du bouton. Elle peut également prendre un attribut `type=`qui a 3 valeurs possibles :
- `submit` : déclenche l'action d'envoi du formulaire *(voir ci-après)*
- `reset` : réinitialise tout le formulaire à ses valeurs par défaut
- `button` : n'a pas d'effet propre. Cette valeur permet par exemple de positionner un bouton qui aura un effet grâce à JavaScript.

### Zones de texte multilignes

Si le formulaire doit contenir une zone de saisie en texte libre sur plusieurs lignes, la balise `<textarea>` permet de placer cet élément.

L'attribut `maxlength=` permet de donner une longueur maximale à ce texte

### Groupes et libellés

Pour regrouper plusieurs éléments de formulaire, il est possible d'utiliser une balise `<fieldset>`. Un bloc `fieldset` peut être légendé au moyen d'une balise `<legend>`.

Tous les autres éléments peuvent être légendés par des balises `<label>`. Elles prennent comme attribut `for=`, qui précise la valeur de l'attribut `id` de l'élément auquel cette légende est associée.

### Envoi des données

Les attributs de la balise `<form>` permettent de contrôler l'envoi des données du formulaire. Cet envoi est effectué par le navigateur au moyen d'une requête HTTP.

L'attribut `action=` donne le chemin de l'URL qui attend de recevoir ces données. S'il s'agit de la page en cours, il est facultatif.

L'attribut `method=` permet de choisir le type de requête HTTP :
- Si sa valeur est `get`, l'envoi se fera par une requête HTTP GET, et les valeurs seront transmises en paramètres d'URL, sous la forme `?name1=valeur&name2=valeur`.
- Si sa valeur est `post`, l'envoi se fera par une requête HTTP POST, et les valeurs seront transmises dans le corps de la requête.

Pour rendre un contrôle obligatoire, il suffit de lui ajouter l'attribut `required`. Au clic sur le bouton d'envoi, le navigateur vérifiera que ces contrôles sont bien remplis, et empêchera l'envoi dans le cas contraire.