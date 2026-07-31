---
okf_version: 0.1
type: documentation
title: "CMSForNerd to CMSForNerd2 Static Migration Guide"
timestamp: "2026-07-31T10:00:00Z"
description: "Comprehensive architectural guide for migrating the database-free flat-file PHP CMS to Astro Static Site Generator (SSG) with HTML5, CSS3, and modern JavaScript."
topics: [migration, astro, static, php, architecture]
---

# 🚀 CMSForNerd to CMSForNerd2: Static Migration Guide
## *From Database-Free PHP to Modern Static Site Generator (Astro SSG)*

---

## 1. Executive Summary & Migration Context

With the rapid progression of web technologies, legacy server-rendered frameworks are increasingly being succeeded by modern Static Site Generators (SSGs) that deliver maximum performance, enhanced security, and simplified deployment models. In this context, the migration of **CMSForNerd** from its flat-file PHP 8.4 implementation to **CMSForNerd2**—a purely static, client-facing architecture—presents a major leap forward.

By removing PHP, the runtime surface area is compressed to zero, eliminating server-side vulnerabilities such as Local File Inclusion (LFI), Directory Traversal, and PHP-FPM misconfiguration exploits. Through the deployment of an SSG-based pipeline, all layout processing is executed at build time. The final output consists entirely of statically served HTML5, CSS3, and JavaScript, deployable to high-availability Content Delivery Networks (CDNs) or simple Nginx web servers.

This document serves as the human-readable architectural blueprint and implementation playbook for migrating CMSForNerd to CMSForNerd2.

---

## 2. Legacy PHP Architecture Analysis

To ensure architectural fidelity during the migration, the fundamental pillars of the legacy PHP CmsForNerd system must be thoroughly understood:

*   **"Pair Logic" Architecture**: Layouts are strictly separated from content. Each controller file (e.g., `index.php`) acts as a master that sets metadata (title, schema type, author) and loads a corresponding HTML/PHP fragment from the `contents/` directory (e.g., `contents/index-body.inc`).
*   **Dual-View Engine (Standard / AMP)**: The central router (`themes/CmsForNerd/pager.php`) parses the query parameter `?view=amp` to toggle between standard desktop rendering and Google-validated Accelerated Mobile Pages (AMP) containing inline styling below the strict 75KB limit.
*   **PWA and SPA-like Hydration Router**: A lightweight vanilla JavaScript router (`router.js`) overrides internal link clicks. By appending the `X-Requested-With: XMLHttpRequest` header, it fetches purely the raw content fragments from PHP and dynamically updates the `<main>` element to provide instantaneous transitions.
*   **Zero-Global Mutable State**: The application runs without global variables, relying entirely on an immutable `CmsContext` object injected into templates to enforce strict functional isolation.

---

## 3. Evaluation of Static Site Frameworks

During the discovery phase, multiple static site generators were evaluated against the core design principles of CMSForNerd (database-free, content-first, zero-JS capability, and high performance):

| Criteria / Feature | Astro 🚀 (Recommended) | Eleventy (11ty) | Hugo | Next.js (Static Export) |
| :--- | :--- | :--- | :--- | :--- |
| **Default JS footprint** | **Zero JS by default** | Zero JS by default | Zero JS by default | Full React runtime bundle |
| **"Pair Logic" Mapping** | **Perfect** (Frontmatter + Layouts) | Moderate (Frontmatter + Markdown) | Moderate (Go templates) | High complexity |
| **Modern Tech Stack** | **HTML5, CSS3, Vite, TS** | HTML5, Node.js | Go templating engine | React, Webpack |
| **Content Security** | Excellent (Static build removes XSS risk) | Good (Static) | Good (Static) | Good (Static) |
| **PWA & SPA Transitions** | **Built-in (View Transitions)** | Manual integration | Manual integration | Built-in |
| **AMP Support** | Excellent (Via custom static paths) | Complex templates | Complex templates | Highly complex |

### Why Astro is the Ultimate Fit

