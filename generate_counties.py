import urllib.request
import json
import math

url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req).read().decode('utf-8')
data = json.loads(response)

STATE_FIPS = {
    '09': 'CT', '10': 'DE', '24': 'MD', '25': 'MA', '33': 'NH',
    '34': 'NJ', '36': 'NY', '42': 'PA', '44': 'RI', '50': 'VT'
}

PRIMARY = {
    '36005', '36047', '36061', '36081', '36085', '36059', '36103', '36119', # NY: NYC, Long Island, Westchester
    '09001', '09003', '09005', '09007', '09009', '09011', '09013', '09015', # CT: Entire state
    '34003', '34013', '34017', '34019', '34023', '34025', '34027', '34031', '34035', '34037', '34039', '34041', # NJ: Northern/NYC Metro
}

features = []
for f in data['features']:
    if f['id'][:2] in STATE_FIPS:
        features.append(f)

# Find Bounding Box
min_x, max_x = float('inf'), float('-inf')
min_y, max_y = float('inf'), float('-inf')

def update_bounds(coords):
    global min_x, max_x, min_y, max_y
    if isinstance(coords[0], (int, float)):
        min_x = min(min_x, coords[0])
        max_x = max(max_x, coords[0])
        min_y = min(min_y, coords[1])
        max_y = max(max_y, coords[1])
    else:
        for c in coords:
            update_bounds(c)

for f in features:
    update_bounds(f['geometry']['coordinates'])

width, height = 600.0, 600.0
pad = 10.0
scale_x = (width - 2 * pad) / (max_x - min_x)
scale_y = (height - 2 * pad) / (max_y - min_y)
scale = min(scale_x, scale_y)

def project(lon, lat):
    x = pad + (lon - min_x) * scale
    y = pad + (max_y - lat) * scale
    return x, y

paths_by_state = {}
for f in features:
    geom_type = f['geometry']['type']
    coords = f['geometry']['coordinates']
    d = []
    
    def process_polygon(ring):
        res = []
        for i, pt in enumerate(ring):
            x, y = project(pt[0], pt[1])
            res.append(f"{'M' if i==0 else 'L'} {x:.2f},{y:.2f}")
        res.append("Z")
        return " ".join(res)
        
    if geom_type == 'Polygon':
        for ring in coords: d.append(process_polygon(ring))
    elif geom_type == 'MultiPolygon':
        for poly in coords:
            for ring in poly: d.append(process_polygon(ring))
                
    path_d = " ".join(d)
    is_primary = "county-primary" if f['id'] in PRIMARY else "county-secondary"
    state_code = STATE_FIPS[f['id'][:2]]
    name = f['properties']['NAME'].replace('"', "'")
    
    if state_code not in paths_by_state:
        paths_by_state[state_code] = []
        
    paths_by_state[state_code].append(f'<path class="map-county {is_primary}" data-name="{name}" d="{path_d}" />')

with open('e:/websites/NTW/map_counties.html', 'w', encoding='utf-8') as f:
    f.write('<svg viewBox="0 0 600 600" width="100%" height="100%" class="deployment-map">\n')
    for state, county_paths in paths_by_state.items():
        f.write(f'  <g class="map-state-group" data-state="{state}">\n')
        for p in county_paths:
            f.write(f"    {p}\n")
        f.write('  </g>\n')
    f.write('</svg>\n')
