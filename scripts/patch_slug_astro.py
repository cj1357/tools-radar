with open("site/src/pages/tool/[slug].astro", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update quickstartLabel
old_label = "let quickstartLabel = tool.install_command ? 'Quick Installation / Run' : 'Quick Start Command';"
new_label = "let quickstartLabel = (tool.id === 'fastrelease') ? 'Post-Purchase Repository Setup' : (tool.install_command ? 'Quick Installation / Run' : 'Quick Start Command');"
content = content.replace(old_label, new_label)

# 2. Update defaultFaqList and support tool.faqs
old_faq_block = """// Structured FAQ dataset tailored for this tool (satisfies Google FAQPage Schema & kills thin content)
const faqList = [
  {
    q: `Is ${tool.name} completely free or does it require a paid subscription?`,
    a: tool.pricing_model === 'Open Source'
      ? `${tool.name} is 100% free and open-source under an open software license. There are no mandatory monthly subscription fees to access the source code or run it locally.`
      : (tool.pricing_model === 'Free'
          ? `${tool.name} is available completely free of charge. Developers can access its core features without payment.`
          : (tool.pricing_model === 'Paid'
              ? `${tool.name} is a commercial developer product with transparent project-based or usage-based pricing designed for professional teams.`
              : `${tool.name} provides an accessible free tier or trial alongside paid upgrades for high-volume production use.`))
  },
  {
    q: `How does ${tool.name} compare to ${tool.primary_alternative || 'competing proprietary alternatives'}?`,
    a: tool.comparison_vs_alt || `Compared to closed proprietary solutions like ${tool.primary_alternative || 'legacy alternatives'}, ${tool.name} offers distinct developer flexibility, streamlined workflows, and focused features.`
  },
  {
    q: `Can I self-host ${tool.name} on private servers or Docker?`,
    a: tool.is_self_hostable
      ? `Yes. ${tool.name} is architected for self-hosting via Docker or direct binary builds. Deploying on your own VPS or private cloud guarantees 100% data sovereignty, eliminates third-party telemetry, and ensures air-gapped security for proprietary codebases.`
      : `${tool.name} is delivered primarily as a cloud-hosted web application or managed API endpoint, providing turnkey infrastructure without requiring dedicated server management.`
  },
  {
    q: `Do I need to create an account or provide a credit card to try ${tool.name}?`,
    a: tool.no_signup_required
      ? `No account creation or credit card is required to evaluate ${tool.name}. You can immediately access core features or run it locally without onboarding friction.`
      : `An account registration is standard to provision secure API keys, manage persistent configurations, and coordinate team access.`
  },
  {
    q: `What is the recommended quickstart workflow for ${tool.name}?`,
    a: quickstartCommand
      ? `You can launch or test ${tool.name} quickly using the following command:\\n\\n${quickstartCommand}\\n\\nVisit the official portal at ${tool.url} for full documentation and sandbox demos.`
      : `Navigate to the official portal at ${tool.url} to review live interactive documentation, guides, and sandbox demos.`
  }
];"""

new_faq_block = """// Structured FAQ dataset tailored for this tool (satisfies Google FAQPage Schema & kills thin content)
const defaultFaqList = [
  {
    q: `Is ${tool.name} completely free or does it require a paid subscription?`,
    a: tool.pricing_model === 'Open Source'
      ? `${tool.name} is 100% free and open-source under an open software license. There are no mandatory monthly subscription fees to access the source code or run it locally.`
      : (tool.pricing_model === 'Free'
          ? `${tool.name} is available completely free of charge. Developers can access its core features without payment.`
          : (tool.pricing_model === 'Paid'
              ? `${tool.name} is a commercial developer product with transparent project-based or usage-based pricing designed for professional teams.`
              : `${tool.name} provides an accessible free tier or trial alongside paid upgrades for high-volume production use.`))
  },
  {
    q: `How does ${tool.name} compare to ${tool.primary_alternative || 'competing alternatives'}?`,
    a: tool.comparison_vs_alt || `Compared to alternative solutions like ${tool.primary_alternative || 'legacy alternatives'}, ${tool.name} offers distinct developer flexibility, streamlined workflows, and focused features.`
  },
  {
    q: `Can I self-host ${tool.name} on private servers or Docker?`,
    a: tool.is_self_hostable
      ? `Yes. ${tool.name} is designed for self-hosting via Docker or direct server deployment. Running on your own infrastructure allows you to maintain direct control over your local compute, database storage, and operational environment.`
      : `${tool.name} is delivered primarily as a cloud-hosted web application or managed API endpoint, providing turnkey infrastructure without requiring dedicated server management.`
  },
  {
    q: `Do I need to create an account or provide a credit card to try ${tool.name}?`,
    a: tool.pricing_model === 'Paid'
      ? `${tool.name} is a commercial developer product acquired directly under official license terms. No free trial account or public evaluation tier is provided.`
      : (tool.no_signup_required
          ? `No account creation or credit card is required to evaluate ${tool.name}. You can immediately access core features or run it locally without onboarding friction.`
          : `An account registration is standard to provision access credentials, manage configurations, and coordinate team access.`)
  },
  {
    q: `What is the recommended quickstart workflow for ${tool.name}?`,
    a: quickstartCommand
      ? `You can launch or test ${tool.name} quickly using the following command:\\n\\n${quickstartCommand}\\n\\nVisit the official portal at ${tool.url} for documentation and guides.`
      : `Navigate to the official portal at ${tool.url} to review documentation, guides, and setup requirements.`
  }
];

const faqList = (tool.faqs && Array.isArray(tool.faqs) && tool.faqs.length > 0)
  ? tool.faqs
  : defaultFaqList;"""

content = content.replace(old_faq_block, new_faq_block)

# 3. Update architecture text
old_arch_text = """        <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin-bottom: 1.5rem;">
          {tool.pricing_model === 'Open Source' 
            ? "Because the underlying code is fully open-source, engineering teams can audit security implementations and self-host updates without vendor phone-home requirements."
            : "The system is structured for rapid developer adoption, providing clear API contracts, turnkey integration primitives, and predictable operational boundaries."}
        </p>"""

new_arch_text = """        <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin-bottom: 1.5rem;">
          {tool.pricing_model === 'Open Source' 
            ? "Because the underlying code is fully open-source, engineering teams can audit security implementations and self-host updates without vendor phone-home requirements."
            : (tool.pricing_model === 'Paid'
                ? "The codebase is configured and deployed directly by the buyer on their selected infrastructure, integrating external providers as required by the application."
                : "The system is structured for rapid developer adoption, providing clear API contracts, turnkey integration primitives, and predictable operational boundaries.")}
        </p>"""

content = content.replace(old_arch_text, new_arch_text)

# 4. Update Data Sovereignty badge label
old_badge = '{tool.is_self_hostable ? "100% Private (On-Premises / Docker)" : "Managed Cloud (Zero-Ops)"}'
new_badge = '{tool.is_self_hostable ? "Self-Hosted (Buyer Infrastructure)" : "Managed Cloud"}'
content = content.replace(old_badge, new_badge)

with open("site/src/pages/tool/[slug].astro", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated site/src/pages/tool/[slug].astro successfully.")
