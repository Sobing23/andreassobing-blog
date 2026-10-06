// RSS-Feed mit den 50 neuesten Artikeln
import rss from '@astrojs/rss';
import { allePosts, anriss, postUrl } from '../lib/blog';

export async function GET(context) {
  const posts = (await allePosts()).slice(0, 50);
  return rss({
    title: 'Blog it Marketing',
    description: 'Mein digitales Notizbuch rund um Marketing, Strategie und Führung.',
    site: context.site,
    items: posts.map((p) => ({ title: p.data.title, pubDate: p.data.date, description: anriss(p, 300), link: postUrl(p) })),
    customData: '<language>de-de</language>',
  });
}
