"""
Tools Radar - Deep AI Backfill Script
Iterates through all tools in data/all_tools.json and enriches those lacking deep AI fields
(verdict, use_cases, pros, cons, target_audience, comparison_vs_alt, install_command).
Features persistent per-item checkpointing, retry backoff, and 4.2s rate-limit pacing.
"""

import os
import sys
import json
import time
import argparse
import requests
from scraper import load_dotenv, classify_and_structure_ai, classify_and_structure_heuristic

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
MASTER_FILE = os.path.join(DATA_DIR, "all_tools.json")

def backfill(limit: int | None = None, force: bool = False, delay: float = 4.2):
    load_dotenv()
    
    api_key = os.environ.get("AI_API_KEY", "").strip() or os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("[!] Error: No AI_API_KEY or OPENAI_API_KEY detected. Backfill requires active AI credentials.")
        sys.exit(1)

    if not os.path.exists(MASTER_FILE):
        print(f"[!] Error: {MASTER_FILE} not found.")
        sys.exit(1)

    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        tools = json.load(f)

    print("=" * 65)
    print(" Tools Radar - Deep AI Knowledge Backfill")
    print(f" Total tools in database: {len(tools)}")
    print(f" Pacing delay: {delay}s per request (~14 RPM safe)")
    print("=" * 65)

    # Filter targets
    targets = []
    for i, t in enumerate(tools):
        # Needs backfill if missing verdict, pros, or key_features
        needs_work = force or not t.get("verdict") or not t.get("pros") or len(t.get("key_features", [])) < 3
        if needs_work:
            targets.append((i, t))

    print(f"Tools requiring deep AI enrichment: {len(targets)}")
    if limit:
        targets = targets[:limit]
        print(f"Target limit applied: Processing first {len(targets)} tools in this batch.")

    if not targets:
        print("[✓] All tools in database are already 100% enriched with deep AI insights! Nothing to do.")
        return

    success_count = 0
    fail_count = 0

    for idx, (original_index, tool) in enumerate(targets):
        prefix = f"[{idx + 1}/{len(targets)}]"
        name = tool.get("name", tool.get("id"))
        print(f"\n{prefix} Processing '{name}' ({tool.get('id')})...")

        raw_item = {
            "raw_name": tool.get("id"),
            "title": tool.get("name"),
            "url": tool.get("url"),
            "github_url": tool.get("github_url"),
            "raw_description": tool.get("summary") or tool.get("tagline") or "",
            "source": tool.get("source", "github_trending"),
            "stars": tool.get("stars", 0),
            "language": tool.get("tags", [None])[0] if tool.get("tags") else None
        }

        start_t = time.time()
        enriched = classify_and_structure_ai(raw_item)
        duration = time.time() - start_t

        if enriched and enriched.get("verdict"):
            # Merge enriched fields while preserving existing id, stars, date_added, featured status
            tool["name"] = enriched.get("name") or tool["name"]
            tool["tagline"] = enriched.get("tagline") or tool["tagline"]
            tool["summary"] = enriched.get("summary") or tool["summary"]
            tool["category"] = enriched.get("category") or tool["category"]
            tool["tags"] = enriched.get("tags") or tool["tags"]
            tool["pricing_model"] = enriched.get("pricing_model") or tool["pricing_model"]
            tool["primary_alternative"] = enriched.get("primary_alternative")
            tool["is_self_hostable"] = enriched.get("is_self_hostable", tool.get("is_self_hostable", False))
            tool["no_signup_required"] = enriched.get("no_signup_required", tool.get("no_signup_required", False))
            tool["verdict"] = enriched.get("verdict")
            tool["key_features"] = enriched.get("key_features") or tool.get("key_features", [])
            tool["use_cases"] = enriched.get("use_cases") or tool.get("use_cases", [])
            tool["pros"] = enriched.get("pros") or tool.get("pros", [])
            tool["cons"] = enriched.get("cons") or tool.get("cons", [])
            tool["target_audience"] = enriched.get("target_audience")
            tool["comparison_vs_alt"] = enriched.get("comparison_vs_alt")
            tool["install_command"] = enriched.get("install_command")
            if enriched.get("signal_score"):
                tool["signal_score"] = enriched["signal_score"]

            tools[original_index] = tool
            success_count += 1
            print(f"  ✓ Enriched successfully in {duration:.2f}s")
            print(f"    • Verdict: {tool['verdict'][:75]}...")
            print(f"    • Pros: {len(tool.get('pros', []))} | Cons: {len(tool.get('cons', []))} | UseCases: {len(tool.get('use_cases', []))}")

            # Persistent immediate save
            with open(MASTER_FILE, "w", encoding="utf-8") as f:
                json.dump(tools, f, indent=2, ensure_ascii=False)

        else:
            fail_count += 1
            print(f"  ✗ AI enrichment failed (took {duration:.2f}s). Skipping update for this item.")

        # Rate-limiting sleep
        if idx + 1 < len(targets):
            time.sleep(delay)

    print("\n" + "=" * 65)
    print(f"Backfill Batch Complete:")
    print(f"  • Successfully Enriched : {success_count}")
    print(f"  • Failed/Skipped        : {fail_count}")
    print(f"  • Database File Saved   : {MASTER_FILE}")
    print("=" * 65)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backfill AI fields for existing tools.")
    parser.add_argument("--limit", type=int, default=None, help="Max number of tools to process in this run")
    parser.add_argument("--force", action="store_true", help="Force re-enrichment of tools even if already enriched")
    parser.add_argument("--delay", type=float, default=4.2, help="Delay in seconds between AI calls")
    args = parser.parse_args()

    backfill(limit=args.limit, force=args.force, delay=args.delay)
