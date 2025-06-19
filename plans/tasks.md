# Technical Improvement Tasks

This file lists the specific, actionable tasks to be completed, ordered by priority. Check off items as they are completed.

### Priority 1: Fix Build Configuration & Dependencies
- [x] **Task 1.1:** ~~Uninstall `@tailwindcss/vite` plugin.~~ (Reverted)
- [x] **Task 1.2:** ~~Install `@astrojs/tailwind` integration.~~ (Reverted due to incompatibility with Tailwind CSS v4)
- [x] **Task 1.3:** Move `astro`, `tailwindcss`, and `@tailwindcss/vite` from `dependencies` to `devDependencies` in `package.json`.

### Priority 2: Enhance Accessibility & Component Design
- [x] **Task 2.1:** Refactor the `Navigation.astro` component to make the desktop dropdown keyboard-accessible.
- [x] **Task 2.2:** Refactor the `Navigation.astro` component to make the mobile menu accessible with ARIA attributes.
- [x] **Task 2.3:** Refactor the `CTAButton.astro` component to be more flexible with a `color` prop or similar.
- [x] **Task 2.4:** Create a reusable `OtherInstructors.astro` component.

### Priority 3: Final Polish (SEO & Visuals)
- [x] **Task 3.1:** Add a canonical URL link to `BaseLayout.astro`.
- [x] **Task 3.2:** Add `og:image` and `twitter:image` meta tags to `BaseLayout.astro`.
- [ ] **Task 3.3:** Replace all placeholder images with actual images. (User task)

### Priority 4: Additional Improvements
- [x] **Task 4.1:** Add a `Footer.astro` component.
- [x] **Task 4.2:** Add the footer to the `BaseLayout.astro`.
- [x] **Task 4.3:** Create a `/terms` page with placeholder content.
- [x] **Task 4.4:** Create a `/privacy` page with placeholder content.