import re, os
idx_content = open("e:/websites/NTW/index.html", "r", encoding="utf-8").read()
nav_match = re.search(r'(<div class="top-bar">.*?</header>)', idx_content, re.DOTALL)
print("Nav length:", len(nav_match.group(1)) if nav_match else "NONE")
ft_match = re.search(r'(<footer class="footer".*?</footer>)', idx_content, re.DOTALL)
print("Footer length:", len(ft_match.group(1)) if ft_match else "NONE")
