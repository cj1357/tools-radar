export interface FAQItem {
  question: string;
  answer: string;
}

export const homepageFaqs: FAQItem[] = [
  {
    question: "What is ToolsRadar and how does it differ from traditional software directories?",
    answer: "ToolsRadar is an independent software intelligence observatory engineered specifically for developers, systems architects, and technical teams. Unlike automated link farms or pay-to-play directories, every project cataloged on ToolsRadar undergoes automated telemetry verification paired with an in-depth 4-chapter architectural dossier detailing technical implementation, real-world engineering use cases, operational trade-offs, and verified open-source alternatives."
  },
  {
    question: "How is the 0–100 Traction Signal Score computed?",
    answer: "The Traction Signal Score is a deterministic algorithmic metric balancing four dimensions: GitHub star acquisition velocity (35%), commit frequency and release recency (25%), organic community discussions across Hacker News and developer hubs (20%), and repository health metrics like issue closure rates (20%). Projects scoring 80 or above represent breakout tools with verified production velocity."
  },
  {
    question: "Why does ToolsRadar place special emphasis on open-source alternatives and self-hosted tools?",
    answer: "Amid escalating SaaS subscription sprawl, surprise price hikes, and restrictive licensing changes, developers require data sovereignty and predictable operating costs. ToolsRadar benchmarks self-hostable, OSI-licensed open-source replacements for proprietary tools (such as Supabase for Firebase, Docmost for Notion, and PostHog for Mixpanel), verifying Docker compose configurations and air-gapped usability."
  },
  {
    question: "Can open-source maintainers and software creators submit tools or request corrections?",
    answer: "Yes. Developers can submit new utilities for evaluation through our free community submission portal. Moreover, we maintain an open factual correction channel—project maintainers can reach out anytime to update documentation, clarify licensing tiers, or correct technical specifications, ensuring our architectural dossiers remain strictly accurate."
  },
  {
    question: "How frequently is radar telemetry refreshed?",
    answer: "Our automated scrapers and telemetry monitors run continuously with a daily CI/CD rebuild cycle every 24 hours. When repositories ship major version upgrades, change pricing tiers, or experience sudden velocity surges, their scores, badges, and dossier records are updated automatically."
  },
  {
    question: "Does ToolsRadar charge vendors for reviews or higher rankings?",
    answer: "No. ToolsRadar operates under a strict zero-payola editorial standard: we never accept payment for tool listings, sponsored reviews, or artificial ranking boosts. All software recommendations and comparison verdicts are 100% independent."
  }
];
