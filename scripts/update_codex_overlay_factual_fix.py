# -*- coding: utf-8 -*-
"""
Apply factual corrections for Codex Quota Overlay in all_tools.json and editorial_reviews.json.
- Remove 'alternative' label / set primary_alternative to None
- Set companion_to to 'Codex Desktop'
- Update tagline to 'Windows quota overlay companion for Codex Desktop'
- Clarify v0.4.0 distribution: Windows 10/11 x64 only (macOS source/CI compatibility exists, but no distributed macOS installer in v0.4.0)
"""

import json

ALL_TOOLS_PATH = r"d:\_projectsTYweb\tools-radar\data\all_tools.json"
EDITORIAL_REVIEWS_PATH = r"d:\_projectsTYweb\tools-radar\data\editorial_reviews.json"

def main():
    with open(ALL_TOOLS_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)

    updated = False
    for t in tools:
        if t.get("id") == "codex-quota-overlay":
            t["tagline"] = "Windows quota overlay companion for Codex Desktop"
            t["primary_alternative"] = None
            t["companion_to"] = "Codex Desktop"
            t["summary"] = (
                "Codex Quota Overlay is an independent, MIT-licensed open-source Windows companion utility "
                "designed specifically for Codex Desktop. Rather than replacing Codex Desktop, it operates alongside it "
                "by interfacing directly with the local Codex App Server methods (account/rateLimits/read and account/usage/read) "
                "to project a transparent, click-through overlay beside the active conversation header. It displays real-time "
                "rate-limit percentages, reset countdowns, and reset credits without stealing keyboard focus or intercepting pointer events. "
                "An optional local Quota Center dashboard provides burn-rate estimation, safe pacing projections, multi-bucket rate limit "
                "inspection, and session-only trend metrics with optional local retention."
            )
            t["comparison_vs_alt"] = (
                "Codex Quota Overlay is engineered as a dedicated companion to Codex Desktop rather than a replacement or alternative. "
                "While Codex Desktop manages reasoning models and coding workflows, its rate-limit telemetry is tucked away in secondary menus. "
                "Codex Quota Overlay reads the local App Server RPC socket to project an ambient, click-through HUD directly beside the active "
                "conversation with zero screen scraping and zero pointer interception."
            )
            t["cons"] = [
                "v0.4.0 distributes precompiled release assets exclusively for Windows 10/11 x64; macOS source/CI validation exists in the repository, but there is no distributed macOS installer package attached to v0.4.0",
                "Binaries are not commercially code-signed with an EV certificate, requiring users to bypass Windows SmartScreen via verified SHA-256 checksums",
                "Requires a ChatGPT-managed Codex sign-in; pure API-key configurations may not expose subscription rate limits via the local App Server"
            ]
            t["faqs"] = [
                {
                    "q": "What is Codex Quota Overlay and what problem does it solve?",
                    "a": "Codex Quota Overlay is an open-source Windows companion utility designed for Codex Desktop. Rather than replacing Codex Desktop, it operates alongside it by projecting remaining quota, reset countdowns, and reset credits in a compact, non-intrusive HUD positioned beside the active conversation title, preventing unexpected rate-limit exhaustion during intense coding sessions."
                },
                {
                    "q": "How does Codex Quota Overlay protect user privacy and sensitive code?",
                    "a": "Codex Quota Overlay operates with strict local privacy. It reads rate-limit metadata exclusively from the local Codex App Server RPC methods (account/rateLimits/read and account/usage/read). It does not request screen recording, never inspects conversational text or window titles, does not access browser cookies, and performs zero unconsented telemetry."
                },
                {
                    "q": "What platforms and operating systems are officially supported in v0.4.0?",
                    "a": "Version 0.4.0 officially distributes precompiled binaries exclusively for Windows 10/11 x64 (both Setup EXE and Portable ZIP). While the repository maintains macOS source code and CI validation, maintainers note that there is no precompiled macOS installer distributed in v0.4.0. Linux is not supported as there is no official Codex Desktop application for Linux."
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
            updated = True
            break

    if updated:
        with open(ALL_TOOLS_PATH, "w", encoding="utf-8") as f:
            json.dump(tools, f, indent=2, ensure_ascii=False)
        print("Updated codex-quota-overlay in all_tools.json")
    else:
        print("Could not find codex-quota-overlay in all_tools.json")

    with open(EDITORIAL_REVIEWS_PATH, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    if "codex-quota-overlay" in reviews:
        r = reviews["codex-quota-overlay"]
        r["article_title"] = "Codex Quota Overlay Architecture Dossier: Local RPC Telemetry, Zero-Focus HUD Ergonomics, and Privacy-Isolated AI Quota Pacing"
        r["editorial_verdict_callout"] = "Codex Quota Overlay is a textbook demonstration of ethical developer tooling: bridging local App Server IPC telemetry with transparent, click-through HUD ergonomics to serve as an indispensable desktop companion for Codex Desktop."
        for ch in r.get("chapters", []):
            if ch.get("id") == "open-source-governance-and-production-verdict":
                ch["content"] = (
                    "Distributed under the permissive MIT license, Codex Quota Overlay represents community open source at its best. "
                    "Version 0.4.0 addresses Windows 10/11 x64 workstations through both a guided Setup EXE and an unprivileged Portable ZIP. "
                    "While macOS source code and maintainer CI validation exist in the repository, version 0.4.0 distributes release assets "
                    "exclusively for Windows, with no distributed macOS installer package attached to the release. Acknowledging that community "
                    "open-source tools cannot justify multi-hundred-dollar annual EV code-signing certificate taxes, the maintainer provides "
                    "cryptographic SHA-256 checksum manifests and CycloneDX Software Bill of Materials (SBOM) artifacts for complete supply-chain "
                    "verifiability. In conclusion, ToolsRadar awards Codex Quota Overlay a Signal Score of 88/100, recommending it as an essential, "
                    "privacy-respecting companion for engineers who demand uninterrupted visibility over their Codex Desktop operational budget."
                )
        with open(EDITORIAL_REVIEWS_PATH, "w", encoding="utf-8") as f:
            json.dump(reviews, f, indent=2, ensure_ascii=False)
        print("Updated editorial review for codex-quota-overlay")

if __name__ == "__main__":
    main()
