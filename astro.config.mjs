// Astro-Konfiguration für andreassobing.de
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { readdirSync, readFileSync } from 'node:fs';
import externeLinks from './src/lib/externe-links.mjs';

// Alte WordPress-Adressen, die es so nicht mehr gibt
const redirects = {
  '/e-mail-marketing-guide': '/thema/e-mail-marketing/',
  '/glossar': '/das-grosse-marketing-glossar-die-wichtigsten-begriffe-einfach-erklaert/',
  '/feed': '/rss.xml',
  '/cookie-richtlinie-eu': '/datenschutz/',
  '/author/sobing': '/',
  '/category/unkategorisiert': '/archiv/',
};

// Änderungsdatum je Seite für die Sitemap (updated, sonst date aus dem Frontmatter)
const lastmod = new Map();
for (const dir of ['src/content/posts', 'src/content/pages']) {
  for (const f of readdirSync(dir).filter((n) => n.endsWith('.md'))) {
    const fm = readFileSync(`${dir}/${f}`, 'utf-8').split('---')[1] || '';
    const slug = fm.match(/^slug:\s*"?([^"\n]+)"?/m)?.[1];
    const datum = fm.match(/^updated:\s*"?([^"\n]+)"?/m)?.[1] || fm.match(/^date:\s*"?([^"\n]+)"?/m)?.[1];
    if (slug && datum) lastmod.set(`/${slug}/`, new Date(datum).toISOString());
  }
}
// Schlagwörter mit höchstens zwei Artikeln: auf der Seite noindex, hier nicht in die Sitemap
const tagSlug = (t) => t.toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
  .replace(/&/g, 'und').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const tagZahl = new Map();
for (const f of readdirSync('src/content/posts').filter((n) => n.endsWith('.md'))) {
  const fm = readFileSync(`src/content/posts/${f}`, 'utf-8').split('---')[1] || '';
  if (/^draft:\s*true/m.test(fm)) continue;
  const block = fm.match(/^tags:\n((?:\s+-.*\n?)+)/m)?.[1] || '';
  for (const m of block.matchAll(/-\s*"?([^"\n]+)"?/g)) tagZahl.set(tagSlug(m[1]), (tagZahl.get(tagSlug(m[1])) || 0) + 1);
}
const duenneSchlagwoerter = new Set([...tagZahl].filter(([, n]) => n <= 2).map(([s]) => `/schlagwort/${s}/`));
const ausschluss = ['/suche/', '/tag/', '/404'];
const weiterleitungen = Object.keys(redirects).map((r) => `${r}/`);

export default defineConfig({
  site: 'https://andreassobing.de',
  trailingSlash: 'always',
  build: { format: 'directory' },
  integrations: [
    sitemap({
      filter: (page) => {
        const pfad = new URL(page).pathname;
        if (ausschluss.some((a) => pfad.startsWith(a)) || weiterleitungen.includes(pfad)) return false;
        return !duenneSchlagwoerter.has(pfad);
      },
      serialize: (item) => {
        const d = lastmod.get(new URL(item.url).pathname);
        if (d) item.lastmod = d;
        return item;
      },
    }),
    externeLinks(),
  ],
  redirects,
});
