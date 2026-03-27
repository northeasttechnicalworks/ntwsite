const fs = require('fs');
const path = require('path');

const rootDir = 'e:/websites/NTW';

const navBlockRoot = `    <header class="navbar">
        <div class="container nav-container">
            <a href="index.html" class="brand-logo"><span style="font-family: var(--font-family-heading); font-weight: 800; color: #fff; font-size: 1.25rem;">NTW</span></a>
            
            <nav class="nav-links desktop-only" aria-label="Main Navigation">
                <a href="/services.html">Services</a>
                <a href="/industries.html">Industries</a>
                <a href="/coverage.html">Coverage</a>
                <a href="/integrators.html">Integrators</a>
                <a href="/about.html">About</a>
                <a href="/blog.html">Blog</a>
                <a href="/contact.html">Contact</a>
                <a href="#" style="opacity: 0.5; border-left: 1px solid var(--c-border-0); padding-left: var(--s-4); cursor: not-allowed; display:flex; align-items:center; gap: 6px;">
                    Portal <span style="font-size: 10px; background: var(--c-surface-1); padding: 2px 6px; border-radius: 4px; color: var(--c-accent-1); border: 1px solid var(--c-border-1);">Soon</span>
                </a>
            </nav>
            
            <div class="nav-actions desktop-only" style="display: flex; gap: var(--s-2);">
                <a href="/contact.html?intent=coverage" class="btn btn-secondary">Request Coverage</a>
                <a href="/contact.html?intent=service" class="btn btn-primary">Request Service</a>
            </div>
            
            <button class="mobile-menu-toggle mobile-only" aria-label="Toggle menu">☰</button>
        </div>
    </header>`;

const footerBlockRoot = `    <footer class="footer" style="background: #020617; padding: 100px 0 40px; border-top: 1px solid #1e293b;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 64px; margin-bottom: 80px;">
                <div style="grid-column: 1 / -1; max-width: 400px; @media(min-width:1024px){grid-column: span 2;}">
                    <span style="font-family: var(--font-heading); font-weight: 800; color: #fff; font-size: 28px; display: block; margin-bottom: 16px; letter-spacing: -1px;">NTW</span>
                    <p style="font-size: 16px; color: #94a3b8; line-height: 1.7; margin-bottom: 32px;">The Northeast corridor's most disciplined infrastructure deployment team. Delivering inspection-ready execution across NY, NJ, and CT.</p>
                    <div>
                        <strong style="color: #fff; display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;">Dispatch Line</strong>
                        <a href="tel:2034181608" style="color: #fff; font-size: 20px; font-weight: 600; text-decoration: none; display: block; margin-bottom: 4px; transition: color 0.2s;" onmouseover="this.style.color='var(--c-accent)'" onmouseout="this.style.color='#fff'">(203) 418-1608</a>
                        <a href="mailto:solutions@northeasttechworks.com" style="color: var(--c-accent); font-size: 16px; text-decoration: none; transition: opacity 0.2s;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">solutions@northeasttechworks.com</a>
                    </div>
                </div>
                
                <div>
                    <h4 style="color: #fff; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px;">Core Capabilities</h4>
                    <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 16px; margin: 0;">
                        <li><a href="/services/structured-cabling.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Structured Cabling</a></li>
                        <li><a href="/services/network-rack-buildouts.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Network Racks</a></li>
                        <li><a href="/services/video-surveillance-installation.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Video Surveillance</a></li>
                        <li><a href="/services/access-control-installation.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Access Control</a></li>
                        <li><a href="/services.html" style="color: var(--c-accent); text-decoration: none; font-size: 15px; transition: opacity 0.2s;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">View All Services &rarr;</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 style="color: #fff; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px;">Operations</h4>
                    <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 16px; margin: 0;">
                        <li><a href="/industries.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Retail Data Rollouts</a></li>
                        <li><a href="/industries.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Enterprise IT Space</a></li>
                        <li><a href="/industries.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Commercial Real Estate</a></li>
                        <li><a href="/coverage.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Coverage Map</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 style="color: #fff; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px;">Corporate</h4>
                    <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 16px; margin: 0;">
                        <li><a href="/about.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Framework & Manifesto</a></li>
                        <li><a href="/integrators.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">National Integrator Program</a></li>
                        <li><a href="/contact.html" style="color: #94a3b8; text-decoration: none; font-size: 15px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Contact Dispatch</a></li>
                    </ul>
                </div>
            </div>
            
            <div style="border-top: 1px solid #1e293b; padding-top: 32px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 24px;">
                <div style="color: #64748b; font-size: 14px;">&copy; 2026 Northeast Technical Works (NTW). All rights reserved.</div>
                <div style="display: flex; gap: 32px;">
                    <a href="/privacy-policy.html" style="color: #64748b; text-decoration: none; font-size: 14px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#64748b'">Privacy</a>
                    <a href="/terms-of-service.html" style="color: #64748b; text-decoration: none; font-size: 14px; transition: color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#64748b'">Terms</a>
                </div>
            </div>
        </div>
    </footer>`;

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;
    
    // Replace NavBar
    const navRegex = /<header class="navbar">[\s\S]*?<\/header>/;
    if (navRegex.test(content)) {
        content = content.replace(navRegex, navBlockRoot);
        modified = true;
    }
    
    // Replace Footer
    const footerRegex = /<footer class="footer">[\s\S]*?<\/footer>/;
    if (footerRegex.test(content)) {
        content = content.replace(footerRegex, footerBlockRoot);
        modified = true;
    } else {
        // Footer is completely missing. Insert it before the main.js script tag or before </body>
        if (content.includes('<script src="js/main.js"')) {
            content = content.replace(/(<script src="js\/main\.js")/, footerBlockRoot + '\n    $1');
        } else {
            content = content.replace(/(<\/body>)/, footerBlockRoot + '\n$1');
        }
        modified = true;
    }
    
    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('Updated ' + filePath);
    }
}

function processDirectory(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            if (file === 'services') processDirectory(fullPath);
        } else if (fullPath.endsWith('.html')) {
            processFile(fullPath);
        }
    }
}

processDirectory(rootDir);
