/**
 * main.js - NTW Interactivity & Motion Engine
 */

document.addEventListener('DOMContentLoaded', () => {
    initMotionObserver();
    initHeroTopology();
    initTimelinePhysics();
});

function isReducedMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

/**
 * Scroll Reveal System
 * Fades and translates elements as they enter the viewport
 */
function initMotionObserver() {
    if (isReducedMotion()) {
        document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-revealed'));
        return;
    }

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -10% 0px',
        threshold: 0.1
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-revealed');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => {
        revealObserver.observe(el);
    });
}

/**
 * HeroTopology Canvas Engine
 * Renders technical nodes and connections
 */
function initHeroTopology() {
    const canvas = document.getElementById('hero-canvas');
    if (!canvas) return;

    if (isReducedMotion() || window.innerWidth < 768) {
        // Fallback applied via CSS, stop script execution
        return;
    }

    const ctx = canvas.getContext('2d');
    let width, height;
    let nodes = [];
    let mouse = { x: -1000, y: -1000 };

    function resize() {
        // Pixel ratio setup for sharp lines
        const dpr = window.devicePixelRatio || 1;
        width = canvas.parentElement.offsetWidth;
        height = canvas.parentElement.offsetHeight;
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        ctx.scale(dpr, dpr);
        canvas.style.width = width + 'px';
        canvas.style.height = height + 'px';
        initNodes();
    }

    window.addEventListener('resize', resize);
    
    canvas.parentElement.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
    });
    
    canvas.parentElement.addEventListener('mouseleave', () => {
        mouse.x = -1000;
        mouse.y = -1000;
    });

    function initNodes() {
        nodes = [];
        const nodeCount = Math.min(Math.floor((width * height) / 15000), 60); // Max 60 nodes
        for (let i = 0; i < nodeCount; i++) {
            nodes.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.3,
                vy: (Math.random() - 0.5) * 0.3,
                radius: Math.random() * 1.5 + 1.5
            });
        }
    }

    function draw() {
        ctx.clearRect(0, 0, width, height);

        nodes.forEach(node => {
            // Mouse repel
            const dx = mouse.x - node.x;
            const dy = mouse.y - node.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            
            if (dist < 150) {
                const force = (150 - dist) / 150;
                node.x -= (dx / dist) * force * 2;
                node.y -= (dy / dist) * force * 2;
            }

            // Drift
            node.x += node.vx;
            node.y += node.vy;

            // Bounds bounce
            if (node.x <= 0 || node.x >= width) node.vx *= -1;
            if (node.y <= 0 || node.y >= height) node.vy *= -1;

            // Draw Node
            ctx.beginPath();
            ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(230, 233, 238, 0.72)'; // var(--c-text-1) approx
            ctx.fill();
        });

        // Draw Edges
        ctx.lineWidth = 1;
        for (let i = 0; i < nodes.length; i++) {
            for (let j = i + 1; j < nodes.length; j++) {
                const nx = nodes[i].x - nodes[j].x;
                const ny = nodes[i].y - nodes[j].y;
                const distLine = Math.sqrt(nx * nx + ny * ny);

                if (distLine < 120) {
                    ctx.beginPath();
                    ctx.moveTo(nodes[i].x, nodes[i].y);
                    ctx.lineTo(nodes[j].x, nodes[j].y);
                    // Fade out based on distance
                    ctx.strokeStyle = `rgba(191, 197, 206, ${0.15 * (1 - distLine/120)})`;
                    ctx.stroke();
                }
            }
        }

        requestAnimationFrame(draw);
    }

    resize();
    draw();
}

/**
 * Timeline Scroll Physics
 * Activates nodes and fills progress bar
 */
function initTimelinePhysics() {
    const tracker = document.getElementById('timeline-tracker');
    const fill = document.getElementById('timeline-fill');
    const steps = document.querySelectorAll('.timeline-step');
    
    if (!tracker || !fill || steps.length === 0) return;

    window.addEventListener('scroll', () => {
        const rect = tracker.getBoundingClientRect();
        const windowHeight = window.innerHeight;
        
        // Calculate how much of the tracker has been scrolled past
        let progress = 0;
        if (rect.top > windowHeight / 2) {
            progress = 0;
        } else if (rect.bottom < windowHeight / 2) {
            progress = 100;
        } else {
            const distance = (windowHeight / 2) - rect.top;
            progress = (distance / rect.height) * 100;
        }
        
        fill.style.height = `${Math.min(Math.max(progress, 0), 100)}%`;
        
        // Activate steps based on line intersection
        steps.forEach(step => {
            const stepRect = step.getBoundingClientRect();
            // If the midpoint of viewport is past the specific step marker
            if (stepRect.top < windowHeight / 2 + 20) {
                step.classList.add('is-active');
            } else {
                step.classList.remove('is-active');
            }
        });
    });
}
