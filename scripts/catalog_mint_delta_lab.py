# -*- coding: utf-8 -*-
"""
Catalog Mint Delta Lab into all_tools.json and editorial_reviews.json.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
all_tools_file = os.path.join(BASE_DIR, 'data', 'all_tools.json')
editorial_file = os.path.join(BASE_DIR, 'data', 'editorial_reviews.json')

MINT_DELTA_LAB_TOOL = {
    "id": "mint-delta-lab",
    "name": "Mint Delta Lab",
    "tagline": "Browser-native Solana token snapshot comparator and state diff analyzer",
    "summary": "Mint Delta Lab is a privacy-first, client-side developer utility engineered for Solana researchers, Web3 developers, and onchain asset analysts. Operating entirely within the visitor's browser without requiring wallet connections, user registration, or remote server uploads, the platform performs deterministic state comparisons between two timestamped token-mint JSON snapshots. Mint Delta Lab calculates granular deltas across circulating token supply, mint and freeze authority rotations, and top-10 account concentration metrics, outputting clean, machine-readable JSON diffs for offline auditing and programmatic integration.",
    "url": "https://headless-rmmjyzloxyt-shunyamer-1409.wix-site-host.com/",
    "github_url": "",
    "source": "submission",
    "category": "developer-tools",
    "tags": [
        "Solana",
        "Web3",
        "Developer Tools",
        "Token Economics",
        "JSON Diff",
        "Client-Side",
        "Privacy"
    ],
    "pricing_model": "Free",
    "stars": 0,
    "primary_alternative": "Solscan",
    "is_self_hostable": False,
    "no_signup_required": True,
    "signal_score": 84,
    "verdict": "A lightweight, privacy-respecting client-side utility that simplifies verifying critical state transitions across Solana token mint observations without exposing telemetry to centralized servers.",
    "deployment_format": "Client-Side Web Application",
    "extensibility": "Structured JSON Diff Exports & Standardized Input Schema",
    "install_command": "",
    "date_added": "2026-11-23",
    "featured": False,
    "key_features": [
        {
            "title": "Deterministic State Delta Verification",
            "description": "Analyzes two timestamped observations of the same SPL token mint to detect net changes in raw token supply, decimals, and issuance dynamics."
        },
        {
            "title": "Authority Rotation Tracking",
            "description": "Instantly highlights whether critical mintAuthority or freezeAuthority keys have been modified, renounced, or transferred between observation windows."
        },
        {
            "title": "Top-Account Concentration Monitoring",
            "description": "Calculates percentage point shifts in top-10 token-account holdings, flagging potential liquidity centralization or insider accumulation."
        },
        {
            "title": "Zero-Telemetry Client-Side Execution",
            "description": "Runs 100% inside browser memory with zero wallet signature requests, no backend database logging, and zero external network calls."
        }
    ],
    "use_cases": [
        "Solana protocol developers and DAO treasuries verifying token parameter stability and authority revocations across protocol upgrades.",
        "Onchain quantitative analysts running periodic offline snapshot differential tests on newly listed SPL tokens.",
        "Security-conscious crypto researchers needing structured JSON diffs without connecting hot Web3 wallets to untrusted third-party dApps."
    ],
    "pros": [
        "Complete data privacy: inputs never leave the client's browser DOM sandbox",
        "Frictionless instant utility with zero wallet connection or account creation requirements",
        "Clean, standardized JSON diff output format ready for automated pipeline ingestion",
        "Transparent, honest scope: avoids exaggerated claims of automated fraud detection or artificial intelligence"
    ],
    "cons": [
        "Requires users to bring their own JSON snapshot observations (no automated live RPC indexing)",
        "Does not perform automated smart contract bytecode decompilation or deep security audits"
    ],
    "target_audience": "Solana developers, Web3 researchers, tokenomics auditors, and DeFi analysts.",
    "comparison_vs_alt": "While blockchain explorers like Solscan require active web traffic and continuous cloud queries, Mint Delta Lab enables private, offline, side-by-side snapshot reconciliation with zero external dependency.",
    "faqs": [
        {
            "q": "What is Mint Delta Lab and how does it work?",
            "a": "Mint Delta Lab is an in-browser utility that compares two user-supplied JSON snapshots of a Solana token mint. It parses both observations to calculate exact deltas in token supply, key authorities, and account concentration."
        },
        {
            "q": "Does Mint Delta Lab connect to my Web3 wallet or query live RPCs?",
            "a": "No. The tool is strictly client-side. It does not require a wallet connection, does not poll live Solana RPC endpoints, and does not upload your pasted JSON data to any remote server."
        },
        {
            "q": "What snapshot format is expected?",
            "a": "The comparator expects two JSON objects sharing the same 'mint' public key with an increasing 'observedAt' timestamp, containing optional fields such as 'rawSupply', 'mintAuthority', 'freezeAuthority', and 'top10TokenAccountsPct', detailed at https://headless-rmmjyzloxyt-shunyamer-1409.wix-site-host.com/docs.html."
        },
        {
            "q": "Is Mint Delta Lab free to use?",
            "a": "Yes, Mint Delta Lab is a completely free developer utility with no paywalls, accounts, or usage limitations."
        }
    ]
}

MINT_DELTA_LAB_REVIEW = {
    "article_title": "Mint Delta Lab Architecture & Solana State Dossier: Client-Side Token Delta Verification, Authority Mechanics, and Offline Auditing",
    "reading_time": "5 min read",
    "editorial_verdict_callout": "Mint Delta Lab champions a pragmatic, privacy-first philosophy for Web3 tooling—proving that targeted client-side differential analysis can provide critical clarity without wallet handshakes or cloud surveillance.",
    "chapters": [
        {
            "id": "solana-state-observation-and-telemetry-risks",
            "number": "01",
            "title": "The State Observation Dilemma: Dynamic SPL Token Telemetry and Centralized Analytics Overhead",
            "content": "On high-throughput blockchain networks like Solana, programmatic token mint accounts undergo rapid, continuous state mutations. Between any two arbitrary block slots, a token's total circulating supply can expand via unrevoked mint authorities, freeze authorities can be exercised or reassigned, and liquidity distributions can consolidate into concentrated insider wallets. For quantitative analysts, protocol engineers, and decentralized governance participants, tracking these micro-mutations is critical for risk modeling. However, inspecting token accounts via centralized web explorers (such as Solscan or commercial security aggregators) introduces persistent telemetry hazards. Commercial platforms routinely track user query histories, demand intrusive Web3 wallet connections for premium endpoints, and monetize user analytical focus. Mint Delta Lab resolves this surveillance friction by delivering a focused, completely offline comparator for token observations."
        },
        {
            "id": "client-side-delta-engine-architecture",
            "number": "02",
            "title": "Deterministic Differential Mechanics: Schema Validation and Browser-Sandboxed Delta Calculation",
            "content": "From an architectural perspective, Mint Delta Lab is structured as a client-side WebAssembly and JavaScript utility operating exclusively inside the user's browser memory sandbox. The comparator accepts two structured JSON objects sharing an identical base mint identifier and an advancing 'observedAt' ISO 8601 timestamp. The client-side parser validates numerical data integrity—including raw supply values, decimals scaling, and percentage distributions—before running deterministic differential algorithms. Because no network payload leaves the local machine, analysts can safely paste proprietary institutional observations or staging-net token configurations without exposing pre-launch tokenomics to external scrapers. Once evaluated, the engine produces an exportable JSON diff format alongside a visual delta summary, enabling seamless integration into automated local audit pipelines."
        },
        {
            "id": "tokenomics-and-authority-rotation-auditing",
            "number": "03",
            "title": "Critical State Vectors: Authority Rotation Mechanics and Concentration Risk Modeling",
            "content": "In analyzing the utility of Mint Delta Lab, its domain specificity shines in tracking three critical risk vectors: mint supply inflation, authority rotation, and token-account concentration. The transition from an active mint authority to an empty or null address is the definitive onchain signal that a token has attained fixed supply invariance. Mint Delta Lab flags changes in both mintAuthority and freezeAuthority flags with zero ambiguity. Similarly, tracking percentage shifts in the top-10 token accounts isolates whether whale wallets or market makers are actively accumulating or distributing supply across the observation interval. By crystallizing these specific state vectors rather than bombarding users with noisy transaction ledgers, the utility accelerates decision velocity for technical teams."
        },
        {
            "id": "offline-developer-ergonomics-and-verdict",
            "number": "04",
            "title": "Operational Utility Verdict: Lightweight Offline Tooling vs. Monolithic Explorers",
            "content": "In assessing production suitability, Mint Delta Lab serves as an exemplary prototype of minimalist, purpose-built developer tooling. The platform does not claim to replace comprehensive live RPC indexing nodes or perform full-spectrum bytecode fuzzing; rather, it delivers an honest, zero-cost differential calculator for observations the developer already controls. With zero sign-up friction, no wallet authorization prerequisites, and an open, well-documented schema, it provides immediate utility for engineers who prioritize operational security and clean data hygiene. For Solana builders seeking a rapid, non-intrusive sanity check on token state evolution, Mint Delta Lab is a remarkably refined addition to the Web3 developer workbench."
        }
    ],
    "tool_id": "mint-delta-lab",
    "model_used": "editorial-team",
    "generated_at": "2026-11-23T11:08:00.000000+00:00"
}

def catalog():
    # 1. Update all_tools.json
    with open(all_tools_file, 'r', encoding='utf-8') as f:
        tools = json.load(f)

    tools = [t for t in tools if t.get('id') != 'mint-delta-lab']
    tools.insert(0, MINT_DELTA_LAB_TOOL)

    with open(all_tools_file, 'w', encoding='utf-8') as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: Cataloged Mint Delta Lab into all_tools.json (Total tools: {len(tools)})")

    # 2. Update editorial_reviews.json
    with open(editorial_file, 'r', encoding='utf-8') as f:
        reviews = json.load(f)

    reviews['mint-delta-lab'] = MINT_DELTA_LAB_REVIEW

    with open(editorial_file, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: Added Mint Delta Lab 4-chapter architectural dossier into editorial_reviews.json (Total reviews: {len(reviews)})")

if __name__ == '__main__':
    catalog()
