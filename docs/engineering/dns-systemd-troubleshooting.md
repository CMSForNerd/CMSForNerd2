---
type: "documentation"
title: "DNS & systemd-resolved Troubleshooting Guide"
description: "Diagnostic procedures and resolution steps for systemd-resolved DNS resolution issues."
topics: ["dns", "systemd", "troubleshooting", "devops", "engineering"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: docs/engineering/dns-systemd-troubleshooting.md
  url: docs/engineering/dns-systemd-troubleshooting.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-08-01T12:00:00Z'
tags: ["dns", "systemd", "troubleshooting", "devops", "engineering"]
---

`[DEVOPS EXECUTION]` — Systems Engineers & SREs

# DNS & systemd-resolved Troubleshooting Guide

This guide outlines diagnostic protocols for diagnosing and fixing DNS name resolution issues controlled by `systemd-resolved`.

---

## 🔍 Diagnostic Workflow

1. **Verify service status:**
   ```bash
   systemctl status systemd-resolved
   ```

2. **Inspect current DNS server configurations:**
   ```bash
   resolvectl status
   ```

3. **Test name resolution explicitly:**
   ```bash
   resolvectl query example.com
   ```

---

## 🛠️ Remediation & Symlink Configuration

Ensure `/etc/resolv.conf` correctly links to the stub resolver:

```bash
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
sudo systemctl restart systemd-resolved
```

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
