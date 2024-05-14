---
title: "Tableaux et formulaires en HTML 5"
date: 2024-05-14T19:00:00+01:00
tags: ["HTML 5"]
categories: ["Formation"]
menu:
  sidebar:
    name: HTML - Principales balises
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

{{< split 6 6 >}}

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

---

|Pays|Drap|Vin|
|:--:|:--:|:-:|
|Angleterre|100|120|
|Portugal|90|80|

*Heures de travail nécessaires à la production d’une unité*

{{< /split >}}

### Tableau avec en-tête et pied de page

A l'instar des blocs sémantiques, il est possible de distinguer 3 zones dans un tableau : l'en-tête, le corps, et le pied de page, grâce aux balises `<thead>`, `<tbody>` et `<tfoot>`.

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

un tableau est dit complexe dès lors que des cellules s'en-tête ou de données s'étendent sur plus d'une ligne ou d'une colonne.
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