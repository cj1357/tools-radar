# -*- coding: utf-8 -*-
"""
Catalog Codex Quota Overlay into data/all_tools.json and data/editorial_reviews.json.
"""

import json
import os

ALL_TOOLS_PATH = r"d:\_projectsTYweb\tools-radar\data\all_tools.json"
EDITORIAL_REVIEWS_PATH = r"d:\_projectsTYweb\tools-radar\data\editorial_reviews.json"

TOOL_DATA = {
  "id": "codex-quota-overlay",
  "name": "Codex Quota Overlay",
  "tagline": "Privacy-conscious Windows companion for Codex Desktop with click-through quota overlay and local analytics",
  "summary": "Codex Quota Overlay is an independent, MIT-licensed open-source companion for Codex Desktop on Windows 10/11. It projects a non-intrusive, click-through overlay directly beside the active conversation title, displaying remaining quota percentages, reset countdowns, and reset credits in real time without stealing window focus or intercepting pointer inputs. Communicating strictly with the documented local Codex App Server methods (account/rateLimits/read and account/usage/read), it eliminates screen recording, cookie extraction, and conversation logging. An optional local Quota Center provides burn-rate estimation, safe pacing projections, multi-bucket rate limit inspection, and session-only trend metrics with optional local retention.",
  "url": "https://github.com/cpys/codex-quota-overlay",
  "github_url": "https://github.com/cpys/codex-quota-overlay",
  "source": "submission",
  "category": "developer-tools",
  "tags": [
    "Codex",
    "Codex Desktop",
    "Desktop App",
    "Windows",
    "Open Source",
    "Developer Tools",
    "Productivity",
    "Quota Monitor",
    "HUD",
    "Privacy"
  ],
  "pricing_model": "Open Source",
  "stars": 4,
  "primary_alternative": "Codex Desktop",
  "is_self_hostable": True,
  "no_signup_required": True,
  "signal_score": 88,
  "verdict": "An exemplary open-source developer companion that solves AI rate-limit anxiety through clean local RPC telemetry, complete privacy isolation, and unobtrusive click-through HUD ergonomics.",
  "deployment_format": "Native Desktop Application (Windows 10/11)",
  "install_command": "Download Setup EXE or Portable ZIP from GitHub Releases v0.4.0",
  "date_added": "2026-11-18",
  "featured": True,
  "key_features": [
    {
      "title": "Click-Through Overlay Beside Active Conversation",
      "description": "Floats seamlessly beside the Codex conversation header; automatically hides when switching applications, minimizing, or quitting, with zero pointer interception or focus stealing."
    },
    {
      "title": "Privacy-Centric Local Architecture",
      "description": "Interrogates documented local App Server RPC endpoints (account/rateLimits/read and account/usage/read) without screen capture, window title scraping, or cookie extraction."
    },
    {
      "title": "Local Quota Center & Multi-Bucket Telemetry",
      "description": "Unpacks every reported rate-limit bucket and secondary window instead of collapsing them, showing burn rates, safe pacing, and exhaustion projections."
    },
    {
      "title": "Flexible Windows Packaging & Verification",
      "description": "Distributes v0.4.0 as both a standard Setup EXE and standalone Portable ZIP for Windows 10/11 x64, backed by cryptographic SHA-256 verification and SBOM manifests."
    }
  ],
  "use_cases": [
    "Developers, prompt engineers, and technical teams relying heavily on Codex Desktop throughout demanding coding sessions who need real-time quota visibility to pace heavy tasks.",
    "Privacy-minded engineers working in regulated or enterprise environments that forbid telemetry tools that scrape screens, read conversation titles, or siphon authentication cookies.",
    "Workstation users requiring non-blocking UI aids that maintain transparency, support high-DPI and multi-monitor setups, and never steal window focus from IDEs or terminals."
  ],
  "pros": [
    "Strictly local privacy architecture: reads only local App Server RPC methods with zero screen scraping, zero title logging, and zero network telemetry by default",
    "Ergonomic click-through HUD never steals focus, passes pointer events directly to Codex, and vanishes when Codex is inactive",
    "Comprehensive Quota Center dashboard calculates burn rate, exhaustion estimates, and primary/secondary bucket limits",
    "100% Free and MIT-licensed open source with clean reproducible build, SHA-256 checksums, and SBOM manifests"
  ],
  "cons": [
    "Version 0.4.0 distributes binaries exclusively for Windows 10/11 x64 (macOS requires source compilation; no Linux desktop package due to official Codex Desktop platform limitations)",
    "Binaries are not commercially code-signed with an EV certificate, requiring users to bypass Windows SmartScreen via verified SHA-256 checksums",
    "Requires a ChatGPT-managed Codex sign-in; pure API-key configurations may not expose subscription rate limits via the local App Server"
  ],
  "target_audience": "Software engineers, AI developers, and technical creators using Codex Desktop on Windows who want to track their rate limits and reset countdowns without breaking workflow focus.",
  "comparison_vs_alt": "Unlike invasive overlay tools or browser extensions that require browser cookie access, scrape conversational DOM trees, or hijack window focus, Codex Quota Overlay relies strictly on documented local App Server RPC endpoints and provides true transparent pointer click-through.",
  "faqs": [
    {
      "q": "What is Codex Quota Overlay and what problem does it solve?",
      "a": "Codex Quota Overlay is an open-source Windows companion utility for Codex Desktop. It projects remaining quota, reset countdowns, and reset credits in a compact, non-intrusive HUD positioned beside the active conversation title, preventing unexpected rate-limit exhaustion during intense coding sessions."
    },
    {
      "q": "How does Codex Quota Overlay protect user privacy and sensitive code?",
      "a": "Codex Quota Overlay operates with strict local privacy. It reads rate-limit metadata exclusively from the local Codex App Server RPC methods (account/rateLimits/read and account/usage/read). It does not request screen recording, never inspects conversational text or window titles, does not access browser cookies, and performs zero unconsented telemetry."
    },
    {
      "q": "What platforms and operating systems are officially supported?",
      "a": "Version 0.4.0 officially distributes precompiled binaries for Windows 10/11 x64 (both Setup EXE and Portable ZIP). The repository maintains macOS source code and CI validation (buildable via npm run build:mac), but does not attach precompiled macOS installers in v0.4.0. Because OpenAI does not publish an official Codex Desktop app for Linux, Linux is not supported."
    },
    {
      "q": "Why does Windows SmartScreen warn about the installer during setup?",
      "a": "As an independent, community-driven open-source project, Codex Quota Overlay does not purchase commercial EV code-signing certificates. Users can safely bypass SmartScreen by downloading exclusively from the official GitHub Releases page and verifying the installer against the provided SHA256SUMS-Windows-0.4.0.txt checksum file."
    },
    {
      "q": "What metrics and analytics are displayed in the local Quota Center?",
      "a": "Opening the Quota Center reveals primary and secondary rate-limit buckets, estimated recent burn rate, safe prompt pacing to reach the next reset, projected exhaustion timestamps, and read-only daily activity totals. Usage history remains session-only in memory by default, with optional user-enabled local retention for 7, 14, 30, or 90 days."
    }
  ]
}

