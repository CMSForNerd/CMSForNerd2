import { getCollection } from 'astro:content';
import { getCleanSlug } from '../utils/navigation';

/**
 * Astro endpoint handler for generating a dynamically populated multi-host XML sitemap.
 *
 * This endpoint compiles sitemap URLs mapped to multiple deployment/publishing hosts:
 * 1. Netlify Production Host (https://cmsfornerd2.netlify.app/)
 * 2. GitHub Pages Subpath Deployment Host (https://cmsfornerd.github.io/CMSForNerd2/)
 * 3. GitBook Educational Host (https://cmsfornerd.gitbook.io/cmsfornerd2/)
 *
 * It generates standard URL sets as well as specific Accelerated Mobile Page (AMP)
 * routes corresponding to each migrated content document.
 *
 * @returns {Promise<Response>} An HTTP Response object containing the compiled XML sitemap payload.
 */
export async function GET() {
  const pages = await getCollection('pages');
  const netlifyBaseUrl = 'https://cmsfornerd2.netlify.app';
  const githubPagesBaseUrl = 'https://cmsfornerd.github.io/CMSForNerd2';

  // Dynamic Astro content routes computed in a single O(N) pass for both Netlify and GitHub Pages
  let netlifyElements = '';
  let githubPagesElements = '';

  for (let i = 0; i < pages.length; i++) {
    const cleanId = getCleanSlug(pages[i].id);
    const isIndex = cleanId === 'index';
    const slugPath = isIndex ? '' : `${cleanId}`;
    const priority = isIndex ? '1.0' : '0.8';

    const netlifyStd = `${netlifyBaseUrl}/${slugPath}`;
    const netlifyAmp = `${netlifyBaseUrl}/${isIndex ? 'amp' : `${cleanId}/amp`}`;

    netlifyElements += `
  <url>
    <loc>${netlifyStd}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>${priority}</priority>
  </url>
  <url>
    <loc>${netlifyAmp}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>`;

    const githubStd = `${githubPagesBaseUrl}/${slugPath}`;
    const githubAmp = `${githubPagesBaseUrl}/${isIndex ? 'amp' : `${cleanId}/amp`}`;

    githubPagesElements += `
  <url>
    <loc>${githubStd}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>${priority}</priority>
  </url>
  <url>
    <loc>${githubAmp}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>`;
  }

  // Static GitBook elements based on SUMMARY.md mapping
  const gitbookBaseUrl = 'https://cmsfornerd.gitbook.io/cmsfornerd2';
  const gitbookPages = [
    { path: '', priority: '1.0', changefreq: 'monthly' },
    { path: 'start-here', priority: '0.8', changefreq: 'monthly' },
    { path: 'docs/migration-guide', priority: '0.8', changefreq: 'monthly' },
    { path: 'docs/context7-integration', priority: '0.8', changefreq: 'monthly' },
    { path: 'agents', priority: '0.8', changefreq: 'monthly' }
  ];

  const gitbookElements = gitbookPages.map(page => {
    const standardUrl = `${gitbookBaseUrl}/${page.path}`;
    return `
  <url>
    <loc>${standardUrl}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
  </url>`;
  }).join('');

  const xmlContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${netlifyBaseUrl}/offline</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.1</priority>
  </url>
  <url>
    <loc>${githubPagesBaseUrl}/offline</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.1</priority>
  </url>${netlifyElements}${githubPagesElements}${gitbookElements}
</urlset>`;

  return new Response(xmlContent, {
    headers: {
      'Content-Type': 'application/xml',
    },
  });
}
