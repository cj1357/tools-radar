# -*- coding: utf-8 -*-
"""
1. Update Mint Delta Lab with author factual corrections.
2. Catalog Qorx / Qorx Void into all_tools.json and editorial_reviews.json.
"""

import json
import os

BASE_DIR = r"d:\_projectsTYweb\tools-radar"
all_tools_file = os.path.join(BASE_DIR, 'data', 'all_tools.json')
editorial_file = os.path.join(BASE_DIR, 'data', 'editorial_reviews.json')

# -------------------------------------------------------------
# 1. MINT DELTA LAB UPDATED DATA
# -------------------------------------------------------------
MINT_DELTA_LAB_TOOL_UPDATE = {
    "summary": "Mint Delta Lab is a privacy-first, client-side developer utility engineered for Solana researchers, Web3 developers, and onchain asset analysts. Operating entirely within the visitor's browser without requiring wallet connections, user registration, or remote server uploads, the platform performs deterministic state comparisons between two timestamped token-mint JSON snapshots. Mint Delta Lab calculates granular deltas across raw token mint supply, mint and freeze authority rotations, and top-10 account concentration metrics (as a percentage of token accounts rather than beneficial owners), outputting clean, machine-readable JSON diffs for offline auditing and programmatic integration.",
    "extensibility": "Structured JSON Diff Exports & Standardized Input Schema (Optional future API beta interest survey available)",
    "key_features": [
        {
            "title": "Deterministic State Delta Verification",
            "description": "Analyzes two timestamped observations of the same SPL token mint to detect net changes in reported raw token mint supply, decimals, and issuance dynamics."
        },
        {
            "title": "Authority Rotation Tracking",
            "description": "Instantly highlights whether critical mintAuthority or freezeAuthority keys have been modified, renounced, or transferred between observation windows."
        },
        {
            "title": "Top-Account Concentration Monitoring",
            "description": "Calculates percentage point shifts across top-10 token-account balances, measuring distribution changes across token accounts without claiming identification of beneficial owners or verified entities."
        },
        {
            "title": "Zero-Telemetry Browser Execution",
            "description": "Runs 100% inside client JavaScript in the browser with zero wallet signature requests, no backend database logging, and zero external network calls."
        }
    ],
    "cons": [
        "Requires users to bring their own JSON snapshot observations (does not query live Solana RPCs or continuously track tokens)",
        "Does not perform automated smart contract bytecode decompilation, security audits, or investment advice"
    ],
    "faqs": [
        {
            "q": "What is Mint Delta Lab and how does it work?",
            "a": "Mint Delta Lab is a browser-based JavaScript utility that compares two user-supplied JSON snapshots of a Solana token mint. It parses both observations to calculate exact deltas in raw token mint supply, key authorities, and account balance concentration."
        },
        {
            "q": "Does Mint Delta Lab connect to my Web3 wallet or query live RPCs?",
            "a": "No. The tool is strictly client-side JavaScript. It does not require a wallet connection, does not poll live Solana RPC endpoints, does not monitor tokens continuously, and does not upload your pasted JSON data to any remote server."
        },
        {
            "q": "What snapshot format is expected?",
            "a": "The comparator expects two JSON objects sharing the same 'mint' public key with an increasing 'observedAt' timestamp, containing optional fields such as 'rawSupply', 'mintAuthority', 'freezeAuthority', and 'top10TokenAccountsPct', detailed at https://headless-rmmjyzloxyt-shunyamer-1409.wix-site-host.com/docs.html."
        },
        {
            "q": "Is Mint Delta Lab free to use?",
            "a": "Yes, Mint Delta Lab is a completely free developer utility with no paywalls, accounts, or usage limitations."
        },
        {
            "q": "Is there a paid API or subscription available?",
            "a": "No. Mint Delta Lab does not offer a functioning paid product or paid API, nor does it collect payments. The team hosts an optional beta survey link for gauging potential future API interest, while the core web comparator remains 100% free and open for public use."
        }
    ]
}

