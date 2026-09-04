---
version: 1

defaults:
  environment: local
  production_access: read-only
  sensitive_data: redact

context:
  sources: []

services: []

channels: []

reproduction:
  preferred_environment: local
  instructions: null
  commands: {}

verification:
  commands: {}
  live: []

records:
  destination: null
  instructions: null
  record_when: Severe, recurring, or architecturally informative.
---

# Debugfile

Add project-specific debugging guidance here.
