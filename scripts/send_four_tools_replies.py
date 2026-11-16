# -*- coding: utf-8 -*-
"""
Send acceptance and featured notification emails via Resend API to all 4 submitters:
1. XM Yang <xm@sweetai.work> (Sweetcraft PDF Tools)
2. Tutuo Marketing <marketing@tutuo.ai> (Octuo)
3. Wayne Hamadi <wayne@datacircle.dev> (Datacircle)
4. 陈威廉 <wlain.cwb@gmail.com> (Kling AI Plugin CLI)
"""

import json
import os
import urllib.request
import urllib.error
import time

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

REPLIES = [
    {
        "name": "Sweetcraft PDF Tools",
        "to": "xm@sweetai.work",
        "subject": "Re: A free PDF tool worth a spot in your ToolsRadar directory is now featured!",
        "tool_url": "https://lordorange.top/tool/sweetcraft-pdf/",
        "badge_url": "https://lordorange.top/badge/sweetcraft-pdf.svg",
        "recipient_name": "XM",
        "category": "Productivity & Document Tools",
        "score": "85/100",
        "tagline": "126 browser-native micro-utilities with 50 client-side PDF tools (zero upload, no limits)",
        "summary": "Our editorial team tested Sweetcraft and verified its client-side WebAssembly execution—delivering 50 dedicated PDF tools without uploading files to remote servers, without paywalls, and without daily rate limits."
    },
    {
        "name": "Octuo",
        "to": "marketing@tutuo.ai",
        "subject": "Re: Submission: Octuo — free listing request is now featured on ToolsRadar!",
        "tool_url": "https://lordorange.top/tool/octuo/",
        "badge_url": "https://lordorange.top/badge/octuo.svg",
        "recipient_name": "Tutuo Marketing Team",
        "category": "AI Agents & Autonomous",
        "score": "88/100",
        "tagline": "Native macOS multi-agent coordinator unifying Claude Code, Codex & MCP with visual canvas",
        "summary": "Our engineering review highlights Octuo's native macOS architecture, its infinite Canvas view and editable memory graph, local encrypted Secrets Vault, and the seamless iOS companion for reviewing agent decisions on the go."
    },
    {
        "name": "Datacircle",
        "to": "wayne@datacircle.dev",
        "subject": "Re: Datacircle for ToolsRadar is now live on our directory!",
        "tool_url": "https://lordorange.top/tool/datacircle/",
        "badge_url": "https://lordorange.top/badge/datacircle.svg",
        "recipient_name": "Wayne",
        "category": "Developer Tools & APIs",
        "score": "82/100",
        "tagline": "Independent benchmarks and evaluation directory for Go-To-Market (GTM) data APIs",
        "summary": "Our review highlights Datacircle's empirical benchmarking methodology, bringing transparent latency, match accuracy, and schema quality metrics to the B2B Go-To-Market data API ecosystem."
    },
    {
        "name": "Kling AI Plugin CLI",
        "to": "wlain.cwb@gmail.com",
        "subject": "Re: [Tool Submission] Kling AI Plugin CLI is now featured on ToolsRadar!",
        "tool_url": "https://lordorange.top/tool/kling-ai-plugin-cli/",
        "badge_url": "https://lordorange.top/badge/kling-ai-plugin-cli.svg",
        "recipient_name": "William (陈威廉)",
        "category": "Developer Tools & AI Video Synthesis",
        "score": "92/100",
        "tagline": "Official terminal CLI & Model Context Protocol (MCP) server for Kling 4.0 video and image generation",
        "summary": "Our technical review highlights Kling AI's official CLI and native MCP Server integration (@klingai/plugin-global and @klingai/plugin-cn), allowing developers and autonomous agents (Claude Code, Cursor) to programmatically orchestrate Kling 4.0 video generation, camera motion control, and reusable Elements character consistency."
    }
]

