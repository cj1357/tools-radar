# -*- coding: utf-8 -*-
"""
Add SkillPi to all_tools.json, editorial_reviews.json, and Layout.astro footer
Mutual link exchange with Charles <charles@outreach.skillpi.com> on 2026-11-11
"""

import json
import os
import re

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
all_tools_path = os.path.join(root_dir, "data", "all_tools.json")
reviews_path = os.path.join(root_dir, "data", "editorial_reviews.json")
layout_path = os.path.join(root_dir, "site", "src", "layouts", "Layout.astro")

SKILLPI_TOOL = {
    "id": "skillpi",
    "name": "SkillPi",
    "tagline": "One Marketplace. Infinite Skills. — a marketplace and directory for AI agent skills",
    "summary": "SkillPi is an AI agent skills marketplace and directory built to help developers discover, review, and install task-specific skills for modern AI coding assistants including Claude Code, Codex, Cursor, Cline, and Antigravity. Built around the core philosophy of 'find the right skill, and use it successfully the first time', SkillPi categorizes modular agent capabilities across development, testing, browser automation, data analysis, and technical copywriting—providing verified setups, source code transparency, licensing details, and reproducible quickstart prompt snippets.",
    "url": "https://skillpi.com",
    "github_url": "",
    "source": "submission",
    "category": "ai-agents",
    "tags": [
        "AI Agents",
        "Skills Marketplace",
        "Claude Code",
        "Cursor",
        "Codex",
        "Developer Tools",
        "Prompt Engineering",
        "Agent Workflows"
    ],
    "pricing_model": "Free",
    "stars": 0,
    "primary_alternative": "Vercel Labs Skills",
    "is_self_hostable": False,
    "no_signup_required": True,
    "signal_score": 89,
    "verdict": "An indispensable ecosystem marketplace for AI agent skills, organizing verified setups and modular prompt libraries for Claude Code, Cursor, and autonomous coding agents.",
    "key_features": [
        {
            "title": "Task & Scene-Based Skills Taxonomy",
            "description": "Browse hundreds of curated agent skills structured by real-world developer tasks: code review, browser automation, security testing, and data analysis."
        },
        {
            "title": "Cross-Agent Multi-Runtime Compatibility",
            "description": "Pre-configured setup instructions and launch prompts tailored for Claude Code, Codex, Cursor, Cline, Continue, and Antigravity."
        },
        {
            "title": "Verified Setup & Execution Evidence",
            "description": "Every listed skill links directly to upstream GitHub repositories, licensing terms, and tested prompt recipes for predictable agent execution."
        }
    ],
    "use_cases": [
        "Software engineers equipping Claude Code and Cursor with specialized domain skills (e.g., exploratory data analysis, canvas design, statistical visualization).",
        "Development teams standardizing reusable agent toolsets across junior and senior engineers without rewriting system prompt files.",
        "Agent builders and skill authors publishing community agent packages to gain adoption across multiple autonomous coding runtimes."
    ],
    "pros": [
        "Organized by concrete developer tasks and professions rather than arbitrary keyword tags",
        "Free to browse and use with zero mandatory signup required for exploring skills",
        "Direct setup recipes for major coding agents (Claude Code, Codex, Cursor, Cline, Antigravity)"
    ],
    "cons": [
        "Execution performance ultimately depends on the capabilities of the underlying LLM model",
        "Third-party upstream skill repositories may have varying maintenance cadences"
    ],
    "target_audience": "AI engineers, prompt engineers, developer advocates, and software teams building with autonomous coding agents (Claude Code, Cursor, Codex).",
    "comparison_vs_alt": "While unorganized GitHub awesome-lists require manual curation and trial-and-error, SkillPi provides a structured directory with verified setup instructions, category scenes, and direct launch prompts for all major agent environments.",
    "install_command": "Explore and install skills at https://skillpi.com/skills",
    "date_added": "2026-11-11",
    "featured": True,
    "faqs": [
        {
            "q": "What is SkillPi?",
            "a": "SkillPi is a curated marketplace and directory for AI agent skills, designed to help developers find and install the right skills for Claude Code, Cursor, Codex, and other coding assistants."
        },
        {
            "q": "Which AI agents and coding tools are supported?",
            "a": "SkillPi supports Claude Code, OpenAI Codex, Cursor, Cline, Continue, Antigravity, Roo Code, Goose, OpenHands, and more."
        },
        {
            "q": "Is SkillPi free to use?",
            "a": "Yes, SkillPi is free to browse and explore. Developers can discover skills, inspect setup documentation, and copy integration snippets without fees."
        },
        {
            "q": "How do I install a skill from SkillPi?",
            "a": "Each skill on SkillPi includes clear installation instructions, setup commands, and starter prompts tailored for your chosen AI agent runtime."
        }
    ]
}

