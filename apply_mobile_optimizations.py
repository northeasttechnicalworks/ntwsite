import os

base_dir = "e:/websites/NTW"
css_path = os.path.join(base_dir, "css", "styles.css")
idx_path = os.path.join(base_dir, "index.html")

# 1. CSS Injection
css_payload = """
/* ------------------------------------- */
/* MOBILE CONVERSION & UX OVERRIDES      */
/* ------------------------------------- */
@media (max-width: 900px) {
    /* Safe Area Padding for fixed CTA */
    body {
        padding-bottom: 80px !important;
    }

    /* Paragraph Readability */
    p {
        line-height: 1.8 !important;
        margin-bottom: 24px !important;
        padding-right: 0 !important; 
    }

    /* Conversion Targeting (Buttons) */
    .btn {
        min-height: 54px !important;
        display: flex !important;
        width: 100% !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 18px !important;
        padding: 16px 24px !important;
        margin-bottom: 16px !important;
    }

    /* Form specific overrides */
    .lead-form .btn { margin-bottom: 0 !important; }

    /* Remove heavy/sticky animations for instant scroll responsiveness */
    .sticky-card {
        height: auto !important;
        min-height: auto !important;
        position: relative !important;
        top: auto !important;
        box-shadow: none !important;
        border-top: none !important;
        padding: 60px 0 !important;
    }
    
    .timeline-step {
       opacity: 1 !important;
       transform: none !important;
       transition: none !important;
    }

    .reveal {
       opacity: 1 !important;
       transform: none !important;
       transition: none !important;
    }

    /* Fixed Sticky CTA */
    .mobile-sticky-cta {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0A0A0A;
        border-top: 1px solid rgba(255,255,255,0.1);
        z-index: 9999;
        display: flex !important;
        padding: 12px 16px;
        padding-bottom: calc(12px + env(safe-area-inset-bottom)); /* iOS safe zone */
        gap: 12px;
        box-shadow: 0 -4px 12px rgba(0,0,0,0.5);
    }
    
    .mobile-sticky-cta .btn {
        width: 50% !important;
        flex: 1 !important;
        margin-bottom: 0 !important;
        border-radius: 6px !important;
        font-size: 16px !important;
        min-height: 48px !important;
        padding: 12px !important;
        font-weight: 600 !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    .mobile-sticky-cta .btn-request {
        background-color: transparent !important;
        color: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }

    .mobile-sticky-cta .btn-call {
        background-color: #C9A646 !important;
        color: #000000 !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(201, 166, 70, 0.4) !important;
    }
}
"""

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if "MOBILE CONVERSION & UX OVERRIDES" not in css_content:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(css_payload)
    print("CSS Payload injected successfully.")
else:
    print("CSS Payload already exists.")

# 2. HTML CTA Injection (index.html)
html_payload = """
    <!-- MOBILE STICKY CTA BAR -->
    <div class="mobile-sticky-cta mobile-only">
        <a href="/contact.html" class="btn btn-request">Request Service</a>
        <a href="tel:2034181608" class="btn btn-call">Call Now</a>
    </div>
"""

with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

if "<!-- MOBILE STICKY CTA BAR -->" not in idx_content:
    idx_content = idx_content.replace(
        "</footer>",
        f"</footer>\n{html_payload}"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("HTML Mobile Sticky injected into index.html successfully.")
else:
    print("HTML Payload already exists in index.html.")
