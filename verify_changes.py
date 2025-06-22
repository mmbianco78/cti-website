#!/usr/bin/env python3
import subprocess
import re

# Fetch the HTML
html = subprocess.check_output(['curl', '-s', 'http://localhost:4321/index3']).decode('utf-8')

# Check for play button removal
if 'play-button' in html:
    print("❌ Play button still found in HTML")
else:
    print("✓ Play button successfully removed")

# Check instructor links
instructor_links = re.findall(r'href="(/[^"]*)"', html)
instructor_links = [link for link in instructor_links if any(name in link for name in ['george', 'anthony', 'zach'])]

print("\nInstructor links found:")
for link in instructor_links:
    print(f"  • {link}")

# Expected links
expected = ['/george-digweed', '/anthony-matarese-jr', '/zach-kienbaum']
for link in expected:
    if link in instructor_links:
        print(f"✓ Found correct link: {link}")
    else:
        print(f"❌ Missing expected link: {link}")

# Check that digital.claytargetinstruction.com is not in instructor cards
if 'class="instructor-cta"' in html:
    instructor_cta_sections = re.findall(r'class="instructor-cta"[^>]*href="([^"]*)"', html)
    print(f"\nInstructor CTA links: {instructor_cta_sections}")
    
    for link in instructor_cta_sections:
        if 'digital.claytargetinstruction.com' in link:
            print(f"❌ Still linking to external site: {link}")
        else:
            print(f"✓ Internal link: {link}")