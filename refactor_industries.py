import os
import re
import sys

base_dir = "e:/websites/NTW"
sys.path.append(base_dir)

# Extract SVGs from old file without re-writing 300 lines of XML
from build_expanded_industries import industries as old_industries
svg_retail = old_industries[0]['svg']
svg_office = old_industries[1]['svg']
svg_datacenter = old_industries[2]['svg']
svg_manufacturing = old_industries[3]['svg']
svg_healthcare = old_industries[4]['svg']
svg_education = old_industries[5]['svg']
svg_hospitality = old_industries[6]['svg']
svg_government = old_industries[7]['svg']

svg_construction = """
<svg viewBox="0 0 500 400" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <!-- Blueprint Grid -->
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
  </pattern>
  <rect width="500" height="400" fill="url(#grid)" />
  
  <!-- Structural Beams -->
  <g transform="translate(100, 100)" stroke="#fbbf24" stroke-width="4" fill="none">
    <path d="M 0 0 L 300 0 L 300 150 L 0 150 Z" stroke="rgba(251, 191, 36, 0.4)" stroke-dasharray="10 5" />
    <path d="M 0 75 L 300 75" stroke="rgba(251, 191, 36, 0.4)" stroke-dasharray="10 5" />
    
    <!-- Solid beams building -->
    <path d="M 0 0 L 300 0" stroke-dasharray="300" stroke-dashoffset="300">
      <animate attributeName="stroke-dashoffset" values="300; 0; 0" dur="4s" repeatCount="indefinite" />
    </path>
    <path d="M 300 0 L 300 150" stroke-dasharray="150" stroke-dashoffset="150">
      <animate attributeName="stroke-dashoffset" values="150; 0; 0" begin="1s" dur="4s" repeatCount="indefinite" />
    </path>
    <path d="M 300 150 L 0 150" stroke-dasharray="300" stroke-dashoffset="300">
      <animate attributeName="stroke-dashoffset" values="300; 0; 0" begin="2s" dur="4s" repeatCount="indefinite" />
    </path>
    <path d="M 0 150 L 0 0" stroke-dasharray="150" stroke-dashoffset="150">
      <animate attributeName="stroke-dashoffset" values="150; 0; 0" begin="3s" dur="4s" repeatCount="indefinite" />
    </path>
  </g>
  
  <!-- Infrastructure Layer overlays -->
  <path d="M 80 80 L 150 150 L 250 150 L 320 80" fill="none" stroke="#4ade80" stroke-width="2" />
  <circle cx="80" cy="80" r="4" fill="#4B5563" />
  <circle cx="150" cy="150" r="4" fill="#4ade80">
      <animate attributeName="r" values="4; 8; 4" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="250" cy="150" r="4" fill="#4ade80">
      <animate attributeName="r" values="4; 8; 4" begin="1s" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="320" cy="80" r="4" fill="#4B5563" />
  
  <rect x="235" y="135" width="30" height="30" rx="4" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
</svg>
"""

