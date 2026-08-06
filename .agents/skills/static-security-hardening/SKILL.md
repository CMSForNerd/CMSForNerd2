---
okf_version: 0.1
type: "skill"
title: "Static Security Hardening Skill"
name: "static-security-hardening"
description: "Applies static security whitelisting, cryptographic CSP hashes, OWASP standard defensive headers, and static performance caching."
timestamp: "2026-08-01T12:00:00Z"
topics: ["security", "hardening", "csp", "nginx", "owasp"]
---

# Static Security Hardening Skill

This skill governs the operational procedures, standards, and defensive configurations required to secure statically served assets in CMSForNerd2 in accordance with OWASP principles.

## When to use this skill

- When configuring or updating web server security headers (e.g., in `nginx/nginx.conf`).
- When introducing or updating inline scripts, stylesheets, or external content origins.
- When updating security-related files such as the RFC 9116 security contact or the robots.txt index path.
- When teaching or demonstrating static security whitelisting and performance hardening via educational materials.

## Operational Standards & Procedures

### 1. Nginx Defensive Header Hardening
By configuring defensive headers in Nginx, the application limits exposure to common web-based vulnerabilities:
- **HSTS (Strict-Transport-Security)**: Force secure HTTPS connections.
- **Permissions-Policy**: Restrict access to browser features and APIs.
- **Content Security Policy (CSP)**: Implement a strict, hardened policy restricting script and resource execution.
- Maintain Nginx rules inside `nginx/nginx.conf` and adhere strictly to OWASP standards.

### 2. Cryptographic CSP Inline Script Whitelisting
To permit essential inline scripts without introducing security vulnerabilities, cryptographically sign inline scripts and whitelist their SHA-256 hashes in the CSP:
- **Theme-Switching Script**: The main theme-switching logic in `src/layouts/Layout.astro` has its `is:inline` attribute removed to compile and bundle it as a cacheable static asset. Early flash prevention remains inline in the `<head>` with its SHA-256 hash whitelisted in Nginx.
- **Other Inline Scripts**: Explicitly whitelist SHA-256 hashes of the graduation signature (`graduation.md`) and sitemap (`sitemap-page.md`), along with trusted external script origins (e.g., `https://cdn.ampproject.org`).

### 3. Public Security Meta-Files
With the static modernisation of CMSForNerd2, maintain active compliance files:
- **RFC 9116 Compliant Security Contact**: Maintain a valid security contact file at `public/.well-known/security.txt`.
- **Modernised Sitemap Crawler Index**: Configure `public/robots.txt` to point explicitly to `/sitemap.xml` instead of `/sitemap.php`.

### 4. Educational Worksheet Integration
In contrast to purely automated configurations, CMSForNerd2 serves as an educational laboratory platform:
- The cmsfornerd2 laboratory manual (`src/content/pages/lab-manual.md`) features an interactive educational worksheet: 'Laboratory Module 7: Static Security Whitelisting & Performance Hardening' (`src/content/pages/lab-module7.md`).
- This module instructs students on applying OWASP standards, cryptographic CSP hashes, Nginx defensive configurations, and static performance caching.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
