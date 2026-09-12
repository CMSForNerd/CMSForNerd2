import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import AstroPWA from '@vite-pwa/astro';
import { unified } from '@astrojs/markdown-remark';

const isGitHubPages = process.env.GITHUB_ACTIONS === 'true';

// Custom Rehype plugin to prefix absolute links in Markdown files when deploying to GitHub Pages
// Custom Rehype plugin to prefix raw root-relative links in Markdown files during the compilation step
function rehypeAddBase() {
  const base = isGitHubPages ? '/CMSForNerd2' : '';
  if (!base || base === '/') {
    return () => {};
  }
  const cleanBase = base.replace(/\/$/, '');
  return (tree) => {
    function walk(node) {
      if (node.type === 'element' && node.tagName === 'a' && node.properties && typeof node.properties.href === 'string') {
        const href = node.properties.href;
        if (href.startsWith('/') && !href.startsWith('//')) {
          node.properties.href = `${cleanBase}${href}`;
        }
      }
      if (node.children) {
        node.children.forEach(walk);
      }
    }
    walk(tree);
  };
}

export default defineConfig({
  site: isGitHubPages ? 'https://cmsfornerd.github.io' : 'https://cmsfornerd2.netlify.app',
  base: isGitHubPages ? '/CMSForNerd2' : '/',
  output: 'static',
  markdown: {
    processor: unified({
      rehypePlugins: [
        rehypeAddBase
      ]
    })
  },
  integrations: [
    mdx(),
    AstroPWA({
      registerType: 'autoUpdate',
      workbox: {
        maximumFileSizeToCacheInBytes: 35 * 1024 * 1024,
        navigateFallback: isGitHubPages ? '/CMSForNerd2/offline/' : '/offline/',
        navigateFallbackAllowlist: [/^[^?*#\.]*$/],
        runtimeCaching: [
          {
            urlPattern: ({ request }) => request.destination === 'document',
            handler: 'NetworkFirst',
            options: {
              cacheName: 'pages-cache',
              expiration: {
                maxEntries: 100,
                maxAgeSeconds: 30 * 24 * 60 * 60,
              },
            },
          },
          {
            urlPattern: ({ request }) =>
              request.destination === 'script' ||
              request.destination === 'style' ||
              request.destination === 'worker',
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'static-resources',
            },
          },
          {
            urlPattern: ({ request }) => request.destination === 'image',
            handler: 'CacheFirst',
            options: {
              cacheName: 'images-cache',
              expiration: {
                maxEntries: 60,
                maxAgeSeconds: 30 * 24 * 60 * 60,
              },
            },
          },
        ],
      },
      manifest: {
        name: 'CMSForNerd2',
        short_name: 'CFN2',
        theme_color: '#0d6efd',
        background_color: '#ffffff',
        display: 'standalone',
        start_url: isGitHubPages ? '/CMSForNerd2/' : '/',
        icons: [
          { src: 'assets/pwa/icon-192x192.png', sizes: '192x192', type: 'image/png' },
          { src: 'assets/pwa/icon-512x512.png', sizes: '512x512', type: 'image/png' }
        ]
      }
    })
  ]
});