new_industries = [
    {
        "title": "Retail & Multi-Site Rollouts",
        "bg": "var(--c-surface-dark)",
        "intro": "Retail environments require fast, consistent rollouts across multiple locations with minimal disruption to operations.",
        "probs": ["Inconsistent installs across locations", "Delays impacting operations or openings", "Poor cable management causing long-term issues", "Vendors needing constant supervision"],
        "helps": ["Consistent installs across all locations", "Work completed to spec every time", "Clean, organized infrastructure", "Reliable timelines and execution"],
        "handles": ["Store cabling", "Camera installs", "Network setup", "Device mounting"],
        "svg": svg_retail
    },
    {
        "title": "Warehousing & Logistics",
        "bg": "#0D1426",
        "intro": "Vast distribution centers require robust infrastructure capable of surviving high-traffic industrial operations without signal failure.",
        "probs": ["Intermittent scanner connectivity causing delays", "Blind spots in critical loading zones", "Exposed wiring vulnerable to machinery", "Disorganized IT closets delaying maintenance"],
        "helps": ["Flawless Wi-Fi mapping and access point mounting", "Strategic camera placement minimizing blind spots", "Conduit sealing and ruggedized routing", "Immaculate rack dressing for quick swaps"],
        "handles": ["Large-scale cabling", "Wide-area surveillance", "Access control systems", "High-bay AP mounting"],
        "svg": svg_manufacturing
    },
    {
        "title": "Commercial Real Estate & Property Management",
        "bg": "#0B1120",
        "intro": "Multi-tenant buildings require complex, secure infrastructure that physically separates tenant networks while maintaining pristine aesthetics.",
        "probs": ["Messy corridors filled with dead legacy wiring", "Unsecured MDF rooms housing multiple tenants", "Inconsistent access hardware failing building codes", "Contractors leaving messy penetrations"],
        "helps": ["Tracing and remediation of abandoned cable runs", "Secure, caged, and segregated core racks", "Code-compliant logic panel locking systems", "Respectful execution preserving high-end finishes"],
        "handles": ["Base building risers", "Tenant buildouts", "Corridor surveillance", "Life-safety door integrations"],
        "svg": svg_hospitality 
    },
    {
        "title": "Healthcare Facilities",
        "bg": "#0B1526",
        "intro": "Hospitals and clinics are precision environments where network failure directly impacts patient care, requiring sterile, hyper-vigilant execution.",
        "probs": ["Contractors violating ICRA dust containment protocols", "Dropped Wi-Fi disconnecting critical medical carts", "Cameras violating structural fire barriers", "Messy wiring causing sanitary issues"],
        "helps": ["Strict adherence to hospital containment standards", "High-density, fault-tolerant network meshes", "Fire-stopping and compliant penetration sealing", "Clean, washable, conduit-protected deployments"],
        "handles": ["Clean, compliant installs", "Minimal disruption", "Secure infrastructure", "Nurse call system routing"],
        "svg": svg_healthcare
    },
    {
        "title": "Corporate Offices & Enterprise Environments",
        "bg": "#15122F",
        "intro": "Enterprise IT environments require immaculately dressed cabling, highly reliable access points, and zero visual clutter in premium spaces.",
        "probs": ["Ugly 'spaghetti' wiring underneath workstations", "Contractors disrupting normal business operations", "Incomplete labeling causing helpdesk delays", "Sagging ceiling tiles and poor cosmetic repair"],
        "helps": ["Perfectly 'waterfalled' drop cables in server rooms", "Off-hours execution with zero operational drag", "Meticulous port-mapping and closeout data", "Invisible routing respecting architectural design"],
        "handles": ["High-density workstation cabling", "Boardroom AV routing", "IDF closet buildouts", "Perimeter security systems"],
        "svg": svg_office
    },
    {
        "title": "Data Centers & IT Infrastructure",
        "bg": "#121A2F",
        "intro": "Mission-critical environments where every patch cable, power drop, and thermal boundary must be executed precisely to spec.",
        "probs": ["Poor routing restricting equipment airflow", "Inaccurate inventory management from bad labeling", "Dead runs taking up valuable rack unit space", "Inconsistent patch cord colors complicating MACs"],
        "helps": ["Flawless overhead tray mapping and dressing", "Velcro-secured, perfectly swept cable management", "Removal and remediation of abandoned runs", "Strict color-coded standardization execution"],
        "handles": ["Massive copper/fiber runs", "Rack and cabinet assembly", "UPS and PDU mounting", "Hot/cold aisle containment wiring"],
        "svg": svg_datacenter
    },
    {
        "title": "Government & Public Sector",
        "bg": "#0D1115",
        "intro": "Municipal and public facilities demand heightened security clearances, rigid compliance with specs, and absolute vendor accountability.",
        "probs": ["Vendors lacking necessary security badging", "Poor documentation failing municipal audits", "Non-compliant materials used to cut costs", "Unmanaged scope creep inflating project budgets"],
        "helps": ["Cleared, vetted, and strictly managed tech crews", "Comprehensive as-built drawings and certifications", "100% adherence to specified, approved Bill of Materials", "Transparent communication and strict scope control"],
        "handles": ["Municipal campus fiber", "Courthouse security systems", "Public Wi-Fi meshes", "Command center wall arrays"],
        "svg": svg_government
    },
    {
        "title": "Construction & General Contractors",
        "bg": "#0D1A30",
        "intro": "Active hard-hat zones require sub-contractors who show up on schedule, coordinate with other trades, and follow site safety protocols blindly.",
        "probs": ["Low-voltage teams delaying drywall or ceiling closeouts", "Poor communication with site superintendents", "Lack of proper PPE or safety certifications", "Sloppy rough-ins causing finish issues later"],
        "helps": ["Aggressive scheduling aligned with trade phases", "Direct, proactive coordination with GCs", "Fully compliant, certified safety adherence", "Clean, highly organized rough-in boxes and rings"],
        "handles": ["Pre-construction planning", "New build low-voltage", "Site-wide temporary networks", "Post-drywall trimming"],
        "svg": svg_construction
    },
    {
        "title": "Educational Institutes & University Campuses",
        "bg": "#0B1526",
        "intro": "Orchestrating campus-wide connectivity bridging thousands of students and faculty across sprawling academic buildings.",
        "probs": ["Dead zones in dense lecture halls", "Insecure access putting student data at risk", "Disjointed paging and emergency intercoms", "Outdated fiber backbones bottlenecking bandwidth"],
        "helps": ["High-density Wi-Fi 6 mapping and deployment", "Secure, compliant networks protecting privacy", "Unified campus safety and mass notification integration", "Massive underground and aerial fiber splicing"],
        "handles": ["Campus Wi-Fi meshes", "Emergency intercoms", "Massive fiber backbones", "Smart classroom AV"],
        "svg": svg_education
    }
]