MINT_DELTA_LAB_REVIEW_UPDATE = {
    "article_title": "Mint Delta Lab Architecture & Solana State Dossier: Client-Side Token Delta Verification, Authority Mechanics, and Offline Auditing",
    "reading_time": "5 min read",
    "editorial_verdict_callout": "Mint Delta Lab champions a pragmatic, privacy-first philosophy for Web3 tooling—proving that targeted client-side differential analysis can provide critical clarity without wallet handshakes or cloud surveillance.",
    "chapters": [
        {
            "id": "solana-state-observation-and-telemetry-risks",
            "number": "01",
            "title": "The State Observation Dilemma: Dynamic SPL Token Telemetry and Centralized Analytics Overhead",
            "content": "On high-throughput blockchain networks like Solana, programmatic token mint accounts undergo rapid, continuous state mutations. Between any two arbitrary block slots, a token's reported raw mint supply can expand via unrevoked mint authorities, freeze authorities can be exercised or reassigned, and token account balance distributions can consolidate into fewer accounts. For quantitative analysts, protocol engineers, and decentralized governance participants, tracking these micro-mutations is critical for risk modeling. However, inspecting token accounts via centralized web explorers (such as Solscan or commercial security aggregators) introduces persistent telemetry hazards. Commercial platforms routinely track user query histories, demand intrusive Web3 wallet connections for premium endpoints, and monetize user analytical focus. Mint Delta Lab resolves this surveillance friction by delivering a focused, completely offline comparator for token observations."
        },
        {
            "id": "client-side-delta-engine-architecture",
            "number": "02",
            "title": "Deterministic Differential Mechanics: Schema Validation and Browser-Sandboxed Delta Calculation",
            "content": "From an architectural perspective, Mint Delta Lab is structured as a client-side JavaScript utility operating exclusively inside the user's browser memory sandbox. The comparator accepts two structured JSON objects sharing an identical base mint identifier and an advancing 'observedAt' ISO 8601 timestamp. The client-side parser validates numerical data integrity—including raw supply values, decimals scaling, and percentage distributions across token accounts—before running deterministic differential algorithms. Because no network payload leaves the local machine, analysts can safely paste proprietary institutional observations or staging-net token configurations without exposing pre-launch tokenomics to external scrapers. Once evaluated, the engine produces an exportable JSON diff format alongside a visual delta summary, enabling seamless integration into automated local audit pipelines."
        },
        {
            "id": "tokenomics-and-authority-rotation-auditing",
            "number": "03",
            "title": "Critical State Vectors: Authority Rotation Mechanics and Concentration Risk Modeling",
            "content": "In analyzing the utility of Mint Delta Lab, its domain specificity shines in tracking three critical state vectors: raw mint supply dynamics, authority rotation, and token-account concentration. The transition from an active mint authority to an empty or null address is the definitive onchain signal that a token has attained fixed supply invariance. Mint Delta Lab flags changes in both mintAuthority and freezeAuthority flags with zero ambiguity. Similarly, tracking percentage shifts across top-10 token accounts quantifies balance distribution variance across token accounts without making unverified assumptions about beneficial ownership or individual whale identities. By crystallizing these specific state vectors rather than bombarding users with noisy transaction ledgers, the utility accelerates decision velocity for technical teams."
        },
        {
            "id": "offline-developer-ergonomics-and-verdict",
            "number": "04",
            "title": "Operational Utility Verdict: Lightweight Offline Tooling vs. Monolithic Explorers",
            "content": "In assessing production suitability, Mint Delta Lab serves as an exemplary prototype of minimalist, purpose-built developer tooling. The platform strictly limits its scope to comparing two user-provided JSON records: it does not fetch live Solana RPC data, continuously monitor tokens, or offer financial, investment, or security audits. The core comparator is entirely free and client-side; any future API inquiries are strictly an optional beta-interest survey rather than a functioning paid product. With zero sign-up friction, no wallet authorization prerequisites, and an open, well-documented schema, it provides immediate utility for engineers who prioritize operational security and clean data hygiene. For Solana builders seeking a rapid, non-intrusive sanity check on token state evolution, Mint Delta Lab is a remarkably refined addition to the Web3 developer workbench."
        }
    ],
    "tool_id": "mint-delta-lab",
    "model_used": "editorial-team",
    "generated_at": "2026-11-24T18:00:00.000000+00:00"
}

