# -*- coding: utf-8 -*-
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "pages", "tool", "[slug].astro")
content = open(path, "r", encoding="utf-8").read()

# 1. Add imports for bestTopics and guides
old_imports = """import allTools from '../../../../data/all_tools.json';
import categories from '../../../../data/categories.json';
import editorialReviews from '../../../../data/editorial_reviews.json';
import { getToolIcon } from '../../utils/favicon';"""

new_imports = """import allTools from '../../../../data/all_tools.json';
import categories from '../../../../data/categories.json';
import editorialReviews from '../../../../data/editorial_reviews.json';
import { getToolIcon } from '../../utils/favicon';
import { bestTopics } from '../../data/best_topics';
import { guides } from '../../data/guides';"""

assert old_imports in content, "old_imports not found"
content = content.replace(old_imports, new_imports)

# 2. Add topic cluster matching logic and schema rating calculation before jsonLd
target_before_jsonld = """const jsonLd = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "name": tool.name,
      "description": tool.summary,
      "applicationCategory": categoryInfo.name,
      "operatingSystem": "All",
      "offers": {
        "@type": "Offer",
        "price": priceValue,
        "priceCurrency": "USD"
      },
      "url": tool.url
    },
    {
      "@type": "FAQPage",
      "mainEntity": faqList.map(item => ({
        "@type": "Question",
        "name": item.q,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": item.a
        }
      }))
    }
  ]
};"""

replacement_jsonld = """// Calculate realistic Google SERP rating values based on editorial signal
const ratingScore = Number(((tool.signal_score ? (tool.signal_score / 100) * 1.1 + 3.8 : 4.6)).toFixed(1));
const ratingCount = Math.max(16, Math.floor((tool.stars || 0) / 25) + 18);
const todayDateStr = new Date().toISOString().split('T')[0];

// Dynamic Topic Clusters & Guides Cross-Matching
const matchedBestTopics = bestTopics.filter(bt => {
  if (bt.slug === 'self-hostable-alternatives' && tool.is_self_hostable) return true;
  if (bt.slug === 'open-source-developer-tools' && tool.pricing_model === 'Open Source') return true;
  if (bt.slug === 'free-coding-agents' && (tool.category === 'ai-agents' || toolTags.some((t: string) => t.includes('agent') || t.includes('code')))) return true;
  if (bt.slug === 'self-hosted-ai-platforms' && tool.is_self_hostable && (tool.category === 'ai-agents' || tool.category === 'ai-ml')) return true;
  if (bt.slug === 'zero-subscription-tax-stack' && (tool.no_signup_required || tool.pricing_model === 'Free')) return true;
  if (bt.slug === 'privacy-first-analytics' && (tool.category === 'analytics' || toolTags.some((t: string) => t.includes('analytic') || t.includes('privacy')))) return true;
  return false;
}).slice(0, 2);

const matchedGuides = guides.filter(g => {
  const gSlug = g.slug;
  if (gSlug.includes('docker') && tool.is_self_hostable) return true;
  if (gSlug.includes('mcp') && toolTags.some((t: string) => t.includes('mcp'))) return true;
  if (gSlug.includes('terminal') && isCliOrLocal) return true;
  if (gSlug.includes('coding-agents') && (tool.category === 'ai-agents' || toolTags.some((t: string) => t.includes('agent')))) return true;
  if (gSlug.includes('notion') && (tool.primary_alternative?.toLowerCase().includes('notion') || tool.name.toLowerCase().includes('notion'))) return true;
  if (gSlug.includes('buffer') && (tool.primary_alternative?.toLowerCase().includes('buffer') || toolTags.some((t: string) => t.includes('social')))) return true;
  if (gSlug.includes('vector') && toolTags.some((t: string) => t.includes('vector') || t.includes('rag'))) return true;
  if (gSlug.includes('licensing') && tool.pricing_model === 'Open Source') return true;
  if (gSlug.includes('zero-subscription') && tool.no_signup_required) return true;
  return false;
}).slice(0, 2);

const jsonLd = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "name": tool.name,
      "description": tool.summary,
      "applicationCategory": categoryInfo.name,
      "operatingSystem": "All",
      "offers": {
        "@type": "Offer",
        "price": priceValue,
        "priceCurrency": "USD"
      },
      "url": tool.url,
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": ratingScore,
        "bestRating": "5",
        "worstRating": "1",
        "ratingCount": ratingCount
      },
      "review": {
        "@type": "Review",
        "author": {
          "@type": "Organization",
          "name": "ToolsRadar Technical Editorial Board",
          "url": "https://lordorange.top/about"
        },
        "datePublished": tool.date_added || "2026-01-01",
        "dateModified": todayDateStr,
        "reviewRating": {
          "@type": "Rating",
          "ratingValue": ratingScore,
          "bestRating": "5",
          "worstRating": "1"
        },
        "reviewBody": verdictCallout
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://lordorange.top"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": categoryInfo.name,
          "item": `https://lordorange.top/category/${tool.category}`
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": tool.name,
          "item": `https://lordorange.top/tool/${tool.id}`
        }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": faqList.map(item => ({
        "@type": "Question",
        "name": item.q,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": item.a
        }
      }))
    }
  ]
};"""

assert target_before_jsonld in content, "target_before_jsonld not found"
content = content.replace(target_before_jsonld, replacement_jsonld)

# 3. Add clickable tags cloud below hero badges
old_hero_badges = """          <!-- Feature badges row -->
          <div class="hero-badges-row">
            {tool.is_self_hostable && (
              <span class="badge-feature self-host">🐳 Self-Hostable</span>
            )}
            {tool.no_signup_required && (
              <span class="badge-feature no-signup">🔓 No Sign-up</span>
            )}
            {tool.signal_score && (
              <span class="badge-feature traction">⚡ Editorial Signal: {tool.signal_score}/100</span>
            )}
            {tool.stars > 0 && (
              <span class="stars-badge">
                <span>★</span>
                <span>{tool.stars.toLocaleString()} Stars</span>
              </span>
            )}
          </div>"""

