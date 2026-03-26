import os
import re

base_dir = "e:/websites/NTW"

# 1. Append Timeline CSS to styles.css if not present
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

timeline_css = """
/* Services Timeline Layout */
.timeline-wrapper { position: relative; padding: 120px 0; max-width: 1100px; margin: 0 auto; }
.timeline-tracker { position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; background: var(--c-border-light); transform: translateX(-50%); z-index: 1; }
.timeline-fill { position: absolute; top: 0; left: 0; width: 100%; height: 0%; background: var(--c-accent); transition: height 0.1s linear; }
.timeline-step { display: flex; align-items: center; justify-content: space-between; margin-bottom: 120px; position: relative; z-index: 2; transition: opacity 0.8s, transform 0.8s; opacity: 0; transform: translateY(40px); }
.timeline-step.is-revealed { opacity: 1; transform: translateY(0); }
.timeline-step:last-child { margin-bottom: 0; }
.timeline-content { width: 42%; }
.timeline-graphic { width: 48%; background: var(--c-surface-dark); border-radius: 20px; display: flex; justify-content: center; align-items: center; border: 1px solid var(--c-dark-border); box-shadow: var(--sh-md); aspect-ratio: 4/3; position: relative; overflow: hidden; }
.timeline-step:nth-child(even) { flex-direction: row-reverse; }
.timeline-step:nth-child(even) .timeline-content { text-align: left; }
.timeline-step:nth-child(odd) .timeline-content { text-align: right; }
.timeline-step:nth-child(odd) .timeline-content .svc-icon-wrap { margin-left: auto; margin-right: 0; }
.timeline-dot { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 24px; height: 24px; background: var(--c-white); border: 4px solid var(--c-border-light); border-radius: 50%; flex-shrink: 0; transition: all 0.4s ease; z-index: 3; box-shadow: 0 0 0 0px rgba(90, 103, 216, 0); }
.timeline-step.is-active .timeline-dot { border-color: var(--c-accent); box-shadow: 0 0 0 8px rgba(90, 103, 216, 0.2); }

@media (max-width: 900px) {
  .timeline-tracker { left: 24px; transform: none; }
  .timeline-dot { left: 24px; transform: translateY(-50%); top: 40px;}
  .timeline-step { flex-direction: column !important; align-items: flex-start; margin-bottom: 80px; padding-left: 64px; }
  .timeline-content, .timeline-graphic { width: 100%; text-align: left !important; }
  .timeline-content .svc-icon-wrap { margin-left: 0 !important; }
  .timeline-graphic { margin-top: 32px; }
}
"""

if ".timeline-wrapper" not in css_content:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(timeline_css)
    print("Appended Timeline CSS to styles.css")

# 2. Extract header/footer from index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

nav_match = re.search(r'(<div class="top-bar">.*?</nav>)', idx_content, re.DOTALL)
new_nav = nav_match.group(1) if nav_match else ""

ft_match = re.search(r'(<footer class="footer">.*?</footer>)', idx_content, re.DOTALL)
new_footer = ft_match.group(1) if ft_match else ""


