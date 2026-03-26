import os
import glob
import re

base_dir = "e:/websites/NTW"

# 1. Extract modern Header and Footer from index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

nav_match = re.search(r'(<div class="top-bar">.*?</nav>)', idx_content, re.DOTALL)
new_nav = nav_match.group(1) if nav_match else ""

ft_match = re.search(r'(<footer class="footer">.*?</footer>)', idx_content, re.DOTALL)
new_footer = ft_match.group(1) if ft_match else ""

if not new_nav or not new_footer:
    print("Error extracting nav or footer from index.html")
    exit(1)

# Force absolute URIs in the nav
new_nav = new_nav.replace('href="index.html"', 'href="/index.html"')
new_nav = new_nav.replace('href="services.html"', 'href="/services.html"')
new_nav = new_nav.replace('href="coverage.html"', 'href="/coverage.html"')
new_nav = new_nav.replace('href="industries.html"', 'href="/industries.html"')
new_nav = new_nav.replace('href="about.html"', 'href="/about.html"')
new_nav = new_nav.replace('href="contact.html"', 'href="/contact.html"')

html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

processed = 0
for filepath in html_files:
    if "index.html" in os.path.basename(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    orig_content = content
    
    # We replace legacy `<header class="navbar"> ... </header>`
    if '<header class="navbar">' in content:
        content = re.sub(r'<header class="navbar">.*?</header>', new_nav, content, flags=re.DOTALL)

    # We replace `<footer class="footer"> ... </footer>`
    if '<footer class="footer">' in content:
        content = re.sub(r'<footer class="footer">.*?</footer>', new_footer, content, flags=re.DOTALL)
        
    if content != orig_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        processed += 1

print(f"Processed and updated {processed} HTML files with new Header/Footer.")

# 2. Update index.html itself to use the Absolute Links
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    idx_content = idx_content.replace(nav_match.group(1), new_nav)
    f.write(idx_content)

# 3. Append legacy CSS compatibility
CSS_APPEND = """
/* --- Legacy Structure Compatibility for Child Pages --- */
.panel {
  background: var(--c-white);
  border: 1px solid var(--c-border-light);
  border-radius: 12px;
  padding: 32px;
  box-shadow: var(--sh-sm);
  margin-bottom: 24px;
}
.theme-dark .panel {
  background: var(--c-surface-dark);
  border: 1px solid var(--c-border-dark);
  color: var(--c-dark-text-body);
}
.theme-dark .panel h2, .theme-dark .panel h3, .theme-dark .panel h4 {
  color: var(--c-white);
}
.btn-secondary {
  background: transparent;
  color: var(--c-text-main);
  border: 1px solid var(--c-border-light);
  display: inline-flex; align-items: center; justify-content: center;
  font-family: var(--font-heading); font-weight: 600;
  padding: 14px 28px; border-radius: 6px;
  transition: all 0.2s ease; cursor: pointer; text-decoration: none;
}
.btn-secondary:hover {
  border-color: var(--c-accent);
  color: var(--c-accent);
}
.theme-dark .btn-secondary { color: var(--c-white); border-color: rgba(255,255,255,0.2); }
.theme-dark .btn-secondary:hover { border-color: var(--c-accent); color: var(--c-white); background: var(--c-accent); }
.blueprint-diagram svg {
  border-radius: 12px;
  background: var(--c-surface-dark);
}
.service-bullets {
  list-style: none; padding: 0;
}
.service-bullets li {
  padding-left: 24px; position: relative; margin-bottom: 8px; font-weight: 500; color: var(--c-text-body);
}
.theme-dark .service-bullets li { color: var(--c-dark-text-body); }
.service-bullets li::before {
  content: "→"; color: var(--c-accent); position: absolute; left: 0; font-weight: bold;
}
.reveal { opacity: 1; transform: none; }
h1 { font-family: var(--font-heading); font-size: 48px; margin-bottom: 24px; letter-spacing: -1px; color: var(--c-text-main); }
.theme-dark h1 { color: var(--c-white); }
.hero-subhead { font-size: 18px; color: var(--c-text-body); line-height: 1.7; }
"""

css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()
if "Legacy Structure Compatibility" not in css_content:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(CSS_APPEND)
    print("Appended legacy compatibility CSS.")