# Extract header/footer from index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

nav_match = re.search(r'(<div class="top-bar">.*?</header>)', idx_content, re.DOTALL)
new_nav = nav_match.group(1) if nav_match else ""

ft_match = re.search(r'(<footer class="footer".*?</footer>)', idx_content, re.DOTALL)
new_footer = ft_match.group(1) if ft_match else ""

html_cards = []
for idx, ind in enumerate(new_industries):
    probs_html = "".join([f'<li style="margin-bottom:8px; display:flex; gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink:0; margin-top:2px;"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg><span style="line-height:1.4;">{p}</span></li>' for p in ind['probs']])
    helps_html = "".join([f'<li style="margin-bottom:8px; display:flex; gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><span style="line-height:1.4;">{h}</span></li>' for h in ind['helps']])
    handles_html = "".join([f'<li style="background:rgba(90,103,216,0.1); padding:6px 14px; border-radius:6px; border:1px solid rgba(90,103,216,0.2);">{h}</li>' for h in ind['handles']])

    card_html = f'''
        <div class="sticky-card" style="background: {ind['bg']}; z-index: {idx + 1};">
            <div class="container h-full">
                <div class="sticky-card-inner">
                    <div class="sticky-text">
                        <div class="sticky-tag">Sector 0{idx+1}</div>
                        <h2 style="font-size:36px; margin-bottom:16px;">{ind['title']}</h2>
                        <p style="font-size:16px; line-height:1.6; color:var(--c-text-body); margin-bottom:24px;">{ind['intro']}</p>
                        
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-bottom:24px;">
                            <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.05); padding:20px; border-radius:12px;">
                                <h4 style="color:#F87171; font-size:15px; margin-bottom:12px; font-family:var(--font-heading);">Common Problems:</h4>
                                <ul style="list-style:none; padding:0; margin:0; font-size:13px; color:#cbd5e1;">
                                    {probs_html}
                                </ul>
                            </div>
                            <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.05); padding:20px; border-radius:12px;">
                                <h4 style="color:#4ade80; font-size:15px; margin-bottom:12px; font-family:var(--font-heading);">How NTW Helps:</h4>
                                <ul style="list-style:none; padding:0; margin:0; font-size:13px; color:#cbd5e1;">
                                    {helps_html}
                                </ul>
                            </div>
                        </div>
                        
                        <div>
                            <h4 style="color:white; font-size:15px; margin-bottom:12px; font-family:var(--font-heading); text-transform:uppercase; letter-spacing:1px;">What We Handle:</h4>
                            <ul style="list-style:none; padding:0; margin:0; font-size:13px; color:var(--c-accent); display:flex; flex-wrap:wrap; gap:10px;">
                                {handles_html}
                            </ul>
                        </div>
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

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Industries We Serve | Northeast Technical Works (NTW)</title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
{new_nav}

    <!-- Hero Section -->
    <section class="hero theme-dark" style="min-height: 35vh; padding-top: 100px; padding-bottom: 50px;">
        <div class="container relative">
            <div class="hero-content">
                <div class="hero-tag" style="margin-bottom: 20px;">Operational Environments</div>
                <h1 style="font-size: 52px; line-height: 1.2; margin-bottom: 16px;">Infrastructure Built for High-Stakes Environments</h1>
                <p style="font-size: 18px; color: var(--c-dark-text-body); max-width: 700px; margin-bottom: 32px;">We execute cabling, security, and network infrastructure across industries where precision, consistency, and reliability matter.</p>
                <div style="display:flex; gap:16px;">
                    <a href="/contact.html" class="btn btn-primary" style="padding: 16px 32px;">Request Deployment</a>
                    <a href="/contact.html" class="btn btn-dark" style="padding: 16px 32px;">Talk to Our Team</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Intro Section -->
    <section style="background: var(--c-surface-light); padding: 80px 0; border-bottom: 1px solid var(--c-border-light);">
        <div class="container text-center" style="max-width: 800px;">
            <p style="font-size: 22px; color: var(--c-text-body); line-height: 1.8;">
                We work across multiple industries, but the common requirement is the same — <strong style="color: var(--c-text-main);">clean, reliable execution in environments where mistakes are not acceptable.</strong>
            </p>
        </div>
    </section>

{deck_wrapper}

    <!-- Trust Section -->
    <section style="background: var(--c-surface-light); padding: 120px 0;">
        <div class="container text-center" style="max-width: 800px;">
            <h2 style="font-size: 40px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Built for Environments Where Mistakes Matter</h2>
            <p style="font-size: 20px; color: var(--c-text-body); line-height: 1.8;">
                Most infrastructure issues come from poor execution in the field.<br>
                We eliminate that risk by delivering clean, consistent work that holds up under inspection and long-term use.
            </p>
        </div>
    </section>

    <!-- Testimonial Section -->
    <section style="padding: 0 0 100px 0; background: var(--c-surface-light);">
        <div class="container">
            <div style="background: var(--c-surface-dark); padding: 60px; border-radius: 16px; position: relative; max-width: 900px; margin: 0 auto;">
                <div style="position: absolute; top: 40px; left: 40px; opacity: 0.1;">
                     <svg width="80" height="80" viewBox="0 0 24 24" fill="currentColor"><path d="M10 11h-4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2z"></path><path d="M22 11h-4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2z"></path></svg>
                </div>
                <p style="font-size: 24px; color: #fff; line-height: 1.6; font-style: italic; max-width: 800px; margin: 0 auto; text-align: center; position: relative; z-index: 2;">“NTW came in on a job that had already gone sideways and got everything back on track. Easy to work with and got it done right.”</p>
                <div style="text-align: center; margin-top: 24px; position: relative; z-index: 2;">
                    <strong style="color: var(--c-accent); font-size: 16px; letter-spacing: 1px;">— Systems Integrator, NY</strong>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section style="padding: 0 0 120px 0; background: var(--c-surface-light);">
        <div class="container text-center" style="display: flex; flex-direction: column; align-items: center;">
            <h2 style="font-size: 40px; margin-bottom: 16px; font-family: var(--font-heading); color: var(--c-text-main);">Working in One of These Environments?</h2>
            <p style="font-size: 20px; color: var(--c-text-body); max-width: 600px; margin: 0 auto 40px;">Send us your scope — we’ll handle the execution.</p>
            <a href="/contact.html" class="btn btn-primary" style="padding: 16px 48px; font-size: 18px;">Request Deployment</a>
        </div>
    </section>

{new_footer}
    <script src="/js/main.js"></script>
</body>
</html>
"""

# Write Output
with open(os.path.join(base_dir, "industries.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)

print("industries.html successfully refactored with new grids and copy!")
