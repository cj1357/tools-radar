import json
import os
import datetime

NEW_TOOLS = [
    {
        "id": "uncensoredlabs",
        "name": "UncensoredLabs",
        "tagline": "Uncensored and abliterated AI models through an OpenAI-compatible API",
        "summary": "UncensoredLabs provides unaligned, uncensored, and abliterated AI LLM endpoints for developers building chatbots, coding assistants, and autonomous agents without safety filter refusals. Existing OpenAI-compatible clients and frameworks can seamlessly connect simply by swapping the API base URL.",
        "url": "https://uncensoredlabs.dev/",
        "github_url": None,
        "source": "submission",
        "category": "ai-tools",
        "tags": [
            "AI Models",
            "Uncensored AI",
            "OpenAI Compatible",
            "LLM API",
            "Developer Tools",
            "Abliterated Models"
        ],
        "pricing_model": "Paid",
        "stars": 0,
        "primary_alternative": "OpenRouter",
        "is_self_hostable": False,
        "no_signup_required": False,
        "signal_score": 84,
        "verdict": "An unopinionated OpenAI-compatible API gateway designed for developers requiring uncensored and abliterated open-weight models without corporate safety filter refusals.",
        "key_features": [
            {
                "title": "OpenAI-Compatible Streaming API",
                "description": "Drop-in replacement for OpenAI endpoints with full streaming chat completions support across popular AI clients."
            },
            {
                "title": "Abliterated & Uncensored Models",
                "description": "Inference endpoints powered by fine-tuned models stripped of refusal guardrails for unrestricted development and research."
            },
            {
                "title": "Spending Limits & Model Allowlists",
                "description": "Granular budget controls and API-key spending limits with prepaid token billing and transparent per-request usage tracking."
            }
        ],
        "use_cases": [
            "Building cybersecurity analysis agents that must inspect and refactor raw malware samples without safety refusals",
            "Powering unconstrained creative writing, roleplay, and uncensored synthetic data generation workflows",
            "Connecting uncensored models into third-party desktop clients like LibreChat, Open WebUI, and NextChat"
        ],
        "pros": [
            "Zero-refusal completions on abliterated open-weight LLMs",
            "100% OpenAI SDK compatibility makes integration a one-line config change",
            "Transparent prepaid pay-as-you-go billing with no monthly subscription lock-in"
        ],
        "cons": [
            "Closed-source commercial hosted infrastructure",
            "No permanent free tier; requires prepaid account balance"
        ],
        "target_audience": "Developers, cybersecurity researchers, and AI builders requiring unaligned and unconstrained model inferences.",
        "comparison_vs_alt": "Unlike mainstream providers like OpenAI or Anthropic that enforce strict safety refusals, UncensoredLabs provides raw, unaligned completions with drop-in OpenAI SDK compatibility.",
        "install_command": "curl -X POST https://api.uncensoredlabs.dev/v1/chat/completions -H \"Authorization: Bearer $UNCENSOREDLABS_API_KEY\"",
        "date_added": "2026-10-29",
        "featured": False
    },
    {
        "id": "agentweb",
        "name": "AgentWeb",
        "tagline": "Structured business and web data for AI agents over REST and hosted MCP",
        "summary": "AgentWeb delivers structured business directories, live web search, and place research specifically engineered for autonomous AI agents and developer workflows. Featuring a hosted Model Context Protocol (MCP) server alongside standard REST endpoints, it allows LLMs and agents to query over 130 million businesses, local venues, weather, and travel data without signup walls or credit card requirements.",
        "url": "https://agentweb.live",
        "github_url": None,
        "source": "submission",
        "category": "ai-agents",
        "tags": [
            "MCP",
            "Model Context Protocol",
            "AI Agents",
            "Business Data",
            "Web Search",
            "REST API",
            "Developer Tools"
        ],
        "pricing_model": "Free",
        "stars": 0,
        "primary_alternative": "Tavily",
        "is_self_hostable": False,
        "no_signup_required": True,
        "signal_score": 86,
        "verdict": "A remarkably agent-friendly data layer combining traditional REST endpoints with hosted Model Context Protocol (MCP) support, enabling AI assistants to query 130M+ verified businesses with zero credit card friction.",
        "key_features": [
            {
                "title": "Hosted Model Context Protocol (MCP)",
                "description": "Native hosted MCP endpoint at api.agentweb.live/mcp, seamlessly connecting into Claude Desktop, Cursor, and custom agent runtimes."
            },
            {
                "title": "130M+ Business Directory & Search",
                "description": "Structured business queries, web search, page retrieval, local places, weather, and travel queries optimized for agent tooling."
            },
            {
                "title": "Zero-Signup Interactive Sandbox",
                "description": "Runnable Node.js examples and open test endpoints allowing developers to inspect live data before provisioning API keys."
            }
        ],
        "use_cases": [
            "Equipping autonomous sales and market research agents with verified business directory information",
            "Integrating local venue and business lookups directly into Claude Desktop or Cursor via hosted MCP",
            "Automating travel, weather, and location-aware workflows inside multi-agent software pipelines"
        ],
        "pros": [
            "Native hosted Model Context Protocol (MCP) support simplifies LLM tool integration",
            "Free tier available with no credit card required to get an API key",
            "Runnable Node.js sample scripts and direct API documentation for rapid prototyping"
        ],
        "cons": [
            "Hosted proprietary data service; underlying pipeline is not open source",
            "Coverage and caching freshness vary by regional business registry source"
        ],
        "target_audience": "AI agent engineers, fullstack developers, and automation builders integrating real-world commercial data.",
        "comparison_vs_alt": "Unlike general search APIs like Tavily or Serper, AgentWeb focuses specifically on structured business entity intelligence and provides a native hosted Model Context Protocol (MCP) endpoint.",
        "install_command": "npx -y @modelcontextprotocol/inspector https://api.agentweb.live/mcp",
        "date_added": "2026-10-29",
        "featured": False
    }
]

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    master_file = os.path.join(data_dir, "all_tools.json")
    daily_file = os.path.join(data_dir, "tools", "2026-10-29.json")
    timestamp_file = os.path.join(base_dir, "site", "src", "data-timestamp.json")

    # 1. Update all_tools.json
    with open(master_file, "r", encoding="utf-8") as f:
        all_tools = json.load(f)

    existing_ids = {t["id"] for t in all_tools}
    added_count = 0
    for tool in NEW_TOOLS:
        if tool["id"] not in existing_ids:
            all_tools.insert(0, tool)
            existing_ids.add(tool["id"])
            added_count += 1
            print(f"Added {tool['name']} to all_tools.json")
        else:
            print(f"Tool {tool['name']} already exists, skipping.")

    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(all_tools, f, indent=2, ensure_ascii=False)

    # 2. Update/create 2026-10-29.json
    daily_tools = []
    if os.path.exists(daily_file):
        with open(daily_file, "r", encoding="utf-8") as f:
            try:
                daily_tools = json.load(f)
            except Exception:
                daily_tools = []

    daily_ids = {t["id"] for t in daily_tools}
    for tool in NEW_TOOLS:
        if tool["id"] not in daily_ids:
            daily_tools.insert(0, tool)
            daily_ids.add(tool["id"])

    with open(daily_file, "w", encoding="utf-8") as f:
        json.dump(daily_tools, f, indent=2, ensure_ascii=False)
    print(f"Updated {daily_file} with {len(daily_tools)} tools.")

    # 3. Update timestamp
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(timestamp_file, "w", encoding="utf-8") as f:
        json.dump({"updated_at": now_iso}, f, indent=2)
    print(f"Updated data-timestamp.json to {now_iso}")

    print(f"\nAll done! Added {added_count} new tools. Total tools now: {len(all_tools)}")

if __name__ == "__main__":
    main()
