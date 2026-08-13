---
okf_version: 0.1
type: "skill"
title: "Dependency Management Skill"
name: "dependency-management"
description: "Maintains pinned dependency determinism and resolves peer-dependency conflicts across all runtime environments."
timestamp: "2026-08-01T12:00:00Z"
topics: ["dependencies", "npm", "peer-deps", "node", "lockfile"]
---

# Dependency Management Skill

This skill governs the standards and procedures used to maintain strict dependency control, build determinism, and automatic peer-dependency resolution.

## When to use this skill

- When installing, upgrading, or removing Node.js dependencies.
- When resolving peer-dependency conflicts between legacy Astro integration packages.
- When configuring local, CI/CD, or cloud containerised build environments.
- When verifying build determinism in the project dependency tree.

## Operational Standards & Procedures

### 1. Pinned Dependency Determinism
To guarantee build determinism and handle peer-dependency constraints with legacy packages (such as `@vite-pwa/astro`):
- Dependencies in `package.json` (such as `astro`, `@astrojs/mdx`, and `@vite-pwa/astro`) must be strictly pinned to exact versions (e.g., `astro@7.1.6`).
- Avoid prefixing dependency versions with carets (`^`) or tildes (`~`) unless explicitly required.

### 2. Peer-Dependency Conflict Resolution
By utilising standard Node Package Manager options, avoid manual peer dependency workarounds:
- The development environment is configured via a root-level `.npmrc` file specifying `legacy-peer-deps=true`.
- This automatically resolves peer-dependency conflicts (such as between `@vite-pwa/astro` and newer Astro versions like `astro@7.1.6`) across any local, containerised, or cloud deployment environments (including Render.com host environments).

### 3. Node.js Environment Determinism
To align compilation across local, dockerised, and CI/CD environments:
- The project requires Node.js v22 (>=22.12.0) for Astro 7.1 compatibility.
- The GitHub Actions deployment workflow (`deploy-gh-pages.yml`) utilises Node.js version 22.
- Both the `Dockerfile` and `Containerfile` configure their builder stage using the standard `node:22-alpine` base image.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
