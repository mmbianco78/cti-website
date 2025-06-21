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
    # Load FAQ page
    driver.get('http://localhost:4321/faq')
    time.sleep(2)
    
    # Take screenshot of top
    screenshot_path = os.path.join(screenshots_dir, 'faq_final_top.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Scroll to general questions
    driver.execute_script("window.scrollTo(0, 600);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'faq_final_general.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Scroll to technical questions
    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'faq_final_technical.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Scroll to contact section
    driver.execute_script("window.scrollTo(0, 3500);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'faq_final_contact.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

finally:
    driver.quit()