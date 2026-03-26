const fs = require('fs');
const https = require('https');
const d3 = require('d3-geo');

const GEOJSON_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json';

const STATE_FIPS = {
    '09': 'CT', '10': 'DE', '24': 'MD', '25': 'MA', '33': 'NH',
    '34': 'NJ', '36': 'NY', '42': 'PA', '44': 'RI', '50': 'VT'
};

const PRIMARY_COUNTIES = {
    // NY: NYC + Long Island + Westchester
    '36005': true, // Bronx
    '36047': true, // Kings (Brooklyn)
    '36061': true, // New York (Manhattan)
    '36081': true, // Queens
    '36085': true, // Richmond (Staten Island)
    '36059': true, // Nassau
    '36103': true, // Suffolk
    '36119': true, // Westchester
    
    // CT: All
    '09001': true, '09003': true, '09005': true, '09007': true,
    '09009': true, '09011': true, '09013': true, '09015': true,

    // NJ: Neighboring NYC/CT (Bergen, Hudson, Passaic, Essex)
    '34003': true, // Bergen
    '34017': true, // Hudson
    '34031': true, // Passaic
    '34013': true, // Essex
    '34039': true, // Union (often grouped with Essex/Hudson)
    
    // RI: Neighboring CT
    '44009': true, // Washington
    '44003': true, // Kent
    '44007': true, // Providence
    
    // MA: Neighboring CT
    '25003': true, // Berkshire
    '25013': true, // Hampden
    '25027': true, // Worcester
};

https.get(GEOJSON_URL, { headers: { 'User-Agent': 'Node' } }, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
        const geojson = JSON.parse(data);
        
        // Filter features
        const neFeatures = geojson.features.filter(f => {
            const stateFips = f.id.substring(0, 2);
            return !!STATE_FIPS[stateFips];
        });

        // Setup D3 Projection
        const projection = d3.geoAlbers()
            .rotate([74, 0])
            .center([0, 41.5]) // Center on NY/CT border
            .scale(4500) // Zoom level
            .translate([300, 300]); // 600x600 viewBox center

        const pathGenerator = d3.geoPath().projection(projection);

        let svgHtml = '<svg viewBox="0 0 600 600" width="100%" height="100%" class="deployment-map">\n';
        svgHtml += '<g class="states-group">\n';

        // Group by state so we can add hover effects easily at the state level if needed
        const statesMap = {};
        for(const feat of neFeatures) {
            const stateCode = STATE_FIPS[feat.id.substring(0, 2)];
            if (!statesMap[stateCode]) statesMap[stateCode] = [];
            statesMap[stateCode].push(feat);
        }

        for (const stateCode in statesMap) {
            svgHtml += `  <g id="state-${stateCode}" class="state-group">\n`;
            for (const f of statesMap[stateCode]) {
                const isPrimary = PRIMARY_COUNTIES[f.id] ? 'county-primary' : 'county-secondary';
                const d = pathGenerator(f);
                if (d) {
                    svgHtml += `    <path class="county ${isPrimary}" id="fips-${f.id}" d="${d}" data-name="${f.properties.NAME}" />\n`;
                }
            }
            svgHtml += `  </g>\n`;
        }

        svgHtml += '</g>\n</svg>';
        
        fs.writeFileSync('../map_counties.html', svgHtml, 'utf8');
        console.log("Map generated at map_counties.html");
    });
}).on('error', err => {
    console.error("Failed to download GeoJSON:", err);
});
