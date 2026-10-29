#!/usr/bin/env python3
"""
Tools Radar - AI Editorial Review Batch Generator
Generates in-depth 4-chapter technical dossiers (~850 words) for tools using LLM (Gemini / OpenAI / New API).
Saves directly into data/editorial_reviews.json.
Supports single-tool generation, limit batching, and resuming.
"""

import os
import sys
import json
import time
import datetime
import argparse
import requests

# Ensure proper stdout encoding on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
MASTER_TOOLS_FILE = os.path.join(DATA_DIR, "all_tools.json")
EDITORIAL_REVIEWS_FILE = os.path.join(DATA_DIR, "editorial_reviews.json")

def load_dotenv(env_path=None):
    if env_path is None:
        env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip("'\"")
                if k and k not in os.environ:
                    os.environ[k] = v

load_dotenv()

def generate_editorial_review_ai(tool: dict, api_key: str, api_base: str, model: str) -> dict | None:
    """Calls OpenAI-compatible / New API / Gemini endpoint to produce an authoritative ~850-word engineering dossier."""
    base = api_base.rstrip("/")
    if not base.endswith("/v1"):
        endpoint = f"{base}/v1/chat/completions"
    else:
        endpoint = f"{base}/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    tool_name = tool.get("name", "")
    tagline = tool.get("tagline", "")
    summary = tool.get("summary", "")
    category = tool.get("category", "")
    pricing = tool.get("pricing_model", "")
    alt = tool.get("primary_alternative")
    is_self_host = tool.get("is_self_hostable", False)
    github_url = tool.get("github_url")
    verdict = tool.get("verdict", "")
    key_features = tool.get("key_features", [])
    pros = tool.get("pros", [])
    cons = tool.get("cons", [])

    features_summary = "; ".join([f"{f.get('title')}: {f.get('description')}" for f in key_features if isinstance(f, dict)])
    pros_summary = "; ".join([str(p) for p in pros[:3]])
    cons_summary = "; ".join([str(c) for c in cons[:2]])

    system_prompt = (
        "You are the Lead Technology Editor & Principal Software Architect at ToolsRadar.\n"
        "Your task is to write an authoritative, in-depth technical dossier (~800 to 950 words total across 4 distinct chapters) evaluating the software tool provided.\n"
        "Your tone must be objective, deeply technical, nuanced, and analytical (Wirecutter/TechRadar meets ACM Queue style).\n"
        "Avoid generic filler or fluffy marketing buzzwords. Focus on real architecture, developer experience, trade-offs, and economics.\n\n"
        "Return ONLY a valid JSON object matching the exact schema below:\n"
        "{\n"
        f'  "article_title": "{tool_name} Architecture & Engineering Dossier: Evaluating [Specific Superpower/Niche]",\n'
        '  "reading_time": "4 min read • ~880 words",\n'
        '  "section1_architecture": "Chapter 1 (~180-220 words): Deep dive into technical underpinnings, stack architecture, runtime responsibilities, database/persistence choices, state management, protocols, and security boundaries.",\n'
        '  "section2_ergonomics": "Chapter 2 (~180-220 words): Detailed developer experience (DX), day-to-day workflow velocity, setup/onboarding friction, configuration ergonomics, and operational maintenance trade-offs.",\n'
        '  "section3_licensing_tco": "Chapter 3 (~180-220 words): Total cost of ownership (TCO), software licensing model analysis, developer hour opportunity costs vs building in-house, and direct economic comparison against commercial alternatives.",\n'
        '  "section4_verdict": "Chapter 4 (~180-220 words): Production readiness assessment, target team profile (who should adopt vs who should avoid), and ToolsRadar editorial conviction.",\n'
        '  "editorial_verdict_callout": "1 punchy, authoritative summary sentence encapsulating the core architectural bottom line"\n'
        "}\n\n"
        "Constraints:\n"
        "- Pure JSON output only, no markdown code block fences.\n"
        "- Respect the factual constraints of the product (e.g. if it is a commercial starter or source code license, do not claim it has a free tier or hosted playground)."
    )

    user_prompt = (
        f"Product: {tool_name}\n"
        f"Tagline: {tagline}\n"
        f"Category: {category}\n"
        f"Pricing: {pricing}\n"
        f"Alternative: {alt or 'N/A'}\n"
        f"Self-Hostable: {'Yes' if is_self_host else 'No'}\n"
        f"GitHub: {github_url or 'N/A'}\n"
        f"Summary: {summary}\n"
        f"Key Features: {features_summary or 'Standard modern architecture'}\n"
        f"Known Pros: {pros_summary or 'High performance'}\n"
        f"Known Cons: {cons_summary or 'Requires configuration'}\n"
        f"Initial Verdict: {verdict or 'Recommended for modern engineering stacks'}"
    )

    payload = {
        "model": model,
        "temperature": 0.3,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    max_retries = 2
    for attempt in range(max_retries):
        try:
            resp = requests.post(endpoint, json=payload, headers=headers, timeout=45)
            if resp.status_code == 429:
                print(f"    [Rate Limit 429] Waiting 10s before retry (attempt {attempt+1}/{max_retries})...")
                time.sleep(10)
                continue
            if resp.status_code != 200:
                print(f"    [API Error] HTTP {resp.status_code}: {resp.text[:140]}")
                return None

            content = resp.json()["choices"][0]["message"]["content"].strip()
            if content.startswith("```json"): content = content[7:]
            if content.startswith("```"): content = content[3:]
            if content.endswith("```"): content = content[:-3]
            review_data = json.loads(content.strip())

            review_data["tool_id"] = tool["id"]
            review_data["model_used"] = model
            review_data["generated_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            return review_data
        except Exception as e:
            print(f"    [AI Exception on attempt {attempt+1}]: {e}")
            time.sleep(2)

    return None

def main():
    parser = argparse.ArgumentParser(description="Generate AI Editorial Reviews for ToolsRadar tools.")
    parser.add_argument("--slug", type=str, help="Generate for a specific tool ID (slug).")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of tools to generate reviews for.")
    parser.add_argument("--all", action="store_true", help="Generate for all pending tools.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing reviews.")
    parser.add_argument("--delay", type=float, default=4.2, help="Delay between API requests in seconds (default: 4.2s for 15 RPM free tier).")
    args = parser.parse_args()

    api_key = os.environ.get("AI_API_KEY", "").strip() or os.environ.get("OPENAI_API_KEY", "").strip() or os.environ.get("GEMINI_API_KEY", "").strip()
    api_base = os.environ.get("AI_API_BASE", "https://api.openai.com/v1").strip()
    model = os.environ.get("AI_MODEL", "google/gemini-3.5-flash-lite").strip()

    if not api_key:
        print("[Error] No AI_API_KEY, OPENAI_API_KEY, or GEMINI_API_KEY found in environment or .env file.")
        print("Please configure your API key in .env or provide it via environment variable.")
        sys.exit(1)

    print("=" * 65)
    print("ToolsRadar - AI Editorial Review Batch Generator")
    print(f"Base: {api_base} | Model: {model} | Delay: {args.delay}s")
    print("=" * 65)

    if not os.path.exists(MASTER_TOOLS_FILE):
        print(f"[Error] Tools master file not found at: {MASTER_TOOLS_FILE}")
        sys.exit(1)

    with open(MASTER_TOOLS_FILE, "r", encoding="utf-8") as f:
        all_tools = json.load(f)

    reviews = {}
    if os.path.exists(EDITORIAL_REVIEWS_FILE):
        try:
            with open(EDITORIAL_REVIEWS_FILE, "r", encoding="utf-8") as f:
                reviews = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load existing reviews: {e}")
            reviews = {}

    print(f"Total tools in database : {len(all_tools)}")
    print(f"Existing AI reviews     : {len(reviews)}")
    pending_count = len([t for t in all_tools if t["id"] not in reviews])
    print(f"Pending reviews needed  : {pending_count}")
    print("-" * 65)

    targets = []
    if args.slug:
        matched = [t for t in all_tools if t["id"] == args.slug]
        if not matched:
            print(f"[Error] Tool with slug '{args.slug}' not found.")
            sys.exit(1)
        targets = matched
    else:
        for t in all_tools:
            if args.overwrite or t["id"] not in reviews:
                targets.append(t)
        if args.limit:
            targets = targets[:args.limit]

    if not targets:
        print("No tools require review generation. (All target tools already have AI reviews. Use --overwrite to regenerate).")
        return

    print(f"Starting generation for {len(targets)} tool(s)...\n")

    success_count = 0
    fail_count = 0

    for idx, tool in enumerate(targets, 1):
        tid = tool["id"]
        tname = tool["name"]
        print(f"[{idx}/{len(targets)}] Generating AI Editorial Review for '{tname}' ({tid})...")

        review = generate_editorial_review_ai(tool, api_key, api_base, model)
        if review:
            reviews[tid] = review
            success_count += 1
            # Atomic save after every single generation
            with open(EDITORIAL_REVIEWS_FILE, "w", encoding="utf-8") as f:
                json.dump(reviews, f, indent=2, ensure_ascii=False)
            print(f"    ✓ Successfully saved! (Total in DB: {len(reviews)})")
        else:
            fail_count += 1
            print(f"    ✗ Generation failed or skipped.")

        if idx < len(targets):
            time.sleep(args.delay)

    print("\n" + "=" * 65)
    print(f"Batch Generation Complete:")
    print(f"  • Successfully Generated : {success_count}")
    print(f"  • Failed/Skipped          : {fail_count}")
    print(f"  • Total Reviews in DB     : {len(reviews)}")
    print(f"  • Saved File              : {EDITORIAL_REVIEWS_FILE}")
    print("=" * 65)

if __name__ == "__main__":
    main()
