import os
import re

base_dir = "e:/websites/NTW"

# Extract header/footer from index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

nav_match = re.search(r'(<div class="top-bar">.*?</header>)', idx_content, re.DOTALL)
new_nav = nav_match.group(1) if nav_match else ""

ft_match = re.search(r'(<footer class="footer".*?</footer>)', idx_content, re.DOTALL)
new_footer = ft_match.group(1) if ft_match else ""

SVG_CHECK = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink:0; color:var(--c-accent);"><polyline points="20 6 9 17 4 12"></polyline></svg>'
SVG_USER = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink:0; color:var(--c-accent);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>'
SVG_EYE = '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--c-accent); margin-bottom:16px;"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>'
SVG_MAP = '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--c-accent); margin-bottom:16px;"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>'
SVG_TOOL = '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--c-accent); margin-bottom:16px;"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>'
SVG_CHECK_LG = '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--c-accent); margin-bottom:16px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>'

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us | Northeast Technical Works (NTW)</title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
{new_nav}

    <!-- Hero Section -->
    <section class="hero theme-dark" style="min-height: 40vh; padding-top: 120px; padding-bottom: 60px;">
        <div class="container relative">
            <div class="hero-content">
                <div class="hero-tag" style="margin-bottom: 24px;">Who We Are</div>
                <h1 style="font-size: 56px; line-height: 1.1; margin-bottom: 20px;">Built on Discipline.<br>Trusted in the Field.</h1>
                <p style="font-size: 20px; color: var(--c-dark-text-body); max-width: 650px; margin-bottom: 32px; line-height: 1.7;">Northeast Technical Works is a field execution team focused on delivering clean, reliable infrastructure across high-demand environments.</p>
                <a href="/contact.html" class="btn btn-primary" style="padding: 16px 32px; font-size: 16px;">Discuss a Project</a>
            </div>
        </div>
    </section>

    <!-- Who We Are -->
    <section style="background: var(--c-surface-light); padding: 100px 0; border-bottom: 1px solid var(--c-border-light);">
        <div class="container">
            <div class="grid grid-2" style="align-items: center; gap: 80px;">
                <div style="position: relative; border-radius: 12px; overflow: hidden; box-shadow: var(--sh-md);">
                    <img src="https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?auto=format&fit=crop&w=800&q=80" alt="NTW technical routing" style="width: 100%; height: auto; display: block; object-fit: cover;" />
                </div>
                <div>
                    <h2 style="font-size: 40px; line-height: 1.2; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Who We Are</h2>
                    <p style="font-size: 20px; color: var(--c-text-body); margin-bottom: 24px; line-height: 1.7;">We’re a field execution company specializing in structured cabling, security systems, and network infrastructure.</p>
                    <p style="font-size: 20px; color: var(--c-text-body); margin-bottom: 0; line-height: 1.7;">We work with integrators, property teams, and contractors who need jobs done right without constant oversight.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Why We Exist -->
    <section style="background: #fff; padding: 120px 0; border-bottom: 1px solid var(--c-border-light);">
        <div class="container text-center" style="max-width: 800px;">
            <div class="sec-tag" style="margin-bottom: 24px;">The Core Problem</div>
            <h2 style="font-size: 44px; margin-bottom: 32px; font-family: var(--font-heading); color: var(--c-text-main);">Why We Exist</h2>
            <p style="font-size: 22px; color: var(--c-text-body); line-height: 1.7; margin-bottom: 24px;">
                Most infrastructure issues don’t come from bad design — <strong style="color: var(--c-text-main);">they come from poor execution in the field.</strong>
            </p>
            <p style="font-size: 20px; color: var(--c-text-body); line-height: 1.7; margin-bottom: 32px;">
                Messy installs, missed details, and inconsistent work create long-term problems.
            </p>
            <div style="display: inline-block; background: var(--c-surface-light); padding: 16px 32px; border-radius: 8px; border: 1px solid var(--c-border-light);">
                <strong style="color: var(--c-accent); font-size: 18px; letter-spacing: 1px; text-transform: uppercase;">We built NTW to eliminate that.</strong>
            </div>
        </div>
    </section>

    <!-- How We Operate -->
    <section style="background: var(--c-surface-light); padding: 120px 0; border-bottom: 1px solid var(--c-border-light);">
        <div class="container">
            <div style="text-align: center; max-width: 700px; margin: 0 auto 60px;">
                <h2 style="font-size: 44px; margin-bottom: 20px; font-family: var(--font-heading); color: var(--c-text-main);">How We Operate</h2>
                <p style="font-size: 20px; color: var(--c-text-body); line-height: 1.6;">We follow a structured approach on every job. <strong style="color: var(--c-text-main);">No shortcuts. No guesswork.</strong></p>
            </div>
            
            <div class="grid grid-4" style="gap: 24px;">
                <div style="background: #fff; padding: 40px 32px; border-radius: 12px; border: 1px solid var(--c-border-light); box-shadow: var(--sh-sm);">
                    {SVG_EYE}
                    <h3 style="font-size: 20px; margin-bottom: 12px; color: var(--c-text-main);">1. Understand the Scope</h3>
                    <p style="font-size: 16px; color: var(--c-text-body); line-height: 1.6; margin:0;">We review blueprints and deliverables before our boots hit the ground.</p>
                </div>
                <div style="background: #fff; padding: 40px 32px; border-radius: 12px; border: 1px solid var(--c-border-light); box-shadow: var(--sh-sm);">
                    {SVG_MAP}
                    <h3 style="font-size: 20px; margin-bottom: 12px; color: var(--c-text-main);">2. Plan Properly</h3>
                    <p style="font-size: 16px; color: var(--c-text-body); line-height: 1.6; margin:0;">Mapping out routes, materials, and potential contingencies ahead of time.</p>
                </div>
                <div style="background: #fff; padding: 40px 32px; border-radius: 12px; border: 1px solid var(--c-border-light); box-shadow: var(--sh-sm);">
                    {SVG_TOOL}
                    <h3 style="font-size: 20px; margin-bottom: 12px; color: var(--c-text-main);">3. Execute Cleanly</h3>
                    <p style="font-size: 16px; color: var(--c-text-body); line-height: 1.6; margin:0;">Meticulous dressing, compliant runs, and perfectly mounted hardware.</p>
                </div>
                <div style="background: #fff; padding: 40px 32px; border-radius: 12px; border: 1px solid var(--c-border-light); box-shadow: var(--sh-sm);">
                    {SVG_CHECK_LG}
                    <h3 style="font-size: 20px; margin-bottom: 12px; color: var(--c-text-main);">4. Verify Everything</h3>
                    <p style="font-size: 16px; color: var(--c-text-body); line-height: 1.6; margin:0;">Testing, labeling, and quality assurance before turnover.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Differences & Who We Work With -->
    <section style="background: #fff; padding: 120px 0;">
        <div class="container">
            <div class="grid grid-2" style="gap: 60px;">
                <!-- Left Block -->
                <div style="background: var(--c-surface-light); padding: 50px; border-radius: 16px; border: 1px solid var(--c-border-light);">
                    <h2 style="font-size: 32px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">What Makes Us Different</h2>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 20px;">
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_CHECK}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">We follow scope and prints exactly</span>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_CHECK}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">We don't need babysitting</span>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_CHECK}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">We keep installs clean and organized</span>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_CHECK}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">We show up prepared</span>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_CHECK}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">We finish properly</span>
                        </li>
                    </ul>
                </div>
                
                <!-- Right Block -->
                <div style="background: var(--c-surface-light); padding: 50px; border-radius: 16px; border: 1px solid var(--c-border-light);">
                    <h2 style="font-size: 32px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">Who We Work With</h2>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 20px;">
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_USER}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">System Integrators</span>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_USER}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">IT Teams</span>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_USER}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">Property Managers</span>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_USER}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">General Contractors</span>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 16px;">
                            {SVG_USER}
                            <span style="font-size: 18px; color: var(--c-text-body); font-weight: 500; line-height: 1.4;">Multi-Site Operators</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Trust Statement & CTA -->
    <section class="theme-dark" style="padding: 120px 0; background: #020617; border-top: 1px solid rgba(255,255,255,0.05); text-align: center;">
        <div class="container" style="max-width: 800px; display: flex; flex-direction: column; align-items: center;">
            <div style="margin-bottom: 60px;">
                <p style="font-size: 26px; color: #fff; line-height: 1.6; font-style: italic; opacity: 0.9;">
                    "We’re usually brought in when the job needs to be done right — whether it’s a clean install from the start or fixing work that didn’t hold up."
                </p>
            </div>
            
            <div style="width: 100%; height: 1px; background: rgba(255,255,255,0.1); margin-bottom: 60px;"></div>
            
            <h2 style="font-size: 40px; margin-bottom: 16px; font-family: var(--font-heading); color: #fff;">Need a Team You Don’t Have to Worry About?</h2>
            <p style="font-size: 20px; color: var(--c-dark-text-body); max-width: 600px; margin: 0 auto 40px;">Send us your scope — we’ll take it from there.</p>
            <a href="/contact.html" class="btn btn-primary" style="padding: 18px 48px; font-size: 18px;">Request Deployment</a>
        </div>
    </section>

{new_footer}
    <script src="/js/main.js"></script>
</body>
</html>
"""

# Write Output
with open(os.path.join(base_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)

print("about.html successfully refactored with new copy layout!")
