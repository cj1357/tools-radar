# -*- coding: utf-8 -*-
"""
Reply to and close GitHub Issues #3, #4, #5, #6 on cj1357/tools-radar
Token is retrieved dynamically from git credential manager.
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

ISSUES_DATA = [
    {
        "number": 6,
        "tool_id": "youtranscripts",
        "name": "YouTranscripts",
        "author": "profitablecreator",
        "comment": """Hi @profitablecreator,

Thank you for submitting **YouTranscripts** to ToolsRadar! 🎉

We are pleased to let you know that our editorial team has accepted your submission. A dedicated profile and a 4-chapter technical dossier have been published on ToolsRadar:

🔗 **Live Tool Profile:** [https://lordorange.top/tool/youtranscripts/](https://lordorange.top/tool/youtranscripts/)

### Editorial Highlights:
- **Zero-Friction Ingestion:** Reads streaming YouTube video captions rapidly without heavy client-side Whisper model setups or video file downloads.
- **Multi-Format Export Flexibility:** Clean, timestamped outputs across TXT, DOCX, PDF, and subtitle-ready SRT / CSV.
- **Multilingual AI Summarization:** Dual-mode takeaways and 17-language neural translation for researchers and creators.

---

### Official ToolsRadar Live Badge:
You can embed your official ToolsRadar live badge in your website or documentation:

```markdown
[![ToolsRadar Featured Tool](https://lordorange.top/badge/youtranscripts.svg)](https://lordorange.top/tool/youtranscripts/)
```

HTML:
```html
<a href="https://lordorange.top/tool/youtranscripts/"><img src="https://lordorange.top/badge/youtranscripts.svg" alt="ToolsRadar Featured Tool" /></a>
```

Thank you for building and sharing YouTranscripts! Closing this issue as completed.
"""
    },
    {
        "number": 5,
        "tool_id": "orkas",
        "name": "Orkas",
        "author": "BlueSkyID666",
        "comment": """Hi @BlueSkyID666,

Thank you for submitting **Orkas** to ToolsRadar! 🎉

We are thrilled to let you know that our editorial team has accepted your submission. A dedicated profile and a 4-chapter engineering dossier have been published on ToolsRadar:

🔗 **Live Tool Profile:** [https://lordorange.top/tool/orkas/](https://lordorange.top/tool/orkas/)

### Editorial Highlights:
- **Hierarchical Commander Pattern:** Intelligently breaks complex goals into subtasks, delegating across 16 specialist agents (Office, Presentation, Research, Coding, Media) while preserving global context.
- **Native Editable Slides & Reports:** Synthesizes raw project materials into fully editable presentation structures rather than flattened static images.
- **Local-First Data Sovereignty:** Files and embeddings stay local by default; supports Bring-Your-Own-Model (BYOM) via Ollama/vLLM endpoints for true offline privacy.
- **Strong Open-Source Traction:** 9,100+ GitHub stars with an active MIT-licensed desktop ecosystem.

---

### Official ToolsRadar Live Badge:
You can embed your official ToolsRadar live badge in your GitHub README or project homepage:

```markdown
[![ToolsRadar Featured Tool](https://lordorange.top/badge/orkas.svg)](https://lordorange.top/tool/orkas/)
```

HTML:
```html
<a href="https://lordorange.top/tool/orkas/"><img src="https://lordorange.top/badge/orkas.svg" alt="ToolsRadar Featured Tool" /></a>
```

Our automated radar monitors GitHub releases and star metrics daily to keep your profile updated. Thank you for building such an incredible open-source tool! Closing this issue as completed.
"""
    },
    {
        "number": 4,
        "tool_id": "revenue-scout",
        "name": "Revenue Scout",
        "author": "akii-technologies",
        "comment": """Hi @akii-technologies,

Thank you for submitting **Revenue Scout** to ToolsRadar! 🎉

We are glad to inform you that our editorial team has accepted your submission. A dedicated profile and a 4-chapter growth intelligence dossier have been published on ToolsRadar:

🔗 **Live Tool Profile:** [https://lordorange.top/tool/revenue-scout/](https://lordorange.top/tool/revenue-scout/)

### Editorial Highlights:
- **7-Platform Omnichannel Listening:** Indexes public organic discussions across Reddit, LinkedIn, X, Facebook, Instagram, TikTok, and YouTube in one unified stream.
- **Semantic Intent Matching:** Identifies high-probability buyer intent based on product offerings rather than blunt keyword scraping.
- **Human-in-the-Loop AI Replies:** Contextual draft generation that gives founders and sales operators total editorial control before posting.
- **Fair-Use Starter Model:** Generous 2,000 starter credits with no credit card requirement.

---

### Official ToolsRadar Live Badge:
You can embed your official ToolsRadar live badge on your website or landing pages:

```markdown
[![ToolsRadar Featured Tool](https://lordorange.top/badge/revenue-scout.svg)](https://lordorange.top/tool/revenue-scout/)
```

HTML:
```html
<a href="https://lordorange.top/tool/revenue-scout/"><img src="https://lordorange.top/badge/revenue-scout.svg" alt="ToolsRadar Featured Tool" /></a>
```

Thank you for contributing to the ToolsRadar directory! Closing this issue as completed.
"""
    },
    {
        "number": 3,
        "tool_id": "akii-seo-ai-search-optimizer",
        "name": "Akii: SEO & AI Search Optimizer",
        "author": "akii-technologies",
        "comment": """Hi @akii-technologies,

Thank you for submitting **Akii: SEO & AI Search Optimizer** to ToolsRadar! 🎉

We are pleased to inform you that our editorial team has accepted your submission. A dedicated profile and a 4-chapter engineering dossier have been published on ToolsRadar:

🔗 **Live Tool Profile:** [https://lordorange.top/tool/akii-seo-ai-search-optimizer/](https://lordorange.top/tool/akii-seo-ai-search-optimizer/)

### Editorial Highlights:
- **Terminal-First SEO Engine:** Brings full technical site auditing, 404 broken link detection, and competitor inspection directly into the Claude Code CLI.
- **Rich Plugin Architecture:** Packed with 12 modular skills, 5 autonomous agents, and 3 slash commands under a permissive MIT open-source license.
- **GEO & AEO Focus:** Forward-looking evaluation of Generative Engine Optimization (ChatGPT Search, Perplexity, Google AI Overviews) and automated Schema.org JSON-LD graph generation.

---

### Official ToolsRadar Live Badge:
You can embed your official ToolsRadar live badge in your GitHub README or project documentation:

```markdown
[![ToolsRadar Featured Tool](https://lordorange.top/badge/akii-seo-ai-search-optimizer.svg)](https://lordorange.top/tool/akii-seo-ai-search-optimizer/)
```

HTML:
```html
<a href="https://lordorange.top/tool/akii-seo-ai-search-optimizer/"><img src="https://lordorange.top/badge/akii-seo-ai-search-optimizer.svg" alt="ToolsRadar Featured Tool" /></a>
```

Our automated radar monitors GitHub releases and star metrics daily to keep your plugin profile updated. Thank you for contributing this great utility to the Claude Code developer ecosystem! Closing this issue as completed.
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

def close_issue(issue_num):
    url = f"{BASE_URL}/{issue_num}"
    data = json.dumps({"state": "closed", "state_reason": "completed"}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "ToolsRadar-Bot/1.0",
            "Content-Type": "application/json"
        },
        method="PATCH"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.load(resp)
            print(f"Issue #{issue_num} closed successfully (State: {res.get('state')})")
            return True
    except urllib.error.HTTPError as e:
        print(f"Failed to close issue #{issue_num}: {e.code} - {e.read().decode('utf-8')}")
        return False

def main():
    for item in ISSUES_DATA:
        num = item["number"]
        name = item["name"]
        print(f"\nProcessing Issue #{num} ({name})...")
        if post_comment(num, item["comment"]):
            close_issue(num)

if __name__ == "__main__":
    main()
