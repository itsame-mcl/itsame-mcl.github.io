---
title: "Travaux pratiques CSS 3 : mettre en forme le mini-site"
description: "Sept exercices corrigés pour pratiquer CSS 3 : charte graphique, modèle de boîte, Flexbox, Grid, responsive design et accessibilité."
date: 2026-10-28T12:00:00+01:00
lastmod: 2026-10-28T12:00:00+01:00
tags: ["HTML", "CSS", "Accessibilité", "Exercices"]
categories: ["Formation"]
menu:
  sidebar:
    name: "TP - CSS (exercices 8 à 14)"
    identifier: tp-css
    parent: html-css
    weight: 100
---

Suite des travaux pratiques : vous partez de la page HTML terminée à l'exercice 7 (voir [le TP HTML]({{< relref "tp-html" >}})) et vous la mettez en forme avec CSS, de la charte graphique jusqu'au responsive design, sans jamais perdre de vue l'accessibilité. Si vous n'avez pas terminé la première partie, vous pouvez repartir du fichier `index.html` de l'annexe en bas de page.

{{< alert type="tip" >}}
Chaque exercice s'appuie sur le précédent. Si vous êtes bloqué, repartez du corrigé de l'exercice précédent plutôt que de rester coincé.
{{< /alert >}}

## Exercice 8 — La charte graphique de base

**Durée indicative : 30 min.** Objectifs : lier une feuille de style ; poser variables, typographie et couleurs accessibles.

1. Créez `style.css` à la racine de `mon-site/` et liez-le dans le `<head>` de `index.html`. Vérifiez la liaison avec une règle temporaire voyante (`body { background: yellow; }`), puis retirez-la.
2. Posez les fondations : le sélecteur universel avec `box-sizing: border-box`, puis un bloc `:root` définissant vos variables : `--couleur-principale`, `--couleur-accent`, `--couleur-fond`, `--couleur-texte`. Choisissez des couleurs évoquant votre ville (mer, pierre, vignes…).
3. Vérifiez le contraste texte/fond de chaque combinaison sur webaim.org/resources/contrastchecker : visez AA (4,5:1) minimum. Ajustez si nécessaire.
4. Stylez `body` : famille de polices avec liste de repli et générique, `font-size: 1rem`, `line-height: 1.5`, couleurs via `var()`.
5. Stylez les titres (`h1`, `h2`) avec votre couleur principale, et les liens : conservez un soulignement (ou un autre indice non chromatique) et définissez un état `:hover` et un état `:focus-visible` avec un `outline` bien visible.

{{< alert type="a11y" >}}
Testez immédiatement au clavier : tabulez à travers la page — le contour de focus doit être évident sur chaque lien.
{{< /alert >}}

{{< alert type="pitfall" >}}
Vous découvrirez peut-être que votre duo de couleurs favori est illisible : c'est normal, et c'est précieux. Ne court-circuitez pas la vérification des contrastes.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 8" >}}
```css
/* ===== Fondations ===== */
* {
    box-sizing: border-box;
}
 
:root {
    --couleur-principale: #14526e;  /* bleu marine profond */
    --couleur-accent: #b3541e;      /* terre cuite */
    --couleur-fond: #fdfaf5;        /* écru */
    --couleur-fond-carte: #ffffff;
    --couleur-texte: #22303a;
}
 
body {
    margin: 0;
    font-family: "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 1rem;
    line-height: 1.5;
    background-color: var(--couleur-fond);
    color: var(--couleur-texte);
}
 
h1, h2, h3 {
    color: var(--couleur-principale);
    line-height: 1.2;
}
 
a {
    color: var(--couleur-principale);
    text-decoration: underline;
}
 
a:hover {
    color: var(--couleur-accent);
}
 
a:focus-visible {
    outline: 3px solid var(--couleur-accent);
    outline-offset: 2px;
}
```

Contrastes du corrigé : `#22303a` sur `#fdfaf5` ≈ 13:1 et `#14526e` sur `#fdfaf5` ≈ 8,2:1 — largement au-dessus du seuil AA de 4,5:1.
{{< /corrige >}}

## Exercice 9 — Le modèle de boîte : encadrés et cartes

**Durée indicative : 30 min.** Objectifs : maîtriser padding, bordures, marges et le centrage d'un bloc.

