import { defineCollection, z } from 'astro:content';

const instructors = defineCollection({
  type: 'content',
  schema: z.object({
    name: z.string(),
    title: z.string(),
    bio: z.string(),
    achievements: z.array(z.string()),
    order: z.number(),
  }),
});

export const collections = {
  instructors,
};