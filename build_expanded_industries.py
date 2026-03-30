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
  <path d="M 50 250 L 450 250 L 400 300 L 0 300 Z" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  <line x1="50" y1="250" x2="0" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <line x1="150" y1="250" x2="100" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <line x1="250" y1="250" x2="200" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <line x1="350" y1="250" x2="300" y2="300" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <g>
    <animateTransform attributeName="transform" type="translate" values="0 0; 200 0" dur="4s" repeatCount="indefinite" />
    <rect x="80" y="210" width="60" height="40" fill="#5A67D8" transform="skewX(-20)" />
    <path d="M 90 220 L 90 240 M 95 220 L 95 240 M 105 220 L 105 240 M 110 220 L 110 240 M 120 220 L 120 240" stroke="rgba(255,255,255,0.5)" stroke-width="2" transform="skewX(-20)" />
  </g>
  <g>
    <animateTransform attributeName="transform" type="translate" values="-200 0; 0 0" dur="4s" repeatCount="indefinite" />
    <rect x="80" y="210" width="60" height="40" fill="#5A67D8" transform="skewX(-20)" />
    <path d="M 90 220 L 90 240 M 95 220 L 95 240 M 105 220 L 105 240 M 110 220 L 110 240 M 120 220 L 120 240" stroke="rgba(255,255,255,0.5)" stroke-width="2" transform="skewX(-20)" />
  </g>
  <path d="M 230 50 L 270 50 L 260 90 L 240 90 Z" fill="#111827" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
  <polygon points="250,90 200,250 300,250" fill="url(#scanBeam)">
    <animate attributeName="opacity" values="0; 1; 1; 0; 0" dur="4s" keyTimes="0; 0.45; 0.55; 0.6; 1" repeatCount="indefinite" />
  </polygon>
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
  <g transform="translate(250, 200) scale(1, 0.5) rotate(45)">
    <rect x="-150" y="-150" width="300" height="300" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
    <line x1="-50" y1="-150" x2="-50" y2="50" stroke="rgba(255,255,255,0.2)" stroke-width="4" />
    <line x1="-50" y1="50" x2="150" y2="50" stroke="rgba(255,255,255,0.2)" stroke-width="4" />
    <rect x="-130" y="-130" width="60" height="60" fill="#5A67D8" opacity="0.3" />
    <circle cx="-100" cy="-100" r="10" fill="#60A5FA">
      <animate attributeName="opacity" values="1; 0.4; 1" dur="2s" repeatCount="indefinite" />
    </circle>
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
  <rect x="150" y="50" width="200" height="300" rx="8" fill="rgba(0,0,0,0.5)" stroke="rgba(255,255,255,0.2)" stroke-width="4" />
  <rect x="170" y="80" width="160" height="40" rx="2" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  <circle cx="190" cy="100" r="4" fill="#4B5563">
    <animate attributeName="fill" values="#4ade80; #4B5563; #4ade80" dur="1s" repeatCount="indefinite" />
  </circle>
  <path d="M 210 100 L 310 100" stroke="rgba(255,255,255,0.1)" stroke-width="4" stroke-dasharray="8 4" />
  <rect x="170" y="130" width="160" height="40" rx="2" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  <circle cx="190" cy="150" r="4" fill="#4B5563">
    <animate attributeName="fill" values="#4B5563; #eab308; #4B5563" dur="1.5s" repeatCount="indefinite" />
  </circle>
  <path d="M 210 150 L 310 150" stroke="rgba(255,255,255,0.1)" stroke-width="4" stroke-dasharray="8 4" />
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
  <path d="M 50 300 L 450 300 M 50 350 L 450 350" stroke="rgba(255,255,255,0.05)" stroke-width="2" />
  <path d="M 100 250 L 100 350 M 200 250 L 200 350 M 300 250 L 300 350 M 400 250 L 400 350" stroke="rgba(255,255,255,0.05)" stroke-width="2" />
  <rect x="230" y="280" width="40" height="20" fill="rgba(255,255,255,0.2)" />
  <polygon points="220,300 280,300 260,350 240,350" fill="rgba(255,255,255,0.1)" />
  <g transform="translate(250, 280)">
    <g>
      <animateTransform attributeName="transform" type="rotate" values="-20; 20; -20" dur="4s" repeatCount="indefinite" additive="sum" />
      <circle cx="0" cy="0" r="15" fill="#5A67D8" />
      <rect x="-10" y="-100" width="20" height="100" rx="4" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
      <g transform="translate(0, -100)">
        <g>
          <animateTransform attributeName="transform" type="rotate" values="45; -45; 45" dur="4s" repeatCount="indefinite" additive="sum" />
          <circle cx="0" cy="0" r="10" fill="#5A67D8" />
          <rect x="-5" y="-80" width="10" height="80" rx="2" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
          <circle cx="0" cy="-80" r="6" fill="#4ade80">
            <animate attributeName="opacity" values="1; 0.2; 1" dur="1s" repeatCount="indefinite" />
          </circle>
          <polygon points="0,-80 -60,-180 60,-180" fill="rgba(74, 222, 128, 0.15)">
            <animate attributeName="opacity" values="0; 1; 0" dur="2s" repeatCount="indefinite" />
          </polygon>
        </g>
      </g>
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
  <rect x="150" y="100" width="200" height="200" rx="20" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  <g transform="translate(250, 200)">
    <circle r="60" fill="none" stroke="rgba(90, 103, 216, 0.3)" stroke-width="4" stroke-dasharray="20 10">
      <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="10s" repeatCount="indefinite" />
    </circle>
    <circle r="40" fill="none" stroke="rgba(90, 103, 216, 0.5)" stroke-width="2" stroke-dasharray="10 5">
      <animateTransform attributeName="transform" type="rotate" values="360; 0" dur="6s" repeatCount="indefinite" />
    </circle>
    <path d="M -15 -10 L -15 -20 A 15 15 0 0 1 15 -20 L 15 -10" fill="none" stroke="#60A5FA" stroke-width="4" stroke-linecap="round" />
    <rect x="-20" y="-10" width="40" height="30" rx="4" fill="#5A67D8" />
    <circle cx="0" cy="5" r="4" fill="#fff">
      <animate attributeName="fill" values="#fff; #4ade80; #fff" dur="3s" repeatCount="indefinite" />
    </circle>
  </g>
  <rect x="150" y="100" width="200" height="4" fill="#4ade80" filter="url(#glow-green)">
    <animate attributeName="y" values="100; 300; 100" dur="3s" repeatCount="indefinite" />
  </rect>
  <path d="M 50 150 L 90 150 L 90 200 C 90 230 70 250 50 260 C 30 250 10 230 10 200 L 10 150 Z" fill="rgba(74, 222, 128, 0.1)" stroke="#4ade80" stroke-width="2" />
  <path d="M 450 150 L 490 150 L 490 200 C 490 230 470 250 450 260 C 430 250 410 230 410 200 L 410 150 Z" fill="rgba(74, 222, 128, 0.1)" stroke="#4ade80" stroke-width="2" />
  <path d="M 30 200 L 50 220 L 70 180" fill="none" stroke="#4ade80" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    <animate attributeName="stroke-dasharray" values="0 100; 100 100" dur="3s" repeatCount="indefinite" />
  </path>
