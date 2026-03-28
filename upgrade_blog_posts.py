import os
import re

blog_dir = r"e:\websites\NTW\blog"
template_path = r"e:\websites\NTW\template_blog.html"

with open(template_path, 'r', encoding='utf-8') as f:
    TEMPLATE = f.read()

STYLE_BLOCK = """    <style>
        :root {
            --blog-bg: #F5F5F3;
            --blog-border: rgba(0,0,0,0.08);
            --blog-gold: #8E7A50;
            --blog-text: #111111;
            --blog-text-muted: #555555;
        }
        
        body { background: var(--blog-bg); color: var(--blog-text); line-height: 1.8; font-family: var(--font-body); }
        
        .article-hero {
            padding: 0;
            background: #f8f9fa;
            border-bottom: 1px solid var(--blog-border);
            text-align: center;
        }

        .hero-image {
            width: 100%;
            height: 350px;
            object-fit: cover;
            filter: grayscale(10%) contrast(1.1);
            display: block;
        }

        .hero-text-wrap {
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 40px 60px;
        }

        .category-tag {
            color: var(--blog-gold);
            font-size: 13px;
            font-weight: 900;
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-bottom: 24px;
            display: inline-block;
        }

        .article-title {
            font-family: var(--font-heading);
            font-size: 56px;
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 24px;
            letter-spacing: -2px;
            color: var(--blog-text);
        }

        .article-meta {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 24px;
            color: var(--blog-text-muted);
            font-size: 14px;
            font-weight: 700;
            border-top: 1px solid var(--blog-border);
            padding-top: 20px;
            margin-top: 32px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .article-body {
            max-width: 900px;
            margin: 0 auto;
            padding: 80px 80px;
            font-size: 20px;
            color: #333333;
            line-height: 1.8;
            background: #FFFFFF;
            box-shadow: 0 4px 24px rgba(0,0,0,0.02);
            margin-top: -40px;
            position: relative;
            z-index: 10;
            border-radius: 4px;
            margin-bottom: 120px;
        }

        .article-body h2 {
            font-family: var(--font-heading);
            font-size: 36px;
            font-weight: 900;
            color: var(--blog-text);
            margin: 64px 0 24px;
            line-height: 1.2;
            letter-spacing: -1px;
        }

        .article-body h3 {
            font-family: var(--font-heading);
            font-size: 26px;
            font-weight: 800;
            color: var(--blog-text);
            margin: 40px 0 20px;
        }

        .article-body p { margin-bottom: 24px; }
        .article-body strong { color: #000; font-weight: 800; }

        .article-img {
            width: 100%;
            height: auto;
            border-radius: 4px;
            margin: 40px 0;
        }

        @media (max-width: 1024px) {
            .article-body { width: 95%; padding: 60px 40px; margin-left: auto; margin-right: auto; }
        }

        @media (max-width: 768px) {
            .article-title { font-size: 38px; }
            .hero-image { height: 300px; }
            .article-body { padding: 40px 20px; font-size: 18px; }
        }
    </style>"""

# High-fidelity unique images
IMAGE_MAP = {
    "zero-downtime-mdf-cutover.html": "/images/blog/cutover.png",
    "osdp-standardization.html": "/images/blog/osdp.png",
    "certifying-fluke-networks.html": "/images/blog/fluke.png",
    "warehouse-surveillance-deployment.html": "/images/blog/warehouse.png",
    "office-infrastructure-buildout.html": "/images/blog/office.png",
    "multi-site-cabling-rollout.html": "/images/blog/retail.png",
    "access-control-installation.html": "/images/blog/logic_panel.png",
    "access-control-deployments.html": "/images/blog/thumb_security.png",
    "conduit-vs-open-cabling.html": "/images/blog/conduit.png",
    "multi-site-rollouts.html": "/images/blog/thumb_operations.png",
    "preventive-maintenance-cost.html": "/images/blog/maintenance.png",
    "cable-management-costs.html": "/images/blog/cable_mgmt.png",
    "surveillance-failure-rates.html": "/images/blog/thumb_cabling.png"
}

files = [f for f in os.listdir(blog_dir) if f.endswith(".html")]

for filename in files:
    path = os.path.join(blog_dir, filename)
    
    # SPECIAL CASE: OSDP reset if clean baseline exists
    clean_baseline = path + "_clean_body.txt"
    if os.path.exists(clean_baseline):
        with open(clean_baseline, 'r', encoding='utf-8') as f:
            article_body_raw = f.read()
    else:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract content from existing article-body
            body_match = re.search(r'<article class="article-body">(.*?)</article>', content, re.DOTALL)
            if body_match:
                article_body_raw = body_match.group(1)
            else:
                article_body_raw = content

    # AGGRESSIVE SANITIZATION
    # 1. Remove all inline styles/scripts
    article_body_raw = re.sub(r'<style.*?</style>', '', article_body_raw, flags=re.DOTALL)
    article_body_raw = re.sub(r'<script.*?</script>', '', article_body_raw, flags=re.DOTALL)
    
    # 2. Identify and remove any DIVs (which are usually CTAs or remnants)
    # We only want P, H1, H2, H3 tags in the pristine dispatch body
    article_body_raw = re.sub(r'<div.*?>.*?</div>', '', article_body_raw, flags=re.DOTALL)
    
    # 3. Final extraction of *only* valid paragraph and header content
    # This prevents nesting issues and phantom padding
    clean_paragraphs = re.findall(r'<(p|h2|h3|h4).*?>.*?</\1>', article_body_raw, re.DOTALL | re.IGNORECASE)
    # Actually re.findall above only returns the tag name. Need to capture the whole block.
    clean_blocks = re.findall(r'(<(p|h2|h3|h4).*?>.*?</\2>)', article_body_raw, re.DOTALL | re.IGNORECASE)
    body_content = "\n\n".join([block[0] for block in clean_blocks])

    # 4. Fallback for non-standard markup
    if not body_content.strip():
        body_content = re.sub(r'<.*?>', '', article_body_raw) # strip all tags as last resort
        body_content = "<p>" + body_content.strip() + "</p>"

    # 5. Extraction of Title/Category for current file
    with open(path, 'r', encoding='utf-8') as f:
        full_content = f.read()
        title_match = re.search(r'<h1.*?>(.*?)</h1>', full_content, re.DOTALL)
        title = title_match.group(1).strip() if title_match else filename.replace(".html", "").replace("-", " ").title()
        title = re.sub(r'<.*?>', '', title)
        
        cat_match = re.search(r'<span class="category-tag">(.*?)</span>', full_content)
        category = cat_match.group(1) if cat_match else "Intelligence"
        
        meta_match = re.search(r'<div class="article-meta">(.*?)</div>', full_content, re.DOTALL)
        meta = meta_match.group(1).strip() if meta_match else "Field Dispatch"

    hero_img = IMAGE_MAP.get(filename, "/images/blog/infrastructure.png")

    # 6. Hero Construction
    HERO_HTML = f"""    <section class="article-hero">
        <img src="{hero_img}" class="hero-image" alt="{title}">
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
    </section>"""

    # 7. Rendering
    final_output = TEMPLATE.replace("[[TITLE]]", title)
    final_output = final_output.replace("[[STYLE_INJECTION]]", STYLE_BLOCK)
    final_output = final_output.replace("[[HERO_INJECTION]]", HERO_HTML)
    final_output = final_output.replace("[[CONTENT_INJECTION]]", body_content.strip())

    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_output)

print(f"Standardized {len(files)} articles with aggressive sanitation and unique imagery.")
