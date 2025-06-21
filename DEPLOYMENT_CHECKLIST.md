# Deployment Checklist - CTI Website

## Pre-Deployment Tasks

### Assets & Content
- [ ] Add Aeonik font files to `public/fonts/` directory
  - Aeonik-Regular.otf
  - Aeonik-Bold.otf
- [ ] Add promo video files to `public/assets/video/`
  - anthony-matarese-promo.mp4
  - Breaking_Clays_Animation_Hero.mp4
- [ ] Update Privacy Policy content (currently placeholder)
- [ ] Update Terms of Service content (currently placeholder)
- [ ] Add social media meta images (og:image) for better sharing

### Content Review
- [ ] Review all instructor bio content for accuracy
- [ ] Verify all external links to digital.claytargetinstruction.com
- [ ] Check that all images have appropriate alt text
- [ ] Ensure FAQ content is up-to-date

### Technical Checks
- [ ] Run `npm run build` - ✅ Completed successfully
- [ ] Test all interactive elements (navigation, FAQ accordion, etc.)
- [ ] Verify mobile responsiveness on actual devices
- [ ] Check cross-browser compatibility (Chrome, Safari, Firefox, Edge)
- [ ] Test all form submissions (newsletter signup, contact form)
- [ ] Verify analytics tracking codes are in place

## Deployment Steps

1. **Final Build**
   ```bash
   npm run build
   ```

2. **Deploy to Hosting**
   - Upload contents of `dist/` folder to web server
   - Or use automated deployment (Vercel, Netlify, etc.)

3. **DNS Configuration**
   - Point domain to hosting provider
   - Configure SSL certificate
   - Set up www redirect if needed

4. **Post-Deployment Verification**
   - [ ] Check all pages load correctly
   - [ ] Test navigation and all links
   - [ ] Verify images and videos load
   - [ ] Test mobile version
   - [ ] Check contact form submission
   - [ ] Verify analytics are tracking
   - [ ] Test page load speed
   - [ ] Check SEO meta tags

## Environment Variables
No environment variables required for this static site.

## Maintenance Notes
- Blog articles are managed through markdown files in `src/content/articles/`
- To add new articles, create new .md files following the existing schema
- Images should be optimized before uploading (WebP preferred for photos)
- Keep instructor course links updated if URLs change on digital platform

## Performance Optimization
- Images are already optimized for web
- Static site generation ensures fast loading
- Consider adding CDN for global distribution
- Enable gzip compression on server

## SEO Checklist
- [ ] Submit sitemap to Google Search Console
- [ ] Verify robots.txt is properly configured
- [ ] Set up 301 redirects from old URLs if applicable
- [ ] Monitor Core Web Vitals after launch

## Security
- [ ] Enable HTTPS across entire site
- [ ] Set security headers (CSP, X-Frame-Options, etc.)
- [ ] Regular updates of dependencies
- [ ] Monitor for vulnerabilities

## Backup & Recovery
- [ ] Set up regular backups of content
- [ ] Document deployment process
- [ ] Keep source code in version control (Git)
- [ ] Tag releases for easy rollback

## Support & Monitoring
- [ ] Set up uptime monitoring
- [ ] Configure error alerts
- [ ] Document support procedures
- [ ] Create content update guide for non-technical users

## Final Notes
The site is built with Astro and uses static site generation for optimal performance. All content is pre-rendered at build time, making the site fast and secure. The blog system uses Astro's content collections for easy management of articles.