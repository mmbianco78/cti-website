# Blog Import Plan

## Structured Blog Import Plan

### Phase 1: Analysis & Inventory
1. **Catalog all blog posts** in the mirror directory
   - Extract post URLs, titles, authors, dates from HTML meta tags
   - Create a complete inventory spreadsheet/JSON
   - Identify post categories and organize by author

2. **Map image assets**
   - Scan all wp-content/uploads directories 
   - Create mapping of image filenames to blog posts
   - Identify image sizes and quality variants

3. **Content structure analysis**
   - Examine existing article schema in CTI website
   - Compare with blog post structure in mirror
   - Define mapping strategy for frontmatter fields

### Phase 2: Automation Setup
1. **Create extraction script** to:
   - Parse HTML files and extract meta data (title, description, author, date, featured image)
   - Extract article content from HTML body
   - Convert HTML content to Markdown
   - Generate proper frontmatter for Astro content collection

2. **Create image processing script** to:
   - Copy all relevant images from wp-content/uploads
   - Organize by date/author structure
   - Optimize image sizes if needed
   - Update image paths in content

### Phase 3: Batch Processing
1. **Run extraction script** on all blog posts
2. **Generate markdown files** with proper frontmatter
3. **Copy all images** in organized structure
4. **Validate output** - check for missing images, broken links

### Phase 4: Content Review & Cleanup
1. **Review generated articles** for formatting issues
2. **Update internal links** to point to new site structure
3. **Categorize and tag** articles appropriately
4. **Update any CTI-specific branding/links**

### Phase 5: Integration
1. **Update articles index page** to show all imported content
2. **Test article pages** and image loading
3. **Update navigation/sitemap** if needed

## Benefits of This Approach:
- **Systematic**: Handles all content at once vs. piecemeal
- **Automated**: Reduces manual work and errors
- **Comprehensive**: Ensures no content is missed
- **Efficient**: Single operation vs. multiple tool calls
- **Maintainable**: Creates reusable process for future imports

## Next Steps:
Would you like me to start with Phase 1 (analysis) or would you prefer I begin building the extraction scripts directly?