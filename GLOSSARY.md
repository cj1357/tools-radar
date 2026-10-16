# ToolsRadar Domain Glossary

This document defines the canonical ubiquitous language and domain model for **ToolsRadar** (`lordorange.top`). All codebase identifiers, page copies, and architecture decisions adhere to these terms.

---

## Core Entities & Concepts

### 1. Radar Engine (雷达引擎)
The automated, continuous ingestion and telemetry pipeline that scans GitHub Trending, Hacker News Show, and Product Hunt every 24 hours to discover and record software releases.

### 2. Tool Entry (工具实体)
A structured profile of a software project cataloged in the database (`all_tools.json`). Each entry contains identity metadata (`id`, `name`, `tagline`, `summary`), licensing (`pricing_model`), operational traits (`is_self_hostable`, `no_signup_required`), benchmark data (`signal_score`, `stars`), and installation recipes.

### 3. Alternative Pair (替代映射)
A domain relationship mapping a high-cost, proprietary commercial SaaS application (e.g. *Notion, Airtable, Datadog*) to a privacy-first, open-source, or self-hostable counterpart (e.g. *AppFlowy, NocoDB, GlitchTip*).

### 4. Traction Signal Score (信号分 / 综合热度)
A normalized 0–100 metric calculated from repository star acceleration, commit frequency, community discussions, and release cadence. Indicates whether a project has sustainable engineering vitality.

### 5. Hands-on Scorecard (上手度评测报告)
A standardized 4-dimension benchmark assessment displayed on tool detail pages:
- **Setup & Onboarding (安装与上手度)**: Ease of deployment (Docker, single binary, or zero sign-up).
- **Code & Auditability (代码透明度)**: Open-source licensing and code visibility.
- **Maintenance & Vitality (生态活跃度)**: Commit frequency and community health.
- **Cost / Value Advantage (成本优势)**: Free tier and TCO advantage over commercial SaaS.

### 6. Technical Guide (深度技术指南 / 白皮书)
A long-form (1,500+ words), peer-reviewed architectural article or comparison analysis published under `/guides` to provide deep technical context beyond raw card listings.

### 7. Spotlight / Editor's Pick (编辑精选 / 今日焦点)
A featured, high-impact tool selected daily or weekly to receive hero placement, in-depth architectural commentary, and interactive showcase treatment.

### 8. Collection / Battleground (专题集合)
A curated thematic group of tools addressing a specific engineering workflow (e.g., *Modern Rust CLI Suite*, *Self-Hosted Cloud PaaS*, *Autonomous Coding Agents*).
