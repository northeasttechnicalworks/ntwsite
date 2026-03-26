# docs/design-system.md

Design intent: Luxury industrial + product clarity.
Theme: Dark, layered, material.

CSS tokens (required)
:root {
  /* Color core */
  --c-bg-0: #0f1115;       /* graphite deep */
  --c-bg-1: #111418;       /* graphite */
  --c-surface-0: #0b1b2a;  /* industrial navy deep */
  --c-surface-1: #0e2a47;  /* industrial navy */
  --c-accent-0: #1f4e79;   /* steel blue */
  --c-accent-1: #2a6aa1;   /* steel blue bright */
  --c-metal-0: #bfc5ce;    /* brushed silver */
  --c-text-0: #e6e9ee;     /* technical gray */
  --c-text-1: rgba(230,233,238,.78);
  --c-text-2: rgba(230,233,238,.60);
  --c-border-0: rgba(191,197,206,.18);
  --c-border-1: rgba(191,197,206,.28);

  /* Shadows (layered luxury) */
  --sh-1: 0 8px 24px rgba(0,0,0,.20);
  --sh-2: 0 18px 48px rgba(0,0,0,.35);
  --sh-glow: 0 0 0 1px rgba(31,78,121,.25), 0 10px 36px rgba(31,78,121,.14);

  /* Radii */
  --r-1: 10px;
  --r-2: 16px;
  --r-3: 22px;

  /* Spacing scale (8pt) */
  --s-1: 4px;
  --s-2: 8px;
  --s-3: 12px;
  --s-4: 16px;
  --s-5: 24px;
  --s-6: 32px;
  --s-7: 48px;
  --s-8: 64px;
  --s-9: 96px;
  --s-10: 128px;

  /* Type scale */
  --fs-0: 12px;
  --fs-1: 14px;
  --fs-2: 16px;
  --fs-3: 18px;
  --fs-4: 22px;
  --fs-5: 28px;
  --fs-6: 36px;
  --fs-7: 48px;
  --fs-8: 56px;
  --fs-9: 72px;

  /* Line heights */
  --lh-tight: 1.08;
  --lh-title: 1.14;
  --lh-body: 1.55;

  /* Grid */
  --container: 1200px;
  --gutter: 24px;

  /* Motion tokens (referenced by motion-system too) */
  --ease-standard: cubic-bezier(.2,.8,.2,1);
  --ease-out: cubic-bezier(0,0,.2,1);
  --dur-1: 120ms;
  --dur-2: 200ms;
  --dur-3: 320ms;
  --dur-4: 520ms;
  --dur-5: 900ms;

  /* Focus */
  --focus: 0 0 0 3px rgba(42,106,161,.35);
}

Typography
- Primary font: Inter
- Secondary font: Manrope (optional for subheads)
Rules:
- H1: 56–72px (desktop), 40–48px (mobile), tight tracking
- H2: 36–48px
- H3: 22–28px
- Body: 16–18px

Layout grid
- Max container: 1200px with 24px gutter
- Section spacing: 96–128px vertical on desktop, 64–96px mobile
- Use 12-column grid (conceptual) but keep components clean:
  - Hero: 6/6 split
  - Services grid: 3 columns desktop, 2 tablet, 1 mobile

Material system (must use)
- Backgrounds are layered:
  - base gradient + noise overlay + grid texture
- Panels use “glass + metal”:
  - surface: --c-surface-0/1
  - border: --c-border-0/1
  - shadow: --sh-1/--sh-2 with subtle glow

Component styling rules
- Avoid hard rectangles. Use radii (16–22px) and layered edges.
- Borders are subtle; glow only on hover or key focus.
- Buttons: pill or softly-rounded, with premium hover.
- Links: underlines on hover only; keep calm.

Responsive breakpoints
- xs: 375
- sm: 640
- md: 768
- lg: 1024
- xl: 1280

Dark-mode only (v1)
This site is intentionally dark to communicate technical authority and luxury restraint.
