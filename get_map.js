const https = require('https');

https.get('https://raw.githubusercontent.com/NewSignature/us-map/master/public/js/us-map.js', (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
        const ny = data.match(/NY:\s*\{\s*name:\s*'New York',\s*path:\s*'([^']+)'/);
        const nj = data.match(/NJ:\s*\{\s*name:\s*'New Jersey',\s*path:\s*'([^']+)'/);
        const ct = data.match(/CT:\s*\{\s*name:\s*'Connecticut',\s*path:\s*'([^']+)'/);
        const pa = data.match(/PA:\s*\{\s*name:\s*'Pennsylvania',\s*path:\s*'([^']+)'/);
        const ma = data.match(/MA:\s*\{\s*name:\s*'Massachusetts',\s*path:\s*'([^']+)'/);
        
        console.log("NY:", ny ? ny[1] : 'not found');
        console.log("NJ:", nj ? nj[1] : 'not found');
        console.log("CT:", ct ? ct[1] : 'not found');
        console.log("PA:", pa ? pa[1] : 'not found');
        console.log("MA:", ma ? ma[1] : 'not found');
    });
});
