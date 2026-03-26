/**
 * map.js - NTW Premium Interactive Map Engine
 */

document.addEventListener('DOMContentLoaded', () => {
    initMapInteractions();
});

function initMapInteractions() {
    const mapContainer = document.querySelector('.map-container');
    if (!mapContainer) return;

    // Create Tooltip Element
    let tooltip = document.getElementById('map-tooltip');
    if (!tooltip) {
        tooltip = document.createElement('div');
        tooltip.id = 'map-tooltip';
        tooltip.className = 'map-tooltip';
        document.body.appendChild(tooltip);
    }

    const coreNodes = document.querySelectorAll('.corridor-node');
    
    coreNodes.forEach(node => {
        node.addEventListener('mouseenter', (e) => {
            const name = node.getAttribute('data-name');
            const type = node.getAttribute('data-type');
            const sub = node.getAttribute('data-sub');
            const isPrimary = type === 'primary';
            
            const cssClass = isPrimary ? 'tooltip-primary' : 'tooltip-secondary';
            
            tooltip.className = `map-tooltip is-visible ${cssClass}`;
            tooltip.innerHTML = `
                <div class="map-tooltip-header">${name}</div>
                <div class="map-tooltip-body">${sub}</div>
            `;
        });
        
        node.addEventListener('mousemove', (e) => {
            let x = e.clientX;
            let y = e.clientY;
            
            // Boundary detection logic to prevent clipping off-screen
            const rect = tooltip.getBoundingClientRect();
            
            // Horizontal boundaries
            if (x - rect.width / 2 < 10) {
                x = rect.width / 2 + 10;
            } else if (x + rect.width / 2 > window.innerWidth - 10) {
                x = window.innerWidth - rect.width / 2 - 10;
            }
            
            // Vertical boundaries (Cursor height approx 20px)
            if (y - rect.height - 15 < 10) {
                y = y + rect.height + 25; // Flip below cursor if hitting top
                tooltip.style.marginTop = '15px';
            } else {
                tooltip.style.marginTop = '-15px'; // Standard above cursor
            }
            
            tooltip.style.left = `${x}px`;
            tooltip.style.top = `${y}px`;
        });
        
        node.addEventListener('mouseleave', () => {
            tooltip.classList.remove('is-visible');
        });
    });
}
