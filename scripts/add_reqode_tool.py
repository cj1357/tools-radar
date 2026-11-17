# -*- coding: utf-8 -*-
"""
Catalog Reqode into data/all_tools.json and data/editorial_reviews.json
Submitted by Dmitry Yurkin <dy@almware.com>, Almware Ltd.
"""

import json
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
all_tools_path = os.path.join(root_dir, "data", "all_tools.json")
reviews_path = os.path.join(root_dir, "data", "editorial_reviews.json")

REQODE_TOOL = {
    "id": "reqode",
    "name": "Reqode",
    "tagline": "Product and architecture context engine for autonomous AI coding agents via MCP",
    "summary": "Reqode (developed by Almware Ltd.) is a centralized specification and architecture workspace engineered to provide autonomous AI coding agents with branch-aware project context. By linking high-level product requirements, Architecture Decision Records (ADRs), feature change scopes, and test specifications into a versioned workspace, Reqode exposes structured context directly to coding agents (such as Claude Code, Cursor, and VS Code) through the Model Context Protocol (MCP). It bridges the operational divide between product intent and code execution, allowing coding agents to write software aligned with architectural constraints and enabling authorized QA agents to retrieve prepared tests and record execution passes.",
    "url": "https://reqode.com",
    "github_url": "",
    "source": "submission",
    "category": "developer-tools",
    "tags": [
        "MCP",
        "AI Coding Agents",
        "Context Engine",
        "Architecture Decisions",
        "Software Requirements",
        "QA Agents",
        "Developer Tools",
        "Product Management"
    ],
    "pricing_model": "Paid",
    "stars": 0,
    "primary_alternative": "Linear",
    "is_self_hostable": False,
    "no_signup_required": False,
    "signal_score": 89,
    "verdict": "An indispensable context and specification layer for modern software teams that grounds autonomous AI coding agents in authentic product requirements and architecture decision records via MCP.",
    "deployment_format": "Cloud SaaS & MCP Server",
    "install_command": "Configure MCP server via https://reqode.com/product/mcp",
    "iconUrl": "https://reqode.com/files/logo-square.png",
    "date_added": "2026-11-17",
    "featured": True,
    "key_features": [
        {
            "title": "Unified Requirements, ADRs & Test Specs Workspace",
            "description": "Centrally links software requirements, architectural decisions (ADRs), change scopes, and acceptance criteria in one structured interface."
        },
        {
            "title": "Branch-Aware MCP Context Delivery",
            "description": "Exposes deterministic, branch-specific feature specifications and architectural constraints to Claude Code, Cursor, and VS Code via Model Context Protocol."
        },
        {
            "title": "Autonomous QA & Test Execution Synchronization",
            "description": "Allows authorized testing and QA agents to retrieve prepared test suites, validate implementations, and automatically record execution results."
        },
        {
            "title": "Multi-Agent Team Alignment",
            "description": "Ensures distributed engineering teams, product managers, and concurrent autonomous agents reference the exact same single source of architectural truth."
        }
    ],
    "use_cases": [
        "Software engineering teams using Claude Code or Cursor who want to eliminate agent hallucinations by injecting versioned requirements and ADRs via MCP.",
        "System architects and tech leads ensuring that autonomous coding loops strictly adhere to approved design patterns and architectural boundaries.",
        "Continuous delivery pipelines deploying autonomous QA agents to retrieve acceptance criteria and automatically log verification results against branches."
    ],
    "pros": [
        "Native Model Context Protocol (MCP) server enables turnkey integration with leading AI agents like Claude Code and Cursor",
        "Branch-aware context retrieval prevents cross-branch specification confusion in multi-agent workflows",
        "Directly unifies requirements, architectural decisions, and QA validation into a machine-readable context graph",
        "Generous 14-day free trial allows engineering teams to validate agent context workflows prior to subscription"
    ],
    "cons": [
        "Cloud-hosted SaaS platform without an on-premises self-hosted Docker distribution",
        "Requires product and engineering teams to establish disciplined specification writing practices to maximize MCP utility"
    ],
    "target_audience": "Software architects, engineering managers, product owners, and developers coordinating autonomous AI coding agents on production codebases.",
    "comparison_vs_alt": "Unlike issue trackers like Linear or Jira that primarily manage kanban boards and human status updates, Reqode formats product specifications, ADRs, and test criteria into machine-actionable context delivered directly into agent loops via MCP.",
    "faqs": [
        {
            "q": "What is Reqode and what problem does it solve for AI coding agents?",
            "a": "Reqode is a centralized specification and architecture workspace that links software requirements, Architecture Decision Records (ADRs), and test specifications, delivering branch-aware project context directly to coding agents like Claude Code, Cursor, and VS Code through the Model Context Protocol (MCP)."
        },
        {
            "q": "How does Reqode deliver context to Claude Code, Cursor, and other agents?",
            "a": "Reqode provides a dedicated Model Context Protocol (MCP) server. When configured in your agent client (e.g., Cursor or Claude Code), the agent dynamically queries feature specifications, architectural boundaries, and acceptance criteria relevant to your current git branch."
        },
        {
            "q": "What is the pricing model and is there a free trial for Reqode?",
            "a": "Reqode Cloud is priced at $19 per user per month. A comprehensive 14-day free trial is provided with no credit card required upfront to evaluate MCP integration and specification workflows."
        },
        {
            "q": "Can QA agents use Reqode to run and log test suites?",
            "a": "Yes. Reqode allows authorized QA agents to retrieve prepared test specifications and automatically record test execution results and validation passes back into the workspace."
        },
        {
            "q": "What is the recommended quickstart setup for Reqode MCP?",
            "a": "Create a workspace at https://reqode.com, draft or import your feature specifications, and connect your AI coding agent using the configuration guide at https://reqode.com/product/mcp."
        }
    ]
}

