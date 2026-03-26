# docs/conversion-system.md

Conversion hierarchy
Primary: Request Coverage
Secondary: Request Service
Tertiary: Download Capability Statement

CTA placement rules
- Above the fold (hero)
- After service grid
- After coverage map
- After timeline
- Inside each service detail block
- Footer CTA band (optional)

Lead types and routing
- coverage_request -> integrator/partnership pipeline
- service_request -> operations/service pipeline
- capability_download -> nurture list

Forms
- Use HubSpot embed (see integrations.md)
- Each form includes hidden fields:
  - intent (coverage/service/integrator)
  - page_source
  - utm params

Micro-conversions
- map interaction (state selection)
- service module expansion
- scroll depth > 60%
Track these for optimization (analytics-measurement.md)

Confirmation UX
- On submit: show “What happens next” 3-step:
  1) Scope review within SLA
  2) Scheduling confirmation
  3) Deployment + closeout
