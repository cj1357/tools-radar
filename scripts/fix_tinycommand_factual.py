# -*- coding: utf-8 -*-
"""
Fix TinyCommand factual corrections:
1. Remove install_command (hosted SaaS, no installation command)
2. Word MCP support as an announced upcoming capability
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
all_tools_file = os.path.join(BASE_DIR, 'data', 'all_tools.json')
editorial_file = os.path.join(BASE_DIR, 'data', 'editorial_reviews.json')

# 1. Update all_tools.json
with open(all_tools_file, 'r', encoding='utf-8') as f:
    tools = json.load(f)

for t in tools:
    if t.get('id') == 'tinycommand':
        t['install_command'] = ""
        t['extensibility'] = "Visual Workflow Canvas & REST API Integrations (Upcoming MCP Support Announced)"
        for feat in t.get('key_features', []):
            if 'mcp' in feat.get('description', '').lower() or 'mcp' in feat.get('title', '').lower():
                feat['description'] = feat['description'].replace("MCP compatibility", "announced upcoming MCP compatibility")
        break

with open(all_tools_file, 'w', encoding='utf-8') as f:
    json.dump(tools, f, ensure_ascii=False, indent=2)

print("SUCCESS: Updated all_tools.json for TinyCommand")

# 2. Update editorial_reviews.json
with open(editorial_file, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

tc_review = reviews.get('tinycommand')
if tc_review:
    for c in tc_review.get('chapters', []):
        if c.get('id') == 'autonomous-agents-and-mcp-extensibility':
            c['content'] = (
                "Beyond deterministic if-this-then-that automation sequences, TinyCommand provides higher-order agentic "
                "capabilities on its Professional tiers. Users can configure and deploy autonomous AI agents endowed with "
                "specific system instructions, persistent working memory, and tool invocation access. These agents can "
                "autonomously execute research tasks, perform targeted web scraping, and draft synthesized customer responses "
                "grounded in team knowledge bases. In alignment with modern agent architectures, TinyCommand has announced "
                "upcoming Model Context Protocol (MCP) server support as a planned capability, designed to eventually enable "
                "external AI assistants to interface with underlying tables and workflows once released."
            )
            break

with open(editorial_file, 'w', encoding='utf-8') as f:
    json.dump(reviews, f, ensure_ascii=False, indent=2)

print("SUCCESS: Updated editorial_reviews.json for TinyCommand")
