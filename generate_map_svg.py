import urllib.request
import json

url = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req).read().decode('utf-8')
data = json.loads(response)

# The states we want
targets = {'New York': 'ny', 'New Jersey': 'nj', 'Connecticut': 'ct', 'Pennsylvania': 'pa', 'Massachusetts': 'ma', 'Rhode Island': 'ri', 'Delaware': 'de', 'Maryland': 'md', 'New Hampshire': 'nh', 'Vermont': 'vt'}

primary = ['ny', 'nj', 'ct']

# Collect coordinates
target_features = []
for f in data['features']:
    if f['properties']['name'] in targets:
        target_features.append((targets[f['properties']['name']], f))

# Find bounding box
min_x, max_x = float('inf'), float('-inf')
min_y, max_y = float('inf'), float('-inf')

def update_bounds(coords):
    global min_x, max_x, min_y, max_y
    # GeoJSON coords can be deep
    if isinstance(coords[0], (int, float)):
        x, y = coords[0], coords[1]
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    else:
        for c in coords:
            update_bounds(c)

for _, f in target_features:
    update_bounds(f['geometry']['coordinates'])

# We want to map to a 500x500 svg, with some padding (e.g. 20px)
width, height = 500.0, 500.0
pad = 20.0

# Calculate scale
scale_x = (width - 2 * pad) / (max_x - min_x)
scale_y = (height - 2 * pad) / (max_y - min_y)
scale = min(scale_x, scale_y)

# Mercator approximation for the latitude scaling
import math
import sys

def project(lon, lat):
    # simple equirectangular with aspect ratio correction for approx 41 degrees north
    lat_rad = lat * math.pi / 180.0
    # better to just do simple linear since bounding box is small
    cx = min_x + (max_x - min_x) / 2
    cy = min_y + (max_y - min_y) / 2
    
    # Just linear transform based on bounds, flip Y because SVG y goes down
    x = pad + (lon - min_x) * scale
    y = pad + (max_y - lat) * scale
    return x, y

# Generate paths
paths = []

for state_id, f in target_features:
    geom_type = f['geometry']['type']
    coords = f['geometry']['coordinates']
    
    d = []
    
    def process_polygon(ring):
        res = []
        for i, pt in enumerate(ring):
            x, y = project(pt[0], pt[1])
            if i == 0:
                res.append(f"M {x:.2f},{y:.2f}")
            else:
                res.append(f"L {x:.2f},{y:.2f}")
        res.append("Z")
        return " ".join(res)
        
    if geom_type == 'Polygon':
        for ring in coords:
             d.append(process_polygon(ring))
    elif geom_type == 'MultiPolygon':
        for poly in coords:
            for ring in poly:
                d.append(process_polygon(ring))
                
    path_d = " ".join(d)
    css_class = "map-state primary" if state_id in primary else "map-state secondary"
    state_html = f'<path class="{css_class}" id="{state_id}" d="{path_d}" />'
    paths.append(state_html)

with open('e:/websites/NTW/map_utf8.html', 'w', encoding='utf-8') as f:
    for p in paths:
        f.write(p + "\n")
