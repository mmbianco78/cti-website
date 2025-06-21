# Critical Notes - CTI Website Migration

## ⚠️ IMPORTANT REMINDERS

### 1. **Platform Strategy**
- **OLD APPROACH (cti-astro)**: Direct course sales with details, pricing, bundles
- **NEW APPROACH (cti-website)**: Simple funnel to digital.claytargetinstruction.com
- **DO NOT**: Add course details, pricing, or bundles to the new site
- **ALL CTAs**: Must point to https://digital.claytargetinstruction.com

### 2. **Missing Assets Required**
```
📁 public/fonts/
   ├── Aeonik-Regular.otf  ⚠️ MISSING
   └── Aeonik-Bold.otf     ⚠️ MISSING

📁 public/assets/video/
   ├── anthony-matarese-promo.mp4      ⚠️ MISSING
   └── Breaking_Clays_Animation_Hero.mp4 ⚠️ MISSING
```

### 3. **Placeholder Content to Update**
- `/privacy` - Currently has placeholder text
- `/terms` - Currently has placeholder text
- Meta images for social sharing (og:image)

### 4. **Build Commands**
```bash
# Development
npm run dev          # Runs on http://localhost:4321

# Production Build
npm run build        # Creates dist/ folder

# Preview Production Build
npm run preview      # Test the built site
```

### 5. **Git Branch Structure**
- `main` - Original version
- `final-merge` - ✅ YOUR COMPLETED WORK IS HERE

### 6. **Key Architecture Decisions**

#### Content Collections
- Blog articles use Astro Content Collections
- Located in `src/content/articles/`
- Schema defined in `src/content/config.ts`
- Categories: technique, equipment, mental-game, competition, training

#### Styling Approach
- Tailwind CSS for utilities
- Custom animations in tailwind.config.mjs
- Special effects in global.css as utility classes
- Aeonik font (when added) as primary font

#### Component Philosophy
- Minimal components for maintainability
- BaseLayout wraps all pages
- Navigation and Footer are global
- Specialized components only where needed

### 7. **Performance Optimizations**
- Static Site Generation (all pages pre-rendered)
- Images served from public/assets/images/
- Minimal JavaScript (only for interactivity)
- No external dependencies beyond build tools

### 8. **Testing Checklist**
Before deploying, always:
1. Run `npm run build` - should complete with no errors
2. Check all CTAs go to digital platform
3. Test FAQ accordion functionality
4. Verify mobile menu works
5. Check all images load
6. Test on real mobile devices

### 9. **Content Management**

#### Adding New Blog Articles
1. Create new .md file in `src/content/articles/`
2. Follow the frontmatter schema:
```yaml
---
title: "Article Title"
description: "Meta description"
date: 2024-01-15
image: "/assets/images/article-image.jpg"
author: "Author Name"
featured: false
tags: ["shooting", "technique"]
category: "technique"
---
```

#### Updating Instructor Info
- Edit files directly in `src/pages/`
- anthony-matarese-jr.astro
- george-digweed.astro
- zach-kienbaum.astro

### 10. **Common Issues & Solutions**

**Font Warnings During Build**
- Expected until Aeonik fonts are added
- Doesn't affect functionality
- Site falls back to system fonts

**Build Errors**
- Usually missing imports or undefined variables
- Check recent changes in git
- Run `npm run dev` for better error messages

**Images Not Showing**
- Ensure paths start with `/assets/images/`
- Check file exists in public folder
- Use lowercase filenames

### 11. **Deployment Notes**
- Deploy contents of `dist/` folder after build
- Ensure hosting serves index.html for all routes
- Enable gzip compression
- Set cache headers for assets
- Configure SSL certificate

### 12. **DO NOT FORGET**
- This is a FUNNEL site, not a course platform
- Keep messaging simple and focused
- All roads lead to digital.claytargetinstruction.com
- Instructor credibility is the main selling point
- No pricing, no course details, no complexity

## Emergency Contacts
If you need to understand any decisions made during this migration, refer to:
- SESSION_LOG.md - Complete record of the migration
- MIGRATION_COMPLETE.md - Summary of changes
- visual-qa-report.md - QA results
- This file - Critical reminders