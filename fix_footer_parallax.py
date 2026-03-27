import os

base_dir = "e:/websites/NTW"
css_path = os.path.join(base_dir, "css", "styles.css")

footer_css = """
/* Footer Parallax Physics Overlay */
.footer {
    position: relative;
    z-index: 100;
    background: #070D1E;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(footer_css)

print("Footer CSS injected.")
