# Index3 Landing Page Specifications
## High-Converting CTI Landing Page Architecture

### Overview
Index3 will be a streamlined, high-converting landing page that combines the best elements from:
- Current index.astro (clean conversion focus)
- index2.astro (stats-first approach, story-driven instructors)
- cti-astro vlander (video assets, comprehensive testimonials)
- Reference materials (proven copy, social proof)

### Core Principles
1. **Single Focus**: Drive visitors to digital.claytargetinstruction.com
2. **Fast Implementation**: Ship today, iterate tomorrow
3. **Mobile-First**: Optimized for all devices
4. **A/B Test Ready**: Modular sections for easy testing
5. **Asset Rich**: Leverage existing videos and images

---

## Page Architecture

### 1. Hero Section
**Goal**: Immediate credibility + clear value proposition

**Structure**:
```
[Stats Ticker Bar]
- Scrolling achievements: "31 World Titles: George Digweed • 2024 FITASC Champion: Zachary Kienbaum • First American World Champion: Anthony Matarese Jr."

[Main Hero]
- Background: Video (Breaking_Clays_Animation_Hero.mp4) with overlay
- Headline: "Three Living Legends. One Proven System."
- Subheadline: "Learn the exact methods that won 36+ world championships"
- Three instructor portraits (circular, small)
- Primary CTA: "Start Learning From Champions →"
- Trust indicators: "5,000+ Students • 4.9★ Average Rating"
```

**Copy Options to Test**:
- "Learn From the World's Most Decorated Shooters"
- "Break More Targets. Win More Events."
- "Every Shooter Has a Next Level. This Is Yours."

### 2. Proof Section
**Goal**: Establish authority quickly

**Structure**:
```
[3-Column Grid]
- Anthony: "Youngest Hall of Fame Inductee" + achievement
- George: "31 World Championships" + achievement  
- Zachary: "2024 World Champion" + achievement
- Each links to their bio page
```

### 3. Video Introduction
**Goal**: Personal connection + demonstrate value

**Structure**:
```
[Centered Video Player]
- Headline: "See Why Champions Choose Our Methods"
- Video: intro.mp4 or hero-video.mp4
- Caption: "Watch how our patented technology reveals champion secrets"
```

### 4. Instructor Spotlight
**Goal**: Build trust through personal stories

**Structure**:
```
[Carousel or Grid - Mobile Responsive]
For each instructor:
- Hero image
- Name + Primary achievement
- Key philosophy quote
- 2-3 bullet points of credentials
- Individual CTA: "Learn From [Name] →"
```

**Content from Research**:
- Anthony: "Build champions through structure, not superstition"
- George: "See the target. Trust the eyes. Let it happen"
- Zachary: "Turns mechanics into confidence and confidence into consistency"

### 5. Social Proof
**Goal**: Overcome objections with peer validation

**Structure**:
```
[Testimonial Slider]
- 6-8 testimonials rotating
- Name, Class Level, Score Improvement
- Mix of outcome types (scores, confidence, technique)
```

**Pull from CSV**:
- "Gained 8 points on my average in 6 months" - Kyle M., B Class
- "Best money I have ever spent... My scores improved dramatically" - Bobby M.
- "Went from D to A class faster than any other coach" - R. Ralph P.

### 6. Course Preview
**Goal**: Show value without giving away farm

**Structure**:
```
[Simple 3-Column]
- Foundation Courses: "Master the fundamentals" + image
- Advanced Courses: "Break through plateaus" + image
- All Access Bundle: "Complete championship system" + image + "BEST VALUE" badge
```

### 7. Final CTA
**Goal**: Create urgency without being pushy

**Structure**:
```
[Full-Width Section]
- Headline: "Your Competition Is Already Training"
- Subheadline: "Join 5,000+ shooters improving their game with champion instruction"
- Primary CTA: "Choose Your Instructor →"
- Secondary link: "See All Course Options"
- Trust badges: ShopperApproved logo + "Secure Checkout"
```

---

## Technical Specifications

### Components Needed
1. **HeroVideo.astro** - Background video with overlay
2. **StatsTicker.astro** - Scrolling achievement bar
3. **InstructorSpotlight.astro** - Reusable instructor card
4. **TestimonialSlider.astro** - Rotating testimonials
5. **CoursePreview.astro** - Simple course cards
6. **TrustBadges.astro** - Security/rating indicators

