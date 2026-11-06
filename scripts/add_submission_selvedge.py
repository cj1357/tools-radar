# -*- coding: utf-8 -*-
"""
Add submission Selvedge to all_tools.json and editorial_reviews.json
Submitted by Mason D (masondelan@gmail.com) on 2026-11-06
"""

import json
import os
import sys

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
all_tools_path = os.path.join(data_dir, "all_tools.json")
reviews_path = os.path.join(data_dir, "editorial_reviews.json")

SELVEDGE_TOOL = {
    "id": "selvedge",
    "name": "Selvedge",
    "tagline": "Local decision history and persistent memory that coding agents can retrieve across sessions",
    "summary": "Selvedge is a lightweight, local-first decision history engine engineered specifically for autonomous AI coding agents (such as Cursor, Claude Code, and Cline). Instead of relying on lossy conversation context or monolithic system instruction files, Selvedge tracks the architectural 'why' behind codebases—recording design decisions, stated rationales, constraints, and explicitly rejected approaches in a project-local SQLite database. Future agent sessions can query historical decisions by function, column, or route via a Python CLI or native Model Context Protocol (MCP) server, preventing agents from breaking unwritten rules or repeating failed code implementations.",
    "url": "https://selvedge.sh/",
    "github_url": "https://github.com/masondelan/selvedge",
    "source": "submission",
    "category": "ai-agents",
    "tags": [
        "AI Agents",
        "Agent Memory",
        "MCP",
        "Developer Tools",
        "SQLite",
        "Local-First",
        "Python",
        "CLI"
    ],
    "pricing_model": "Free",
    "stars": 26,
    "primary_alternative": "ADRs / Mem0",
    "is_self_hostable": True,
    "no_signup_required": True,
    "signal_score": 86,
    "verdict": "An indispensable local memory layer for autonomous coding agents, capturing architectural rationale, constraints, and explicitly rejected approaches in local SQLite without external cloud dependencies.",
    "key_features": [
        {
            "title": "Local SQLite Decision Storage",
            "description": "Stores architectural decisions, stated rationales, and rejected paths in a zero-latency SQLite database versioned alongside the project codebase."
        },
        {
            "title": "Entity-Keyed History Queries",
            "description": "Look up relevant design constraints and past attempts by querying specific named functions, database columns, API routes, or custom entities."
        },
        {
            "title": "Dual CLI & Native MCP Integration",
            "description": "Seamlessly accessible via standard Python CLI commands or natively integrated into AI coding agents via the Model Context Protocol (MCP)."
        }
    ],
    "use_cases": [
        "Preventing autonomous coding agents from repeating previously tested and rejected implementation approaches across fresh conversation sessions",
        "Preserving architectural decisions and unwritten constraints without bloating agent context windows with monolithic instruction documents",
        "Providing human developers with a structured, queryable rationale log of why specific functions or schemas were engineered a certain way"
    ],
    "pros": [
        "100% free and open-source under MIT license with complete local-first data privacy in SQLite",
        "Native Model Context Protocol (MCP) server enables zero-configuration agent tooling for Cursor, Claude Code, and Cline",
        "Explicitly records rejected approaches—a critical dimension omitted by traditional git blame or markdown ADRs"
    ],
    "cons": [
        "Requires agents or developers to explicitly record decisions during or after implementation",
        "Best suited for project-scoped context rather than cross-repository enterprise knowledge graphs"
    ],
    "target_audience": "AI software engineers, agent framework developers, and teams building with autonomous coding assistants who need reliable cross-session architectural continuity.",
    "comparison_vs_alt": "While Architecture Decision Records (ADRs) capture formal high-level project milestones and rule files (e.g. .cursorrules) define standing constraints, Selvedge provides granular, entity-keyed micro-decisions and rejected paths stored locally in SQLite and queryable on demand via MCP.",
    "install_command": "pip install selvedge",
    "date_added": "2026-11-06",
    "featured": True,
    "faqs": [
        {
            "q": "What is Selvedge and how does it help coding agents?",
            "a": "Selvedge is a local decision history engine that stores architectural decisions, rationales, and rejected approaches in project-local SQLite. It gives AI coding agents persistent cross-session memory so they don't repeat failed approaches or break unwritten constraints."
        },
        {
            "q": "How do AI coding agents query Selvedge?",
            "a": "Coding agents connect to Selvedge natively via the Model Context Protocol (MCP) or by invoking the local Python CLI. When editing a specific function, class, or route, the agent queries Selvedge for entity-specific decision history."
        },
        {
            "q": "Does Selvedge replace Architecture Decision Records (ADRs) or agent instruction files?",
            "a": "No. Agent instruction files (like AGENTS.md or .cursorrules) suit standing rules, and ADRs suit reviewed high-level architecture milestones. Selvedge complements them by adding queryable entity-level micro-decision history and rejected alternatives."
        },
        {
            "q": "Is Selvedge free and open source?",
            "a": "Yes. Selvedge is 100% free and open source under the permissive MIT license. All data is stored locally on your machine in SQLite with zero cloud telemetry."
        },
        {
            "q": "How do I install and configure Selvedge?",
            "a": "You can install Selvedge via pip (pip install selvedge) or uv. Run 'selvedge init' in your repository root to initialize the local SQLite database and configure the local MCP server."
        }
    ]
}