# -------------------------------------------------------------
# 2. QORX / QORX VOID DATA
# -------------------------------------------------------------
QORX_TOOL = {
    "id": "qorx",
    "name": "Qorx Void",
    "tagline": "Local-first codebase indexer and token-squeezing context gateway for Claude Code and Codex",
    "summary": "Qorx is an open-source, evidence-first context management utility and local retrieval engine built in Rust for AI coding agents such as Claude Code, Codex, and OpenCode. Rather than feeding massive source files into LLM context windows and burning through prompt tokens, Qorx indexes codebases locally and exposes an MCP stdio server that answers architectural queries with exact file paths and line numbers. Paired with Qorx Void—a native Windows desktop companion that coordinates cross-agent skills and notes—the platform slashes context consumption by up to 85% on targeted code investigations.",
    "url": "https://github.com/bbrainfuckk/qorx",
    "github_url": "https://github.com/bbrainfuckk/qorx",
    "source": "submission",
    "category": "developer-tools",
    "tags": [
        "AI Code Agents",
        "Rust",
        "Model Context Protocol",
        "Token Optimization",
        "Local-First",
        "CLI",
        "Claude Code",
        "Developer Tools"
    ],
    "pricing_model": "Freemium",
    "stars": 28,
    "primary_alternative": "Ripgrep",
    "is_self_hostable": True,
    "no_signup_required": True,
    "signal_score": 88,
    "verdict": "A sharp, pragmatic developer tool that tackles LLM prompt inflation at the root by providing agentic workflows with pin-point local line-level citations instead of dumping raw file trees.",
    "deployment_format": "Rust CLI & Native Windows Desktop Application",
    "extensibility": "Model Context Protocol (MCP) Stdio Server & Shared Skills Pipeline",
    "install_command": "cargo install --git https://github.com/bbrainfuckk/qorx --tag v1.0.6 --locked qorx",
    "date_added": "2026-11-24",
    "featured": False,
    "key_features": [
        {
            "title": "Exact Line-Level Codebase Retrieval",
            "description": "Indexes project repositories locally and resolves architectural questions with compact line citations, avoiding whole-file ingestion."
        },
        {
            "title": "Native Model Context Protocol (MCP) Server",
            "description": "Provides standard stdio tools (qorx.squeeze, qorx.map, qorx.strict_answer) directly pluggable into Claude Code and Codex environments."
        },
        {
            "title": "Token-Squeezing Economy",
            "description": "Proven ~85% prompt token reduction in benchmarks (e.g., Express relative-path inspection reduced from 6,535 tokens to 975 tokens)."
        },
        {
            "title": "Qorx Void Cross-Agent Coordination",
            "description": "Windows companion application enabling shared workflow notes, prompt skills, and memory synchronization across disparate AI developer tools."
        }
    ],
    "use_cases": [
        "Software engineers using Claude Code, Codex, or OpenCode looking to cut LLM token usage and prevent context saturation on large codebases.",
        "Multi-agent programming setups requiring shared skills, project notes, and local proof-carrying evidence without cloud telemetry.",
        "Developers working on latency-critical or budget-constrained coding sessions who need surgical, line-numbered citations."
    ],
    "pros": [
        "Free and open-source Rust CLI core supporting Linux, macOS, and Windows under AGPL-3.0",
        "Dramatic prompt token savings (empirically demonstrated 85% context reduction in real-world benchmarks)",
        "First-class Model Context Protocol (MCP) support for seamless integration into Claude Code and Codex",
        "100% local-first architecture keeps sensitive intellectual property and proprietary source code on local disks"
    ],
    "cons": [
        "Full desktop workflow features and GUI note synchronization (Qorx Void) require Windows and a $15/month subscription after the 24-hour trial",
        "Initial codebase indexing creates a one-time local CPU and storage footprint on huge monorepos"
    ],
    "target_audience": "Software engineers, AI agent practitioners, Claude Code and Codex power users, and developers optimizing LLM context costs.",
    "comparison_vs_alt": "Unlike simple grep searches that lack agentic interfaces, or cloud code graph indexers that require uploading source files, Qorx operates entirely locally and serves line-exact evidence packages directly over MCP.",
    "faqs": [
        {
            "q": "What is Qorx and how does it reduce token consumption?",
            "a": "Qorx indexes codebases locally and generates tight, line-specific evidence packages. Instead of passing an entire 5,000-line file to an AI agent, it returns the exact lines answering the question, cutting prompt tokens by up to 85%."
        },
        {
            "q": "What is the difference between Qorx and Qorx Void?",
            "a": "Qorx is the free, open-source Rust CLI and MCP server available for Windows, macOS, and Linux. Qorx Void is a dedicated Windows desktop application from the Microsoft Store that adds GUI management and cross-agent skill and note sharing ($15/month after a 24-hour trial)."
        },
        {
            "q": "Which AI tools can connect to Qorx?",
            "a": "Any tool supporting the Model Context Protocol (MCP) or command-line execution, including Anthropic Claude Code, OpenAI Codex, OpenCode, and local developer scripts."
        },
        {
            "q": "How do I install the CLI?",
            "a": "You can build and install the Rust binary using Cargo: cargo install --git https://github.com/bbrainfuckk/qorx --tag v1.0.6 --locked qorx."
        }
    ]
}

