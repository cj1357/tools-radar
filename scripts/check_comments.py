# -*- coding: utf-8 -*-
import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

repo = "cj1357/tools-radar"
for num in [3, 4, 5, 6]:
    url = f"https://api.github.com/repos/{repo}/issues/{num}/comments"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            comments = json.load(resp)
            print(f"=== Issue #{num}: {len(comments)} comments ===")
            for c in comments:
                print(f"Author: {c['user']['login']}")
                print(f"Body:\n{c['body']}\n{'-'*40}")
    except Exception as e:
        print(f"Issue #{num} error:", e)
