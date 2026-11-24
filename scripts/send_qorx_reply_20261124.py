# -*- coding: utf-8 -*-
"""
Send acceptance and cataloging confirmation email to Marvin Villanueva <msarvillan@gmail.com> (Qorx Void)
"""

import json
import os
import urllib.request
import urllib.error

def load_resend_api_key():
    key = os.environ.get("RESEND_API_KEY")
    if key:
        return key
    env_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("RESEND_API_KEY="):
                    return line.split("=", 1)[1].strip()
    return None

API_KEY = load_resend_api_key()
API_URL = "https://api.resend.com/emails"
FROM_EMAIL = "ToolsRadar Editorial Team <hello@lordorange.top>"

PAYLOAD = {
    "from": FROM_EMAIL,
    "to": ["msarvillan@gmail.com"],
    "subject": "Re: Tool submission — Qorx Void for Claude Code and Codex",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 640px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 8px;">
  <div style="border-bottom: 2px solid #0ea5e9; padding-bottom: 12px; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
    <p style="margin: 4px 0 0; color: #64748b; font-size: 14px;">Editorial Review & Tool Cataloging Confirmation</p>
  </div>

  <p>Hi Marvin,</p>

  <p>Thank you for submitting <strong>Qorx Void</strong> to ToolsRadar! Our editorial team has evaluated your submission and local-first architecture, and we are pleased to inform you that Qorx Void is now officially cataloged and featured under <strong>Developer Tools / AI Code Agents / Local Indexing</strong>.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; margin-bottom: 8px;">1. Live Tool Profile & 4-Chapter Technical Dossier</h3>
  <p>Your dedicated profile and in-depth architectural evaluation are live across our global directory:</p>
  <p style="margin: 16px 0;">
    <a href="https://lordorange.top/tool/qorx/" style="background-color: #0ea5e9; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: 600; display: inline-block;">View Live Qorx Profile &rarr;</a>
  </p>

  <p>Our review highlights:</p>
  <ul style="padding-left: 20px; color: #334155;">
    <li><strong>Token Optimization in Practice:</strong> We spotlighted your Express relative-path lookup benchmark (975 tokens retrieved vs. 6,535 tokens whole-file ingestion), illustrating the real-world 85% token-saving advantage for Claude Code and Codex workflows.</li>
    <li><strong>Native MCP Integration:</strong> Detailed coverage of the Model Context Protocol stdio server tools (<code>qorx.squeeze</code>, <code>qorx.map</code>, <code>qorx.strict_answer</code>).</li>
    <li><strong>Dual-Tier Model:</strong> Transparent breakdown between the free, open-source Rust CLI on GitHub (AGPL-3.0) and the commercial Windows desktop companion (Qorx Void on Microsoft Store with a 24-hour trial).</li>
    <li><strong>Initial Signal Score:</strong> Rated <strong>88/100</strong> for high developer ergonomics, proof-carrying citations, and zero-telemetry local execution.</li>
  </ul>

  <h3 style="color: #0f172a; font-size: 16px; margin-top: 28px; margin-bottom: 8px;">2. Official "Featured on ToolsRadar" Badge</h3>
  <p>You can embed our official dynamic SVG badge on your GitHub README, documentation portal, or project site to showcase your listing:</p>

  <p style="margin-bottom: 6px; font-size: 13px; font-weight: 600; color: #475569;">Markdown Snippet (for GitHub / Docs):</p>
  <pre style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; color: #0f172a;"><code>[![Featured on ToolsRadar](https://lordorange.top/badge/qorx.svg)](https://lordorange.top/tool/qorx/)</code></pre>

  <p style="margin-top: 14px; margin-bottom: 6px; font-size: 13px; font-weight: 600; color: #475569;">HTML Snippet (for Website / Marketing Pages):</p>
  <pre style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; color: #0f172a;"><code>&lt;a href="https://lordorange.top/tool/qorx/" target="_blank" rel="noopener"&gt;&lt;img src="https://lordorange.top/badge/qorx.svg" alt="Featured on ToolsRadar" /&gt;&lt;/a&gt;</code></pre>

  <p style="margin-top: 20px;">If you ever release major protocol updates, publish additional benchmarks, or expand desktop platform support, feel free to reply directly to this thread.</p>

  <div style="border-top: 1px solid #e2e8f0; padding-top: 16px; margin-top: 32px; font-size: 13px; color: #64748b;">
    <p style="margin: 0;">Best regards,</p>
    <p style="margin: 4px 0 0; font-weight: 600; color: #334155;">ToolsRadar Editorial Team</p>
    <p style="margin: 2px 0 0;"><a href="https://lordorange.top" style="color: #0ea5e9; text-decoration: none;">lordorange.top</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0ea5e9; text-decoration: none;">hello@lordorange.top</a></p>
  </div>
</div>
""",
    "text": """ToolsRadar Developer Radar
Editorial Review & Tool Cataloging Confirmation

Hi Marvin,

Thank you for submitting Qorx Void to ToolsRadar! Our editorial team has evaluated your submission and local-first architecture, and we are pleased to inform you that Qorx Void is now officially cataloged and featured under Developer Tools / AI Code Agents / Local Indexing.

1. Live Tool Profile & 4-Chapter Technical Dossier

Your dedicated profile and in-depth architectural evaluation are live across our global directory:
[View Live Qorx Profile →](https://lordorange.top/tool/qorx/)

Our review highlights:
- Token Optimization in Practice: We spotlighted your Express relative-path lookup benchmark (975 tokens retrieved vs. 6,535 tokens whole-file ingestion), illustrating the real-world 85% token-saving advantage for Claude Code and Codex workflows.
- Native MCP Integration: Detailed coverage of the Model Context Protocol stdio server tools (qorx.squeeze, qorx.map, qorx.strict_answer).
- Dual-Tier Model: Transparent breakdown between the free, open-source Rust CLI on GitHub (AGPL-3.0) and the commercial Windows desktop companion (Qorx Void on Microsoft Store with a 24-hour trial).
- Initial Signal Score: Rated 88/100 for high developer ergonomics, proof-carrying citations, and zero-telemetry local execution.

2. Official "Featured on ToolsRadar" Badge

Markdown Snippet (for Docs / GitHub):
[![Featured on ToolsRadar](https://lordorange.top/badge/qorx.svg)](https://lordorange.top/tool/qorx/)

HTML Snippet (for Website / Marketing Pages):
<a href="https://lordorange.top/tool/qorx/" target="_blank" rel="noopener"><img src="https://lordorange.top/badge/qorx.svg" alt="Featured on ToolsRadar" /></a>

If you ever release major protocol updates, publish additional benchmarks, or expand desktop platform support, feel free to reply directly to this thread.

Best regards,
ToolsRadar Editorial Team
[ToolsRadar](https://lordorange.top) • hello@lordorange.top
"""
}

def send_email():
    if not API_KEY:
        print("ERROR: RESEND_API_KEY is not configured.")
        return False
    data = json.dumps(PAYLOAD).encode("utf-8")
    req = urllib.request.Request(API_URL, data=data, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "ToolsRadar-Mail-Dispatcher/1.0"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            res = json.loads(body)
            print(f"SUCCESS to {PAYLOAD['to'][0]}: ID = {res.get('id')}")
            return True
    except urllib.error.HTTPError as e:
        print(f"HTTP ERROR {e.code}: {e.read().decode('utf-8')}")
        return False
    except Exception as e:
        print(f"FAILED: {e}")
        return False

if __name__ == "__main__":
    send_email()
