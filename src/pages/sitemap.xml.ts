import { getCollection } from 'astro:content';
import { getCleanSlug } from '../utils/navigation';

export async function GET() {
  const pages = await getCollection('pages');
  const baseUrl = 'https://cmsfornerd2.netlify.app'; // Fallback base URL

  const urlElements = pages.map(page => {
    const cleanId = getCleanSlug(page.id);
    const slugPath = cleanId === 'index' ? '' : `${cleanId}`;
    const standardUrl = `${baseUrl}/${slugPath}`;
    const ampUrl = `${baseUrl}/${cleanId === 'index' ? 'amp' : `${cleanId}/amp`}`;

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

  const xmlContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${baseUrl}/offline</loc>
    <lastmod>2026-07-30</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.1</priority>
  </url>${urlElements}
</urlset>`;

  return new Response(xmlContent, {
    headers: {
      'Content-Type': 'application/xml',
    },
  });
}
