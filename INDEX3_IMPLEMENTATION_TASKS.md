# Index3 Implementation Task List

## Pre-Build Checklist
- [ ] Current working directory: `/Users/marcobianco/code/claytargetinstruction/cti-website`
- [ ] Dev server will run on port 4321 (or 4322 if occupied)
- [ ] Build will use Astro + Tailwind CSS

---

## Task 1: Asset Migration (15 min)

### Create directories
```bash
mkdir -p public/assets/video
mkdir -p src/data
```

### Copy video files
```bash
# Hero video
cp ../cti-astro/public/assets/video/Breaking_Clays_Animation_Hero.mp4 public/assets/video/

# Instructor promo videos
cp ../cti-astro/public/assets/video/anthony-matarese-promo.mp4 public/assets/video/
cp ../cti-astro/public/assets/video/zachary-kienbaum-promo.mp4 public/assets/video/
cp ../cti-astro/public/assets/video/intro.mp4 public/assets/video/
```

### Copy missing images
```bash
cp ../cti-astro/public/assets/images/ShopperApprovedLogo.svg public/assets/images/
```

---

## Task 2: Create Data File (10 min)

### Create `src/data/testimonials.json`
```json
{
  "featured": [
    {
      "text": "I gained 8 points on my average in 6 months",
      "author": "Kyle M.",
      "details": "B Class",
      "instructor": "anthony",
      "rating": 5
    },
    {
      "text": "Best money I have ever spent. Cost less than two cases of shells but packed with years of experience",
      "author": "Bobby M.",
      "details": "Verified Buyer",
      "instructor": "platform",
      "rating": 5
    },
    {
      "text": "Zach's course helped me go from D to A class faster than any other coach I've worked with",
      "author": "R. Ralph P.",
      "details": "Verified Review",
      "instructor": "zachary",
      "rating": 5
    },
    {
      "text": "It's like being on the range with the GOAT. I finally understand how to shoot teal targets",
      "author": "Forum User",
      "details": "C Class",
      "instructor": "george",
      "rating": 5
    },
    {
      "text": "Seeing exactly where George looks changed everything. Gained 12 targets on my average",
      "author": "Mike T.",
      "details": "Master Class",
      "instructor": "george",
      "rating": 5
    },
    {
      "text": "My 10-year-old son could select videos to reinforce concepts. Site easy to use",
      "author": "Amy",
      "details": "PA",
      "instructor": "platform",
      "rating": 5
    }
  ],
  "additional": [
    {
      "text": "Anthony's online course is structured perfectly and the quality is incredible",
      "author": "Shopper Approved",
      "instructor": "anthony",
      "rating": 5
    },
    {
      "text": "Zach's breakdowns of crossing targets were the clearest I've seen anywhere",
      "author": "Emily S.",
      "details": "Recreational Shooter",
      "instructor": "zachary",
      "rating": 5
    },
    {
      "text": "Having access to George's footage is like stealing decades of experience",
      "author": "James R.",
      "details": "NSCA Competitor",
      "instructor": "george",
      "rating": 5
    },
    {
      "text": "The ShotKam integration is a game-changer - seeing exactly where to look was the key",
      "author": "James R.",
      "details": "A Class",
      "instructor": "platform",
      "rating": 5
    },
    {
      "text": "Best investment in my shooting career. The improvement has been noticeable and consistent",
      "author": "HunterX",
      "instructor": "anthony",
      "rating": 5
    },
    {
      "text": "His attention to detail were unparalleled. Highly recommend!",
      "author": "JohnD",
      "details": "Experienced Shooter",
      "instructor": "anthony",
      "rating": 5
    },
    {
      "text": "Finally broke 90 for the first time",
      "author": "James R.",
      "instructor": "platform",
      "rating": 5
    },
    {
      "text": "My scores jumped 15%",
      "author": "Lisa M.",
      "instructor": "platform",
      "rating": 5
    }
  ]
}
```

