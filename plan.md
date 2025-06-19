# Technical Improvement Plan

This document outlines the strategic plan to improve the technical quality, maintainability, and performance of the CTI Website. The plan is divided into four priorities, from foundational build corrections to final polishing.

## Priority 1: Fix Build Configuration & Dependencies

**Goal:** Correct the foundational setup of the project to align with modern best practices and Astro standards. This is a critical first step to ensure a stable and correct development environment.

- **Correct Tailwind CSS Integration:** Switch from the non-standard Vite plugin to the official `@astrojs/tailwind` integration.
- **Correct Dependency Types:** Separate production dependencies from development dependencies in `package.json`.

## Priority 2: Improve Content Management & Maintainability

**Goal:** Decouple content from presentation by moving hardcoded page content into Astro's content collections. This will make the site significantly easier to update and manage.

- **Implement Astro Content Collections:** Define schemas and create Markdown files for instructors and other content types.
- **Refactor Pages:** Update the Astro pages to dynamically render content from the new collections.

## Priority 3: Enhance Accessibility & Component Design

**Goal:** Ensure the website is accessible to all users and improve the reusability of components.

- **Make Navigation Accessible:** Re-implement interactive elements like dropdowns and mobile menus to follow accessibility best practices (ARIA).
- **Improve Component Reusability:** Refactor components like `CTAButton` to be more flexible and create new reusable components for repeated sections like "Other Instructors".

## Priority 4: Final Polish (SEO & Visuals)

**Goal:** Complete the project improvements by addressing SEO and visual details.

- **Improve SEO:** Add missing meta tags for canonical URLs and social media sharing.
- **Replace Placeholder Images:** Add final, high-quality images throughout the site.