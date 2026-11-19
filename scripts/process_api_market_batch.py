# -*- coding: utf-8 -*-
"""
Catalog API.market MCP Gateway into data/all_tools.json and data/editorial_reviews.json.
"""

import json

ALL_TOOLS_PATH = r"d:\_projectsTYweb\tools-radar\data\all_tools.json"
EDITORIAL_REVIEWS_PATH = r"d:\_projectsTYweb\tools-radar\data\editorial_reviews.json"

TOOL_DATA = {
  "id": "api-market-mcp-gateway",
  "name": "API.market MCP Gateway",
  "tagline": "Hosted Model Context Protocol gateway connecting AI agents to 550+ APIs and 3,410+ tools",
  "summary": "API.market MCP Gateway (by MagicAPI Inc) is a unified, hosted Model Context Protocol (MCP) server that connects AI agent environments—including Claude, ChatGPT, Cursor, VS Code, and Codex—to an extensive catalog of 550+ APIs and 3,410+ tools across 44 categories. Operating over Streamable HTTP at https://api.market/api/mcp/gateway with automatic OAuth or API key authorization, the gateway allows agents to discover APIs, inspect operation schemas, manage subscriptions, and execute tool calls in a single session without juggling separate MCP servers or individual vendor integrations.",
  "url": "https://api.market/mcp",
  "github_url": "",
  "source": "submission",
  "category": "ai-agents",
  "tags": [
    "MCP",
    "Model Context Protocol",
    "AI Agents",
    "API Gateway",
    "Developer Tools",
    "Streamable HTTP",
    "OAuth",
    "API Marketplace"
  ],
  "pricing_model": "Freemium",
  "stars": 0,
  "primary_alternative": "RapidAPI",
  "is_self_hostable": False,
  "no_signup_required": False,
  "signal_score": 88,
  "verdict": "A powerful consolidation layer for the Model Context Protocol ecosystem, turning hundreds of standalone commercial APIs into a single streamable MCP gateway for AI coding agents.",
  "deployment_format": "Hosted MCP Gateway (Streamable HTTP)",
  "install_command": "Configure MCP endpoint: https://api.market/api/mcp/gateway",
  "date_added": "2026-11-19",
  "featured": True,
  "key_features": [
    {
      "title": "Single Streamable HTTP Endpoint for 550+ APIs",
      "description": "Consolidates 3,410+ API tools across 44 categories into one streamable MCP URL (https://api.market/api/mcp/gateway), eliminating the need to maintain dozens of local Docker or Node MCP instances."
    },
    {
      "title": "Turnkey OAuth & API Key Authentication",
      "description": "Supports automatic OAuth sign-in across Claude Desktop, ChatGPT, Cursor, and VS Code, alongside traditional API key headers for CLI agents."
    },
    {
      "title": "Dynamic Discovery & Schema Inspection",
      "description": "Enables AI agents to query the catalog in natural language, retrieve JSON schema signatures, and inspect operational requirements on demand."
    },
    {
      "title": "Granular Per-API Metering & Free Tiers",
      "description": "Provides unified balance tracking and usage quotas across heterogeneous API providers under flexible pay-as-you-go and free tier models."
    }
  ],
  "use_cases": [
    "AI agent developers and prompt engineers building multi-tool agentic workflows in Cursor, Claude, or Codex who need instant access to diverse data sources without provisioning separate servers.",
    "Autonomous agent workflows requiring dynamic tool discovery and runtime schema resolution across thousands of commercial endpoints.",
    "Software engineering teams seeking centralized API billing, key management, and quota governance across dozens of third-party API services."
  ],
  "pros": [
    "One single MCP gateway URL replaces dozens of fragmented standalone MCP servers",
    "Native Streamable HTTP transport with automated OAuth support for Claude, ChatGPT, Cursor, and VS Code",
    "Extensive catalog spanning 550+ APIs and 3,410+ tools across 44 domain categories",
    "Transparent usage dashboards and free tiers available for supported APIs"
  ],
  "cons": [
    "Proprietary hosted gateway without an open-source self-hosted runtime package",
    "Requires an API.market account and provider subscriptions for paid or rate-limited API tiers",
    "For single-provider workflows (e.g. only using GitHub or Slack), dedicated native MCP servers may offer more specialized deep primitives"
  ],
  "target_audience": "AI agent developers, Cursor and Claude power users, full-stack software engineers, and autonomous agent architects.",
  "comparison_vs_alt": "While RapidAPI pioneered the developer API marketplace model with traditional REST keys and web dashboards, it lacks a unified Model Context Protocol streaming gateway. API.market MCP Gateway bridges standard API catalogs directly into agentic IDEs and LLM runtimes via MCP Streamable HTTP.",
  "faqs": [
    {
      "q": "What is API.market MCP Gateway and how does it work?",
      "a": "API.market MCP Gateway is a hosted Model Context Protocol service hosted by API.market. It exposes over 550 APIs and 3,410+ operational tools through a single Streamable HTTP endpoint (https://api.market/api/mcp/gateway). AI agents in Claude, Cursor, ChatGPT, or VS Code can connect to this endpoint to discover APIs, inspect schemas, and execute calls directly."
    },
    {
      "q": "How do I connect the MCP Gateway to Claude, Cursor, or VS Code?",
      "a": "In your AI client (e.g., Claude Desktop, Cursor, or VS Code), add a new MCP server with the URL https://api.market/api/mcp/gateway using Streamable HTTP transport. You can authenticate either via automatic OAuth browser sign-in or by supplying your API.market API key."
    },
    {
      "q": "How does pricing work across different APIs?",
      "a": "Pricing is freemium on a per-API basis. Many APIs include generous free tiers for prototyping and low-volume queries, while high-throughput or compute-heavy endpoints (like image or video generation) follow transparent pay-as-you-go pricing billed through your unified API.market account."
    },
    {
      "q": "Is API.market MCP Gateway open-source or self-hostable?",
      "a": "The gateway is a proprietary hosted cloud service operated by MagicAPI Inc. While the MCP client connection protocol is standard and open, the routing gateway, multi-provider credential aggregation, and billing infrastructure are managed in the cloud."
    },
    {
      "q": "How does this compare to running individual open-source MCP servers?",
      "a": "Running separate open-source MCP servers requires installing, containerizing, and authenticating each tool individually on your local workstation. API.market MCP Gateway consolidates hundreds of diverse APIs into one cloud-hosted connection, reducing local configuration overhead while providing dynamic catalog discovery."
    }
  ]
}

