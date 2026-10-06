// Astro-Konfiguration für andreassobing.de
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import externeLinks from './src/lib/externe-links.mjs';

export default defineConfig({
  site: 'https://andreassobing.de',
  trailingSlash: 'always',
  build: { format: 'directory' },
  integrations: [sitemap({ filter: (page) => !page.includes('/suche/') }), externeLinks()],
  // Alte WordPress-Adressen, die es so nicht mehr gibt
  redirects: {
    '/glossar': '/das-grosse-marketing-glossar-die-wichtigsten-begriffe-einfach-erklaert/',
    '/feed': '/rss.xml',
    '/cookie-richtlinie-eu': '/datenschutz/',
    '/author/sobing': '/',
    '/category/unkategorisiert': '/archiv/',
  },
});
