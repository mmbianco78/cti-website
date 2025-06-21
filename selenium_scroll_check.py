#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

try:
    # Load an article page
    driver.get('http://localhost:4321/articles/improve-sporting-clays-score')
    time.sleep(2)
    
    # Scroll to show h2 headings
    driver.execute_script("window.scrollTo(0, 800);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'article_content_headings.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Scroll more to show different content
    driver.execute_script("window.scrollTo(0, 1600);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'article_content_mid.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

finally:
    driver.quit()