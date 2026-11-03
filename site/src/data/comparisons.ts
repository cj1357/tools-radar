import allToolsRaw from '../../../data/all_tools.json';

export interface ToolItem {
  id: string;
  name: string;
  tagline: string;
  summary: string;
  url: string;
  github_url?: string;
  category: string;
  pricing_model: string;
  stars?: number;
  primary_alternative?: string;
  is_self_hostable?: boolean;
  no_signup_required?: boolean;
  signal_score?: number;
  verdict?: string;
  key_features?: string[];
  pros?: string[];
  cons?: string[];
  use_cases?: string[];
  comparison_vs_alt?: string;
  install_command?: string;
  date_added?: string;
  featured?: boolean;
}

export interface ComparisonPair {
  slug: string;
  toolA: ToolItem;
  toolBName: string;
  toolB: ToolItem | null;
  category: string;
  comparisonText: string;
  verdictA: string;
  verdictB: string;
  isFeaturedPair: boolean;
}

const allTools: ToolItem[] = allToolsRaw as ToolItem[];

const toolsById = new Map<string, ToolItem>();
const toolsByName = new Map<string, ToolItem>();

allTools.forEach(t => {
  toolsById.set(t.id, t);
  toolsByName.set(t.name.toLowerCase().trim(), t);
});

// High-impact head-to-head pairs to prioritize
const PRIORITY_SLUGS = new Set([
  'postiz-vs-buffer',
  'uncensoredlabs-vs-openrouter',
  'agentweb-vs-tavily',
  'coolify-vs-heroku',
  'titleart-vs-canva',
  'neatbo-svg-pattern-generator-vs-hero-patterns',
  'hob-vs-chatgpt-desktop',
  'ai-design-skills-vs-figma-ai',
  'mangatranslate-vs-manual-ocr-photoshop-typesetting',
  'deeptutor-vs-khanmigo',
  'ai-video-ugc-vs-heygen',
  'encarta-95-web-vs-wikipedia',
  'spec-first-vs-cursor',
  'aqueous-archive-format-vs-tar',
  'cirkit-vs-altium-designer'
]);

const knownFreeKeywords = [
  'git', 'blender', 'audacity', 'gimp', 'obsidian', 'vs code', 'vscode', 'vscodium',
  'cursor', 'neovim', 'vim', 'emacs', 'linux', 'curl', 'wget', 'ffmpeg', 'tar',
  'sqlite', 'postgresql', 'postgres', 'mysql', 'redis', 'docker', 'kubernetes', 'k8s',
  'python', 'rust', 'go', 'golang', 'nodejs', 'deno', 'bun', 'react', 'vue', 'astro',
  'next.js', 'svelte', 'tailwind', 'bootstrap', 'wikipedia', 'libreoffice', 'vlc',
  'keepass', 'bitwarden', 'wireshark', 'postman', 'thunderbird', 'firefox', 'chromium',
  'manual', 'photoshop typesetting', 'spreadsheet', 'excel'
];

function buildPairs(): ComparisonPair[] {
  const pairs: ComparisonPair[] = [];
  const seenSlugs = new Set<string>();

  for (const tool of allTools) {
    const rawAlt = tool.primary_alternative;
    if (!rawAlt || rawAlt.trim().length < 2) continue;

    const altName = rawAlt.trim();
    const altSlug = altName.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    if (!altSlug || tool.id === altSlug) continue;

    const pairSlug = `${tool.id}-vs-${altSlug}`;
    if (seenSlugs.has(pairSlug)) continue;
    seenSlugs.add(pairSlug);

    const internalB = toolsById.get(altSlug) || toolsByName.get(altName.toLowerCase()) || null;
    const isKnownFreeB = internalB 
      ? (internalB.pricing_model === 'Open Source' || internalB.pricing_model === 'Free')
      : knownFreeKeywords.some(k => altName.toLowerCase().includes(k));

    const compText = tool.comparison_vs_alt || 
      `${tool.name} serves as a specialized, developer-centric alternative to ${altName}, offering enhanced control, tailored workflows, and modern architecture.`;

    const verdictA = tool.pricing_model === 'Open Source'
      ? `Choose ${tool.name} if you require full code sovereignty, zero SaaS lock-in, self-hosted Docker deployments, and complete ownership of your data infrastructure.`
      : `Choose ${tool.name} if you want a streamlined, purpose-built workflow with developer-friendly pricing and transparent architecture.`;

    const verdictB = internalB 
      ? `Choose ${internalB.name} if its specific feature set and ecosystem integrations align closer with your immediate production requirements.`
      : (isKnownFreeB
          ? `Choose ${altName} if you prefer a mature, widely adopted ecosystem standard with battle-tested workflows, universal command-line or desktop adoption, and comprehensive community documentation.`
          : `Choose ${altName} if you prefer an established, turnkey commercial cloud service with hosted infrastructure, managed maintenance, and official enterprise SLA guarantees.`);

    const isFeatured = PRIORITY_SLUGS.has(pairSlug) || Boolean(tool.featured && (tool.stars || 0) > 1000);

    pairs.push({
      slug: pairSlug,
      toolA: tool,
      toolBName: altName,
      toolB: internalB,
      category: tool.category || 'developer-tools',
      comparisonText: compText,
      verdictA,
      verdictB,
      isFeaturedPair: isFeatured,
    });
  }

  // Sort: featured first, then by Tool A stars / signal score
  return pairs.sort((a, b) => {
    if (a.isFeaturedPair && !b.isFeaturedPair) return -1;
    if (!a.isFeaturedPair && b.isFeaturedPair) return 1;
    const scoreA = (a.toolA.signal_score || 90) + Math.min(10, (a.toolA.stars || 0) / 1000);
    const scoreB = (b.toolA.signal_score || 90) + Math.min(10, (b.toolA.stars || 0) / 1000);
    return scoreB - scoreA;
  });
}

export const comparisonPairs = buildPairs();

export function getComparisonPairBySlug(slug: string): ComparisonPair | undefined {
  return comparisonPairs.find(p => p.slug === slug);
}

export function getPairsForTool(toolId: string): ComparisonPair[] {
  return comparisonPairs.filter(p => p.toolA.id === toolId || (p.toolB && p.toolB.id === toolId));
}

export function getTopComparisons(limit = 24): ComparisonPair[] {
  return comparisonPairs.slice(0, limit);
}
