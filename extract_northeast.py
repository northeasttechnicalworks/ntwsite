import urllib.request
import xml.etree.ElementTree as ET

url = "https://upload.wikimedia.org/wikipedia/commons/1/1a/Blank_US_Map_%28states_only%29.svg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
svg_data = urllib.request.urlopen(req).read().decode('utf-8')

# The Wikipedia SVG has states with ID attributes like id="NY", id="NJ", etc.
# But sometimes they use names like id="New_York". Let's check.
import re

states = ['NY', 'NJ', 'CT', 'PA', 'MA', 'VT', 'NH', 'RI', 'DE', 'MD']
paths = []

for state in states:
    # Match <path ... id="NY" ... d="..." /> or similar
    match = re.search(r'<path[^>]*id="(' + state + r')"[^>]*d="([^"]+)"', svg_data)
    if not match:
        match = re.search(r'<path[^>]*d="([^"]+)"[^>]*id="(' + state + r')"', svg_data)
    
    if match:
        if '"' + state + '"' in match.group(0):
            d = match.group(2) if match.group(1) == state else match.group(1)
            paths.append((state, d))
    else:
        # Check inside groups or just any tag with id
        match = re.search(r'<path[^>]*id="[^"]*' + state + r'"[^>]*d="([^"]+)"', svg_data, re.IGNORECASE)
        if match:
             paths.append((state, match.group(1)))

print(paths)

# Let's extract exactly using ElementTree with namespaces
root = ET.fromstring(svg_data.replace('xmlns="http://www.w3.org/2000/svg"', ''))
res = {}
def extract(el):
    tag = el.tag.split('}')[-1]
    if tag in ['path', 'g'] and 'id' in el.attrib:
        ID = el.attrib['id']
        if ID in states:
            if tag == 'path':
                res[ID] = el.attrib['d']
            elif tag == 'g':
                # some states like HI, or small states are groups
                d = []
                for child in el:
                    if 'd' in child.attrib:
                        d.append(child.attrib['d'])
                res[ID] = " ".join(d)
    for child in el:
        extract(child)

extract(root)
print("EXTRACTED FROM ETREE:")
for k, v in res.items():
    print(k, ":", v[:50], "...")

