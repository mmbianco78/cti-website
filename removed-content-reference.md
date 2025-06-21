# Removed Content Reference - CTI Website Index Page

This file contains all the content that was removed or replaced during the page restructuring on 2025-06-21.

## 1. Three Methods Section (Previously lines 513-582)

```astro
<!-- Three Methods Section -->
<section class="section-padding bg-surface">
  <div class="container-max">
    <div class="mb-16 text-center">
      <PageHeadline
        title="Three Champions. Three Proven Methods."
        subtitle="Each instructor brings their unique championship approach, giving you multiple paths to shooting excellence"
        showPill={true}
        pillText="PROVEN SYSTEMS"
        pillVariant="primary"
      />
    </div>
    
    <div class="methods-grid">
      <div class="method-card">
        <img src="/anthony-i-matarese-jr_instructor_hero_desktop.jpg" alt="Anthony Matarese Jr." class="method-instructor-img" />
        <h3>Anthony Matarese Jr.</h3>
        <div class="method-subtitle">The Structured System</div>
        <p class="method-description">Master Anthony's analytical approach that breaks down every shot into repeatable, measurable components</p>
        <ul class="method-features">
          <li>Step-by-step progression</li>
          <li>Data-driven improvement</li>
          <li>Consistent fundamentals</li>
        </ul>
      </div>
      
      <div class="method-card">
        <img src="/george_digweed_instructor_hero_desktop.jpg" alt="George Digweed MBE" class="method-instructor-img" />
        <h3>George Digweed MBE</h3>
        <div class="method-subtitle">The Instinctive Approach</div>
        <p class="method-description">Learn George's natural shooting style that emphasizes flow, rhythm, and subconscious execution</p>
        <ul class="method-features">
          <li>Visual smoothness</li>
          <li>Pressure management</li>
          <li>Championship mindset</li>
        </ul>
      </div>
      
      <div class="method-card">
        <img src="/zachary-kienbaum_instructor_hero_desktop.jpg" alt="Zachary Kienbaum" class="method-instructor-img" />
        <h3>Zachary Kienbaum</h3>
        <div class="method-subtitle">The Technical Precision</div>
        <p class="method-description">Perfect Zach's meticulous technique focusing on timing, tempo, and optimal equipment setup</p>
        <ul class="method-features">
          <li>Equipment optimization</li>
          <li>Precision timing</li>
          <li>Strategic planning</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

## 2. Learning Outcomes Subsection (Previously lines 240-264)

```astro
<div class="learning-outcomes-section mt-20">
  <h3 class="learning-title">What You'll Learn in Our Courses</h3>
  <div class="learning-grid">
    <div class="learning-item">
      <div class="learning-icon">🎯</div>
      <h4>Gun Mount & Hold Points</h4>
      <p>Master the fundamentals of consistent gun mounting and optimal hold point selection for every target presentation</p>
    </div>
    <div class="learning-item">
      <div class="learning-icon">👁️</div>
      <h4>Visual Focus & Target Reading</h4>
      <p>Develop champion-level visual skills to read targets faster and track them more accurately through their flight path</p>
    </div>
    <div class="learning-item">
      <div class="learning-icon">🧠</div>
      <h4>Mental Game & Competition Prep</h4>
      <p>Build unshakeable confidence with proven mental routines and pressure-management techniques from world champions</p>
    </div>
    <div class="learning-item">
      <div class="learning-icon">📊</div>
      <h4>Course Management & Strategy</h4>
      <p>Learn how to analyze stations, plan your approach, and execute consistently under competitive conditions</p>
    </div>
  </div>
</div>
```

## 3. Transformation Grid Subsection (Previously lines 266-293)

```astro
<div class="transformation-grid mt-16">
  <div class="transformation-card">
    <h4 class="transformation-title">Before CTI Training</h4>
    <ul class="transformation-list before">
      <li>Inconsistent results</li>
      <li>Wasted ammo and practice time</li>
      <li>Plateaued performance</li>
      <li>Confusion about what went wrong</li>
    </ul>
  </div>
  
  <div class="transformation-arrow">
    <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <line x1="5" y1="12" x2="19" y2="12"></line>
      <polyline points="12 5 19 12 12 19"></polyline>
    </svg>
  </div>
  
  <div class="transformation-card success">
    <h4 class="transformation-title">After CTI Training</h4>
    <ul class="transformation-list after">
      <li>Predictable, repeatable success</li>
      <li>Strategic confidence on every shot</li>
      <li>Championship-level knowledge</li>
      <li>Clear understanding of technique</li>
    </ul>
  </div>
</div>
```

## 4. Results Banner Subsection (Previously lines 295-313)

```astro
<div class="results-banner">
  <div class="results-content">
    <div class="results-stat">
      <span class="results-number">87%</span>
      <span class="results-label">of students see improvement in 30 days</span>
    </div>
    <div class="results-divider"></div>
    <div class="results-stat">
      <span class="results-number">4.9/5</span>
      <span class="results-label">average course rating</span>
    </div>
    <div class="results-divider"></div>
    <div class="results-stat">
      <span class="results-number">1,000+</span>
      <span class="results-label">positive reviews</span>
    </div>
  </div>
