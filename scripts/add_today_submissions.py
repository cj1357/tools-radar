import json
import os
import datetime

NEW_TOOLS = [
    {
        "id": "api-crest",
        "name": "API Crest",
        "tagline": "Unified AI API gateway with Python & Node.js examples for chat, vision, and media",
        "summary": "API Crest is a developer-centric AI API platform designed to streamline multi-model integration across text, vision, and asynchronous generative media jobs. By offering public, production-ready Python and Node.js code patterns—including Anthropic-compatible message routing, multipart image editing, and polling handlers—it reduces integration complexity for software engineers building AI-native applications.",
        "url": "https://apicrest.com",
        "github_url": "https://github.com/yanbo0520/apicrest-developer-examples",
        "source": "submission",
        "category": "web-scraping-apis",
        "tags": [
            "AI APIs",
            "API Gateway",
            "Anthropic API",
            "Python SDK",
            "Node.js",
            "Developer Tools"
        ],
        "pricing_model": "Usage-based",
        "stars": 12,
        "primary_alternative": "OpenRouter",
        "is_self_hostable": False,
        "no_signup_required": False,
        "signal_score": 86,
        "verdict": "A pragmatic, documentation-first AI API gateway that stands out by providing verified, offline-checked Python and Node.js integration recipes for complex generative tasks like async media rendering and multipart payloads.",
        "key_features": [
            {
                "title": "Anthropic & Multimodal Message Routing",
                "description": "Unified endpoints supporting Anthropic-style conversational messaging alongside modern multimodal generative formats."
            },
            {
                "title": "Async Media & Image Task Polling",
                "description": "Battle-tested architectural recipes for handling long-running image transformations and media jobs without blocking worker threads."
            },
            {
                "title": "Defensive Integration Guidelines",
                "description": "Built-in developer advice covering timeout resilience, ambiguous error triage, and avoiding unintentional billable retries."
            }
        ],
        "use_cases": [
            "Integrating multi-provider AI text and vision models into existing Python or Node.js web backends",
            "Executing asynchronous image editing pipelines with robust job status polling",
            "Simplifying AI gateway error handling and retry logic using documented best practices"
        ],
        "pros": [
            "Transparent, public GitHub repository with reproducible developer examples",
            "Comprehensive documentation featuring both light and dark reading modes",
            "Direct support for complex multipart image manipulations and async polling"
        ],
        "cons": [
            "Usage-based billing requires monitoring to prevent runaway costs during high-throughput tests",
            "Newer entrant compared to established gateway platforms like OpenRouter"
        ],
        "target_audience": "Backend engineers, full-stack developers, AI app builders, and startups seeking flexible API integrations.",
        "comparison_vs_alt": "Unlike standard raw API proxies, API Crest couples its gateway with comprehensive, defensive SDK examples and developer FAQs tailored to real-world edge cases.",
        "install_command": "git clone https://github.com/yanbo0520/apicrest-developer-examples.git\ncd apicrest-developer-examples\nnpm install",
        "date_added": "2026-10-27",
        "featured": True
    },
    {
        "id": "fastrelease",
        "name": "Fastrelease",
        "tagline": "Commercial Node.js codebase for building self-hosted, multi-tenant SaaS",
        "summary": "Fastrelease is a production-grade commercial Node.js SaaS starter kit engineered for developers building self-hosted web applications. It packages user authentication, multi-tenant workspace isolation, Stripe subscription billing, PostgreSQL persistence, and Docker orchestration into a unified architecture, eliminating months of boilerplate setup.",
        "url": "https://fastrelease.net/",
        "github_url": None,
        "source": "submission",
        "category": "developer-tools",
        "tags": [
            "Node.js",
            "SaaS Boilerplate",
            "Docker",
            "PostgreSQL",
            "Stripe",
            "Multi-Tenancy"
        ],
        "pricing_model": "Paid",
        "stars": 0,
        "primary_alternative": "ShipFast",
        "is_self_hostable": True,
        "no_signup_required": False,
        "signal_score": 83,
        "verdict": "A robust, backend-heavy starter kit tailored specifically for developers who prefer Node.js, Docker, and self-hosted multi-tenancy over serverless-only boilerplates.",
        "key_features": [
            {
                "title": "Built-in Stripe & Tiered Billing",
                "description": "Pre-configured checkout flows, recurring subscriptions, and webhook handlers out of the box."
            },
            {
                "title": "Docker & Multi-Tenant Architecture",
                "description": "Full containerized environment with data isolation across organizations and teams using PostgreSQL."
            },
            {
                "title": "Complete Codebase Ownership",
                "description": "Full commercial source code access provided upon purchase with zero vendor lock-in."
            }
        ],
        "use_cases": [
            "Bootstrapping a B2B SaaS product with organization-level permissions and team billing",
            "Deploying on-premise or self-hosted software instances for enterprise clients",
            "Skipping repetitive auth, database schema, and payment infrastructure engineering"
        ],
        "pros": [
            "Comprehensive multi-tenancy and Dockerized setup ready for production VPS deployments",
            "Clean Node.js architecture with mature PostgreSQL backing",
            "One-time purchase license options without recurring starter kit subscription fees"
        ],
        "cons": [
            "Commercial closed codebase provided only post-purchase (not open source)",
            "Requires Node.js and Docker server operational familiarity"
        ],
        "target_audience": "Indie hackers, technical solopreneurs, and backend engineers launching commercial SaaS products.",
        "comparison_vs_alt": "Unlike lightweight frontend-only starters like ShipFast, Fastrelease provides deep backend architecture with true multi-tenancy, Docker support, and robust PostgreSQL schemas.",
        "install_command": None,
        "date_added": "2026-10-27",
        "featured": False
    },
    {
        "id": "mkclip",
        "name": "MKClip",
        "tagline": "Turn product screenshots into animated showcase clips using browser motion templates",
        "summary": "MKClip is a browser-based creative utility that transforms static software screenshots and UI images into animated product showcase videos. By leveraging ready-made motion templates and client-side rendering, makers can produce MP4 and WebM promo clips directly in their browser without heavy video editing software or AI hallucinations.",
        "url": "https://mkclip.com/",
        "github_url": None,
        "source": "submission",
        "category": "design-ui",
        "tags": [
            "Video Creation",
            "Product Showcase",
            "UI Motion",
            "Mockup Animation",
            "Browser Rendering"
        ],
        "pricing_model": "Freemium",
        "stars": 0,
        "primary_alternative": "Screen Studio",
        "is_self_hostable": False,
        "no_signup_required": True,
        "signal_score": 85,
        "verdict": "A lightweight, instant alternative to complex timeline editors and expensive desktop recorders, perfect for makers wanting to animate their screenshots for Twitter, Product Hunt, and landing pages.",
        "key_features": [
            {
                "title": "Instant Browser-Based Motion Templates",
                "description": "Curated animation styles designed specifically for presenting UI features and dashboard screenshots."
            },
            {
                "title": "Local Client-Side Rendering",
                "description": "Processes animations directly in the browser with fast MP4 and WebM video export."
            },
            {
                "title": "Zero-Friction Online Editor",
                "description": "Immediate access to the canvas editor at mkclip.com/editor with free 720p exports."
            }
        ],
        "use_cases": [
            "Creating slick animated demo clips for Product Hunt and Twitter/X launch announcements",
            "Transforming static feature screenshots into engaging hero section video assets",
            "Making UI visual teasers for newsletters and investor update decks"
        ],
        "pros": [
            "Runs entirely in the browser with no heavy software installation required",
            "Free editing, instant previews, and free 720p video downloads",
            "Avoids AI video rendering artifacts by using clean, deterministic motion geometry"
        ],
        "cons": [
            "Higher resolution 1080p/4K exports require paid credits or subscription",
            "Focused specifically on screenshot animations rather than full timeline video production"
        ],
        "target_audience": "Product makers, UI designers, indie founders, and growth marketers looking for rapid video teasers.",
        "comparison_vs_alt": "Unlike Screen Studio which requires a macOS desktop app and live screen capture, MKClip takes existing still screenshots and animates them inside any modern browser.",
        "install_command": None,
        "date_added": "2026-10-27",
        "featured": True
    }
]

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    master_file = os.path.join(data_dir, "all_tools.json")
    daily_file = os.path.join(data_dir, "tools", "2026-10-27.json")
    timestamp_file = os.path.join(base_dir, "site", "src", "data-timestamp.json")

    # 1. Update daily file
    daily_tools = []
    if os.path.exists(daily_file):
        with open(daily_file, "r", encoding="utf-8") as f:
            daily_tools = json.load(f)
    
    daily_map = {t["id"]: t for t in daily_tools}
    for t in NEW_TOOLS:
        daily_map[t["id"]] = t
    
    with open(daily_file, "w", encoding="utf-8") as f:
        json.dump(list(daily_map.values()), f, indent=2, ensure_ascii=False)
    print(f"Updated {daily_file} with {len(daily_map)} tools")

    # 2. Update master all_tools.json
    with open(master_file, "r", encoding="utf-8") as f:
        all_tools = json.load(f)

    tools_map = {t["id"]: t for t in all_tools}
    for t in NEW_TOOLS:
        tools_map[t["id"]] = t

    sorted_tools = sorted(tools_map.values(), key=lambda x: x.get("date_added", ""), reverse=True)

    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(sorted_tools, f, indent=2, ensure_ascii=False)
    print(f"Updated master {master_file} with {len(sorted_tools)} tools")

    # 3. Update timestamp
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(timestamp_file, "w", encoding="utf-8") as f:
        json.dump({"updated_at": now_iso}, f, indent=2)
    print(f"Updated timestamp in {timestamp_file} to {now_iso}")

if __name__ == "__main__":
    main()
