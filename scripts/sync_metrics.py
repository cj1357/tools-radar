"""
Tools Radar - GitHub Metrics & Stars Synchronizer
Fetches live stars and repository metrics directly from the GitHub REST API without burning LLM tokens.
Recalculates traction/signal score to keep the leaderboard fresh and accurate.
Supports GITHUB_TOKEN authentication (5,000 req/hr) or unauthenticated fallback (60 req/hr).
"""

import os
import sys
import re
import json
import time
import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
MASTER_FILE = os.path.join(DATA_DIR, "all_tools.json")

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

def extract_github_repo(url: str | None) -> str | None:
    if not url or "github.com" not in url:
        return None
    match = re.search(r"github\.com/([^/]+)/([^/#?]+)", url)
    if match:
        owner, repo = match.group(1), match.group(2)
        repo = repo.rstrip(".git")
        return f"{owner}/{repo}"
    return None

def compute_signal_score(tool: dict) -> int:
    stars = tool.get("stars", 0)
    source = tool.get("source", "")
    is_self_host = tool.get("is_self_hostable", False)
    alt = tool.get("primary_alternative")

    base = 65
    if stars > 10000:
        base += 25
    elif stars > 1000:
        base += 18
    elif stars > 100:
        base += 10
    elif stars > 20:
        base += 5

    if is_self_host:
        base += 4
    if alt:
        base += 3
    if source == "github_trending":
        base += 3
    elif source == "producthunt":
        base += 2

    return min(base, 99)

def sync_metrics():
    print("=" * 60)
    print(" Tools Radar - GitHub Metrics Synchronizer")
    print("=" * 60)

    if not os.path.exists(MASTER_FILE):
        print(f"Error: {MASTER_FILE} not found.")
        sys.exit(1)

    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        tools = json.load(f)

    print(f"Loaded {len(tools)} tools from database.")

    github_token = os.environ.get("GITHUB_TOKEN", "").strip()
    headers = {
        "User-Agent": "ToolsRadar-MetricsSync",
        "Accept": "application/vnd.github.v3+json"
    }
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"
        print("[Auth Mode] GITHUB_TOKEN detected. High rate limit enabled (5,000 req/hr).")
    else:
        print("[Unauthenticated Mode] No GITHUB_TOKEN found. Limited to 60 req/hr.")

    session = requests.Session()
    session.headers.update(headers)

    updated_count = 0
    star_gain_total = 0
    checked_count = 0

    for i, tool in enumerate(tools):
        gh_url = tool.get("github_url") or (tool.get("url") if "github.com" in tool.get("url", "") else None)
        repo_path = extract_github_repo(gh_url)
        if not repo_path:
            continue

        checked_count += 1
        old_stars = tool.get("stars", 0)
        api_url = f"https://api.github.com/repos/{repo_path}"

        try:
            resp = session.get(api_url, timeout=10)
            if resp.status_code == 403 or resp.status_code == 429:
                print(f"\n[Rate Limit Exceeded] HTTP {resp.status_code}. Stopping sync to preserve quota.")
                break
            if resp.status_code == 404:
                # Repo might be private or renamed
                continue
            if resp.status_code != 200:
                print(f"  [{repo_path}] HTTP {resp.status_code}: {resp.text[:80]}")
                continue

            repo_data = resp.json()
            new_stars = repo_data.get("stargazers_count", old_stars)

            # Update fields
            tool["stars"] = new_stars
            if "forks_count" in repo_data:
                tool["forks"] = repo_data.get("forks_count")

            # Recalculate signal score
            new_signal = compute_signal_score(tool)
            tool["signal_score"] = new_signal

            if new_stars != old_stars:
                diff = new_stars - old_stars
                star_gain_total += diff
                updated_count += 1
                diff_str = f"+{diff}" if diff > 0 else str(diff)
                print(f"  [{checked_count}] {repo_path}: {old_stars} -> {new_stars} ({diff_str}) | Score: {new_signal}")
            else:
                print(f"  [{checked_count}] {repo_path}: {new_stars} stars (unchanged)")

            # Polite pacing (0.2s between calls)
            time.sleep(0.2)

        except Exception as e:
            print(f"  Error querying {repo_path}: {e}")

    print("\n" + "-" * 50)
    print("Metrics Sync Completed:")
    print(f"  • Repos Checked   : {checked_count}")
    print(f"  • Tools Updated   : {updated_count}")
    print(f"  • Net Stars Delta : +{star_gain_total if star_gain_total > 0 else star_gain_total}")
    print("-" * 50)

    # Save back to MASTER_FILE
    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)

    print(f"Saved refreshed metrics to {MASTER_FILE} successfully!")

if __name__ == "__main__":
    sync_metrics()
