# ToolsRadar - Automated Tech Radar & Curated Directory

A fully automated, zero-maintenance trending tool directory and SEO pipeline designed for indie hackers and developers.

## 🏗️ Architecture

```
GitHub Trending / Hacker News / Product Hunt
                     │
                     ▼
         scripts/scraper.py (Python)
                     │
                     ▼
         data/tools/YYYY-MM-DD.json
         data/all_tools.json
                     │
                     ▼
            site/ (Astro SSG)
                     │
                     ▼
       Cloudflare Pages (Global Edge CDN)
```

- **Daily Crawl**: Powered by GitHub Actions (`.github/workflows/daily-scraper.yml`) running at 00:00 UTC.
- **Frontend**: Astro v7 generating 100% static HTML, ultra-lightweight and SEO-optimized.
- **Pages Generated**:
  - `/` - Homepage with today's drops and category filters.
  - `/category/[slug]` - Vertical category index pages for high-volume keywords.
  - `/tool/[slug]` - Dedicated landing pages for each tool with Schema.org `SoftwareApplication` JSON-LD.
  - `/daily/[date]` - Daily archive feeds for fast search engine recrawling.
  - `/about` & `/privacy` - Essential policy and E-E-A-T trust signals.

## 🚀 Local Development

### 1. Run Scraper
```bash
python scripts/scraper.py
```

### 2. Run Site Locally
```bash
cd site
npm run dev
```

### 3. Build Static Files
```bash
cd site
npm run build
```
Output will be generated in `site/dist/`.

## 🌐 Cloudflare Pages Deployment

1. Go to the [Cloudflare Dashboard](https://dash.cloudflare.com/) -> **Workers & Pages** -> **Create application** -> **Pages** -> **Connect to Git**.
2. Select repository `tools-radar`.
3. Set the build configuration:
   - **Framework preset**: `Astro`
   - **Root directory**: `site`
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
4. Bind your custom subdomain (e.g. `tools.yourdomain.com`).
5. (Optional) In GitHub Repository Secrets, add `GEMINI_API_KEY` or `DEEPSEEK_API_KEY` for LLM-enhanced summaries.