</svg>"""
    },
    {
        "title": "Education & University Campuses",
        "description": "Orchestrating campus-wide Wi-Fi meshes, paging and intercom systems, and sprawling fiber backbones bridging thousands of students across dozens of academic buildings.",
        "bg": "#0D1A30",
        "svg": """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <!-- Campus Buildings -->
  <rect x="100" y="200" width="80" height="150" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <rect x="220" y="150" width="100" height="200" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
  <rect x="360" y="220" width="60" height="130" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="2" />

  <!-- Fiber links between buildings -->
  <path d="M 180 320 Q 200 340 220 320" fill="none" stroke="#5A67D8" stroke-width="4" />
  <path d="M 320 320 Q 340 340 360 320" fill="none" stroke="#5A67D8" stroke-width="4" />
  
  <circle r="4" fill="#60A5FA">
    <animateMotion dur="1.5s" repeatCount="indefinite" path="M 180 320 Q 200 340 220 320" />
  </circle>
  <circle r="4" fill="#60A5FA">
    <animateMotion dur="1.5s" repeatCount="indefinite" path="M 220 320 Q 200 340 180 320" />
  </circle>
  <circle r="4" fill="#60A5FA">
    <animateMotion dur="1.5s" repeatCount="indefinite" path="M 320 320 Q 340 340 360 320" />
  </circle>

  <!-- Wi-Fi Waves emanating from central building -->
  <g transform="translate(270, 150)">
    <circle r="4" fill="#4ade80" />
    <path d="M -15 -15 A 21 21 0 0 1 15 -15" fill="none" stroke="#4ade80" stroke-width="2" stroke-linecap="round">
      <animate attributeName="opacity" values="0; 1; 0" dur="2s" keyTimes="0; 0.3; 1" repeatCount="indefinite" />
    </path>
    <path d="M -25 -25 A 35 35 0 0 1 25 -25" fill="none" stroke="#4ade80" stroke-width="2" stroke-linecap="round">
      <animate attributeName="opacity" values="0; 1; 0" dur="2s" keyTimes="0; 0.6; 1" begin="0.3s" repeatCount="indefinite" />
    </path>
    <path d="M -35 -35 A 49 49 0 0 1 35 -35" fill="none" stroke="#4ade80" stroke-width="2" stroke-linecap="round">
      <animate attributeName="opacity" values="0; 1; 0" dur="2s" keyTimes="0; 0.9; 1" begin="0.6s" repeatCount="indefinite" />
    </path>
  </g>
