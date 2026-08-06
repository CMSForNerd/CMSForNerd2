const fs = require("fs");
const path = require("path");

// Recursively find all markdown files
function getMarkdownFiles(dir, files = []) {
  const list = fs.readdirSync(dir);
  for (const file of list) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      if (file !== "node_modules" && file !== ".git") {
        getMarkdownFiles(filePath, files);
      }
    } else {
      if (file.endsWith(".md")) {
        files.push(filePath);
      }
    }
  }
  return files;
}

// Quote value if it contains any special characters or if it is a string
function formatValue(key, value) {
  const lowerKey = key.toLowerCase();

  // Do not format version numbers as strings unless they were already strings
  if (lowerKey === "okf_version" || lowerKey === "okf-version") {
    const cleaned = value.replace(/['"]/g, "").trim();
    if (cleaned === "0.1") {
      return "0.1";
    }
    return `"${cleaned}"`;
  }

  // Format arrays: topics, tags, etc.
  if (value.startsWith("[") && value.endsWith("]")) {
    const inside = value.substring(1, value.length - 1).trim();
    if (!inside) {
      return "[]";
    }
    const elements = inside.split(",").map(el => el.trim());
    const quoted = elements.map(el => {
      let unwrapped = el;
      if ((unwrapped.startsWith('"') && unwrapped.endsWith('"')) || (unwrapped.startsWith("'") && unwrapped.endsWith("'"))) {
        unwrapped = unwrapped.substring(1, unwrapped.length - 1);
      }
      // Escape any nested double quotes
      const escaped = unwrapped.replace(/\\"/g, '"').replace(/"/g, '\\"');
      return `"${escaped}"`;
    });
    return `[${quoted.join(", ")}]`;
  }

  // Keep booleans unquoted
  if (value === "true" || value === "false") {
    return value;
  }

  // Otherwise, wrap string value in double quotes
  let unwrapped = value;
  if ((unwrapped.startsWith('"') && unwrapped.endsWith('"')) || (unwrapped.startsWith("'") && unwrapped.endsWith("'"))) {
    unwrapped = unwrapped.substring(1, unwrapped.length - 1);
  }

  // Escape nested quotes
  const escaped = unwrapped.replace(/\\"/g, '"').replace(/"/g, '\\"');
  return `"${escaped}"`;
}

function processFile(filePath) {
  const content = fs.readFileSync(filePath, "utf8");

  // Special case: README.md might be missing the front matter entirely
  if (path.basename(filePath) === "README.md" && !content.startsWith("---")) {
    console.log(`Adding missing OKF frontmatter to README.md`);
    const frontmatter = `---
okf_version: 0.1
type: "documentation"
title: "CMSForNerd2 (Modern HTML5 & CSS3 Static Edition)"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

`;
    fs.writeFileSync(filePath, frontmatter + content, "utf8");
    return;
  }

  if (!content.startsWith("---")) {
    console.log(`Skipping file without frontmatter starting on line 1: ${filePath}`);
    return;
  }

  const endIdx = content.indexOf("---", 3);
  if (endIdx === -1) {
    console.log(`Error: unclosed frontmatter in ${filePath}`);
    return;
  }

  const frontmatterText = content.substring(3, endIdx);
  const bodyText = content.substring(endIdx + 3);

  const lines = frontmatterText.split(/\r?\n/);
  const updatedLines = [];
  const parsedKeys = new Set();

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      updatedLines.push("");
      continue;
    }

    const colonIdx = line.indexOf(":");
    if (colonIdx === -1 || line.startsWith(" ")) {
      // Preserve comments, list items, multiline, or unrecognised structure as-is
      updatedLines.push(line);
      continue;
    }

    const key = line.substring(0, colonIdx).trim();
    const value = line.substring(colonIdx + 1).trim();

    parsedKeys.add(key.toLowerCase());

    if (value === "") {
      updatedLines.push(`${key}:`);
    } else {
      const formatted = formatValue(key, value);
      updatedLines.push(`${key}: ${formatted}`);
    }
  }

  // Validate and inject any missing required keys of OKF v0.1: okf_version, type, title, timestamp, topics
  if (!parsedKeys.has("okf_version") && !parsedKeys.has("okf-version")) {
    console.log(`Injecting missing okf_version in ${filePath}`);
    updatedLines.push("okf_version: 0.1");
  }

  if (!parsedKeys.has("type")) {
    console.log(`Injecting missing type in ${filePath}`);
    const defaultType = filePath.includes("src/content/pages") ? "content_page" : "documentation";
    updatedLines.push(`type: "${defaultType}"`);
  }

  if (!parsedKeys.has("title")) {
    console.log(`Injecting missing title in ${filePath}`);
    const nameWithoutExt = path.basename(filePath, ".md");
    const capitalized = nameWithoutExt.split(/[-_]/).map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(" ");
    updatedLines.push(`title: "${capitalized}"`);
  }

  if (!parsedKeys.has("timestamp")) {
    console.log(`Injecting missing timestamp in ${filePath}`);
    updatedLines.push('timestamp: "2026-08-01T12:00:00Z"');
  }

  if (!parsedKeys.has("topics") && !parsedKeys.has("tags")) {
    console.log(`Injecting missing topics in ${filePath}`);
    updatedLines.push('topics: ["documentation"]');
  }

  // Build new file contents
  // Clean up leading newlines in updated lines and ensure exact formatting
  let cleanFM = updatedLines.join("\n").replace(/^\n+/, "").replace(/\n+$/, "");
  const updatedContent = `---
${cleanFM}
---${bodyText}`;

  fs.writeFileSync(filePath, updatedContent, "utf8");
  console.log(`Refactored frontmatter: ${filePath}`);
}

function main() {
  const mdFiles = getMarkdownFiles(".");
  console.log(`Found ${mdFiles.length} markdown files.`);
  for (const file of mdFiles) {
    processFile(file);
  }
  console.log("Refactoring complete.");
}

main();
