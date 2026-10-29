---
title: "Travaux pratiques HTML 5 : le mini-site d'une ville"
description: "Sept exercices corrigés pour pratiquer HTML 5 : structure sémantique, contenus, tableaux, formulaire et audit d'accessibilité."
date: 2026-10-28T12:00:00+01:00
lastmod: 2026-10-28T12:00:00+01:00
tags: ["HTML", "CSS", "Accessibilité", "Exercices"]
categories: ["Formation"]
menu:
  sidebar:
    name: "TP - HTML (exercices 1 à 7)"
    identifier: tp-html
    parent: html-css
    weight: 90
---

Cette page rassemble les exercices du chapitre HTML. Vous allez construire pas à pas une page d'accueil complète, en appliquant chaque notion du cours. Chaque exercice est suivi de son corrigé, à ouvrir seulement après avoir essayé.

## Mode d'emploi pour apprendre seul

Ces exercices ont été conçus pour un stage de deux journées, mais ils se pratiquent très bien en autonomie, à raison d'environ une journée de travail pour chacune des deux parties (HTML puis CSS).

- **Alternez lecture et pratique.** Lisez un chapitre du cours, puis faites aussitôt l'exercice correspondant : chaque chapitre indique en fin de page les exercices à réaliser.
- **Chaque exercice s'appuie sur le précédent.** Si vous êtes bloqué, repartez du corrigé de l'exercice précédent plutôt que de rester coincé : ne passez pas des heures sur un seul point.
- **Les bonus sont facultatifs.** Ils servent à aller plus loin quand on va vite.
- **L'esthétique se peaufine plus tard.** Ne passez pas vingt minutes à choisir vos couleurs ou vos photos : l'objectif est la technique.
- **L'accessibilité est un fil rouge.** Les encadrés « Accessibilité » signalent les critères à vérifier à chaque étape, et les deux audits (exercices 7 et 14) servent de bilan.

### Matériel

