import subprocess
import time

# First, let's use curl to save the HTML and check it
print("Fetching HTML...")
html = subprocess.check_output(['curl', '-s', 'http://localhost:4321/index3']).decode('utf-8')

# Save HTML to file for inspection
with open('index3_output.html', 'w') as f:
    f.write(html)

print(f"HTML length: {len(html)} characters")

# Check for key content
checks = {
    'Testimonials': 'Kyle M.',
    'Features': 'Patented Laser Technology',
    'Instructors': 'George Digweed MBE',
    'Trust badges': 'ShopperApprovedLogo.svg',
    'Video': 'Breaking_Clays_Animation_Hero.mp4'
}

for name, text in checks.items():
    if text in html:
        print(f"✓ {name} found in HTML")
    else:
        print(f"✗ {name} NOT FOUND in HTML")

# Look for potential CSS issues
if 'container-max' in html:
    print("\n✓ container-max class is used")
    
# Check for error messages
if 'Error' in html or 'error' in html:
    print("\n⚠️  Found 'error' in HTML")
    
print("\nHTML saved to index3_output.html for inspection")