---

## Task 3: Create Components (45 min)

### Component 1: `src/components/HeroVideo.astro`
```astro
---
export interface Props {
  videoSrc: string;
  posterSrc: string;
  overlayOpacity?: number;
}

const { videoSrc, posterSrc, overlayOpacity = 0.5 } = Astro.props;
---

<div class="hero-video-container">
  <video 
    class="hero-video"
    autoplay 
    muted 
    loop 
    playsinline
    poster={posterSrc}
  >
    <source src={videoSrc} type="video/mp4">
  </video>
  <div class="hero-overlay" style={`--overlay-opacity: ${overlayOpacity}`}>
    <div class="hero-content">
      <slot />
    </div>
  </div>
</div>

<style>
  .hero-video-container {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
  }

  .hero-video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translate(-50%, -50%);
    z-index: -1;
    object-fit: cover;
  }

  .hero-overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, var(--overlay-opacity));
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .hero-content {
    width: 100%;
    max-width: 1200px;
    padding: 2rem;
    text-align: center;
    color: white;
  }

  /* Mobile: Show poster only */
  @media (max-width: 768px) {
    .hero-video {
      display: none;
    }
    
    .hero-video-container {
      background-image: var(--poster-bg);
      background-size: cover;
      background-position: center;
    }
  }
</style>

<script>
  // Pause video on mobile to save bandwidth
  if (window.innerWidth <= 768) {
    const video = document.querySelector('.hero-video') as HTMLVideoElement;
    if (video) {
      video.pause();
      video.removeAttribute('autoplay');
    }
  }
</script>
```

### Component 2: `src/components/StatsTicker.astro`
```astro
---
const stats = [
  "31 World Titles: George Digweed MBE",
  "2024 FITASC Champion: Zachary Kienbaum", 
  "First American World Champion: Anthony Matarese Jr.",
  "5,000+ Students Worldwide",
  "500+ Five-Star Reviews",
  "Students in 52 Countries"
];
---

<div class="stats-ticker-container">
  <div class="stats-ticker">
    {stats.map(stat => (
      <>
        <span class="stat-item">{stat}</span>
        <span class="stat-separator">•</span>
      </>
    ))}
    <!-- Duplicate for seamless loop -->
    {stats.map(stat => (
      <>
        <span class="stat-item">{stat}</span>
        <span class="stat-separator">•</span>
      </>
    ))}
  </div>
</div>

<style>
  .stats-ticker-container {
    background: var(--color-dark);
    color: var(--color-light);
    padding: 0.75rem 0;
    overflow: hidden;
    white-space: nowrap;
  }

  .stats-ticker {
    display: inline-flex;
    animation: scroll 60s linear infinite;
  }

  .stat-item {
    padding: 0 1rem;
    font-size: 0.9rem;
  }

  .stat-separator {
    color: var(--color-accent);
  }

  @keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
  }

  @media (max-width: 768px) {
    .stat-item {
      font-size: 0.8rem;
      padding: 0 0.5rem;
    }
  }
</style>
```

