# -*- coding: utf-8 -*-
import urllib.request
import json
import os

url = "https://api.github.com/repos/cj1357/tools-radar/issues?state=open"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

try:
    with urllib.request.urlopen(req) as resp:
        issues = json.load(resp)
        print(f"Total open issues fetched: {len(issues)}")
        for item in issues:
            print("=" * 60)
            print(f"Issue #{item.get('number')}: {item.get('title')}")
            print(f"Author: {item.get('user', {}).get('login')}")
            print("Body:\n", item.get('body'))
        
        # Save to json file for reference
        out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "open_issues.json"))
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(issues, f, indent=2, ensure_ascii=False)
        print(f"\nSaved issues to {out_path}")
except Exception as e:
    print("Error fetching issues:", e)
