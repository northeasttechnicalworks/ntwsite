/**
 * main.js - NTW Interactivity & Motion Engine
 */

document.addEventListener('DOMContentLoaded', () => {
    initMotionObserver();
    initHeroTopology();
    initTimelinePhysics();
    initForms();

    // Mobile Menu Toggle
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            menuBtn.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
        
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                menuBtn.classList.remove('active');
                document.body.classList.remove('menu-open');
            });
        });
    }
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

/**
 * Global Form Handler
 * Intercepts FormSubmit requests to send via AJAX and display in-place acknowledgement.
 */
function initForms() {
    const forms = document.querySelectorAll('form[action*="formsubmit.co"]');
    forms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn ? submitBtn.innerText : 'Submit';
            if (submitBtn) {
                submitBtn.innerText = 'Transmitting...';
                submitBtn.disabled = true;
                submitBtn.style.opacity = '0.7';
                submitBtn.style.cursor = 'not-allowed';
            }

            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());
            
            // Appending FormSubmit configuration fields silently
            data['_captcha'] = 'false';
            data['_template'] = 'table';
            data['_subject'] = 'Deployment Initiation | NTW Website';

            let actionUrl = form.action;
            if (!actionUrl.includes('/ajax/')) {
                actionUrl = actionUrl.replace('formsubmit.co/', 'formsubmit.co/ajax/');
            }

            try {
                const response = await fetch(actionUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                if (response.ok) {
                    const isDarkTheme = form.closest('.theme-dark') !== null || !!form.closest('[style*="background: #0f172a"]');
                    const textColor = isDarkTheme ? '#ffffff' : '#0f172a';
                    const pColor = isDarkTheme ? '#94a3b8' : '#475569';
                    
                    const successMsg = document.createElement('div');
                    successMsg.style.textAlign = 'center';
                    successMsg.style.padding = '40px 20px';
                    successMsg.style.animation = 'fadeIn 0.5s ease forwards';
                    
                    if (!document.getElementById('ntw-form-styles')) {
                        const style = document.createElement('style');
                        style.id = 'ntw-form-styles';
                        style.textContent = '@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }';
                        document.head.appendChild(style);
                    }

                    successMsg.innerHTML = `
                        <div style="width: 64px; height: 64px; background: rgba(16, 185, 129, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; border: 1px solid rgba(16, 185, 129, 0.2);">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                                <polyline points="22 4 12 14.01 9 11.01"></polyline>
                            </svg>
                        </div>
                        <h3 style="font-family: var(--font-heading, sans-serif); font-size: 28px; margin-bottom: 12px; color: ${textColor}; letter-spacing: -0.5px;">Transmission Successful</h3>
                        <p style="font-size: 16px; line-height: 1.6; color: ${pColor}; max-width: 400px; margin: 0 auto;">Your deployment requirements have been securely logged. An execution specialist will review your specifications and contact you shortly.</p>
                    `;
                    
                    form.replaceWith(successMsg);
                } else {
                    throw new Error('Server returned ' + response.status);
                }
            } catch (err) {
                console.error('Form submission error:', err);
                alert('We encountered a temporary network issue. Please call us at (203) 418-1608 or email solutions@northeasttechworks.com directly.');
                if (submitBtn) {
                    submitBtn.innerText = originalBtnText;
                    submitBtn.disabled = false;
                    submitBtn.style.opacity = '1';
                    submitBtn.style.cursor = 'pointer';
                }
            }
        });
    });
}
