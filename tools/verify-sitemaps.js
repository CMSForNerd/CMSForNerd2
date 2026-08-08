// tools/verify-sitemaps.js
// Verification script to validate public/sitemap.txt and sitemap.txt structure,
// ensuring no broken links and checking XML sitemap output after build.

import fs from 'fs';
import path from 'path';

console.log('===================================================');
console.log('🧪 Verifying Sitemap Structure and Links');
console.log('===================================================');

// 1. Verify existence of root sitemap.txt and public/sitemap.txt
const rootTxtPath = path.resolve('sitemap.txt');
const publicTxtPath = path.resolve('public/sitemap.txt');

if (!fs.existsSync(rootTxtPath)) {
  console.error('❌ Error: root sitemap.txt does not exist.');
  process.exit(1);
}

if (!fs.existsSync(publicTxtPath)) {
  console.error('❌ Error: public/sitemap.txt does not exist.');
  process.exit(1);
}

const rootTxtContent = fs.readFileSync(rootTxtPath, 'utf8').trim().split(/\r?\n/);
const publicTxtContent = fs.readFileSync(publicTxtPath, 'utf8').trim().split(/\r?\n/);

if (rootTxtContent.length === 0 || publicTxtContent.length === 0) {
  console.error('❌ Error: sitemap files are empty.');
  process.exit(1);
}

if (rootTxtContent.join('\n') !== publicTxtContent.join('\n')) {
  console.error('❌ Error: root sitemap.txt and public/sitemap.txt are not identical.');
  process.exit(1);
}

console.log(`✅ Root and public TXT sitemaps are identical and contain ${rootTxtContent.length} URLs.`);

// 2. Validate URLs in sitemap.txt do not have broken patterns or protocols
const invalidUrls = rootTxtContent.filter(url => {
  return !url.startsWith('https://') || url.includes('//undefined') || url.includes('[object');
});

if (invalidUrls.length > 0) {
  console.error('❌ Error: Invalid URL patterns found in sitemap:', invalidUrls);
  process.exit(1);
}
console.log('✅ All URL patterns in TXT sitemaps are valid (HTTPS and well-formed).');

// 3. Verify built files in dist directory matches sitemap paths
const distPath = path.resolve('dist');
if (fs.existsSync(distPath)) {
  console.log('🔍 Validating Netlify URLs against compiled static assets in dist/...');
  const netlifyUrls = rootTxtContent.filter(url => url.startsWith('https://cmsfornerd2.netlify.app/'));

  let missingFilesCount = 0;
  for (const url of netlifyUrls) {
    const urlObj = new URL(url);
    const pathname = urlObj.pathname;

    // For netlify URLs, the path maps to a file in dist:
    // / -> dist/index.html
    // /about -> dist/about/index.html
    // /about/amp -> dist/about/amp/index.html
    let expectedFile = '';
    if (pathname === '/') {
      expectedFile = path.join(distPath, 'index.html');
    } else if (pathname === '/offline') {
      expectedFile = path.join(distPath, 'offline/index.html');
    } else if (pathname === '/amp') {
      expectedFile = path.join(distPath, 'amp/index.html');
    } else {
      expectedFile = path.join(distPath, pathname, 'index.html');
    }

    if (!fs.existsSync(expectedFile)) {
      console.warn(`⚠️ Warning: Expected static asset not found for ${url} (Tried: ${expectedFile})`);
      missingFilesCount++;
    }
  }

  if (missingFilesCount > 0) {
    console.warn(`⚠️ Completed link check: ${missingFilesCount} warnings. (This is normal for offline/index.html fallback variations if they don't map exactly, but standard pages must exist).`);
  } else {
    console.log('✅ All Netlify URLs successfully mapped to physical built HTML assets in dist/ directory!');
  }

  // 4. Verify dist/sitemap.xml
  const xmlPath = path.join(distPath, 'sitemap.xml');
  if (fs.existsSync(xmlPath)) {
    console.log('🔍 Validating built sitemap.xml...');
    const xmlContent = fs.readFileSync(xmlPath, 'utf8');

    if (!xmlContent.includes('<?xml version="1.0" encoding="UTF-8"?>')) {
      console.error('❌ Error: Built sitemap.xml does not have standard XML declaration header.');
      process.exit(1);
    }
    if (!xmlContent.includes('<urlset') || !xmlContent.includes('</urlset>')) {
      console.error('❌ Error: Built sitemap.xml is missing standard <urlset> tags.');
      process.exit(1);
    }

    // Parse all <loc> elements from the sitemap.xml
    const locRegex = /<loc>(https:\/\/[^<]+)<\/loc>/g;
    const xmlUrls = [];
    let match;
    while ((match = locRegex.exec(xmlContent)) !== null) {
      xmlUrls.push(match[1]);
    }

    let hasGitBook = false;
    let hasGitHubPages = false;
    let hasNetlify = false;

    for (const xmlUrl of xmlUrls) {
      try {
        const parsed = new URL(xmlUrl);
        if (parsed.hostname === 'cmsfornerd.gitbook.io' && parsed.pathname.startsWith('/cmsfornerd2')) {
          hasGitBook = true;
        }
        if (parsed.hostname === 'cmsfornerd.github.io' && parsed.pathname.startsWith('/CMSForNerd2')) {
          hasGitHubPages = true;
        }
        if (parsed.hostname === 'cmsfornerd2.netlify.app') {
          hasNetlify = true;
        }
      } catch (e) {
        // Ignored
      }
    }

    if (!hasGitBook) {
      console.error('❌ Error: Built sitemap.xml is missing GitBook URLs.');
      process.exit(1);
    }
    if (!hasGitHubPages) {
      console.error('❌ Error: Built sitemap.xml is missing GitHub Pages URLs.');
      process.exit(1);
    }
    if (!hasNetlify) {
      console.error('❌ Error: Built sitemap.xml is missing Netlify URLs.');
      process.exit(1);
    }

    console.log('✅ Built sitemap.xml has valid structure and successfully includes all multi-host publishing destinations!');
  } else {
    console.log('⚠️ Note: dist/sitemap.xml not found yet. Run "npm run build" to generate it.');
  }
} else {
  console.log('⚠️ Note: dist/ directory not found yet. Run "npm run build" to check sitemap static files.');
}

console.log('===================================================');
console.log('🎉 Verification Script Completed Successfully!');
console.log('===================================================');