REVIEW_DATA = {
  "article_title": "Codex Quota Overlay Architecture Dossier: Local RPC Telemetry, Zero-Focus HUD Ergonomics, and Privacy-Isolated AI Quota Pacing",
  "reading_time": "6 min read",
  "editorial_verdict_callout": "Codex Quota Overlay is a textbook demonstration of ethical developer tooling: bridging local App Server IPC telemetry with transparent, click-through HUD ergonomics without compromising workstation security or user privacy.",
  "chapters": [
    {
      "id": "rate-limit-anxiety-in-agentic-coding",
      "number": "01",
      "title": "The Rate-Limit Blindspot: Mitigating Workflow Disruption in Intensive Desktop LLM Engineering",
      "content": "As software engineering teams transition from sporadic chatbot queries to continuous, agentic coding workflows in desktop environments like Codex Desktop, local usage patterns transform dramatically. Complex architectural refactoring, automated test generation, and deep context-gathering can burn through rate-limit windows at an accelerating pace. In native desktop AI interfaces, however, rate-limit status is frequently opaque—tucked away behind multi-step profile menus or revealed only when an abrupt HTTP 429 / exhaustion modal interrupts an active reasoning loop. This operational blindspot forces developers into defensive guessing games. Codex Quota Overlay emerged directly from the community to resolve this tension: translating raw rate-limit telemetry into immediate, ambient awareness directly beside the developer's field of view."
    },
    {
      "id": "zero-focus-hud-and-window-ergonomics",
      "number": "02",
      "title": "Zero-Focus HUD Architecture: Non-Intrusive Overlay Projection and Multi-Monitor Display Synchronization",
      "content": "Building an effective on-screen companion application requires solving intricate operating system window management constraints. Traditional desktop overlays frequently suffer from aggressive focus-stealing, pointer capture bugs, and visual jitter when the target application resizes or transitions across high-DPI displays. Codex Quota Overlay resolves these ergonomic challenges through a disciplined Windows subsystem implementation. The overlay window is configured with the WS_EX_TRANSPARENT and WS_EX_NOACTIVATE extended window styles, ensuring that all mouse clicks, scrolls, and keystrokes fall unimpeded directly through to the underlying Codex interface. Furthermore, the companion hooks into native window identity events: the overlay appears strictly when Codex Desktop is the active, foreground application, and immediately vanishes whenever the user switches to their IDE, terminal, or browser. Multi-monitor setups, DPI scaling differentials, and vertical/horizontal placement offsets are cleanly accommodated without requiring manual window realignment."
    },
    {
      "id": "privacy-isolation-documented-rpc-vs-scraping",
      "number": "03",
      "title": "Privacy Isolation: Documented Local RPC Telemetry vs Fragile Screen-Scraping Anti-Patterns",
      "content": "A rampant anti-pattern among third-party productivity companions is the reliance on invasive surveillance techniques: capturing desktop screenshots, parsing DOM elements via accessibility APIs, or extracting browser session cookies to replicate user sessions on remote servers. In stark contrast, Codex Quota Overlay demonstrates rigorous architectural discipline. The application interfaces exclusively with the documented local Codex App Server RPC socket on the user's workstation, issuing lightweight read-only queries against account/rateLimits/read and account/usage/read. It deliberately leaves window title buffers empty, requests zero screen-recording entitlements, and never reads conversational text or sensitive source code. Furthermore, data telemetry remains local by default: trend history is retained purely in transient session memory, with optional user-activated local disk persistence (7, 14, 30, or 90 days) that stores only normalized percentages and timestamps. Short diagnostics are capped at 200 characters, intentionally stripping usernames, IPs, paths, and raw tokens to ensure leak-proof bug reporting."
    },
    {
      "id": "open-source-governance-and-production-verdict",
      "number": "04",
      "title": "Open-Source Governance, Packaging Integrity & Editorial Recommendation",
      "content": "Distributed under the permissive MIT license, Codex Quota Overlay represents community open source at its best. Version 0.4.0 addresses Windows 10/11 x64 workstations through both a guided Setup EXE and an unprivileged Portable ZIP. Acknowledging that community open-source tools cannot justify multi-hundred-dollar annual EV code-signing certificate taxes, the maintainer provides cryptographic SHA-256 checksum manifests and CycloneDX Software Bill of Materials (SBOM) artifacts for complete supply-chain verifiability. While macOS maintainer validation exists in CI, the deliberate focus on Windows fills a critical gap in a developer ecosystem often skewed toward Unix workstations. In conclusion, ToolsRadar awards Codex Quota Overlay a Signal Score of 88/100, recommending it as an essential, privacy-respecting companion for engineers who demand uninterrupted visibility over their Codex Desktop operational budget."
    }
  ],
  "tool_id": "codex-quota-overlay",
  "model_used": "editorial-team",
  "generated_at": "2026-11-18T04:30:00.000000+00:00"
}

def main():
    with open(ALL_TOOLS_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)
    
    # Check if already present
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
