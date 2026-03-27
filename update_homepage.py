import os
import re

base_dir = "e:/websites/NTW"
idx_path = os.path.join(base_dir, "index.html")

with open(idx_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract top-bar and navbar
nav_match = re.search(r'(<!-- 1\. Top Bar -->[\s\S]*?</nav>)', content)
nav_block = nav_match.group(1) if nav_match else ""

# Extract footer
ft_match = re.search(r'(<footer class="footer">[\s\S]*?</footer>)', content)
ft_block = ft_match.group(1) if ft_match else ""

new_body = f"""
    {nav_block}

    <!-- 3. Hero Section -->
    <section class="hero theme-dark">
        <div class="container relative">
            <div class="hero-content">
                <div class="hero-tag" style="letter-spacing: 2px;">DEPLOYMENT ENGINE</div>
                <h1 style="font-weight: 800; letter-spacing: -1px;">Infrastructure Execution for<br>High-Stakes Environments</h1>
                <p style="font-size: 20px; color: #cbd5e1; max-width: 650px;">Structured cabling, surveillance, and access control deployments executed with precision across the Northeast.</p>
                <div style="display: flex; gap: 16px; margin-top: 40px;">
                    <a href="#request-service" class="btn btn-primary">Request Deployment</a>
                    <a href="/services.html" class="btn" style="border: 1px solid rgba(255,255,255,0.2); background: transparent; color: #fff;">View Capabilities</a>
                </div>
            </div>
            
            <div style="position: absolute; right: 0; bottom: -20px; display: flex; align-items:center; gap: 16px;">
                <div style="text-align: right;">
                    <strong style="color: #fff; display: block; font-family: var(--font-heading); font-size: 22px; line-height: 1;">100%</strong>
                    <span style="color: var(--c-dark-text-body); font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Inspection-Ready</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Trust Strip -->
    <section class="partner-strip" style="background: #000; border-bottom: 1px solid #1a1a2e; padding: 48px 0;">
        <div class="container partner-container">
            <div class="partner-title" style="color: var(--c-dark-text-body); text-transform: uppercase; letter-spacing: 2px; font-size: 12px;">Operating Environments</div>
            <div class="partner-logos" style="opacity: 0.8;">
                <div style="font-weight: 600; font-size: 18px; color: #fff;">Banking</div>
                <div style="color: rgba(255,255,255,0.2); font-size: 24px;">&middot;</div>
                <div style="font-weight: 600; font-size: 18px; color: #fff;">Healthcare</div>
                <div style="color: rgba(255,255,255,0.2); font-size: 24px;">&middot;</div>
                <div style="font-weight: 600; font-size: 18px; color: #fff;">Real Estate</div>
                <div style="color: rgba(255,255,255,0.2); font-size: 24px;">&middot;</div>
                <div style="font-weight: 600; font-size: 18px; color: #fff;">Data Centers</div>
            </div>
            
            <div class="partner-title" style="color: var(--c-dark-text-body); text-transform: uppercase; letter-spacing: 2px; font-size: 12px; margin-top: 40px;">Execution Standards</div>
            <div class="partner-logos" style="opacity: 0.9; gap: 24px;">
                <div style="font-weight: 600; font-size: 14px; letter-spacing: 1px; color: #fff; border: 1px solid #333; padding: 8px 24px; border-radius: 4px; background: #0a0a0a;">ANSI/BICSI</div>
                <div style="font-weight: 600; font-size: 14px; letter-spacing: 1px; color: #fff; border: 1px solid #333; padding: 8px 24px; border-radius: 4px; background: #0a0a0a;">OSHA-Trained</div>
                <div style="font-weight: 600; font-size: 14px; letter-spacing: 1px; color: #fff; border: 1px solid #333; padding: 8px 24px; border-radius: 4px; background: #0a0a0a;">Inspection-Ready</div>
            </div>
        </div>
    </section>

    <!-- 5. Value Section -->
    <section class="section about-section" style="background: #fff; padding: 140px 0;">
        <div class="container about-grid">
            <div class="about-image">
                <img src="https://images.unsplash.com/photo-1558494949-ef010cbd1317?auto=format&fit=crop&w=800&q=80" alt="Server Room Infrastructure" style="height: 600px; filter: grayscale(40%) contrast(1.1); border-radius: 4px;" />
            </div>
            
            <div class="about-content" style="padding-left: 20px;">
                <div class="sec-tag" style="background: #e2e8f0; color: #0f172a; border-color: #cbd5e1; font-weight: 700;">Infrastructure Delivery</div>
                <h2 style="font-family: var(--font-heading); font-size: 52px; line-height: 1.1; margin-bottom: 32px; color: #0f172a; letter-spacing: -1px;">Built for Execution</h2>
                <div style="display: flex; flex-direction: column; gap: 24px; font-size: 19px; color: #334155; line-height: 1.7;">
                    <p>We are a meticulously disciplined execution firm purpose-built for the Northeast's most demanding technical deployments. Our focus is singular: delivering physical layer infrastructure exactly to specification, on schedule, and definitively ready for inspection.</p>
                    <p>When high-stakes environments demand meticulous structured cabling, integrated security hardware, and precise routing, integrators and properties rely on our field teams to eliminate variance.</p>
                    <p style="font-weight: 800; color: #0f172a; font-size: 26px; margin-top: 24px; border-left: 4px solid #0f172a; padding-left: 20px; line-height: 1.3;">We don’t consult.<br>We execute.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Core Capabilities -->
    <style>
        .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
        @media (max-width: 1024px) {{ .grid-4 {{ grid-template-columns: repeat(2, 1fr); }} }}
        @media (max-width: 600px) {{ .grid-4 {{ grid-template-columns: 1fr; }} }}
    </style>
    <section class="section services-section theme-dark" id="capabilities" style="background: #020617; padding: 140px 0;">
        <div class="container">
            <div class="services-header" style="margin-bottom: 80px; text-align: left; display: flex; flex-direction: column;">
                <div class="sec-tag" style="border-color: rgba(255,255,255,0.1); color: #cbd5e1; align-self: flex-start; margin-bottom: 24px;">Core Capabilities</div>
                <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 40px;">
                    <h2 style="font-family: var(--font-heading); font-size: 48px; line-height: 1.1; margin: 0; max-width: 500px;">Precision Deployment Spheres</h2>
                    <p style="color: #94a3b8; font-size: 18px; max-width: 500px; margin: 0;">Zero-variance execution across our four core infrastructure verticals. Standardized protocols map to rigorous security and operational requirements.</p>
                </div>
            </div>

            <div class="grid grid-4">
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg></div>
                    <h3 style="font-size: 22px; color: #fff; margin-bottom: 16px;">Structured Cabling</h3>
                    <p style="color: #94a3b8; font-size: 16px; line-height: 1.7;">High-density Cat6A/fiber optic backbones. Immaculate dressing, strict labeling standards, and certified fluke testing arrays.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2" ry="2"></rect><path d="M12 16v-4"></path><path d="M8 12h8"></path></svg></div>
                    <h3 style="font-size: 22px; color: #fff; margin-bottom: 16px;">Video Surveillance</h3>
                    <p style="color: #94a3b8; font-size: 16px; line-height: 1.7;">Precision IP camera mounting. Direct FOV mapping and massive multi-server VMS storage architecture deployment.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                    <h3 style="font-size: 22px; color: #fff; margin-bottom: 16px;">Access Control</h3>
                    <p style="color: #94a3b8; font-size: 16px; line-height: 1.7;">Total physical barrier mitigation. OSDP reader installation, logic panel termination, and complex door hardware electrified routing.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg></div>
                    <h3 style="font-size: 22px; color: #fff; margin-bottom: 16px;">Network Infrastructure</h3>
                    <p style="color: #94a3b8; font-size: 16px; line-height: 1.7;">Enterprise MDF/IDF rack buildouts. Switch chassis elevation, UPS installation, and staging environments for core networking hardware.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 7. Image Break -->
    <div class="img-break" style="background-image: url('https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=1600&q=80'); filter: grayscale(100%) contrast(1.2);"></div>

    <!-- 8. Execution Model -->
    <section class="section bg-white" id="execution-model" style="background: #f8fafc; padding: 140px 0;">
        <div class="container">
            <div class="cs-header" style="text-align: center; margin-bottom: 100px;">
                <div class="sec-tag" style="justify-content:center; margin: 0 auto 24px; background:#e2e8f0; color:#0f172a; border-color:#cbd5e1; font-weight:700;">The Methodology</div>
                <h2 style="font-family: var(--font-heading); font-size: 48px; color: #0f172a; line-height: 1.1; margin-bottom: 24px;">Execution Model</h2>
                <p style="color: #475569; font-size: 19px; max-width: 650px; margin: 0 auto; line-height: 1.7;">A rigorous, standardized four-step deployment protocol ensuring every site is completely verified before turnover.</p>
            </div>

            <div style="display: flex; flex-direction: column; gap: 0; position: relative; max-width: 800px; margin: 0 auto;">
                <div style="position: absolute; left: 32px; top: 0; bottom: 0; width: 2px; background: #cbd5e1; z-index: 1;"></div>
                
                <div style="display: flex; gap: 48px; position: relative; z-index: 2; padding-bottom: 64px;">
                    <div style="width: 64px; height: 64px; border-radius: 50%; background: #0f172a; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 22px; flex-shrink: 0; border: 6px solid #f8fafc; box-shadow: 0 0 0 1px #cbd5e1;">01</div>
                    <div style="padding-top: 14px;">
                        <h3 style="font-size: 28px; color: #0f172a; margin-bottom: 16px;">Site Assessment</h3>
                        <p style="color: #475569; font-size: 17px; line-height: 1.7;">Detailed physical survey, hazard identification, and exact pathway mapping to eliminate execution variances.</p>
                    </div>
                </div>
                <div style="display: flex; gap: 48px; position: relative; z-index: 2; padding-bottom: 64px;">
                    <div style="width: 64px; height: 64px; border-radius: 50%; background: #0f172a; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 22px; flex-shrink: 0; border: 6px solid #f8fafc; box-shadow: 0 0 0 1px #cbd5e1;">02</div>
                    <div style="padding-top: 14px;">
                        <h3 style="font-size: 28px; color: #0f172a; margin-bottom: 16px;">Deployment Planning</h3>
                        <p style="color: #475569; font-size: 17px; line-height: 1.7;">Logistics scheduling, bill of materials staging, and personnel dispatch coordination tailored strictly to site tolerances.</p>
                    </div>
                </div>
                <div style="display: flex; gap: 48px; position: relative; z-index: 2; padding-bottom: 64px;">
                    <div style="width: 64px; height: 64px; border-radius: 50%; background: #0f172a; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 22px; flex-shrink: 0; border: 6px solid #f8fafc; box-shadow: 0 0 0 1px #cbd5e1;">03</div>
                    <div style="padding-top: 14px;">
                        <h3 style="font-size: 28px; color: #0f172a; margin-bottom: 16px;">Field Execution</h3>
                        <p style="color: #475569; font-size: 17px; line-height: 1.7;">Precision installation by directed technicians adhering universally to NEC, ANSI/TIA, and BICSI codes.</p>
                    </div>
                </div>
                <div style="display: flex; gap: 48px; position: relative; z-index: 2;">
                    <div style="width: 64px; height: 64px; border-radius: 50%; background: #0f172a; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 22px; flex-shrink: 0; border: 6px solid #f8fafc; box-shadow: 0 0 0 1px #cbd5e1;">04</div>
                    <div style="padding-top: 14px;">
                        <h3 style="font-size: 28px; color: #0f172a; margin-bottom: 16px;">Verification & Delivery</h3>
                        <p style="color: #475569; font-size: 17px; line-height: 1.7;">Complete fluke testing, visual closeout documentation protocol, and absolutely seamless site turnover.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 9. Partner / Audience Array -->
    <section class="section" style="background: #fff; padding: 140px 0; border-top: 1px solid #e2e8f0;">
        <div class="container">
            <div class="grid grid-2" style="gap: 100px; align-items: center;">
                <div>
                    <div class="sec-tag" style="background: #e2e8f0; color: #0f172a; border-color: #cbd5e1; font-weight: 700; margin-bottom: 24px;">Who We Work With</div>
                    <h2 style="font-family: var(--font-heading); font-size: 46px; color: #0f172a; margin-bottom: 40px; line-height: 1.1;">Partners in Execution</h2>
                    <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 24px;">
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> System Integrators</li>
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Enterprise IT Teams</li>
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Property Managers</li>
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> General Contractors</li>
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Multi-Site Operators</li>
                    </ul>
                </div>
                <div style="background: #0f172a; padding: 80px 64px; border-radius: 4px; text-align: center;">
                    <div style="display: inline-flex; align-items: center; justify-content: center; width: 64px; height: 64px; border-radius: 50%; background: rgba(255,255,255,0.05); color: #fff; margin-bottom: 32px; border: 1px solid rgba(255,255,255,0.1);">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                    </div>
                    <h3 style="color: #fff; font-size: 32px; font-family: var(--font-heading); margin-bottom: 24px; letter-spacing: -1px;">Location</h3>
                    <div style="margin-top: 40px; color: #fff; font-size: 22px; font-weight: 800; letter-spacing: 1px; display: flex; flex-direction: column; gap: 24px;">
                        <span>Fairfield County, CT</span>
                        <div style="width: 24px; height: 1px; background: rgba(255,255,255,0.2); margin: 0 auto;"></div>
                        <span>New York</span>
                        <div style="width: 24px; height: 1px; background: rgba(255,255,255,0.2); margin: 0 auto;"></div>
                        <span>New Jersey</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 10. Final CTA -->
    <section class="section form-section" id="request-service" style="padding: 160px 0; background: #020617; text-align: center;">
        <div class="container">
            <h2 style="font-family: var(--font-heading); font-size: 64px; color: #fff; margin-bottom: 32px; line-height: 1.1; letter-spacing: -2px;">Start Your Deployment</h2>
            
            <a href="mailto:solutions@northeasttechworks.com" style="display: block; font-size: 28px; color: #94a3b8; font-weight: 400; margin-bottom: 56px; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">solutions@northeasttechworks.com</a>
            
            <a href="mailto:solutions@northeasttechworks.com" class="btn btn-primary" style="padding: 24px 64px; font-size: 16px; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; background: #fff; color: #020617;">Request Deployment</a>
        </div>
    </section>

{ft_block}
    <script src="js/main.js"></script>
</body>
</html>
"""

# HTML template setup
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Northeast Technical Works | Infrastructure Deployment Done Right</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
{new_body}
"""

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print("Updated index.html to high-end infrastructure copy")
