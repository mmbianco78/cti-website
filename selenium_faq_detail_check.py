#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    # Load FAQ page
    driver.get('http://localhost:4321/faq')
    time.sleep(2)
    
    # Check what's actually being displayed
    faq_items = driver.find_elements(By.CLASS_NAME, "faq-item")
    print(f"Found {len(faq_items)} FAQ items")
    
    if faq_items:
        first_item = faq_items[0]
        # Get the HTML content
        inner_html = driver.execute_script("return arguments[0].innerHTML;", first_item)
        print("First FAQ item HTML:")
        print(inner_html)
        
        # Check for answer elements
        answers = first_item.find_elements(By.CLASS_NAME, "faq-answer")
        print(f"\nFound {len(answers)} answer elements")
        
        if answers:
            answer_text = answers[0].text
            print(f"Answer text: {answer_text}")
        
    # Take detailed screenshot
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'faq_detail_check.png')
    driver.save_screenshot(screenshot_path)
    print(f"\nScreenshot saved: {screenshot_path}")

finally:
    driver.quit()