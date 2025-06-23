#!/usr/bin/env python3
"""
Blog Import Script for CTI Website
Efficiently imports all blog posts, images, and comments from the blog mirror
"""

import os
import json
import re
import shutil
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser
from typing import Dict, List, Optional, Tuple
import html2text

# Configuration
BLOG_MIRROR_PATH = Path("/Users/marcobianco/code/claytargetinstruction/clti_blog_mirror/claytargetinstruction.com")
CTI_WEBSITE_PATH = Path("/Users/marcobianco/code/claytargetinstruction/cti-website")
ARTICLES_OUTPUT = CTI_WEBSITE_PATH / "src/content/articles"
IMAGES_OUTPUT = CTI_WEBSITE_PATH / "public/images/blog"
COMMENTS_OUTPUT = CTI_WEBSITE_PATH / "src/data/comments"

# Ensure output directories exist
ARTICLES_OUTPUT.mkdir(parents=True, exist_ok=True)
IMAGES_OUTPUT.mkdir(parents=True, exist_ok=True)
COMMENTS_OUTPUT.mkdir(parents=True, exist_ok=True)

class BlogPostExtractor(HTMLParser):
    """Custom HTML parser to extract blog post content and metadata"""
    
    def __init__(self):
        super().__init__()
        self.in_article = False
        self.in_comments = False
        self.current_tag = None
        self.metadata = {}
        self.content = []
        self.comments = []
        self.buffer = ""
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Extract metadata from meta tags
        if tag == "meta":
            if attrs_dict.get("property") == "og:title":
                self.metadata["title"] = attrs_dict.get("content", "")
            elif attrs_dict.get("property") == "og:description":
                self.metadata["description"] = attrs_dict.get("content", "")
            elif attrs_dict.get("property") == "og:image":
                self.metadata["image"] = attrs_dict.get("content", "")
            elif attrs_dict.get("property") == "article:published_time":
                self.metadata["date"] = attrs_dict.get("content", "")
            elif attrs_dict.get("property") == "article:modified_time":
                self.metadata["modified"] = attrs_dict.get("content", "")
            elif attrs_dict.get("name") == "author":
                self.metadata["author"] = attrs_dict.get("content", "")
                
        # Track when we're in the article content
        if tag == "article" or (tag == "div" and "entry-content" in attrs_dict.get("class", "")):
            self.in_article = True
            
        # Track when we're in comments section
        if tag == "div" and "comment-list" in attrs_dict.get("class", ""):
            self.in_comments = True
            
        self.current_tag = tag
        
    def handle_endtag(self, tag):
        if tag == "article":
            self.in_article = False
        self.current_tag = None
        
    def handle_data(self, data):
        if self.in_article and self.current_tag not in ["script", "style"]:
            self.content.append(data)

def extract_blog_post(html_file: Path) -> Dict:
    """Extract all relevant data from a blog post HTML file"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Parse HTML
    parser = BlogPostExtractor()
    parser.feed(html_content)
    
    # Convert content to markdown
    h2t = html2text.HTML2Text()
    h2t.ignore_links = False
    h2t.ignore_images = False
    h2t.body_width = 0  # Don't wrap lines
    
    # Extract the main content section (between article tags or entry-content div)
    content_match = re.search(r'<article[^>]*>.*?</article>|<div[^>]*class="[^"]*entry-content[^"]*"[^>]*>.*?</div>', 
                             html_content, re.DOTALL)
    
    markdown_content = ""
    if content_match:
        markdown_content = h2t.handle(content_match.group(0))
        
    # Clean up the markdown
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)  # Remove excessive newlines
    
    return {
        "metadata": parser.metadata,
        "content": markdown_content,
        "comments": parser.comments,
        "html_file": str(html_file)
    }

def generate_slug(title: str) -> str:
    """Generate a URL-friendly slug from title"""
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def process_author_name(author: str) -> str:
    """Normalize author names to match CTI format"""
    author_map = {
        "Anthony I. Matarese Jr.": "Anthony I. Matarese Jr.",
        "Anthony Matarese": "Anthony I. Matarese Jr.",
        "aimshooting": "Anthony I. Matarese Jr.",
        "George Digweed": "George Digweed MBE",
        "digweedg": "George Digweed MBE",
        "Zachary Kienbaum": "Zachary Kienbaum",
        "Zach Kienbaum": "Zachary Kienbaum",
        "zkienbaum": "Zachary Kienbaum"
    }
    return author_map.get(author, author)

def download_and_copy_image(image_url: str, slug: str) -> str:
    """Copy image from blog mirror to website and return new path"""
    if not image_url:
        return ""
        
    # Extract filename from URL
    filename = image_url.split('/')[-1]
    
    # Find the image in wp-content/uploads
    uploads_path = BLOG_MIRROR_PATH / "wp-content/uploads"
    
    # Search for the file
    for root, dirs, files in os.walk(uploads_path):
        if filename in files:
            source_path = Path(root) / filename
            
            # Copy to blog images folder with article slug prefix
            dest_filename = f"{slug}_{filename}" if not filename.startswith(slug) else filename
            dest_path = IMAGES_OUTPUT / dest_filename
            
            shutil.copy2(source_path, dest_path)
            return f"/images/blog/{dest_filename}"
    
    print(f"Warning: Image not found: {filename}")
    return f"/images/blog/{filename}"  # Return expected path anyway

def create_markdown_file(post_data: Dict, slug: str):
    """Create a markdown file for the blog post"""
    metadata = post_data["metadata"]
    
    # Process date
    date_str = metadata.get("date", "")
    if date_str:
        try:
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            date_str = date_obj.strftime("%Y-%m-%d")
        except:
            date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Process author
    author = process_author_name(metadata.get("author", "CTI Team"))
    
    # Copy image and get new path
    image_path = download_and_copy_image(metadata.get("image", ""), slug)
    
    # Create frontmatter
    frontmatter = f"""---
