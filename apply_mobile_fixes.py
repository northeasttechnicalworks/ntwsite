import os

base_dir = "e:/websites/NTW"

# 1. Update css/styles.css
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

mobile_css = """
/* ------------------------------------- */
/* GLOBAL MOBILE FLUIDITY OVERRIDES      */
/* ------------------------------------- */
.mobile-menu-btn {
  display: none;
  background: transparent;
  border: none;
  color: var(--c-text-main);
  cursor: pointer;
  z-index: 1001;
  position: relative;
}

@media (max-width: 900px) {
  /* Typography Scaling */
  .hero h1 { font-size: 42px !important; line-height: 1.15; margin-bottom: 16px; }
  .hero p { font-size: 16px !important; margin-bottom: 24px; }
  h1 { font-size: 40px !important; }
  h2 { font-size: 32px !important; line-height: 1.25; margin-bottom: 16px !important; }
  h3 { font-size: 24px !important; margin-bottom: 12px !important; }
  p { font-size: 16px !important; }

  /* Spacing Reductions */
  .section, .section-sm { padding: 64px 0 !important; }
  .hero { min-height: auto !important; padding: 120px 0 60px 0 !important; }

  /* Top Bar Reshaping */
  .top-bar .flex-between { flex-direction: column; align-items: flex-start; gap: 12px; }
  .top-contact { flex-direction: column; gap: 8px; }

  /* Mobile Navbar Overlay */
  .mobile-menu-btn.mobile-only {
      display: flex !important;
  }
  .nav-links {
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100vh;
      background: rgba(7, 13, 30, 0.98);
      backdrop-filter: blur(10px);
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 32px;
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s ease;
      z-index: 1000;
  }
  .nav-links.active {
      opacity: 1;
      pointer-events: auto;
  }
  .nav-links li a {
      font-family: var(--font-heading);
      font-size: 32px;
      color: var(--c-white) !important;
      text-transform: none;
  }
  .nav-links li a:hover {
      color: var(--c-accent) !important;
  }
  body.menu-open {
      overflow: hidden;
  }
}
"""

if "GLOBAL MOBILE FLUIDITY OVERRIDES" not in css_content:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(mobile_css)

# 2. Update js/main.js
js_path = os.path.join(base_dir, "js", "main.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

mobile_js = """
    // Mobile Menu Toggle
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            menuBtn.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
        
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                menuBtn.classList.remove('active');
                document.body.classList.remove('menu-open');
            });
        });
    }
"""

if "Mobile Menu Toggle" not in js_content:
    js_content = js_content.replace(
        "initTimelinePhysics();\n});",
        "initTimelinePhysics();\n" + mobile_js + "});"
    )
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)


# 3. Update refactor_industries.py grids
ind_path = os.path.join(base_dir, "refactor_industries.py")
with open(ind_path, "r", encoding="utf-8") as f:
    ind_content = f.read()

ind_content = ind_content.replace('style="display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-bottom:24px;"', 'class="grid grid-2" style="margin-bottom:24px; align-items:start;"')

with open(ind_path, "w", encoding="utf-8") as f:
    f.write(ind_content)

print("Applied CSS, JS, and Python code patches!")
