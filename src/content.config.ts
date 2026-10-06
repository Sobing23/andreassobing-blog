// Inhaltsdefinition: Beiträge und Seiten als Markdown-Dateien
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const RUBRIKEN = ['marketing', 'strategie', 'email-marketing', 'marke', 'psychologie', 'ki-tools', 'arbeitsweisen', 'fundstuecke'] as const;

const posts = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    seoTitle: z.string().optional(),
    slug: z.string(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    description: z.string().optional(),
    image: z.string().optional(),
    category: z.enum(RUBRIKEN),
    tags: z.array(z.string()).default([]),
    vgwort: z.string().url().optional(),
    wpId: z.number().optional(),
    draft: z.boolean().default(false),
  }),
});

const pages = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/pages' }),
  schema: z.object({
    title: z.string(),
    seoTitle: z.string().optional(),
    slug: z.string(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    description: z.string().optional(),
    image: z.string().optional(),
    vgwort: z.string().url().optional(),
    wpId: z.number().optional(),
  }),
});

export const collections = { posts, pages };
