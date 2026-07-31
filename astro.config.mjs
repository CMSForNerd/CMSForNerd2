import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import AstroPWA from '@vite-pwa/astro';

export default defineConfig({
  output: 'static',
  integrations: [
    mdx(),
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
