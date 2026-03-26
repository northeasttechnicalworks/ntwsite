import os
import re

base_dir = "e:/websites/NTW"

# Extract header/footer from index.html (the one the user praised and loved)
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
    <title>{{{{title}}}} | Northeast Technical Works (NTW)</title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
{new_nav}

    <!-- 3. Hero Section (Subpage Profile) -->
    <section class="hero theme-dark" style="min-height: 35vh; padding-top: 100px; padding-bottom: 50px;">
        <div class="container relative">
            <div class="hero-content">
                <div class="hero-tag" style="margin-bottom: 20px;">{{{{tag}}}}</div>
                <h1 style="font-size: 52px; line-height: 1.2; margin-bottom: 16px;">{{{{title}}}}</h1>
                <p style="font-size: 18px; color: var(--c-dark-text-body); max-width: 700px;">{{{{subtitle}}}}</p>
            </div>
        </div>
    </section>

    <!-- 4. Main Body Content Grid -->
    <section class="section bg-white">
        <div class="container">
{{{{content}}}}
        </div>
    </section>

{new_footer}
    <script src="/js/main.js"></script>
    {{{{scripts}}}}
</body>
</html>
"""


# ---------------------------------------------------------
# about.html
# ---------------------------------------------------------
about_body = '''
    <div class="grid grid-2" style="align-items: center; gap: 80px;">
        <div style="position: relative; border-radius: 16px; overflow: hidden; box-shadow: var(--sh-md);">
            <img src="https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?auto=format&fit=crop&w=800&q=80" alt="Team working" style="width: 100%; height: auto; display: block; object-fit: cover;" />
        </div>
        <div>
            <div class="sec-tag" style="margin-bottom: 16px;">About NTW Company</div>
            <h2 style="font-size: 36px; line-height: 1.3; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">The Northeast Corridor's Most Disciplined Deployment Team</h2>
            <p style="font-size: 18px; color: var(--c-text-body); margin-bottom: 24px; line-height: 1.7;">We deliver reliable IT solutions and custom physical-layer deployments that help businesses innovate, grow, and stay ahead in a fast-changing tech landscape.</p>
            <p style="font-size: 18px; color: var(--c-text-body); margin-bottom: 32px; line-height: 1.7;">Delivering inspection-ready execution across NY, NJ, and CT.</p>
            
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 16px;">
                <li style="display: flex; align-items: flex-start; gap: 12px; font-size: 16px; color: var(--c-text-main); font-weight: 500;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="3" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Focused on delivering reliable, scaleable digital solutions</li>
                <li style="display: flex; align-items: flex-start; gap: 12px; font-size: 16px; color: var(--c-text-main); font-weight: 500;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="3" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Aligned with your business goals and future growth</li>
                <li style="display: flex; align-items: flex-start; gap: 12px; font-size: 16px; color: var(--c-text-main); font-weight: 500;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="3" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Dedicated to continuous improvement and innovation</li>
            </ul>
        </div>
    </div>
'''
with open(os.path.join(base_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE.replace("{{title}}", "About Us").replace("{{tag}}", "Our DNA").replace("{{subtitle}}", "Infrastructure in Motion. We execute across heavily regulated, high-density environments.").replace("{{content}}", about_body).replace("{{scripts}}", ""))


# ---------------------------------------------------------
# contact.html
# ---------------------------------------------------------
contact_body = '''
    <div style="background: var(--c-surface-dark); border-radius: 20px; overflow: hidden; display: flex; flex-wrap: wrap;">
        <!-- Left Side: Form -->
        <div style="flex: 1; min-width: 400px; padding: 60px; background: var(--c-white);">
            <h2 style="font-size: 32px; margin-bottom: 32px; font-family: var(--font-heading); color: var(--c-text-main);">Send a Message</h2>
            <div class="grid grid-2" style="gap: 24px; margin-bottom: 24px;">
                <div style="display:flex; flex-direction:column; gap:8px;">
                    <label style="font-size:14px; font-weight:600; color:var(--c-text-main);">Name</label>
                    <input type="text" placeholder="Your name" style="padding:14px; border:1px solid var(--c-border-light); border-radius:8px; outline:none; background:#F8FAFC;">
                </div>
                <div style="display:flex; flex-direction:column; gap:8px;">
                    <label style="font-size:14px; font-weight:600; color:var(--c-text-main);">Email</label>
                    <input type="email" placeholder="Your email" style="padding:14px; border:1px solid var(--c-border-light); border-radius:8px; outline:none; background:#F8FAFC;">
                </div>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px; margin-bottom: 24px;">
                <label style="font-size:14px; font-weight:600; color:var(--c-text-main);">Select Service</label>
                <select style="padding:14px; border:1px solid var(--c-border-light); border-radius:8px; outline:none; background:#F8FAFC; color:var(--c-text-body);">
                    <option>Select service</option>
                    <option>Structured Cabling</option>
                    <option>Video Surveillance</option>
                    <option>Access Control</option>
                </select>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px; margin-bottom: 32px;">
                <label style="font-size:14px; font-weight:600; color:var(--c-text-main);">Message</label>
                <textarea rows="5" placeholder="Describe your deployment needs..." style="padding:14px; border:1px solid var(--c-border-light); border-radius:8px; outline:none; background:#F8FAFC; resize:vertical;"></textarea>
            </div>
            <button class="btn btn-primary" style="width: 100%; border: none; cursor: pointer; text-align: center; justify-content: center;">Submit Request</button>
        </div>
        
        <!-- Right Side: Info -->
        <div style="flex: 1; min-width: 400px; padding: 60px; display:flex; flex-direction:column; justify-content:center;">
            <div class="sec-tag" style="color:var(--c-accent); border-color:rgba(90,103,216,0.3); margin-bottom:20px;">Get Consultation</div>
            <h2 style="font-size: 36px; color: var(--c-white); margin-bottom: 24px; font-family: var(--font-heading); line-height:1.2;">Get Tailored Advice for Your Business</h2>
            <p style="color: var(--c-dark-text-body); font-size: 16px; margin-bottom: 40px; line-height: 1.7;">Connect with our experts to receive personalized physical-layer deployment guidance that aligns with your goals, challenges, and growth strategy.</p>

            <div style="margin-bottom: 40px;">
                <h4 style="color: var(--c-white); font-size: 18px; margin-bottom: 8px;">Contact Dispatch</h4>
                <p style="font-size: 16px; color: var(--c-dark-text-body); line-height: 1.6;">Email: deploy@ne-technical.com<br>Call us: +1 (800) 555-0199</p>
            </div>
            
            <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 32px;">
                <h4 style="color: var(--c-white); font-size: 18px; margin-bottom: 20px;">Your benefit when contacting us:</h4>
                <ul style="list-style: none; display: flex; flex-direction: column; gap: 16px; font-size: 15px; color: var(--c-dark-text-body);">
                    <li style="display: flex; align-items: flex-start; gap: 12px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="color: var(--c-accent); width: 18px; height: 18px; flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> 2-5 Business Days Scheduling Lead</li>
                    <li style="display: flex; align-items: flex-start; gap: 12px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="color: var(--c-accent); width: 18px; height: 18px; flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Scopes Reviewed within 1 Day</li>
                    <li style="display: flex; align-items: flex-start; gap: 12px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="color: var(--c-accent); width: 18px; height: 18px; flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> After-Hours Cutovers Available</li>
                </ul>
            </div>
        </div>
    </div>
'''
with open(os.path.join(base_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE.replace("{{title}}", "Contact Us").replace("{{tag}}", "Action Phase").replace("{{subtitle}}", "Submit your regional footprint requirements. We will map our available technical resources immediately.").replace("{{content}}", contact_body).replace("{{scripts}}", ""))


# ---------------------------------------------------------
# services.html
# ---------------------------------------------------------
srv_body = '''
    <div class="grid grid-3">
        <div class="svc-card svc-dark">
            <div class="svc-icon-wrap"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg></div>
            <h3 style="font-size: 22px;">Structured Cabling & Routing</h3>
            <p style="font-size: 15px;">Execute structured cabling systems that support enterprise connectivity and security endpoints. Our teams deliver immaculate cable dressing, strict labeling standards, and certified test results.</p>
        </div>

        <div class="svc-card svc-light" style="box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <div class="svc-icon-wrap"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2" ry="2"></rect><path d="M12 16v-4"></path><path d="M8 12h8"></path></svg></div>
            <h3 style="font-size: 22px;">Video Surveillance</h3>
            <p style="font-size: 15px;">High-density IP camera mounting, precise FOV adjustments, and multi-server VMS storage architecture deployment.</p>
        </div>

        <div class="svc-card svc-dark">
            <div class="svc-icon-wrap"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
            <h3 style="font-size: 22px;">Access Control</h3>
            <p style="font-size: 15px;">Total physical barrier mapping and implementation. Deploying OSDP readers, logic panels, and complex door hardware systems.</p>
        </div>

        <div class="svc-card svc-light" style="box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <div class="svc-icon-wrap"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg></div>
            <h3 style="font-size: 22px;">Intrusion Systems</h3>
            <p style="font-size: 15px;">Perimeter defense and interior volumetric threat detection arrays. We install the sensors that secure operational footprints.</p>
        </div>

        <div class="svc-card svc-dark">
            <div class="svc-icon-wrap"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg></div>
            <h3 style="font-size: 22px;">Network Infrastructure</h3>
            <p style="font-size: 15px;">Clean, precise buildouts of the core networking environments. We prepare the physical stage for IT engineers to activate.</p>
        </div>

        <div class="svc-card svc-light" style="box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <div class="svc-icon-wrap"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>
            <h3 style="font-size: 22px;">Technology Rollouts</h3>
            <p style="font-size: 15px;">Scalable deployment solutions for regional footprints. We map identical, repeatable installation protocols across hundreds of locations simultaneously.</p>
        </div>
    </div>
'''
with open(os.path.join(base_dir, "services.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE.replace("{{title}}", "Infrastructure Services").replace("{{tag}}", "What We Do").replace("{{subtitle}}", "Comprehensive physical execution across 8 core disciplines. Standardized logistics mapped to rigorous security requirements.").replace("{{content}}", srv_body).replace("{{scripts}}", ""))


# ---------------------------------------------------------
# coverage.html
# ---------------------------------------------------------
map_svg = ""
cov_path = os.path.join(base_dir, "coverage.html")
if os.path.exists(cov_path):
    with open(cov_path, "r", encoding="utf-8") as f:
        c_cont = f.read()
    mm = re.search(r'(<svg viewBox="0 0 600 900".*?</svg>)', c_cont, re.DOTALL)
    map_svg = mm.group(1) if mm else ""

cov_body = f'''
    <div class="grid grid-2" style="align-items: stretch; gap: 60px;">
        <div style="display:flex; flex-direction:column; justify-content:center;">
            <h2 style="font-size: 32px; margin-bottom: 16px; font-family: var(--font-heading); color: var(--c-text-main);">Primary Operations Tier</h2>
            <p style="font-size: 18px; margin-bottom: 48px; color: var(--c-text-body); line-height:1.7;">New York, New Jersey, Connecticut.</p>
            
            <h2 style="font-size: 32px; margin-bottom: 16px; font-family: var(--font-heading); color: var(--c-text-main);">Secondary Support Tier</h2>
            <p style="font-size: 18px; color: var(--c-text-body); line-height:1.7;">Pennsylvania, Massachusetts, Rhode Island, Delaware, Maryland.</p>

            <div style="margin-top: 48px; padding: 40px; background: #F8FAFC; border-radius: 16px; border: 1px solid var(--c-border-light);">
                <h3 style="margin-bottom: 12px; font-size:24px; color: var(--c-text-main);">Standard SLA</h3>
                <p style="color: var(--c-text-body); font-size:16px; line-height:1.6;">2-5 business days scheduling lead. Scopes reviewed and processed within 1 day.</p>
                <div style="width: 100%; height: 1px; background: var(--c-border-light); margin: 24px 0;"></div>
                <h3 style="margin-bottom: 12px; font-size:24px; color: var(--c-text-main);">After-Hours Cutovers</h3>
                <p style="color: var(--c-text-body); font-size:16px; line-height:1.6;">Routine coordination for overnight or weekend deployments directly involving property managers.</p>
            </div>
        </div>
        <div style="background: var(--c-surface-dark); border-radius: 20px; padding: 40px; display:flex; justify-content:center; align-items:center; min-height: 600px; box-shadow: var(--sh-lg); overflow: hidden;">
            {map_svg}
        </div>
    </div>
'''
with open(os.path.join(base_dir, "coverage.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE.replace("{{title}}", "Northeast Coverage Map").replace("{{tag}}", "Where We Deploy").replace("{{subtitle}}", "Built exclusively for the hardest deployment logistics in the U.S. We mobilize across hyper-dense metros and expansive state footprints.").replace("{{content}}", cov_body).replace("{{scripts}}", '<script src="/js/map.js"></script>'))


# ---------------------------------------------------------
# industries.html
# ---------------------------------------------------------
ind_body = '''
        <div class="grid grid-2" style="align-items: center; gap: 80px; margin-bottom: 96px;">
            <div>
                <h2 style="font-size: 36px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Retail Rollouts</h2>
                <p style="font-size: 18px; color: var(--c-text-body); line-height: 1.8;">Overnight deployments, tight store opening windows, and standardized checklists across 50+ locations securely deployed across the Northeast.</p>
            </div>
            <div style="background: var(--c-surface-dark); padding: 80px 40px; border-radius: 20px; box-shadow: var(--sh-md); text-align: center;">
                <div class="svc-icon-wrap" style="margin: 0 auto 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                <h4 style="color: white; margin: 0; font-size: 28px;">Multi-Site Scalability</h4>
            </div>
        </div>

        <div class="grid grid-2" style="align-items: center; gap: 80px; direction: rtl;">
            <div style="direction: ltr;">
                <h2 style="font-size: 36px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Commercial Office & Enterprise IT</h2>
                <p style="font-size: 18px; color: var(--c-text-body); line-height: 1.8;">IDF buildouts, Cat6A workstations, tenant-safe access control, and highly coordinated, low-disruption execution for white-collar workflows.</p>
            </div>
            <div style="background: #F8FAFC; border: 1px solid var(--c-border-light); padding: 80px 40px; border-radius: 20px; direction: ltr; box-shadow: var(--sh-md); text-align: center;">
                <div class="svc-icon-wrap" style="margin: 0 auto 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect></svg></div>
                <h4 style="color: var(--c-text-main); margin: 0; font-size: 28px;">Clean Work Environments</h4>
            </div>
        </div>
'''
with open(os.path.join(base_dir, "industries.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE.replace("{{title}}", "Industries We Serve").replace("{{tag}}", "Operational Environments").replace("{{subtitle}}", "We execute across heavily regulated, high-density, and operational environments where tenant safety and zero-disruption are mandatory.").replace("{{content}}", ind_body).replace("{{scripts}}", ""))

# ---------------------------------------------------------
# integrators.html
# ---------------------------------------------------------
int_body = '''
        <div class="grid grid-3">
             <div class="svc-card svc-dark">
                 <div class="svc-icon-wrap" style="margin-bottom: 32px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                 <h3 style="font-size: 22px; margin-bottom: 16px;">White-Label Execution</h3>
                 <p style="font-size: 16px; color: var(--c-dark-text-body); line-height: 1.6;">We arrive representing your brand, fulfilling your scope with precise professional adherence. No truck logos, no branded shirts.</p>
             </div>
             <div class="svc-card svc-light" style="box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
                 <div class="svc-icon-wrap" style="margin-bottom: 32px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg></div>
                 <h3 style="font-size: 22px; margin-bottom: 16px; color: var(--c-text-main);">Closeout Packages</h3>
                 <p style="font-size: 16px; color: var(--c-text-body); line-height: 1.6;">We capture every MAC address, serial number, and required deliverable photo standard before our technicians leave the site.</p>
             </div>
             <div class="svc-card svc-dark">
                 <div class="svc-icon-wrap" style="margin-bottom: 32px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>
                 <h3 style="font-size: 22px; margin-bottom: 16px;">Geographic Reach</h3>
                 <p style="font-size: 16px; color: var(--c-dark-text-body); line-height: 1.6;">Complete dense coverage mapping across the tri-state NY, NJ, and CT markets. One throat to choke for your regional rollout.</p>
             </div>
        </div>
        
        <div style="margin-top: 80px; text-align: center;">
            <a href="/contact.html" class="btn btn-primary" style="padding: 16px 40px; font-size: 18px;">Connect With Us Today</a>
        </div>
'''
with open(os.path.join(base_dir, "integrators.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE.replace("{{title}}", "For National Integrators").replace("{{tag}}", "Partnerships").replace("{{subtitle}}", "We serve as the silent, highly-trusted physical execution arm for national integrators lacking internal field technicians in the Northeast.").replace("{{content}}", int_body).replace("{{scripts}}", ""))

print("Nuclear fix completely finalized for all root subpages!")
