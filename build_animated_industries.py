import os
import re

base_dir = "e:/websites/NTW"
ind_path = os.path.join(base_dir, "industries.html")
css_path = os.path.join(base_dir, "css", "styles.css")

industries = [
    {
        "title": "Retail & National Logistics",
        "description": "High-volume, multi-site deployments executed with military precision. We deploy standardized infrastructure across 50+ locations securely matching your aggressive store opening windows.",
        "bg": "var(--c-surface-dark)",
        "svg": """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="scanBeam" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0" />
      <stop offset="90%" stop-color="#ef4444" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#ef4444" stop-opacity="1" />
    </linearGradient>
  </defs>
  <!-- Conveyor Belt -->
  <path d="M 50 250 L 450 250 L 400 300 L 0 300 Z" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  <line x1="50" y1="250" x2="0" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <line x1="150" y1="250" x2="100" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <line x1="250" y1="250" x2="200" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <line x1="350" y1="250" x2="300" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  
  <!-- Packages -->
  <g>
    <animateTransform attributeName="transform" type="translate" values="0 0; 200 0" dur="4s" repeatCount="indefinite" />
    <rect x="80" y="210" width="60" height="40" fill="#5A67D8" transform="skewX(-20)" />
    <!-- Barcode -->
    <path d="M 90 220 L 90 240 M 95 220 L 95 240 M 105 220 L 105 240 M 110 220 L 110 240 M 120 220 L 120 240" stroke="rgba(255,255,255,0.5)" stroke-width="2" transform="skewX(-20)" />
  </g>
  <g>
    <animateTransform attributeName="transform" type="translate" values="-200 0; 0 0" dur="4s" repeatCount="indefinite" />
    <rect x="80" y="210" width="60" height="40" fill="#5A67D8" transform="skewX(-20)" />
    <!-- Barcode -->
    <path d="M 90 220 L 90 240 M 95 220 L 95 240 M 105 220 L 105 240 M 110 220 L 110 240 M 120 220 L 120 240" stroke="rgba(255,255,255,0.5)" stroke-width="2" transform="skewX(-20)" />
  </g>

  <!-- Laser Scanner Overhead -->
  <path d="M 230 50 L 270 50 L 260 90 L 240 90 Z" fill="#111827" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
  <!-- Sweeping Laser Beam -->
  <polygon points="250,90 200,250 300,250" fill="url(#scanBeam)">
    <animate attributeName="opacity" values="0; 1; 1; 0; 0" dur="4s" keyTimes="0; 0.45; 0.55; 0.6; 1" repeatCount="indefinite" />
  </polygon>
  <!-- Scan Success LED -->
  <circle cx="250" cy="70" r="4" fill="#111827">
    <animate attributeName="fill" values="#111827; #4ade80; #111827" dur="4s" keyTimes="0; 0.5; 0.6" repeatCount="indefinite" />
  </circle>
</svg>"""
    },
    {
        "title": "Commercial Office & Enterprise IT",
        "description": "IDF buildouts, dense Cat6A workstation meshes, tenant-safe access control, and highly coordinated, low-disruption execution tailored for white-collar workflows.",
        "bg": "#0B1120",
        "svg": """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <!-- Isometric Floorplan Grid -->
  <g transform="translate(250, 200) scale(1, 0.5) rotate(45)">
    <!-- Base Floor -->
    <rect x="-150" y="-150" width="300" height="300" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
    <!-- Inner Walls -->
    <line x1="-50" y1="-150" x2="-50" y2="50" stroke="rgba(255,255,255,0.2)" stroke-width="4" />
    <line x1="-50" y1="50" x2="150" y2="50" stroke="rgba(255,255,255,0.2)" stroke-width="4" />
    
    <!-- MDF Room -->
    <rect x="-130" y="-130" width="60" height="60" fill="#5A67D8" opacity="0.3" />
    <circle cx="-100" cy="-100" r="10" fill="#60A5FA">
      <animate attributeName="opacity" values="1; 0.4; 1" dur="2s" repeatCount="indefinite" />
    </circle>
    
    <!-- Workstations -->
    <rect x="0" y="-100" width="40" height="40" fill="rgba(255,255,255,0.1)" />
    <circle cx="20" cy="-80" r="5" fill="#4B5563">
      <animate attributeName="fill" values="#4B5563; #4ade80; #4B5563" dur="3s" begin="0s" repeatCount="indefinite" />
    </circle>
    
    <rect x="80" y="-100" width="40" height="40" fill="rgba(255,255,255,0.1)" />
    <circle cx="100" cy="-80" r="5" fill="#4B5563">
      <animate attributeName="fill" values="#4B5563; #4ade80; #4B5563" dur="3s" begin="0.5s" repeatCount="indefinite" />
    </circle>

    <rect x="0" y="80" width="40" height="40" fill="rgba(255,255,255,0.1)" />
    <circle cx="20" cy="100" r="5" fill="#4B5563">
      <animate attributeName="fill" values="#4B5563; #4ade80; #4B5563" dur="3s" begin="1s" repeatCount="indefinite" />
    </circle>
    
    <!-- Data Links pulsing from MDF to workstations -->
    <path d="M -100 -100 L -20 -100 L 20 -80" fill="none" stroke="#60A5FA" stroke-width="2" stroke-dasharray="4 4">
      <animate attributeName="stroke-dashoffset" values="8; 0" dur="1s" repeatCount="indefinite" />
    </path>
    <path d="M -100 -100 L -20 -100 L 100 -80" fill="none" stroke="#60A5FA" stroke-width="2" stroke-dasharray="4 4">
      <animate attributeName="stroke-dashoffset" values="8; 0" dur="1s" repeatCount="indefinite" />
    </path>
    <path d="M -100 -100 L -100 100 L 20 100" fill="none" stroke="#60A5FA" stroke-width="2" stroke-dasharray="4 4">
      <animate attributeName="stroke-dashoffset" values="8; 0" dur="1s" repeatCount="indefinite" />
    </path>
  </g>
</svg>"""
    },
    {
        "title": "Mission-Critical Data Centers",
        "description": "Colocation facilities and edge computing hubs. We dress vast overhead fiber trays, terminate massive high-density copper bundles, and execute zero-downtime infrastructure grooming.",
        "bg": "#121A2F",
        "svg": """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <defs>
    <filter id="glow-rack">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <!-- Main Frame -->
  <rect x="150" y="50" width="200" height="300" rx="8" fill="rgba(0,0,0,0.5)" stroke="rgba(255,255,255,0.2)" stroke-width="4" />
  
  <!-- Server Units -->
  <!-- Unit 1 -->
  <rect x="170" y="80" width="160" height="40" rx="2" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  <circle cx="190" cy="100" r="4" fill="#4B5563">
    <animate attributeName="fill" values="#4ade80; #4B5563; #4ade80" dur="1s" repeatCount="indefinite" />
  </circle>
  <path d="M 210 100 L 310 100" stroke="rgba(255,255,255,0.1)" stroke-width="4" stroke-dasharray="8 4" />
  
  <!-- Unit 2 -->
  <rect x="170" y="130" width="160" height="40" rx="2" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  <circle cx="190" cy="150" r="4" fill="#4B5563">
    <animate attributeName="fill" values="#4B5563; #eab308; #4B5563" dur="1.5s" repeatCount="indefinite" />
  </circle>
  <path d="M 210 150 L 310 150" stroke="rgba(255,255,255,0.1)" stroke-width="4" stroke-dasharray="8 4" />
  
  <!-- Cooling Fans -->
  <g transform="translate(170, 250)">
    <rect x="0" y="0" width="160" height="70" rx="2" fill="rgba(0,0,0,0.8)" stroke="#5A67D8" stroke-width="2" />
    <g transform="translate(40, 35)">
      <circle r="25" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
      <path d="M 0 -20 L 0 20 M -20 0 L 20 0 M -14 -14 L 14 14 M -14 14 L 14 -14" stroke="rgba(255,255,255,0.4)" stroke-width="4">
        <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="0.5s" repeatCount="indefinite" />
      </path>
    </g>
    <g transform="translate(120, 35)">
      <circle r="25" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
      <path d="M 0 -20 L 0 20 M -20 0 L 20 0 M -14 -14 L 14 14 M -14 14 L 14 -14" stroke="rgba(255,255,255,0.4)" stroke-width="4">
        <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="0.5s" repeatCount="indefinite" />
      </path>
    </g>
  </g>
  
  <!-- Outer Fiber Cabling looping down the side -->
  <path d="M 360 80 Q 450 150 360 300" fill="none" stroke="#5A67D8" stroke-width="6" opacity="0.3" />
  <circle r="6" fill="#60A5FA" filter="url(#glow-rack)">
    <animateMotion dur="2s" repeatCount="indefinite" path="M 360 80 Q 450 150 360 300" />
  </circle>
  <circle r="6" fill="#60A5FA" filter="url(#glow-rack)">
    <animateMotion dur="2s" begin="1s" repeatCount="indefinite" path="M 360 80 Q 450 150 360 300" />
  </circle>
</svg>"""
    },
    {
        "title": "Industrial & Manufacturing",
        "description": "Hard-hat deployment zones. We wire heavy manufacturing floors for Wi-Fi automation, sensor arrays, and mount robust ruggedized surveillance frameworks high in the rafters.",
        "bg": "#0D1426",
        "svg": """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <!-- Factory Background -->
  <path d="M 50 300 L 450 300 M 50 350 L 450 350" stroke="rgba(255,255,255,0.05)" stroke-width="2" />
  <path d="M 100 250 L 100 350 M 200 250 L 200 350 M 300 250 L 300 350 M 400 250 L 400 350" stroke="rgba(255,255,255,0.05)" stroke-width="2" />

  <!-- Robotic Arm Base -->
  <rect x="230" y="280" width="40" height="20" fill="rgba(255,255,255,0.2)" />
  <polygon points="220,300 280,300 260,350 240,350" fill="rgba(255,255,255,0.1)" />
  
  <!-- Robotic Arm Mechanism -->
  <g transform="translate(250, 280)">
    <!-- Arm Base Rotate -->
    <animateTransform attributeName="transform" type="rotate" values="-20; 20; -20" dur="4s" repeatCount="indefinite" />
    
    <circle cx="0" cy="0" r="15" fill="#5A67D8" />
    <rect x="-10" y="-100" width="20" height="100" rx="4" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
    
    <g transform="translate(0, -100)">
      <!-- Arm Joint Rotate -->
      <animateTransform attributeName="transform" type="rotate" values="45; -45; 45" dur="4s" repeatCount="indefinite" />
      <circle cx="0" cy="0" r="10" fill="#5A67D8" />
      <rect x="-5" y="-80" width="10" height="80" rx="2" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
      
      <!-- Sensor Node at end of arm -->
      <circle cx="0" cy="-80" r="6" fill="#4ade80">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="1s" repeatCount="indefinite" />
      </circle>
      
      <!-- Sensor Scan Cone -->
      <polygon points="0,-80 -60,-180 60,-180" fill="rgba(74, 222, 128, 0.15)">
        <animate attributeName="opacity" values="0; 1; 0" dur="2s" repeatCount="indefinite" />
      </polygon>
    </g>
  </g>
</svg>"""
    },
    {
        "title": "Healthcare & Pharmaceuticals",
        "description": "Sterile network plotting. Deploying complex nurse call systems, compliant patient Wi-Fi arrays, and highly secure biometric access points across hospital corridors without disrupting patient care.",
        "bg": "#0B1526",
        "svg": """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <defs>
    <filter id="glow-green">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  
  <!-- Biometric Hand/Identity Scan Plate -->
  <rect x="150" y="100" width="200" height="200" rx="20" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  
  <!-- Fingerprint / Crosshair -->
  <g transform="translate(250, 200)">
    <circle r="60" fill="none" stroke="rgba(90, 103, 216, 0.3)" stroke-width="4" stroke-dasharray="20 10">
      <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="10s" repeatCount="indefinite" />
    </circle>
    <circle r="40" fill="none" stroke="rgba(90, 103, 216, 0.5)" stroke-width="2" stroke-dasharray="10 5">
      <animateTransform attributeName="transform" type="rotate" values="360; 0" dur="6s" repeatCount="indefinite" />
    </circle>
    
    <!-- Central Identity Lock -->
    <path d="M -15 -10 L -15 -20 A 15 15 0 0 1 15 -20 L 15 -10" fill="none" stroke="#60A5FA" stroke-width="4" stroke-linecap="round" />
    <rect x="-20" y="-10" width="40" height="30" rx="4" fill="#5A67D8" />
    
    <circle cx="0" cy="5" r="4" fill="#fff">
      <animate attributeName="fill" values="#fff; #4ade80; #fff" dur="3s" repeatCount="indefinite" />
    </circle>
  </g>

  <!-- Scanning Laser Bar -->
  <rect x="150" y="100" width="200" height="4" fill="#4ade80" filter="url(#glow-green)">
    <animate attributeName="y" values="100; 300; 100" dur="3s" repeatCount="indefinite" />
  </rect>
  
  <!-- Shield Icon Overlay -->
  <path d="M 50 150 L 90 150 L 90 200 C 90 230 70 250 50 260 C 30 250 10 230 10 200 L 10 150 Z" fill="rgba(74, 222, 128, 0.1)" stroke="#4ade80" stroke-width="2" />
  <path d="M 450 150 L 490 150 L 490 200 C 490 230 470 250 450 260 C 430 250 410 230 410 200 L 410 150 Z" fill="rgba(74, 222, 128, 0.1)" stroke="#4ade80" stroke-width="2" />
  
  <path d="M 30 200 L 50 220 L 70 180" fill="none" stroke="#4ade80" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    <animate attributeName="stroke-dasharray" values="0 100; 100 100" dur="3s" repeatCount="indefinite" />
  </path>
</svg>"""
    }
]

