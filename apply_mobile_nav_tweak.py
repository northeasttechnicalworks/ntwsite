import os

base_dir = "e:/websites/NTW"

# 1. CSS Injection
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

css_payload = """
/* ------------------------------------- */
/* MOBILE NAV HEADER & SOCIALS OVERRIDE  */
/* ------------------------------------- */
@media (max-width: 900px) {
    /* Hide top bar */
    .top-bar { display: none !important; }

    /* Shrink the header CTA button */
    .header-cta-mobile {
        display: inline-flex !important;
        width: auto !important;
        margin-left: auto !important;
        margin-right: 24px !important; /* ample space between button and menu */
        margin-bottom: 0 !important;
        font-size: 13px !important;
        padding: 8px 16px !important;
        min-height: auto !important;
        border-radius: 4px !important;
        background: var(--c-bg-dark) !important;
        color: #fff !important;
        white-space: nowrap !important;
    }

    /* Keep the logo and container tight */
    .nav-container {
        padding: 0 16px !important;
    }

    /* Socials Tray inside Mobile Nav Links */
    .mobile-social-tray {
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        gap: 32px !important;
        margin-top: 40px !important;
        width: 100% !important;
    }
    .mobile-social-tray a {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 56px !important;
        height: 56px !important;
        background: rgba(255,255,255,0.05) !important;
        border-radius: 50% !important;
        transition: all 0.3s ease !important;
    }
    .mobile-social-tray a svg {
        width: 24px !important;
        height: 24px !important;
        color: #fff !important;
    }
}
"""
if "MOBILE NAV HEADER & SOCIALS OVERRIDE" not in css_content:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(css_payload)
    print("CSS Payload Injected")

# 2. HTML Injection
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

# Replace the desktop-only btn
idx_content = idx_content.replace(
    '<a href="/contact.html" class="btn btn-dark desktop-only">Contact Us</a>',
    '<a href="/contact.html" class="btn btn-dark header-cta-mobile">Contact Us</a>'
)

# Replace the end of the ul element
socials_payload = """                <li><a href="/blog.html">Blog</a></li>
                <li class="mobile-social-tray mobile-only">
                    <a href="mailto:solutions@northeasttechworks.com" aria-label="Email Us">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    </a>
                    <a href="tel:2034181608" aria-label="Call Us">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                    </a>
                    <a href="https://linkedin.com/company/northeast-technical-works" target="_blank" aria-label="LinkedIn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                    </a>
                </li>
            </ul>"""

if "mobile-social-tray" not in idx_content:
    idx_content = idx_content.replace('<li><a href="/blog.html">Blog</a></li>\n            </ul>', socials_payload)
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("HTML Payload Injected to index.html")