# 3. Create SVG Motion Graphics
svg_cabling = """
<svg viewBox="0 0 400 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cableGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#5A67D8" stop-opacity="0" />
      <stop offset="50%" stop-color="#5A67D8" stop-opacity="1" />
      <stop offset="100%" stop-color="#5A67D8" stop-opacity="0" />
    </linearGradient>
  </defs>
  <!-- Background Grid -->
  <path d="M0 100 L400 100 M0 200 L400 200 M100 0 L100 300 M200 0 L200 300 M300 0 L300 300" stroke="rgba(255,255,255,0.03)" stroke-width="1" />
  
  <!-- Server Racks -->
  <rect x="40" y="60" width="60" height="180" rx="4" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  <rect x="300" y="60" width="60" height="180" rx="4" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="2" />

  <!-- Cables -->
  <path id="path1" d="M100 100 C 150 100, 250 150, 300 150" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="4" stroke-linecap="round"/>
  <path id="path2" d="M100 150 C 180 150, 220 100, 300 100" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="4" stroke-linecap="round"/>
  <path id="path3" d="M100 200 C 200 200, 200 200, 300 200" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="4" stroke-linecap="round"/>

  <!-- Flowing Packets -->
  <circle r="4" fill="#5A67D8">
    <animateMotion dur="2.5s" repeatCount="indefinite" keyPoints="0;1" keyTimes="0;1">
      <mpath href="#path1" />
    </animateMotion>
  </circle>
  <circle r="4" fill="#60A5FA">
    <animateMotion dur="3s" repeatCount="indefinite" begin="1s" keyPoints="0;1" keyTimes="0;1">
      <mpath href="#path2" />
    </animateMotion>
  </circle>
  <circle r="4" fill="#5A67D8">
    <animateMotion dur="2s" repeatCount="indefinite" begin="0.5s" keyPoints="0;1" keyTimes="0;1">
      <mpath href="#path3" />
    </animateMotion>
  </circle>

  <!-- Ports -->
  <circle cx="100" cy="100" r="4" fill="#4B5563" />
  <circle cx="100" cy="150" r="4" fill="#4B5563" />
  <circle cx="100" cy="200" r="4" fill="#4B5563" />
  <circle cx="300" cy="150" r="4" fill="#4B5563" />
  <circle cx="300" cy="100" r="4" fill="#4B5563" />
  <circle cx="300" cy="200" r="4" fill="#4B5563" />
</svg>
"""

svg_surveillance = """
<svg viewBox="0 0 400 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="radarGrad" cx="50%" cy="0%" r="100%" fx="50%" fy="0%">
      <stop offset="0%" stop-color="rgba(90, 103, 216, 0.4)" />
      <stop offset="100%" stop-color="rgba(90, 103, 216, 0)" />
    </radialGradient>
    <clipPath id="coneClip">
      <path d="M200 60 L60 250 A 180 30 0 0 0 340 250 Z" />
    </clipPath>
  </defs>

  <path d="M0 100 L400 100 M0 200 L400 200 M100 0 L100 300 M200 0 L200 300 M300 0 L300 300" stroke="rgba(255,255,255,0.03)" stroke-width="1" />

  <!-- Base View Cone -->
  <path d="M200 60 L60 250 A 180 30 0 0 0 340 250 Z" fill="rgba(255,255,255,0.02)" />

  <!-- Animated Sensor Sweep -->
  <g clip-path="url(#coneClip)">
    <g transform="translate(200 60)">
      <polygon points="0,0 -80,220 80,220" fill="url(#radarGrad)">
        <animateTransform attributeName="transform" type="rotate" values="-45; 45; -45" dur="6s" repeatCount="indefinite" />
      </polygon>
    </g>
  </g>

  <!-- Identified targets (squares) -->
  <rect x="120" y="180" width="20" height="20" rx="4" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2">
    <animate attributeName="stroke" values="rgba(255,255,255,0.3); #4ade80; rgba(255,255,255,0.3)" dur="6s" repeatCount="indefinite" />
  </rect>
  <rect x="260" y="210" width="20" height="20" rx="4" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2">
    <animate attributeName="stroke" values="rgba(255,255,255,0.3); #4ade80; rgba(255,255,255,0.3)" begin="2s" dur="6s" repeatCount="indefinite" />
  </rect>

  <!-- Dome Camera -->
  <circle cx="200" cy="50" r="16" fill="rgba(255,255,255,0.8)" />
  <path d="M184 50 A 16 16 0 0 0 216 50 Z" fill="#111827" />
  <circle cx="200" cy="58" r="4" fill="#DC2626">
    <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite" />
  </circle>
  <path d="M170 34 L230 34" stroke="rgba(255,255,255,0.8)" stroke-width="6" stroke-linecap="round" />
</svg>
"""

