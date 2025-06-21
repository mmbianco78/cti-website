#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

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
    
    # Find first FAQ answer
    answer = driver.find_element(By.CLASS_NAME, "faq-answer")
    
    # Get computed styles
    styles = driver.execute_script("""
        var elem = arguments[0];
        var styles = window.getComputedStyle(elem);
        return {
            display: styles.display,
            visibility: styles.visibility,
            opacity: styles.opacity,
            color: styles.color,
            fontSize: styles.fontSize,
            lineHeight: styles.lineHeight,
            height: styles.height,
            overflow: styles.overflow,
            textContent: elem.textContent
        };
    """, answer)
    
    print("Answer element computed styles:")
    for key, value in styles.items():
        print(f"{key}: {value}")
    
    # Get parent styles
    parent = answer.find_element(By.XPATH, "..")
    parent_styles = driver.execute_script("""
        var elem = arguments[0];
        var styles = window.getComputedStyle(elem);
        return {
            height: styles.height,
            overflow: styles.overflow,
            display: styles.display
        };
    """, parent)
    
    print("\nParent element computed styles:")
    for key, value in parent_styles.items():
        print(f"{key}: {value}")

finally:
    driver.quit()