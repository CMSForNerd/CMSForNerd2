/**
 * @file tools/validate-mermaid.js
 * @description Headless Mermaid diagram syntax validator for Markdown files.
 * Uses jsdom, DOMPurify, and the official Mermaid parser to validate all embedded mermaid blocks.
 *
 * @author Repository Architect & OKF v0.2 Compliance Agent
 * @license GNU General Public License v3.0
 */

import fs from 'node:fs';
import path from 'node:path';
import { JSDOM } from 'jsdom';
import createDOMPurify from 'dompurify';
import mermaid from 'mermaid';

// Initialize headless JSDOM environment for Mermaid parser
const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>', {
  url: 'http://localhost/',
});

globalThis.window = dom.window;
globalThis.document = dom.window.document;

if (!globalThis.navigator || !globalThis.navigator.userAgent) {
  Object.defineProperty(globalThis, 'navigator', {
    value: dom.window.navigator,
    writable: true,
    configurable: true,
  });
}

// Bind DOMPurify instance to window and factory for Mermaid internal sanitizer
const dompurify = createDOMPurify(dom.window);
Object.assign(createDOMPurify, dompurify);

dom.window.DOMPurify = dompurify;
globalThis.DOMPurify = dompurify;

mermaid.initialize({
  startOnLoad: false,
  suppressErrorRendering: true,
  securityLevel: 'loose',
});

const EXCLUDE_DIRS = new Set(['node_modules', '.git', 'dist', '.astro', '.pytest_cache']);

/**
 * Recursively find all Markdown (.md) files in the directory.
 *
 * @param {string} dirPath - Directory to search.
 * @returns {string[]} Array of absolute file paths.
 */
function getMarkdownFiles(dirPath) {
  let results = [];
  const entries = fs.readdirSync(dirPath, { withFileTypes: true });

  for (const entry of entries) {
    if (EXCLUDE_DIRS.has(entry.name)) {
      continue;
    }
    const fullPath = path.join(dirPath, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(getMarkdownFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      results.push(fullPath);
    }
  }
  return results;
}

/**
 * Extract Mermaid diagram blocks from Markdown content.
 *
 * @param {string} content - Markdown file content.
 * @returns {string[]} Array of Mermaid diagram code strings.
 */
function extractMermaidBlocks(content) {
  const regex = /```mermaid\r?\n([\s\S]*?)```/gi;
  const blocks = [];
  let match;
  while ((match = regex.exec(content)) !== null) {
    blocks.push(match[1].trim());
  }
  return blocks;
}

/**
 * Main validation execution function.
 */
async function main() {
  const rootDir = process.cwd();
  const mdFiles = getMarkdownFiles(rootDir);
  console.log(`🔍 [Mermaid Validator] Scanning ${mdFiles.length} Markdown files for Mermaid diagrams...`);

  let totalDiagrams = 0;
  let errorCount = 0;

  for (const filePath of mdFiles) {
    const relPath = path.relative(rootDir, filePath);
    const content = fs.readFileSync(filePath, 'utf-8');
    const blocks = extractMermaidBlocks(content);

    if (blocks.length === 0) {
      continue;
    }

    for (let i = 0; i < blocks.length; i++) {
      const block = blocks[i];
      totalDiagrams++;
      try {
        await mermaid.parse(block);
      } catch (err) {
        errorCount++;
        console.error(`❌ [Mermaid Syntax Error] File: ${relPath} (Diagram #${i + 1})`);
        console.error(`Message: ${err.message || err}`);
        console.error(`--- Code Snippet ---\n${block}\n--------------------`);
      }
    }
  }

  console.log(`\n📊 Validation Summary: Checked ${totalDiagrams} Mermaid diagrams across ${mdFiles.length} files.`);
  if (errorCount > 0) {
    console.error(`❌ Validation Failed: ${errorCount} invalid Mermaid diagram(s) detected.`);
    process.exit(1);
  } else {
    console.log(`✅ All ${totalDiagrams} Mermaid diagrams passed syntax validation cleanly!`);
  }
}

main().catch((err) => {
  console.error('Fatal execution error in Mermaid validator:', err);
  process.exit(1);
});