svg_access = """
<svg viewBox="0 0 400 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 100 L400 100 M0 200 L400 200 M100 0 L100 300 M200 0 L200 300 M300 0 L300 300" stroke="rgba(255,255,255,0.03)" stroke-width="1" />
  
  <!-- Reader Backplate -->
  <rect x="150" y="80" width="100" height="140" rx="12" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
  <rect x="170" y="100" width="60" height="60" rx="8" fill="rgba(255,255,255,0.1)" />
  
  <!-- Status LED -->
  <circle cx="200" cy="180" r="8" fill="#111827" stroke="rgba(255,255,255,0.2)" stroke-width="2">
    <animate attributeName="fill" values="#111827; #111827; #4ade80; #111827; #111827" keyTimes="0; 0.4; 0.5; 0.8; 1" dur="4s" repeatCount="indefinite" />
    <animate attributeName="stroke" values="rgba(255,255,255,0.2); rgba(255,255,255,0.2); #4ade80; rgba(255,255,255,0.2); rgba(255,255,255,0.2)" keyTimes="0; 0.4; 0.5; 0.8; 1" dur="4s" repeatCount="indefinite" />
  </circle>

  <!-- Animated Swipe Card -->
  <g>
    <animateTransform attributeName="transform" type="translate" values="50 0; -10 0; -10 0; 50 0" keyTimes="0; 0.4; 0.8; 1" dur="4s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="0; 1; 1; 0" keyTimes="0; 0.4; 0.8; 1" dur="4s" repeatCount="indefinite" />
    <rect x="230" y="110" width="60" height="40" rx="4" fill="#5A67D8" transform="rotate(-15 260 130)" />
    <rect x="235" y="125" width="20" height="15" rx="2" fill="rgba(255,255,255,0.5)" transform="rotate(-15 260 130)" />
    <line x1="260" y1="125" x2="280" y2="125" stroke="rgba(255,255,255,0.5)" stroke-width="2" transform="rotate(-15 260 130)" />
    <line x1="260" y1="135" x2="275" y2="135" stroke="rgba(255,255,255,0.5)" stroke-width="2" transform="rotate(-15 260 130)" />
  </g>

  <!-- Unlock Ripples -->
  <circle cx="200" cy="130" r="10" fill="none" stroke="#4ade80" stroke-width="2" opacity="0">
    <animate attributeName="r" values="10; 80" keyTimes="0; 1" begin="1.6s" dur="1s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="0; 0.8; 0" keyTimes="0; 0.1; 1" begin="1.6s" dur="1s" repeatCount="indefinite" />
  </circle>
</svg>
"""

svg_intrusion = """
<svg viewBox="0 0 400 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 100 L400 100 M0 200 L400 200 M100 0 L100 300 M200 0 L200 300 M300 0 L300 300" stroke="rgba(255,255,255,0.03)" stroke-width="1" />
  
  <g transform="translate(200, 150)">
    <!-- Expanding Radar Pulses -->
    <circle cx="0" cy="0" r="0" fill="none" stroke="#5A67D8" stroke-width="2">
      <animate attributeName="r" values="0; 150" dur="3s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="1; 0" dur="3s" repeatCount="indefinite" />
    </circle>
    <circle cx="0" cy="0" r="0" fill="none" stroke="#5A67D8" stroke-width="2">
      <animate attributeName="r" values="0; 150" begin="1s" dur="3s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="1; 0" begin="1s" dur="3s" repeatCount="indefinite" />
    </circle>
    <circle cx="0" cy="0" r="0" fill="none" stroke="#5A67D8" stroke-width="2">
      <animate attributeName="r" values="0; 150" begin="2s" dur="3s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="1; 0" begin="2s" dur="3s" repeatCount="indefinite" />
    </circle>

    <!-- Node Center -->
    <circle cx="0" cy="0" r="16" fill="rgba(255,255,255,0.1)" stroke="#5A67D8" stroke-width="4" />
    <circle cx="0" cy="0" r="6" fill="#F87171">
      <animate attributeName="opacity" values="1; 0.2; 1" dur="1s" repeatCount="indefinite" />
    </circle>
    
    <!-- Floor plan boundary -->
    <rect x="-100" y="-80" width="200" height="160" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2" stroke-dasharray="8 8" />
  </g>
</svg>
"""

