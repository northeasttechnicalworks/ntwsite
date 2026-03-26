# docs/performance-budgets.md

Performance goals
- LCP <= 2.5s (p75)
- CLS <= 0.1 (p75)
- INP <= 200ms (p75)

Budgets (guidance)
- CSS: <= 100KB compressed
- JS: <= 250KB compressed initial (defer the rest)
- Images: hero media <= 400KB (use modern formats)
- Fonts: 2 families max; subset; preload primary

Animation budgets
- Maintain 60fps when enabled
- Frame budget: aim < 16ms/frame on typical desktop
- Canvas:
  - cap node count
  - throttle mousemove
  - pause when tab hidden

Loading strategy
- Lazy load offscreen diagrams
- Inline critical CSS for above-fold
- Defer non-critical scripts

Mobile fallback
- Disable canvas hero under 768px if performance is poor
- Replace with static SVG topology + subtle gradient
