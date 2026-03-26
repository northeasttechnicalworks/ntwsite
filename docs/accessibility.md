# docs/accessibility.md

Target: WCAG 2.2 AA conformance.

Requirements
- Semantic landmarks: header/nav/main/footer
- Single H1 per page
- All interactive elements keyboard reachable
- Visible focus state (must be obvious on dark backgrounds)
- Contrast: meet AA for text and UI controls
- Tooltips accessible: aria-live or aria-describedby
- Skip-to-content link required

Reduced motion
- Respect prefers-reduced-motion:
  - disable continuous background animation
  - no parallax
  - keep essential state changes

Forms
- Labels must be explicit
- Error messages in text (not color only)
- Inputs have focus styling

Coverage map
- Each state is a focusable element
- Provide list-view fallback on mobile
