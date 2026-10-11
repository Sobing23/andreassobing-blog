// Astro-Integration: Nach dem Bauen alle Links auf fremde Seiten in einem neuen Tab öffnen
// (target="_blank" rel="noopener noreferrer"). Eigene Links bleiben im selben Tab.
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const EIGENE = /^(https?:)?\/\/(www\.)?(andreassobing\.de|hun-gry\.com|hun-gry\.de|neu\.andreassobing\.de)(\/|$)/i;

export function markiereExterneLinks(html) {
  return html.replace(/<a\b([^>]*?)\bhref="([^"]*)"([^>]*)>/gi, (tag, vor, href, nach) => {
    if (!/^(https?:)?\/\//i.test(href) || EIGENE.test(href) || /\btarget=/i.test(vor + nach)) return tag;
    return `<a${vor}href="${href}"${nach} target="_blank" rel="noopener noreferrer">`;
  });
}

async function* htmlDateien(dir) {
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) yield* htmlDateien(p);
    else if (e.name.endsWith('.html')) yield p;
  }
}

// Bilder ohne loading-Attribut erst beim Scrollen laden (Titelbilder mit fetchpriority und Zählpixel ausgenommen)
export function bilderLazy(html) {
  return html.replace(/<img\b(?![^>]*\bloading=)(?![^>]*fetchpriority)(?![^>]*class="vgwort")([^>]*)>/gi, '<img loading="lazy" decoding="async"$1>');
}

// Video-Platzhalter: Titel und Link zu YouTube schon im HTML, damit Suchmaschinen und Leser ohne JavaScript sehen, worum es geht
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const dauer = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
export function videoPlatzhalter(html, videos) {
  return html.replace(/<div class="video" data-provider="youtube" data-id="([^"]+)"><\/div>/g, (tag, id) => {
    const v = videos.get(id);
    const link = `https://www.youtube.com/watch?v=${id}`;
    if (!v) return `<div class="video" data-provider="youtube" data-id="${id}"><a href="${link}">Video auf YouTube ansehen</a></div>`;
    const titel = esc(v.titel.replace(/#shorts?/gi, '').replace(/\s+/g, ' ').trim());
    return `<div class="video" data-provider="youtube" data-id="${id}" data-titel="${titel}" data-dauer="${dauer(v.dauer)}"><p class="video-titel">${titel}</p><a href="${link}">Video auf YouTube ansehen (${dauer(v.dauer)} Min.)</a></div>`;
  });
}

export default function externeLinks() {
  return {
    name: 'externe-links-neuer-tab',
    hooks: {
      'astro:build:done': async ({ dir }) => {
        const liste = JSON.parse(await readFile(new URL('../data/videos.json', import.meta.url), 'utf8'));
        const videos = new Map(liste.map((v) => [v.id, v]));
        for await (const f of htmlDateien(fileURLToPath(dir))) {
          const alt = await readFile(f, 'utf8');
          const neu = bilderLazy(markiereExterneLinks(videoPlatzhalter(alt, videos)));
          if (neu !== alt) await writeFile(f, neu);
        }
      },
    },
  };
}
