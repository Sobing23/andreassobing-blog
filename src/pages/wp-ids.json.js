// Zuordnung alte WordPress-ID -> neue Adresse (für Links der Form /?p=123)
import { getCollection } from 'astro:content';
export async function GET() {
  const map = {};
  for (const c of ['posts', 'pages']) for (const e of await getCollection(c)) if (e.data.wpId) map[e.data.wpId] = `/${e.data.slug === 'index' ? '' : e.data.slug + '/'}`;
  return new Response(JSON.stringify(map), { headers: { 'Content-Type': 'application/json' } });
}
