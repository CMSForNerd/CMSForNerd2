import { defineCollection, z } from 'astro:content';

const pagesCollection = defineCollection({
  type: 'content',
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
