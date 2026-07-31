import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

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