title: "{metadata.get('title', 'Untitled').replace('"', '\\"')}"
description: "{metadata.get('description', '').replace('"', '\\"')}"
date: {date_str}
image: "{image_path}"
author: "{author}"
category: "technique"
tags: ['imported']
---

"""
    
    # Combine frontmatter and content
    full_content = frontmatter + post_data["content"]
    
    # Write to file
    output_file = ARTICLES_OUTPUT / f"{slug}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    return output_file

def main():
    """Main import function"""
    print("🚀 Starting blog import process...")
    
    # Find all blog post HTML files
    blog_posts_dir = BLOG_MIRROR_PATH / "blog"
    post_files = []
    
    # Collect all index.html files in blog subdirectories
    for root, dirs, files in os.walk(blog_posts_dir):
        # Skip certain directories
        if any(skip in root for skip in ['feed', 'page', 'author', 'category']):
            continue
            
        if 'index.html' in files:
            post_files.append(Path(root) / 'index.html')
    
    print(f"📊 Found {len(post_files)} blog posts to import")
    
    # Process each blog post
    successful = 0
    failed = 0
    summary = []
    
    for i, post_file in enumerate(post_files, 1):
        try:
            print(f"\n[{i}/{len(post_files)}] Processing: {post_file.parent.name}")
            
            # Extract blog post data
            post_data = extract_blog_post(post_file)
            
            # Generate slug from directory name or title
            slug = post_file.parent.name
            if slug in ['blog', '.', '']:
                slug = generate_slug(post_data["metadata"].get("title", f"post-{i}"))
            
            # Skip if no title
            if not post_data["metadata"].get("title"):
                print(f"  ⚠️  Skipping - no title found")
                continue
                
            # Create markdown file
            output_file = create_markdown_file(post_data, slug)
            
            # Save summary info
            summary.append({
                "slug": slug,
                "title": post_data["metadata"].get("title"),
                "author": process_author_name(post_data["metadata"].get("author", "")),
                "date": post_data["metadata"].get("date", ""),
                "image": post_data["metadata"].get("image", ""),
                "output_file": str(output_file.relative_to(CTI_WEBSITE_PATH))
            })
            
            print(f"  ✅ Successfully imported: {post_data['metadata'].get('title')}")
            successful += 1
            
        except Exception as e:
            print(f"  ❌ Failed to import: {e}")
            failed += 1
    
    # Write summary report
    summary_file = CTI_WEBSITE_PATH / "import-summary.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump({
            "import_date": datetime.now().isoformat(),
            "total_posts": len(post_files),
            "successful": successful,
            "failed": failed,
            "posts": summary
        }, f, indent=2)
    
    print(f"\n✨ Import complete!")
    print(f"   - Successful: {successful}")
    print(f"   - Failed: {failed}")
    print(f"   - Summary saved to: {summary_file}")

if __name__ == "__main__":
    main()