### Component 3: `src/components/TestimonialGrid.astro`
```astro
---
import testimonials from '../data/testimonials.json';

const featured = testimonials.featured;
---

<section class="testimonials-section">
  <div class="container-max">
    <h2 class="testimonials-title">Join 5,000+ Shooters Already Improving Their Game</h2>
    <p class="testimonials-subtitle">Real results from real shooters at every level</p>
    
    <div class="testimonial-grid">
      {featured.map((testimonial) => (
        <div class="testimonial-card">
          <div class="testimonial-stars">
            {"★".repeat(testimonial.rating)}
          </div>
          <p class="testimonial-text">"{testimonial.text}"</p>
          <div class="testimonial-author">
            <span class="author-name">{testimonial.author}</span>
            {testimonial.details && (
              <span class="author-details">{testimonial.details}</span>
            )}
          </div>
        </div>
      ))}
    </div>

    <div class="trust-badges">
      <img src="/assets/images/ShopperApprovedLogo.svg" alt="Shopper Approved" class="trust-badge" />
      <div class="rating-summary">
        <span class="rating-number">4.9</span>
        <span class="rating-stars">★★★★★</span>
        <span class="rating-count">500+ Reviews</span>
      </div>
    </div>
  </div>
</section>

<style>
  .testimonials-section {
    padding: 4rem 0;
    background: var(--color-surface);
  }

  .testimonials-title {
    font-size: 2.5rem;
    text-align: center;
    margin-bottom: 0.5rem;
  }

  .testimonials-subtitle {
    text-align: center;
    color: var(--color-gray-light);
    margin-bottom: 3rem;
  }

  .testimonial-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
  }

  .testimonial-card {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .testimonial-stars {
    color: var(--color-accent);
    font-size: 1.2rem;
    margin-bottom: 1rem;
  }

  .testimonial-text {
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
  }

  .testimonial-author {
    display: flex;
    flex-direction: column;
  }

  .author-name {
    font-weight: 600;
  }

  .author-details {
    color: var(--color-gray-light);
    font-size: 0.9rem;
  }

  .trust-badges {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 3rem;
  }

  .trust-badge {
    height: 60px;
  }

  .rating-summary {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .rating-number {
    font-size: 2rem;
    font-weight: bold;
  }

  .rating-stars {
    color: var(--color-accent);
  }

  @media (max-width: 768px) {
    .testimonial-grid {
      grid-template-columns: 1fr;
    }
    
    .trust-badges {
      flex-direction: column;
      gap: 1rem;
    }
  }
</style>
```

### Component 4: `src/components/InstructorVideoPreview.astro`
```astro
---
export interface Props {
  name: string;
  videoSrc: string;
  posterSrc: string;
  achievement: string;
  philosophy: string;
  authorId: string;
}

const { name, videoSrc, posterSrc, achievement, philosophy, authorId } = Astro.props;
---

<div class="instructor-video-card">
  <div class="video-container">
    <img src={posterSrc} alt={name} class="video-poster" />
    <button class="play-button" data-video={videoSrc}>
      <svg viewBox="0 0 24 24" fill="currentColor">
        <path d="M8 5v14l11-7z"/>
      </svg>
    </button>
  </div>
  <div class="instructor-info">
    <h3 class="instructor-name">{name}</h3>
    <p class="instructor-achievement">{achievement}</p>
    <p class="instructor-philosophy">"{philosophy}"</p>
    <a 
      href={`https://digital.claytargetinstruction.com?authorId=${authorId}`}
      class="instructor-cta"
      data-tracking={`index3_instructor_${name.toLowerCase().replace(/\s+/g, '_')}`}
    >
      Learn From {name.split(' ')[0]} →
    </a>
  </div>
</div>