1. Limitez la largeur du contenu : `main { max-width: 70rem; margin: 0 auto; padding: 0 1rem; }`. Observez l'effet en redimensionnant la fenêtre.
2. Transformez l'`<aside>` « Le saviez-vous ? » en encadré : fond légèrement teinté, `padding` confortable, bordure gauche épaisse dans votre couleur d'accent, coins arrondis (`border-radius`).
3. Créez une classe `.carte` (fond blanc, bordure fine, `padding`, coins arrondis, légère ombre avec `box-shadow`) et appliquez-la à la `<figure>` de l'exercice 3.
4. Stylez vos deux tableaux : `border-collapse: collapse` sur `table`, `padding` dans les cellules, bordures fines, lignes zébrées avec `tbody tr:nth-child(even)`, et mise en évidence du `<tfoot>`.
5. Avec les outils de développement (F12, onglet « Inspecteur »), survolez vos boîtes et observez le diagramme du modèle de boîte (contenu / padding / bordure / marge).

**Bonus** : stylez le formulaire — champs sur toute la largeur de leur conteneur, `padding` interne, bordure qui change de couleur au `:focus-visible`.

{{< alert type="tip" >}}
Le modèle de boîte est le concept central du CSS : prenez le temps d'inspecter vos boîtes avec les outils de développement (F12) plutôt que de deviner.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 9" >}}
```css
main {
    max-width: 70rem;
    margin: 0 auto;
    padding: 0 1rem;
}
 
aside {
    background-color: #eef4f7;
    border-left: 6px solid var(--couleur-accent);
    border-radius: 8px;
    padding: 1rem 1.5rem;
    margin: 1.5rem 0;
}
 
.carte {
    background-color: var(--couleur-fond-carte);
    border: 1px solid #d8d8d8;
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 6px rgb(0 0 0 / 0.08);
}
 
/* ===== Tableaux ===== */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.5rem 0;
}
 
caption {
    font-style: italic;
    margin-bottom: 0.5rem;
}
 
th, td {
    border: 1px solid #c5cdd3;
    padding: 0.5rem 0.75rem;
    text-align: left;
}
 
thead th {
    background-color: var(--couleur-principale);
    color: #ffffff;
}
 
tbody tr:nth-child(even) {
    background-color: #f0f4f7;
}
 
tfoot {
    font-weight: bold;
    background-color: #e3ecf2;
}
```
{{< /corrige >}}

## Exercice 10 — La navigation en Flexbox

**Durée indicative : 20 min.** Objectifs : construire une barre de navigation moderne ; comprendre axes et alignements.

