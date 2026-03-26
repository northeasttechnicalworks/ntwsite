import os
import glob
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
    {{{{scripts}}}}
</body>
</html>
"""

# Rebuild services.html
with open(os.path.join(base_dir, "services.html"), "r", encoding="utf-8") as f:
    srv_cont = f.read()

services = re.findall(r'<h2>(.*?)</h2>\s*<p.*?>(.*?)</p>', srv_cont, re.DOTALL)
srv_grid = '<div class="grid grid-3">\n'
for i, (title, desc) in enumerate(services):
    desc_clean = re.sub(r'<.*?>', '', desc).replace("Overview:", "").strip()
    cls = "svc-light" if i % 2 == 1 else "svc-dark"
    srv_grid += f'''
        <div class="svc-card {cls}">
            <div class="svc-icon-wrap"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3 style="font-size: 20px;">{title}</h3>
            <p style="font-size: 15px;">{desc_clean}</p>
        </div>
'''
srv_grid += '</div>'

srv_html = HTML_TEMPLATE.replace("{{title}}", "Our Services") \
                        .replace("{{tag}}", "What We Do") \
                        .replace("{{subtitle}}", "Comprehensive physical execution across core disciplines.") \
                        .replace("{{content}}", srv_grid)\
                        .replace("{{scripts}}", "")
                        
with open(os.path.join(base_dir, "services.html"), "w", encoding="utf-8") as f:
    f.write(srv_html)


# Rebuild coverage.html
with open(os.path.join(base_dir, "coverage.html"), "r", encoding="utf-8") as f:
    cov_cont = f.read()

map_match = re.search(r'(<svg viewBox="0 0 600 900".*?</svg>)', cov_cont, re.DOTALL)
map_svg = map_match.group(1) if map_match else ""

cov_body = f'''
    <div class="grid grid-2" style="align-items: stretch; gap: 80px;">
        <div style="display:flex; flex-direction:column; justify-content:center;">
            <h2 style="font-size: 32px; margin-bottom: 16px;">Primary Operations Tier</h2>
            <p style="font-size: 18px; margin-bottom: 48px; color: var(--c-text-body);">New York, New Jersey, Connecticut.</p>
            
            <h2 style="font-size: 32px; margin-bottom: 16px;">Secondary Support Tier</h2>
            <p style="font-size: 18px; color: var(--c-text-body);">Pennsylvania, Massachusetts, Rhode Island, Delaware, Maryland.</p>

            <div style="margin-top: 48px; padding: 40px; background: var(--c-bg-light); border-radius: 12px; border: 1px solid var(--c-border-light);">
                <h3 style="margin-bottom: 12px;">Standard SLA</h3>
                <p style="color: var(--c-text-body);">2-5 business days scheduling lead. Scopes reviewed and processed within 1 day.</p>
                <h3 style="margin-top: 32px; margin-bottom: 12px;">After-Hours Cutovers</h3>
                <p style="color: var(--c-text-body);">Routine coordination for overnight or weekend deployments directly involving property managers.</p>
            </div>
        </div>
        <div style="background: var(--c-bg-dark); border-radius: 24px; padding: 40px; display:flex; justify-content:center; align-items:center; min-height: 500px; box-shadow: var(--sh-md);">
            {map_svg}
        </div>
    </div>
'''

cov_html = HTML_TEMPLATE.replace("{{title}}", "Northeast Coverage") \
                        .replace("{{tag}}", "Where We Deploy") \
                        .replace("{{subtitle}}", "Built exclusively for the hardest deployment logistics in the U.S.") \
                        .replace("{{content}}", cov_body)\
                        .replace("{{scripts}}", '<script src="/js/map.js"></script>')

with open(os.path.join(base_dir, "coverage.html"), "w", encoding="utf-8") as f:
    f.write(cov_html)


# Rebuild contact.html
contact_body = '''
    <div class="form-wrapper">
        <div class="form-box">
            <h2 style="font-size: 32px; margin-bottom: 32px;">Send a Message</h2>
            <div class="grid grid-2" style="gap: 24px;">
                <div class="form-group">
                    <label class="form-label">Name</label>
                    <input type="text" class="form-control" placeholder="Your name">
                </div>
                <div class="form-group">
                    <label class="form-label">Email</label>
                    <input type="email" class="form-control" placeholder="Your email">
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Select Service</label>
                <select class="form-control">
                    <option>Select service</option>
                    <option>Structured Cabling</option>
                    <option>Video Surveillance</option>
                    <option>Access Control</option>
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Message</label>
                <textarea class="form-control" placeholder="Describe your deployment needs..."></textarea>
            </div>
            <button class="btn btn-primary" style="width: 100%;">Submit Request</button>
        </div>
        <div class="form-info">
            <div class="sec-tag" style="color:var(--c-accent); margin-bottom:16px;">Get Consultation</div>
            <h2 style="font-size: 36px; color: var(--c-white); margin-bottom: 24px;">Get Tailored Advice for Your Business</h2>
            <p style="color: var(--c-dark-text-body);">Connect with our experts to receive personalized IT guidance that aligns with your goals, challenges, and growth strategy.</p>

            <div class="info-grid" style="margin-top: 48px; margin-bottom: 48px; display: grid; grid-template-columns: 1fr; gap: 40px;">
                <div class="info-block">
                    <h4 style="color: var(--c-white); font-size: 18px; margin-bottom: 8px;">Contact Dispatch</h4>
                    <p style="font-size: 16px; color: var(--c-dark-text-body);">Email: deploy@ne-technical.com<br>Call us: +1 (800) 555-0199</p>
                </div>
            </div>
            <div class="info-benefits">
                <h4 style="color: var(--c-white); font-size: 18px; margin-bottom: 16px;">Your benefit when contacting us:</h4>
                <ul style="list-style: none; display: grid; grid-template-columns: 1fr; gap: 16px; font-size: 14px; color: var(--c-dark-text-body);">
                    <li style="display: flex; align-items: flex-start; gap: 8px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="color: var(--c-accent); width: 16px; height: 16px; flex-shrink:0; margin-top:3px;"><polyline points="20 6 9 17 4 12"></polyline></svg> 2-5 Business Days Scheduling Lead</li>
                    <li style="display: flex; align-items: flex-start; gap: 8px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="color: var(--c-accent); width: 16px; height: 16px; flex-shrink:0; margin-top:3px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Scopes Reviewed within 1 Day</li>
                    <li style="display: flex; align-items: flex-start; gap: 8px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="color: var(--c-accent); width: 16px; height: 16px; flex-shrink:0; margin-top:3px;"><polyline points="20 6 9 17 4 12"></polyline></svg> After-Hours Cutovers Available</li>
                </ul>
            </div>
        </div>
    </div>
'''
contact_html = HTML_TEMPLATE.replace("{{title}}", "Contact Us") \
                        .replace("{{tag}}", "Get In Touch") \
                        .replace("{{subtitle}}", "Submit your regional footprint requirements. We will map our available technical resources.") \
                        .replace("{{content}}", contact_body)\
                        .replace("{{scripts}}", "")
with open(os.path.join(base_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)

# Clean up CSS from hacky legacy adapter
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()
if "/* --- Legacy Structure Compatibility" in css_content:
    css_content = css_content.split("/* --- Legacy Structure Compatibility")[0]
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)

print("Natively rebuilt core subpages gracefully.")