svg_network = """
<svg viewBox="0 0 400 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 100 L400 100 M0 200 L400 200 M100 0 L100 300 M200 0 L200 300 M300 0 L300 300" stroke="rgba(255,255,255,0.03)" stroke-width="1" />
  
  <rect x="120" y="40" width="160" height="220" rx="4" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  
  <!-- Server Unit 1 -->
  <rect x="130" y="60" width="140" height="30" rx="4" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" />
  <circle cx="145" cy="75" r="4" fill="#4ade80">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
  </circle>
  <rect x="160" y="70" width="10" height="10" fill="#111827" />
  <rect x="180" y="70" width="10" height="10" fill="#111827" />
  <rect x="200" y="70" width="10" height="10" fill="#111827" />
  <rect x="220" y="70" width="10" height="10" fill="#111827" />
  <circle cx="260" cy="75" r="3" fill="#60A5FA">
      <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite" />
  </circle>

  <!-- Server Unit 2 / Switch -->
  <rect x="130" y="100" width="140" height="40" rx="4" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" />
  <g fill="#111827">
    <rect x="140" y="110" width="8" height="8" /><rect x="152" y="110" width="8" height="8" />
    <rect x="164" y="110" width="8" height="8" /><rect x="176" y="110" width="8" height="8" />
    <rect x="188" y="110" width="8" height="8" /><rect x="200" y="110" width="8" height="8" />
    <rect x="212" y="110" width="8" height="8" /><rect x="224" y="110" width="8" height="8" />
    <rect x="140" y="122" width="8" height="8" /><rect x="152" y="122" width="8" height="8" />
    <rect x="164" y="122" width="8" height="8" /><rect x="176" y="122" width="8" height="8" />
    <rect x="188" y="122" width="8" height="8" /><rect x="200" y="122" width="8" height="8" />
    <rect x="212" y="122" width="8" height="8" /><rect x="224" y="122" width="8" height="8" />
  </g>
  <!-- Port LEDs -->
  <rect x="142" y="112" width="4" height="4" fill="#4ade80"><animate attributeName="opacity" values="1;0;1" dur="0.2s" repeatCount="indefinite" /></rect>
  <rect x="178" y="112" width="4" height="4" fill="#4ade80"><animate attributeName="opacity" values="1;0;1" dur="0.3s" repeatCount="indefinite" /></rect>
  <rect x="202" y="124" width="4" height="4" fill="#4ade80"><animate attributeName="opacity" values="1;0;1" dur="0.5s" repeatCount="indefinite" /></rect>
  <rect x="226" y="112" width="4" height="4" fill="#4ade80"><animate attributeName="opacity" values="1;0;1" dur="0.4s" repeatCount="indefinite" /></rect>

  <!-- Server Unit 3 -->
  <rect x="130" y="150" width="140" height="30" rx="4" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" />
  <circle cx="145" cy="165" r="4" fill="#4ade80">
      <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" />
  </circle>
  <rect x="160" y="160" width="10" height="10" fill="#111827" />
  <rect x="180" y="160" width="10" height="10" fill="#111827" />
  
  <!-- UPS Unit -->
  <rect x="130" y="200" width="140" height="50" rx="4" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.1)" />
  <rect x="145" y="210" width="30" height="30" rx="15" fill="#111827" stroke="rgba(255,255,255,0.1)" />
  <path d="M155 225 L160 225 L160 220 L165 220 M155 225 L155 230 L150 230" stroke="#5A67D8" stroke-width="2" fill="none" />
</svg>
"""