<style>
  .instructor-video-card {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
  }

  .instructor-video-card:hover {
    transform: translateY(-4px);
  }

  .video-container {
    position: relative;
    aspect-ratio: 16/9;
    overflow: hidden;
  }

  .video-poster {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .play-button {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 60px;
    height: 60px;
    background: rgba(0,0,0,0.8);
    border: none;
    border-radius: 50%;
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .play-button:hover {
    background: var(--color-accent);
    transform: translate(-50%, -50%) scale(1.1);
  }

  .play-button svg {
    width: 24px;
    height: 24px;
    margin-left: 4px;
  }

  .instructor-info {
    padding: 1.5rem;
  }

  .instructor-name {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }

  .instructor-achievement {
    color: var(--color-accent);
    font-weight: 600;
    margin-bottom: 1rem;
  }

  .instructor-philosophy {
    font-style: italic;
    color: var(--color-gray);
    margin-bottom: 1.5rem;
  }

  .instructor-cta {
    display: inline-block;
    background: var(--color-accent);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    text-decoration: none;
    font-weight: 600;
    transition: background 0.3s ease;
  }

  .instructor-cta:hover {
    background: var(--color-accent-dark);
  }
</style>

<script>
  // Simple video modal handler
  document.querySelectorAll('.play-button').forEach(button => {
    button.addEventListener('click', (e) => {
      const videoSrc = (e.currentTarget as HTMLElement).dataset.video;
      // For now, just link to digital platform
      // TODO: Implement modal video player
      window.location.href = 'https://digital.claytargetinstruction.com';
    });
  });
</script>
```

### Component 5: `src/components/TrustIndicators.astro`
```astro
---
---

<div class="trust-indicators">
  <div class="trust-item">
    <span class="trust-icon">🏆</span>
    <span class="trust-value">36+</span>
    <span class="trust-label">World Championships</span>
  </div>
  <div class="trust-item">
    <span class="trust-icon">⭐</span>
    <span class="trust-value">4.9/5</span>
    <span class="trust-label">Average Rating</span>
  </div>
  <div class="trust-item">
    <span class="trust-icon">👥</span>
    <span class="trust-value">5,000+</span>
    <span class="trust-label">Active Students</span>
  </div>
</div>

<style>
  .trust-indicators {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin: 2rem 0;
  }

  .trust-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .trust-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }

  .trust-value {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--color-accent);
  }

  .trust-label {
    font-size: 0.9rem;
    color: var(--color-gray-light);
  }

  @media (max-width: 768px) {
    .trust-indicators {
      gap: 1.5rem;
    }
    
    .trust-value {
      font-size: 1.2rem;
    }
  }
