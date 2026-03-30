import os
import re

base_dir = "e:/websites/NTW"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

# Grab the footer + the mobile CTA section
# We'll use a regex that captures from <footer class="footer"... to </div> just before the main.js script
match = re.search(r'(<footer class="footer".*?<!-- MOBILE STICKY CTA BAR -->.*?</div>)', idx_content, re.DOTALL)

if not match:
    print("Could not extract footer and CTA from index.html")
    exit(1)

new_footer_block = match.group(1)

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') and file != 'index.html':
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Remove old footer completely. Some might have the mobilecta already, some might not.
            # Easiest way is to remove everything from <footer class="footer"> down to </body>
            # Wait, </body> is at the end. I can just regex replace <footer class="footer"... to </footer> or the next script.
            
            # Let's replace the old footer (and maybe existing CTA) with the new combined block
            # If the file hasn't been updated with CTA, it only has a footer.
            if "<!-- MOBILE STICKY CTA BAR -->" in content:
                # Replace footer to the end of CTA
                content = re.sub(r'<footer class="footer".*?<!-- MOBILE STICKY CTA BAR -->.*?</div>', new_footer_block, content, flags=re.DOTALL)
            else:
                # Replace just footer with the combined block
                content = re.sub(r'<footer class="footer".*?</footer>', new_footer_block, content, flags=re.DOTALL)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
print(f"Successfully synced global CTA block to {count} HTML files!")
