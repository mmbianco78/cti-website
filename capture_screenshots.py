import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import subprocess

def capture_full_page_screenshots():
    # Create screenshots directory
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    # Initialize the driver
    driver = webdriver.Chrome(options=options)
    
    try:
        # Navigate to the page
        print("Loading page...")
        driver.get('http://localhost:4323')
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(2)  # Additional wait for any dynamic content
        
        # Get page dimensions
        total_height = driver.execute_script("return document.body.scrollHeight")
        viewport_height = driver.execute_script("return window.innerHeight")
        
        print(f"Page height: {total_height}px")
        print(f"Viewport height: {viewport_height}px")
        
        # Calculate number of screenshots needed
        num_screenshots = (total_height // viewport_height) + 1
        
        # Capture screenshots while scrolling
        for i in range(num_screenshots):
            # Calculate scroll position
            scroll_position = i * viewport_height
            
            # Scroll to position
            driver.execute_script(f"window.scrollTo(0, {scroll_position});")
            time.sleep(1)  # Wait for smooth scrolling and any lazy-loaded content
            
            # Take screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{screenshots_dir}/screenshot_{i+1:02d}_{timestamp}.png"
            driver.save_screenshot(filename)
            print(f"Captured screenshot {i+1}/{num_screenshots}: {filename}")
            
            # Log visible content
            visible_elements = driver.execute_script("""
                const elements = document.querySelectorAll('h1, h2, h3, section, .hero, .section');
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
            """)
            
            print(f"Visible elements at position {scroll_position}px:")
            for elem in visible_elements:
                print(f"  - {elem['tag']} {elem['class']} {elem['id']}: {elem['text']}...")
        
        # Scroll back to top for final full-page screenshot
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
        # Set window size to capture full page
        driver.set_window_size(1920, total_height)
        time.sleep(2)
        
        # Take full page screenshot
        full_page_filename = f"{screenshots_dir}/full_page_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(full_page_filename)
        print(f"\nCaptured full page screenshot: {full_page_filename}")
        
        # Analyze page structure
        print("\nAnalyzing page structure...")
        
        # Get all sections
        sections = driver.execute_script("""
            const sections = document.querySelectorAll('section, .section, [class*="section"]');
            return Array.from(sections).map(section => ({
                tag: section.tagName,
                class: section.className,
                id: section.id,
                height: section.offsetHeight,
                childCount: section.children.length,
                hasImages: section.querySelectorAll('img').length > 0,
                heading: section.querySelector('h1, h2, h3')?.innerText || 'No heading'
            }));
        """)
        
        print(f"\nFound {len(sections)} sections:")
        for idx, section in enumerate(sections):
            print(f"\nSection {idx + 1}:")
            print(f"  Tag: {section['tag']}")
            print(f"  Class: {section['class']}")
            print(f"  ID: {section['id']}")
            print(f"  Height: {section['height']}px")
            print(f"  Children: {section['childCount']}")
            print(f"  Has images: {section['hasImages']}")
            print(f"  Heading: {section['heading'][:50]}...")
        
        # Get color scheme
        colors = driver.execute_script("""
            const body = document.body;
            const computedStyle = window.getComputedStyle(body);
            return {
                backgroundColor: computedStyle.backgroundColor,
                color: computedStyle.color,
                fontFamily: computedStyle.fontFamily
            };
        """)
        
        print(f"\nPage styling:")
        print(f"  Background: {colors['backgroundColor']}")
        print(f"  Text color: {colors['color']}")
        print(f"  Font family: {colors['fontFamily']}")
        
        # Check for repetitive content
        headings = driver.execute_script("""
            const headings = document.querySelectorAll('h1, h2, h3');
            return Array.from(headings).map(h => ({
                level: h.tagName,
                text: h.innerText,
                parent: h.parentElement.className
            }));
        """)
        
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
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        driver.quit()
        print("\nScreenshot capture complete!")

if __name__ == "__main__":
    capture_full_page_screenshots()