</style>
```

---

## Task 4: Create index3.astro (30 min)

### Full page implementation at `src/pages/index3.astro`
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import HeroVideo from '../components/HeroVideo.astro';
import StatsTicker from '../components/StatsTicker.astro';
import TestimonialGrid from '../components/TestimonialGrid.astro';
import InstructorVideoPreview from '../components/InstructorVideoPreview.astro';
import TrustIndicators from '../components/TrustIndicators.astro';
import CTAButton from '../components/CTAButton.astro';

const instructors = [
  {
    name: "George Digweed MBE",
    videoSrc: "/assets/video/george-digweed-promo.mp4",
    posterSrc: "/assets/images/george_digweed_instructor_hero_desktop.jpg",
    achievement: "31 World Championships",
    philosophy: "See the target. Trust the eyes. Let it happen.",
    authorId: "2136725"
  },
  {
    name: "Anthony Matarese Jr.",
    videoSrc: "/assets/video/anthony-matarese-promo.mp4", 
    posterSrc: "/assets/images/anthony-i-matarese-jr_instructor_hero_desktop.jpg",
    achievement: "Youngest Hall of Fame Inductee",
    philosophy: "Build champions through structure, not superstition.",
    authorId: "1232914"
  },
  {
    name: "Zachary Kienbaum",
    videoSrc: "/assets/video/zachary-kienbaum-promo.mp4",
    posterSrc: "/assets/images/zachary-kienbaum_instructor_hero_desktop.jpg",
    achievement: "2024 FITASC World Champion",
    philosophy: "Turns mechanics into confidence and confidence into consistency.",
    authorId: "2149776"
  }
];
---

<BaseLayout 
  title="Learn From World Champions | Clay Target Instruction"
  description="3 World Champions. 36+ Championships. One Revolutionary Platform. Learn the exact methods that built the greatest careers in clay shooting."
>
  <!-- Stats Ticker -->
  <StatsTicker />

  <!-- Hero Section -->
  <HeroVideo 
    videoSrc="/assets/video/Breaking_Clays_Animation_Hero.mp4"
    posterSrc="/assets/images/zachary-kienbaum_instructor_hero_desktop.jpg"
    overlayOpacity={0.5}
  >
    <div class="hero-content-inner">
      <h1 class="hero-title">
        3 World Champions.<br>
        One Revolutionary Platform.<br>
        Your Future.
      </h1>
      
      <p class="hero-subtitle">
        Learn the exact methods that won 36+ world championships
      </p>

      <div class="instructor-badges">
        {instructors.map(instructor => (
          <div class="instructor-badge">
            <img src={instructor.posterSrc} alt={instructor.name} />
            <span>{instructor.name.split(' ')[0]}</span>
          </div>
        ))}
      </div>

      <TrustIndicators />

      <div class="hero-ctas">
        <CTAButton 
          href="https://digital.claytargetinstruction.com"
          text="Watch How Champions Really Shoot"
          variant="primary"
          size="large"
          trackingId="index3_hero_primary"
        />
        <a href="#testimonials" class="secondary-cta">See Student Results ↓</a>
      </div>
    </div>
  </HeroVideo>

  <!-- Intro Video Section -->
  <section class="intro-video-section">
    <div class="container-max">
      <h2>See What Makes CTI Different in 90 Seconds</h2>
      <div class="video-wrapper">
        <video 
          controls 
          poster="/assets/images/anthony-i-matarese-jr_instructor_hero_desktop.jpg"
          preload="metadata"
        >
          <source src="/assets/video/intro.mp4" type="video/mp4">
        </video>
      </div>
      <p class="video-caption">
        "The ShotKam integration is a game-changer - seeing exactly where to look was the key" - James R.
      </p>
    </div>
  </section>

  <!-- Instructor Video Previews -->
  <section class="instructors-section">
    <div class="container-max">
      <h2>Learn Directly From Your Champions</h2>
      <p class="section-subtitle">
        Click to preview each instructor's unique teaching style
      </p>
      
      <div class="instructor-grid">
        {instructors.map(instructor => (
          <InstructorVideoPreview {...instructor} />
        ))}
      </div>
    </div>
  </section>

  <!-- Technology Features -->
  <section class="features-section">
    <div class="container-max">
      <h2>Why 5,000+ Shooters Choose CTI</h2>
      
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">🎯</div>
          <h3>Patented Laser Technology</h3>
          <p>See exactly where champions look and point - the invisible fundamentals revealed</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon">📐</div>
          <h3>Multi-Angle HD Footage</h3>
          <p>Every technique shown from multiple angles in crystal-clear 4K quality</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon">📊</div>
          <h3>Structured Learning Path</h3>
          <p>Not random tips—complete systems that build from fundamentals to advanced</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon">♾️</div>
          <h3>Lifetime Access</h3>
          <p>Learn at your pace, rewatch anytime, on any device - yours forever</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon">🎯</div>
          <h3>Direct from Champions</h3>
          <p>No interpreters - learn directly from the legends themselves</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon">📈</div>
          <h3>Proven Results</h3>
          <p>Join thousands of students improving their scores every day</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Testimonials -->
  <div id="testimonials">
    <TestimonialGrid />
  </div>

  <!-- Skill Levels -->
  <section class="skill-levels-section">
    <div class="container-max">
      <h2>Wherever You Are, We'll Take You Higher</h2>
      
      <div class="skill-levels-grid">
        <div class="skill-level">
          <div class="level-icon">🎯</div>
          <h3>New Shooters</h3>
          <p>Build perfect fundamentals from day one. Start right, progress faster.</p>
        </div>
        
        <div class="skill-level">
          <div class="level-icon">📈</div>
          <h3>Intermediate</h3>
          <p>Break through plateaus with proven techniques from world champions.</p>
        </div>
        
        <div class="skill-level">
          <div class="level-icon">🏆</div>
          <h3>Competitors</h3>
          <p>Gain the mental edge and refinements that separate good from great.</p>
        </div>
      </div>
      
      <p class="skill-tagline">One platform. Every journey. Your success.</p>
    </div>
  </section>

  <!-- Final CTA -->
  <section class="final-cta-section">
    <div class="container-max">
      <h2>Join an Elite Community of Improving Shooters</h2>
      
      <div class="community-stats">
        <div class="stat">5,247 students currently enrolled</div>
        <div class="stat">New lessons added monthly</div>
        <div class="stat">Students in 52 countries</div>
      </div>
      
      <p class="urgency-text">
        Every day you wait is a day your competition gets better
      </p>
      
      <CTAButton 
        href="https://digital.claytargetinstruction.com"
        text="Start Learning From Champions Today"
        variant="primary"
        size="large"
        trackingId="index3_final_cta"
      />
      
      <p class="guarantee">
        ✓ 30-day money-back guarantee ✓ Instant access ✓ All devices
      </p>
    </div>
  </section>

  <style>
    /* Hero Styles */
    .hero-content-inner {
      max-width: 900px;
      margin: 0 auto;
    }

    .hero-title {
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 800;
      line-height: 1.1;
      margin-bottom: 1.5rem;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    .hero-subtitle {
      font-size: 1.5rem;
      margin-bottom: 2rem;
      opacity: 0.9;
    }

    .instructor-badges {
      display: flex;
      justify-content: center;
      gap: 2rem;
      margin: 2rem 0;
    }

    .instructor-badge {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
    }

    .instructor-badge img {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      border: 3px solid white;
    }

    .instructor-badge span {
      font-weight: 600;
      font-size: 0.9rem;
    }

    .hero-ctas {
      display: flex;
      gap: 2rem;
      justify-content: center;
      align-items: center;
      margin-top: 2rem;
    }

    .secondary-cta {
      color: white;
      text-decoration: none;
      font-weight: 600;
      opacity: 0.9;
      transition: opacity 0.3s ease;
    }

    .secondary-cta:hover {
      opacity: 1;
    }

    /* Intro Video Section */
    .intro-video-section {
      padding: 4rem 0;
      text-align: center;
      background: white;
    }

    .intro-video-section h2 {
      font-size: 2.5rem;
      margin-bottom: 2rem;
    }

    .video-wrapper {
      max-width: 800px;
      margin: 0 auto 2rem;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    }

    .video-wrapper video {
      width: 100%;
      height: auto;
    }

    .video-caption {
      font-style: italic;
      color: var(--color-gray);
      max-width: 600px;
      margin: 0 auto;
    }

    /* Instructors Section */
    .instructors-section {
      padding: 4rem 0;
      background: var(--color-surface);
    }

    .instructors-section h2 {
      text-align: center;
      font-size: 2.5rem;
      margin-bottom: 0.5rem;
    }

    .section-subtitle {
      text-align: center;
      color: var(--color-gray-light);
      margin-bottom: 3rem;
    }

    .instructor-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      max-width: 1200px;
      margin: 0 auto;
    }

    /* Features Section */
    .features-section {
      padding: 4rem 0;
      background: white;
    }

    .features-section h2 {
      text-align: center;
      font-size: 2.5rem;
      margin-bottom: 3rem;
    }

    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      max-width: 1000px;
      margin: 0 auto;
    }

    .feature-card {
      text-align: center;
      padding: 2rem;
    }

    .feature-icon {
      font-size: 3rem;
      margin-bottom: 1rem;
    }

    .feature-card h3 {
      font-size: 1.3rem;
      margin-bottom: 1rem;
    }

    .feature-card p {
      color: var(--color-gray);
      line-height: 1.6;
    }

    /* Skill Levels Section */
    .skill-levels-section {
      padding: 4rem 0;
      background: var(--color-surface);
      text-align: center;
    }

    .skill-levels-section h2 {
      font-size: 2.5rem;
      margin-bottom: 3rem;
    }

    .skill-levels-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      max-width: 900px;
      margin: 0 auto 2rem;
    }

    .skill-level {
      padding: 2rem;
    }

    .level-icon {
      font-size: 3rem;
      margin-bottom: 1rem;
    }

    .skill-level h3 {
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    .skill-tagline {
      font-size: 1.3rem;
      font-weight: 600;
      color: var(--color-accent);
    }

    /* Final CTA Section */
    .final-cta-section {
      padding: 4rem 0;
      background: var(--color-dark);
      color: white;
      text-align: center;
    }

    .final-cta-section h2 {
      font-size: 2.5rem;
      margin-bottom: 2rem;
    }

    .community-stats {
      display: flex;
      justify-content: center;
      gap: 3rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }

    .stat {
      font-size: 1.1rem;
      opacity: 0.9;
    }

    .urgency-text {
      font-size: 1.3rem;
      margin-bottom: 2rem;
      color: var(--color-accent);
    }

    .guarantee {
      margin-top: 1.5rem;
      opacity: 0.8;
    }

    /* Mobile Styles */
    @media (max-width: 768px) {
      .hero-title {
        font-size: 2rem;
      }

      .hero-subtitle {
        font-size: 1.2rem;
      }

      .instructor-badges {
        gap: 1rem;
      }

      .instructor-badge img {
        width: 60px;
        height: 60px;
      }

      .hero-ctas {
        flex-direction: column;
        gap: 1rem;
      }

      .community-stats {
        flex-direction: column;
        gap: 1rem;
      }
    }
  </style>
</BaseLayout>
```

