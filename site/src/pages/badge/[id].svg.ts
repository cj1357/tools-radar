import type { APIRoute } from 'astro';
import allTools from '../../../../data/all_tools.json';

export function getStaticPaths() {
  return allTools.map((tool) => ({
    params: { id: tool.id },
    props: { tool },
  }));
}

export const GET: APIRoute = ({ props }) => {
  const tool = props.tool as {
    id: string;
    name: string;
    signal_score?: number;
    category?: string;
  };

  const score = tool?.signal_score || 95;
  const toolName = (tool?.name || 'Tool').length > 18 
    ? `${tool.name.slice(0, 16)}…` 
    : (tool?.name || 'Tool');

  // Escape XML characters
  const escapeXml = (unsafe: string) =>
    unsafe.replace(/[<>&'"]/g, (c) => {
      switch (c) {
        case '<': return '&lt;';
        case '>': return '&gt;';
        case '&': return '&amp;';
        case '\'': return '&apos;';
        case '"': return '&quot;';
        default: return c;
      }
    });

  const safeName = escapeXml(toolName);

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="230" height="38" viewBox="0 0 230 38" fill="none" role="img" aria-label="${safeName} on ToolsRadar">
  <title>${safeName} - Featured on ToolsRadar</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="230" y2="38" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="score-grad" x1="0" y1="0" x2="100%" y2="0">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <linearGradient id="beam" x1="12" y1="12" x2="21" y2="5" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0.1"/>
    </linearGradient>
  </defs>

  <!-- Border & Background -->
  <rect x="0.5" y="0.5" width="229" height="37" rx="8" fill="url(#bg)" stroke="rgba(56, 189, 248, 0.35)" stroke-width="1"/>

  <!-- Radar Icon -->
  <g transform="translate(10, 7)">
    <circle cx="12" cy="12" r="10" stroke="rgba(129, 140, 248, 0.25)" stroke-width="1" fill="none"/>
    <circle cx="12" cy="12" r="6.5" stroke="rgba(56, 189, 248, 0.5)" stroke-width="1" fill="rgba(56, 189, 248, 0.1)"/>
    <circle cx="12" cy="12" r="3" stroke="rgba(56, 189, 248, 0.9)" stroke-width="1.2" fill="none"/>
    <circle cx="12" cy="12" r="1.5" fill="#ffffff"/>
    <path d="M 12 12 L 20 6 A 10 10 0 0 0 12 2 Z" fill="url(#beam)"/>
  </g>

  <!-- Brand Typography -->
  <g transform="translate(42, 0)">
    <text x="0" y="15" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="8.5" font-weight="700" letter-spacing="0.6">FEATURED ON</text>
    <text x="0" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12.5" font-weight="800" letter-spacing="0.2">Tools<tspan fill="#38bdf8">Radar</tspan></text>
  </g>

  <!-- Separator Line -->
  <line x1="150" y1="8" x2="150" y2="30" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1"/>

  <!-- Signal Score Box -->
  <g transform="translate(160, 0)">
    <text x="0" y="15" fill="#64748b" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="8" font-weight="700" letter-spacing="0.6">SIGNAL</text>
    <text x="0" y="29" fill="url(#score-grad)" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="13" font-weight="800">${score}<tspan font-size="8.5" fill="#64748b">/100</tspan></text>
  </g>
</svg>`;

  return new Response(svg, {
    headers: {
      'Content-Type': 'image/svg+xml; charset=utf-8',
      'Cache-Control': 'public, max-age=86400, s-maxage=604800, stale-while-revalidate=86400',
    },
  });
};
