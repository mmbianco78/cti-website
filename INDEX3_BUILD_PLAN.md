# Index3 Build & Site-Wide Update Plan

## Phase 1: Index3 Development (Day 1)

### 1.1 Asset Migration (30 min)
```bash
# Copy video assets from cti-astro to cti-website
cp /cti-astro/public/assets/video/Breaking_Clays_Animation_Hero.mp4 → /cti-website/public/assets/video/
cp /cti-astro/public/assets/video/anthony-matarese-promo.mp4 → /cti-website/public/assets/video/
cp /cti-astro/public/assets/video/zachary-kienbaum-promo.mp4 → /cti-website/public/assets/video/
cp /cti-astro/public/assets/video/intro.mp4 → /cti-website/public/assets/video/

# Copy any missing images
cp /cti-astro/public/assets/images/ShopperApprovedLogo.svg → /cti-website/public/assets/images/
```

### 1.2 Component Creation (2 hours)
Create new components in `/src/components/`:

```
1. HeroVideo.astro
   - Video background with overlay
   - Responsive fallback to static image
   - Performance optimized loading

2. StatsTicker.astro  
   - Scrolling achievement bar
   - Mobile responsive behavior
   - Smooth animations

3. TestimonialRotator.astro
   - Categorized testimonials
   - Auto-rotation with pause on hover
   - Manual navigation dots

4. InstructorVideoCard.astro
   - Video thumbnail with play button
   - Modal or inline player
   - Fallback for slow connections

5. TrustBadges.astro
   - ShopperApproved widget
   - Security badges
   - Rating display

6. LiveSocialProof.astro
   - Student counter
   - Recent activity feed
   - Animated updates
```

### 1.3 Page Development (2 hours)
Create `/src/pages/index3.astro`:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import HeroVideo from '../components/HeroVideo.astro';
import StatsTicker from '../components/StatsTicker.astro';
import TestimonialRotator from '../components/TestimonialRotator.astro';
import InstructorVideoCard from '../components/InstructorVideoCard.astro';
import TrustBadges from '../components/TrustBadges.astro';
import LiveSocialProof from '../components/LiveSocialProof.astro';
import CTAButton from '../components/CTAButton.astro';

// Import testimonial data
import testimonials from '../data/testimonials.json';
---

<BaseLayout title="Learn From World Champions | Clay Target Instruction">
  <!-- Implementation following our spec -->
</BaseLayout>
```

### 1.4 Data Setup (30 min)
Create `/src/data/testimonials.json`:
```json
{
  "anthony": [
    {
      "text": "I gained 8 points on my average in 6 months",
      "author": "Kyle M.",
      "class": "B Class",
      "category": "improvement"
    }
    // ... all testimonials
  ],
  "george": [...],
  "zachary": [...],
  "platform": [...]
}
```

---

## Phase 2: Review & Iteration Process (Day 1-2)

### 2.1 Self Review Checklist
```
Desktop (1920x1080):
□ Hero video loads and plays smoothly
□ Stats ticker animates properly
□ All CTAs are prominent and trackable
□ Testimonials rotate smoothly
□ Instructor videos load on demand
□ Trust badges display correctly

Tablet (768px):
□ Layout stacks appropriately
□ Videos still functional
□ Touch targets are 48px+
□ Readable without zooming

Mobile (375px):
□ Hero simplifies correctly
□ Video has play button (no autoplay)
□ Testimonials are swipeable
□ CTAs are full width
□ Page loads under 3 seconds
```

### 2.2 Stakeholder Review Process
1. **Deploy to staging**: `/index3-preview`
2. **Share review link** with tracking enabled
3. **Collect feedback** via structured form:
   - First impression (1-10)
   - Clarity of message
   - Desire to click CTA
   - Any confusion points
   - Technical issues

### 2.3 A/B Test Setup
```javascript
// Simple A/B test framework
const variants = {
  headline: [
    "3 World Champions. One Revolutionary Platform.",
    "See Exactly How World Champions Break Every Target",
    "36+ Championships Worth of Secrets. Now Yours."
  ],
  cta: [
    "Watch How Champions Really Shoot →",
    "Start Learning From Champions →",
    "See The Champion Difference →"
  ]
};
```

### 2.4 Performance Review
- Run Lighthouse audit
- Test on slow 3G
- Check video loading times
- Verify tracking pixels fire
- Test all CTAs to destination

---

## Phase 3: Site-Wide Updates (Day 2-3)

### 3.1 Design System Updates
Create `/src/styles/design-system.css`:
```css
:root {
  /* Updated based on index3 success */
  --hero-height: 100vh;
  --video-overlay: rgba(0, 0, 0, 0.4);
  --cta-style: bold with arrow;
  --testimonial-style: rotating cards;
  --trust-badge-position: above-fold;
}
```

### 3.2 Page Update Priority

#### High Priority (Day 2)
1. **Homepage (index.astro)**
   - Add video hero option
   - Include testimonial rotator
   - Add trust badges above fold
   - Update CTAs to match style

2. **Instructor Pages**
   - Add video preview for each
   - Include instructor-specific testimonials
   - Update hero to match index3 style
   - Add "other instructors" video cards

#### Medium Priority (Day 3)
3. **About Page**
   - Add platform statistics section
   - Include combined testimonials
   - Update imagery to be more dynamic
   - Add video compilation

4. **Contact Page**
   - Add testimonials for trust
   - Include instructor video messages
   - Update form styling to match

5. **FAQ Page**
   - Add video answers where applicable
   - Include relevant testimonials
   - Update layout to match new style

#### Low Priority (Week 2)
6. **Article Pages**
   - Update typography to match
   - Add author video previews
   - Include related testimonials
   - Update CTA styling

7. **Legal Pages**
   - Update header/footer only
   - Maintain simple layout
   - Ensure consistent navigation

### 3.3 Component Updates

#### Update Existing Components:
```
1. Navigation.astro
   - Add subtle animation on scroll
   - Include trust indicators (rating)
   - Mobile menu improvements

