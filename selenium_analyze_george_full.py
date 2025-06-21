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
    # Load George Digweed page
    driver.get('http://localhost:4321/george-digweed')
    time.sleep(2)
    
    # Get page height
    page_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Total page height: {page_height}px")
    
    # Take screenshots at intervals
    scroll_positions = [0, 600, 1200, 1800, 2400, 3000]
    
    for i, pos in enumerate(scroll_positions):
        if pos < page_height:
            driver.execute_script(f"window.scrollTo(0, {pos});")
            time.sleep(1)
            
            screenshot_path = os.path.join(screenshots_dir, f'george_full_flow_{i}.png')
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot {i} saved at scroll position {pos}px")

finally:
    driver.quit()