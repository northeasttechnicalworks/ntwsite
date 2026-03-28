import os
import re

blog_dir = r"e:\websites\NTW\blog"
files = [f for f in os.listdir(blog_dir) if f.endswith(".html")]

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
            <a href="/contact.html" class="btn btn-dark">Start Your Deployment</a>
        </div>
    </header>"""

FOOTER = """    <footer class="footer" style="background: #020617; padding: 100px 0 40px; border-top: 1px solid #1e293b;">
        <div class="container">
            <div class="footer-top">
                <div style="max-width: 400px;">
                    <span style="font-family: var(--font-heading); font-weight: 800; color: #fff; font-size: 28px; display: block; margin-bottom: 16px; letter-spacing: -1px;">NTW</span>
                    <p style="font-size: 16px; color: #94a3b8; line-height: 1.7; margin-bottom: 24px;">The Northeast corridor's most disciplined infrastructure deployment team. Delivering inspection-ready execution across NY, NJ, and CT.</p>
                    <p style="font-size: 14px; color: #64748b; font-style: italic; margin-bottom: 32px;">Northeast Technical Works is built for environments where failure is not tolerated.</p>
                    <div>
                        <strong style="color: #fff; display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;">Dispatch Line</strong>
                        <a href="tel:2034181608" style="color: #fff; font-size: 20px; font-weight: 600; text-decoration: none; display: block; margin-bottom: 4px; transition: color 0.2s;" onmouseover="this.style.color='var(--c-accent)'" onmouseout="this.style.color='#fff'">(203) 418-1608</a>
                        <a href="mailto:solutions@northeasttechworks.com" style="color: var(--c-accent); font-size: 16px; text-decoration: none; transition: opacity 0.2s;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">solutions@northeasttechworks.com</a>
                    </div>
                </div>
                
                <div>
                    <h4 style="color: #fff; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px;">Core Capabilities</h4>
                    <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 16px; margin: 0;">
                        <li><a href="/services/structured-cabling.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Structured Cabling</a></li>
                        <li><a href="/services/network-rack-buildouts.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Network Racks</a></li>
                        <li><a href="/services/video-surveillance-installation.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Video Surveillance</a></li>
                        <li><a href="/services/access-control-installation.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Access Control</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>"""

for filename in files:
    path = os.path.join(blog_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extract corrupted Metadata
    cat_match = re.search(r'<span class="category-tag">(.*?)</span>', content)
    title_match = re.search(r'<h1 class="article-title">(.*?)</h1>', content)
    meta_match = re.search(r'<div class="article-meta">(.*?)</div>', content, re.DOTALL)

    category = cat_match.group(1) if cat_match else "Intelligence"
    title = title_match.group(1) if title_match else "Untitled Breakdown"
    meta = meta_match.group(1) if meta_match else "<span>January 2026</span>"

    # 2. Re-construct the entire Header and Hero area
    # From <body> to the start of <article>
    NEW_HEADER_HERO = f"""<body>
{NAVBAR}

    <section class="article-hero">
        <div class="container">
            <div style="max-width: 900px; margin: 0 auto;">
                <a href="/blog.html" style="color: #111111; text-decoration: none; font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 2.5px; display: flex; align-items: center; gap: 10px; margin-bottom: 40px;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    Back to Insights
                </a>
                <span class="category-tag">{category}</span>
                <h1 class="article-title">{title}</h1>
                <div class="article-meta">
                    {meta.strip()}
                </div>
            </div>
        </div>
    </section>

    <article class="article-body">"""

    # Replace everything from <body> to <article class="article-body">
    content = re.sub(r'<body>.*?<article class="article-body">', NEW_HEADER_HERO, content, flags=re.DOTALL)

    # 3. Fix Author Box
    content = re.sub(r'<div class="author-box">.*?</div>', 
                     """<div class="author-box">
            <div style="width: 64px; height: 64px; background: #111111; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 800; font-size: 18px;">NTW</div>
            <div class="author-info">
                <h4>NTW Field Intelligence</h4>
                <p>Technical dispatches from our deployment teams. Direct, grounded, and focused on physical-layer reality.</p>
            </div>
        </div>""", content, flags=re.DOTALL)

    # 4. Standardize Footer
    content = re.sub(r'<footer class="footer".*?</footer>', FOOTER, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Repaired {len(files)} blog dispatches.")
