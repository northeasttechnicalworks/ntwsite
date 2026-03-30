import os
import re

base_dir = "e:/websites/NTW"
services_dir = os.path.join(base_dir, "services")
os.makedirs(services_dir, exist_ok=True)

# Extract core assets
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

nav_match = re.search(r'(<div class="top-bar">.*?</header>)', idx_content, re.DOTALL)
new_nav = nav_match.group(1) if nav_match else ""
ft_match = re.search(r'(<footer class="footer".*?</footer>)', idx_content, re.DOTALL)
new_footer = ft_match.group(1) if ft_match else ""

# Modify nav links to be root-relative since these are sub-pages
new_nav = new_nav.replace('href="index', 'href="/index')
new_nav = new_nav.replace('href="services', 'href="/services')
new_nav = new_nav.replace('href="coverage', 'href="/coverage')
new_nav = new_nav.replace('href="industries', 'href="/industries')
new_nav = new_nav.replace('href="about', 'href="/about')
new_nav = new_nav.replace('href="blog', 'href="/blog')
new_nav = new_nav.replace('href="contact', 'href="/contact')

# Fix logo path specifically
new_nav = new_nav.replace('href="index.html"', 'href="/index.html"')

PAGES = [
    {
        "filename": "structured-cabling.html",
        "title": "Structured Cabling Systems NY, NJ, CT | Northeast Technical Works",
        "meta": "Premium structured cabling, fiber, and copper installation across NY, NJ, and CT. Clean, certified routing for commercial environments.",
        "hero": "Structured Cabling Systems Done Right the First Time",
        "short_name": "Structured Cabling",
        "tag": "Core Infrastructure",
        "intro": "Structured cabling is the nervous system of your facility. It requires strict adherence to NEC standards, immaculately planned routing, and certified termination. Whether you need an office completely rewired or a massive warehouse network mapped out, our structured cabling contractors in NY, NJ, and CT ensure data flows flawlessly from endpoint to core without latency or visual clutter.",
        "what": ["High-density fiber drop installations", "Category 6/6A copper runs and terminations", "Cable tray routing and strict path management", "Fluke testing and full network certification"],
        "where": ["Corporate office buildouts", "Industrial warehouses", "Medical and healthcare facilities", "Retail multi-site branches", "Data centers"],
        "why": ["Perfectly dressed, uniform cables", "Work completed to precise electrical spec", "Deadlines met without disruption", "No aesthetic 'spaghetti' shortcuts", "Immediate, transparent closeout packages"],
        "probs": ["Messy, disorganized drop ceilings", "Failed local low-voltage inspections", "Intermittent network failures", "Impossible-to-trace legacy ports"]
    },
    {
        "filename": "network-rack-buildouts.html",
        "title": "Network Infrastructure & MDF/IDF Buildouts | Northeast Technical Works",
        "meta": "Expert network rack buildouts and MDF/IDF infrastructure installations across NY, NJ, and CT. Scalable edge deployment.",
        "hero": "Network Infrastructure & Buildouts Done Right the First Time",
        "short_name": "Network Racks",
        "tag": "Core Infrastructure",
        "intro": "The Main Distribution Frame (MDF) and Intermediate Distribution Frames (IDF) are the command centers of your local network. A poorly built rack leads to overheating, impossible troubleshooting, and operational downtime. Our network infrastructure contractors across NY, NJ, and CT architect beautifully routed, highly functional rack environments that your IT engineers will be proud to manage.",
        "what": ["Server rack and cabinet assembly", "Core switch and patch panel mounting", "UPS (Uninterruptible Power Supply) integration", "Strict wire management and waterfall dressing"],
        "where": ["Corporate HQs and branch offices", "Logistics and distribution centers", "Hospitality venues and stadiums", "Enterprise data closets", "Higher education campuses"],
        "why": ["Immaculately organized patch cables", "Proper weight distribution and grounding", "Strict thermal management clearance", "Clear, color-coded port assignments", "Ready for instant IT commissioning"],
        "probs": ["Overloaded, sagging equipment racks", "Thermal shutdown from dense wiring", "Impossible move-add-change (MAC) operations", "Unlabeled, chaotic patch panels"]
    },
    {
        "filename": "video-surveillance-installation.html",
        "title": "Surveillance Systems & Commercial CCTV Installation | NTW",
        "meta": "Professional surveillance systems and CCTV installations for commercial spaces in NY, NJ, and CT. Flawless VMS integration.",
        "hero": "Surveillance Systems Done Right the First Time",
        "short_name": "CCTV Systems",
        "tag": "Physical Security",
        "intro": "Cameras are useless if they have blind spots, drop offline, or trigger false alerts. Commercial CCTV installation requires strategic field-of-view mapping, secure mounting, and robust data backhauling. We deploy heavy-duty surveillance systems across NY, NJ, and CT that actively protect your assets and seamlessly tie back to your enterprise VMS networks.",
        "what": ["IP multi-sensor and PTZ camera mounting", "Strategic field-of-view (FOV) alignment", "NVR/Server rack integration", "Conduit routing and weatherized outdoor sealing"],
        "where": ["High-risk retail environments", "Distribution loading docks", "Corporate lobbies and perimeters", "Manufacturing assembly lines", "K-12 and university campuses"],
        "why": ["Tamper-resistant mounting hardware", "Clean conduit pipes with no exposed wires", "Certified integration with existing IT networks", "Zero blind-spot execution", "Detailed IP mapping spreadsheets upon closeout"],
        "probs": ["Cameras dropping connection intermittently", "Exposed wiring leading to vandalism", "Poor angles missing critical events", "Incorrect focal lengths resulting in blur"]
    },
    {
        "filename": "access-control-installation.html",
        "title": "Access Control Systems & Reader Installation NY/NJ/CT | NTW",
        "meta": "Enterprise access control systems, OSDP readers, and door hardware integrated securely across New York, New Jersey, and Connecticut.",
        "hero": "Access Control Systems Done Right the First Time",
        "short_name": "Access Control",
        "tag": "Physical Security",
        "intro": "Locking down a commercial facility goes far beyond mounting a card reader. It requires complex logic-board programming, electrified door hardware, and fail-safe life safety integration. We routinely execute complex access control installations in NY, NJ, and CT, ensuring only authorized personnel cross your thresholds while adhering strictly to fire and building codes.",
        "what": ["Mullion and keypad OSDP reader installation", "Electric strike and magnetic lock integration", "Intelligent logic panel mounting and wiring", "Life safety sensor and request-to-exit wiring"],
        "where": ["Corporate tenant spaces", "Restricted healthcare wings", "Multi-tenant high-rises", "Government and municipal sectors", "Datacenter server floors"],
        "why": ["100% compliant with local fire codes", "Clean mullion cuts and flush plate mounting", "Secure, dressed panels—no loose wiring", "Tested dual-authentication flows", "End-to-end door schematic adherence"],
        "probs": ["Doors failing to release during fire alarms", "Messy sealant and ruined door frames", "Ghost-reads and intermittent logic board failures", "Incorrect voltage burning out locking hardware"]
    },
    {
        "filename": "intrusion-detection.html",
        "title": "Intrusion Detection & Alarm Systems | Northeast Technical Works",
        "meta": "Commercial alarm systems and perimeter intrusion detection installation across NY, NJ, and CT. Secure, monitored execution.",
        "hero": "Intrusion Detection Systems Done Right the First Time",
        "short_name": "Alarm Systems",
        "tag": "Physical Security",
        "intro": "Off-hours threats require immediate, flawless notification. An intrusion system is only as reliable as its field installation—a loose contact or poorly aligned motion sensor can cripple your security posture. We deploy advanced commercial alarm systems across NY, NJ, and CT, installing the defensive sensors that definitively secure your perimeter.",
        "what": ["Door and window perimeter contact wiring", "Volumetric motion and glassbreak sensors", "Alarm keypad and hub deployment", "Central monitoring station integration testing"],
        "where": ["Standalone retail storefronts", "Commercial banking branches", "Pharmaceutical storage facilities", "High-value distribution spaces", "Class-A corporate offices"],
        "why": ["Concealed wiring for tamper-proofing", "Precise sensor alignment to avoid false alarms", "Testing across all armed zones", "Seamless integration with access platforms", "Reliable dispatch protocols"],
        "probs": ["Persistent false alarms causing police fines", "Dead zones missing critical perimeter breaches", "Exposed wires bypassing security entirely", "Systems failing instantly upon power loss"]
    },
    {
        "filename": "multi-site-rollouts.html",
        "title": "Multi-Site Technology Rollouts & Deployments | NTW",
        "meta": "Coordinated multi-site technology rollouts and deployments seamlessly managed across NY, NJ, and CT execution territories.",
        "hero": "Multi-Site Technology Rollouts Done Right the First Time",
        "short_name": "National Rollouts",
        "tag": "Field Operations",
        "intro": "Upgrading technology across 50 regional locations simultaneously requires logistical dominance and absolute field consistency. Variability is the enemy of an enterprise rollout. As your premiere IT rollout contractor in NJ, NY, and CT, we deploy identical, repeatable installation protocols to ensure Site #1 matches Site #50 with zero deviation in quality.",
        "what": ["Simultaneous regional deployment management", "Standardized hardware unboxing and staging", "Identical rack and system configuration execution", "Synchronized end-of-day reporting per site"],
        "where": ["Quick-service restaurant chains", "National retail footprint upgrades", "Regional banking branches", "Franchised healthcare clinics", "Corporate satellite offices"],
        "why": ["We act as a single localized execution arm", "Zero variability between regional builds", "Aggressive multi-team deployment scheduling", "Standardized daily closeout packages", "Streamlined local communication channels"],
        "probs": ["Managing multiple unreliable local contractors", "Inconsistent installations between locations", "Missing inventory due to poor staging", "Project drift and blown rollout timelines"]
    },
    {
        "filename": "infrastructure-remediation.html",
        "title": "Infrastructure Remediation & MDF Cleanup NY/NJ/CT | NTW",
        "meta": "MDF/IDF infrastructure remediation, IT rack cleanup, and cable management restoration across New York, New Jersey, and Connecticut.",
        "hero": "Infrastructure Remediation Done Right the First Time",
        "short_name": "Remediation",
        "tag": "Core Infrastructure",
        "intro": "Over years of reactive upgrades, IT closets degrade into dangerous, unnavigable messes known as 'spaghetti.' When your rack restricts airflow and causes outages, it's time for an intervention. Our IT rack cleanup teams in NY, NJ, and CT specialize in after-hours infrastructure remediation—tracing, removing, and restructuring dead runs into pristine, highly functional network cores.",
        "what": ["Auditing and tone-tracing chaotic legacy wiring", "Removal of dead 'abandoned' cable runs", "Total rack restructuring and cable waterfalling", "As-built re-labeling and documentation packages"],
        "where": ["Acquired commercial buildings", "Legacy hospital campuses", "Older manufacturing plants", "Offices undergoing heavy tech refreshes", "Overloaded data center rows"],
        "why": ["Executed completely during off-hours", "Zero unplanned network downtime", "Rigid tracking of live vs dead connections", "Massive airflow and thermal improvements", "Restores engineering sanity"],
        "probs": ["Engineers unable to locate critical switch ports", "Violations regarding abandoned plenum cabling", "Heat degradation due to blocked equipment", "Accidental unplugging during routine changes"]
    },
    {
        "filename": "field-services-dispatch.html",
        "title": "IT Field Services & Technician Dispatch NY/NJ/CT | NTW",
        "meta": "On-demand IT field services and smart hands dispatch across commercial territories in NY, NJ, and CT. Reliable, rapid deployment.",
        "hero": "Field Services & Dispatch Done Right the First Time",
        "short_name": "Field Dispatch",
        "tag": "Field Operations",
        "intro": "When a switch goes down in Connecticut or a camera goes offline in New Jersey, national integrators and out-of-state engineers need hands on the ground they can trust blindly. Our IT field services and smart hands dispatch in NY, NJ, and CT act as the direct physical extension of your remote engineering teams, resolving issues seamlessly and professionally.",
        "what": ["On-demand break/fix troubleshooting", "Emergency hardware swapping and RMA support", "ISP circuit turn-ups and demarc extensions", "Site surveys and scope-alignment mapping"],
        "where": ["Remote office locations", "Retail stores during peak hours", "Distributed regional medical pods", "Industrial floors out of engineering reach", "Unmanned data center cages"],
        "why": ["Technicians arrive prepared with proper tooling", "White-labeled representation of your firm", "Live communication bridges with your engineers", "Professional triage without guesswork", "Detailed photographic proof-of-work"],
        "probs": ["Local contractors failing to show up", "Unprepared techs requiring heavy hand-holding", "Repeated costly dispatches for the same issue", "Lack of clear follow-up communication"]
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta}">
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
{new_nav}

    <!-- Hero Section -->
    <section class="hero theme-dark" style="min-height: 40vh; display:flex; align-items:center;">
        <div class="container relative">
            <div class="hero-content" style="padding-top: 64px;">
                <div class="hero-tag" style="margin-bottom: 20px;">{tag}</div>
                <h1 style="font-size: 56px; line-height: 1.1; margin-bottom:24px;">{hero}</h1>
                <p style="font-size: 20px; color: var(--c-dark-text-body); margin-bottom:32px; max-width: 700px; line-height: 1.6;">Clean, organized, and fully executed installations for commercial and industrial environments across NY, NJ, and CT.</p>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <section class="section bg-white">
        <div class="container">
            <div class="grid grid-2" style="align-items: start; gap: 80px;">
                
                <!-- Left Content -->
                <div>
                    <a href="/services.html" style="font-size: 14px; margin-bottom: 40px; display: inline-block; color: var(--c-accent); font-weight: 600;">← Back to All Services</a>
                    
                    <h2 style="font-size: 36px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Overview</h2>
                    <p style="font-size: 18px; color: var(--c-text-body); line-height: 1.8; margin-bottom: 48px;">{intro}</p>

                    <h3 style="font-size: 28px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">What We Do</h3>
                    <ul style="list-style: none; padding: 0; color: var(--c-text-body); margin-bottom: 56px;">
                        {what_list}
                    </ul>

                    <h3 style="font-size: 28px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Where This Is Used</h3>
                    <ul style="list-style: none; padding: 0; color: var(--c-text-body); margin-bottom: 56px; display: flex; flex-wrap: wrap; gap: 12px;">
                        {where_list}
                    </ul>

                    <h3 style="font-size: 28px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Common Problems We Fix</h3>
                    <div style="display:grid; grid-template-columns:1fr; gap:16px; margin-bottom:48px;">
                        {probs_list}
                    </div>
                </div>
                
                <!-- Right Sidebar -->
                <div style="position: sticky; top: 120px;">
                    <div style="background: var(--c-surface-light); border-radius: 16px; padding: 40px; border: 1px solid var(--c-border-light); margin-bottom:32px;">
                        <h3 style="font-size: 22px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Why NTW for {short_name}?</h3>
                        <ul style="list-style: none; padding: 0; color: var(--c-text-body);">
                            {why_list}
                        </ul>
                    </div>

                    <div style="background: #020617; border-radius: 16px; padding: 40px; color: white;">
                        <h3 style="font-size: 24px; margin-bottom: 16px; font-family: var(--font-heading);">Service Area</h3>
                        <p style="font-size: 16px; color: #cbd5e1; line-height: 1.7; margin-bottom: 24px;">We serve the entire Northeast corridor, aggressively focusing on dense operational areas:</p>
                        <ul style="list-style: none; padding: 0; color: #fff; font-size:16px; line-height:1.6; margin-bottom:0;">
                            <li style="margin-bottom:16px;"><strong>Primary Execution Zones:</strong> New York (NYC, Westchester, Long Island), Connecticut, New Jersey</li>
                            <li><strong>Secondary Extent:</strong> Pennsylvania, Maryland, Rhode Island, Massachusetts, Delaware, Vermont, New Hampshire, Maine</li>
                        </ul>
                    </div>
                </div>

            </div>

            <!-- Footer Conversion Elements -->
            <div style="margin-top: 100px; max-width: 900px; margin-left: auto; margin-right: auto;">
                 <div style="margin-bottom: 80px; background: var(--c-surface-dark); padding: 60px; border-radius: 16px; position: relative;">
                    <div style="position: absolute; top: 40px; left: 40px; opacity: 0.1;">
                         <svg width="80" height="80" viewBox="0 0 24 24" fill="currentColor"><path d="M10 11h-4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2z"></path><path d="M22 11h-4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2z"></path></svg>
                    </div>
                    <p style="font-size: 24px; color: #fff; line-height: 1.6; font-style: italic; max-width: 800px; margin: 0 auto; text-align: center; position: relative; z-index: 2;">“NTW came in on a job that had already gone sideways and got everything back on track. Easy to work with and got it done right.”</p>
                    <div style="text-align: center; margin-top: 24px; position: relative; z-index: 2;">
                        <strong style="color: var(--c-accent); font-size: 16px; letter-spacing: 1px;">— Systems Integrator, NY</strong>
                    </div>
                 </div>

                 <div style="text-align: center; margin-bottom: 20px;">
                    <h2 style="font-size: 40px; margin-bottom: 16px; font-family: var(--font-heading); color: var(--c-text-main);">Need this done right?</h2>
                    <p style="font-size: 20px; color: var(--c-text-body); max-width: 600px; margin: 0 auto 40px;">Send us your scope — we’ll take it from there.</p>
                    <a href="/contact.html" class="btn btn-primary" style="padding: 16px 48px; font-size: 18px;">Talk to Dispatch</a>
                </div>
            </div>

        </div>
    </section>

{new_footer}
    <script src="/js/main.js"></script>
</body>
</html>"""

def build_svg_li(text, accent_color="var(--c-accent)", style=""):
    return f'<li style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 12px; font-size: 17px;"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{accent_color}" stroke-width="2.5" style="flex-shrink:0; margin-top:1px; {style}"><polyline points="20 6 9 17 4 12"></polyline></svg> {text}</li>'

def build_where_li(text):
    return f'<li style="background: rgba(90, 103, 216, 0.05); color: var(--c-text-main); font-weight: 500; padding: 10px 20px; border-radius: 6px; border: 1px solid rgba(90, 103, 216, 0.15);">{text}</li>'

def build_prob_li(text):
    return f'<div style="background: #FEF2F2; color: #991B1B; padding: 16px 24px; border-radius: 8px; border-left: 4px solid #F87171; font-weight: 500; display:flex; gap:12px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink:0; margin-top:2px;"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg> {text}</div>'

for page in PAGES:
    what_html = "".join([build_svg_li(w) for w in page["what"]])
    where_html = "".join([build_where_li(w) for w in page["where"]])
    why_html = "".join([build_svg_li(w, accent_color="#64748b", style="stroke-width:2") for w in page["why"]])
    probs_html = "".join([build_prob_li(w) for w in page["probs"]])
    
    html = HTML_TEMPLATE.format(
        title=page["title"],
        meta=page["meta"],
        new_nav=new_nav,
        tag=page["tag"],
        hero=page["hero"],
        intro=page["intro"],
        short_name=page["short_name"],
        what_list=what_html,
        where_list=where_html,
        why_list=why_html,
        probs_list=probs_html,
        new_footer=new_footer
    )
    
    out_path = os.path.join(services_dir, page["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Successfully generated all 8 SEO service pages.")
