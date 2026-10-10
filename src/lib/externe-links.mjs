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

export default function externeLinks() {
  return {
    name: 'externe-links-neuer-tab',
    hooks: {
      'astro:build:done': async ({ dir }) => {
        for await (const f of htmlDateien(fileURLToPath(dir))) {
          const alt = await readFile(f, 'utf8');
          const neu = bilderLazy(markiereExterneLinks(alt));
          if (neu !== alt) await writeFile(f, neu);
        }
      },
    },
  };
}
