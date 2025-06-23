#!/usr/bin/env python3
"""
Test script to validate blog import approach
Tests on a single blog post before running full import
"""

import os
from pathlib import Path

# Configuration
BLOG_MIRROR_PATH = Path("/Users/marcobianco/code/claytargetinstruction/clti_blog_mirror/claytargetinstruction.com")

def scan_blog_structure():
    """Scan and report on blog structure"""
    blog_dir = BLOG_MIRROR_PATH / "blog"
    
    print("📁 Scanning blog structure...")
    
    # Count different types of content
    post_dirs = []
    category_dirs = []
    author_dirs = []
    
    for item in blog_dir.iterdir():
        if item.is_dir():
            if item.name == "category":
                for cat in item.iterdir():
                    if cat.is_dir():
                        category_dirs.append(cat.name)
            elif item.name == "author":
                for auth in item.iterdir():
                    if auth.is_dir():
                        author_dirs.append(auth.name)
            elif item.name not in ["feed", "page"]:
                # This is likely a blog post
                if (item / "index.html").exists():
                    post_dirs.append(item.name)
    
    print(f"\n📊 Blog Structure Summary:")
    print(f"   - Blog posts found: {len(post_dirs)}")
    print(f"   - Categories: {len(set(category_dirs))}")
    print(f"   - Authors: {len(set(author_dirs))}")
    
    print(f"\n👥 Authors found:")
    for author in sorted(set(author_dirs)):
        print(f"   - {author}")
        
    print(f"\n📑 Categories found:")
    for category in sorted(set(category_dirs)):
        print(f"   - {category}")
        
    print(f"\n📝 Sample blog posts:")
    for post in post_dirs[:5]:
        print(f"   - {post}")
        
    return post_dirs

def analyze_single_post(post_dir: str):
    """Analyze a single blog post structure"""
    post_path = BLOG_MIRROR_PATH / "blog" / post_dir / "index.html"
    
    print(f"\n🔍 Analyzing post: {post_dir}")
    
    if not post_path.exists():
        print("   ❌ index.html not found")
        return
        
    # Check file size
    size = post_path.stat().st_size / 1024  # KB
    print(f"   - File size: {size:.1f} KB")
    
    # Quick scan for key elements
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check for metadata
    has_title = '<meta property="og:title"' in content
    has_desc = '<meta property="og:description"' in content
    has_image = '<meta property="og:image"' in content
    has_author = '<meta name="author"' in content
    has_date = '<meta property="article:published_time"' in content
    
    print(f"   - Has title meta: {'✅' if has_title else '❌'}")
    print(f"   - Has description: {'✅' if has_desc else '❌'}")
    print(f"   - Has featured image: {'✅' if has_image else '❌'}")
    print(f"   - Has author: {'✅' if has_author else '❌'}")
    print(f"   - Has date: {'✅' if has_date else '❌'}")
    
    # Check for content markers
    has_article = '<article' in content or 'entry-content' in content
    has_comments = 'comment' in content.lower()
    
    print(f"   - Has article content: {'✅' if has_article else '❌'}")
    print(f"   - Has comments section: {'✅' if has_comments else '❌'}")

def main():
    """Run tests"""
    print("🧪 Testing Blog Import Approach\n")
    
    # First, scan the structure
    post_dirs = scan_blog_structure()
    
    # Analyze a few sample posts
    if post_dirs:
        print("\n" + "="*50)
        print("ANALYZING SAMPLE POSTS")
        print("="*50)
        
        # Test different types of posts
        test_posts = [
            "practice-and-training",  # We know this exists
            "what-is-sporting-clays",  # We know this exists
            post_dirs[0] if post_dirs else None
        ]
        
        for post in test_posts:
            if post:
                analyze_single_post(post)

if __name__ == "__main__":
    main()