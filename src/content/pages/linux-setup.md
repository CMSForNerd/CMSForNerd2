---
okf_version: 0.1
type: "content_page"
title: "Linux Setup Guide (Node.js & Astro) | CMSForNerd2 Lab"
description: "Official laboratory guide for installing Node.js 20+ and Astro 7.1 on Debian, Ubuntu LTS, and AlmaLinux."
schemaType: "HowTo"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="lab-worksheet linux-setup" itemscope itemtype="https://schema.org/HowTo">
<header class="setup-header">
<h1 itemprop="name">🐧 Linux Setup Guide: Laboratory Readiness</h1>
<p class="subtitle">Ensuring Node.js 20+ & Astro 7.1 Compatibility on Debian, Ubuntu LTS & AlmaLinux</p>
</header>

<div class="requirement-alert" role="alert">
<strong>RFC 2119 REQUIRED:</strong> To complete the laboratory modules, your development environment <strong>MUST</strong> run <strong>Node.js 20.0</strong> or higher to compile Astro 7.1.
</div>

<section class="os-selector">
<div class="os-block debian" itemprop="step">
<h2>📦 Option A: Debian & Ubuntu</h2>
<p>Using the official <strong>NodeSource</strong> repository to install the latest LTS version of Node.js.</p>

<div class="terminal-block">
<code># Install dependencies
sudo apt update && sudo apt install -y curl ca-certificates gnupg git
# Add NodeSource GPG Key and Repo
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
# Install Node.js
sudo apt update && sudo apt install -y nodejs
# Verify installations
node -v && npm -v</code>
</div>
</div>

<div class="os-block almalinux" itemprop="step">
<h2>📦 Option B: AlmaLinux (9+)</h2>
<p>Using the official DNF module streams to enable Node.js 20 on Red Hat-based environments.</p>

<div class="terminal-block">
<code># Enable Node.js 20 stream
sudo dnf module reset nodejs -y
sudo dnf module enable nodejs:20 -y
# Install Node.js, npm, and git
sudo dnf install -y nodejs npm git
# Verify installations
node -v && npm -v</code>
</div>
</div>
</section>

<section class="permissions" itemprop="step">
<h2>📂 Workspace Initialization</h2>
<p>Initialize the repository and install project-level node modules:</p>
<div class="terminal-block">
<code># Clone the workspace and enter directory
git clone https://github.com/CMSForNerd/CMSForNerd2.git
cd CMSForNerd2

# Install local dependencies
npm install --legacy-peer-deps

# Start Astro 7.1 dev server
npm run dev</code>
</div>
</section>

<footer class="standards-summary">
<h2>🎓 Linux Compliance Summary</h2>
<ul>
<li><strong>MUST:</strong> Deliver all package updates and npm commands via secure channels.</li>
<li><strong>REQUIRED:</strong> Run Node.js v20.0 or higher.</li>
<li><strong>SHOULD:</strong> Leverage Visual Studio Code with official Astro language extension support.</li>
</ul>
</footer>

<nav class="progress-nav">
<a href="/windows-setup" class="btn btn-secondary">&lt; Previous: Windows Setup</a>
<a href="/welcome-kit" class="btn btn-primary">Next: Student Welcome Kit &gt;</a>
</nav>
</article>

<style>
:root { --linux-green: #2ecc71; --terminal-bg: #1a1a1a; --linux-border: #ddd; }
.linux-setup { max-width: 950px; margin: 0 auto; line-height: 1.7; }
.setup-header h1 { color: var(--linux-green); border-bottom: 3px solid var(--linux-green); }
.subtitle { color: #666; font-style: italic; }
.requirement-alert { background: #e8f5e9; border: 1px solid #c8e6c9; padding: 15px; border-radius: 8px; margin: 20px 0; }
.os-selector { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 30px 0; }
.os-block { background: #fdfdfd; padding: 20px; border: 1px solid var(--linux-border); border-radius: 10px; }
.terminal-block { background: var(--terminal-bg); color: #a2f2a2; padding: 15px; border-radius: 6px; font-family: 'Consolas', monospace; margin: 15px 0; border-left: 5px solid var(--linux-green); overflow-x: auto; }
.terminal-block code { white-space: pre-wrap; word-break: break-all; }
.standards-summary { background: #f8f9fa; padding: 25px; border-radius: 12px; margin-top: 40px; }
.progress-nav { display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; }
.btn { padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; }
.btn-primary { background: var(--linux-green); color: white; }
.btn-secondary { background: #eee; color: #333; }
@media (max-width: 800px) { .os-selector { grid-template-columns: 1fr; } }
</style>