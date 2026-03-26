# docs/data-model.md

CMS-agnostic content entities

Entities
- Service
  - id, name, slug, summary, description
  - subservices[]
  - deliverables[]
  - slaTiers[]
  - exampleScopes[]
  - relatedServices[]
  - industries[]
  - locationsSupported[]
  - seoMeta { title, description }
- Industry
  - id, name, slug
  - painPoints[]
  - typicalDeployments[]
  - proofArtifacts[]
  - relatedServices[]
- Location
  - id, name, type (state/metro)
  - coverageTier (primary/secondary)
  - notes[]
- ProofArtifact
  - id, type (photo/doc/example)
  - title, caption
  - redactionStatus
- Persona
  - role, goals, painPoints, objections, decisionCriteria, proofRequired[]

Relationships
- Service <-> Industry (many-to-many)
- Service <-> Location (many-to-many)
- Service -> ProofArtifact (one-to-many)
- Persona -> Service (many-to-many)

Content governance
- Changes to service taxonomy must update:
  - services page
  - SEO slug list
  - internal linking modules
