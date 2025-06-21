import { defineCollection, z } from 'astro:content';

const articles = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    image: z.string().optional(),
    author: z.string(),
    featured: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    category: z.enum(['technique', 'equipment', 'mental-game', 'competition', 'training']).default('technique'),
  }),
});

export const collections = { articles };