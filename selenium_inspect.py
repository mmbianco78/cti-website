#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')

# Create driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Load an article page
    driver.get('http://localhost:4321/articles/improve-sporting-clays-score')
    time.sleep(2)
    
    # Wait for article content
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "article-content"))
    )
    
    # Get the article content HTML
    content_div = driver.find_element(By.CLASS_NAME, "article-content")
    inner_html = driver.execute_script("return arguments[0].innerHTML;", content_div)
    
    print("=== Article Content HTML (first 1000 chars) ===")
    print(inner_html[:1000])
    print("\n")
    
    # Check if h2 elements exist
    h2_elements = content_div.find_elements(By.TAG_NAME, "h2")
    print(f"Number of H2 elements found: {len(h2_elements)}")
    
    if h2_elements:
        for i, h2 in enumerate(h2_elements[:3]):  # First 3 h2s
            print(f"\nH2 #{i+1} text: {h2.text}")
            print(f"H2 #{i+1} computed styles:")
            styles = driver.execute_script("""
                var elem = arguments[0];
                var styles = window.getComputedStyle(elem);
                return {
                    fontSize: styles.fontSize,
                    color: styles.color,
                    fontWeight: styles.fontWeight,
                    fontFamily: styles.fontFamily,
                    className: elem.className,
                    id: elem.id
                };
            """, h2)
            print(styles)
    
    # Check for any style tags
    style_tags = driver.find_elements(By.TAG_NAME, "style")
    print(f"\nNumber of style tags found: {len(style_tags)}")
    
    # Check if our custom styles are in the page
    page_source = driver.page_source
    if "2.75rem !important" in page_source:
        print("\nCustom h2 styles (2.75rem) found in page source!")
    else:
        print("\nCustom h2 styles (2.75rem) NOT found in page source!")
        
    # Check the actual style tag content
    if style_tags:
        for i, style in enumerate(style_tags[:3]):
            content = driver.execute_script("return arguments[0].innerHTML;", style)
            if "article-content" in content:
                print(f"\nStyle tag {i+1} with article-content rules:")
                print(content[:500])

finally:
    driver.quit()