html_cards = []
for idx, ind in enumerate(industries):
    # Sticky overlapping mechanics:
    # Each specific card uses sticky. It's inside a flex column containing them.
    # The sticky wrapper gives the physical feeling of cards stacking on top of each other.
    card_html = f'''
        <div class="sticky-card" style="background: {ind['bg']}; z-index: {idx + 1};">
            <div class="container h-full">
                <div class="sticky-card-inner">
                    <div class="sticky-text">
                        <div class="sticky-tag">Sector 0{idx+1}</div>
                        <h2>{ind['title']}</h2>
                        <p>{ind['description']}</p>
                    </div>
                    <div class="sticky-visual">
                        {ind['svg']}
                    </div>
                </div>
            </div>
        </div>
'''
    html_cards.append(card_html)

deck_wrapper = f'''
    <div class="sticky-deck-wrapper">
        {''.join(html_cards)}
    </div>
'''

# Update CSS for sticky deck
sticky_css = '''
/* Sticky Card Deck Layout for Industries */
.sticky-deck-wrapper {
  position: relative;
  width: 100%;
  padding-bottom: 150px;
  background: var(--c-surface-dark);
}
.sticky-card {
  position: sticky;
  top: 80px; /* Offset for header */
  height: 90vh;
  min-height: 800px;
  display: flex;
  align-items: center;
  border-top: 1px solid rgba(255,255,255,0.05);
  box-shadow: 0 -10px 40px rgba(0,0,0,0.5);
}
.sticky-card-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 80px;
}
.sticky-text {
  width: 45%;
}
.sticky-tag {
  display: inline-block;
  color: var(--c-accent);
  font-family: var(--font-body);
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 24px;
  padding: 6px 12px;
  border: 1px solid rgba(90, 103, 216, 0.4);
  border-radius: 4px;
}
.sticky-text h2 {
  font-family: var(--font-heading);
  font-size: 56px;
  color: var(--c-white);
  line-height: 1.1;
  margin-bottom: 24px;
}
.sticky-text p {
  font-size: 20px;
  color: var(--c-dark-text-body);
  line-height: 1.7;
}
.sticky-visual {
  width: 50%;
  height: 100%;
  min-height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (max-width: 900px) {
  .sticky-card {
    height: auto;
    position: relative;
    top: auto;
    padding: 80px 0;
  }
  .sticky-card-inner {
    flex-direction: column;
  }
  .sticky-text, .sticky-visual {
    width: 100%;
  }
  .sticky-text h2 { font-size: 40px; }
}
'''

with open(css_path, "r", encoding="utf-8") as f:
    current_css = f.read()
if ".sticky-deck-wrapper" not in current_css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n" + sticky_css)

with open(ind_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace everything from `<section class="section bg-white">` down to `</section>` (excluding footer)
html_content = re.sub(r'<section class="section bg-white">.*?</section>', deck_wrapper, html_content, flags=re.DOTALL)

with open(ind_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Industries Sticky Deck successfully compiled and injected!")