</div>
```

## 5. CTA Button After Video (Previously lines 348-358)

```astro
<div class="text-center mt-12">
  <CTAButton
    text="Start Your Journey"
    href="https://digital.claytargetinstruction.com"
    variant="primary"
    size="large"
    external={true}
    withArrow={true}
    usePulse={true}
  />
</div>
```

## 6. Original "Structured Learning for Every Level" Section

This was the section before we transformed it into the Learning Journey section with target rings:

```astro
<!-- Course Levels Section -->
<section class="section-padding bg-surface-contrast">
  <div class="container-max">
    <div class="mb-16 text-center">
      <PageHeadline
        title="Structured Learning for Every Level"
        subtitle="From first-time shooters to seasoned competitors, our progressive curriculum takes you exactly where you want to go"
        showPill={true}
        pillText="ALL SKILL LEVELS"
        pillVariant="secondary"
      />
    </div>
    
    <div class="course-levels-container">
      <div class="course-level">
        <div class="level-badge foundation">Foundation</div>
        <h3 class="level-title">Master the Fundamentals</h3>
        <div class="level-price">$99 per course</div>
        <p class="level-description">Build an unshakeable foundation with championship-proven basics</p>
        <ul class="level-topics">
          <li>Perfect gun mount & stance</li>
          <li>Eye dominance optimization</li>
          <li>Target focus techniques</li>
          <li>Lead picture development</li>
          <li>Pre-shot routine basics</li>
          <li>Mental game introduction</li>
        </ul>
        <div class="level-stats">
          <div class="stat">
            <span class="stat-number">13-29</span>
            <span class="stat-label">Chapters</span>
          </div>
          <div class="stat">
            <span class="stat-number">1.5-2</span>
            <span class="stat-label">Hours</span>
          </div>
        </div>
      </div>
      
      <div class="course-level">
        <div class="level-badge advanced">Advanced</div>
        <h3 class="level-title">Elevate Your Game</h3>
        <div class="level-price">$99 per course</div>
        <p class="level-description">Master complex targets and competition strategies</p>
        <ul class="level-topics">
          <li>Crossers, teal & chandelle</li>
          <li>Rabbit & battue targets</li>
          <li>Pair strategies & timing</li>
          <li>Competition preparation</li>
          <li>Advanced mental game</li>
          <li>Equipment optimization</li>
        </ul>
        <div class="level-stats">
          <div class="stat">
            <span class="stat-number">26+</span>
            <span class="stat-label">Chapters</span>
          </div>
          <div class="stat">
            <span class="stat-number">2.5+</span>
            <span class="stat-label">Hours</span>
          </div>
        </div>
      </div>
      
      <div class="course-level featured">
        <div class="level-badge bundle">Complete Bundle</div>
        <h3 class="level-title">The Ultimate Training System</h3>
        <div class="level-price">
          <span class="original-price">$594</span>
          <span class="bundle-price">$453.60</span>
          <span class="savings">Save $140.40</span>
        </div>
        <p class="level-description">Get all 6 courses from all 3 world champions</p>
        <ul class="level-topics special">
          <li>3 complete teaching methods</li>
          <li>6 comprehensive courses</li>
          <li>100+ detailed chapters</li>
          <li>12+ hours of instruction</li>
          <li>Lifetime access to everything</li>
          <li>Future updates included</li>
        </ul>
        <CTAButton
          text="Get Complete Access"
          href="https://digital.claytargetinstruction.com/l/products/all-courses-bundle"
          variant="primary"
          size="medium"
          external={true}
          withArrow={true}
        />
      </div>
    </div>
    
    <div class="bundle-options">
      <h4 class="bundle-title">Or Choose Individual Bundles</h4>
      <div class="bundle-grid">
        <div class="bundle-item">
          <span class="bundle-instructor">Per Instructor Bundle</span>
          <span class="bundle-price">$189</span>
          <span class="bundle-desc">Foundation + Advanced</span>
        </div>
        <div class="bundle-item">
          <span class="bundle-instructor">All Foundation Bundle</span>
          <span class="bundle-price">$237.60</span>
          <span class="bundle-desc">3 Foundation Courses</span>
        </div>
        <div class="bundle-item">
          <span class="bundle-instructor">All Advanced Bundle</span>
          <span class="bundle-price">$237.60</span>
          <span class="bundle-desc">3 Advanced Courses</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

## Notes

- All CSS styles associated with these sections should also be preserved in case we need to reference them later
- The content can be repurposed or reintegrated in different ways if needed
- Some of this content (like the transformation grid) will be moved to other sections rather than completely removed