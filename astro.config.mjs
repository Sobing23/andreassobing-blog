// Astro-Konfiguration für andreassobing.de
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://andreassobing.de',
  trailingSlash: 'always',
  build: { format: 'directory' },
  integrations: [sitemap({ filter: (page) => !page.includes('/suche/') })],
  // Alte WordPress-Adressen, die es so nicht mehr gibt
  redirects: {
    '/feed': '/rss.xml',
    '/cookie-richtlinie-eu': '/datenschutz/',
    '/author/sobing': '/',
    '/category/unkategorisiert': '/archiv/',
  },
});