SELVEDGE_REVIEW = {
    "article_title": "Selvedge Architecture & Engineering Dossier: Persistent Decision Memory & Rejected Paths for Coding Agents",
    "reading_time": "6 min read",
    "editorial_verdict_callout": "Selvedge provides the missing memory substrate for AI coding assistants: a local-first, entity-keyed decision ledger that records not just what code was written, but why alternative approaches were rejected.",
    "chapters": [
        {
            "id": "architecture-mechanics",
            "number": "01",
            "title": "Architectural Foundation & The 'Cross-Session Amnesia' Problem",
            "content": (
                "Modern AI coding agents—ranging from terminal agents like Claude Code to IDE extensions like Cursor and Windsurf—excel at localized code generation and refactoring. "
                "However, they suffer from a systemic operational flaw: cross-session amnesia. When an agent starts a new conversation session, the entire chain-of-thought, intermediate trial-and-error, "
                "and architectural trade-offs discussed in previous sessions vanish. Developers frequently observe agents reverting intentional trade-offs or repeatedly proposing implementations "
                "that were already tested and explicitly rejected days earlier. Traditional solutions fall short: git blame only reveals line mutations without capturing rejected paths; Architecture "
                "Decision Records (ADRs) are too heavyweight for micro-decisions; and monolithic instruction files (such as .cursorrules) quickly exhaust precious context window tokens. "
                "Selvedge solves this fundamental friction by introducing a structured, entity-keyed decision ledger designed to run locally alongside the codebase."
            )
        },
        {
            "id": "local-sqlite-engine",
            "number": "02",
            "title": "Local-First Entity Graph & SQLite Storage Engine",
            "content": (
                "At the core of Selvedge is a zero-latency, local SQLite storage engine embedded directly within the target repository. Instead of indexing generic text blobs or embedding vectors, "
                "Selvedge structures memory around named programmatic entities—functions, classes, database columns, API routes, or config parameters. Every recorded entry captures three vital dimensions: "
                "the decision taken, the technical rationale behind it, and the alternatives that were rejected along with reasons for their rejection. Because storage is local SQLite, reads execute in sub-millisecond time "
                "with zero cloud latency, zero external API costs, and complete privacy for proprietary codebases. Decisions can be grouped using shared changeset tags across multiple files and routes, "
                "allowing agents to inspect full architectural blast radiuses before modifying dependent modules."
            )
        },
        {
            "id": "mcp-agent-integration",
            "number": "03",
            "title": "Model Context Protocol (MCP) & Cross-Session Recall",
            "content": (
                "Selvedge achieves seamless integration with modern coding workflows through two interoperable interfaces: a lightweight Python CLI and a native Model Context Protocol (MCP) server. "
                "When configured as an MCP client within an agent environment (such as Claude Desktop, Cursor, or Cline), Selvedge exposes specialized retrieval and mutation tools directly to the agent's function-calling runtime. "
                "Before refactoring a database schema or modifying an authentication route, the agent autonomously executes a lookup tool against the relevant entity name. The MCP server returns the structured decision history "
                "and rejected approaches directly into the agent's scratchpad, steering the model toward compliant implementations without human intervention. Developers can also inspect, export, or audit records using standard CLI commands "
                "like 'selvedge log' or generate markdown digests for documentation."
            )
        },
        {
            "id": "production-tradeoffs",
            "number": "04",
            "title": "Production Trade-offs, Operational Best Practices & Verdict",
            "content": (
                "Selvedge provides an exceptionally pragmatic balance between informal code comments and formal enterprise architecture documentation. Its primary strength lies in its explicit capture of negative knowledge: "
                "recording why an approach failed is often ten times more valuable for an AI agent than merely seeing the current code. The operational requirement is discipline: either the developer or the agent must invoke "
                "the recording tool when a key technical fork is decided. For software engineering teams leveraging autonomous AI coding assistants, Selvedge represents a high-signal, zero-cost productivity multiplier. "
                "By pairing local SQLite data ownership with standardized MCP connectivity, it establishes a reliable architectural memory substrate that preserves hard-won engineering context across agent sessions."
            )
        }
    ]
}

def main():
    # 1. Update all_tools.json
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # Check if selvedge already exists
    existing_idx = next((i for i, t in enumerate(tools) if t.get("id") == "selvedge"), None)
    if existing_idx is not None:
        print("Updating existing selvedge entry in all_tools.json...")
        tools[existing_idx] = SELVEDGE_TOOL
    else:
        print("Prepending selvedge to all_tools.json...")
        tools.insert(0, SELVEDGE_TOOL)

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    print(f"all_tools.json updated successfully. Total tools: {len(tools)}")

    # 2. Update editorial_reviews.json
    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews["selvedge"] = SELVEDGE_REVIEW
    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)
    print("editorial_reviews.json updated successfully with selvedge review.")

if __name__ == "__main__":
    main()
