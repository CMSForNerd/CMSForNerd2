---
spec_version: "0.2"
type: "skill"
skill_id: "openapi_spec_generation"
name: "openapi-spec-generation"
title: "OpenAPI 3.1 Specification Generation Skill"
description: "Generates, validates, and maintains OpenAPI 3.1+ specifications, contract compliance, and SDK schema documentation."
version: "1.0.0"
timestamp: "2026-09-06T00:00:00Z"
author: "AI Workspace Assistant"
tags: ["openapi", "api-docs", "contract-testing", "json-schema", "rest"]
status: "stable"
sources:
  - id: "wshobson_openapi_spec"
    title: "OpenAPI Spec Generation Skill"
    url: "https://github.com/wshobson/agents"
  - id: "openapi_31_spec"
    title: "OpenAPI 3.1.0 Specification"
    url: "https://spec.openapis.org/oas/v3.1.0"
inputs:
  source_routes:
    type: "string"
    description: "Code routes, schemas, or design notes to synthesize into OpenAPI specification."
outputs:
  openapi_spec:
    type: "string"
    description: "Validated OpenAPI 3.1 YAML/JSON contract file."

okf_version: "0.1"
---

# OpenAPI 3.1 Specification Generation Skill (`openapi-spec-generation`)

The `openapi-spec-generation` skill provides tools for drafting, validating, and maintaining OpenAPI 3.1+ specifications for API contracts, static endpoints, and interactive documentation.

## Operational Directives

1. **Contract First & Schema Integrity**:
   - Ensure explicit definitions for `paths`, `components/schemas`, `responses`, `requestBodies`, and `securitySchemes`.
   - Never invent response fields; inspect route code, TypeScript types, or test suites to confirm actual return types.

2. **OpenAPI 3.1 Features**:
   - Enforce full JSON Schema draft 2020-12 compatibility for data types.
   - Include realistic request and response examples for every HTTP status code (e.g. `200 OK`, `400 Bad Request`, `404 Not Found`).

3. **Documentation Integration**:
   - Synthesize OpenAPI definitions into Markdown reference guides or Astro static endpoints (`/sitemap.xml`, API endpoints).

## FAQs

### Which OpenAPI specification versions are supported?
This skill focuses specifically on OpenAPI 3.1.0 and above.

### Can this skill be used for design-first API drafting?
Yes, it supports both design-first drafting and code-first spec extraction.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