1. Sur le `<ul>` du menu : supprimez puces, marges et padding par défaut (`list-style: none; margin: 0; padding: 0;`), puis passez-le en `display: flex` avec `gap: 1.5rem`.
2. Centrez le menu avec `justify-content: center`, puis testez tour à tour `space-between`, `space-evenly`, `flex-end` : observez et retenez la différence.
3. Agrandissez la zone cliquable des liens : `display: block` et `padding: 0.75rem 1rem` sur les `<a>` du menu (une cible tactile d'au moins 44 px de haut).
4. Ajoutez un état de survol ET de focus (`:hover`, `:focus-visible`) : changement de fond, pas seulement de couleur de texte.
5. Signalez la page courante : ajoutez `aria-current="page"` sur le lien « Accueil » dans le HTML, puis stylez-le en CSS avec le sélecteur d'attribut `nav a[aria-current="page"]`.
6. Rendez l'en-tête « collant » : `header { position: sticky; top: 0; }` (avec un fond opaque et un `z-index` suffisant pour passer au-dessus du contenu).

**Bonus** : passez `flex-direction` à `column` pour prévisualiser ce que donnera le menu sur mobile (exercice 13), puis revenez en `row`.

{{< alert type="tip" >}}
Pour vous entraîner en jouant : [Flexbox Froggy](https://flexboxfroggy.com/) (Flexbox) et [Grid Garden](https://cssgridgarden.com/) (Grid) sont de bons compléments aux exercices 10 à 12.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 10" >}}
```css
header {
    position: sticky;
    top: 0;
    z-index: 10;
    background-color: var(--couleur-principale);
    padding: 0.5rem 1rem;
}
 
header h1 {
    color: #ffffff;
    margin: 0.25rem 0;
}
 
nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 1.5rem;
}
 
nav a {
    display: block;
    padding: 0.75rem 1rem;
    color: #ffffff;
    text-decoration: none;
    font-weight: bold;
}
 
nav a:hover,
nav a:focus-visible {
    background-color: var(--couleur-accent);
    border-radius: 4px;
}
 
nav a[aria-current="page"] {
    border-bottom: 3px solid #ffffff;
}
```

> **Accessibilité.** Les liens du menu perdent ici leur soulignement, mais restent identifiables : ils sont isolés dans une zone de navigation, en gras et sur fond contrasté — le contexte remplace l'indice chromatique. Dans le corps du texte, en revanche, le soulignement est conservé.
{{< /corrige >}}

## Exercice 11 — La galerie « incontournables » en Grid

**Durée indicative : 20 min.** Objectifs : créer une grille de cartes ; découvrir fr, repeat() et minmax().

1. Dans la section « Découvrir », sous le Top 5, créez dans le HTML une galerie : un `<div class="galerie">` contenant 4 à 6 `<figure class="carte">` (image + `<figcaption>`), une par lieu incontournable. Chaque image a son `alt` (ou `alt=""` si la légende dit déjà tout).
2. Passez `.galerie` en `display: grid` avec `grid-template-columns: repeat(3, 1fr)` et `gap: 1.5rem`. Observez le comportement quand vous réduisez la fenêtre : les colonnes rétrécissent mais leur nombre ne change pas.
3. Remplacez la définition des colonnes par `repeat(auto-fit, minmax(240px, 1fr))` et observez : la grille se réorganise seule selon la largeur disponible.
4. Rendez les images uniformes : `width: 100%; height: 220px; object-fit: cover;` sur les images de la galerie.
5. Mettez un lieu à l'honneur : faites occuper 2 colonnes à la première carte avec `grid-column: span 2` (que se passe-t-il sur les écrans étroits ?).

{{< corrige title="Corrigé de l'exercice 11" >}}
```css
.galerie {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}
 
.galerie img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-radius: 4px;
}
 
.galerie figure {
    margin: 0;   /* les figure ont une marge par défaut */
}
 
.vedette {
    grid-column: span 2;
}
```

Avec `auto-fit`/`minmax`, la carte `.vedette` peut provoquer un débordement quand la grille ne compte plus qu'une colonne : c'est l'accroche parfaite pour l'exercice 13, où le `span` ne sera appliqué qu'à partir de 768 px.
{{< /corrige >}}

## Exercice 12 — Le gabarit de page en Grid

**Durée indicative : 20 min.** Objectifs : composer la page entière avec grid-template-areas.

1. Passez le `<body>` en `display: grid` et définissez le gabarit : `grid-template-columns: 2fr 1fr`, et `grid-template-areas` dessinant trois rangées : `"header header"`, `"main aside"`, `"footer footer"`, avec `gap: 1.5rem`.
2. Affectez chaque zone : `header { grid-area: header; }`, `main { grid-area: main; }`, `aside { grid-area: aside; }`, `footer { grid-area: footer; }`.
3. L'`<aside>` étant sorti du `<main>` pour devenir une zone à part entière, déplacez la balise dans le HTML : elle devient un enfant direct du `<body>`, entre `<main>` et `<footer>`.
4. Ajustez : le `main` n'a plus besoin de son `margin: 0 auto` (le gabarit s'en charge) — déplacez la contrainte de largeur sur le `body` (`max-width: 75rem; margin: 0 auto;`).
5. Vérifiez au clavier et à la lecture du code que l'**ordre du HTML** reste logique (contenu principal avant contenu secondaire) : Grid a changé la présentation, pas la structure.

{{< alert type="tip" >}}
Les exercices 10 et 11 (Flexbox et Grid) sont à faire en priorité. Si vous manquez de temps, lisez le corrigé de celui-ci plutôt que de le sauter : il montre comment composer toute une page avec `grid-template-areas`.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 12" >}}
```css
body {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-areas:
        "header header"
        "main   aside"
        "footer footer";
    gap: 1.5rem;
    max-width: 75rem;
    margin: 0 auto;
}
 
header { grid-area: header; }
main   { grid-area: main; }
aside  { grid-area: aside; }
footer { grid-area: footer; }
```

Côté HTML, l'`<aside>` devient enfant direct du `<body>`, placé entre `</main>` et `<footer>`. L'ordre du code reste logique : contenu principal d'abord, complément ensuite.

> **Attention.** Le `header` en `position: sticky` doit rester pleine largeur et opaque ; si le `body` est contraint en largeur, le fond du header s'arrête à ses bords — un compromis acceptable ici, à discuter avec le groupe (solution complète : sortir la contrainte de largeur dans un conteneur interne).
{{< /corrige >}}

## Exercice 13 — Passage au responsive

**Durée indicative : 30 min.** Objectifs : adopter la démarche mobile first ; écrire ses premières media queries.

1. Ouvrez le mode « appareil mobile » des outils de développement (F12 → icône téléphone/tablette) et regardez votre site en 375 px de large : listez ce qui ne va pas (menu à l'étroit, aside écrasé, carte `span 2` débordante…).
2. Vérifiez que la meta `viewport` est bien présente (exercice 1) et ajoutez la règle des images fluides : `img { max-width: 100%; height: auto; }`.
3. Réorganisez la feuille de style en mobile first : les styles **de base** décrivent la version mobile — gabarit en une seule colonne (`grid-template-columns: 1fr` et `grid-template-areas` empilées : header, main, aside, footer), menu en `flex-direction: column`, carte vedette sans `span`.
4. Ajoutez une media query `@media (min-width: 768px)` qui rétablit pour les grands écrans : le gabarit deux colonnes de l'exercice 12, le menu en ligne, le `span 2` de la carte vedette.
5. Testez aux différentes largeurs, y compris intermédiaires : aucune barre de défilement horizontale ne doit apparaître, quel que soit l'écran.

{{< alert type="a11y" >}}
Dans le navigateur, zoomez à 200 % (Ctrl +) : le contenu doit se réorganiser sans perte d'information ni défilement horizontal — c'est un critère WCAG, et votre mise en page responsive vient de le satisfaire.
{{< /alert >}}

{{< alert type="tip" >}}
Le changement de point de vue à retenir : **les styles de base décrivent la version mobile**, et les media queries ajoutent les adaptations pour les grands écrans. Le mode « appareil mobile » des outils de développement vous accompagnera tout au long de l'exercice.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 13" >}}
Les règles de base décrivent désormais le mobile ; la media query rétablit la mise en page large. Extrait de la feuille réorganisée :

```css
/* ===== Base (mobile) ===== */
img {
    max-width: 100%;
    height: auto;
}
 
body {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-areas:
        "header"
        "main"
        "aside"
        "footer";
    gap: 1rem;
}
 
nav ul {
    flex-direction: column;
    gap: 0;
}
 
/* ===== Écrans ≥ 768 px ===== */
@media (min-width: 768px) {
    body {
        grid-template-columns: 2fr 1fr;
        grid-template-areas:
            "header header"
            "main   aside"
            "footer footer";
        gap: 1.5rem;
        max-width: 75rem;
        margin: 0 auto;
    }
 
    nav ul {
        flex-direction: row;
        gap: 1.5rem;
    }
 
    .vedette {
        grid-column: span 2;
    }
}
```

La règle `.vedette { grid-column: span 2; }` des styles de base est **supprimée** : elle ne vit plus que dans la media query. La galerie en `auto-fit`/`minmax` n'a, elle, besoin d'aucune media query : elle était déjà fluide.
{{< /corrige >}}

## Exercice 14 — Finitions accessibilité et audit final

**Durée indicative : 20 min.** Objectifs : livrer un site conforme aux bonnes pratiques vues sur les deux jours.

1. Ajoutez un **lien d'évitement** : premier enfant du `<body>`, `<a class="evitement" href="#contenu">Aller au contenu</a>` pointant vers `<main id="contenu">`. En CSS, masquez-le hors écran et faites-le réapparaître au `:focus-visible` (voir la classe `.sr-only` du cours, chapitre 10).
2. Ajoutez la media query `prefers-reduced-motion: reduce` neutralisant vos éventuelles transitions/animations.
3. Repassez l'audit complet : validateur W3C (HTML et CSS), Lighthouse « Accessibility », vérification des contrastes, et un parcours intégral au clavier.
4. Échangez votre place avec votre voisin : chacun teste le site de l'autre au clavier seul et note ce qui le gêne. Restitution collective.

**Bonus** : ajoutez un thème sombre automatique avec `@media (prefers-color-scheme: dark)` en ne redéfinissant que vos variables CSS — si votre charte est bien construite sur les variables de l'exercice 8, quatre lignes suffisent.

**Bonus ultime** : créez une vraie page `decouvrir.html` reprenant l'en-tête et le pied de page, et transformez les ancres du menu en vrais liens entre pages — vous venez de faire un site multi-pages, et votre feuille de style est déjà mutualisée.

{{< alert type="tip" >}}
Si vous travaillez seul, remplacez l'échange avec un voisin par un test au clavier seul, souris mise de côté : vous découvrirez vous-même les défauts de votre site.
{{< /alert >}}

{{< corrige title="Corrigé de l'exercice 14" >}}
```css
/* Lien d'évitement : masqué hors écran, visible au focus */
.evitement {
    position: absolute;
    left: -9999px;
}
 
.evitement:focus-visible {
    position: fixed;
    left: 1rem;
    top: 1rem;
    z-index: 100;
    background-color: var(--couleur-accent);
    color: #ffffff;
    padding: 0.75rem 1.25rem;
    border-radius: 4px;
}
 
/* Respect des préférences de mouvement */
@media (prefers-reduced-motion: reduce) {
    * {
        animation: none;
        transition: none;
        scroll-behavior: auto;
    }
}
 
/* Bonus : thème sombre automatique */
@media (prefers-color-scheme: dark) {
    :root {
        --couleur-fond: #16212a;
        --couleur-fond-carte: #1f2d38;
        --couleur-texte: #e8eef2;
        --couleur-principale: #7fb6d9;
    }
}
```

Côté HTML : `<a class="evitement" href="#contenu">Aller au contenu</a>` en premier enfant du `<body>`, et `id="contenu"` sur le `<main>`. Vérification finale : Tab depuis la barre d'adresse — le lien d'évitement doit être le premier élément atteint.

> **À noter.** Si le thème sombre est activé, refaire un contrôle de contraste : les variables sombres du corrigé conservent des ratios supérieurs à 7:1.
{{< /corrige >}}

## Annexe — Les fichiers finaux

L'arborescence finale du projet :

```
mon-site/
├── index.html
├── style.css
└── images/
    ├── vieux-port.jpg
    ├── citadelle.jpg
    ├── musee.jpg
    ├── sentier.jpg
    └── frise-vagues.png
```

La structure complète de `index.html` en fin de formation (contenus abrégés) :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Visiter Bellerive-sur-Mer — Accueil</title>
    <meta name="description" content="…">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <a class="evitement" href="#contenu">Aller au contenu</a>
    <header id="top">
        <h1>Visiter Bellerive-sur-Mer</h1>
        <nav>
            <ul>
                <li><a href="index.html" aria-current="page">Accueil</a></li>
                <li><a href="#decouvrir">Découvrir</a></li>
                <li><a href="#infos">Infos pratiques</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main id="contenu">
        <section id="decouvrir">
            <h2>Découvrir la ville</h2>
            <p>…introduction…</p>
            <h3>Le top 5 des incontournables</h3>
            <ol>…</ol>
            <div class="galerie">
                <figure class="carte vedette">…</figure>
                <figure class="carte">…</figure>
                <figure class="carte">…</figure>
                <figure class="carte">…</figure>
            </div>
            <h3>La ville en chiffres</h3>
            <table>…tableau complexe (exercice 5)…</table>
        </section>
        <section id="infos">
            <h2>Infos pratiques</h2>
            <ul>…conseils…</ul>
            <table>…horaires (exercice 4)…</table>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <form>…formulaire (exercice 6)…</form>
        </section>
    </main>
    <aside>
        <h2>Le saviez-vous ?</h2>
        <p>…anecdote…</p>
        <dl>…glossaire…</dl>
    </aside>
    <footer>
        <p>© 2026 Office de tourisme de Bellerive-sur-Mer —
           <a href="#top">Retour en haut de page</a></p>
    </footer>
</body>
</html>
```

La feuille `style.css` finale est l'assemblage, dans cet ordre, des corrigés des exercices 8 (fondations), 9 (boîtes et tableaux), 10 (navigation), 11 (galerie), 13 (gabarit mobile first et media query — qui remplace le gabarit fixe de l'exercice 12) et 14 (finitions).
