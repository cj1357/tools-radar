# -*- coding: utf-8 -*-
"""
Send link exchange acceptance & confirmation email to Charles <charles@outreach.skillpi.com> for SkillPi.
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

TO_EMAIL = "charles@outreach.skillpi.com"
FROM_EMAIL = "ToolsRadar Editorial Team <hello@lordorange.top>"
SUBJECT = "Re: Link exchange request: SkillPi × ToolsRadar"

HTML_CONTENT = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; max-width: 620px; margin: 0 auto; line-height: 1.6; padding: 24px;">
  <div style="border-bottom: 2px solid #06b6d4; padding-bottom: 16px; margin-bottom: 24px;">
    <h1 style="color: #0f172a; font-size: 22px; margin: 0 0 6px 0; letter-spacing: -0.02em;">ToolsRadar Developer Radar</h1>
    <p style="color: #64748b; font-size: 14px; margin: 0;">Partnership & Ecosystem Link Exchange</p>
  </div>

  <p>Hi Charles,</p>

  <p>Thank you for reaching out! We are delighted to accept your mutual link exchange proposal. <strong>SkillPi</strong> is an exceptional fit for ToolsRadar's developer audience—modular agent skills for Claude Code, Cursor, and Codex are right at the frontier of what our community tracks.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">1. We've Added SkillPi to ToolsRadar Global Footer</h3>
  <p>We have added SkillPi directly under our global <strong>Ecosystem & Partners</strong> section, live across all pages on our site:</p>
  <ul>
    <li><strong>Anchor Text:</strong> <code>SkillPi (Agent Skills) ↗</code></li>
    <li><strong>Target URL:</strong> <a href="https://skillpi.com" style="color: #0284c7;">https://skillpi.com</a></li>
    <li><strong>Placement:</strong> Global Footer (<a href="https://lordorange.top/" style="color: #0284c7;">https://lordorange.top/</a>)</li>
  </ul>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">2. Dedicated Profile & 4-Chapter Architectural Dossier</h3>
  <p>In addition to the footer partner link, our editorial team has curated SkillPi as a featured platform in our radar index, publishing a dedicated 4-chapter technical dossier:</p>
  <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 6px; padding: 14px 18px; margin: 16px 0;">
    <a href="https://lordorange.top/tool/skillpi/" style="color: #0284c7; font-size: 15px; font-weight: 600; text-decoration: underline; word-break: break-all;">https://lordorange.top/tool/skillpi/</a>
    <p style="margin: 6px 0 0 0; color: #475569; font-size: 13px;">
      Signal Score: <strong>89/100</strong> &bull; Category: <strong>AI Agents & Workflows</strong> &bull; Live Radar Badge: <code>https://lordorange.top/badge/skillpi.svg</code>
    </p>
  </div>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">3. ToolsRadar Link Information for SkillPi</h3>
  <p>Here is our preferred link info for your links / partners page:</p>
  <div style="background: #0f172a; color: #e2e8f0; padding: 14px 18px; border-radius: 6px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 13px; line-height: 1.6;">
    <div><strong>Name:</strong> ToolsRadar</div>
    <div><strong>URL:</strong> https://lordorange.top/</div>
    <div><strong>Tagline:</strong> The Intelligence Radar for Breakthrough DevTools & AI Agents</div>
    <div><strong>Description:</strong> Independent real-time tracking of high-signal developer tools, autonomous AI agents, and open-source alternatives.</div>
  </div>

  <p style="margin-top: 24px;">Please drop us a quick note once the link is live on your side. Looking forward to long-term collaboration!</p>

  <p style="margin-top: 24px;">
    Best regards,<br />
    <strong>ToolsRadar Editorial Team</strong><br />
    <span style="color: #64748b; font-size: 13px;">Radar: <a href="https://lordorange.top/" style="color: #0284c7;">https://lordorange.top/</a></span>
  </p>
</div>
"""

TEXT_CONTENT = """Hi Charles,

Thank you for reaching out! We are delighted to accept your mutual link exchange proposal. SkillPi is an exceptional fit for ToolsRadar's developer audience.

1. We've Added SkillPi to ToolsRadar Global Footer:
- Anchor Text: SkillPi (Agent Skills) ↗
- Target URL: https://skillpi.com
- Placement: Global Footer on https://lordorange.top/

2. Dedicated Profile & 4-Chapter Architectural Dossier:
In addition to the footer link, our editorial team has curated SkillPi as a featured platform on our radar:
https://lordorange.top/tool/skillpi/
(Signal Score: 89/100 | Category: AI Agents)

3. ToolsRadar Link Information for SkillPi:
- Name: ToolsRadar
- URL: https://lordorange.top/
- Tagline: The Intelligence Radar for Breakthrough DevTools & AI Agents
- Description: Independent real-time tracking of high-signal developer tools, autonomous AI agents, and open-source alternatives.

Please let us know once the link is live on your side. Looking forward to long-term collaboration!

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