By selecting **Astro**, the project gains several critical advantages:
1.  **Component Frontmatter (Build-Time Pair Logic)**: Astro uses an HTML-like component format (`.astro`) featuring a JS/TS frontmatter block (`---`). This executes solely during the build process, mapping 1-to-1 to the PHP "Pair Logic" pattern where meta-variables are initialised prior to UI rendering.
2.  **Islands Architecture**: Standard pages are compiled down to zero client-side JavaScript. Client-side code is only loaded where explicit interactivity is required, matching the "Zero-Debt" and high-performance philosophy.
3.  **Built-in SPA Routing**: Astro's `<ViewTransitions />` component provides a native, hardware-accelerated SPA routing mechanism, completely replacing the custom, error-prone `router.js` fragment.
4.  **Static View Differentiation**: Rather than using dynamic query strings (`?view=amp`), Astro's build engine can compile dual outputs statically (e.g., `dist/index.html` and `dist/amp/index.html`), preserving 100% offline and static compatibility.

---

## 4. Target Architecture for CMSForNerd2

Through this modernisation, CMSForNerd2 will leverage the latest web technologies:

*   **Languages**: Modern HTML5, modern CSS3 (utilising native CSS variables, custom media queries, and modern flexbox/grid layouts), and TypeScript (where dynamic client-side code is necessary).
*   **Core Framework**: Astro (v7.1, configured with static output to leverage stable features such as Vite 8, the optimised Rust-based compiler, Sätteri Markdown pipeline, and refined Content Security Policy directives).
*   **Styling**: Standardised, decoupled CSS files using native CSS nesting and variables. This keeps styling fully compliant with legacy aesthetics while enabling automated CSS shaking to satisfy the 75KB AMP budget.
*   **State Management**: Static context parameters passed at build time, replicating the immutable `CmsContext` pattern.
*   **PWA Capabilities**: Service workers managed via `@vite-pwa/astro` or native script registration in Astro's `public/` folder, ensuring robust offline cache performance.

---

## 5. Step-by-Step Migration Process

To perform a structured and bug-free migration, developers should follow this step-by-step playbook:

### Step 5.1: Initialising CMSForNerd2
In the root directory of the target repository, bootstrap the Astro project:
```bash
npm create astro@latest -- --template minimal --install --git false
```
*Note: Ensure that the output in `astro.config.mjs` has `output: 'static'` configured:*
```javascript
import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'static',
  // Configuration options for pre-rendering, markdown processing, and assets
});
```

### Step 5.2: Directory Mapping Strategy
By restructuring directories, files are mapped from PHP to the SSG standard:

| Legacy PHP Source Directory | New Astro Target Directory | Purpose |
| :--- | :--- | :--- |
| `contents/*.inc` | `src/content/pages/` | Contains markdown/MDX page content fragments. |
| `contents/left-side.inc` | `src/components/Navigation.astro` | Dynamic navigation component. |
| `contents/right-side.inc` | `src/components/Widgets.astro` | Sidebar widget items. |
| `themes/CmsForNerd/style.css` | `src/styles/global.css` | Main desktop styles. |
| `themes/CmsForNerd/*.tpl` | `src/layouts/Layout.astro` | Global layout wrapper. |
| `assets/pwa/*` | `public/assets/pwa/` | Static static assets and PWA icons. |
| `robots.txt` / `favicon.ico` | `public/` | Standard root static assets. |

### Step 5.3: Migrating Controllers and Fragments (Pair Logic)
In Astro, the separation of concerns is maintained via layout components.

For example, a typical legacy controller `about.php` and its content fragment `contents/about-body.inc` are merged and modernised into `src/pages/about.astro`:

