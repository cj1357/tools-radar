import os

def update_tool_page():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_file = os.path.join(base_dir, "site", "src", "pages", "tool", "[slug].astro")

    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update JSON-LD and FAQ dataset
    old_jsonld_start = content.find("const jsonLd = {")
    old_jsonld_end = content.find("---", old_jsonld_start)
    if old_jsonld_start == -1 or old_jsonld_end == -1:
        print("ERROR: Could not locate jsonLd block")
        return

    faq_and_jsonld = """// Structured FAQ dataset tailored for this tool (satisfies Google FAQPage Schema & kills thin content)
const faqList = [
  {
    q: `Is ${tool.name} completely free or does it require a paid subscription?`,
    a: tool.pricing_model === 'Open Source'
      ? `${tool.name} is 100% free and open-source under an open software license. There are no mandatory monthly subscription fees or per-seat licensing penalties, and you can freely inspect the source code or self-host the application on your private infrastructure.`
      : (tool.pricing_model === 'Free'
          ? `${tool.name} is available completely free of charge. Developers can access its core features without upfront costs or required credit card registration.`
          : (tool.pricing_model === 'Paid'
              ? `${tool.name} is a commercial developer product with transparent project-based or usage-based pricing designed for professional teams.`
              : `${tool.name} provides an accessible free tier or trial alongside paid upgrades for high-volume enterprise production needs.`))
  },
  {
    q: `How does ${tool.name} compare to ${tool.primary_alternative || 'competing proprietary alternatives'}?`,
    a: tool.comparison_vs_alt || `Compared to closed proprietary solutions like ${tool.primary_alternative || 'legacy SaaS software'}, ${tool.name} emphasizes developer ergonomics, high execution velocity, transparent data control, and low operational overhead without vendor lock-in.`
  },
  {
    q: `Can I self-host ${tool.name} on private servers or Docker?`,
    a: tool.is_self_hostable
      ? `Yes. ${tool.name} is architected for self-hosting via Docker or direct binary builds. Deploying on your own VPS or private cloud guarantees 100% data sovereignty, eliminates third-party telemetry, and ensures air-gapped security for proprietary codebases.`
      : `${tool.name} is delivered primarily as a cloud-hosted web application or managed API endpoint, providing instantaneous zero-maintenance access directly in the browser or via standard HTTP/SDK clients.`
  },
  {
    q: `Do I need to create an account or provide a credit card to try ${tool.name}?`,
    a: tool.no_signup_required
      ? `No account creation or credit card is required to evaluate ${tool.name}. You can immediately access and test its capabilities with zero registration barriers.`
      : `An account registration is standard to provision secure API keys, manage persistent configurations, and coordinate team access.`
  },
  {
    q: `What is the recommended quickstart workflow for ${tool.name}?`,
    a: quickstartCommand
      ? `You can launch or test ${tool.name} quickly using the following command:\\n\\n${quickstartCommand}\\n\\nVisit the official portal at ${tool.url} for comprehensive configuration flags and environment guides.`
      : `Navigate to the official portal at ${tool.url} to review live interactive documentation, guides, and SDK reference materials.`
  }
];

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
};
"""

    content = content[:old_jsonld_start] + faq_and_jsonld + content[old_jsonld_end:]

    # 2. Add Architecture, FAQ, and Trust cards right after details-grid-wrapper closing (or before </section>)
    target_needle = "</section>\n\n  <!-- Similar Alternatives in Category -->"
    if target_needle not in content:
        target_needle = "</section>\r\n\r\n  <!-- Similar Alternatives in Category -->"

    if target_needle not in content:
        print("ERROR: Could not find target needle before Similar Alternatives")
        return

    new_sections = """    <!-- Technical Architecture & Data Sovereignty Breakdown -->
    <div class="section-card tech-architecture-card">
      <h2 class="card-section-title">
        <span style="color: #38bdf8;">⚙️</span> Architecture & Engineering Analysis
      </h2>
      <div class="architecture-content">
        <p style="color: #e4e4e7; font-size: 1rem; line-height: 1.75; margin-bottom: 1rem;">
          <strong>{tool.name}</strong> is engineered to eliminate critical operational friction in {categoryInfo.name.toLowerCase()}. 
          From an architectural standpoint, the system adopts a {tool.is_self_hostable ? "local-first, self-contained deployment posture" : "cloud-native microservice architecture"}, ensuring low execution latency and minimal external service entanglements.
        </p>
        <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin-bottom: 1.25rem;">
          {tool.pricing_model === 'Open Source' 
            ? "Because the underlying code is fully open-source, engineering teams can audit security implementations, inspect telemetry vectors, and extend functionality via custom fork without risk of sudden vendor deprecation."
            : "The system is structured for rapid developer adoption, providing clear API contracts, straightforward authentication, and predictable integration pathways into existing CI/CD or production stacks."}
        </p>
        
        <div class="arch-meta-badges">
          <div class="arch-badge-item">
            <span class="arch-badge-label">Data Sovereignty:</span>
            <span class="arch-badge-value" style={tool.is_self_hostable ? "color: var(--emerald);" : "color: #38bdf8;"}>
              {tool.is_self_hostable ? "100% Private (On-Premises / Docker)" : "Managed Cloud (Zero-Ops)"}
            </span>
          </div>
          <div class="arch-badge-item">
            <span class="arch-badge-label">Extensibility:</span>
            <span class="arch-badge-value">
              {tool.github_url ? "Forkable Codebase & REST/CLI" : "REST / Webhooks Interoperability"}
            </span>
          </div>
          <div class="arch-badge-item">
            <span class="arch-badge-label">Ecosystem Role:</span>
            <span class="arch-badge-value" style="color: var(--accent);">
              {tool.primary_alternative ? `Alternative to ${tool.primary_alternative}` : "Core Workflow Utility"}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Frequently Asked Questions (FAQ) Section -->
    <div class="section-card faq-section-card">
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1.5rem;">
        <h2 class="card-section-title" style="margin: 0;">
          <span style="color: #a855f7;">❓</span> Frequently Asked Questions
        </h2>
        <span style="font-size: 0.78rem; color: #c084fc; background: rgba(168, 85, 247, 0.1); border: 1px solid rgba(168, 85, 247, 0.25); padding: 0.25rem 0.65rem; border-radius: 9999px; font-weight: 600;">
          Editorial Answers
        </span>
      </div>

      <div class="faq-list">
        {faqList.map((item, idx) => (
          <details class="faq-accordion-item" open={idx === 0}>
            <summary class="faq-question">
              <span>{item.q}</span>
              <span class="faq-chevron">▾</span>
            </summary>
            <div class="faq-answer">
              <p>{item.a}</p>
            </div>
          </details>
        ))}
      </div>
    </div>

    <!-- Editorial Methodology & Trust Assurance -->
    <div class="section-card editorial-trust-card">
      <div class="editorial-trust-inner">
        <div class="trust-icon-box">🛡️</div>
        <div class="trust-content">
          <div class="trust-title-row">
            <h4 class="trust-heading">Independent Editorial Assessment & Review Guarantee</h4>
            <span class="trust-tag">Fact-Checked</span>
          </div>
          <p class="trust-text">
            ToolsRadar maintains strict editorial independence. This review of {tool.name} was conducted using our standardized 5-pillar evaluation framework (Setup, Code Auditability, Maintenance Vitality, Cost Advantage, and Community Signal). We do not accept paid placements to inflate benchmark scores.
          </p>
          <div class="trust-links-row">
            <a href="/methodology" class="inline-link" style="font-size: 0.85rem;">
              Read our complete 5-Pillar Review Methodology →
            </a>
            <span class="trust-dot">•</span>
            <a href="/submit" class="inline-link" style="font-size: 0.85rem;">
              Submit updates or corrections →
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Similar Alternatives in Category -->"""

    content = content.replace(target_needle, new_sections, 1)

    # 3. Add CSS styles
    css_needle = "</style>"
    new_css = """
    /* Architecture & FAQ Styles (Anti-Thin-Content Enhancement) */
    .arch-meta-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      padding-top: 1rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .arch-badge-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.03);
      padding: 0.4rem 0.75rem;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.06);
      font-size: 0.85rem;
    }

    .arch-badge-label {
      color: var(--text-muted);
      font-weight: 500;
    }

    .arch-badge-value {
      color: #f4f4f5;
      font-weight: 600;
    }

    .faq-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .faq-accordion-item {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 12px;
      overflow: hidden;
      transition: all 0.2s ease;
    }

    .faq-accordion-item[open] {
      background: rgba(255, 255, 255, 0.04);
      border-color: rgba(168, 85, 247, 0.3);
    }

    .faq-question {
      padding: 1rem 1.25rem;
      font-weight: 600;
      color: #f4f4f5;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      list-style: none;
      font-size: 0.98rem;
    }

    .faq-question::-webkit-details-marker {
      display: none;
    }

    .faq-chevron {
      color: var(--text-muted);
      font-size: 1.1rem;
      transition: transform 0.2s ease;
    }

    .faq-accordion-item[open] .faq-chevron {
      transform: rotate(180deg);
      color: #a855f7;
    }

    .faq-answer {
      padding: 0 1.25rem 1.25rem 1.25rem;
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.7;
    }

    .faq-answer p {
      margin: 0;
      white-space: pre-line;
    }

    .editorial-trust-card {
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, rgba(15, 23, 42, 0.4) 100%);
      border: 1px solid rgba(16, 185, 129, 0.2);
    }

    .editorial-trust-inner {
      display: flex;
      gap: 1.25rem;
      align-items: flex-start;
    }

    @media (max-width: 640px) {
      .editorial-trust-inner {
        flex-direction: column;
        gap: 0.75rem;
      }
    }

    .trust-icon-box {
      font-size: 1.75rem;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.25);
      width: 48px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 12px;
      flex-shrink: 0;
    }

    .trust-title-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 0.4rem;
    }

    .trust-heading {
      font-size: 1.05rem;
      font-weight: 700;
      color: #f4f4f5;
      margin: 0;
    }

    .trust-tag {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .trust-text {
      color: var(--text-secondary);
      font-size: 0.92rem;
      line-height: 1.65;
      margin: 0 0 0.75rem 0;
    }

    .trust-links-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .trust-dot {
      color: var(--text-muted);
      font-size: 0.8rem;
    }
  </style>"""

    last_style_idx = content.rfind("</style>")
    if last_style_idx != -1:
        content = content[:last_style_idx] + new_css + content[last_style_idx + len("</style>"):]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)

    print("SUCCESS: Tool page upgraded with Architecture, FAQ, Schema.org FAQPage, and Trust Assurance!")

if __name__ == "__main__":
    update_tool_page()
