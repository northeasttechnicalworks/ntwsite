import os

base_dir = "e:/websites/NTW"
css_path = os.path.join(base_dir, "css", "styles.css")

css_payload = """
/* ------------------------------------- */
/* MOBILE UX REFINEMENTS (ROUND 2)       */
/* ------------------------------------- */
@media (max-width: 900px) {

    /* 1. Navbar & Fullscreen Menu Fix */
    .navbar {
        z-index: 1002 !important;
    }
    .nav-links {
        padding-top: 100px !important; /* Offset for the header */
        background: #020617 !important; /* Solid dark theme instead of glass */
        z-index: 1000 !important;
        justify-content: flex-start !important;
        gap: 24px !important;
    }
    body.menu-open .navbar {
        background: #020617 !important;
        border-bottom-color: rgba(255,255,255,0.05) !important;
    }
    body.menu-open .brand-logo {
        color: #fff !important;
    }
    .nav-links li a {
        font-size: 24px !important; /* Reduce from 32px to 24px for cleaner look */
        width: 100%;
        text-align: center;
    }

    /* 2. Trust Strip (Partner bar) Fix */
    .partner-strip .container {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 20px !important;
    }
    .partner-strip .container > div {
        row-gap: 12px !important;
        column-gap: 16px !important;
        justify-content: flex-start !important;
    }

    /* 3. Footer Fix */
    .footer {
        padding: 60px 0 40px !important;
    }
    .footer-top {
        gap: 32px !important;
        margin-bottom: 40px !important;
    }
    .footer-top h4 {
        margin-bottom: 16px !important;
    }
    .footer-top > div {
        margin-bottom: 8px !important;
    }
    
    /* Extra: Reduce oversized H1s even more */
    .hero h1 { font-size: 36px !important; }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(css_payload)

print("CSS UX enhancements applied globally.")