svg_rollouts = """
<svg viewBox="0 0 400 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 100 L400 100 M0 200 L400 200 M100 0 L100 300 M200 0 L200 300 M300 0 L300 300" stroke="rgba(255,255,255,0.03)" stroke-width="1" />
  
  <g transform="translate(40, 60)">
    <!-- Branching Network Links -->
    <path d="M40 90 L120 40 L200 90 L280 40 L200 140 Z M120 40 L120 140 M200 90 L280 140" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
    
    <!-- Nodes -->
    <g>
      <!-- Node 1 -->
      <circle cx="40" cy="90" r="10" fill="#111827" stroke="rgba(255,255,255,0.2)" stroke-width="2">
        <animate attributeName="fill" values="#111827; #5A67D8; #5A67D8; #111827" keyTimes="0; 0.1; 0.9; 1" dur="5s" repeatCount="indefinite" />
        <animate attributeName="stroke" values="rgba(255,255,255,0.2); #fff; #fff; rgba(255,255,255,0.2)" keyTimes="0; 0.1; 0.9; 1" dur="5s" repeatCount="indefinite" />
      </circle>
      
      <!-- Node 2 -->
      <circle cx="120" cy="40" r="12" fill="#111827" stroke="rgba(255,255,255,0.2)" stroke-width="2">
        <animate attributeName="fill" values="#111827; #5A67D8; #5A67D8; #111827" keyTimes="0; 0.1; 0.9; 1" begin="0.5s" dur="5s" repeatCount="indefinite" />
        <animate attributeName="stroke" values="rgba(255,255,255,0.2); #fff; #fff; rgba(255,255,255,0.2)" keyTimes="0; 0.1; 0.9; 1" begin="0.5s" dur="5s" repeatCount="indefinite" />
      </circle>
      
      <!-- Node 3 -->
      <circle cx="120" cy="140" r="10" fill="#111827" stroke="rgba(255,255,255,0.2)" stroke-width="2">
        <animate attributeName="fill" values="#111827; #5A67D8; #5A67D8; #111827" keyTimes="0; 0.1; 0.9; 1" begin="1s" dur="5s" repeatCount="indefinite" />
        <animate attributeName="stroke" values="rgba(255,255,255,0.2); #fff; #fff; rgba(255,255,255,0.2)" keyTimes="0; 0.1; 0.9; 1" begin="1s" dur="5s" repeatCount="indefinite" />
      </circle>

      <!-- Node 4 -->
      <circle cx="200" cy="90" r="16" fill="#111827" stroke="rgba(255,255,255,0.2)" stroke-width="2">
        <animate attributeName="fill" values="#111827; #5A67D8; #5A67D8; #111827" keyTimes="0; 0.1; 0.9; 1" begin="1.5s" dur="5s" repeatCount="indefinite" />
        <animate attributeName="stroke" values="rgba(255,255,255,0.2); #fff; #fff; rgba(255,255,255,0.2)" keyTimes="0; 0.1; 0.9; 1" begin="1.5s" dur="5s" repeatCount="indefinite" />
      </circle>

      <!-- Node 5 -->
      <circle cx="280" cy="40" r="10" fill="#111827" stroke="rgba(255,255,255,0.2)" stroke-width="2">
        <animate attributeName="fill" values="#111827; #5A67D8; #5A67D8; #111827" keyTimes="0; 0.1; 0.9; 1" begin="2s" dur="5s" repeatCount="indefinite" />
        <animate attributeName="stroke" values="rgba(255,255,255,0.2); #fff; #fff; rgba(255,255,255,0.2)" keyTimes="0; 0.1; 0.9; 1" begin="2s" dur="5s" repeatCount="indefinite" />
      </circle>

      <!-- Node 6 -->
      <circle cx="280" cy="140" r="14" fill="#111827" stroke="rgba(255,255,255,0.2)" stroke-width="2">
        <animate attributeName="fill" values="#111827; #5A67D8; #5A67D8; #111827" keyTimes="0; 0.1; 0.9; 1" begin="2.5s" dur="5s" repeatCount="indefinite" />
        <animate attributeName="stroke" values="rgba(255,255,255,0.2); #fff; #fff; rgba(255,255,255,0.2)" keyTimes="0; 0.1; 0.9; 1" begin="2.5s" dur="5s" repeatCount="indefinite" />
      </circle>
    </g>
  </g>
</svg>
"""


