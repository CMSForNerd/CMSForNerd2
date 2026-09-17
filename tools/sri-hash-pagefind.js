/**
 * @file sri-hash-pagefind.js
 * @description Automated Subresource Integrity (SRI) auto-hashing utility for Pagefind WebAssembly
 * binaries and client bundle assets in static distribution builds (dist/pagefind/).
 * Computes base64-encoded SHA-384 hashes for all Pagefind .wasm, .js, and .css assets and
 * outputs a compliant manifest file at dist/pagefind/pagefind-sri.json.
 */

import fs from 'fs';
import path from 'path';
import crypto from 'crypto';

/**
 * Recursively retrieves all file paths under a directory.
 *
 * @param {string} dirPath - Base directory path.
 * @returns {string[]} Array of absolute file paths.
 */
function getAllFiles(dirPath) {
  let results = [];
  if (!fs.existsSync(dirPath)) {
    return results;
  }
  const list = fs.readdirSync(dirPath);
  for (const file of list) {
    const filePath = path.join(dirPath, file);
    const stat = fs.statSync(filePath);
    if (stat && stat.isDirectory()) {
      results = results.concat(getAllFiles(filePath));
    } else {
      results.push(filePath);
    }
  }
  return results;
}

/**
 * Calculates SHA-384 Subresource Integrity (SRI) hash string for a file buffer.
 * Format: sha384-<base64_encoded_digest>
 *
 * @param {Buffer} buffer - File buffer content.
 * @returns {string} SRI formatted hash string.
 */
function calculateSriHash(buffer) {
  const hash = crypto.createHash('sha384').update(buffer).digest('base64');
  return `sha384-${hash}`;
}

/**
 * Scans dist/pagefind/, computes cryptographic SRI hashes, and outputs dist/pagefind/pagefind-sri.json.
 *
 * @returns {void}
 */
function generatePagefindSriHashes() {
  console.log('===================================================');
  console.log('🔒 Generating Subresource Integrity (SRI) Hashes');
  console.log('===================================================');

  const pagefindDir = path.resolve('dist/pagefind');

  if (!fs.existsSync(pagefindDir)) {
    console.warn(`⚠️ Warning: Directory ${pagefindDir} does not exist. Run "npm run build" first.`);
    return;
  }

  const allFiles = getAllFiles(pagefindDir);
  const sriManifest = {
    generated_at: new Date().toISOString(),
    algorithm: 'sha384',
    files: {},
  };

  let hashedCount = 0;

  for (const filePath of allFiles) {
    const relativePath = path.relative(pagefindDir, filePath).replace(/\\/g, '/');
    const ext = path.extname(filePath).toLowerCase();

    // Hash .wasm, .js, and .css files
    if (['.wasm', '.js', '.css'].includes(ext)) {
      const fileBuffer = fs.readFileSync(filePath);
      const sriHash = calculateSriHash(fileBuffer);
      sriManifest.files[relativePath] = sriHash;
      hashedCount++;
      console.log(`  ✓ ${relativePath}: ${sriHash.substring(0, 24)}...`);
    }
  }

  const manifestPath = path.join(pagefindDir, 'pagefind-sri.json');
  fs.writeFileSync(manifestPath, JSON.stringify(sriManifest, null, 2), 'utf8');

  console.log(`✅ Successfully generated SRI manifest with ${hashedCount} entries at:`);
  console.log(`   ${manifestPath}`);
  console.log('===================================================');
}

generatePagefindSriHashes();
