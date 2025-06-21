#!/usr/bin/env python3
"""
Selenium-based visual review script for CTI website
Captures screenshots and analyzes page structure at different viewport sizes
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

class CTIVisualReview:
    def __init__(self, base_url="http://localhost:4323"):
        self.base_url = base_url
        self.screenshot_dir = "visual_review_screenshots"
        self.create_screenshot_directory()
        
    def create_screenshot_directory(self):
        """Create directory for screenshots if it doesn't exist"""
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            
    def setup_driver(self, width, height, device_name=""):
        """Setup Chrome driver with specific viewport size"""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in background
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f'--window-size={width},{height}')
        
        if device_name:
            # Mobile emulation
            mobile_emulation = {"deviceName": device_name}
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(width, height)
        return driver
        
    def capture_full_page_screenshot(self, driver, filename):
        """Capture full page screenshot using Chrome DevTools Protocol"""
        # Get the total height of the page
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(driver.get_window_size()['width'], total_height)
        
        # Take screenshot
        screenshot_path = os.path.join(self.screenshot_dir, filename)
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        return screenshot_path
        
    def analyze_hero_section(self, driver):
        """Analyze hero section elements and properties"""
        print("\n=== HERO SECTION ANALYSIS ===")
        
        try:
            # Wait for hero section to load
            hero = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".hero-section, .hero, [class*='hero']"))
            )
            
            # Get hero dimensions
            hero_height = hero.size['height']
            hero_width = hero.size['width']
            print(f"Hero dimensions: {hero_width}x{hero_height}px")
            
            # Analyze text elements
            headings = hero.find_elements(By.CSS_SELECTOR, "h1, h2")
            for i, heading in enumerate(headings):
                text = heading.text
                font_size = heading.value_of_css_property('font-size')
                color = heading.value_of_css_property('color')
                print(f"Heading {i+1}: '{text[:50]}...' - Font: {font_size}, Color: {color}")
                
            # Analyze CTAs
            ctas = hero.find_elements(By.CSS_SELECTOR, "a.btn, button, a[class*='button'], a[class*='cta']")
            print(f"\nCTAs found: {len(ctas)}")
            for i, cta in enumerate(ctas):
                text = cta.text
                bg_color = cta.value_of_css_property('background-color')
                position = cta.location
                print(f"CTA {i+1}: '{text}' - BG: {bg_color}, Position: {position}")
                
            # Check for background images
            bg_image = hero.value_of_css_property('background-image')
            if bg_image and bg_image != 'none':
                print(f"\nBackground image detected: {bg_image[:50]}...")
                
        except Exception as e:
            print(f"Error analyzing hero section: {e}")
            
    def analyze_page_sections(self, driver):
        """Analyze main page sections and their flow"""
        print("\n=== PAGE SECTIONS ANALYSIS ===")
        
        # Common section selectors
        section_selectors = [
            "section", 
            "[class*='section']", 
            "main > div",
            ".container > div"
        ]
        
        sections = []
        for selector in section_selectors:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if elements:
                sections.extend(elements)
                break
                
        print(f"Total sections found: {len(sections)}")
        
        for i, section in enumerate(sections[:10]):  # Analyze first 10 sections
            try:
                # Get section info
                classes = section.get_attribute('class') or 'no-class'
                height = section.size['height']
                
                # Get section heading if exists
                headings = section.find_elements(By.CSS_SELECTOR, "h1, h2, h3")
                heading_text = headings[0].text if headings else "No heading"
                
                print(f"\nSection {i+1}:")
                print(f"  Classes: {classes}")
                print(f"  Height: {height}px")
                print(f"  Heading: {heading_text[:50]}...")
                
                # Check for content density
                text_length = len(section.text)
                print(f"  Text length: {text_length} chars")
                
            except Exception as e:
                print(f"  Error analyzing section {i+1}: {e}")
                
    def check_mobile_responsiveness(self, driver, viewport_width):
        """Check specific mobile responsiveness issues"""
        print(f"\n=== MOBILE CHECK ({viewport_width}px) ===")
        
        # Check for horizontal scroll
        body_width = driver.execute_script("return document.body.scrollWidth")
        viewport_width_actual = driver.execute_script("return window.innerWidth")
        
        if body_width > viewport_width_actual:
            print(f"⚠️  Horizontal scroll detected! Body width: {body_width}px > Viewport: {viewport_width_actual}px")
        else:
            print("✓ No horizontal scroll")
            
        # Check text readability
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")[:5]  # Check first 5 paragraphs
        for i, p in enumerate(paragraphs):
            font_size = p.value_of_css_property('font-size')
            line_height = p.value_of_css_property('line-height')
            print(f"Paragraph {i+1} - Font: {font_size}, Line height: {line_height}")
            
    def run_visual_review(self):
        """Run complete visual review at different viewport sizes"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Test configurations
        test_configs = [
            {"width": 1920, "height": 1080, "name": "desktop_full", "device": ""},
            {"width": 1366, "height": 768, "name": "desktop_laptop", "device": ""},
            {"width": 768, "height": 1024, "name": "tablet", "device": ""},
            {"width": 375, "height": 812, "name": "mobile", "device": "iPhone X"},
        ]
        
        for config in test_configs:
            print(f"\n{'='*60}")
            print(f"Testing: {config['name']} ({config['width']}x{config['height']})")
            print(f"{'='*60}")
            
            driver = self.setup_driver(config['width'], config['height'], config['device'])
            
            try:
                # Load the page
                driver.get(self.base_url)
                time.sleep(3)  # Wait for page to fully load
                
                # Take initial viewport screenshot
                screenshot_name = f"{timestamp}_{config['name']}_viewport.png"
                driver.save_screenshot(os.path.join(self.screenshot_dir, screenshot_name))
                print(f"Viewport screenshot saved: {screenshot_name}")
                
                # Analyze hero section
                self.analyze_hero_section(driver)
                
                # Analyze page sections
                self.analyze_page_sections(driver)
                
                # Mobile-specific checks
                if config['width'] < 768:
                    self.check_mobile_responsiveness(driver, config['width'])
                
                # Take full page screenshot
                full_screenshot_name = f"{timestamp}_{config['name']}_full.png"
                self.capture_full_page_screenshot(driver, full_screenshot_name)
                
                # Scroll to check lazy loading
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2)")
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(1)
                
                # Take screenshot after scrolling
                after_scroll_name = f"{timestamp}_{config['name']}_after_scroll.png"
                driver.save_screenshot(os.path.join(self.screenshot_dir, after_scroll_name))
                
            except Exception as e:
                print(f"Error during review: {e}")
                
            finally:
                driver.quit()
                
        print(f"\n\n=== VISUAL REVIEW COMPLETE ===")
        print(f"Screenshots saved in: {self.screenshot_dir}")
        print("\nSummary:")
        print("1. Check screenshots for visual issues")
        print("2. Review console output for technical details")
        print("3. Pay special attention to mobile layouts")
        
if __name__ == "__main__":
    reviewer = CTIVisualReview()
    reviewer.run_visual_review()