SKILLPI_REVIEW = {
    "article_title": "SkillPi Architecture & Ecosystem Dossier: Modular Skills Taxonomy, Multi-Agent Runtimes, and Developer Curation",
    "reading_time": "6 min read",
    "editorial_verdict_callout": "SkillPi delivers the missing package directory for autonomous coding agents: a task-driven skills marketplace that replaces bloated system prompts with verified, on-demand agent competencies.",
    "chapters": [
        {
            "id": "modular-skills-shift",
            "number": "01",
            "title": "The Rise of Modular Agent Skills: Beyond Monolithic System Prompts",
            "content": (
                "Early AI coding workflows relied on monolithic prompt files (such as 2,000-line .cursorrules or massive system instruction headers). "
                "However, stuffing an agent's context window with every conceivable guideline causes instruction degradation, token bloat, and conflicting behaviors. "
                "The industry has rapidly shifted toward modular, task-triggered 'skills'—discrete, on-demand operational routines pioneered by frameworks like "
                "Anthropic's skills architecture, Claude Code plugins, and agentic customization standards. SkillPi emerged to address the discovery bottleneck "
                "in this new paradigm: creating a unified, authoritative catalog where developers can find pre-tested agent skills and install them with zero guesswork."
            )
        },
        {
            "id": "taxonomy-scenes",
            "number": "02",
            "title": "SkillPi Architecture: Task Taxonomy, Scene Categorization, and Multi-Agent Setup Guides",
            "content": (
                "Rather than organizing skills by arbitrary buzzwords, SkillPi structures its directory around real-world developer workflows (termed 'Scenes'). "
                "Engineers can filter skills across Development & Operations (code review, testing, security), Systems & Automation (browser manipulation, workflow runners), "
                "Data & Analytics (database querying, statistical visualization), and Content Engineering. Crucially, each skill listing abstracts multi-runtime integration: "
                "a single skill page provides explicit, copy-paste setup recipes for Claude Code, OpenAI Codex, Cursor, Cline, and Antigravity, eliminating platform lock-in."
            )
        },
        {
            "id": "interoperability-standardization",
            "number": "03",
            "title": "Ecosystem Interoperability: Bridging Claude Code, Cursor, and Autonomous Coding Workflows",
            "content": (
                "The fragmentation of agent ecosystems poses a serious hurdle for skill authors: maintaining separate documentation for terminal CLI agents (Claude Code, Kiro) "
                "versus IDE extensions (Cursor, Roo Code, Continue) is tedious. SkillPi serves as an interoperability bridge. By validating source repositories against standard "
                "manifest schemas and providing reproducible verification evidence, SkillPi ensures that a frontend design skill or SQL optimization skill functions reliably "
                "regardless of whether the host environment is a terminal session or a GUI editor."
            )
        },
        {
            "id": "community-governance",
            "number": "04",
            "title": "Community Curation, License Transparency & Editorial Verdict",
            "content": (
                "SkillPi strikes an exemplary balance between community openness and technical curation. Every skill entry provides transparent attribution, licensing terms, "
                "and direct links to upstream repositories. For software engineering teams looking to elevate their AI assistants from generic chat responders to specialized "
                "domain experts, SkillPi provides an indispensable springboard. By establishing an organized, trustworthy hub for agent skills, SkillPi accelerates "
                "the broader developer ecosystem toward modular, composable artificial intelligence."
            )
        }
    ]
}

