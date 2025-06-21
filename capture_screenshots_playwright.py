import asyncio
import os
from datetime import datetime
from playwright.async_api import async_playwright

async def capture_full_page_screenshots():
    # Create screenshots directory
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()
        
        try:
            # Navigate to the page
            print("Loading page...")
            await page.goto('http://localhost:4323', wait_until='networkidle')
            
            # Wait a bit more for any animations
            await page.wait_for_timeout(2000)
            
            # Get page dimensions
            dimensions = await page.evaluate('''() => {
                return {
                    width: document.documentElement.scrollWidth,
                    height: document.documentElement.scrollHeight,
                    viewportHeight: window.innerHeight
                }
            }''')
            
            total_height = dimensions['height']
            viewport_height = dimensions['viewportHeight']
            
            print(f"Page height: {total_height}px")
            print(f"Viewport height: {viewport_height}px")
            
            # Calculate number of screenshots needed
            num_screenshots = (total_height // viewport_height) + 1
            
            # Capture screenshots while scrolling
            for i in range(num_screenshots):
                # Calculate scroll position
                scroll_position = i * viewport_height
                
                # Scroll to position
                await page.evaluate(f'window.scrollTo(0, {scroll_position})')
                await page.wait_for_timeout(1000)  # Wait for smooth scrolling
                
                # Take screenshot
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{screenshots_dir}/screenshot_{i+1:02d}_{timestamp}.png"
                await page.screenshot(path=filename)
                print(f"Captured screenshot {i+1}/{num_screenshots}: {filename}")
                
                # Log visible content
                visible_elements = await page.evaluate('''() => {
                    const elements = document.querySelectorAll('h1, h2, h3, section, .hero, .section, [class*="section"]');
                    const visible = [];
                    elements.forEach(el => {
                        const rect = el.getBoundingClientRect();
                        if (rect.top < window.innerHeight && rect.bottom > 0) {
                            visible.push({
                                tag: el.tagName,
                                class: el.className,
                                text: el.innerText ? el.innerText.substring(0, 50) : '',
                                id: el.id
                            });
                        }
                    });
                    return visible;
                }''')
                
                print(f"Visible elements at position {scroll_position}px:")
                for elem in visible_elements:
                    if elem['text']:
                        print(f"  - {elem['tag']} {elem['class']} {elem['id']}: {elem['text']}...")
            
            # Take full page screenshot
            await page.evaluate('window.scrollTo(0, 0)')
            await page.wait_for_timeout(500)
            
            full_page_filename = f"{screenshots_dir}/full_page_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            await page.screenshot(path=full_page_filename, full_page=True)
            print(f"\nCaptured full page screenshot: {full_page_filename}")
            
            # Analyze page structure
            print("\nAnalyzing page structure...")
            
            # Get all sections
            sections = await page.evaluate('''() => {
                const sections = document.querySelectorAll('section, .section, [class*="section"], main > div');
                return Array.from(sections).map(section => ({
                    tag: section.tagName,
                    class: section.className,
                    id: section.id,
                    height: section.offsetHeight,
                    childCount: section.children.length,
                    hasImages: section.querySelectorAll('img').length > 0,
                    heading: section.querySelector('h1, h2, h3')?.innerText || 'No heading',
                    backgroundColor: window.getComputedStyle(section).backgroundColor
                }));
            }''')
            
            print(f"\nFound {len(sections)} sections:")
            for idx, section in enumerate(sections):
                if section['height'] > 100:  # Only show significant sections
                    print(f"\nSection {idx + 1}:")
                    print(f"  Tag: {section['tag']}")
                    print(f"  Class: {section['class']}")
                    print(f"  Height: {section['height']}px")
                    print(f"  Has images: {section['hasImages']}")
                    print(f"  Heading: {section['heading'][:50]}...")
                    print(f"  Background: {section['backgroundColor']}")
            
            # Get color scheme
            colors = await page.evaluate('''() => {
                const body = document.body;
                const computedStyle = window.getComputedStyle(body);
                return {
                    backgroundColor: computedStyle.backgroundColor,
                    color: computedStyle.color,
                    fontFamily: computedStyle.fontFamily
                };
            }''')
            
            print(f"\nPage styling:")
            print(f"  Background: {colors['backgroundColor']}")
            print(f"  Text color: {colors['color']}")
            print(f"  Font family: {colors['fontFamily']}")
            
            # Check for repetitive content
            headings = await page.evaluate('''() => {
                const headings = document.querySelectorAll('h1, h2, h3, h4');
                return Array.from(headings).map(h => ({
                    level: h.tagName,
                    text: h.innerText,
                    parent: h.closest('section, .section, [class*="section"]')?.className || h.parentElement.className
                }));
            }''')
            
            print(f"\nPage headings ({len(headings)} total):")
            heading_texts = []
            for h in headings:
                print(f"  {h['level']}: {h['text']} (in {h['parent']})")
                heading_texts.append(h['text'].lower())
            
            # Check for repetition
            from collections import Counter
            heading_counts = Counter(heading_texts)
            repetitive = [h for h, count in heading_counts.items() if count > 1]
            if repetitive:
                print(f"\nRepetitive headings found:")
                for h in repetitive:
                    print(f"  '{h}' appears {heading_counts[h]} times")
            
            # Check for instructor sections
            instructor_sections = await page.evaluate('''() => {
                const instructorElements = document.querySelectorAll('[class*="instructor"], [id*="instructor"]');
                return Array.from(instructorElements).map(el => ({
                    class: el.className,
                    id: el.id,
                    heading: el.querySelector('h1, h2, h3')?.innerText || '',
                    hasImage: el.querySelectorAll('img').length > 0
                }));
            }''')
            
            if instructor_sections:
                print(f"\nInstructor sections found ({len(instructor_sections)}):")
                for inst in instructor_sections:
                    print(f"  - {inst['heading']} (class: {inst['class']}, has image: {inst['hasImage']})")
            
            # Check testimonials
            testimonials = await page.evaluate('''() => {
                const testimonialElements = document.querySelectorAll('[class*="testimonial"], [class*="review"], blockquote');
                return testimonialElements.length;
            }''')
            
            print(f"\nTestimonials/Reviews found: {testimonials}")
            
            # Get CTA buttons
            ctas = await page.evaluate('''() => {
                const buttons = document.querySelectorAll('a[href*="contact"], button:not([type="submit"]), .cta, [class*="cta"]');
                return Array.from(buttons).map(btn => ({
                    text: btn.innerText,
                    href: btn.href || '',
                    class: btn.className
                }));
            }''')
            
            if ctas:
                print(f"\nCTA elements found ({len(ctas)}):")
                for cta in ctas[:5]:  # Show first 5
                    print(f"  - {cta['text']} (href: {cta['href']})")
                    
        except Exception as e:
            print(f"Error: {e}")
            
        finally:
            await browser.close()
            print("\nScreenshot capture complete!")

if __name__ == "__main__":
    asyncio.run(capture_full_page_screenshots())