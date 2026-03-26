# docs/motion-system.md

Motion intent: Infrastructure activity (signals, connections, systems waking up).
Luxury rule: Motion must feel deliberate, not playful.

Global motion rules
- No bounce easing.
- No rapid looping background unless extremely subtle.
- Motion must be disabled or reduced when prefers-reduced-motion is enabled.

Timing + easing
- Micro interactions: 120–200ms, --ease-out
- Standard UI: 200–320ms, --ease-standard
- Section reveals: 520–900ms, --ease-standard
- Background ambience: 9–18s loops, linear or subtle ease

Reduced motion
- If prefers-reduced-motion: reduce:
  - disable parallax
  - disable continuous canvas drift
  - keep only opacity fades <= 200ms
  - replace signal pulses with static highlights

HeroTopology animation spec (canvas)
- Node count: 40–80 desktop; 20–40 tablet; 0–20 mobile (or disabled)
- Frame budget: target < 16ms/frame on desktop
- Signals: pulse travels along edges every 3–6 seconds
- Interaction: mouse movement shifts layers up to 8–12px
- Visual: thin lines, subtle glow, no neon
- Fallback: static SVG topology image if canvas fails or mobile low-power

Scroll reveal system
- Reveal direction: fade + slight translate (8–16px)
- Stagger: 60–120ms between elements
- Avoid heavy transforms on large images to prevent jank

Hover interactions
- Cards rise 6–10px with shadow + glow border
- Icons: stroke draw or subtle rotate <= 6 degrees
- Buttons: subtle highlight sweep or glow

CoverageMap motion
- On section entry: primary states pulse once (not loop)
- Hover: border brighten + tooltip fade in 120–200ms
- Selection: state fill transitions 320ms

Timeline motion
- Progress line grows based on scroll position
- Each step activates once; do not replay repeatedly

Animation implementation hints
- Use requestAnimationFrame for canvas
- Use IntersectionObserver for scroll triggers
- Respect prefers-reduced-motion media query in CSS and JS
