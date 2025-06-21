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
    # Load the cti-astro instructor page
    driver.get('https://cti-astro.onrender.com/instructors/george-digweed-mbe')
    time.sleep(4)  # Give it time to load
    
    # Take screenshots at different scroll positions
    # Hero section
    screenshot_path = os.path.join(screenshots_dir, 'cti_astro_instructor_hero.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Scroll to content
    driver.execute_script("window.scrollTo(0, 800);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'cti_astro_instructor_content.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Scroll to achievements
    driver.execute_script("window.scrollTo(0, 1600);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'cti_astro_instructor_achievements.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    
    screenshot_path = os.path.join(screenshots_dir, 'cti_astro_instructor_bottom.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Analyze page elements
    print("\n=== Page Analysis ===")
    
    # Check for specific elements
    elements_to_check = [
        ("stat boxes", ".stat-box"),
        ("achievement items", ".achievement-item"),
        ("timeline", ".timeline"),
        ("course cards", ".course-card"),
        ("video elements", "video"),
        ("gradient headers", ".gradient-text"),
        ("cta buttons", ".cta-button"),
        ("background effects", ".bg-gradient")
    ]
    
    for name, selector in elements_to_check:
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if elements:
                print(f"Found {len(elements)} {name}")
        except:
            pass

finally:
    driver.quit()