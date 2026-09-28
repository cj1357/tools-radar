import allTools from '../../../data/all_tools.json';

export async function GET() {
  const searchIndex = allTools.map((t) => ({
    id: t.id,
    name: t.name,
    tagline: t.tagline,
    category: t.category,
    tags: t.tags || [],
    pricing_model: t.pricing_model,
    source: t.source,
    stars: t.stars || 0,
    primary_alternative: t.primary_alternative || null,
    is_self_hostable: Boolean(t.is_self_hostable),
    no_signup_required: Boolean(t.no_signup_required),
    signal_score: t.signal_score || 0,
    url: t.url,
    github_url: t.github_url || null,
  }));

  return new Response(JSON.stringify(searchIndex), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=86400, stale-while-revalidate=604800',
    },
  });
}