def main():
    # 1. Update all_tools.json
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)

    existing_idx = next((i for i, t in enumerate(tools) if t.get("id") == "skillpi"), None)
    if existing_idx is not None:
        print("Updating existing skillpi in all_tools.json...")
        tools[existing_idx] = SKILLPI_TOOL
    else:
        print("Prepending skillpi to all_tools.json...")
        tools.insert(0, SKILLPI_TOOL)

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    print(f"all_tools.json updated. Total tools: {len(tools)}")

    # 2. Update editorial_reviews.json
    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews["skillpi"] = SKILLPI_REVIEW
    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)
    print("editorial_reviews.json updated with skillpi review.")

    # 3. Update Layout.astro footer
    with open(layout_path, "r", encoding="utf-8") as f:
        layout_content = f.read()

    # Add Ecosystem & Partners column if not already present
    if "https://skillpi.com" not in layout_content:
        old_trust_col = """          <div class="footer-col">
            <span class="footer-col-title">Trust & Legal</span>
            <ul class="footer-col-links">
              <li><a href="/about">About ToolsRadar</a></li>
              <li><a href="/methodology">Editorial Methodology</a></li>
              <li><a href="/contact">Contact & Inquiries</a></li>
              <li><a href="/privacy">Privacy Policy</a></li>
              <li><a href="/terms">Terms of Service</a></li>
              <li><a href="https://github.com/cj1357/tools-radar" target="_blank" rel="noopener noreferrer">Source Code ↗</a></li>
            </ul>
          </div>"""

        new_cols = """          <div class="footer-col">
            <span class="footer-col-title">Trust & Legal</span>
            <ul class="footer-col-links">
              <li><a href="/about">About ToolsRadar</a></li>
              <li><a href="/methodology">Editorial Methodology</a></li>
              <li><a href="/contact">Contact & Inquiries</a></li>
              <li><a href="/privacy">Privacy Policy</a></li>
              <li><a href="/terms">Terms of Service</a></li>
              <li><a href="https://github.com/cj1357/tools-radar" target="_blank" rel="noopener noreferrer">Source Code ↗</a></li>
            </ul>
          </div>

          <div class="footer-col">
            <span class="footer-col-title">Ecosystem & Partners</span>
            <ul class="footer-col-links">
              <li><a href="https://skillpi.com" target="_blank" rel="noopener" title="SkillPi - AI Agent Skills Marketplace for Claude Code, Codex & Cursor">SkillPi (Agent Skills) ↗</a></li>
              <li><a href="mailto:hello@lordorange.top?subject=Link%20Exchange%20Inquiry">Exchange Links ↗</a></li>
            </ul>
          </div>"""

        # Update CSS for 4 columns on desktop
        old_css = """      @media (min-width: 600px) {
        .footer-nav-grid {
          grid-template-columns: repeat(3, 1fr);
        }
      }"""

        new_css = """      @media (min-width: 600px) {
        .footer-nav-grid {
          grid-template-columns: repeat(2, 1fr);
        }
      }

      @media (min-width: 860px) {
        .footer-nav-grid {
          grid-template-columns: repeat(4, 1fr);
        }
      }"""

        layout_norm = layout_content.replace("\r\n", "\n")
        assert old_trust_col.replace("\r\n", "\n") in layout_norm, "old_trust_col not found"
        assert old_css.replace("\r\n", "\n") in layout_norm, "old_css not found"

        layout_norm = layout_norm.replace(old_trust_col.replace("\r\n", "\n"), new_cols.replace("\r\n", "\n"))
        layout_norm = layout_norm.replace(old_css.replace("\r\n", "\n"), new_css.replace("\r\n", "\n"))

        is_crlf = "\r\n" in layout_content
        final_layout = layout_norm.replace("\n", "\r\n") if is_crlf else layout_norm

        with open(layout_path, "w", encoding="utf-8") as f:
            f.write(final_layout)
        print("Layout.astro footer successfully updated with Ecosystem & Partners!")
    else:
        print("SkillPi link already present in Layout.astro.")

if __name__ == "__main__":
    main()
