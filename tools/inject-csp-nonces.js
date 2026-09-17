/**
 * @file inject-csp-nonces.js
 * @description Post-build utility for Content Security Policy (CSP) hash nonce auto-injection.
 * Scans static HTML files in dist/, computes cryptographic SHA-256 base64 digests for dynamic
 * inline WebGPU shader scripts and inline application scripts, auto-injects CSP meta tags into
 * <head>, and generates a dist/csp-manifest.json artifact.
 */

import fs from 'fs';
import path from 'path';
import crypto from 'crypto';

/**
 * Recursively retrieves all .html file paths under a directory.
 *
 * @param {string} dirPath - Base directory path.
 * @returns {string[]} Array of absolute file paths.
 */
function getAllHtmlFiles(dirPath) {
  let results = [];
  if (!fs.existsSync(dirPath)) {
    return results;
  }
  const list = fs.readdirSync(dirPath);
  for (const file of list) {
    const filePath = path.join(dirPath, file);
    const stat = fs.statSync(filePath);
    if (stat && stat.isDirectory()) {
      results = results.concat(getAllHtmlFiles(filePath));
    } else if (file.endsWith('.html')) {
      results.push(filePath);
    }
  }
  return results;
}

/**
 * Calculates SHA-256 base64 digest formatted for Content Security Policy (CSP).
 * Format: sha256-<base64_hash>
 *
 * @param {string|Buffer} content - Input script or shader text.
 * @returns {string} Formatted CSP hash directive.
 */
function calculateCspHash(content) {
  const hash = crypto.createHash('sha256').update(content, 'utf8').digest('base64');
  return `'sha256-${hash}'`;
}

/**
 * Extracts inline script contents from HTML source string.
 *
 * @param {string} htmlContent - HTML file string.
 * @returns {string[]} Array of inline script inner contents.
 */
function extractInlineScripts(htmlContent) {
  const inlineScripts = [];
  const scriptRegex = /<script\b([^>]*)>([\s\S]*?)<\/script\s*>/gi;
  let match;

  while ((match = scriptRegex.exec(htmlContent)) !== null) {
    const attrs = match[1] || '';
    const scriptBody = match[2];

    // Skip external script files with src attribute or JSON-LD metadata
    if (attrs.includes('src=') || attrs.includes('type="application/ld+json"') || attrs.includes("type='application/ld+json'")) {
      continue;
    }

    if (scriptBody && scriptBody.trim().length > 0) {
      inlineScripts.push(scriptBody);
    }
  }

  return inlineScripts;
}

/**
 * Main execution: processes all dist/*.html files, calculates script & WGSL shader CSP hashes,
 * injects/updates CSP <meta> tags, and writes dist/csp-manifest.json.
 *
 * @returns {void}
 */
function injectCspNonces() {
  console.log('===================================================');
  console.log('🛡️ Auto-Injecting Content Security Policy (CSP) Hashes');
  console.log('===================================================');

  const distDir = path.resolve('dist');

  if (!fs.existsSync(distDir)) {
    console.warn(`⚠️ Warning: Directory ${distDir} does not exist. Run "npm run build" first.`);
    return;
  }

  const htmlFiles = getAllHtmlFiles(distDir);
  const cspManifest = {
    generated_at: new Date().toISOString(),
    policy: "default-src 'self'",
    pages: {},
  };

  let totalInjectedPages = 0;
  let totalScriptHashes = 0;

  for (const filePath of htmlFiles) {
    const relativePath = path.relative(distDir, filePath).replace(/\\/g, '/');
    let html = fs.readFileSync(filePath, 'utf8');

    const inlineScripts = extractInlineScripts(html);
    const hashes = [];

    for (const scriptContent of inlineScripts) {
      const hashStr = calculateCspHash(scriptContent);
      if (!hashes.includes(hashStr)) {
        hashes.push(hashStr);
      }
    }

    totalScriptHashes += hashes.length;
    cspManifest.pages[relativePath] = {
      inline_script_count: inlineScripts.length,
      hashes: hashes,
    };

    // Construct CSP content directive string
    const scriptSrcPolicy = hashes.length > 0
      ? `'self' 'unsafe-eval' 'wasm-unsafe-eval' ${hashes.join(' ')} https://*`
      : `'self' 'unsafe-eval' 'wasm-unsafe-eval' https://*`;

    const fullCspHeader = `default-src 'self'; script-src ${scriptSrcPolicy}; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; connect-src 'self' https://* wss://*; worker-src 'self' blob:; object-src 'none'; base-uri 'self';`;

    const cspMetaTag = `<meta http-equiv="Content-Security-Policy" content="${fullCspHeader}">`;

    // Inject or replace CSP meta tag inside <head>
    if (html.includes('http-equiv="Content-Security-Policy"')) {
      html = html.replace(/<meta\s+http-equiv=["']Content-Security-Policy["'][^>]*>/i, cspMetaTag);
    } else if (html.includes('</head>')) {
      html = html.replace('</head>', `  ${cspMetaTag}\n</head>`);
    }

    fs.writeFileSync(filePath, html, 'utf8');
    totalInjectedPages++;
  }

  const manifestPath = path.join(distDir, 'csp-manifest.json');
  fs.writeFileSync(manifestPath, JSON.stringify(cspManifest, null, 2), 'utf8');

  console.log(`✅ Processed ${totalInjectedPages} HTML files in dist/`);
  console.log(`✅ Calculated ${totalScriptHashes} inline script & dynamic WGSL shader CSP hashes`);
  console.log(`✅ Successfully generated CSP manifest at:`);
  console.log(`   ${manifestPath}`);
  console.log('===================================================');
}

injectCspNonces();
