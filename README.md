# Blog it Marketing – andreassobing.de

Statische Website, gebaut mit [Astro](https://astro.build), veröffentlicht über GitHub Pages.

## Neuen Artikel schreiben

1. Neue Datei in `src/content/posts/` anlegen, z. B. `mein-neuer-artikel.md`.
2. Oben die Angaben eintragen:

```markdown
---
title: "Titel des Artikels"
slug: "mein-neuer-artikel"
date: 2026-10-06T09:00:00
description: "Ein bis zwei Sätze für Google und die Startseite."
image: "/wp-content/uploads/2026/10/bild.jpg"
category: "marketing"
tags:
  - "OKR"
vgwort: "https://vg0X.met.vgwort.de/na/ÖFFENTLICHE-ZÄHLMARKE"
---

Hier beginnt der Text. ## Zwischenüberschrift, **fett**, - Aufzählung.
```

3. Bilder in `public/wp-content/uploads/JAHR/MONAT/` ablegen.
4. In GitHub Desktop: **Commit** und **Push**. Nach 1–2 Minuten ist der Artikel online.

**Rubriken (`category`):** `marketing`, `strategie`, `email-marketing`, `marke`, `psychologie`, `ki-tools`, `arbeitsweisen`, `fundstuecke`

**VG Wort:** Nur die **öffentliche** Zählmarke eintragen, niemals die private.

**Video einbetten:** `<div class="video" data-provider="youtube" data-id="VIDEO-ID"></div>` – wird erst nach Klick geladen.

## Lokal ansehen

```
npm install
npm run dev
```

## Ordner

- `src/content/posts/` – alle Artikel (Markdown)
- `src/content/pages/` – Impressum, Datenschutz und weitere Seiten
- `public/wp-content/uploads/` – Bilder
- `src/layouts`, `src/pages`, `src/styles` – Design und Seitenaufbau
- `tools/` – einmalige Skripte vom Umzug aus WordPress (2026)
