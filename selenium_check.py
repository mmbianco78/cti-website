#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Create screenshots directory
screenshots_dir = '/Users/marcobianco/code/claytargetinstruction/cti-website/screenshots'
os.makedirs(screenshots_dir, exist_ok=True)

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')

# Create driver
driver = webdriver.Chrome(options=chrome_options)

def take_screenshot(url, filename):
    try:
        driver.get(url)
        time.sleep(2)  # Wait for page to load
        
        # Scroll to capture more content
        driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(1)
        
        screenshot_path = os.path.join(screenshots_dir, filename)
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        
        # Get computed styles for article content
        if 'articles/' in url and url != 'http://localhost:4321/articles':
            try:
                # Wait for article content to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "article-content"))
                )
                
                # Get font sizes
                content = driver.find_element(By.CLASS_NAME, "article-content")
                font_size = driver.execute_script("return window.getComputedStyle(arguments[0]).fontSize;", content)
                print(f"Article content font-size: {font_size}")
                
                # Check h2 styles
                h2_elements = content.find_elements(By.TAG_NAME, "h2")
                if h2_elements:
                    h2_style = driver.execute_script("""
                        var h2 = arguments[0];
                        var styles = window.getComputedStyle(h2);
                        return {
                            fontSize: styles.fontSize,
                            color: styles.color,
                            fontWeight: styles.fontWeight
                        };
                    """, h2_elements[0])
                    print(f"H2 styles: {h2_style}")
                
                # Check paragraph styles
                p_elements = content.find_elements(By.TAG_NAME, "p")
                if p_elements:
                    p_style = driver.execute_script("""
                        var p = arguments[0];
                        var styles = window.getComputedStyle(p);
                        return {
                            fontSize: styles.fontSize,
                            lineHeight: styles.lineHeight,
                            color: styles.color
                        };
                    """, p_elements[0])
                    print(f"Paragraph styles: {p_style}")
                    
            except Exception as e:
                print(f"Error getting styles: {e}")
        
    except Exception as e:
        print(f"Error taking screenshot of {url}: {e}")

try:
    # Check article list page
    print("\n=== Checking Articles List Page ===")
    take_screenshot('http://localhost:4321/articles', 'articles_list_check.png')
    
    # Check individual article pages
    articles = [
        ('improve-sporting-clays-score', 'Improve Your Sporting Clays Score'),
        ('what-is-sporting-clays', 'What is Sporting Clays?'),
        ('practice-and-training', 'Practice and Training Fundamentals')
    ]
    
    for slug, title in articles:
        print(f"\n=== Checking Article: {title} ===")
        take_screenshot(f'http://localhost:4321/articles/{slug}', f'article_{slug}_check.png')

finally:
    driver.quit()
    print("\nSelenium check complete!")