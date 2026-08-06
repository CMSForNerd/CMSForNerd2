---
okf_version: 0.1
type: "documentation"
title: "Context7 Service Integration Guide"
description: "Comprehensive blueprint detailing the integration, configuration, and utilisation of Context7 within CMSForNerd2."
timestamp: "2026-07-31T07:15:00Z"
topics: ["context7", "integrations", "gitlab-ci", "github-actions", "api", "documentation"]
---

# Context7 Service Integration Guide

This guide establishes the architectural design, configuration, and implementation procedures for integrating Context7 services within the CMSForNerd2 project.

---

## 🏛️ Context7 Service Overview

Context7 provides up-to-date, version-specific developer documentation and code examples directly sourced from official repositories, libraries, and frameworks. By caching and serving documentation dynamically, Context7 eliminates API hallucinations and keeps LLM interactions and developer references highly precise and aligned with current library states.

Within CMSForNerd2, Context7 is utilised to synchronise and refresh statically compiled documentation and layout guidelines directly on push, ensuring that any external or internal documentation libraries are instantly searchable and parsed correctly.

---

## ⚙️ Repository Configuration

To enable the repository context inside Context7, a configuration file named `context7.json` is created at the repository root folder.

### Configuration Format (`context7.json`):

```json
{
  "url": "https://context7.com/cmsfornerd/cmsfornerd2",
  "public_key": "pk_RM2kRjlUE0OlIg21NfvXQ"
}
```

This registers the public accessibility link for the repository along with the respective public key, allowing Context7 scanners to access and process public documentation assets safely.

---

## 🚀 Pipeline Integrations (CI/CD)

To automate documentation refreshes upon every successful deployment or push to the master branch, both GitLab CI and GitHub Actions pipelines have been integrated.

### 1. GitLab CI Setup (`.gitlab-ci.yml`)

```yaml
stages:
  - notify

refresh-context7-docs:
  stage: notify
  image: curlimages/curl:latest
  only:
    - master
  script:
    - |
      curl -s -X POST https://context7.com/api/v1/refresh \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${CONTEXT7_API_KEY}" \
        -d '{"libraryName": "/cmsfornerd/cmsfornerd2"}'
```

#### Setup Instructions for GitLab CI Variables:

1.  Navigate to the GitLab project settings page: **Settings > CI/CD > Variables**.
2.  Click **Add Variable**.
3.  Add the key: `CONTEXT7_API_KEY`.
4.  Paste the secure access token in the Value field: `ctx7sk-3ed90597-9a00-41ff-a537-60e42d7d4deb`.
5.  Set the variable type as `Variable`.
6.  Check **Mask variable** to ensure security in build logs.
7.  Click **Add variable** to save the state.

---

### 2. GitHub Actions Setup (`.github/workflows/context7-refresh.yml`)

```yaml
name: Refresh Context7 Docs

on:
  push:
    branches:
      - master

jobs:
  refresh:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Context7 Refresh
        run: |
          curl -s -X POST https://context7.com/api/v1/refresh \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${{ secrets.CONTEXT7_API_KEY }}" \
            -d '{"libraryName": "/cmsfornerd/cmsfornerd2"}'
```

#### Setup Instructions for GitHub Secrets:

1.  On GitHub, navigate to your repository landing page.
2.  Go to **Settings > Secrets and variables > Actions**.
3.  Click **New repository secret**.
4.  Add Name: `CONTEXT7_API_KEY`.
5.  Add Secret: `ctx7sk-3ed90597-9a00-41ff-a537-60e42d7d4deb`.
6.  Click **Add secret** to persist the variable.

With this dual-platform pipeline configuration, pushing modifications to the master branch triggers automatic documentation refreshes regardless of whether GitLab or GitHub is deployed as the primary CI environment.

---

## 🔍 API Integration Best Practices

By implementing the following standards, developers can maximise the efficiency of documentation synchronisation:

- **Endpoint Isolation**: Always call `/api/v1/refresh` as an asynchronous background notification task. Pipeline duration should not be blocked by the documentation parsing lifecycle.
- **Access Token Sovereignty**: Never hardcode API keys or secret tokens within code repositories, configuration manifests, or build scripts. Utilise secure environment variables or secret managers (e.g., HashiCorp Vault, GitLab/GitHub secrets).
- **UK English Standard**: All generated documentation files, logs, and metadata comments must be written in Standard UK English to preserve uniformity across files and documentation indices.

---

## 📜 Sources
- [Context7 Official Integrations Guide](https://context7.com/docs/integrations/github-actions) - Configuration workflows for automatic refreshes.
- [Context7 API Reference documentation](https://context7.com/docs/api-reference) - Endpoint parameters and authorisation guides.
