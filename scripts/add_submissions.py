import json
import os
import datetime

NEW_TOOLS = [
    {
        "id": "hypergsc",
        "name": "HyperGSC",
        "tagline": "Google Search Console data for AI assistants via hosted read-only MCP",
        "summary": "HyperGSC connects Google Search Console directly to AI assistants like Claude, ChatGPT, and Cursor through a hosted, read-only Model Context Protocol (MCP) server. It enables conversational analysis of organic clicks, impressions, query trends, and indexing status without manual CSV exports.",
        "url": "https://hypergsc.com",
        "github_url": None,
        "source": "submission",
        "category": "ai-agents",
        "tags": [
            "MCP",
            "Google Search Console",
            "SEO",
            "AI Assistant",
            "Cursor",
            "Claude"
        ],
        "pricing_model": "Freemium",
        "stars": 0,
        "primary_alternative": "Manual GSC CSV Export",
        "is_self_hostable": False,
        "no_signup_required": False,
        "signal_score": 88,
        "verdict": "A game-changing MCP integration for SEO professionals and technical founders who want their AI coding assistants to audit organic search performance and indexing issues directly in-context.",
        "key_features": [
            {
                "title": "Hosted Read-Only MCP Server",
                "description": "Seamlessly integrates with Cursor, Claude Desktop, and ChatGPT using the open Model Context Protocol standard."
            },
            {
                "title": "Search Analytics On-Demand",
                "description": "Query impressions, clicks, click-through rates, and average positions for specific landing pages and queries via natural language."
            },
            {
                "title": "Zero-Risk OAuth Access",
                "description": "Scoped to read-only access with granular per-property authorization to safeguard sensitive Search Console credentials."
            }
        ],
        "use_cases": [
            "Asking Claude or Cursor to analyze which blog posts lost ranking after an algorithm update",
            "Troubleshooting indexing bottlenecks and coverage drops conversationally",
            "Automating weekly organic traffic summary reports inside AI developer environments"
        ],
        "pros": [
            "Eliminates repetitive manual spreadsheet exports and pivot tables",
            "Strictly read-only OAuth architecture prevents unintended configuration changes",
            "Generous free tier covering single-property auditing for solo developers"
        ],
        "cons": [
            "Paid subscription required for multi-domain agency portfolios and extended historical lookbacks",
            "Currently depends on Model Context Protocol client support (e.g. Claude Desktop, Cursor)"
        ],
        "target_audience": "SEO specialists, technical marketers, indie founders, and engineers using AI IDEs to monitor site traffic.",
        "comparison_vs_alt": "Unlike static spreadsheet exports or heavy enterprise SEO suites like Ahrefs, HyperGSC brings real-time search performance telemetry straight into interactive AI chat prompts.",
        "install_command": None,
        "date_added": "2026-10-26",
        "featured": True
    },
    {
        "id": "soundclean",
        "name": "SoundClean",
        "tagline": "AI-powered background noise removal for audio and video recordings",
        "summary": "SoundClean is an AI utility engineered to strip ambient noise, electrical hum, reverberation, and background disturbances from audio and video recordings. Users can upload recordings, test an instant 10-second cleaned preview for free, and export crystal-clear media for podcasts, interviews, and courses.",
        "url": "https://soundclean.app/",
        "github_url": None,
        "source": "submission",
        "category": "ai-tools",
        "tags": [
            "AI Audio",
            "Noise Reduction",
            "Podcast",
            "Video Editing",
            "Speech Enhancement"
        ],
        "pricing_model": "Freemium",
        "stars": 0,
        "primary_alternative": "Adobe Podcast AI",
        "is_self_hostable": False,
        "no_signup_required": True,
        "signal_score": 84,
        "verdict": "A fast, pay-as-you-go audio enhancement utility that delivers studio-quality speech clarity without requiring expensive DAW subscriptions or complex audio engineering skills.",
        "key_features": [
            {
                "title": "Dual Audio & Video Processing",
                "description": "Cleans background audio across all common media formats including MP3, WAV, M4A, MP4, and MOV up to 500 MB."
            },
            {
                "title": "Instant 10s A/B Comparison",
                "description": "Hear side-by-side original and cleaned audio samples before committing to a paid render."
            },
            {
                "title": "Flexible Pay-Per-File or Subscriptions",
                "description": "Full file downloads start at just $0.50 per track with monthly tiers for high-volume creators."
            }
        ],
        "use_cases": [
            "Rescuing noisy field interview audio recorded on mobile phones or in windy environments",
            "Cleaning voiceover tracks for YouTube video essays and online educational courses",
            "Polishing podcast recordings plagued by air conditioner buzz or room echo"
        ],
        "pros": [
            "Free 10-second preview lets you verify acoustic results before spending a penny",
            "Micro-transaction pricing ($0.50/file) avoids forced recurring monthly subscriptions",
            "Supports video container inputs directly without needing separate audio demuxing"
        ],
        "cons": [
            "File upload cap at 500 MB limits multi-hour 4K raw video ingestion",
            "Cloud-based processing is not suitable for air-gapped or confidential legal recordings"
        ],
        "target_audience": "Podcasters, video creators, journalists, educators, and remote workers recording voice notes.",
        "comparison_vs_alt": "Unlike Adobe Podcast which requires a Creative Cloud ecosystem or heavy subscriptions, SoundClean offers single-asset on-demand cleaning starting at fifty cents.",
        "install_command": None,
        "date_added": "2026-10-26",
        "featured": False
    },
    {
        "id": "askoure-business-tool-chooser",
        "name": "Askoure Business Tool Chooser",
        "tagline": "Arabic-first four-question wizard to match marketing and lead capture tools",
        "summary": "Askoure Business Tool Chooser is a free, Arabic-first interactive decision wizard created to guide solo entrepreneurs and small businesses toward the right digital marketing and conversion software. Through a streamlined four-question assessment, it cuts through software directory noise to recommend proven landing page and lead-generation stacks.",
        "url": "https://askoure-systems.floot.app/tools/choose-business-tool",
        "github_url": "https://github.com/zongsm-cmyk/zongsm-cmyk/tree/main/resources/affiliate-ai-studio/offer-matcher",
        "source": "submission",
        "category": "productivity",
        "tags": [
            "Arabic-First",
            "Business Tools",
            "Lead Capture",
            "Interactive Wizard",
            "RTL"
        ],
        "pricing_model": "Free",
        "stars": 0,
        "primary_alternative": "G2 / Capterra",
        "is_self_hostable": False,
        "no_signup_required": True,
        "signal_score": 80,
        "verdict": "A refreshing, zero-friction tool discovery wizard that tailors digital marketing recommendations specifically for emerging MENA region entrepreneurs with native RTL support.",
        "key_features": [
            {
                "title": "Arabic-First & RTL Optimization",
                "description": "Crafted natively for Arabic-speaking business owners navigating English-dominated software ecosystems."
            },
            {
                "title": "Four-Question Needs Screening",
                "description": "Replaces hours of catalog browsing with a focused decision tree evaluating business size, budget, and channel focus."
            },
            {
                "title": "Open Architecture Prototype",
                "description": "Technical decision logic and matching rules are openly published on GitHub for verification."
            }
        ],
        "use_cases": [
            "Helping non-technical regional agencies pick the best lead capture platform for local clients",
            "Guiding freelancers in the MENA region to select budget-conscious digital marketing stacks",
            "Serving as a lightweight interactive qualification funnel for SaaS advisory"
        ],
        "pros": [
            "Completely free with no registration or credit card wall required to view matches",
            "Native RTL layout caters directly to underserved Arabic digital commerce markets",
            "Transparent technical prototype open-sourced on GitHub for community audit"
        ],
        "cons": [
            "Narrow focus primarily oriented around lead capture and marketing stacks",
            "Lightweight wizard format does not provide deep enterprise matrix comparisons"
        ],
        "target_audience": "Arab-world small business owners, freelancers, digital agency leads, and growth marketers.",
        "comparison_vs_alt": "Unlike cluttered aggregators like Capterra with thousands of sponsored listings, Askoure offers an opinionated, 60-second questionnaire tailored to regional operational needs.",
        "install_command": None,
        "date_added": "2026-10-26",
        "featured": False
    },
    {
        "id": "gh-pull",
        "name": "gh-pull",
        "tagline": "Local multi-repo GitHub pull-request dashboard as a CLI extension",
        "summary": "gh-pull is an open-source GitHub CLI extension that renders a consolidated, interactive pull-request review dashboard in your terminal. Designed for engineers managing PR reviews across multiple repositories, it provides saved review filters, stacked PR dependency lanes, CI statuses, and unread discussion thread counters.",
        "url": "https://github.com/shiqicao/gh-pull",
        "github_url": "https://github.com/shiqicao/gh-pull",
        "source": "submission",
        "category": "developer-tools",
        "tags": [
            "GitHub CLI",
            "DevTools",
            "Pull Requests",
            "Code Review",
            "Terminal",
            "Open Source"
        ],
        "pricing_model": "Free",
        "stars": 45,
        "primary_alternative": "GitHub Web PR Dashboard",
        "is_self_hostable": True,
        "no_signup_required": True,
        "signal_score": 92,
        "verdict": "An indispensable CLI superpower for tech leads and open-source maintainers who find GitHub's web PR navigation fragmented when reviewing across dozens of repositories.",
        "key_features": [
            {
                "title": "Unified Multi-Repo Overview",
                "description": "Consolidates all PRs assigned to you or awaiting your review across personal and organization repos into a single pane."
            },
            {
                "title": "Stacked PR Dependency Lanes",
                "description": "Visually graphs pull request chains and dependency branches to prevent merge order conflicts."
            },
            {
                "title": "Native GitHub CLI Integration",
                "description": "Installs with a single command via 'gh extension install shiqicao/gh-pull' and runs with 'gh pull'."
            }
        ],
        "use_cases": [
            "Triage daily pull request queues in seconds without opening dozens of browser tabs",
            "Reviewing stacked PR diffs and CI test statuses directly from the terminal",
            "Tracking unresolved review threads and approval statuses across microservice repositories"
        ],
        "pros": [
            "100% Free and open-source under the permissive MIT license",
            "Keyboard-first navigation with sticky headers for rapid triage",
            "Cross-platform support across macOS, Linux, and Windows terminal environments"
        ],
        "cons": [
            "Requires GitHub CLI (gh) installed and authenticated on the local machine",
            "Tailored specifically for engineers comfortable with terminal-first workflows"
        ],
        "target_audience": "Staff engineers, open-source maintainers, DevOps engineers, and developers reviewing pull requests across multiple repositories.",
        "comparison_vs_alt": "While the default GitHub web UI requires hopping between separate repository tabs, gh-pull creates a unified, real-time command-center view directly inside your terminal.",
        "install_command": "gh extension install shiqicao/gh-pull\ngh pull",
        "date_added": "2026-10-26",
        "featured": True
    }
]

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    tools_dir = os.path.join(data_dir, "tools")
    master_file = os.path.join(data_dir, "all_tools.json")
    daily_file = os.path.join(tools_dir, "2026-10-26.json")
    timestamp_file = os.path.join(base_dir, "site", "src", "data-timestamp.json")

    # 1. Save daily snapshot
    with open(daily_file, "w", encoding="utf-8") as f:
        json.dump(NEW_TOOLS, f, indent=2, ensure_ascii=False)
    print(f"Saved daily snapshot to {daily_file}")

    # 2. Update master all_tools.json
    with open(master_file, "r", encoding="utf-8") as f:
        all_tools = json.load(f)

    # Use dict to ensure no duplicate ID
    tools_map = {t["id"]: t for t in all_tools}
    for t in NEW_TOOLS:
        tools_map[t["id"]] = t

    # Sort tools with latest date first
    sorted_tools = sorted(tools_map.values(), key=lambda x: x.get("date_added", ""), reverse=True)

    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(sorted_tools, f, indent=2, ensure_ascii=False)
    print(f"Updated {master_file} with {len(sorted_tools)} total tools (added {len(NEW_TOOLS)})")

    # 3. Update timestamp to trigger Cloudflare CI
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(timestamp_file, "w", encoding="utf-8") as f:
        json.dump({"updated_at": now_iso}, f, indent=2)
    print(f"Updated timestamp in {timestamp_file} to {now_iso}")

if __name__ == "__main__":
    main()