- Un éditeur de code : Visual Studio Code, avec l'extension Live Server qui recharge la page à chaque enregistrement, ou tout éditeur de texte.
- Un navigateur récent avec ses outils de développement (touche F12).
- Le [validateur du W3C](https://validator.w3.org/), le [vérificateur de contraste de WebAIM](https://webaim.org/resources/contrastchecker/) et [MDN Web Docs](https://developer.mozilla.org/fr/) à garder ouverts.

## Le fil rouge : promouvoir la ville de votre choix

Dans la première partie (HTML), vous bâtirez la **structure et les contenus** en HTML : pages, textes, images, tableaux de statistiques et d'horaires, formulaire de contact. Dans la seconde (CSS), vous mettrez le site **en forme** avec CSS : charte graphique, navigation, galerie, gabarit de page, adaptation mobile — avec l'accessibilité en fil conducteur du début à la fin.

Les corrigés, placés sous chaque exercice, s'appuient sur une ville fictive, **Bellerive-sur-Mer** (petit port de caractère, sa citadelle, son festival des lanternes…). Ils sont directement transposables à votre ville : seuls les contenus changent, jamais la technique.

### Organisation des fichiers
Créez un dossier de travail `mon-site/` contenant à la racine vos fichiers `index.html` puis `style.css`, et un sous-dossier `images/`. Pour les images, utilisez vos propres photos, ou des images libres de droits (unsplash.com, pexels.com), en veillant à des fichiers raisonnablement légers (moins de 300 Ko).

## Exercice 1 — Le squelette de la page d'accueil

**Durée indicative : 25 min.** Objectifs : créer un document HTML 5 valide ; renseigner les métadonnées essentielles.

1. Créez le dossier `mon-site/` et, à l'intérieur, un fichier `index.html`.
2. Écrivez le squelette minimal : doctype, élément racine avec la langue, `head` et `body`.
3. Dans le `head`, renseignez dans l'ordre : l'encodage UTF-8, la balise meta `viewport`, un `<title>` de la forme « Visiter [Votre ville] — Accueil », et une meta `description` d'une ou deux phrases donnant envie de visiter la ville.
4. Dans le `body`, placez provisoirement un paragraphe « Bienvenue à [Votre ville] ! » et ouvrez le fichier dans votre navigateur (double-clic, ou clic droit → « Open with Live Server » sous VS Code).
5. Validez votre page sur validator.w3.org (onglet « Validate by File Upload ») et corrigez les éventuelles erreurs.

{{< alert type="a11y" >}}
Vérifiez que l'attribut `lang="fr"` figure bien sur la balise `<html>` : c'est le premier critère d'accessibilité de toute page.
{{< /alert >}}

{{< alert type="pitfall" >}}
Fichier enregistré avec l'extension `.txt` (certains systèmes masquent les extensions) ; page ouverte depuis l'explorateur de fichiers plutôt que via Live Server, ce qui oblige à recharger la page à la main après chaque modification.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 1" >}}
```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Visiter Bellerive-sur-Mer — Accueil</title>
        <meta name="description" content="Port de caractère entre mer et vignes :
              découvrez la citadelle, le vieux port et le festival des lanternes.">
    </head>
    <body>
        <p>Bienvenue à Bellerive-sur-Mer !</p>
    </body>
</html>
```

> **À noter.** Points de vigilance récurrents : le `lang="fr"` oublié ; la meta `charset` placée après le `<title>` (elle doit le précéder) ; un `<title>` vide ou générique.
{{< /corrige >}}

## Exercice 2 — La structure sémantique

**Durée indicative : 35 min.** Objectifs : découper la page en zones sémantiques ; préparer la navigation du site.

1. Remplacez le contenu du `body` par la structure suivante : un `<header>` de page, un `<main>`, et un `<footer>` de page.
2. Dans le `<header>` : le nom du site (qui deviendra le `<h1>` à l'exercice 3) et un bloc `<nav>` contenant une liste non ordonnée de 4 liens : Accueil (`index.html`), Découvrir (`#decouvrir`), Infos pratiques (`#infos`), Contact (`#contact`). Les trois derniers sont pour l'instant des ancres internes à la page d'accueil.
3. Dans le `<main>` : trois `<section>` portant les identifiants `decouvrir`, `infos` et `contact` — les cibles des ancres du menu.
4. Ajoutez, entre les sections « découvrir » et « infos », un `<aside>` qui accueillera plus tard un encadré « Le saviez-vous ? ».
5. Dans le `<footer>` : un paragraphe de type « © 2026 Office de tourisme de [Votre ville] » et un lien de retour en haut de page.
6. Testez chaque lien du menu : la page doit défiler jusqu'à la bonne section.

{{< alert type="note" >}}
La page paraît vide et sans style : c'est normal. La première partie porte sur la structure et le contenu ; la seconde sur l'apparence. Résistez à la tentation d'ajouter le moindre attribut de mise en forme dans le HTML.
{{< /alert >}}

{{< alert type="pitfall" >}}
Assurez-vous de bien comprendre le couple `href="#id"` / `id="…"` avant de poursuivre : il sert à toutes les ancres, et la suite du TP s'appuie dessus.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 2" >}}
```html
<body>
    <header>
        Visiter Bellerive-sur-Mer
        <nav>
            <ul>
                <li><a href="index.html">Accueil</a></li>
                <li><a href="#decouvrir">Découvrir</a></li>
                <li><a href="#infos">Infos pratiques</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="decouvrir"></section>
        <aside></aside>
        <section id="infos"></section>
        <section id="contact"></section>
    </main>
    <footer>
        <p>© 2026 Office de tourisme de Bellerive-sur-Mer —
           <a href="#top">Retour en haut de page</a></p>
    </footer>
</body>
```

Le lien « Retour en haut » suppose une ancre `id="top"` posée sur le `<header>` (ou l'usage du fragment vide `href="#"`, moins explicite). L'`<aside>` est ici dans le `<main>` ; il en sortira à l'exercice 12 pour devenir une zone du gabarit.
{{< /corrige >}}

## Exercice 3 — Les contenus : textes, listes, images

**Durée indicative : 35 min.** Objectifs : hiérarchiser les titres ; utiliser les listes et emphases à bon escient ; insérer des images accessibles.

1. Donnez un `<h1>` à la page (« Visiter [Votre ville] », dans le `<header>`), puis un `<h2>` à chaque section (« Découvrir la ville », « Infos pratiques », « Contact »). Vérifiez la hiérarchie : un seul `h1`, pas de saut de niveau.
2. Section « Découvrir » : rédigez un paragraphe d'introduction contenant au moins une emphase `<em>` et une emphase forte `<strong>`, puis une liste **ordonnée** « Top 5 des incontournables » (vos 5 lieux préférés).
3. Toujours dans « Découvrir » : insérez une photo emblématique de la ville dans une balise `<figure>` avec sa `<figcaption>`. L'image doit avoir un `alt` descriptif ainsi que ses attributs `width` et `height`.
4. Dans l'`<aside>` : un `<h2>` « Le saviez-vous ? » et une anecdote sur votre ville, avec une liste de **descriptions** (`<dl>`) définissant 2 ou 3 termes locaux (nom des habitants, spécialité culinaire, monument…).
5. Section « Infos pratiques » : une liste **non ordonnée** de conseils pratiques (venir en train, se garer, meilleure saison…), dont au moins un élément contient un lien vers un site externe (SNCF, site officiel de la ville…) avec un intitulé explicite.
6. Ajoutez une image purement décorative où bon vous semble (séparateur, motif…) : quel `alt` doit-elle recevoir ?

{{< alert type="a11y" >}}
Relisez chaque intitulé de lien seul, sorti de son contexte : dit-il clairement où il mène ? Bannissez « cliquez ici » et « en savoir plus ».
{{< /alert >}}

**Bonus** : ajoutez une balise `<time>` avec son attribut `datetime` pour annoncer la date du prochain événement de la ville.

{{< alert type="pitfall" >}}
Le chemin d'une image est relatif au fichier HTML (`images/photo.jpg`) : une faute de dossier, de nom ou de casse donne une image cassée. Retenez aussi qu'une image décorative reçoit un `alt` **vide mais présent** (`alt=""`), pas un `alt` absent.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 3" >}}
Section « Découvrir » (extraits significatifs) :

```html
<section id="decouvrir">
    <h2>Découvrir la ville</h2>
    <p>Blottie entre la falaise et le vignoble, <strong>Bellerive-sur-Mer</strong>
       cultive un art de vivre <em>résolument</em> maritime. Du haut de la
       citadelle, le regard porte jusqu'aux îles Sanguinaires.</p>
 
    <h3>Le top 5 des incontournables</h3>
    <ol>
        <li>La citadelle Vauban et son chemin de ronde</li>
        <li>Le vieux port et ses façades colorées</li>
        <li>Le musée maritime</li>
        <li>Le sentier des douaniers</li>
        <li>Le marché aux poissons du samedi</li>
    </ol>
 
    <figure>
        <img src="images/vieux-port.jpg"
             alt="Le vieux port au couchant, barques amarrées devant les façades colorées"
             width="800" height="450">
        <figcaption>Le vieux port, cœur battant de la ville.</figcaption>
    </figure>
</section>
 
<aside>
    <h2>Le saviez-vous ?</h2>
    <p>La citadelle n'a jamais été prise : ses assiégeants de 1653 ont préféré
       négocier… autour d'une bourriche d'huîtres.</p>
    <dl>
        <dt>Bellerivains</dt>
        <dd>Nom des habitants de Bellerive-sur-Mer.</dd>
        <dt>La lanterne</dt>
        <dd>Brioche locale au miel, tressée comme un cordage.</dd>
    </dl>
</aside>
```

L'image décorative reçoit un `alt` **vide** : `<img src="images/frise-vagues.png" alt="" width="1200" height="40">`. Le lien externe est explicite : `<a href="https://www.sncf-connect.com">Préparer son trajet en train sur SNCF Connect</a>`. Bonus : `<time datetime="2026-08-14">14 août 2026</time>`.
{{< /corrige >}}

## Exercice 4 — Tableau simple : les horaires

**Durée indicative : 15 min.** Objectifs : construire un tableau de données simple et accessible.

1. Dans la section « Infos pratiques », créez un tableau des horaires d'ouverture de l'office de tourisme (ou d'un lieu emblématique) : une colonne « Jour », une colonne « Horaires », 7 lignes de données.
2. Structurez-le avec `<thead>` et `<tbody>`, une `<caption>` explicite, des `<th scope="col">` pour les en-têtes de colonnes et des `<th scope="row">` pour les jours.
3. Validez la page, puis vérifiez la lecture du tableau : chaque cellule doit pouvoir être rattachée sans ambiguïté à ses en-têtes.

{{< corrige title="Corrigé de l'exercice 4" >}}
```html
<table>
    <caption>Horaires d'ouverture de l'office de tourisme (juillet–août)</caption>
    <thead>
        <tr>
            <th scope="col">Jour</th>
            <th scope="col">Horaires</th>
        </tr>
    </thead>
    <tbody>
        <tr><th scope="row">Lundi</th><td>9 h – 18 h</td></tr>
        <tr><th scope="row">Mardi</th><td>9 h – 18 h</td></tr>
        <tr><th scope="row">Mercredi</th><td>9 h – 18 h</td></tr>
        <tr><th scope="row">Jeudi</th><td>9 h – 18 h</td></tr>
        <tr><th scope="row">Vendredi</th><td>9 h – 20 h (nocturne)</td></tr>
        <tr><th scope="row">Samedi</th><td>9 h – 20 h</td></tr>
        <tr><th scope="row">Dimanche</th><td>10 h – 13 h</td></tr>
    </tbody>
</table>
```
{{< /corrige >}}

## Exercice 5 — Tableau complexe : les statistiques de fréquentation

**Durée indicative : 25 min.** Objectifs : fusionner des cellules ; garantir l'accessibilité d'un tableau à double entrée.

L'office de tourisme publie ses statistiques de fréquentation. Reproduisez le tableau suivant (inventez des chiffres plausibles pour votre ville) :

| **Site** | **2024 — Été** | **2024 — Hors saison** | **2025 — Été** | **2025 — Hors saison** |
|---|---|---|---|---|
| Citadelle | 48 200 | 12 700 | 51 400 | 14 100 |
| Musée maritime | 21 300 | 9 800 | 23 900 | 11 200 |
| Total | 69 500 | 22 500 | 75 300 | 25 300 |

1. Dans la section « Découvrir » (ou une nouvelle sous-section « La ville en chiffres »), construisez ce tableau avec un `<thead>` sur **deux lignes** : une première ligne où « Site » occupe deux lignes (`rowspan`) et où chaque année occupe deux colonnes (`colspan`), une seconde ligne avec les saisons.
2. Placez la ligne « Total » dans un `<tfoot>`.
3. Le tableau étant complexe, remplacez les `scope` par le couple `id=` (sur chaque `<th>`) / `headers=` (sur chaque `<td>`, listant tous ses en-têtes séparés par des espaces).
4. Ajoutez une `<caption>` précisant la source et l'unité (« Nombre de visiteurs — source : office de tourisme »).

{{< alert type="tip" >}}
Vous constaterez combien l'attribut `headers` devient vite verbeux : un tableau complexe gagne souvent à être découpé en plusieurs tableaux simples. Si le temps manque, construisez le `<thead>` fusionné, puis complétez le `<tbody>` plus tard à partir du corrigé.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 5" >}}
```html
<table>
    <caption>Nombre de visiteurs par site — source : office de tourisme</caption>
    <thead>
        <tr>
            <th id="site" rowspan="2">Site</th>
            <th id="a2024" colspan="2">2024</th>
            <th id="a2025" colspan="2">2025</th>
        </tr>
        <tr>
            <th id="ete24" headers="a2024">Été</th>
            <th id="hs24" headers="a2024">Hors saison</th>
            <th id="ete25" headers="a2025">Été</th>
            <th id="hs25" headers="a2025">Hors saison</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th id="citadelle" headers="site">Citadelle</th>
            <td headers="citadelle a2024 ete24">48 200</td>
            <td headers="citadelle a2024 hs24">12 700</td>
            <td headers="citadelle a2025 ete25">51 400</td>
            <td headers="citadelle a2025 hs25">14 100</td>
        </tr>
        <tr>
            <th id="musee" headers="site">Musée maritime</th>
            <td headers="musee a2024 ete24">21 300</td>
            <td headers="musee a2024 hs24">9 800</td>
            <td headers="musee a2025 ete25">23 900</td>
            <td headers="musee a2025 hs25">11 200</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th id="total" headers="site">Total</th>
            <td headers="total a2024 ete24">69 500</td>
            <td headers="total a2024 hs24">22 500</td>
            <td headers="total a2025 ete25">75 300</td>
            <td headers="total a2025 hs25">25 300</td>
        </tr>
    </tfoot>
</table>
```
{{< /corrige >}}

## Exercice 6 — Le formulaire de contact

**Durée indicative : 50 min, peut se faire en deux temps.** Objectifs : construire un formulaire complet, valide et accessible.

L'office de tourisme souhaite un formulaire de **demande de brochure et d'inscription à une visite guidée**. Dans la section « Contact », créez un formulaire (`method="post"`, `action="#"` faute de serveur) comportant :

1. Un premier `<fieldset>` « Vos coordonnées » : nom (texte), adresse électronique (`email`), téléphone (`tel`, facultatif). Chaque champ a un `<label>` relié par `for`/`id`, l'attribut `autocomplete` approprié (`name`, `email`, `tel`), et les deux premiers sont `required`.
2. Un deuxième `<fieldset>` « Votre visite » : une liste déroulante `<select>` des visites guidées proposées (avec une première option vide « — Choisir — »), un sélecteur de `date`, un champ `number` « Nombre de participants » borné par `min="1"` et `max="15"`.
3. Un troisième `<fieldset>` « Vos centres d'intérêt » : trois cases à cocher (patrimoine, gastronomie, nature…).
4. Un quatrième `<fieldset>` « Formule » : deux boutons radio « Visite libre » / « Visite guidée » partageant le même `name`, l'un étant pré-coché.
5. Une zone `<textarea>` « Votre message » (facultative, `maxlength="500"`), puis un bouton d'envoi explicite (« Envoyer ma demande » plutôt que « OK »).
6. Testez la validation native : essayez d'envoyer le formulaire vide, avec un courriel mal formé, avec 20 participants.

{{< alert type="a11y" >}}
Test décisif : cliquez sur chaque **libellé** — le champ correspondant doit recevoir le focus. Puis parcourez tout le formulaire au clavier seul (Tab, flèches dans les radios, Espace pour cocher) : rien ne doit être inatteignable.
{{< /alert >}}

**Bonus** : ajoutez un champ « Ville de départ » utilisant `<input list=…>` et une `<datalist>` de suggestions.

{{< alert type="tip" >}}
C'est l'exercice à ne sacrifier à aucun prix : mieux vaut passer rapidement sur le tableau complexe de l'exercice 5 que sur le formulaire. Il se poursuit naturellement sur la séance suivante.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 6" >}}
```html
<form method="post" action="#">
    <fieldset>
        <legend>Vos coordonnées</legend>
        <label for="nom">Nom</label>
        <input type="text" name="nom" id="nom" autocomplete="name" required>
 
        <label for="courriel">Adresse électronique</label>
        <input type="email" name="courriel" id="courriel"
               autocomplete="email" required>
 
        <label for="tel">Téléphone (facultatif)</label>
        <input type="tel" name="tel" id="tel" autocomplete="tel">
    </fieldset>
 
    <fieldset>
        <legend>Votre visite</legend>
        <label for="visite">Visite guidée</label>
        <select name="visite" id="visite">
            <option value="">— Choisir —</option>
            <option value="citadelle">La citadelle Vauban</option>
            <option value="port">Le vieux port</option>
            <option value="douaniers">Le sentier des douaniers</option>
        </select>
 
        <label for="date">Date souhaitée</label>
        <input type="date" name="date" id="date">
 
        <label for="nb">Nombre de participants</label>
        <input type="number" name="nb" id="nb" min="1" max="15" value="2">
    </fieldset>
 
    <fieldset>
        <legend>Vos centres d'intérêt</legend>
        <label><input type="checkbox" name="interet" value="patrimoine"> Patrimoine</label>
        <label><input type="checkbox" name="interet" value="gastronomie"> Gastronomie</label>
        <label><input type="checkbox" name="interet" value="nature"> Nature</label>
    </fieldset>
 
    <fieldset>
        <legend>Formule</legend>
        <label><input type="radio" name="formule" value="libre" checked> Visite libre</label>
        <label><input type="radio" name="formule" value="guidee"> Visite guidée</label>
    </fieldset>
 
    <label for="message">Votre message</label>
    <textarea name="message" id="message" rows="5" maxlength="500"></textarea>
 
    <button type="submit">Envoyer ma demande</button>
</form>
```

Bonus `datalist` : `<input list="villes" id="depart" name="depart">` suivi de `<datalist id="villes"><option value="Nantes"><option value="Rennes"></datalist>`.

> **À noter.** Le corrigé relie les libellés courts (cases, radios) par imbrication, et les champs par `for`/`id` : les deux méthodes sont valides ; la liaison explicite reste préférable pour les champs isolés.
{{< /corrige >}}

## Exercice 7 — Audit express

**Durée indicative : 15 min.** Objectifs : ancrer le réflexe de validation ; faire un premier audit d'accessibilité.

1. Repassez `index.html` au validateur W3C : zéro erreur exigé.
2. Passez la checklist d'accessibilité de la partie HTML : `lang` présent ; un seul `h1` et hiérarchie de titres sans saut ; toutes les images ont un `alt` pertinent (vide si décoratives) ; tous les liens sont explicites ; tableaux avec `caption` et en-têtes reliés ; tous les champs ont un label.
3. Lancez un audit Lighthouse (F12 → onglet Lighthouse → catégorie « Accessibility ») et analysez les éventuels signalements.

{{< alert type="note" >}}
Score Lighthouse de 100 ≠ page accessible : l'outil ne détecte qu'une partie des problèmes. Mais un score &lt; 100 signale à coup sûr de vrais défauts à corriger.
{{< /alert >}}

**Bonus « vu par les machines »** : affichez votre page comme la voient les robots d'indexation et les IA génératives — code source brut (Ctrl+U) ou CSS désactivé (dans Firefox : Affichage → Style de la page → Aucun style). Trois questions : le contenu principal se distingue-t-il des menus ? Chaque section reste-t-elle compréhensible sortie de son contexte ? Le `<title>` et la meta `description` décrivent-ils fidèlement la page ? Si oui, votre page est bien armée pour le SEO comme pour le GEO (voir cours, section 2.6).

{{< corrige title="Corrigé de l'exercice 7" >}}
Il n'y a pas de code attendu : la production est la checklist vérifiée. Erreurs typiquement relevées à ce stade — un `alt` manquant sur l'image décorative (il doit être présent **et** vide), un saut de `h1` à `h3`, un `<li>` hors de tout `<ul>`/`<ol>`, un `label` non relié (faute de frappe entre `for` et `id`), l'attribut `headers` incomplet dans le tableau complexe.
{{< /corrige >}}
