import os
import re

base_dir = "e:/websites/NTW"
cov_path = os.path.join(base_dir, "coverage.html")

nodes = {
    # Primaries
    "New York City Metro": (280, 500, "primary", "All Boroughs"),
    "Westchester County": (300, 420, "primary", "Primary Operations"),
    "Connecticut": (360, 320, "primary", "County Segmentation"),
    "Long Island": (350, 540, "primary", "Nassau & Suffolk"),
    "Northern New Jersey": (220, 560, "primary", "Dense Metro Operations"),
    
    # Secondaries
    "Pennsylvania": (120, 580, "secondary", "Extended Coverage"),
    "Delaware": (160, 680, "secondary", "Extended Coverage"),
    "Maryland": (120, 760, "secondary", "Extended Coverage"),
    
    "Rhode Island": (440, 280, "secondary", "Extended Coverage"),
    "Massachusetts": (420, 200, "secondary", "Extended Coverage"),
    "New Hampshire": (400, 120, "secondary", "Extended Coverage"),
    "Vermont": (320, 80, "secondary", "Extended Coverage"),
    "Maine": (480, 60, "secondary", "Extended Coverage"),
}

# Define bezier paths connecting nodes (Main spine and branches)
connections = [
    # Top edge connections
    ("Maine", "New Hampshire"),
    ("New Hampshire", "Vermont"),
    ("New Hampshire", "Massachusetts"),
    ("Vermont", "Massachusetts"),
    
    # Core Spine
    ("Massachusetts", "Rhode Island"),
    ("Massachusetts", "Connecticut"),
    ("Rhode Island", "Connecticut"),
    ("Connecticut", "Westchester County"),
    ("Westchester County", "New York City Metro"),
    ("New York City Metro", "Long Island"),
    ("New York City Metro", "Northern New Jersey"),
    
    # Southern Edge
    ("Northern New Jersey", "Pennsylvania"),
    ("Northern New Jersey", "Delaware"),
    ("Delaware", "Maryland"),
    ("Pennsylvania", "Maryland"),
]

# Build the Fancy SVG String
svg_pieces = []
svg_pieces.append('''<svg viewBox="0 0 600 900" width="100%" height="100%" class="fancy-corridor-map" preserveAspectRatio="xMidYMid slice">
  <defs>
    <!-- Background Grid Pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1" />
      <circle cx="40" cy="40" r="1.5" fill="rgba(255,255,255,0.06)" />
    </pattern>

    <!-- Glows -->
    <filter id="glow-primary" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-secondary" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-packet">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- HUD Background -->
  <rect width="100%" height="100%" fill="url(#grid)" />
  
  <!-- Outer Corner HUD Elements -->
  <g stroke="rgba(90, 103, 216, 0.5)" stroke-width="3" fill="none">
    <!-- Top Left -->
    <path d="M 20 60 L 20 20 L 60 20" />
    <circle cx="20" cy="20" r="4" fill="#5A67D8" />
    <!-- Top Right -->
    <path d="M 580 60 L 580 20 L 540 20" />
    <circle cx="580" cy="20" r="4" fill="#5A67D8" />
    <!-- Bottom Left -->
    <path d="M 20 840 L 20 880 L 60 880" />
    <circle cx="20" cy="880" r="4" fill="#5A67D8" />
    <!-- Bottom Right -->
    <path d="M 580 840 L 580 880 L 540 880" />
    <circle cx="580" cy="880" r="4" fill="#5A67D8" />
  </g>
''')

# Build Paths
svg_pieces.append('  <g class="corridor-paths">\n')
path_idx = 0
for n1, n2 in connections:
    c1 = nodes[n1]
    c2 = nodes[n2]
    # Simple straight line for Mpath calculation, but represented as a curved quadratic visually if we want.
    # To keep mpath tracking aligned with visual path perfectly, we'll use a subtle Q curve relying on an offset control point.
    cx = (c1[0] + c2[0]) / 2 + 20
    cy = (c1[1] + c2[1]) / 2 - 20
    
    d_str = f"M {c1[0]} {c1[1]} Q {cx} {cy} {c2[0]} {c2[1]}"
    
    # The visible glowing path
    svg_pieces.append(f'    <path id="route-{path_idx}" d="{d_str}" fill="none" stroke="rgba(90, 103, 216, 0.15)" stroke-width="3" stroke-linecap="round" />\n')
    
    # Animated packet traveling the path
    dur = 2 + (path_idx % 3) # randomish duration between 2 and 4s
    svg_pieces.append(f'''    <circle r="3" fill="#60A5FA" filter="url(#glow-packet)">
      <animateMotion dur="{dur}s" repeatCount="indefinite">
        <mpath href="#route-{path_idx}" />
      </animateMotion>
    </circle>\n''')
    path_idx += 1
svg_pieces.append('  </g>\n')

# Build Nodes
svg_pieces.append('  <g class="corridor-nodes">\n')
for name, data in nodes.items():
    x, y, tier, sub = data
    if tier == "primary":
        svg_pieces.append(f'''
    <g class="corridor-node node-primary" transform="translate({x}, {y})">
      <!-- Radar Pulse -->
      <circle r="12" fill="none" stroke="#5A67D8" stroke-width="2">
        <animate attributeName="r" values="12; 40" dur="2s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.8; 0" dur="2s" repeatCount="indefinite" />
      </circle>
      <circle r="12" fill="none" stroke="#5A67D8" stroke-width="2">
        <animate attributeName="r" values="12; 40" begin="1s" dur="2s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.8; 0" begin="1s" dur="2s" repeatCount="indefinite" />
      </circle>
      
      <!-- Core -->
      <circle r="16" class="node-ring" fill="rgba(7, 13, 30, 0.8)" stroke="#5A67D8" stroke-width="2" />
      <circle r="10" class="node-dot" fill="#fff" filter="url(#glow-primary)" />
      
      <text x="25" y="5" text-anchor="start" fill="#ffffff" font-size="18px" font-family="var(--font-heading)" font-weight="700" style="pointer-events:none; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));">{name}</text>
    </g>\n''')
    else:
        svg_pieces.append(f'''
    <g class="corridor-node node-secondary" transform="translate({x}, {y})">
      <circle r="12" fill="rgba(7, 13, 30, 0.8)" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
      <circle r="5" fill="#9CA3AF" filter="url(#glow-secondary)" />
      
      <text x="20" y="4" text-anchor="start" fill="rgba(255,255,255,0.7)" font-size="14px" font-family="var(--font-heading)" font-weight="500" style="pointer-events:none;">{name}</text>
    </g>\n''')
svg_pieces.append('  </g>\n')
svg_pieces.append('</svg>')

final_svg = "".join(svg_pieces)

# Read coverage.html and replace SVG
with open(cov_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace between `<svg viewBox="0 0 600 900"` and `</svg>` inside coverage
new_content = re.sub(r'<svg viewBox="0 0 600 900" width="100%" height="100%" class="corridor-map">.*?</svg>', final_svg, content, flags=re.DOTALL)

with open(cov_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Coverage Map Animated SVG Generated Successfully!")
