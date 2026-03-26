# docs/component-library.md

All pages must be built from these components.

Component list
- NavBar
- HeroTopology (canvas) OR HeroMap OR HeroProofStack
- CTAButton
- ServiceCapabilityGrid (interactive)
- ServiceCapabilityCard
- CoverageMapNE (interactive SVG)
- DeploymentTimeline
- ProofArtifactsStrip
- IndustryGrid
- TestimonialQuote (optional)
- StatsBar (optional)
- FAQAccordion
- HubSpotFormEmbed
- Footer

Component props (examples)

NavBar (YAML)
type: NavBar
props:
  links:
    - { label: "Home", href: "/" }
    - { label: "Services", href: "/services" }
    - { label: "Industries", href: "/industries" }
    - { label: "Coverage", href: "/coverage" }
    - { label: "Integrators", href: "/integrators" }
    - { label: "About", href: "/about" }
    - { label: "Contact", href: "/contact" }
  ctas:
    - { label: "Request Coverage", href: "/contact?intent=coverage", variant: "primary" }
    - { label: "Request Service", href: "/contact?intent=service", variant: "secondary" }

HeroTopology (JSON)
{
  "type": "HeroTopology",
  "props": {
    "headline": "Northeast Infrastructure Deployment Done Right.",
    "subhead": "Disciplined field execution for security and network infrastructure across NY, NJ, and CT—built for inspection and closeout.",
    "ctas": [
      { "label": "Request Coverage", "href": "/contact?intent=coverage", "variant": "primary" },
      { "label": "Request Service", "href": "/contact?intent=service", "variant": "secondary" }
    ],
    "microproof": ["After-hours cutovers", "Multi-site rollouts", "Inspection-ready installs"]
  }
}

ServiceCapabilityCard
Required:
- title
- shortDescription
- icon (stroke)
- diagramThumb (SVG)
- bullets (max 5)
States:
- default, hover, expanded
Behavior:
- hover expands bullets (max 3 visible)
- click expands drawer with full bullets + deliverables + CTA

CoverageMapNE
Required:
- statesPrimary[]
- statesSecondary[]
- tooltipTemplate
- sidePanelEnabled (true)
Accessibility:
- keyboard nav
- aria-live tooltip
Mobile:
- bottom sheet tooltip

DeploymentTimeline
Required:
- steps[]
- scrollProgressEnabled true
- expandOnClick optional

Footer
Required:
- about blurb
- quick links
- services links
- contact info
- social icons
- capability statement download link
- legal links

A11y requirements for all components
- Must be keyboard navigable
- Must have visible focus states
- Must support reduced motion
- Must have semantic headings and landmarks