</svg>"""
    },
    {
        "title": "Hospitality & Entertainment",
        "description": "Outfitting luxury hotels, convention centers, and massive stadiums with robust high-density Wi-Fi networks and multi-zone commercial AV frameworks where guest experience is everything.",
        "bg": "#15122F",
        "svg": """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <!-- Circular Stadium / Casino Layout -->
  <circle cx="250" cy="200" r="120" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="4" />
  <circle cx="250" cy="200" r="80" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="4" />
  <circle cx="250" cy="200" r="40" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="4" />

  <!-- Concentric Coverage Sweeps -->
  <circle cx="250" cy="200" r="40" fill="none" stroke="#eab308" stroke-width="3">
    <animate attributeName="r" values="40; 160" dur="3s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="1; 0" dur="3s" repeatCount="indefinite" />
  </circle>
  <circle cx="250" cy="200" r="40" fill="none" stroke="#eab308" stroke-width="3">
    <animate attributeName="r" values="40; 160" dur="3s" begin="1.5s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="1; 0" dur="3s" begin="1.5s" repeatCount="indefinite" />
  </circle>

  <!-- Access Points -->
  <g transform="translate(250, 200)">
    <!-- 8 Nodes around ring -->
    <circle cx="0" cy="-80" r="5" fill="#facc15" />
    <circle cx="56.5" cy="-56.5" r="5" fill="#facc15" />
    <circle cx="80" cy="0" r="5" fill="#facc15" />
    <circle cx="56.5" cy="56.5" r="5" fill="#facc15" />
    <circle cx="0" cy="80" r="5" fill="#facc15" />
    <circle cx="-56.5" cy="56.5" r="5" fill="#facc15" />
    <circle cx="-80" cy="0" r="5" fill="#facc15" />
    <circle cx="-56.5" cy="-56.5" r="5" fill="#facc15" />
  </g>
  
  <!-- Audio Waveform in Center -->
  <rect x="235" y="195" width="4" height="10" fill="#fff" rx="2">
    <animate attributeName="height" values="10; 30; 10" dur="0.8s" repeatCount="indefinite" />
    <animate attributeName="y" values="195; 185; 195" dur="0.8s" repeatCount="indefinite" />
  </rect>
  <rect x="245" y="190" width="4" height="20" fill="#fff" rx="2">
    <animate attributeName="height" values="20; 50; 20" dur="0.6s" repeatCount="indefinite" />
    <animate attributeName="y" values="190; 175; 190" dur="0.6s" repeatCount="indefinite" />
  </rect>
  <rect x="255" y="195" width="4" height="10" fill="#fff" rx="2">
    <animate attributeName="height" values="10; 40; 10" dur="1s" repeatCount="indefinite" />
    <animate attributeName="y" values="195; 180; 195" dur="1s" repeatCount="indefinite" />
  </rect>
  <rect x="265" y="193" width="4" height="14" fill="#fff" rx="2">
    <animate attributeName="height" values="14; 24; 14" dur="0.7s" repeatCount="indefinite" />
    <animate attributeName="y" values="193; 188; 193" dur="0.7s" repeatCount="indefinite" />
  </rect>
