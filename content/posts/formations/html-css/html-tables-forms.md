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

### Tableau complexe

## Formulaires