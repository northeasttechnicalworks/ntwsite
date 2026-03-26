# docs/integrations.md

Required integrations
- HubSpot forms (embed code placeholder)
- Analytics (unspecified)
- Error monitoring (optional)
- Map rendering (SVG internal)

HubSpot
- Use HubSpot embed script on contact + integrators pages
- Use intent routing with querystring:
  - /contact?intent=coverage
  - /contact?intent=service
  - /contact?intent=integrator

Analytics options (choose one)
- GA4 (standard)
- Plausible (privacy-friendly)
- PostHog (product analytics)
Mark selection as [[ANALYTICS_PROVIDER]] until decided.

Error monitoring options
- Sentry
- Rollbar
Mark selection as [[ERROR_MONITORING]].

Map
- Use custom inline SVG for Northeast states. No Mapbox dependency required.

Assets
- Icons: Lucide or Phosphor
- Diagrams: SVG authored in code (or exported)
