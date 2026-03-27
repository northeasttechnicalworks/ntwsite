import os
import re

file_path = "e:/websites/NTW/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Map styling & HTML
map_section = """
    <!-- 10. Coverage Map Showcase -->
    <style>
        .map-section { background: #020617; padding: 140px 0; border-top: 1px solid #1e293b; overflow: hidden; position: relative; }
        .map-section::before { content: ""; position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(90, 103, 216, 0.05) 0%, transparent 70%); pointer-events: none; }
    </style>
    <section class="section map-section" id="coverage">
        <div class="container">
            <div class="grid grid-2" style="align-items: center; gap: 80px;">
                <div>
                    <div class="sec-tag" style="border-color: rgba(255,255,255,0.1); color: #cbd5e1; margin-bottom: 24px;">Territory Mapping</div>
                    <h2 style="font-family: var(--font-heading); font-size: 48px; color: #fff; margin-bottom: 32px; line-height: 1.1; letter-spacing: -1px;">The Northeast Corridor<br>Execution Grid</h2>
                    <p style="color: #94a3b8; font-size: 18px; line-height: 1.7; margin-bottom: 40px;">Purpose-built for the most challenging topological deployments in the United States. We command the logistical execution path from the dense New York Metro to the expansive perimeters of neighboring states.</p>
                    <div style="display: flex; gap: 40px; margin-bottom: 40px;">
                        <div>
                            <strong style="color: #fff; font-size: 32px; display: block; margin-bottom: 8px;">3</strong>
                            <span style="color: #64748b; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Primary States</span>
                        </div>
                        <div>
                            <strong style="color: #fff; font-size: 32px; display: block; margin-bottom: 8px;">24/7</strong>
                            <span style="color: #64748b; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Dispatch Readiness</span>
                        </div>
                    </div>
                    <a href="/coverage.html" class="btn btn-primary" style="background: transparent; border: 1px solid #64748b; color: #fff;">View Full Coverage Topology</a>
                </div>
                <div style="position: relative; height: 600px; border-radius: 12px; background: rgba(15, 23, 42, 0.4); border: 1px solid #1e293b; box-shadow: 0 0 80px rgba(0,0,0,0.5) inset; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                    <svg viewBox="0 0 600 900" width="100%" height="150%" style="transform: scale(0.85);" preserveAspectRatio="xMidYMid slice">
                      <defs>
                        <pattern id="hp-grid" width="40" height="40" patternUnits="userSpaceOnUse">
                          <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.02)" stroke-width="1" />
                        </pattern>
                        <filter id="hp-glow" x="-50%" y="-50%" width="200%" height="200%">
                          <feGaussianBlur stdDeviation="4" result="blur" />
                          <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>
                      </defs>
                      <rect width="100%" height="100%" fill="url(#hp-grid)" />
                      <!-- Simple representation of the node network -->
                      <g stroke="rgba(90, 103, 216, 0.2)" stroke-width="2" fill="none">
                          <path d="M 300 300 L 250 400 L 320 500 L 400 350 Z" />
                          <path d="M 250 400 L 150 450" />
                          <path d="M 320 500 L 280 650" />
                      </g>
                      <!-- Animated blips -->
                      <circle r="3" fill="#60A5FA" filter="url(#hp-glow)">
                        <animateMotion dur="3s" repeatCount="indefinite" path="M 300 300 L 250 400 L 320 500 L 400 350 Z" />
                      </circle>
                      <circle r="3" fill="#60A5FA" filter="url(#hp-glow)">
                        <animateMotion dur="4s" repeatCount="indefinite" path="M 250 400 L 150 450" />
                      </circle>
                      <!-- Nodes -->
                      <g transform="translate(300, 300)"><circle r="8" fill="#5A67D8"/><circle r="4" fill="#fff" filter="url(#hp-glow)"/></g>
                      <g transform="translate(250, 400)">
                        <circle r="12" fill="none" stroke="#5A67D8"><animate attributeName="r" values="12; 30" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.8; 0" dur="2s" repeatCount="indefinite"/></circle>
                        <circle r="8" fill="#5A67D8"/><circle r="4" fill="#fff" filter="url(#hp-glow)"/><text x="20" y="5" fill="#fff" font-family="var(--font-heading)" font-weight="700">New York</text>
                      </g>
                      <g transform="translate(320, 500)"><circle r="8" fill="#5A67D8"/><circle r="4" fill="#fff" filter="url(#hp-glow)"/><text x="20" y="5" fill="#fff" font-family="var(--font-heading)" font-weight="700">New Jersey</text></g>
                      <g transform="translate(400, 350)"><circle r="8" fill="#5A67D8"/><circle r="4" fill="#fff" filter="url(#hp-glow)"/><text x="20" y="5" fill="#fff" font-family="var(--font-heading)" font-weight="700">Connecticut</text></g>
                      <g transform="translate(150, 450)"><circle r="6" fill="#475569"/><circle r="3" fill="#94a3b8"/></g>
                      <g transform="translate(280, 650)"><circle r="6" fill="#475569"/><circle r="3" fill="#94a3b8"/></g>
                    </svg>
                </div>
            </div>
        </div>
    </section>
"""

