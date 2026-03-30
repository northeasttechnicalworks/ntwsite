import os
import re

base_dir = "e:/websites/NTW"

# Extract header from index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

nav_match = re.search(r'(<header class="navbar">.*?</header>)', idx_content, re.DOTALL)
if not nav_match:
    print("Could not find navbar in index.html!")
    exit(1)

new_nav = nav_match.group(1)

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') and file != 'index.html':
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace the <header class="navbar"> block
            new_content = re.sub(r'<header class="navbar">.*?</header>', new_nav, content, flags=re.DOTALL)
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1
                
print(f"Successfully synced global navbar to {count} HTML files!")
