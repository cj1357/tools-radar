# -*- coding: utf-8 -*-
"""
Post a reply to GitHub Issue #4 (Revenue Scout) in cj1357/tools-radar.
"""

import json
import subprocess
import urllib.request
import urllib.error

def get_github_token():
    proc = subprocess.Popen(
        ['git', 'credential', 'fill'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    out, _ = proc.communicate('protocol=https\nhost=github.com\n')
    for line in out.splitlines():
        if line.startswith('password='):
            return line.split('=', 1)[1].strip()
    return None

token = get_github_token()
if not token:
    raise RuntimeError("Could not retrieve GitHub token from git credential manager.")

url = "https://api.github.com/repos/cj1357/tools-radar/issues/4/comments"
body_text = """Hi @akii-technologies,

Thanks for reaching out with the update! We have refreshed Revenue Scout's profile and technical dossier across ToolsRadar:

1. **Tagline & Share Text**: Updated to **"Your Agentic Coworker for sales prospecting"**.
2. **Search Phrase Exploration Workflow**: Updated the summary and architecture breakdown to highlight that Scout uses the requested lead and related results to explore better search phrases (keeping enabled phrases active), alongside human-in-the-loop review for manual social replies and separate approval for Gmail sends.
3. **Features & Collaboration Scope**: Updated the review, FAQs, and pricing notes to clarify that every plan (including Free) includes all features, team collaboration, and all 7 platforms, with paid tiers differing solely by credit capacity.

The updates are live on your profile:
https://lordorange.top/tool/revenue-scout/

Thanks again for keeping the listing accurate!"""

payload = json.dumps({"body": body_text}).encode('utf-8')

req = urllib.request.Request(
    url,
    data=payload,
    headers={
        'User-Agent': 'ToolsRadar-Editorial-Bot',
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("SUCCESS: Comment created!")
        print("Comment ID:", res.get("id"))
        print("Comment URL:", res.get("html_url"))
except urllib.error.HTTPError as e:
    print(f"HTTPError {e.code}: {e.read().decode('utf-8')}")
    raise
