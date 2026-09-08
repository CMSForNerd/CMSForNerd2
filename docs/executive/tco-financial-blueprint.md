---
type: "documentation"
title: "36-Month TCO & Financial Blueprint"
description: "Complete 36-month total cost of ownership analysis, non-AWS operational overheads, and quarterly OpEx cost projections."
topics: ["financial", "tco", "costing", "opex", "executive"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: docs/executive/tco-financial-blueprint.md
  url: docs/executive/tco-financial-blueprint.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-08-01T12:00:00Z'
tags: ["financial", "tco", "costing", "opex", "executive"]
---

`[STRATEGIC FINANCIAL]` — C-Suite & Project Managers

# 36-Month TCO & Financial Blueprint

This document presents the comprehensive 36-Month Total Cost of Ownership (TCO) and financial model for the infrastructure deployment.

---

## 💰 Financial Overview

- **36-Month TCO Total:** $92,509.78 USD ($\sim\text{RM } 416,294.01$)
- **Average Monthly OpEx:** $2,569.72 USD
- **AWS Direct Cloud Spend Allocation:** 65%
- **Non-AWS Operational Overheads Allocation:** 35%

---

## 📊 Cost Breakdown & Non-AWS Operational Overheads

The TCO model incorporates direct cloud resources alongside non-AWS operational costs:

1. **Cloud Infrastructure (AWS AP-Southeast-5):**
   - Compute (EC2 Graviton t4g series)
   - Database (RDS PostgreSQL / Percona)
   - Networking & WAF (Application Load Balancers, Route 53, WAFv2)
   - Persistent Storage (AWS EFS & S3 Backups)

2. **Non-AWS Operational Overheads:**
   - On-premises hardware maintenance and local backup nodes
   - Compliance auditing, security posture assessments (SPA), and vulnerability scanning
   - Technical support, licensing, and domain management

---

## 📈 Quarterly OpEx Curves

Operating expenses follow a phased adoption curve:

- **Year 1 (Q1 - Q4):** Baseline setup, migration, and initial optimization phase.
- **Year 2 (Q5 - Q8):** Steady-state operations with reserved instance capacity cost optimizations.
- **Year 3 (Q9 - Q12):** Scaled operations and automated governance.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