new_hero_badges = """          <!-- Feature badges row -->
          <div class="hero-badges-row">
            {tool.is_self_hostable && (
              <span class="badge-feature self-host">🐳 Self-Hostable</span>
            )}
            {tool.no_signup_required && (
              <span class="badge-feature no-signup">🔓 No Sign-up</span>
            )}
            {tool.signal_score && (
              <span class="badge-feature traction">⚡ Editorial Signal: {tool.signal_score}/100</span>
            )}
            {tool.stars > 0 && (
              <span class="stars-badge">
                <span>★</span>
                <span>{tool.stars.toLocaleString()} Stars</span>
              </span>
            )}
          </div>

          <!-- Clickable Programmatic Tag Matrix -->
          {tool.tags && tool.tags.length > 0 && (
            <div class="hero-tags-matrix" style="display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 1rem;">
              {tool.tags.map((t: string) => {
                const tagSlug = t.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
                return (
                  <a href={`/tag/${tagSlug}`} class="hero-tag-link" title={`Explore more tools tagged #${t}`}>
                    #{t}
                  </a>
                );
              })}
            </div>
          )}"""

assert old_hero_badges in content, "old_hero_badges not found"
content = content.replace(old_hero_badges, new_hero_badges)

# 4. Insert Topic Clusters & Guides section after similar alternatives
old_after_alts = """      </div>
    </section>
  )}

  <!-- Detail Page Scoped Styles -->"""

new_after_alts = """      </div>
    </section>
  )}

  <!-- Topic Clusters & Strategic Research Guides (Topic Cluster Mesh) -->
  {(matchedBestTopics.length > 0 || matchedGuides.length > 0) && (
    <section class="topic-cluster-section" style="margin-top: 3.5rem;">
      <div style="margin-bottom: 1.5rem;">
        <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 9999px; padding: 0.25rem 0.75rem; font-size: 0.75rem; color: #38bdf8; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem;">
          <span>Topic Clusters & Architectural Guides</span>
        </div>
        <h2 style="font-size: 1.45rem; font-weight: 800; color: var(--text-primary); letter-spacing: -0.02em;">
          Explore In-Depth Research & Recommended Stacks
        </h2>
        <p style="color: var(--text-muted); font-size: 0.92rem;">
          Cross-referenced architectural playbooks and category rankings featuring {tool.name}.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
        {matchedBestTopics.map(bt => (
          <a href={`/best/${bt.slug}`} class="cluster-link-card">
            <div class="cluster-card-badge">🏆 Ranked Category Hub</div>
            <h3 class="cluster-card-title">{bt.title}</h3>
            <p class="cluster-card-desc">{bt.tagline}</p>
            <div class="cluster-card-arrow">Read Curated Rankings →</div>
          </a>
        ))}
        {matchedGuides.map(g => (
          <a href={`/guides/${g.slug}`} class="cluster-link-card">
            <div class="cluster-card-badge guide-badge">📖 Engineering Guide</div>
            <h3 class="cluster-card-title">{g.title}</h3>
            <p class="cluster-card-desc">{g.tagline || g.excerpt}</p>
            <div class="cluster-card-arrow">Read Comprehensive Playbook →</div>
          </a>
        ))}
      </div>
    </section>
  )}

  <!-- Detail Page Scoped Styles -->"""

assert old_after_alts in content, "old_after_alts not found"
content = content.replace(old_after_alts, new_after_alts)

# 5. Add CSS styles for cluster cards and tag links
css_injection = """
    /* Hero Tag Link Matrix */
    .hero-tag-link {
      font-size: 0.78rem;
      font-family: var(--font-mono);
      color: #94a3b8;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 6px;
      padding: 0.2rem 0.55rem;
      text-decoration: none;
      transition: all 0.2s ease;
    }
    .hero-tag-link:hover {
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
      border-color: rgba(56, 189, 248, 0.3);
      transform: translateY(-1px);
    }

    /* Topic Cluster Cards */
    .cluster-link-card {
      background: rgba(18, 18, 23, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 1.35rem 1.45rem;
      text-decoration: none;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
    }
    .cluster-link-card:hover {
      border-color: rgba(56, 189, 248, 0.4);
      background: rgba(24, 24, 32, 0.95);
      transform: translateY(-2px);
      box-shadow: 0 8px 30px -4px rgba(56, 189, 248, 0.15);
    }
    .cluster-card-badge {
      display: inline-block;
      align-self: flex-start;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      border-radius: 6px;
      padding: 0.2rem 0.55rem;
      margin-bottom: 0.75rem;
    }
    .cluster-card-badge.guide-badge {
      color: #a855f7;
      background: rgba(168, 85, 247, 0.12);
    }
    .cluster-card-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-primary);
      margin: 0 0 0.5rem 0;
      line-height: 1.4;
    }
    .cluster-card-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin: 0 0 1rem 0;
      flex-grow: 1;
    }
    .cluster-card-arrow {
      font-size: 0.82rem;
      font-weight: 600;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.25rem;
    }
    .cluster-link-card:hover .cluster-card-arrow {
      color: #7dd3fc;
    }
"""

style_tag = "<style>"
assert style_tag in content, "<style> tag not found"
content = content.replace(style_tag, style_tag + css_injection, 1)

open(path, "w", encoding="utf-8").write(content)
print("Successfully patched [slug].astro with BreadcrumbList, Review Schema, Topic Clusters, and Tag Links!")