### Assets to Migrate
**From cti-astro**:
- Breaking_Clays_Animation_Hero.mp4
- intro.mp4 or hero-video.mp4
- ShopperApprovedLogo.svg
- Course bundle images

**Already in cti-website**:
- Instructor hero images
- CTI logos
- Existing components (CTAButton, PageHeadline)

### Tracking Implementation
```javascript
// All CTAs should include:
{
  trackingId: 'index3_[section]_[action]',
  authorId: '[instructor_id]' // when applicable
}
```

### Performance Targets
- Page load: <3 seconds
- Video lazy load after hero
- Image optimization (WebP with fallbacks)
- Above-fold content priority

---

## A/B Testing Strategy

### Test Variations
1. **Headlines**
   - Version A: "Three Living Legends. One Proven System."
   - Version B: "Learn From World Champions. Shoot Like One."
   - Version C: "Break More Targets. Win More Events."

2. **Video Placement**
   - Version A: After proof section
   - Version B: In hero background
   - Version C: Replace instructor spotlight

3. **CTA Text**
   - Version A: "Start Learning From Champions"
   - Version B: "Choose Your Instructor"
   - Version C: "See Course Options"

4. **Social Proof**
   - Version A: Testimonial slider
   - Version B: Static grid with ratings
   - Version C: Video testimonials

### Success Metrics
- Primary: Click-through to digital.claytargetinstruction.com
- Secondary: Time on page, scroll depth
- Tertiary: Instructor bio page visits

---

## Content Priorities

### Must Have (Ship Today)
1. Strong hero with video background
2. Three instructor cards with CTAs
3. 5-6 testimonials
4. Clear final CTA
5. Mobile responsive

### Nice to Have (Phase 2)
1. Stats ticker
2. Course preview section
3. FAQ section
4. Exit intent popup
5. Countdown timer for bundles

### Future Iterations
1. Personalization by traffic source
2. Geographic targeting
3. Retargeting variations
4. Seasonal promotions
5. Live chat integration

---

## Copy Bank

### Headlines
- "Three Living Legends. One Proven System."
- "Learn From the World's Most Decorated Shooters"
- "36+ World Championships. One Platform."
- "The Champions' Secret Is No Longer Secret"
- "World-Class Instruction. World-Class Results."

### Subheadlines
- "Join 5,000+ shooters already training with champions"
- "Proven methods that built the greatest careers in clay shooting"
- "Stop guessing. Start learning from those who've already won."
- "The difference between good and great is the right coach"

### CTAs
- Primary: "Start Learning From Champions →"
- Secondary: "Choose Your Instructor"
- Tertiary: "Explore Course Options"
- Urgent: "Join 5,000+ Students Today"

### Trust Elements
- "90+ Years Combined Experience"
- "36+ World Championships"
- "5,000+ Students Worldwide"
- "4.9★ Average Student Rating"
- "Lifetime Access Guarantee"
- "Secure Checkout via Teachable"

---

## Implementation Checklist

### Phase 1 (Today)
- [ ] Create index3.astro based on BaseLayout
- [ ] Migrate video assets from cti-astro
- [ ] Build HeroVideo component
- [ ] Create InstructorSpotlight cards
- [ ] Add TestimonialSlider with CSV data
- [ ] Implement tracking on all CTAs
- [ ] Test mobile responsiveness
- [ ] Optimize images and videos

### Phase 2 (This Week)
- [ ] Add stats ticker
- [ ] Create course preview section
- [ ] Implement A/B testing framework
- [ ] Add analytics events
- [ ] Create variation components
- [ ] Set up heatmap tracking

### Phase 3 (Next Sprint)
- [ ] FAQ integration
- [ ] Exit intent functionality
- [ ] Advanced personalization
- [ ] Performance optimization
- [ ] Schema markup enhancement
- [ ] Social proof widgets

---

## Notes for Development

1. **Component Reuse**: Leverage existing CTAButton and PageHeadline components
2. **Style Consistency**: Use existing CSS variables from global.css
3. **Image Strategy**: Use existing instructor images, add course images from cti-astro
4. **Video Loading**: Implement lazy loading for below-fold videos
5. **Fallbacks**: Ensure graceful degradation if video doesn't load
6. **Testing**: Create easily toggleable feature flags for A/B tests