REVIEW_DATA = {
  "article_title": "API.market MCP Gateway Architecture Dossier: Streamable HTTP Federation, Agentic Tool Routing, and Unified API Economics",
  "reading_time": "6 min read",
  "editorial_verdict_callout": "API.market MCP Gateway delivers a compelling operational abstraction: converting thousands of disparate third-party REST APIs into a single streamable Model Context Protocol conduit for modern AI coding agents.",
  "chapters": [
    {
      "id": "mcp-fragmentation-bottleneck-in-agent-workflows",
      "number": "01",
      "title": "The MCP Toolchain Sprawl: Taming Multi-Server Overhead in Agentic Development",
      "content": "Since Anthropic introduced the Model Context Protocol (MCP) as an open standard for LLM tool augmentation, the developer ecosystem has seen an explosion of specialized servers. However, this proliferation quickly created a new engineering tax: workstation configuration sprawl. A developer orchestrating an autonomous coding agent might need web search, scraping, geographic routing, image transformation, and financial lookup tools. Running each provider as an isolated local stdio process or Docker container consumes substantial memory, requires managing discrete environment keys, and risks configuration drift. The API.market MCP Gateway addresses this friction directly: acting as a managed aggregation proxy that condenses hundreds of vendor integrations into a single remote connection."
    },
    {
      "id": "streamable-http-and-dynamic-schema-negotiation",
      "number": "02",
      "title": "Streamable HTTP Mechanics: OAuth Handshakes, Dynamic Schemas, and Low-Latency Tool Routing",
      "content": "Architecturally, API.market MCP Gateway transitions from brittle local stdio pipes to modern Streamable HTTP (hosted at api.market/api/mcp/gateway). This protocol shift unlocks key ergonomics: AI environments like Claude Desktop, Cursor, ChatGPT, and VS Code can authenticate via standard OAuth 2.0 web redirects or API key headers without requiring local CLI runtime dependencies. More critically, the gateway solves the context-window saturation problem. Instead of blindly injecting the full tool schemas of 3,410+ endpoints into the LLM system prompt—which would exhaust token limits—the gateway exposes meta-discovery tools. Agents dynamically query catalog subsets, inspect JSON schema signatures on demand, and invoke subscribed APIs with validated parameters in a clean, multi-turn sequence."
    },
    {
      "id": "the-agentic-marketplace-shift",
      "number": "03",
      "title": "The Agent-First Marketplace: Bridging Discovery, Subscriptions, and Execution into Single Turns",
      "content": "Traditional API marketplaces like RapidAPI were fundamentally architected for human developers: browsing documentation on a web portal, copying cURL snippets, entering credit card details manually, and embedding static keys into backend codebases. In an agentic paradigm, this human-in-the-loop workflow creates severe friction. API.market's gateway reimagines the marketplace as an interactive runtime environment. An AI agent facing a complex task (e.g., 'transcribe this audio file and geocode the address mentioned') can query the gateway, identify capable candidate tools, verify that the active user account possesses an adequate free or paid tier, and execute the call without forcing the developer to leave their IDE."
    },
    {
      "id": "cost-economics-governance-and-verdict",
      "number": "04",
      "title": "Unified Billing Governance, Provider Centralization & Editorial Verdict",
      "content": "From an operational governance perspective, API.market consolidates multi-vendor billing into a coherent dashboard. Engineering teams avoid managing dozens of independent credit card subscriptions across disparate micro-SaaS providers. However, teams must recognize the architectural trade-offs: relying on a centralized cloud gateway introduces a network dependency compared to fully air-gapped, on-premises local MCP daemons, and organizations with deep single-vendor commitments (e.g., dedicated GitHub or Linear tooling) may still prefer native vendor-maintained servers. Nonetheless, for cross-domain tool flexibility and zero-friction IDE setup, ToolsRadar awards API.market MCP Gateway an 88/100 Signal Score, designating it as a premier aggregation tier for modern agentic engineering."
    }
  ],
  "tool_id": "api-market-mcp-gateway",
  "model_used": "editorial-team",
  "generated_at": "2026-11-19T03:00:00.000000+00:00"
}

def main():
    with open(ALL_TOOLS_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)

    existing_idx = None
    for i, t in enumerate(tools):
        if t.get("id") == TOOL_DATA["id"]:
            existing_idx = i
            break

    if existing_idx is not None:
        tools[existing_idx] = TOOL_DATA
        print(f"Updated existing {TOOL_DATA['id']} in all_tools.json")
    else:
        tools.append(TOOL_DATA)
        print(f"Appended {TOOL_DATA['id']} to all_tools.json. New total: {len(tools)}")

    with open(ALL_TOOLS_PATH, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)

    with open(EDITORIAL_REVIEWS_PATH, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews[TOOL_DATA["id"]] = REVIEW_DATA
    print(f"Added editorial review for {TOOL_DATA['id']}. Total reviews: {len(reviews)}")

    with open(EDITORIAL_REVIEWS_PATH, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
