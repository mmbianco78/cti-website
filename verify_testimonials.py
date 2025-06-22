#!/usr/bin/env python3
import subprocess

# Fetch the HTML
html = subprocess.check_output(['curl', '-s', 'http://localhost:4321/index3']).decode('utf-8')

# Check for trust badges content
if '<div class="trust-badges"' in html:
    print("✓ Trust badges div found")
    
    # Extract the section around trust badges
    start = html.find('<div class="trust-badges"')
    end = html.find('</div>', start + 200)
    section = html[start:end+6]
    
    print("\nTrust badges HTML snippet:")
    print(section[:500] + "...")
    
if 'ShopperApprovedLogo.svg' in html:
    print("\n✓ ShopperApproved logo referenced")
    
if '4.9' in html:
    print("✓ Rating number (4.9) found")
    
if '295+ Verified Reviews' in html:
    print("✓ 295+ Verified Reviews text found")
    
# Check CSS classes
css_checks = [
    'trust-badges',
    'rating-summary', 
    'rating-number',
    'rating-stars',
    'rating-count'
]

print("\nCSS class checks:")
for cls in css_checks:
    if f'class="{cls}"' in html:
        print(f"  ✓ {cls} class applied")