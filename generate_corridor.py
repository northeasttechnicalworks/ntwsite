import json
import re

nodes = [
    {"id": "vt", "label": "Vermont", "type": "secondary", "x": 400, "y": 60, "sub": "Extended Coverage"},
    {"id": "nh", "label": "New Hampshire", "type": "secondary", "x": 480, "y": 90, "sub": "Extended Coverage"},
    {"id": "ma", "label": "Massachusetts", "type": "secondary", "x": 420, "y": 180, "sub": "Extended Coverage"},
    {"id": "ri", "label": "Rhode Island", "type": "secondary", "x": 510, "y": 240, "sub": "Extended Coverage"},
    {"id": "ct", "label": "Connecticut", "type": "primary", "x": 370, "y": 270, "sub": "County Segmentation"},
    {"id": "westchester", "label": "Westchester County", "type": "primary", "x": 320, "y": 380, "sub": "Primary Operations"},
    {"id": "nyc", "label": "New York City Metro", "type": "primary", "x": 280, "y": 500, "sub": "All Boroughs"},
    {"id": "li", "label": "Long Island", "type": "primary", "x": 420, "y": 480, "sub": "County Segmentation"},
    {"id": "nnj", "label": "Northern New Jersey", "type": "primary", "x": 210, "y": 600, "sub": "Regional County Groupings"},
    {"id": "pa", "label": "Pennsylvania", "type": "secondary", "x": 80, "y": 560, "sub": "Extended Coverage"},
    {"id": "de", "label": "Delaware", "type": "secondary", "x": 160, "y": 720, "sub": "Extended Coverage"},
    {"id": "md", "label": "Maryland", "type": "secondary", "x": 110, "y": 820, "sub": "Extended Coverage"},
]

edges = [
    ("vt", "ma"),
    ("nh", "ma"),
    ("ma", "ct"),
    ("ma", "ri"),
    ("ct", "westchester"),
    ("westchester", "nyc"),
    ("nyc", "li"),
    ("nyc", "nnj"),
    ("nnj", "pa"),
    ("nnj", "de"),
    ("de", "md")
]

node_dict = {n['id']: n for n in nodes}

svg_lines = []

svg_lines.append('<svg viewBox="0 0 600 900" width="100%" height="100%" class="corridor-map">')

# Definitions for glows and gradients
svg_lines.append('  <defs>')
svg_lines.append('    <filter id="glow-primary" x="-50%" y="-50%" width="200%" height="200%">')
svg_lines.append('      <feGaussianBlur stdDeviation="8" result="blur" />')
svg_lines.append('      <feComposite in="SourceGraphic" in2="blur" operator="over" />')
svg_lines.append('    </filter>')
svg_lines.append('    <filter id="glow-secondary" x="-50%" y="-50%" width="200%" height="200%">')
svg_lines.append('      <feGaussianBlur stdDeviation="4" result="blur" />')
svg_lines.append('      <feComposite in="SourceGraphic" in2="blur" operator="over" />')
svg_lines.append('    </filter>')
svg_lines.append('  </defs>')

# Draw edges
svg_lines.append('  <g class="corridor-edges">')
for u, v in edges:
    n1, n2 = node_dict[u], node_dict[v]
    # Base technical line
    svg_lines.append(f'    <line x1="{n1["x"]}" y1="{n1["y"]}" x2="{n2["x"]}" y2="{n2["y"]}" class="corridor-edge-base" />')
    # Pulse line overlapping
    d = f"M {n1['x']},{n1['y']} L {n2['x']},{n2['y']}"
    svg_lines.append(f'    <path d="{d}" class="corridor-edge-pulse" />')
svg_lines.append('  </g>')

# Draw nodes
svg_lines.append('  <g class="corridor-nodes">')
for n in nodes:
    node_class = f'corridor-node node-{n["type"]}'
    r = 12 if n["type"] == "primary" else 6
    filter_url = 'url(#glow-primary)' if n["type"] == "primary" else 'url(#glow-secondary)'
    
    svg_lines.append(f'    <g class="{node_class}" transform="translate({n["x"]}, {n["y"]})" data-name="{n["label"]}" data-type="{n["type"]}" data-sub="{n["sub"]}">')
    
    # Outer ring
    svg_lines.append(f'      <circle r="{r + 6}" class="node-ring" />')
    # Inner solid dot
    svg_lines.append(f'      <circle r="{r}" class="node-dot" filter="{filter_url}" />')
    
    # Label
    font_size = "18px" if n["type"] == "primary" else "14px"
    font_weight = "bold" if n["type"] == "primary" else "normal"
    text_color = "#ffffff" if n["type"] == "primary" else "rgba(191,197,206,0.7)"
    align = "start" if int(n["x"]) > 300 else "end"
    offset_x = 25 if int(n["x"]) > 300 else -25
    
    # We add labels statically as requested, but also rely on tooltip for subregions
    svg_lines.append(f'      <text x="{offset_x}" y="5" text-anchor="{align}" fill="{text_color}" font-size="{font_size}" font-family="var(--font-family-heading)" font-weight="{font_weight}" class="node-label" style="pointer-events:none;">{n["label"]}</text>')
    
    svg_lines.append(f'    </g>')
svg_lines.append('  </g>')

svg_lines.append('</svg>')

final_svg = "\\n".join(svg_lines)

# Write to files
with open("e:/websites/NTW/index.html", "r", encoding="utf-8") as f:
    idx = f.read()

idx = re.sub(r'<svg viewBox=".*?<\/svg>', final_svg, idx, flags=re.DOTALL)

with open("e:/websites/NTW/index.html", "w", encoding="utf-8") as f:
    f.write(idx)

with open("e:/websites/NTW/coverage.html", "r", encoding="utf-8") as f:
    cov = f.read()

cov = re.sub(r'<svg viewBox=".*?<\/svg>', final_svg, cov, flags=re.DOTALL)

with open("e:/websites/NTW/coverage.html", "w", encoding="utf-8") as f:
    f.write(cov)

print("Corridor map injected into index and coverage.")
