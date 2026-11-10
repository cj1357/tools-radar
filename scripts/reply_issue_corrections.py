# -*- coding: utf-8 -*-
"""
Reply to @akii-technologies on GitHub Issues #3 and #4 confirming the requested corrections.
"""

import subprocess
import urllib.request
import urllib.error
import json
import sys

def get_github_token():
    try:
        p = subprocess.Popen(
            ["git", "credential", "fill"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, _ = p.communicate("protocol=https\nhost=github.com\n")
        for line in out.splitlines():
            if line.startswith("password="):
                return line.split("=", 1)[1].strip()
    except Exception as e:
        print("Error getting token from git credential manager:", e)
    return None

TOKEN = get_github_token()
if not TOKEN:
    print("Error: Could not retrieve GitHub token.")
    sys.exit(1)

REPO = "cj1357/tools-radar"
BASE_URL = f"https://api.github.com/repos/{REPO}/issues"

REPLIES = [
    {
        "number": 3,
        "comment": """Hi @akii-technologies,

Thank you for the quick clarification! We have updated both lines in the review and database accordingly:

1. **Telemetry:** Updated from "zero external telemetry" to explicitly state that the plugin includes anonymized install telemetry with an opt-out.
2. **On-Demand Engine Queries:** Clarified that SEO and GEO checks run on demand using public web signals or optional Ahrefs Brand Radar data, with no direct queries sent to AI engines.

The updated dossier is already live on ToolsRadar:
👉 [https://lordorange.top/tool/akii-seo-ai-search-optimizer/](https://lordorange.top/tool/akii-seo-ai-search-optimizer/)

Thanks again for helping keep the technical details accurate!
"""
    },
    {
        "number": 4,
        "comment": """Hi @akii-technologies,

Thank you for the pricing clarification! We have updated the review, pros, and FAQ sections accordingly:

- Updated "2,000-credit free trial" to **"2,000 free welcome credits once per verified customer"**.
- Noted that no card is required, and the welcome credits never expire or refill.

The updated dossier is already live on ToolsRadar:
👉 [https://lordorange.top/tool/revenue-scout/](https://lordorange.top/tool/revenue-scout/)

Thank you for the feedback!
"""
    }
]

def post_comment(issue_num, body):
    url = f"{BASE_URL}/{issue_num}/comments"
    data = json.dumps({"body": body}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "ToolsRadar-Bot/1.0",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.load(resp)
            print(f"Comment posted on #{issue_num}: {res.get('html_url')}")
            return True
    except urllib.error.HTTPError as e:
        print(f"Failed to post comment on #{issue_num}: {e.code} - {e.read().decode('utf-8')}")
        return False

def main():
    for item in REPLIES:
        num = item["number"]
        print(f"Replying on Issue #{num}...")
        post_comment(num, item["comment"])

if __name__ == "__main__":
    main()
