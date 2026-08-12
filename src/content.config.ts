/**
 * @file content.config.ts
 * @description Astro Content Collection configuration and schema validation definition.
 * Sets up the dynamic loading structure for transitioned flat-file Markdown pages.
 */

import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Defines the type-safe collection schema for migrated static pages.
 * Validates metadata, author information, SEO description, and schema properties.
 */
const pagesCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    schemaType: z.string().default('WebPage'),
    author: z.string().default('Harisfazillah Jamel')
  })
});

export const collections = {
  'pages': pagesCollection,
};
