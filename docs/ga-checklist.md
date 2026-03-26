# docs/qa-checklist.md

QA gates (must pass)

Visual design
- No placeholder blocks
- Consistent spacing rhythm
- Typography hierarchy matches design-system
- Luxury material layers present (noise, grid, depth)

Motion
- Motion is subtle and not distracting
- Reduced motion works (prefers-reduced-motion)
- No jank on scroll; animations smooth

Performance
- LCP/CLS/INP targets met or close
- JS bundle within budget
- Canvas does not spike CPU on idle
- Lazy loading works

Accessibility
- Keyboard navigation works everywhere
- Focus states visible
- Map accessible (keyboard + list fallback)
- Forms labeled with errors readable
- Color contrast AA

SEO
- Unique meta title/desc per page
- Schema JSON-LD included where required
- Sitemap and internal linking in place
- Clean headings (one H1)

Forms & conversion
- CTAs lead to correct intent
- HubSpot embed loads and submits
- Confirmation messaging appears

Test cases
- Desktop Chrome/Firefox/Safari
- iOS Safari + Android Chrome
- Reduced motion enabled
- Low-power mode (simulate) -> canvas disabled
