# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

tools = json.load(open('d:/_projectsTYweb/tools-radar/data/all_tools.json', 'r', encoding='utf-8'))
reviews = json.load(open('d:/_projectsTYweb/tools-radar/data/editorial_reviews.json', 'r', encoding='utf-8'))

akii_tool = next((t for t in tools if t['id'] == 'akii-seo-ai-search-optimizer'), None)
rs_tool = next((t for t in tools if t['id'] == 'revenue-scout'), None)
akii_rev = reviews.get('akii-seo-ai-search-optimizer')
rs_rev = reviews.get('revenue-scout')

print("=== Akii in all_tools.json ===")
if akii_tool:
    print("pros:", akii_tool.get("pros"))
    print("summary:", akii_tool.get("summary"))
    print("key_features:", akii_tool.get("key_features"))
    print("comparison_vs_alt:", akii_tool.get("comparison_vs_alt"))

print("\n=== Akii in editorial_reviews.json ===")
if akii_rev:
    for ch in akii_rev.get("chapters", []):
        print(f"Chapter {ch.get('number')}: {ch.get('title')}")
        print(f"Content: {ch.get('content')}\n")

print("=== Revenue Scout in all_tools.json ===")
if rs_tool:
    print("pros:", rs_tool.get("pros"))
    print("faqs:", rs_tool.get("faqs"))

print("\n=== Revenue Scout in editorial_reviews.json ===")
if rs_rev:
    for ch in rs_rev.get("chapters", []):
        if "2,000" in ch.get("content", ""):
            print(f"Chapter {ch.get('number')}: {ch.get('title')}")
            print(f"Content: {ch.get('content')}\n")
