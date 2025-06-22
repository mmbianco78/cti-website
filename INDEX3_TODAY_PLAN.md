# Index3 - Ship Today Plan

## Next 2 Hours: Build & Launch

### Hour 1: Core Setup (60 min)

#### 1. Quick Asset Copy (10 min)
```bash
# Create video directory if needed
mkdir -p public/assets/video

# Copy critical videos only
cp ../cti-astro/public/assets/video/Breaking_Clays_Animation_Hero.mp4 public/assets/video/
cp ../cti-astro/public/assets/video/intro.mp4 public/assets/video/

# Copy ShopperApproved logo
cp ../cti-astro/public/assets/images/ShopperApprovedLogo.svg public/assets/images/
```

#### 2. Create index3.astro (30 min)
Start with copying index2.astro and modify:
```bash
cp src/pages/index2.astro src/pages/index3.astro
```

Focus on:
- Replace hero with video background
- Add testimonials section (hardcode for now)
- Update headlines to our winning copy
- Add trust badges

#### 3. Quick Components (20 min)
Create only what's ESSENTIAL:

**HeroVideo.astro** - Simple video background
```astro
<div class="hero-video">
  <video autoplay muted loop playsinline poster="/assets/images/zachary-kienbaum_instructor_hero_desktop.jpg">
    <source src="/assets/video/Breaking_Clays_Animation_Hero.mp4" type="video/mp4">
  </video>
  <div class="hero-overlay">
    <slot />
  </div>
</div>

<style>
  .hero-video { position: relative; height: 100vh; overflow: hidden; }
  video { position: absolute; top: 50%; left: 50%; min-width: 100%; min-height: 100%; transform: translate(-50%, -50%); }
  .hero-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center; }
</style>
```

**TestimonialSection.astro** - Hardcode our best ones
```astro
<section class="testimonials">
  <h2>Join 5,000+ Shooters Already Improving</h2>
  <div class="testimonial-grid">
    <!-- Hardcode 6 best testimonials -->
  </div>
</section>
```

### Hour 2: Polish & Deploy (60 min)

#### 1. Critical CSS Only (20 min)
Add to global.css:
- Video hero styles
- Testimonial cards
- Mobile fixes for video
- Trust badge positioning

#### 2. Mobile Check (20 min)
- Test on phone browser
- Ensure video doesn't autoplay on mobile
- Check CTA tap targets
- Verify testimonials are readable

#### 3. Deploy (20 min)
```bash
# Quick test
npm run build
npm run preview

# If good, deploy
git add .
git commit -m "Add index3 high-converting landing page"
git push

# Deploy to production
```

---

## What We're Building (Simplified)

### Section 1: Video Hero
```
[Video Background - Breaking_Clays_Animation_Hero.mp4]
"3 World Champions. One Revolutionary Platform."
[3 instructor photos]
[CTA: "Watch How Champions Really Shoot →"]
```

### Section 2: Instant Credibility
```
🏆 36+ World Championships
⭐ 4.9/5 from 500+ Reviews
👥 5,000+ Active Students
```

### Section 3: Testimonials (Hardcoded)
```
"I gained 8 points in 6 months" - Kyle M.
"Best money I ever spent" - Bobby M.
"D to A class in one season" - Ralph P.
"Finally understand teal targets" - Forum User
"Seeing where George looks changed everything" - Mike T.
"My 10-year-old could follow" - Amy
```

### Section 4: Instructors (Reuse from index2)
- Keep the existing instructor cards
- Just update the CTAs to be consistent

### Section 5: Simple CTA
```
"Ready to Learn from the Best?"
[Start Training with Champions →]
✓ Instant access ✓ All devices ✓ Beginners welcome
```

---

## What We're NOT Doing Today

❌ No complex components
❌ No testimonial rotators  
❌ No live counters
❌ No A/B testing setup
❌ No instructor videos (just hero video)
❌ No fancy animations
❌ No perfect mobile optimization

---

## Quick Wins We CAN Do

✅ Strong video hero (huge impact)
✅ 6 powerful testimonials (we have them)
✅ Trust badges (just images)
✅ Clean, focused message
✅ Multiple CTAs
✅ Mobile functional (not perfect)

---

## Testing Checklist (30 min)

### Desktop
- [ ] Video plays
- [ ] Text is readable over video
- [ ] CTAs work
- [ ] Testimonials display

### Mobile  
- [ ] Video has poster image
- [ ] CTAs are tappable
- [ ] Page loads fast enough
- [ ] No horizontal scroll

### Critical Only
- [ ] All links go to digital.claytargetinstruction.com
- [ ] No console errors
- [ ] Page loads under 5 seconds

---

## If Something Breaks

1. **Video won't play**: Use poster image only
2. **Too slow**: Remove video, use static hero
3. **Mobile broken**: Hide complex sections on mobile
4. **Testimonials ugly**: Use simple quotes
5. **No time**: Just update index.astro hero

---

## Success = Shipped

A good page live today beats a perfect page next week. We can iterate tomorrow based on real data.

**Goal**: By end of today, index3 is live and driving traffic to the digital platform with:
- Video hero ✓
- Strong testimonials ✓  
- Clear CTAs ✓
- Trust elements ✓

Everything else is iteration.