2. Footer.astro
   - Add testimonial ticker
   - Include trust badges
   - Update social links

3. CTAButton.astro
   - New arrow animation
   - Consistent styling across site
   - Better mobile tap targets
```

#### Create Shared Components:
```
1. VideoPlayer.astro
   - Consistent player across site
   - Lazy loading built in
   - Mobile optimizations

2. TestimonialCard.astro
   - Reusable testimonial display
   - Multiple layout options
   - Author attribution

3. StatsDisplay.astro
   - Animated number counters
   - Responsive grid layout
   - Icon support
```

---

## Phase 4: Quality Assurance (Day 3-4)

### 4.1 Technical QA
```
□ All pages load under 3 seconds
□ Videos play on all devices
□ Forms submit correctly
□ Analytics tracking works
□ No console errors
□ SEO meta tags updated
□ Sitemap includes new pages
□ 404 page styled consistently
```

### 4.2 Content QA
```
□ All testimonials attributed correctly
□ Instructor info consistent across pages
□ CTAs lead to correct destinations
□ Trust badges display properly
□ Videos have proper alt text
□ Copy is spell-checked
□ Legal links work
□ Contact info is current
```

### 4.3 Cross-Browser Testing
- Chrome (latest)
- Safari (latest)
- Firefox (latest)
- Edge (latest)
- iOS Safari
- Chrome Android

### 4.4 Performance Benchmarks
Target metrics:
- First Contentful Paint: <1.5s
- Largest Contentful Paint: <2.5s
- Time to Interactive: <3.5s
- Cumulative Layout Shift: <0.1
- Lighthouse Score: 90+

---

## Phase 5: Launch & Monitor (Day 4-5)

### 5.1 Soft Launch
1. Deploy index3 as new homepage
2. Keep index.astro as `/index-old`
3. Monitor analytics for 24 hours
4. Check error logs
5. Monitor conversion rates

### 5.2 Success Metrics
Track hourly for first 24 hours:
- Bounce rate (target: <50%)
- Click-through rate (target: >15%)
- Video engagement (target: >30% completion)
- Scroll depth (target: >60% reach bottom)
- Conversion to digital platform

### 5.3 Quick Fixes
If metrics are below target:
1. **Hour 1-4**: Fix any breaking issues
2. **Hour 4-8**: Adjust hero headline
3. **Hour 8-24**: Modify CTA placement
4. **Day 2**: Test testimonial variations
5. **Day 3**: Try different video

### 5.4 Full Site Rollout
Once index3 proves successful:
1. Update all pages with new components
2. Roll out in phases (high traffic first)
3. Monitor each page's performance
4. Document what's working
5. Create template for future pages

---

## Implementation Timeline

### Day 1 (8 hours)
- Morning: Asset migration & component creation
- Afternoon: Build index3 page
- Evening: Internal testing & fixes

### Day 2 (6 hours)
- Morning: Stakeholder review
- Afternoon: Implement feedback
- Evening: Update high-priority pages

### Day 3 (6 hours)
- Morning: Continue page updates
- Afternoon: QA testing
- Evening: Performance optimization

### Day 4 (4 hours)
- Morning: Final testing
- Afternoon: Soft launch
- Evening: Monitor metrics

### Day 5 (4 hours)
- Morning: Analyze data
- Afternoon: Quick optimizations
- Evening: Plan full rollout

---

## Risk Mitigation

### Backup Plans:
1. **If video kills performance**: Static image with animation
2. **If testimonials seem fake**: Add video testimonials
3. **If CTR is low**: Test urgency messaging
4. **If mobile breaks**: Simplified mobile version
5. **If stakeholders hate it**: A/B test against current

### Rollback Strategy:
- Keep all original files
- One-click rollback ready
- Monitor for 48 hours
- Document lessons learned
- Iterate based on data

---

## Long-term Maintenance

### Weekly Tasks:
- Update testimonial rotation
- Check video performance
- Monitor conversion trends
- Test new headlines
- Update student counts

### Monthly Tasks:
- Add new testimonials
- Update instructor content
- Refresh video content
- Analyze user recordings
- Plan new tests

### Quarterly Tasks:
- Major design updates
- New component development
- Platform feature integration
- Competitive analysis
- Strategic planning

This plan ensures systematic implementation, thorough testing, and data-driven iteration while maintaining the ability to quickly adjust based on performance.