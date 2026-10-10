// Gemeinsame Helfer: Rubriken, Datumsformat, Lesezeit, Anrisstext, ähnliche Artikel
import { getCollection, type CollectionEntry } from 'astro:content';

export type Post = CollectionEntry<'posts'>;

export const RUBRIKEN = [
  { key: 'marketing', name: 'Marketing & Wachstum', kurz: 'Marketing' },
  { key: 'strategie', name: 'Strategie & Führung', kurz: 'Strategie' },
  { key: 'email-marketing', name: 'E-Mail-Marketing', kurz: 'E-Mail' },
  { key: 'marke', name: 'Marke & Positionierung', kurz: 'Marke' },
  { key: 'psychologie', name: 'Psychologie & Verkauf', kurz: 'Psychologie' },
  { key: 'ki-tools', name: 'KI & Tools', kurz: 'KI & Tools' },
  { key: 'arbeitsweisen', name: 'Arbeitsweisen & Produktivität', kurz: 'Arbeitsweisen' },
  { key: 'fundstuecke', name: 'Fundstücke', kurz: 'Fundstücke' },
] as const;

export const rubrik = (key: string) => RUBRIKEN.find((r) => r.key === key)!;
export const rubrikUrl = (key: string) => `/rubrik/${key}/`;
export const postUrl = (p: Post) => `/${p.data.slug}/`;

export const tagSlug = (tag: string) =>
  tag
    .toLowerCase()
    .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
    .replace(/&/g, 'und')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
export const tagUrl = (tag: string) => `/schlagwort/${tagSlug(tag)}/`;

const fmt = new Intl.DateTimeFormat('de-DE', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Europe/Berlin' });
export const datum = (d: Date) => fmt.format(d);

/** Lesezeit in Minuten (200 Wörter pro Minute, mindestens 1). */
export function lesezeit(body = ''): number {
  const text = body.replace(/<[^>]+>/g, ' ').replace(/!\[[^\]]*\]\([^)]*\)/g, ' ').replace(/\]\([^)]*\)/g, ']');
  const words = (text.match(/[\p{L}\p{N}]+/gu) || []).length;
  return Math.max(1, Math.round(words / 200));
}

/** Klartext aus Markdown für Anrisstexte. */
function klartext(body = ''): string {
  return body
    .replace(/<[^>]+>/g, ' ')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/^#+\s.*$/gm, ' ')
    .replace(/[*_>`#|]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Meta-Beschreibung, sonst die ersten Sätze des Textes (max. ~160 Zeichen). */
export function anriss(p: { data: { description?: string }; body?: string }, max = 160): string {
  if (p.data.description) return p.data.description;
  const text = klartext(p.body);
  if (text.length <= max) return text;
  const cut = text.slice(0, max);
  const satz = cut.lastIndexOf('. ');
  return satz > 60 ? cut.slice(0, satz + 1) : cut.replace(/\s\S*$/, '') + ' …';
}

let cache: Post[] | null = null;
/** Alle veröffentlichten Beiträge, neueste zuerst. */
export async function allePosts(): Promise<Post[]> {
  if (!cache) {
    cache = (await getCollection('posts', (p) => !p.data.draft)).sort(
      (a, b) => b.data.date.getTime() - a.data.date.getTime(),
    );
  }
  return cache;
}

/** Ähnliche Artikel: gleiche Rubrik, gemeinsame Schlagwörter und Titelwörter, zeitliche Nähe. */
export async function aehnliche(p: Post, anzahl = 3): Promise<Post[]> {
  const posts = await allePosts();
  const woerter = (s: string) => new Set(s.toLowerCase().match(/[\p{L}]{5,}/gu) || []);
  const eigene = woerter(p.data.title);
  const scored = posts
    .filter((o) => o.id !== p.id)
    .map((o) => {
      let s = 0;
      if (o.data.category === p.data.category) s += 3;
      s += o.data.tags.filter((t) => p.data.tags.includes(t)).length * 2;
      for (const w of woerter(o.data.title)) if (eigene.has(w)) s += 2;
      const jahre = Math.abs(o.data.date.getTime() - p.data.date.getTime()) / 3.15e10;
      s -= Math.min(jahre, 5) * 0.3;
      return { o, s };
    })
    .sort((a, b) => b.s - a.s);
  return scored.slice(0, anzahl).map((x) => x.o);
}

// Themenseiten (Cluster): Übersichtsseite je Thema, Artikel nach Abschnitten
import themenDaten from '../data/themen.json';
export type Thema = (typeof themenDaten)[number];
export const THEMEN: Thema[] = themenDaten;
export const themaUrl = (key: string) => `/thema/${key}/`;
/** Thema und Abschnitt, zu dem ein Artikel gehört (oder undefined) */
export function themaFuer(slug: string) {
  for (const t of THEMEN) {
    const abschnitt = t.abschnitte.find((a) => a.artikel.includes(slug));
    if (abschnitt) return { thema: t, abschnitt, anzahl: t.abschnitte.reduce((n, a) => n + a.artikel.length, 0) };
  }
  return undefined;
}

// Handbuch: Reihenfolge der Kapitel (Teile aus handbuch.json), Kapitelnummer je Thema
import handbuchDaten from '../data/handbuch.json';
export const HANDBUCH = handbuchDaten;
export const KAPITEL_REIHENFOLGE: string[] = [
  ...handbuchDaten.teile.flatMap((t) => t.kapitel),
  ...THEMEN.map((t) => t.key).filter((k) => !handbuchDaten.teile.some((t) => t.kapitel.includes(k))),
];
export const kapitelNummer = (key: string) => KAPITEL_REIHENFOLGE.indexOf(key) + 1;
export const HANDBUCH_URL = '/handbuch/';
/** Einfache Inline-Links [Text](/pfad/) in sonst reinem Text, HTML wird escaped */
export const mitLinks = (t: string) =>
  t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
   .replace(/\[([^\]]+)\]\((\/[a-z0-9\/-]*)\)/g, '<a href="$2">$1</a>');
