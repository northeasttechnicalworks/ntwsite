import re

# Read the newly generated map
with open('e:/websites/NTW/map_counties.html', 'r', encoding='utf-8') as f:
    new_map = f.read()

# Extract inner SVG or the whole SVG
# just take the whole SVG
svg_pattern = r'<svg viewBox="0 0 600 600" width="100%" height="100%" class="deployment-map">.*?</svg>'
new_svg_match = re.search(svg_pattern, new_map, re.DOTALL)
if not new_svg_match:
    print("Could not find SVG in new map")
    exit(1)
new_svg = new_svg_match.group(0)

# Read index.html
with open('e:/websites/NTW/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace the existing SVG in index.html
old_svg_pattern = r'<svg viewBox="0 0 [56]00 [56]00" width="100%" height="100%"(?: class="deployment-map")?>.*?</svg>'
index_html = re.sub(old_svg_pattern, new_svg.replace('\\', '\\\\'), index_html, flags=re.DOTALL)

with open('e:/websites/NTW/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Map injected successfully into index.html")

# Read coverage.html
with open('e:/websites/NTW/coverage.html', 'r', encoding='utf-8') as f:
    coverage_html = f.read()

# Replace the existing SVG in coverage.html (could be 500 500)
old_svg_pattern_coverage = r'<svg viewBox="0 0 500 500" width="100%" height="100%">.*?</svg>'
coverage_html = re.sub(old_svg_pattern_coverage, new_svg.replace('\\', '\\\\'), coverage_html, flags=re.DOTALL)

# verify map.js is linked in coverage.html
if '<script src="js/map.js"></script>' not in coverage_html:
    coverage_html = coverage_html.replace('<script src="js/main.js"></script>', '<script src="js/map.js"></script>\n    <script src="js/main.js"></script>')

with open('e:/websites/NTW/coverage.html', 'w', encoding='utf-8') as f:
    f.write(coverage_html)

print("Map injected successfully into coverage.html")
