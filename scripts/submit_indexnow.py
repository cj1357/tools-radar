# -*- coding: utf-8 -*-
"""
IndexNow Real-Time SEO Push Script for ToolsRadar.
Instantly notifies Microsoft Bing, Yandex, Naver, and Seznam about new and updated pages.
"""

import json
import os
import sys
import urllib.request
import urllib.error

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HOST = "lordorange.top"
KEY = "48a17684074c4314b1ce3b3135bf51d6"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"

def gather_urls():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tools_path = os.path.join(base_dir, "data", "all_tools.json")
    
    urls = [
        f"https://{HOST}/",
        f"https://{HOST}/tag",
        f"https://{HOST}/best",
        f"https://{HOST}/guides",
        f"https://{HOST}/vs",
        f"https://{HOST}/category/ai-agents",
        f"https://{HOST}/category/developer-tools",
        f"https://{HOST}/category/open-source",
    ]

    if os.path.exists(tools_path):
        with open(tools_path, "r", encoding="utf-8") as f:
            tools = json.load(f)

        # Include recent tools (first 60 newest)
        for t in tools[:60]:
            urls.append(f"https://{HOST}/tool/{t['id']}")

        # Include top tags
        tag_counts = {}
        for t in tools:
            for tag in t.get("tags", []):
                s = tag.strip().lower().replace(" ", "-")
                if s and len(s) >= 2:
                    tag_counts[s] = tag_counts.get(s, 0) + 1
        
        top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:30]
        for tag_slug, count in top_tags:
            if count >= 3:
                urls.append(f"https://{HOST}/tag/{tag_slug}")

    # Remove duplicates
    seen = set()
    unique_urls = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique_urls.append(u)

    return unique_urls

def submit_urls(urls):
    print(f"Submitting {len(urls)} URLs to IndexNow ({INDEXNOW_ENDPOINT})...")
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "ToolsRadar-IndexNow/1.0"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status_code = resp.getcode()
            print(f"[SUCCESS] IndexNow accepted payload. HTTP Status: {status_code}")
            return True
    except urllib.error.HTTPError as e:
        # IndexNow returns 200 or 202 for success.
        if e.code in [200, 202]:
            print(f"[SUCCESS] IndexNow response: {e.code}")
            return True
        print(f"[ERROR] IndexNow submission failed with HTTP {e.code}: {e.read().decode('utf-8', errors='ignore')}")
        return False
    except Exception as e:
        print(f"[ERROR] Connection error during IndexNow push: {e}")
        return False

if __name__ == "__main__":
    urls = gather_urls()
    print(f"Sample URLs being submitted (showing 5 of {len(urls)}):")
    for u in urls[:5]:
        print(f"  - {u}")
    submit_urls(urls)