```astro
---
// src/pages/about.astro
import Layout from '../layouts/Layout.astro';
import SidebarLeft from '../components/SidebarLeft.astro';
import SidebarRight from '../components/SidebarRight.astro';

// Initialize the Immutable build context (replicating CmsContext)
const pageContext = {
  title: "About Us | The Developer's Laboratory",
  description: "A static modernization of the lightweight flat-file CMS.",
  schemaType: "AboutPage"
};
---

<Layout context={pageContext}>
  <div class="layout-grid">
    <aside id="left">
      <SidebarLeft />
    </aside>

    <main id="content">
      <article class="modernized-page">
        <h1>About the Laboratory</h1>
        <p>
          This is a static content page migrated from the PHP flat-file contents.
          All content is fully compiled to static HTML during the build process.
        </p>
      </article>
    </main>

    <aside id="right">
      <SidebarRight />
    </aside>
  </div>
</Layout>
```

### Step 5.4: Migrating Content via Markdown & Content Collections
To simplify long-term editing, page fragments should be migrated from raw `.inc` files to `.md` files under `src/content/pages/`.

Define the type-safe schema in `src/content/config.ts`:
```typescript
import { defineCollection, z } from 'astro:content';

const pagesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    schemaType: z.string().default('WebPage'),
    author: z.string().default('Harisfazillah Jamel')
  })
});

export const collections = {
  'pages': pagesCollection,
};
```
Through this validation pattern, compile-time checks are executed to ensure content metadata matches strict rules, providing the same safety guarantees as PHPStan Level 8 did for PHP code.

### Step 5.5: Static Dual-View Generation (AMP View)
To preserve Accelerated Mobile Pages (AMP) support without runtime PHP, Astro leverages its dynamic static path generation.

Create `src/pages/[pageName]/amp.astro` or `src/pages/amp/[pageName].astro`:
```astro
---
import { getCollection } from 'astro:content';
import AmpLayout from '../../layouts/AmpLayout.astro';

export async function getStaticPaths() {
  const pages = await getCollection('pages');
  return pages.map(page => ({
    params: { pageName: page.slug },
    props: { page }
  }));
}

const { page } = Astro.props;
const { Content } = await page.render();
---

<AmpLayout title={page.data.title} description={page.data.description}>
  <article>
    <h1>{page.data.title}</h1>
    <Content />
  </article>
</AmpLayout>
```
During the build step, Astro compiles both the standard layout and the stripped-down, AMP-validated `<amp-img>` and AMP CSS layout automatically.

### Step 5.6: PWA Service Worker & SPA Client-Side Routing
With Astro's client-side capabilities, the custom AJAX routing logic is modernised:
*   **Routing**: Incorporate the `<ViewTransitions />` component into the primary Layout to enable buttery smooth, SPA-like client-side hydration without writing any custom JavaScript.
*   **Service Worker**: Install the `@vite-pwa/astro` integration to manage caching, background syncing, and full offline support. Configure it in `astro.config.mjs`:
    ```javascript
    import { defineConfig } from 'astro/config';
    import AstroPWA from '@vite-pwa/astro';

    export default defineConfig({
      integrations: [
        AstroPWA({
          registerType: 'autoUpdate',
          manifest: {
            name: 'CMSForNerd2',
            short_name: 'CFN2',
            theme_color: '#0d6efd',
            background_color: '#ffffff',
            display: 'standalone',
            start_url: '/',
            icons: [
              { src: 'assets/pwa/icon-192x192.png', sizes: '192x192', type: 'image/png' },
              { src: 'assets/pwa/icon-512x512.png', sizes: '512x512', type: 'image/png' }
            ]
          }
        })
      ]
    });
    ```

---

## 6. Build & Deployment Architecture

By migrating to static assets, Day 2 operations are massively simplified. High-availability container orchestration is replaced or augmented by GitOps-driven deployment.

### Build Step
Execute the production build to compile static assets:
```bash
npm run build
```
This writes all HTML, CSS, and JS files to the `dist/` directory, completely self-contained.

### Deploying to Render.com with NGINX
To deploy CMSForNerd2 to Render.com, we utilise a secure multi-stage Docker build that compiles our Astro 7.1 application and packages it within a lightweight, unprivileged NGINX Alpine container.

