# Styling Recommendations for CTI Website Pages

## Current State Analysis

### Index Page (New Design)
- **Typography**: 3rem for h2s, 800 font-weight, consistent sizing
- **Colors**: Dark/light alternating sections, orange/purple accents
- **Effects**: Glass-morphism, backdrop blur, gradient backgrounds
- **CTAs**: Using CTAButton component with arrows and pulse effects
- **Cards**: Rounded corners (16px), hover transforms, glass effects

### Instructor Pages (Anthony, George, Zach)
- **Issues**: 
  - Inconsistent with index design language
  - Using Tailwind classes vs styled components
  - Different heading sizes (4xl vs 3rem)
  - Missing glass-morphism effects
  - No consistent section backgrounds
  - Stats display different from index hero stats

### FAQ Page
- **Issues**:
  - Very basic styling
  - No visual hierarchy matching index
  - Missing dark/light section alternation
  - No glass effects or modern touches
  - Basic expand/collapse without smooth animations

### Articles Page
- **Issues**:
  - Minimal styling
  - Different CTA style than CTAButton component
  - No consistent section patterns
  - Missing visual interest

## Recommendations

### 1. Instructor Pages Updates

#### Hero Section
- Replace gradient background with dark video/image background like index
- Add glass-morphism stats bar similar to index hero
- Use consistent heading sizes (3rem for main)
- Add subtle glow to instructor name like index

#### Content Sections
- Implement dark/light alternating backgrounds
- Add glass-morphism to feature cards
- Use consistent padding (5rem vertical)
- Add radial gradient backgrounds for depth

#### CTAs
- Replace all CTAs with CTAButton component
- Add pulse effect to main CTA
- Ensure all use withArrow prop

#### Visual Enhancements
- Add backdrop blur effects
- Implement hover transforms on cards
- Use consistent border-radius (16px)
- Add subtle animations

### 2. FAQ Page Updates

#### Hero Section
- Add dark gradient background
- Center the headline
- Add visual interest with subtle gradients

#### FAQ Items
- Redesign with glass-morphism cards
- Add smooth expand/collapse animations
- Implement hover effects
- Use consistent spacing

#### Structure
- Group FAQs in glass containers
- Add icon indicators
- Improve typography hierarchy

### 3. Articles Page Updates

#### Layout
- Add hero section with dark background
- Implement card-based article display
- Add hover effects on article cards

#### CTAs
- Replace inline button with CTAButton
- Add consistent styling throughout

### 4. Global Consistency Items

#### Typography
```css
/* Headings */
h1: font-size: clamp(2.5rem, 5vw, 3.5rem); font-weight: 800;
h2: font-size: 3rem; font-weight: 800;
h3: font-size: 1.5rem; font-weight: 700;

/* Body */
p: font-size: 1.1rem; line-height: 1.6;
small: font-size: 0.9rem;
```

#### Colors
```css
/* Backgrounds */
Dark sections: linear-gradient(135deg, #0A0A0B 0%, #1A1A1C 100%)
Light sections: #f8f8f8 or #f5f5f5
Glass effects: rgba(30, 30, 30, 0.4) with backdrop-filter: blur(10px)

/* Text */
On dark: #FFFFFF (primary), #A0A0A0 (secondary)
On light: #111111 (primary), #666666 (secondary)
```

#### Spacing
```css
Section padding: 5rem 0
Container max-width: 1200px (grids), 1000px (content)
Card padding: 2.5rem
Grid gaps: 2rem
```

#### Effects
```css
/* Hover */
transform: translateY(-4px);
box-shadow: 0 10px 30px rgba(255, 102, 0, 0.2);

/* Glass */
background: rgba(30, 30, 30, 0.4);
backdrop-filter: blur(10px);
border: 1px solid rgba(255, 255, 255, 0.1);

/* Transitions */
transition: all 0.3s ease;
```

## Implementation Priority

1. **High Priority** (Brand consistency)
   - Update all CTAs to use CTAButton component
   - Implement consistent typography scale
   - Add dark/light section patterns

2. **Medium Priority** (Visual enhancement)
   - Add glass-morphism effects
   - Implement hover states
   - Update color usage

3. **Low Priority** (Polish)
   - Add animations
   - Enhance micro-interactions
   - Fine-tune responsive behavior

## Files to Update

1. `anthony-matarese-jr.astro`
2. `george-digweed.astro`
3. `zach-kienbaum.astro`
4. `faq.astro`
5. `articles/index.astro`
6. Components: `FAQSingle.astro`, `MinimalArticleCard.astro`

## Expected Impact

- **Consistency**: Unified design language across all pages
- **Modern Feel**: Glass-morphism and gradient effects throughout
- **Better UX**: Consistent interactions and visual feedback
- **Brand Strength**: Orange/purple theme reinforced everywhere
- **Performance**: No negative impact, mostly CSS changes