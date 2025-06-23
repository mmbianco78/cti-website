# Index Page Migration Plan

## Current State Analysis
- **index.astro** (77k) - Current primary homepage
- **index2.astro** (46k) - Alternative version
- **index3.astro** (37k) - New design to become primary
- **index-backup.astro** (46k) - Existing backup

## Migration Goals
1. Make index3.astro the new primary homepage (index.astro)
2. Preserve current index.astro as a backup
3. Maintain all existing files for reference
4. Ensure no broken links or references

## Pre-Migration Checklist
- [ ] Check for hardcoded links to index pages
- [ ] Verify no components import specific index files
- [ ] Check navigation references
- [ ] Review routing configuration
- [ ] Test current site functionality

## Migration Steps

### Step 1: Create New Branch
```bash
git checkout -b index3-to-primary-migration
```

### Step 2: Create Backups
1. Rename current index.astro → index-original-[date].astro
2. Keep index2.astro as is
3. Keep index3.astro as reference

### Step 3: File Operations
```bash
# Backup current index
mv src/pages/index.astro src/pages/index-original-2024-06-23.astro

# Copy index3 to become new index
cp src/pages/index3.astro src/pages/index.astro
```

### Step 4: Verification
- [ ] Run dev server and check homepage loads
- [ ] Verify all navigation links work
- [ ] Check console for errors
- [ ] Test responsive design
- [ ] Verify all CTAs function

### Step 5: Component Updates (if needed)
- Update any components that might reference specific index files
- Update navigation if needed

### Step 6: Testing
1. Homepage loads correctly
2. All sections render properly
3. Videos play
4. CTAs link correctly
5. Instructor cards work
6. Testimonials display

### Step 7: Commit Changes
```bash
git add -A
git commit -m "Migrate index3 to primary homepage"
```

## Rollback Plan
If issues occur:
```bash
git checkout index3-flow-improvements
git branch -D index3-to-primary-migration
```

## Post-Migration
- [ ] Test all pages
- [ ] Check for console errors
- [ ] Verify SEO meta tags
- [ ] Test on multiple browsers
- [ ] Mobile responsiveness check