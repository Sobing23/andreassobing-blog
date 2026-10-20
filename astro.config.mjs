// Astro-Konfiguration für andreassobing.de
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { readdirSync, readFileSync } from 'node:fs';
import externeLinks from './src/lib/externe-links.mjs';

// Alte WordPress-Adressen, die es so nicht mehr gibt
const redirects = {
  '/e-mail-marketing-guide': '/thema/e-mail-marketing/',
  '/youtube': '/videos/',
  '/glossar': '/das-grosse-marketing-glossar-die-wichtigsten-begriffe-einfach-erklaert/',
  '/feed': '/rss.xml',
  '/cookie-richtlinie-eu': '/datenschutz/',
  '/author/sobing': '/',
  '/category/unkategorisiert': '/archiv/',
  // Runde 1 Zusammenführung (Oktober 2026)
  '/die-4ps-fuer-deinen-marketing-mix': '/die-4ps-des-marketings-ein-umfassender-leitfaden-fuer-einsteiger/',
  '/4ps-marketing-beispiele': '/die-4ps-des-marketings-ein-umfassender-leitfaden-fuer-einsteiger/',
  '/das-aidas-modell-die-weiterentwicklung-eines-bekannten-modells': '/die-aida-formel-dein-schluessel-zum-erfolgreichen-marketing/',
  '/mit-dem-jobs-to-be-done-modell-kundenbeduerfnisse-besser-verstehen': '/jobs-to-be-done-jtbd-fuer-die-kundenbeduerfnisse/',
  '/phasen-der-customer-journey': '/die-customer-journey/',
  '/kaufentscheidungsprozess-so-ticken-kunden': '/der-kaufentscheidungsprozess/',
  '/mit-dem-aaker-modell-baust-du-eine-starke-marke-auf': '/aakers-5-dimensionen-modell/',
  '/das-kapferer-identitaetsprisma': '/das-identitaetsprisma-von-kapferer/',
  '/marktpositionierung-konkurrenz-schlagen': '/marktpositionierung-erfolg-planen/',
  '/warum-du-eine-mission-und-vision-fuer-dein-unternehmen-benoetigst': '/mission-vs-vision-der-wegweiser-fuer-dein-unternehmen/',
  '/die-kunst-einer-wirkungsvollen-vision-und-mission': '/mission-vs-vision-der-wegweiser-fuer-dein-unternehmen/',
  '/wie-du-ein-effektives-unternehmensleitbild-erstellst': '/wieso-du-ein-unternehmensleitbild-benoetigst/',
  '/das-7-s-modell-ein-umfassender-blick-auf-unternehmenserfolg': '/das-mckinsey-7-s-modell/',
  '/balanced-scorecard-fuer-nachhaltigen-erfolg': '/balanced-scorecard-einfach-erklaert/',
  '/warum-das-moderne-betriebsmodell-nutzen': '/warum-du-ein-modernes-betriebsmodell-fuer-dein-unternehmen-brauchst/',
  '/okr-connected-strategic-implementation-stack': '/der-connected-strategic-stack/',
  '/okrs-im-change-management': '/okr-im-change-management/',
  '/preiselastizitaet-der-nachfrage': '/preiselastizitaet-der-nachfrage-ein-muss-fuer-jedes-marketing/',
  '/diminishing-returns-das-gesetz-der-abnehmenden-ertraege-erklaert': '/ertragsgesetz-grundlagen-und-praktische-bedeutung/',
  '/customer-lifecycle-clc': '/der-customer-life-cycle-im-ueberblick/',
  '/wie-du-den-customer-lifetime-value-erhoehst': '/customer-lifetime-value-der-wert-deiner-kunden/',
  '/ctr-vs-ctor': '/ctr-vs-cto-im-e-mail-marketing/',
  '/click-to-open-rate-ctor-fuer-erfolgreiches-e-mail-marketing': '/ctr-vs-cto-im-e-mail-marketing/',
  '/die-bedeutung-der-e-mail-personalisierung': '/e-mail-personalisierung-wie-du-deine-kunden-wirklich-erreichst/',
  '/was-du-ueber-personalisierte-e-mails-wissen-musst': '/e-mail-personalisierung-wie-du-deine-kunden-wirklich-erreichst/',
  '/warum-du-eine-pillar-page-auf-deiner-webseite-brauchst': '/effektive-inhalte-mit-pillar-seiten/',
  '/kotters-8-schritte-modell-zur-steuerung-der-marketingveraenderungen': '/kotters-8-stufen-modell/',
  '/kurt-lewins-phasenmodell': '/lewins-3-stufen-modell/',
  '/zeitfresser-meeting-und-9-gegenmassnahmen': '/tipps-fuer-effektive-meetings/',
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