# Blog Insights Section HTML
blog_section = """
    <!-- 11. Execution Insights / Blog -->
    <style>
        .blog-card { display: flex; flex-direction: column; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; transition: transform 0.3s, box-shadow 0.3s; height: 100%; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
        .blog-card:hover { transform: translateY(-5px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); }
        .blog-card-img { width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid #e2e8f0; }
        .blog-card-content { padding: 32px; display: flex; flex-direction: column; flex-grow: 1; }
        .blog-meta { display: flex; gap: 16px; color: #64748b; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; }
        .blog-title { font-family: var(--font-heading); font-size: 24px; color: #0f172a; margin-bottom: 16px; line-height: 1.3; }
        .blog-excerpt { color: #475569; font-size: 16px; line-height: 1.6; margin-bottom: 24px; flex-grow: 1; }
        .blog-link { color: var(--c-accent); font-weight: 700; text-transform: uppercase; font-size: 13px; letter-spacing: 1px; text-decoration: none; display: flex; align-items: center; gap: 8px; }
        .blog-link:hover { text-decoration: underline; }
    </style>
    <section class="section" style="background: #f8fafc; padding: 140px 0; border-top: 1px solid #e2e8f0;">
        <div class="container">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 80px; flex-wrap: wrap; gap: 40px;">
                <div>
                    <div class="sec-tag" style="background: #e2e8f0; color: #0f172a; border-color: #cbd5e1; font-weight: 700; margin-bottom: 24px;">Execution Logs</div>
                    <h2 style="font-family: var(--font-heading); font-size: 46px; color: #0f172a; line-height: 1.1; margin: 0;">Infrastructure Insights</h2>
                </div>
                <a href="/blog.html" class="btn btn-outline" style="border: 2px solid #0f172a; color: #0f172a; font-weight: 700; padding: 14px 32px;">Read Full Dispatch Log</a>
            </div>
            
            <div class="grid grid-3" style="align-items: stretch;">
                
                <article class="blog-card">
                    <img src="https://images.unsplash.com/photo-1558494949-ef010cbd1317?auto=format&fit=crop&w=600&q=80" alt="Enterprise Rack Architecture" class="blog-card-img" style="filter: grayscale(30%) contrast(1.1);">
                    <div class="blog-card-content">
                        <div class="blog-meta">
                            <span>Case File</span><span>&middot;</span><span>Mar 24</span>
                        </div>
                        <h3 class="blog-title"><a href="/blog/zero-downtime-mdf-cutover.html" style="color: inherit; text-decoration: none;">Executing a Zero-Downtime MDF Cutover for a 12-Story Manhattan Tower</a></h3>
                        <p class="blog-excerpt">We unpack the rigorous logistics, contingency pathways, and off-hour execution matrix required to upgrade a core switching environment traversing tenanted floors without disrupting live trading operations.</p>
                        <a href="/blog/zero-downtime-mdf-cutover.html" class="blog-link">Review Dispatch <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg></a>
                    </div>
                </article>
                
                <article class="blog-card">
                    <img src="https://images.unsplash.com/photo-1520869562399-e772f042f422?auto=format&fit=crop&w=600&q=80" alt="Access Control Hardware" class="blog-card-img" style="filter: grayscale(30%) contrast(1.1);">
                    <div class="blog-card-content">
                        <div class="blog-meta">
                            <span>Protocol</span><span>&middot;</span><span>Feb 12</span>
                        </div>
                        <h3 class="blog-title"><a href="/blog/osdp-standardization.html" style="color: inherit; text-decoration: none;">Why OSDP is Now Mandatory for Real Estate Access Deployments</a></h3>
                        <p class="blog-excerpt">Legacy Wiegand wiring leaves commercial real estate critically vulnerable. Here is why we mandate Open Supervised Device Protocol (OSDP) across all new tenant security and perimeter barrier rollouts.</p>
                        <a href="/blog/osdp-standardization.html" class="blog-link">Review Dispatch <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg></a>
                    </div>
                </article>
                
                <article class="blog-card">
                    <img src="https://images.unsplash.com/photo-1614064641913-6b71a2a47291?auto=format&fit=crop&w=600&q=80" alt="Cat6A Cabling Bundles" class="blog-card-img" style="filter: grayscale(30%) contrast(1.1);">
                    <div class="blog-card-content">
                        <div class="blog-meta">
                            <span>Standard</span><span>&middot;</span><span>Jan 08</span>
                        </div>
                        <h3 class="blog-title"><a href="/blog/certifying-fluke-networks.html" style="color: inherit; text-decoration: none;">The Cost of Uncertified Drops: Why We Fluke-Test Every Run</a></h3>
                        <p class="blog-excerpt">Cabling isn't just copper; it's the physics handling your throughput. We explain our rigid testing standards, cross-talk mitigation, and why uncertified field work destroys long-term IT scalability.</p>
                        <a href="/blog/certifying-fluke-networks.html" class="blog-link">Review Dispatch <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg></a>
                    </div>
                </article>
                
            </div>
        </div>
    </section>
"""

# Splice directly before the footer script/element
footer_marker = '<script src="/js/main.js"></script>'
if footer_marker in content:
    content = content.replace(footer_marker, map_section + '\n' + blog_section + '\n' + footer_marker)
else:
    content = content.replace('<footer class="footer"', map_section + '\n' + blog_section + '\n<footer class="footer"')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Map and Blog injected!")
