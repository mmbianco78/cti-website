# Theming Implementation Plan

This plan outlines the steps to integrate the new brand theme from the style guide into the Astro and Tailwind CSS project.

## Phase 1: Setup and Configuration (The Foundation)

This phase establishes the core theme settings.

1.  **Create Tailwind Configuration File:**
    *   A new file, `tailwind.config.mjs`, will be created in the project root. This file will define the custom theme.

2.  **Define CSS Custom Properties and Import Fonts:**
    *   The color palette from the style guide will be added to `src/styles/global.css` as CSS custom properties under the `:root` selector.
    *   The Google Fonts (Poppins and Inter) will be imported in `src/layouts/BaseLayout.astro`.
    *   The base background and text colors will be applied to the `body` in `src/styles/global.css` to set the default dark theme.

3.  **Extend Tailwind Theme:**
    *   The `tailwind.config.mjs` file will be configured to extend the default theme.
    *   **Colors:** The CSS custom properties will be mapped to Tailwind's color palette (e.g., `primary: 'var(--color-primary)'`).
    *   **Fonts:** The font families will be added to the `fontFamily` theme object: `sans` will be `Inter`, and a new `heading` font will be `Poppins`.
    *   **Content Path:** The `content` array will be configured to scan all `.astro`, `.md`, and `.html` files for Tailwind classes.

## Phase 2: Component and Layout Refactoring

In this phase, we will apply the new theme to the existing components.

1.  **Update Base Layout:**
    *   Modify `src/layouts/BaseLayout.astro` to import the Google Fonts.
    *   Apply the `font-sans` class to the `body` to set the default font to Inter.

2.  **Refactor Core Components:**
    *   **Navigation (`src/components/Navigation.astro`):** Update links, buttons, and background to use the new theme colors.
    *   **Buttons (`src/components/CTAButton.astro`):** Refactor this component to match the `primary` and `secondary` button styles defined in the style guide.
    *   **Footer (`src/components/Footer.astro`):** Apply the new background and text colors.

3.  **Update Page Content:**
    *   Review and update the content pages in `src/pages/` to ensure headings use `font-heading` (Poppins) and body text uses `font-sans` (Inter). This includes files like `src/pages/index.astro` and `src/pages/about.astro`.

## Workflow Diagram

```mermaid
graph TD
    subgraph Phase 1: Configuration
        A[Create tailwind.config.mjs] --> B{Define CSS Variables & Import Fonts};
        B --> C{Extend Tailwind Theme};
    end

    subgraph Phase 2: Refactoring
        D[Update BaseLayout.astro] --> E[Refactor Core Components];
        E --> F[Update Page Content];
    end

    subgraph Phase 3: Verification
        G[Review Site for Consistency] --> H[Final Polish];
    end

    C --> D;
    F --> G;