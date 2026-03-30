import os
import re

blog_dir = r"e:\websites\NTW\blog"
files = [f for f in os.listdir(blog_dir) if f.endswith(".html")]

IMAGE_MAP = {
    "access-control-deployments.html": "thumb_security.png",
    "access-control-installation.html": "logic_panel.png",
    "cable-management-costs.html": "cable_mgmt.png",
    "certifying-fluke-networks.html": "fluke.png",
    "conduit-vs-open-cabling.html": "conduit.png",
    "multi-site-cabling-rollout.html": "retail.png",
    "multi-site-rollouts.html": "thumb_operations.png",
    "office-infrastructure-buildout.html": "office.png",
    "osdp-standardization.html": "osdp.png",
    "preventive-maintenance-cost.html": "maintenance.png",
    "surveillance-failure-rates.html": "analytics.png", 
    "warehouse-surveillance-deployment.html": "warehouse.png",
    "zero-downtime-mdf-cutover.html": "cutover.png"
}

NAVBAR = """    <!-- 1. Top Bar -->
    <div class="top-bar">
        <div class="container flex-between">
            <div class="top-contact">
                <span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    solutions@northeasttechworks.com
                </span>
                <span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                    (203) 418-1608
                </span>
            </div>
            <div class="top-contact" style="gap: 16px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
            </div>
        </div>
    </div>

    <header class="navbar">
        <div class="container nav-container">
            <a href="/index.html" class="brand-logo">
                <div class="brand-icon">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="white" style="margin: 5px;"><rect x="2" y="2" width="20" height="20" rx="4"/></svg>
                </div>
                NTW
            </a>
            <ul class="nav-links">
                <li><a href="/index.html">Home</a></li>
                <li><a href="/services.html">Services</a></li>
                <li><a href="/coverage.html">Coverage</a></li>
                <li><a href="/industries.html">Industries</a></li>
                <li><a href="/about.html">About</a></li>
                <li><a href="/blog.html">Blog</a></li>
            </ul>
            <a href="/contact.html" class="btn btn-dark">Contact Us</a>
        </div>
    </header>"""

for filename in files:
    path = os.path.join(blog_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine Image
    image_name = IMAGE_MAP.get(filename, "analytics.png")

    cat_match = re.search(r'<span class="category-tag">(.*?)</span>', content)
    title_match = re.search(r'<h1 class="article-title">(.*?)</h1>', content)
    meta_match = re.search(r'<div class="article-meta">(.*?)</div>', content, re.DOTALL)

    category = cat_match.group(1) if cat_match else "Intelligence"
    title = title_match.group(1) if title_match else "Untitled"
    meta = meta_match.group(1).strip() if meta_match else "<span>January 2026</span>"

    NEW_HEADER_HERO = f'''<body>
{NAVBAR}

    <section class="article-hero">
        <img src="/images/blog/{image_name}" class="hero-image" alt="{title}">
        <div class="container">
            <div class="hero-text-wrap">
                <a href="/blog.html" style="color: #111111; text-decoration: none; font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 2.5px; display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 32px;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    Back to Insights
                </a>
                <span class="category-tag">{category}</span>
                <h1 class="article-title">{title}</h1>
                <div class="article-meta">
                    {meta}
                </div>
            </div>
        </div>
    </section>

    <article class="article-body">'''

    content = re.sub(r'<body>.*?<article class="article-body">', NEW_HEADER_HERO, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Repaired hero mapping for {len(files)} blog dispatches.")