SERVICES_DATA = [
    ("Structured Cabling & Routing", "Execute structured cabling systems that support enterprise connectivity and security endpoints. Our teams deliver immaculate cable dressing, strict labeling standards, and certified test results.", svg_cabling, "polyline points='22 12 18 12 15 21 9 3 6 12 2 12'"),
    ("Video Surveillance", "High-density IP camera mounting, precise FOV adjustments, and multi-server VMS storage architecture deployment.", svg_surveillance, "rect x='2' y='4' width='20' height='16' rx='2' ry='2'/><path d='M12 16v-4'/><path d='M8 12h8'/>"),
    ("Access Control", "Total physical barrier mapping and implementation. Deploying OSDP readers, logic panels, and complex door hardware systems.", svg_access, "path d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'"),
    ("Intrusion Systems", "Perimeter defense and interior volumetric threat detection arrays. We install the sensors that secure operational footprints.", svg_intrusion, "path d='M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9'/><path d='M13.73 21a2 2 0 0 1-3.46 0'/>"),
    ("Network Infrastructure", "Clean, precise buildouts of the core networking environments. We prepare the physical stage for IT engineers to activate.", svg_network, "rect x='4' y='4' width='16' height='16' rx='2' ry='2'/><rect x='9' y='9' width='6' height='6'/><line x1='9' y1='1' x2='9' y2='4'/><line x1='15' y1='1' x2='15' y2='4'/><line x1='9' y1='20' x2='9' y2='23'/><line x1='15' y1='20' x2='15' y2='23'/><line x1='20' y1='9' x2='23' y2='9'/><line x1='20' y1='14' x2='23' y2='14'/><line x1='1' y1='9' x2='4' y2='9'/><line x1='1' y1='14' x2='4' y2='14'/>"),
    ("Technology Rollouts", "Scalable deployment solutions for regional footprints. We map identical, repeatable installation protocols across hundreds of locations simultaneously.", svg_rollouts, "rect x='2' y='3' width='20' height='14' rx='2' ry='2'/><line x1='8' y1='21' x2='16' y2='21'/><line x1='12' y1='17' x2='12' y2='21'/>")
]

timeline_html = '''
    <div class="timeline-wrapper">
        <div class="timeline-tracker" id="timeline-tracker">
            <div class="timeline-fill" id="timeline-fill"></div>
        </div>
'''

for index, (title, desc, graphic, icon) in enumerate(SERVICES_DATA):
    # Determine which file to link it to
    link = "/contact.html"
    if title == "Structured Cabling & Routing": link = "/services/structured-cabling.html"
    elif title == "Video Surveillance": link = "/services/video-surveillance-installation.html"
    elif title == "Access Control": link = "/services/access-control-installation.html"
    elif title == "Network Infrastructure": link = "/services/network-rack-buildouts.html"
    
    timeline_html += f'''
        <div class="timeline-step">
            <div class="timeline-content">
                <div class="svc-icon-wrap" style="width: 48px; height: 48px; margin-bottom: 24px; border-radius: 12px; background: rgba(90, 103, 216, 0.1); color: var(--c-accent); border: 1px solid rgba(90, 103, 216, 0.2);">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{icon}</svg>
                </div>
                <h3 style="font-size: 32px; margin-bottom: 16px;">{title}</h3>
                <p style="font-size: 18px; color: var(--c-text-body); line-height: 1.7; margin-bottom: 24px;">{desc}</p>
                <a href="{link}" class="btn btn-primary" style="font-size: 14px; padding: 10px 24px;">Explore Capability</a>
            </div>
            
            <div class="timeline-dot"></div>
            
            <div class="timeline-graphic reveal">
                {graphic}
            </div>
        </div>
'''

timeline_html += '''
    </div>
'''

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Infrastructure Services | Northeast Technical Works (NTW)</title>
    <!-- CRITICAL: Force absolute path for styles.css -->
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
{new_nav}

    <!-- 3. Hero Section -->
    <section class="hero theme-dark" style="min-height: 35vh; padding-top: 100px; padding-bottom: 50px;">
        <div class="container relative">
            <div class="hero-content">
                <div class="hero-tag" style="margin-bottom: 20px;">What We Do</div>
                <h1 style="font-size: 52px; line-height: 1.2; margin-bottom: 16px;">Infrastructure Services</h1>
                <p style="font-size: 18px; color: var(--c-dark-text-body); max-width: 700px;">Comprehensive physical execution across 6 core disciplines. Highly visual, animated technology pipelines tracking precise deployment operations.</p>
            </div>
        </div>
    </section>

    <!-- 4. Main Body Content Graphic Timeline -->
    <section class="section bg-white" style="position: relative; overflow: hidden; padding-bottom: 200px;">
        <div class="container">
{timeline_html}
        </div>
    </section>

{new_footer}
    <script src="/js/main.js"></script>
    <script>
      // Trigger scroll event on load to populate tracker if already scrolled midway
      setTimeout(() => window.dispatchEvent(new Event('scroll')), 100);
    </script>
</body>
</html>
"""

with open(os.path.join(base_dir, "services.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)

print("Dynamic Animated Services Timeline Rebuilt Successfully!")
