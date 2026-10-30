import allToolsRaw from '../../../data/all_tools.json';

export interface BestTopic {
  slug: string;
  title: string;
  h1: string;
  tagline: string;
  metaDesc: string;
  categoryFilter?: string;
  customFilter?: (tool: any) => boolean;
  annualSavingsEstimate: string;
  editorialIntro: string;
  keyEvaluationCriteria: string[];
  faqs: { q: string; a: string }[];
}

export const bestTopics: BestTopic[] = [
  {
    slug: 'open-source-developer-tools',
    title: 'Best Open Source Developer Tools (2026 Ranked)',
    h1: 'Best Open Source Developer Tools in 2026',
    tagline: 'High-signal, production-tested utilities with transparent codebases and active communities.',
    metaDesc: 'Discover the top-ranked open-source developer tools of 2026. Audited for code sovereignty, active GitHub maintenance, zero SaaS lock-in, and engineering ergonomics.',
    annualSavingsEstimate: '$3,600 / year',
    customFilter: (t) => t.pricing_model === 'Open Source' && (t.stars || 0) > 200,
    editorialIntro: 'In 2026, the developer tool ecosystem is experiencing an unprecedented shift toward open-source sovereignty. Rising SaaS subscription fatigue, arbitrary seat licenses, and sudden relicensing controversies have driven independent engineers and platform teams to prioritize tools that can be compiled, inspected, and self-hosted on owned infrastructure. This curated ranking features developer utilities that combine modern UI/UX with permissive open-source foundations.',
    keyEvaluationCriteria: [
      'Permissive licensing without hidden proprietary upstream traps',
      'High release velocity and active GitHub pull request reviews',
      'Zero mandatory cloud telemetry or vendor phone-home requirements',
      'Reproducible Docker Compose and standalone binary deployment options'
    ],
    faqs: [
      {
        q: 'Why should engineering teams prefer open-source developer tools in 2026?',
        a: 'Open-source tools eliminate per-seat SaaS taxes, provide immunity against sudden price hikes or service shutdowns, and allow engineering teams to inspect and modify source code for compliance and internal integration.'
      },
      {
        q: 'How does ToolsRadar rank open-source projects?',
        a: 'We evaluate projects through a composite Radar Signal Score combining GitHub commit velocity, issue resolution rates, documentation completeness, and community adoption signals.'
      }
    ]
  },
  {
    slug: 'self-hostable-alternatives',
    title: 'Top Self-Hostable Alternatives to Popular SaaS (2026)',
    h1: 'Top Self-Hostable Alternatives to Commercial SaaS',
    tagline: 'Take back data ownership by replacing expensive monthly cloud subscriptions with self-hosted software.',
    metaDesc: 'Explore the definitive list of self-hostable open-source software replacements for Notion, Buffer, Sentry, Vercel, and Airtable. Save thousands annually with Docker.',
    annualSavingsEstimate: '$5,400 / year',
    customFilter: (t) => Boolean(t.is_self_hostable) && Boolean(t.primary_alternative),
    editorialIntro: 'The "Subscription Tax" is real: a solo developer or boutique studio easily spends $400 to $800 each month on a fragmented web of project management, social schedulers, observability platforms, and analytics SaaS. Every tool in this collection provides a turnkey self-hosted alternative that runs on a modest $10–$20 VPS via Docker Compose, reducing your monthly overhead while giving you complete ownership over your customer data.',
    keyEvaluationCriteria: [
      'Effortless 1-click or single-command Docker deployment',
      'Feature parity with incumbent enterprise cloud equivalents',
      'Local database persistence with zero external phone-home mandates',
      'Low memory footprint suitable for budget VPS environments'
    ],
    faqs: [
      {
        q: 'What VPS specifications do I need to run self-hosted alternatives?',
        a: 'Most modern self-hosted tools (like Postiz, PocketBase, or Uptime Kuma) run comfortably on a 2 vCPU / 4GB RAM VPS costing approximately $10 to $15 per month on providers like Hetzner or DigitalOcean.'
      },
      {
        q: 'How do I handle updates and backups for self-hosted tools?',
        a: 'Using automated Docker orchestration tools like Coolify, Watchtower, or scheduled cron backup scripts to Cloudflare R2 or AWS S3 makes maintenance hands-off and reliable.'
      }
    ]
  },
  {
    slug: 'free-coding-agents',
    title: 'Top Free & Open AI Coding Agents (2026 Guide)',
    h1: 'Top Free & Autonomous AI Coding Agents',
    tagline: 'Command-line agents, local repository indexers, and unconstrained software engineering assistants.',
    metaDesc: 'Compare the best free and open-source AI coding agents of 2026. Benchmark CLI agents, IDE extensions, MCP servers, and local model assistants.',
    annualSavingsEstimate: '$2,400 / year',
    categoryFilter: 'ai-agents',
    customFilter: (t) => t.category === 'ai-agents' && (t.pricing_model === 'Free' || t.pricing_model === 'Open Source'),
    editorialIntro: 'Autonomous coding agents have graduated from experimental demos to mission-critical engineering accelerators. Instead of locked-in closed GUI editors that charge steep monthly subscription premiums, modern developers are assembling flexible setups combining CLI agent tools, Model Context Protocol (MCP) servers, and open LLM gateways. This list ranks the most capable free and open-source coding agents available today.',
    keyEvaluationCriteria: [
      'Support for local terminal execution and arbitrary shell tools',
      'Compatibility with standard Model Context Protocol (MCP) integrations',
      'Transparent context management and token expenditure tracking',
      'Multi-model provider support (Ollama, Anthropic, OpenRouter, OpenAI)'
    ],
    faqs: [
      {
        q: 'Can open-source coding agents compete with proprietary IDEs like Cursor?',
        a: 'Yes. CLI-based agents like Claude Code, Aider, and OpenCode coupled with custom MCP server workflows frequently outperform monolithic GUI IDEs in multi-file refactoring, terminal tasks, and test-driven validation.'
      },
      {
        q: 'How do free coding agents handle API usage costs?',
        a: 'Free agents use your own API keys (BYOK) with pay-per-token pricing, or run entirely locally using Ollama and DeepSeek-Coder weights with zero marginal cost.'
      }
    ]
  },
  {
    slug: 'privacy-first-analytics',
    title: 'Best Privacy-First & Cookieless Analytics (2026)',
    h1: 'Best Privacy-First & Cookieless Analytics Tools',
    tagline: 'Lightweight web telemetry without cookie banners, GDPR violations, or invasive user tracking.',
    metaDesc: 'The top privacy-friendly and cookieless website analytics tools of 2026. Lightweight, GDPR/CCPA compliant alternatives to Google Analytics.',
    annualSavingsEstimate: '$1,800 / year',
    customFilter: (t) => (t.tags && (t.tags.includes('analytics') || t.tags.includes('privacy'))) || t.category === 'developer-tools',
    editorialIntro: 'Google Analytics 4 has become notoriously complex, heavyweight, and legally risky for international operations requiring intrusive cookie banners. Privacy-first analytics platforms strip away intrusive personal fingerprinting in favor of aggregate pageview statistics, high-performance lightweight script payloads (< 2KB), and complete compliance with GDPR, CCPA, and PECR without nagging consent modals.',
    keyEvaluationCriteria: [
      'Payload size under 3KB with zero performance impact on Core Web Vitals',
      'No personal data collection (IP hashing without permanent storage)',
      '100% compliance without requiring cookie consent banners',
      'Option for custom domain proxying to bypass ad-blockers'
    ],
    faqs: [
      {
        q: 'Do privacy-friendly analytics tools require a cookie consent banner?',
        a: 'No. Because these tools do not place persistent tracking cookies or store personally identifiable information (PII), they are exempt from GDPR ePrivacy Directive consent requirements in Europe.'
      }
    ]
  },
  {
    slug: 'zero-subscription-tax-stack',
    title: 'The Zero Subscription Tax Stack: Best Free Indie Tools (2026)',
    h1: 'The Zero Subscription Tax Software Stack',
    tagline: 'Run your entire startup and digital operations on open-source and generous free-tier software.',
    metaDesc: 'Stop bleeding money on software subscriptions. The ultimate 2026 developer stack of open-source, self-hosted, and free-forever tools for indie makers.',
    annualSavingsEstimate: '$6,200 / year',
    customFilter: (t) => (t.pricing_model === 'Open Source' || t.pricing_model === 'Free') && (t.signal_score || 0) >= 95,
    editorialIntro: 'The greatest threat to an early-stage startup or indie developer is cash burn before product-market fit. By deliberately selecting sovereign open-source infrastructure and generous free-tier tools, you can run scalable production workloads, CI/CD, database clusters, and marketing automation for the cost of a single cheap VPS server. Here is our curated blueprint for the Zero Subscription Tax stack in 2026.',
    keyEvaluationCriteria: [
      'Zero credit card required to start and scale initial workloads',
      'Complete absence of aggressive per-seat monetization traps',
      'Full exportability of all relational data and assets',
      'Battle-tested community reliability with thousands of production installs'
    ],
    faqs: [
      {
        q: 'How much money does the Zero Subscription Tax stack save on average?',
        a: 'Based on our benchmarks comparing common SaaS stacks (DataDog + Buffer + Notion Team + Zapier + Vercel Pro), an indie developer or small team saves between $4,500 and $7,200 annually.'
      }
    ]
  },
  {
    slug: 'self-hosted-ai-platforms',
    title: 'Top Self-Hosted AI & Local LLM Platforms (2026 Ranked)',
    h1: 'Top Self-Hosted AI & Local LLM Platforms',
    tagline: 'Sovereign AI workstations, private model inference engines, and modular generation pipelines.',
    metaDesc: 'Compare the best self-hosted and local AI platforms of 2026. Deploy Open WebUI, ComfyUI, vLLM, and BitNet to eliminate AI subscriptions and protect data privacy.',
    annualSavingsEstimate: '$4,800 / year',
    customFilter: (t) => {
      const priorityIds = [
        'open-webui',
        'comfyui',
        'vllm',
        'airllm',
        'bitnet',
        'voicestudio',
        'moneyprinterturbo',
        'buzz',
        'openmausbot',
        'lugh-xtudio',
        'openbot',
        'hindsight',
        'claude-mem',
        'hyperframes',
        'openmontage'
      ];
      if (priorityIds.includes(t.id)) return true;
      const isAi = t.category === 'ai-tools' || t.category === 'ai-agents';
      const isSelfHost = Boolean(t.is_self_hostable) || t.pricing_model === 'Open Source';
      const tags = (t.tags || []).join(' ').toLowerCase();
      const hasLocalTag = tags.includes('inference') || tags.includes('local') || tags.includes('offline') || tags.includes('speech') || tags.includes('diffusion');
      return isAi && isSelfHost && hasLocalTag;
    },
    editorialIntro: 'In 2026, enterprise data privacy concerns and surging API token invoices have triggered a massive migration toward self-hosted and localized artificial intelligence. Engineering teams and privacy-conscious organizations are no longer willing to transmit proprietary source code, internal knowledge bases, and customer records to closed commercial AI clouds. This ranking highlights the premier self-hosted AI workstations, local model runners, and generative DAG pipelines that run reliably on private GPU hardware or sovereign on-premise servers.',
    keyEvaluationCriteria: [
      'Zero cloud API dependency with complete offline data sovereignty',
      'High-throughput GPU/CPU inference optimization (quantization, GGUF, vLLM paging)',
      'Standardized OpenAI-compatible API endpoints for drop-in client compatibility',
      'Turnkey containerized deployment via Docker and lightweight WebUI interfaces'
    ],
    faqs: [
      {
        q: 'Why should developers and teams self-host AI models in 2026?',
        a: 'Self-hosting eliminates recurring $20–$30/seat AI subscriptions, guarantees zero third-party training on proprietary intellectual property, complies with strict GDPR/HIPAA regulations, and prevents unexpected downtime from cloud rate limits.'
      },
      {
        q: 'What hardware is needed to run self-hosted AI platforms effectively?',
        a: 'Modern quantized models (GGUF, AWQ, BitNet) run comfortably on consumer hardware: an Apple Silicon Mac (M2/M3/M4 with 24GB+ unified memory) or a single NVIDIA RTX 4070/4090 GPU can easily serve 8B to 70B parameter models at interactive speeds.'
      }
    ]
  }
];

export function getBestTopicBySlug(slug: string): BestTopic | undefined {
  return bestTopics.find(t => t.slug === slug);
}

export function getRankedToolsForTopic(topic: BestTopic, limit = 12) {
  const all = allToolsRaw as any[];
  let filtered = all;

  if (topic.categoryFilter) {
    filtered = filtered.filter(t => t.category === topic.categoryFilter);
  }

  if (topic.customFilter) {
    filtered = filtered.filter(topic.customFilter);
  }

  // Sort by signal_score desc, then stars desc
  return filtered
    .sort((a, b) => {
      const scoreA = (a.signal_score || 90) * 1000 + (a.stars || 0);
      const scoreB = (b.signal_score || 90) * 1000 + (b.stars || 0);
      return scoreB - scoreA;
    })
    .slice(0, limit);
}
