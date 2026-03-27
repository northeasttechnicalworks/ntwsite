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

const footerBlockRoot = `    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col" style="flex: 2;">
                    <span style="font-family: var(--font-family-heading); font-weight: 800; color: #fff; font-size: 1.5rem; display:block; margin-bottom:var(--s-4);">Northeast Technical Works</span>
                    <p style="font-size: var(--fs-1); margin-bottom: var(--s-4); max-width: 300px; color: var(--c-text-1);">The Northeast corridor's most disciplined infrastructure deployment team. Delivering inspection-ready execution across NY, NJ, and CT.</p>
                    <div style="margin-bottom: var(--s-4);">
                        <strong style="color: #fff; display: block; margin-bottom: var(--s-1);">Contact Dispatch</strong>
                        <a href="tel:2034181608" style="color: var(--c-accent-1); display: block;">(203) 418-1608</a>
                        <a href="mailto:solutions@northeasttechworks.com" style="color: var(--c-accent-1); display: block;">solutions@northeasttechworks.com</a>
                    </div>
                </div>
                <div class="footer-col">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="/services/structured-cabling.html">Structured Cabling</a></li>
                        <li><a href="/services/network-rack-buildouts.html">Network Racks</a></li>
                        <li><a href="/services/video-surveillance-installation.html">Video Surveillance</a></li>
                        <li><a href="/services/access-control-installation.html">Access Control</a></li>
                        <li><a href="/services.html">View All Services</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Industries & Coverage</h4>
                    <ul>
                        <li><a href="/industries.html">Retail Rollouts</a></li>
                        <li><a href="/industries.html">Enterprise IT</a></li>
                        <li><a href="/industries.html">Commercial Real Estate</a></li>
                        <li><a href="/coverage.html#ny">New York (Primary)</a></li>
                        <li><a href="/coverage.html#nj">New Jersey (Primary)</a></li>
                        <li><a href="/coverage.html#ct">Connecticut (Primary)</a></li>
                        <li><a href="/coverage.html">Full Coverage Map</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="/about.html">About & Manifesto</a></li>
                        <li><a href="/integrators.html">For Integrators</a></li>
                        <li><a href="/contact.html">Contact Us</a></li>
                        <li><a href="#" style="color: var(--c-accent-1);">Download Capability Statement</a></li>
                    </ul>
                    <div style="margin-top: var(--s-4); display: flex; gap: var(--s-2);">
                        <!-- LinkedIn -->
                        <a href="#" aria-label="LinkedIn" style="color: var(--c-text-1);"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
                        <!-- Twitter -->
                        <a href="#" aria-label="Twitter" style="color: var(--c-text-1);"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
                        <!-- YouTube -->
                        <a href="#" aria-label="YouTube" style="color: var(--c-text-1);"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom" style="margin-top: var(--s-6); border-top: 1px solid var(--c-border-0); padding-top: var(--s-6); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: var(--s-4);">
                 <div style="color: var(--c-text-2); font-size: var(--fs-1);">&copy; 2026 Northeast Technical Works (NTW). All rights reserved.</div>
                 <div style="display:flex; gap:var(--s-4); font-size: var(--fs-1);">
                     <a href="/privacy-policy.html">Privacy Policy</a>
                     <a href="/terms-of-service.html">Terms of Service</a>
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