def build_html(item):
    return f"""
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; max-width: 620px; margin: 0 auto; line-height: 1.6; padding: 24px;">
  <div style="border-bottom: 2px solid #06b6d4; padding-bottom: 16px; margin-bottom: 24px;">
    <h1 style="color: #0f172a; font-size: 22px; margin: 0 0 6px 0; letter-spacing: -0.02em;">ToolsRadar Developer Radar</h1>
    <p style="color: #64748b; font-size: 14px; margin: 0;">Editorial Review & Tool Cataloging Confirmation</p>
  </div>

  <p>Hi {item['recipient_name']},</p>

  <p>Thank you for submitting <strong>{item['name']}</strong> to ToolsRadar! Our editorial engineering team has reviewed your tool, and we are delighted to inform you that it is now officially cataloged and featured on ToolsRadar.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">1. Live Tool Profile & 4-Chapter Technical Dossier</h3>
  <p>Your dedicated profile and in-depth architectural review are now live across our global directory:</p>
  <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 6px; padding: 14px 18px; margin: 16px 0;">
    <a href="{item['tool_url']}" style="color: #0284c7; font-size: 15px; font-weight: 600; text-decoration: underline; word-break: break-all;">{item['tool_url']}</a>
    <p style="margin: 6px 0 0 0; color: #475569; font-size: 13px;">
      Signal Score: <strong>{item['score']}</strong> &bull; Category: <strong>{item['category']}</strong>
    </p>
  </div>

  <p>{item['summary']}</p>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">2. Official ToolsRadar Featured Badge</h3>
  <p>You can embed your dynamic ToolsRadar badge directly in your project README, website footer, or documentation:</p>
  <div style="margin: 16px 0;">
    <img src="{item['badge_url']}" alt="Featured on ToolsRadar" style="height: 32px; display: block; margin-bottom: 12px;" />
    <pre style="background: #0f172a; color: #e2e8f0; padding: 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; white-space: pre-wrap;">&lt;a href="{item['tool_url']}" target="_blank" rel="noopener"&gt;
  &lt;img src="{item['badge_url']}" alt="Featured on ToolsRadar" /&gt;
&lt;/a&gt;</pre>
  </div>

  <p>Markdown format:</p>
  <pre style="background: #0f172a; color: #e2e8f0; padding: 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; white-space: pre-wrap;">[![Featured on ToolsRadar]({item['badge_url']})]({item['tool_url']})</pre>

  <p style="margin-top: 24px;">Thank you for contributing to the developer tooling ecosystem. If you ever release major updates, new CLI flags, or platform features, feel free to reply directly to this email to update your listing!</p>

  <p style="margin-top: 24px;">
    Best regards,<br />
    <strong>ToolsRadar Editorial Team</strong><br />
    <span style="color: #64748b; font-size: 13px;">Radar: <a href="https://lordorange.top/" style="color: #0284c7;">https://lordorange.top/</a></span>
  </p>
</div>
"""

def build_text(item):
    return f"""Hi {item['recipient_name']},

Thank you for submitting {item['name']} to ToolsRadar! Our editorial engineering team has reviewed your tool, and we are delighted to inform you that it is now officially cataloged and featured on ToolsRadar.

1. Live Tool Profile & 4-Chapter Technical Dossier:
{item['tool_url']}
(Signal Score: {item['score']} | Category: {item['category']})

{item['summary']}

2. Official ToolsRadar Featured Badge:
Direct SVG: {item['badge_url']}

HTML:
<a href="{item['tool_url']}" target="_blank" rel="noopener">
  <img src="{item['badge_url']}" alt="Featured on ToolsRadar" />
</a>

Markdown:
[![Featured on ToolsRadar]({item['badge_url']})]({item['tool_url']})

Thank you for building such a high-signal tool for the developer community! Feel free to keep us updated as you introduce new capabilities.

Best regards,
ToolsRadar Editorial Team
https://lordorange.top/
"""

def send_all():
    if not API_KEY:
        print("Error: RESEND_API_KEY not found.")
        return

    for item in REPLIES:
        payload = {
            "from": FROM_EMAIL,
            "to": [item["to"]],
            "subject": item["subject"],
            "html": build_html(item),
            "text": build_text(item)
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
                resp_data = json.loads(resp.read().decode("utf-8"))
                print(f"Sent to {item['to']} ({item['name']}): Status {resp.status}, ID: {resp_data.get('id')}")
        except urllib.error.HTTPError as e:
            print(f"Failed to send to {item['to']}: {e.code} - {e.read().decode('utf-8')}")
        except Exception as e:
            print(f"Error for {item['to']}: {e}")
        time.sleep(1)

if __name__ == "__main__":
    send_all()
