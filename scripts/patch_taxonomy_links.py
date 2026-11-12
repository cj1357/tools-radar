# -*- coding: utf-8 -*-
"""
Patch TaxonomyClusterSection.astro to fix 404 links:
1. Replace non-existent featuredVS pairs with real top VS battlegrounds.
2. Replace non-existent tag slugs (no-signup -> ai-coding, self-host -> self-hosted, vector-search -> vector-database).
3. Ensure all links have canonical trailing slashes.
"""

import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "site", "src", "components", "TaxonomyClusterSection.astro"))
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace featuredVS
old_vs_block = """const featuredVS = [
  { pair: "cursor-vs-github-copilot", label: "Cursor vs GitHub Copilot", desc: "AI Coding Assistant & IDE" },
  { pair: "supabase-vs-firebase", label: "Supabase vs Firebase", desc: "Open-Source vs Cloud BaaS" },
  { pair: "raycast-vs-alfred", label: "Raycast vs Alfred", desc: "macOS Developer Command Bar" },
  { pair: "ollama-vs-vllm", label: "Ollama vs vLLM", desc: "Local LLM Serving & Inference" },
  { pair: "posthog-vs-mixpanel", label: "PostHog vs Mixpanel", desc: "Product Analytics & Session Replay" }
];"""

new_vs_block = """const featuredVS = [
  { pair: "supabase-vs-firebase", label: "Supabase vs Firebase", desc: "Open-Source vs Cloud BaaS" },
  { pair: "sentry-vs-datadog", label: "Sentry vs Datadog", desc: "Error Tracking & Observability" },
  { pair: "vantage-vs-github-copilot", label: "Vantage vs GitHub Copilot", desc: "AI Coding Assistant & Workspace" },
  { pair: "opaline-vs-posthog", label: "Opaline vs PostHog", desc: "Product Analytics & Session Replay" },
  { pair: "superhuman-go-vs-raycast", label: "Superhuman Go vs Raycast", desc: "Command Bar & AI Productivity" }
];"""

content = content.replace(old_vs_block.replace("\n", "\r\n"), new_vs_block.replace("\n", "\r\n"))
content = content.replace(old_vs_block, new_vs_block)

# Replace popularTags
old_tags_block = """const popularTags = [
  { name: "ai-agents", count: "168+" },
  { name: "self-host", count: "388+" },
  { name: "no-signup", count: "534+" },
  { name: "developer-tools", count: "117+" },
  { name: "open-source", count: "350+" },
  { name: "database", count: "42+" },
  { name: "privacy", count: "65+" },
  { name: "cli", count: "89+" },
  { name: "rust", count: "78+" },
  { name: "python", count: "120+" },
  { name: "typescript", count: "145+" },
  { name: "docker", count: "95+" },
  { name: "terminal", count: "64+" },
  { name: "machine-learning", count: "110+" },
  { name: "vector-search", count: "36+" },
  { name: "automation", count: "75+" },
  { name: "monitoring", count: "48+" },
  { name: "security", count: "52+" },
  { name: "devops", count: "86+" },
  { name: "api", count: "62+" },
  { name: "desktop", count: "40+" }
];"""

new_tags_block = """const popularTags = [
  { name: "ai-agents", count: "316+" },
  { name: "self-hosted", count: "388+" },
  { name: "ai-coding", count: "140+" },
  { name: "developer-tools", count: "117+" },
  { name: "open-source", count: "350+" },
  { name: "database", count: "42+" },
  { name: "privacy", count: "65+" },
  { name: "cli", count: "89+" },
  { name: "rust", count: "78+" },
  { name: "python", count: "120+" },
  { name: "typescript", count: "145+" },
  { name: "docker", count: "95+" },
  { name: "terminal", count: "64+" },
  { name: "machine-learning", count: "110+" },
  { name: "vector-database", count: "36+" },
  { name: "automation", count: "75+" },
  { name: "monitoring", count: "48+" },
  { name: "security", count: "52+" },
  { name: "devops", count: "86+" },
  { name: "api", count: "62+" },
  { name: "desktop", count: "40+" }
];"""

content = content.replace(old_tags_block.replace("\n", "\r\n"), new_tags_block.replace("\n", "\r\n"))
content = content.replace(old_tags_block, new_tags_block)

# Add trailing slashes to all template URLs
content = content.replace("href={`/guides/${guide.slug}`}", "href={`/guides/${guide.slug}/`}")
content = content.replace("href={`/vs/${vs.pair}`}", "href={`/vs/${vs.pair}/`}")
content = content.replace("href={`/tag/${tag.name}`}", "href={`/tag/${tag.name}/`}")
content = content.replace('href="/guides"', 'href="/guides/"')
content = content.replace('href="/vs"', 'href="/vs/"')
content = content.replace('href="/tag"', 'href="/tag/"')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("TaxonomyClusterSection.astro patched successfully.")
