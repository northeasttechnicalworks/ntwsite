import os
import re

base_dir = "e:/websites/NTW"

# 1. Extract NavBar & Footer from index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

nav_match = re.search(r'(<div class="top-bar">.*?</nav>)', idx_content, re.DOTALL)
new_nav = nav_match.group(1) if nav_match else ""

ft_match = re.search(r'(<footer class="footer">.*?</footer>)', idx_content, re.DOTALL)
new_footer = ft_match.group(1) if ft_match else ""

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{{{title}}}} | Northeast Technical Works</title>
    <!-- CRITICAL: Force absolute path for styles.css -->
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
{new_nav}

    <!-- Subpage Hero -->
    <section class="hero theme-dark" style="min-height: 40vh; display:flex; align-items:center;">
        <div class="container relative">
            <div class="hero-content" style="padding-top: 64px;">
                <div class="hero-tag">{{{{tag}}}}</div>
                <h1 style="font-size: 56px;">{{{{title}}}}</h1>
                <p style="font-size: 18px; color: var(--c-dark-text-body); max-width: 600px;">{{{{subtitle}}}}</p>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <section class="section bg-white">
        <div class="container">
{{{{content}}}}
        </div>
    </section>

{new_footer}
    <script src="/js/main.js"></script>
</body>
</html>
"""

# Targets
service_pages = [
    ("services/access-control-installation.html", "Access Control Installation", "Physical Security", "Deploying OSDP readers, panels, and integrated locks."),
    ("services/network-rack-buildouts.html", "Network Rack Buildouts", "Core Infrastructure", "Clean, precise buildouts of core networking environments."),
    ("services/structured-cabling-new-york.html", "Structured Cabling - NY", "Regional Deployment", "Cat6A and Fiber Optic deployment focused on the NY Metro Area."),
    ("services/structured-cabling.html", "Structured Cabling & Routing", "Core Infrastructure", "Immaculate cable dressing, strict labeling, and Fluke certification."),
    ("services/video-surveillance-installation.html", "Video Surveillance Installation", "Physical Security", "High-density IP camera mounting, VMS architecture deployment.")
]

for path, title, tag, sub in service_pages:
    filepath = os.path.join(base_dir, path)
    content = f'''
        <div class="grid grid-2" style="align-items: start; gap: 80px;">
            <div>
                <a href="/services.html" style="font-size: 14px; margin-bottom: 32px; display: inline-block; color: var(--c-accent); font-weight: 600;">← Back to All Services</a>
                <h2 style="font-size: 36px; margin-bottom: 24px;">{title} Overview</h2>
                <p style="font-size: 18px; color: var(--c-text-body); line-height: 1.8; margin-bottom: 32px;">We deliver flawless physical execution of {title} tailored for high-compliance enterprise environments. Our technicians are trained to execute rigid documentation arrays alongside the physical installation.</p>
                
                <h4 style="font-size: 20px; margin-bottom: 16px;">Typical Deployment Features</h4>
                <ul style="list-style: none; padding: 0; color: var(--c-text-body);">
                    <li style="margin-bottom: 12px; display: flex; align-items: flex-start; gap: 12px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="3" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Inspection-Ready Standards</li>
                    <li style="margin-bottom: 12px; display: flex; align-items: flex-start; gap: 12px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="3" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Closeout Deliverable Packages</li>
                    <li style="margin-bottom: 12px; display: flex; align-items: flex-start; gap: 12px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="3" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Advanced Troubleshooting</li>
                </ul>
            </div>
            
            <div style="background: var(--c-bg-light); border-radius: 16px; padding: 48px; border: 1px solid var(--c-border-light);">
                <div class="sec-tag" style="color:var(--c-accent); font-weight:bold; margin-bottom:12px; font-size:14px; display:block;">Start a Deployment</div>
                <h3 style="font-size: 24px; margin-bottom: 16px;">Ready to deploy this service?</h3>
                <p style="color: var(--c-text-body); margin-bottom: 32px;">Send us your scope for a rapid review and scheduling availability inside our operations tier.</p>
                <a href="/contact.html" class="btn btn-primary" style="width: 100%;">Connect with Dispatch</a>
            </div>
        </div>
    '''
    final_html = HTML_TEMPLATE.replace("{{title}}", title).replace("{{tag}}", tag).replace("{{subtitle}}", sub).replace("{{content}}", content)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_html)

# Industries page
filepath = os.path.join(base_dir, "industries.html")
content = '''
        <div class="grid grid-2" style="align-items: center; gap: 80px; margin-bottom: 96px;">
            <div>
                <h2 style="font-size: 36px; margin-bottom: 24px;">Retail Rollouts</h2>
                <p style="font-size: 18px; color: var(--c-text-body); line-height: 1.8;">Overnight deployments, tight store opening windows, and standardized checklists across 50+ locations securely deployed across the Northeast.</p>
            </div>
            <div style="background: var(--c-surface-dark); padding: 64px; border-radius: 16px; box-shadow: var(--sh-md);">
                <div class="svc-icon-wrap" style="margin: 0 auto 24px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                <h4 style="color: white; text-align: center; margin: 0; font-size: 24px;">Multi-Site Scalability</h4>
            </div>
        </div>

        <div class="grid grid-2" style="align-items: center; gap: 80px; direction: rtl;">
            <div style="direction: ltr;">
                <h2 style="font-size: 36px; margin-bottom: 24px;">Commercial Office & Enterprise IT</h2>
                <p style="font-size: 18px; color: var(--c-text-body); line-height: 1.8;">IDF buildouts, Cat6A workstations, tenant-safe access control, and highly coordinated, low-disruption execution for white-collar workflows.</p>
            </div>
            <div style="background: var(--c-bg-light); border: 1px solid var(--c-border-light); padding: 64px; border-radius: 16px; direction: ltr; box-shadow: var(--sh-md);">
                <div class="svc-icon-wrap" style="margin: 0 auto 24px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect></svg></div>
                <h4 style="color: var(--c-text-main); text-align: center; margin: 0; font-size: 24px;">Clean Work Environments</h4>
            </div>
        </div>
'''
final_html = HTML_TEMPLATE.replace("{{title}}", "Industries We Serve").replace("{{tag}}", "Operational Environments").replace("{{subtitle}}", "We execute across heavily regulated, high-density, and operational environments.").replace("{{content}}", content)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(final_html)

# Integrators page
filepath = os.path.join(base_dir, "integrators.html")
content = '''
        <div style="max-width: 800px; margin: 0 auto; text-align: center; margin-bottom: 64px;">
            <h2 style="font-size: 40px; margin-bottom: 24px;">For National Integrators</h2>
            <p style="font-size: 18px; color: var(--c-text-body); line-height: 1.8;">We serve as the silent, highly-trusted physical execution arm for national integrators lacking internal field technicians in the Northeast.</p>
        </div>
        
        <div class="grid grid-3">
             <div class="svc-card svc-dark">
                 <div class="svc-icon-wrap" style="margin-bottom: 32px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                 <h3 style="font-size: 22px; margin-bottom: 16px;">White-Label Execution</h3>
                 <p style="font-size: 16px; color: var(--c-dark-text-body);">We arrive representing your brand, fulfilling your scope with precise professional adherence.</p>
             </div>
             <div class="svc-card svc-light" style="box-shadow: var(--sh-md);">
                 <div class="svc-icon-wrap" style="margin-bottom: 32px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg></div>
                 <h3 style="font-size: 22px; margin-bottom: 16px; color: var(--c-text-main);">Closeout Packages</h3>
                 <p style="font-size: 16px; color: var(--c-text-body);">We capture every MAC address, serial number, and required deliverable photo standard.</p>
             </div>
             <div class="svc-card svc-dark">
                 <div class="svc-icon-wrap" style="margin-bottom: 32px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>
                 <h3 style="font-size: 22px; margin-bottom: 16px;">Geographic Reach</h3>
                 <p style="font-size: 16px; color: var(--c-dark-text-body);">Complete dense coverage mapping across the tri-state NY, NJ, and CT markets.</p>
             </div>
        </div>
'''
final_html = HTML_TEMPLATE.replace("{{title}}", "National Integrator Support").replace("{{tag}}", "Partnerships").replace("{{subtitle}}", "Your localized boots on the ground for major Northeast deployments.").replace("{{content}}", content)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Final remaining pages cleanly rebuilt natively from scratch.")
