import re

# 1. Update Layout.astro with /vs link
with open("site/src/layouts/Layout.astro", "r", encoding="utf-8") as f:
    layout_content = f.read()

# Add to desktop nav
if '<li><a href="/vs">Comparisons</a></li>' not in layout_content:
    layout_content = layout_content.replace(
        '<li><a href="/guides">Guides</a></li>',
        '<li><a href="/guides">Guides</a></li>\n          <li><a href="/vs">Comparisons</a></li>'
    )

# Add to mobile drawer
if '<a href="/vs" class="mobile-nav-item"' not in layout_content:
    layout_content = layout_content.replace(
        '<a href="/guides" class="mobile-nav-item"',
        '<a href="/vs" class="mobile-nav-item" style="color: #38bdf8; font-weight: 600;">⚡ Head-to-Head Comparisons</a>\n        <a href="/guides" class="mobile-nav-item"'
    )

# Add to footer
if '<li><a href="/vs">Head-to-Head Comparisons</a></li>' not in layout_content:
    layout_content = layout_content.replace(
        '<li><a href="/guides">Technical Guides Hub</a></li>',
        '<li><a href="/vs">Head-to-Head Comparisons</a></li>\n              <li><a href="/guides">Technical Guides Hub</a></li>'
    )

with open("site/src/layouts/Layout.astro", "w", encoding="utf-8") as f:
    f.write(layout_content)
print("Updated Layout.astro with /vs links.")

# 2. Update tool/[slug].astro
with open("site/src/pages/tool/[slug].astro", "r", encoding="utf-8") as f:
    tool_content = f.read()

# Add comparisonPairSlug definition if not present
if "comparisonPairSlug" not in tool_content:
    target_pos = tool_content.find("const pageTitle =")
    slug_code = """const altClean = tool.primary_alternative?.trim() || '';
const altSlug = altClean ? altClean.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') : '';
const comparisonPairSlug = (altSlug && altSlug !== tool.id) ? `${tool.id}-vs-${altSlug}` : null;

"""
    tool_content = tool_content[:target_pos] + slug_code + tool_content[target_pos:]

# Add Head-to-Head Banner & Badge Box after FAQ section
badge_and_banner_markup = """
  <!-- Head-to-Head Comparison Callout Banner -->
  {comparisonPairSlug && (
    <section class="head-to-head-banner" style="margin-top: 2.5rem; background: linear-gradient(135deg, rgba(56, 189, 248, 0.08) 0%, rgba(168, 85, 247, 0.08) 100%); border: 1px solid rgba(56, 189, 248, 0.28); border-radius: 14px; padding: 1.5rem 1.75rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.25rem;">
      <div style="max-width: 650px;">
        <div style="display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; color: #38bdf8; margin-bottom: 0.35rem;">
          <span>⚡ HEAD-TO-HEAD MATRIX</span>
        </div>
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin: 0 0 0.3rem;">
          Compare {tool.name} vs {altClean}
        </h3>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin: 0; line-height: 1.5;">
          Review our 2026 architectural breakdown comparing licensing, self-hosting ease, data sovereignty, and total cost of ownership.
        </p>
      </div>
      <a href={`/vs/${comparisonPairSlug}`} class="btn btn-primary" style="padding: 0.7rem 1.4rem; font-size: 0.9rem; font-weight: 700; white-space: nowrap;">
        View Comparison Dossier →
      </a>
    </section>
  )}

  <!-- Official ToolsRadar Verification Badge Card -->
  <section class="official-badge-card" style="margin-top: 2.5rem; background: #0c1018; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 1.75rem;">
    <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.75rem;">
      <span style="font-size: 1.25rem;">🏅</span>
      <h3 style="font-size: 1.2rem; font-weight: 800; color: #ffffff; margin: 0;">
        Official ToolsRadar Verification Badge
      </h3>
    </div>
    <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 1.25rem; max-width: 760px;">
      Maintainers of <strong>{tool.name}</strong> and community advocates can display this real-time verification badge in your GitHub README, official documentation, or landing page.
    </p>

    <div style="display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 1.25rem; padding: 1rem 1.25rem; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 10px;">
      <div>
        <span style="font-size: 0.72rem; font-weight: 700; letter-spacing: 0.06em; color: #64748b; display: block; margin-bottom: 0.35rem;">LIVE BADGE PREVIEW</span>
        <img 
          src={`/badge/${tool.id}.svg`} 
          alt={`${tool.name} ToolsRadar Signal Badge`} 
          width="230" 
          height="38" 
          style="display: block; border-radius: 8px;"
        />
      </div>
      <div style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5;">
        <span>✓ Real-time Signal Score ({tool.signal_score || 95}/100)</span><br/>
        <span>✓ Clean SVG vector format (Retina & Dark-mode optimized)</span><br/>
        <span>✓ Permanent backlink to your curated dossier</span>
      </div>
    </div>

    <!-- Snippet Copy Tabs -->
    <div style="display: flex; flex-direction: column; gap: 0.75rem;">
      <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
          <span style="font-size: 0.78rem; font-weight: 700; color: #94a3b8;">Markdown (for GitHub README)</span>
          <button 
            type="button" 
            onclick={`navigator.clipboard.writeText('[![Featured on ToolsRadar](https://lordorange.top/badge/${tool.id}.svg)](https://lordorange.top/tool/${tool.id})'); this.innerText = 'Copied!'; setTimeout(() => this.innerText = 'Copy Markdown', 2000);`}
            style="background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3); color: #38bdf8; font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.65rem; border-radius: 4px; cursor: pointer;"
          >
            Copy Markdown
          </button>
        </div>
        <pre style="margin: 0; padding: 0.75rem 1rem; background: #05070c; border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #38bdf8; overflow-x: auto;"><code>{`[![Featured on ToolsRadar](https://lordorange.top/badge/${tool.id}.svg)](https://lordorange.top/tool/${tool.id})`}</code></pre>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
          <span style="font-size: 0.78rem; font-weight: 700; color: #94a3b8;">HTML Embed</span>
          <button 
            type="button" 
            onclick={`navigator.clipboard.writeText('<a href="https://lordorange.top/tool/${tool.id}" target="_blank"><img src="https://lordorange.top/badge/${tool.id}.svg" alt="Featured on ToolsRadar" /></a>'); this.innerText = 'Copied!'; setTimeout(() => this.innerText = 'Copy HTML', 2000);`}
            style="background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255, 255, 255, 0.12); color: #ffffff; font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.65rem; border-radius: 4px; cursor: pointer;"
          >
            Copy HTML
          </button>
        </div>
        <pre style="margin: 0; padding: 0.75rem 1rem; background: #05070c; border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #94a3b8; overflow-x: auto;"><code>{`<a href="https://lordorange.top/tool/${tool.id}" target="_blank"><img src="https://lordorange.top/badge/${tool.id}.svg" alt="Featured on ToolsRadar" /></a>`}</code></pre>
      </div>
    </div>
  </section>
"""

marker = "<!-- Similar Alternatives in Category -->"
if "official-badge-card" not in tool_content and marker in tool_content:
    tool_content = tool_content.replace(marker, badge_and_banner_markup + "\n  " + marker)

with open("site/src/pages/tool/[slug].astro", "w", encoding="utf-8") as f:
    f.write(tool_content)
print("Updated tool/[slug].astro with Badge Card & Comparison Callout.")
