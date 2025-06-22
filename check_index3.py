#!/usr/bin/env python3
import subprocess
import time

# Wait a moment for server
time.sleep(1)

# Fetch the HTML
try:
    html = subprocess.check_output(['curl', '-s', 'http://localhost:4321/index3'], timeout=5).decode('utf-8')
    print(f"✓ Successfully fetched page ({len(html)} characters)")
    
    # Check for key content
    checks = {
        'Testimonials section': 'Join 5,000+ Shooters Already Improving Their Game',
        'Kyle M. testimonial': 'I gained 8 points on my average in 6 months',
        'Features section': 'Why 5,000+ Shooters Choose CTI',
        'Laser Technology': 'Patented Laser Technology',
        'Instructors section': 'Learn Directly From Your Champions',
        'George Digweed': 'George Digweed MBE',
        'Anthony Matarese': 'Anthony Matarese Jr.',
        'Zachary Kienbaum': 'Zachary Kienbaum',
        'Trust badges': 'ShopperApprovedLogo',
        'Skill levels': 'Wherever You Are',
        'Final CTA': 'Join an Elite Community'
    }
    
    print("\nContent checks:")
    missing = []
    for name, text in checks.items():
        if text in html:
            print(f"  ✓ {name}")
        else:
            print(f"  ✗ {name} NOT FOUND")
            missing.append(name)
    
    if missing:
        print(f"\n⚠️  Missing {len(missing)} sections: {', '.join(missing)}")
        
        # Save HTML for inspection
        with open('index3_debug.html', 'w') as f:
            f.write(html)
        print("HTML saved to index3_debug.html for inspection")
    else:
        print("\n✅ All content sections found!")
        
except subprocess.CalledProcessError as e:
    print(f"❌ Failed to fetch page: {e}")
except subprocess.TimeoutExpired:
    print("❌ Request timed out")