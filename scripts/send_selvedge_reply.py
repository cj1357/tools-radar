# -*- coding: utf-8 -*-
"""
Send editorial acceptance & publication confirmation email to Mason D for Selvedge.
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

TO_EMAIL = "masondelan@gmail.com"
FROM_EMAIL = "ToolsRadar Editorial Team <hello@lordorange.top>"
SUBJECT = "Re: [Tool Submission] Selvedge is now featured on ToolsRadar!"

HTML_CONTENT = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; max-width: 620px; margin: 0 auto; line-height: 1.6; padding: 24px;">
  <div style="border-bottom: 2px solid #06b6d4; padding-bottom: 16px; margin-bottom: 24px;">
    <h1 style="color: #0f172a; font-size: 22px; margin: 0 0 6px 0; letter-spacing: -0.02em;">ToolsRadar Developer Radar</h1>
    <p style="color: #64748b; font-size: 14px; margin: 0;">Editorial Review & Tool Curation Dispatch</p>
  </div>

  <p>Hi Mason,</p>

  <p>Thank you for submitting <strong>Selvedge</strong> to ToolsRadar! We are thrilled to let you know that our editorial team has accepted your submission and published a dedicated tool profile alongside a 4-chapter technical dossier.</p>

  <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 6px; padding: 16px 20px; margin: 20px 0;">
    <div style="font-size: 13px; font-weight: 700; color: #0891b2; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">Live Dossier URL</div>
    <a href="https://lordorange.top/tool/selvedge/" style="color: #0284c7; font-size: 16px; font-weight: 600; text-decoration: underline; word-break: break-all;">https://lordorange.top/tool/selvedge/</a>
    <p style="margin: 8px 0 0 0; color: #475569; font-size: 14px;">
      Signal Score: <strong>86/100</strong> &bull; Category: <strong>AI Agents</strong> &bull; License: <strong>MIT (Free & Open Source)</strong>
    </p>
  </div>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">Why we love Selvedge</h3>
  <p>Capturing the architectural <em>"why"</em> behind code mutations—especially recording <strong>explicitly rejected alternatives</strong> so agents don't repeat discarded approaches across new conversation sessions—is one of the most acute friction points with Cursor, Claude Code, and autonomous coding agents today. Pairing local-first SQLite storage with native Model Context Protocol (MCP) connectivity makes Selvedge an elegant and practical memory layer.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">Showcase Your Live Radar Badge</h3>
  <p>You can embed your official ToolsRadar live badge into your GitHub README or project homepage. It automatically mirrors your latest curation status:</p>

  <div style="text-align: center; margin: 16px 0;">
    <img src="https://lordorange.top/badge/selvedge.svg" alt="ToolsRadar Featured Badge" style="max-height: 28px;" />
  </div>

  <div style="background: #0f172a; color: #e2e8f0; padding: 12px 16px; border-radius: 6px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; overflow-x: auto; margin-bottom: 12px;">
    <code>[![ToolsRadar](https://lordorange.top/badge/selvedge.svg)](https://lordorange.top/tool/selvedge/)</code>
  </div>

  <p style="font-size: 13px; color: #64748b;">Or HTML:</p>
  <div style="background: #0f172a; color: #e2e8f0; padding: 12px 16px; border-radius: 6px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; overflow-x: auto;">
    <code>&lt;a href="https://lordorange.top/tool/selvedge/"&gt;&lt;img src="https://lordorange.top/badge/selvedge.svg" alt="ToolsRadar Featured Badge" /&gt;&lt;/a&gt;</code>
  </div>

  <p style="margin-top: 24px;">Our automated scraper monitors GitHub releases and star metrics daily, keeping your profile fresh. Feel free to ping us whenever you ship major architectural milestones or new agent integrations!</p>

  <p style="margin-top: 24px;">
    Best regards,<br />
    <strong>ToolsRadar Editorial Team</strong><br />
    <span style="color: #64748b; font-size: 13px;">Radar: <a href="https://lordorange.top/" style="color: #0284c7;">https://lordorange.top/</a></span>
  </p>
</div>
"""

TEXT_CONTENT = """Hi Mason,

Thank you for submitting Selvedge to ToolsRadar!

We are pleased to inform you that our editorial team has accepted your submission and published a dedicated profile alongside a 4-chapter technical dossier:

Live URL: https://lordorange.top/tool/selvedge/

Why we love Selvedge:
Capturing the architectural 'why' behind code mutations—especially recording explicitly rejected approaches so agents don't repeat discarded implementations across sessions—is an essential breakthrough for autonomous coding agents. Pairing local SQLite with native MCP connectivity makes Selvedge an elegant and pragmatic memory layer.

Showcase Your Official Radar Badge:
You can embed your official ToolsRadar badge in your GitHub README:
[![ToolsRadar](https://lordorange.top/badge/selvedge.svg)](https://lordorange.top/tool/selvedge/)

HTML:
<a href="https://lordorange.top/tool/selvedge/"><img src="https://lordorange.top/badge/selvedge.svg" alt="ToolsRadar Featured Badge" /></a>

Our automated scraper tracks GitHub releases and star metrics daily to keep your profile updated. Feel free to reach out anytime you launch major updates!

Best regards,
ToolsRadar Editorial Team
https://lordorange.top/
"""

def send_email():
    if not API_KEY:
        print("Error: RESEND_API_KEY not found in environment or .env file.")
        return False

    payload = {
        "from": FROM_EMAIL,
        "to": [TO_EMAIL],
        "subject": SUBJECT,
        "html": HTML_CONTENT,
        "text": TEXT_CONTENT
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "ToolsRadar-AutoReply/1.0"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            resp_body = resp.read().decode("utf-8")
            print("Status:", resp.status)
            print("Response:", resp_body)
            return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"HTTPError: {e.code} - {error_body}")
        return False
    except Exception as e:
        print("Error:", str(e))
        return False

if __name__ == "__main__":
    send_email()