The deployment infrastructure is defined via three root-level files:
1.  **`render.yaml`** (Blueprint Specification) — Declares a web service using the Docker runtime on the Starter plan in the Singapore region, pointing to `/healthz` for health checks.
2.  **`Dockerfile`** / **`Containerfile`** — Leverages `node:20-alpine` to compile the static Astro build and then copies the output directory (`dist/`) into an unprivileged `nginx:alpine-slim` runtime.
3.  **`nginx/nginx.conf`** — Formulates a highly-hardened unprivileged NGINX configuration listening on port `8080`, supporting Clean URLs (routing `/about` to `/about.html` and falling back to `index.html`), gzip compression, and secure HTTP response headers.

### Hardened NGINX Container Configuration
To satisfy unprivileged execution rules and defend against host compromise, standardise on our hardened `./nginx/nginx.conf`:
```nginx
worker_processes auto;
pid /tmp/nginx.pid;

events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging settings
    access_log /dev/stdout;
    error_log /dev/stderr warn;

    # Performance optimisation
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    # Gzip compression configuration
    gzip on;
    gzip_disable "msie6";
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_buffers 16 8k;
    gzip_http_version 1.1;
    gzip_min_length 256;
    gzip_types
        text/plain
        text/css
        application/json
        application/javascript
        application/x-javascript
        text/xml
        application/xml
        application/xml+rss
        text/javascript
        image/svg+xml;

    server {
        # Port 8080 for unprivileged operation
        listen 8080 default_server;
        listen [::]:8080 default_server;
        server_name _;

        root /usr/share/nginx/html;
        index index.html;

        # Custom security headers
        add_header X-Frame-Options "DENY" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header Referrer-Policy "no-referrer-when-downgrade" always;
        add_header Content-Security-Policy "default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://*; connect-src 'self' https://*;" always;

        # Healthcheck location
        location = /healthz {
            access_log off;
            add_header Content-Type text/plain;
            return 200 "OK";
        }

        # Handling static assets with caching
        location /assets/ {
            expires 1y;
            add_header Cache-Control "public, no-transform";
            try_files $uri =404;
        }

        # Clean URLs routing for Astro static pages
        location / {
            try_files $uri $uri/ $uri.html /index.html =404;
        }

        # Error handling
        error_page 404 /404.html;
        location = /404.html {
            internal;
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            internal;
        }
    }
}
```

---

## 7. Migration Timeline & Checklist

To coordinate the team's operational efforts, follow this milestone progression:

1.  **Phase 1: Project Bootstrapping** (Days 1–2)
    *   [ ] Bootstrapping the Astro framework in CMSForNerd2.
    *   [ ] Migrating global stylesheet and static icons.
2.  **Phase 2: Content Remapping** (Days 3–5)
    *   [ ] Remapping PHP layout templates (`bodytop.tpl`, `bodyfooter.tpl`) to Astro components.
    *   [ ] Converting flat-file pages under `contents/*.inc` to Markdown Content Collections.
3.  **Phase 3: Dual-View and SEO Calibration** (Days 6–8)
    *   [ ] Building static paths for standard views and AMP-compliant views.
    *   [ ] Implementing structured Schema.org JSON-LD generation based on `schemaType`.
4.  **Phase 4: Service Worker & Performance Audit** (Days 9–10)
    *   [ ] Implementing `@vite-pwa/astro` for instant offline loading.
    *   [ ] Compiling files and running Lighthouse audits to achieve 100/100 performance scores.

---

## SOURCES
- [Astro Documentation](https://docs.astro.build) - Comprehensive specifications for static site building, layouts, content collections, and routing.
- [Accelerated Mobile Pages (AMP) Specifications](https://amp.dev) - Official layout guidelines, validation rules, and CSS limits for mobile views.
- [Vite PWA Plugin](https://vite-pwa-org.netlify.app) - Implementation guide for offline service worker registration and caching strategies.
- [CMSForNerd Legacy Repository](https://github.com/CMSForNerd/CmsForNerd) - The baseline codebase containing the flat-file PHP 8.4 dual-view logic and contents.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-30*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