QORX_REVIEW = {
    "article_title": "Qorx & Qorx Void Architecture: Proof-Carrying Context Squeezing, Local AST Retrieval, and MCP Agent Optimization",
    "reading_time": "6 min read",
    "editorial_verdict_callout": "By replacing indiscriminate context dumping with surgical, local-first line retrieval over MCP, Qorx delivers the precise missing link between large software repositories and cost-effective AI coding agents.",
    "chapters": [
        {
            "id": "context-window-tax-and-llm-saturation",
            "number": "01",
            "title": "The Context Window Tax: Why Full-File Ingestion Breaks Agent Efficiency",
            "content": "As autonomous AI coding agents like Anthropic Claude Code and OpenAI Codex become standard development companions, software engineers face a new architectural dilemma: context window saturation. When an agent is asked to diagnose a bug, review an API endpoint, or explain a control flow in a complex framework, the conventional agent loop involves greedily ingesting whole source files into the prompt. A routine inspection of a single module—such as Express.js path resolution—frequently consumes 6,000 to 10,000 tokens per round trip. This aggressive context ingestion accelerates token burn rates, degrades inference latency, and induces 'lost in the middle' cognitive degradation where LLMs overlook critical nuances buried within thousands of irrelevant lines. Qorx addresses this fundamental inefficiency by establishing an evidence-first, local retrieval gateway."
        },
        {
            "id": "local-ast-indexing-and-mcp-architecture",
            "number": "02",
            "title": "Architectural Mechanics of Qorx: AST Indexing, Evidence Squeezing, and MCP Stdio Integration",
            "content": "Under the hood, Qorx is engineered in high-performance Rust, compiling to native binaries across Windows, macOS, and Linux under an AGPL-3.0 license. The runtime initiates a local daemon (`qorx daemon start`) and constructs a local semantic index (`qorx index .`) of the developer's workspace. When queried through its CLI (`qorx strict-answer`) or via its Model Context Protocol (MCP) stdio server interface, Qorx evaluates the AST and token spans to extract an 'evidence package' containing strictly the relevant file paths and bounded line numbers. Through native MCP endpoints (`qorx.squeeze`, `qorx.map`, `qorx.strict_answer`), external agents can request exact line-bounded slices rather than streaming raw byte buffers. This guarantees that intellectual property remains safely sandboxed on the local machine while external AI APIs receive only distilled, verifiable code evidence."
        },
        {
            "id": "empirical-benchmarking-and-cross-agent-sharing",
            "number": "03",
            "title": "Empirical Benchmarking: The 975 vs 6,535 Token Differential in Action",
            "content": "The economic impact of Qorx's retrieval model is most pronounced during iterative debugging workflows. In standardized benchmark lookups—such as verifying relative-path validation rules inside the Express framework—an agent reading the complete module requires 6,535 prompt tokens. Executing the identical lookup through Qorx's localized index resolves the answer in just 975 tokens, achieving an 85.1% context reduction. Beyond raw token squeezing, the broader ecosystem introduces Qorx Void—a Windows companion application that bridges knowledge across different agent instances. Qorx Void enables developers to persist specialized skills, operational notes, and project constraints across disparate tools, ensuring that knowledge discovered by Claude Code is seamlessly accessible to Codex or CLI subagents without duplicating prompts."
        },
        {
            "id": "operational-verdict-cli-vs-desktop-ecosystem",
            "number": "04",
            "title": "Operational Verdict: Open Source Core vs. Qorx Void Commercial Desktop",
            "content": "ToolsRadar evaluates Qorx as a major step forward for professional AI-assisted software engineering. The free, open-source Rust CLI and MCP server provide immediate, production-grade value for any developer seeking to rein in token expenses and improve agent speed on CLI workflows. For teams seeking a unified GUI experience and automated cross-agent skill synchronization, the Qorx Void Windows application ($15/month following a 24-hour trial) presents a compelling commercial upgrade. By adhering to a strict local-first privacy standard and prioritizing surgical, verifiable evidence over brute-force token ingestion, Qorx sets an exemplary benchmark for sustainable AI developer tooling."
        }
    ],
    "tool_id": "qorx",
    "model_used": "editorial-team",
    "generated_at": "2026-11-24T18:00:00.000000+00:00"
}

def execute():
    # 1. Update all_tools.json
    with open(all_tools_file, 'r', encoding='utf-8') as f:
        tools = json.load(f)

    # Update Mint Delta Lab in all_tools.json
    mdl_found = False
    for t in tools:
        if t.get('id') == 'mint-delta-lab':
            t.update(MINT_DELTA_LAB_TOOL_UPDATE)
            mdl_found = True
            break
    print(f"Mint Delta Lab updated in all_tools.json: {mdl_found}")

    # Add or update Qorx in all_tools.json
    tools = [t for t in tools if t.get('id') != 'qorx']
    tools.insert(0, QORX_TOOL)

    with open(all_tools_file, 'w', encoding='utf-8') as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: all_tools.json saved with {len(tools)} tools.")

    # 2. Update editorial_reviews.json
    with open(editorial_file, 'r', encoding='utf-8') as f:
        reviews = json.load(f)

    reviews['mint-delta-lab'] = MINT_DELTA_LAB_REVIEW_UPDATE
    reviews['qorx'] = QORX_REVIEW

    with open(editorial_file, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: editorial_reviews.json saved with {len(reviews)} reviews.")

if __name__ == '__main__':
    execute()