REQODE_REVIEW = {
    "article_title": "Reqode Architecture & Engineering Dossier: Branch-Aware Context Delivery, Model Context Protocol (MCP), and Agentic Requirements Alignment",
    "reading_time": "6 min read",
    "editorial_verdict_callout": "Reqode provides the missing architectural link in the AI coding revolution: elevating autonomous agents from raw code guessers into disciplined software engineers guided by versioned product specifications and ADRs via MCP.",
    "chapters": [
        {
            "id": "context-deficit-in-autonomous-coding",
            "number": "01",
            "title": "The Context Deficit in Autonomous Coding: Why Repositories Alone Are Insufficient",
            "content": "As autonomous AI coding agents (such as Claude Code, OpenAI Codex, and Cursor) assume increasingly substantial development responsibilities, engineering organizations are encountering a fundamental bottleneck: the context deficit. While modern language models excel at local syntax generation, refactoring, and code completion, their performance degrades when implementing complex, multi-component features. The root cause is not model intelligence, but information opacity. A git repository contains the current implementation artifacts of software, but it rarely preserves the rationale behind architecture decisions, product constraints, edge-case requirements, or business objectives. When an agent is prompted simply to 'build feature X,' it is forced to infer architectural intent from existing code alone, frequently resulting in subtle regressions, violated architectural patterns, or hallucinated requirements. Reqode directly solves this context deficit by introducing a purpose-built workspace where product requirements, Architecture Decision Records (ADRs), and verification criteria live alongside implementation branches."
        },
        {
            "id": "reqode-mcp-branch-aware-pipeline",
            "number": "02",
            "title": "Reqode MCP Architecture: Branch-Aware Context Delivery & Architectural Constraints",
            "content": "Architecturally, Reqode positions itself as the deterministic context engine for developer workstations through the Model Context Protocol (MCP). Rather than expecting developers to manually copy-paste long product requirement documents (PRDs) or system design specifications into agent chat contexts, Reqode exposes an authenticated MCP server interface. When a developer or agent initiates a task on a specific git branch, the Reqode MCP server detects the active working branch and dynamically queries the Reqode Cloud context graph. It injects exactly the relevant feature scope, linked architectural guidelines, dependent service interfaces, and non-functional requirements into the agent's context window. This branch-aware scoping prevents cross-feature context pollution, ensuring that agents operating on experimental branches never ingest unapproved architectural changes from concurrent work streams."
        },
        {
            "id": "closing-verification-loop-qa-agents",
            "number": "03",
            "title": "Closing the Verification Loop: Autonomous QA Agents & Test Specification Ingestion",
            "content": "Beyond code generation, a critical differentiator of Reqode's architecture is its bidirectional verification loop. In standard AI development pipelines, test generation is typically treated as an afterthought—models generate unit tests that mirror the code they just authored, creating confirmation bias that misses core business logic flaws. Reqode decouples test specification from code authoring by linking explicit acceptance criteria and test plans directly to requirements. Through authorized MCP endpoints, autonomous QA agents can independently retrieve prepared test scenarios, execute test runners against the active build, and record granular execution passes, performance benchmarks, and failure traces back into the Reqode workspace. This automated verification loop provides engineering managers with verifiable proof of specification conformance before pull requests are merged."
        },
        {
            "id": "enterprise-roi-strategic-verdict",
            "number": "04",
            "title": "Enterprise ROI Audit, Pricing Economics & Strategic Implementation Verdict",
            "content": "Reqode Cloud is offered under a transparent commercial subscription tier at $19 per user per month, preceded by a 14-day fully featured evaluation trial. In evaluating total cost of ownership (TCO), engineering teams must contrast this predictable per-seat cost against the significant engineering hours currently wasted debugging misaligned AI agent pull requests, rewriting violating architectures, and manually writing agent prompts. By formalizing requirements, ADRs, and QA criteria into an MCP-queryable knowledge substrate, Reqode transforms AI coding assistants from isolated autocomplete utilities into synchronized team members. While teams must commit to maintaining structured specifications, the resulting developer velocity and architectural consistency make Reqode a standout addition to the modern AI-assisted engineering stack."
        }
    ],
    "tool_id": "reqode",
    "model_used": "editorial-team",
    "generated_at": "2026-11-17T06:20:00.000000+00:00"
}

def main():
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # Check if already present
    tools = [t for t in tools if t.get("id") != "reqode"]
    # Insert right at position 1 (prominent top placement)
    tools.insert(1, REQODE_TOOL)

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    print(f"Cataloged Reqode into all_tools.json. Total count: {len(tools)}")

    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews["reqode"] = REQODE_REVIEW
    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)
    print(f"Added editorial review for Reqode into editorial_reviews.json. Total reviews: {len(reviews)}")

if __name__ == "__main__":
    main()