---

## Task 5: Add Mobile Optimizations (15 min)

### Add to global.css
```css
/* Video Background Mobile Fix */
@media (max-width: 768px) {
  .hero-video-container {
    background-image: url('/assets/images/zachary-kienbaum_instructor_hero_desktop.jpg');
    background-size: cover;
    background-position: center;
  }
  
  .hero-video-container video {
    display: none;
  }
}

/* Testimonial Mobile Scroll */
@media (max-width: 768px) {
  .testimonial-grid {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    gap: 1rem;
    padding: 0 1rem;
  }
  
  .testimonial-card {
    flex: 0 0 280px;
    scroll-snap-align: start;
  }
}

/* CTA Mobile Full Width */
@media (max-width: 768px) {
  .cta-button {
    width: 100%;
    text-align: center;
  }
}
```

---

## Task 6: Testing & Deploy (20 min)

### Local Testing
```bash
# Build and preview
npm run build
npm run preview
# Visit http://localhost:4321/index3
```

### Testing Checklist
- [ ] Video plays on desktop
- [ ] Mobile shows poster image
- [ ] All CTAs have tracking IDs
- [ ] Testimonials display correctly
- [ ] Trust badges visible
- [ ] Page loads under 5 seconds
- [ ] No console errors
- [ ] Links go to correct destinations

### Deploy
```bash
# Commit changes
git add .
git commit -m "Add index3: high-converting landing page with video hero and testimonials"
git push origin another-final-branch-v1

# Deploy command depends on your setup
# npm run deploy or push to trigger automatic deployment
```

---

## Quick Fixes If Needed

### If video won't play:
- Check file path
- Ensure video is in public/assets/video/
- Try different video format
- Fall back to static image

### If testimonials break:
- Check JSON syntax
- Ensure proper imports
- Use hardcoded testimonials as backup

### If mobile is broken:
- Hide complex sections with display: none
- Use simple stacked layout
- Ensure touch targets are large enough

### If page is slow:
- Remove video autoplay
- Lazy load images
- Reduce testimonial count
- Optimize video file size

---

## Success Criteria
- [ ] Page loads successfully at /index3
- [ ] Video hero creates strong first impression
- [ ] Testimonials build trust
- [ ] Multiple CTAs throughout page
- [ ] Mobile experience is functional
- [ ] All tracking in place
- [ ] Ready to drive traffic