</svg>"""
    },
    {
        "title": "Government & Public Sector",
        "description": "Securing municipal spaces and state facilities. We navigate bureaucratic compliance, rigid architectural limitations in historical buildings, and highly locked-down security protocols.",
        "bg": "#0D1115",
        "svg": """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <!-- Government Building Silhouette -->
  <polygon points="250,100 150,150 350,150" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <rect x="150" y="150" width="200" height="20" fill="rgba(255,255,255,0.1)" />
  <rect x="160" y="170" width="20" height="100" fill="rgba(255,255,255,0.08)" />
  <rect x="200" y="170" width="20" height="100" fill="rgba(255,255,255,0.08)" />
  <rect x="240" y="170" width="20" height="100" fill="rgba(255,255,255,0.08)" />
  <rect x="280" y="170" width="20" height="100" fill="rgba(255,255,255,0.08)" />
  <rect x="320" y="170" width="20" height="100" fill="rgba(255,255,255,0.08)" />
  <rect x="140" y="270" width="220" height="30" fill="rgba(255,255,255,0.1)" />
  
  <!-- Encrypted Data Shield Rings surrounding it -->
  <g transform="translate(250, 200)">
    <ellipse cx="0" cy="50" rx="160" ry="40" fill="none" stroke="#5A67D8" stroke-width="3" stroke-dasharray="30 20">
      <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="8s" repeatCount="indefinite" />
    </ellipse>
    <ellipse cx="0" cy="50" rx="140" ry="30" fill="none" stroke="#60A5FA" stroke-width="2" stroke-dasharray="10 5">
      <animateTransform attributeName="transform" type="rotate" values="360; 0" dur="5s" repeatCount="indefinite" />
    </ellipse>
    
    <!-- Lock Icon in Center Shield -->
    <path d="M -15 30 L -15 20 A 15 15 0 0 1 15 20 L 15 30" fill="none" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round" />
    <rect x="-20" y="30" width="40" height="30" rx="4" fill="#64748b" stroke="#ffffff" stroke-width="2" />
    <circle cx="0" cy="45" r="4" fill="#fff" />
  </g>
</svg>"""
    }
]

html_cards = []
for idx, ind in enumerate(industries):
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

with open(ind_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Carefully inject deck wrapper
start_idx = html_content.find('<section class="section bg-white">')
if start_idx == -1:
    start_idx = html_content.find('<div class="sticky-deck-wrapper">')

end_idx = html_content.find('<script src="/js/main.js">')
if end_idx == -1:
    end_idx = html_content.find('<footer class="footer"')

html_content = html_content[:start_idx] + deck_wrapper + '\n' + html_content[end_idx:]


with open(ind_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Industries Sticky Deck successfully expanded to 8 Sectors with physics fix applied!")
