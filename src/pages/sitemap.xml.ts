import { getCollection } from 'astro:content';
import { getCleanSlug } from '../utils/navigation';

export async function GET() {
  const pages = await getCollection('pages');
  const netlifyBaseUrl = 'https://cmsfornerd2.netlify.app';
  const githubPagesBaseUrl = 'https://cmsfornerd.github.io/CMSForNerd2';

  // Dynamic Astro content routes for Netlify
  const netlifyElements = pages.map(page => {
    const cleanId = getCleanSlug(page.id);
    const slugPath = cleanId === 'index' ? '' : `${cleanId}`;
    const standardUrl = `${netlifyBaseUrl}/${slugPath}`;
    const ampUrl = `${netlifyBaseUrl}/${cleanId === 'index' ? 'amp' : `${cleanId}/amp`}`;

    return `
  <url>
    <loc>${standardUrl}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>${cleanId === 'index' ? '1.0' : '0.8'}</priority>
  </url>
  <url>
    <loc>${ampUrl}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>`;
  }).join('');

  // Dynamic Astro content routes for GitHub Pages
  const githubPagesElements = pages.map(page => {
    const cleanId = getCleanSlug(page.id);
    const slugPath = cleanId === 'index' ? '' : `${cleanId}`;
    const standardUrl = `${githubPagesBaseUrl}/${slugPath}`;
    const ampUrl = `${githubPagesBaseUrl}/${cleanId === 'index' ? 'amp' : `${cleanId}/amp`}`;

    return `
  <url>
    <loc>${standardUrl}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>${cleanId === 'index' ? '1.0' : '0.8'}</priority>
  </url>
  <url>
    <loc>${ampUrl}</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>`;
  }).join('');

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
