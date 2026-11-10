# -*- coding: utf-8 -*-
"""
Apply author corrections for Akii SEO & AI Search Optimizer and Revenue Scout
based on feedback from @akii-technologies on GitHub Issues #3 and #4.
"""

import json
import os

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
all_tools_path = os.path.join(data_dir, "all_tools.json")
reviews_path = os.path.join(data_dir, "editorial_reviews.json")

def update_akii(tools, reviews):
    # 1. Update all_tools.json
    akii = next((t for t in tools if t.get("id") == "akii-seo-ai-search-optimizer"), None)
    if akii:
        akii["pros"] = [
            "100% free and open-source under MIT license, designed natively for the Claude Code plugin ecosystem",
            "Comprehensive suite containing 12 skills, 5 autonomous agents, and 3 slash commands in one package",
            "Zero hosted service backend—runs on demand within Claude Code with anonymized, opt-out install telemetry and no direct queries to AI engines"
        ]
        for feat in akii.get("key_features", []):
            if "GEO & AI Search Visibility" in feat.get("title", ""):
                feat["description"] = "Evaluate domain positioning for AI search visibility (GEO/AEO) on demand using public web signals and optional Ahrefs Brand Radar data, with no direct queries to AI engines."
        print("Updated Akii in all_tools.json")

    # 2. Update editorial_reviews.json
    rev = reviews.get("akii-seo-ai-search-optimizer")
    if rev:
        for ch in rev.get("chapters", []):
            if ch.get("number") == "03":
                ch["content"] = (
                    "As generative AI search engines—including Perplexity, ChatGPT Search, and Google AI Overviews—transform how users discover software and technical solutions, "
                    "traditional keyword density strategies are becoming obsolete. Akii addresses the emerging disciplines of Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO). "
                    "All SEO and GEO checks run strictly on demand using public web signals or optional Ahrefs Brand Radar data (with no direct queries sent to AI engines), "
                    "analyzing how LLM synthesis models extract factual entities from a website's semantic markup to provide actionable recommendations for entity graph clarity, "
                    "structured JSON-LD references, and brand citation authority."
                )
            if ch.get("number") == "04":
                ch["content"] = (
                    "Akii: SEO & AI Search Optimizer represents an exemplary developer utility for modern AI agent environments. "
                    "By delivering 100% free, MIT-licensed source code (with anonymized, opt-out install telemetry only) and no mandatory cloud subscriptions, it respects developer autonomy. "
                    "For software engineers building Astro, Next.js, or static web architectures who want continuous on-demand SEO and GEO verification without leaving their command line, "
                    "Akii is an indispensable addition to the Claude Code toolkit."
                )
        print("Updated Akii in editorial_reviews.json")

def update_revenue_scout(tools, reviews):
    # 1. Update all_tools.json
    rs = next((t for t in tools if t.get("id") == "revenue-scout"), None)
    if rs:
        rs["pros"] = [
            "Monitors 7 major social channels in one unified interface, eliminating siloed platform monitoring",
            "2,000 free welcome credits once per verified customer (no card required, never expires or refills), plus non-expiring purchased credits",
            "Emphasizes human-in-the-loop review, preserving brand reputation and community authenticity"
        ]
        for faq in rs.get("faqs", []):
            if "pricing model" in faq.get("q", "").lower():
                faq["a"] = "Each verified customer receives 2,000 free welcome credits once with no credit card required. These free credits never expire or refill. Monthly plans start at $49, with non-expiring credit top-ups starting at $15."
        print("Updated Revenue Scout in all_tools.json")

    # 2. Update editorial_reviews.json
    rev = reviews.get("revenue-scout")
    if rev:
        for ch in rev.get("chapters", []):
            if ch.get("number") == "03":
                ch["content"] = (
                    "To prevent brand damage and community alienation caused by automated bot replies, Revenue Scout enforces a strict human-in-the-loop workflow. "
                    "The platform drafts proposed responses tailored to the conversational context of the source thread. Operators can inspect, adjust, and approve drafts before posting manually, "
                    "ensuring brand authenticity and community compliance. With non-expiring purchased credit pools and 2,000 free welcome credits once per verified customer (no credit card required, "
                    "never expiring or refilling), the platform provides risk-free onboarding for early-stage teams."
                )
        print("Updated Revenue Scout in editorial_reviews.json")

def main():
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)
    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    update_akii(tools, reviews)
    update_revenue_scout(tools, reviews)

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)

    print("All editorial corrections applied successfully!")

if __name__ == "__main__":
    main()
