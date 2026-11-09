# -*- coding: utf-8 -*-
"""
Send editorial acceptance & publication confirmation emails for Cloudbrowser and ReelAI.
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

CLOUDBROWSER_HTML = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; max-width: 620px; margin: 0 auto; line-height: 1.6; padding: 24px;">
  <div style="border-bottom: 2px solid #06b6d4; padding-bottom: 16px; margin-bottom: 24px;">
    <h1 style="color: #0f172a; font-size: 22px; margin: 0 0 6px 0; letter-spacing: -0.02em;">ToolsRadar Developer Radar</h1>
    <p style="color: #64748b; font-size: 14px; margin: 0;">Editorial Review & Tool Curation Dispatch</p>
  </div>

  <p>Hi Zuch,</p>

  <p>Thank you for submitting <strong>Cloudbrowser</strong> to ToolsRadar! We are delighted to inform you that our editorial team has accepted your submission and published a dedicated profile alongside a comprehensive 4-chapter technical engineering dossier.</p>

  <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 6px; padding: 16px 20px; margin: 20px 0;">
    <div style="font-size: 13px; font-weight: 700; color: #0891b2; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">Live Dossier URL</div>
    <a href="https://lordorange.top/tool/cloudbrowser/" style="color: #0284c7; font-size: 16px; font-weight: 600; text-decoration: underline; word-break: break-all;">https://lordorange.top/tool/cloudbrowser/</a>
    <p style="margin: 8px 0 0 0; color: #475569; font-size: 14px;">
      Signal Score: <strong>88/100</strong> &bull; Category: <strong>AI Agents & Autonomous</strong> &bull; Pricing: <strong>Freemium</strong>
    </p>
  </div>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">Editorial Take on Cloudbrowser</h3>
  <p>Providing managed, persistent Chrome cloud sessions with zero-friction Chrome DevTools Protocol (CDP) connectivity solves a major operational headache for autonomous agent builders (Playwright, Puppeteer, Stagehand). Combining session state persistence with real-time Live View and pause/resume lifecycle controls provides the visual observability and operational reliability teams need in production.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">Showcase Your Live Radar Badge</h3>
  <p>You can embed your official ToolsRadar live badge directly into your homepage or docs. It automatically mirrors your verified curation status:</p>

  <div style="text-align: center; margin: 16px 0;">
    <img src="https://lordorange.top/badge/cloudbrowser.svg" alt="ToolsRadar Featured Badge" style="max-height: 28px;" />
  </div>

  <div style="background: #0f172a; color: #e2e8f0; padding: 12px 16px; border-radius: 6px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; overflow-x: auto; margin-bottom: 12px;">
    <code>[![ToolsRadar](https://lordorange.top/badge/cloudbrowser.svg)](https://lordorange.top/tool/cloudbrowser/)</code>
  </div>

  <p style="font-size: 13px; color: #64748b;">Or HTML:</p>
  <div style="background: #0f172a; color: #e2e8f0; padding: 12px 16px; border-radius: 6px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; overflow-x: auto;">
    <code>&lt;a href="https://lordorange.top/tool/cloudbrowser/"&gt;&lt;img src="https://lordorange.top/badge/cloudbrowser.svg" alt="ToolsRadar Featured Badge" /&gt;&lt;/a&gt;</code>
  </div>

  <p style="margin-top: 24px;">Feel free to keep us updated whenever you ship major updates or agent integrations!</p>

  <p style="margin-top: 24px;">
    Best regards,<br />
    <strong>ToolsRadar Editorial Team</strong><br />
    <span style="color: #64748b; font-size: 13px;">Radar: <a href="https://lordorange.top/" style="color: #0284c7;">https://lordorange.top/</a></span>
  </p>
</div>
"""

CLOUDBROWSER_TEXT = """Hi Zuch,

Thank you for submitting Cloudbrowser to ToolsRadar!

We are pleased to inform you that our editorial team has accepted your submission and published a dedicated profile alongside a 4-chapter technical engineering dossier:

Live URL: https://lordorange.top/tool/cloudbrowser/

Editorial Take:
Providing managed, persistent Chrome cloud sessions with zero-friction Chrome DevTools Protocol (CDP) connectivity solves a major operational headache for autonomous agent builders. Combining persistent profile memory with real-time Live View and pause/resume lifecycle controls provides the visual observability and operational reliability teams need in production.

Showcase Your Official Radar Badge:
You can embed your official ToolsRadar badge in your website or docs:
[![ToolsRadar](https://lordorange.top/badge/cloudbrowser.svg)](https://lordorange.top/tool/cloudbrowser/)

HTML:
<a href="https://lordorange.top/tool/cloudbrowser/"><img src="https://lordorange.top/badge/cloudbrowser.svg" alt="ToolsRadar Featured Badge" /></a>

Best regards,
ToolsRadar Editorial Team
https://lordorange.top/
"""

REELAI_HTML = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; max-width: 620px; margin: 0 auto; line-height: 1.6; padding: 24px;">
  <div style="border-bottom: 2px solid #06b6d4; padding-bottom: 16px; margin-bottom: 24px;">
    <h1 style="color: #0f172a; font-size: 22px; margin: 0 0 6px 0; letter-spacing: -0.02em;">ToolsRadar Developer Radar</h1>
    <p style="color: #64748b; font-size: 14px; margin: 0;">Editorial Review & Tool Curation Dispatch</p>
  </div>

  <p>Hi ReelAI Team,</p>

  <p>Thank you for submitting <strong>ReelAI</strong> to ToolsRadar! We are happy to let you know that our editorial team has accepted your submission and published a dedicated profile alongside an in-depth product dossier.</p>

  <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 6px; padding: 16px 20px; margin: 20px 0;">
    <div style="font-size: 13px; font-weight: 700; color: #0891b2; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">Live Dossier URL</div>
    <a href="https://lordorange.top/tool/reelai/" style="color: #0284c7; font-size: 16px; font-weight: 600; text-decoration: underline; word-break: break-all;">https://lordorange.top/tool/reelai/</a>
    <p style="margin: 8px 0 0 0; color: #475569; font-size: 14px;">
      Signal Score: <strong>82/100</strong> &bull; Category: <strong>AI Tools & Generative Media</strong> &bull; Pricing: <strong>Paid</strong>
    </p>
  </div>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">Editorial Take on ReelAI</h3>
  <p>Rather than requiring users to master complex camera physics and text prompting in general-purpose video models, ReelAI focuses directly on speed and commercial utility for short-form creators. Pre-engineered viral motion presets (such as Rumpelstiltskin and Window Peeper) paired with watermark-free commercial exports provide a fast track for TikTok and Instagram creators looking to convert still photos into engaging video hooks.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">Showcase Your Live Radar Badge</h3>
  <p>You can embed your official ToolsRadar live badge on your website or landing pages:</p>

  <div style="text-align: center; margin: 16px 0;">
    <img src="https://lordorange.top/badge/reelai.svg" alt="ToolsRadar Featured Badge" style="max-height: 28px;" />
  </div>

  <div style="background: #0f172a; color: #e2e8f0; padding: 12px 16px; border-radius: 6px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; overflow-x: auto; margin-bottom: 12px;">
    <code>[![ToolsRadar](https://lordorange.top/badge/reelai.svg)](https://lordorange.top/tool/reelai/)</code>
  </div>

  <p style="font-size: 13px; color: #64748b;">Or HTML:</p>
  <div style="background: #0f172a; color: #e2e8f0; padding: 12px 16px; border-radius: 6px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; overflow-x: auto;">
    <code>&lt;a href="https://lordorange.top/tool/reelai/"&gt;&lt;img src="https://lordorange.top/badge/reelai.svg" alt="ToolsRadar Featured Badge" /&gt;&lt;/a&gt;</code>
  </div>

  <p style="margin-top: 24px;">Best regards,<br />
    <strong>ToolsRadar Editorial Team</strong><br />
    <span style="color: #64748b; font-size: 13px;">Radar: <a href="https://lordorange.top/" style="color: #0284c7;">https://lordorange.top/</a></span>
  </p>
</div>
"""

REELAI_TEXT = """Hi ReelAI Team,

Thank you for submitting ReelAI to ToolsRadar!

We are pleased to inform you that our editorial team has accepted your submission and published a dedicated profile alongside a product dossier:

Live URL: https://lordorange.top/tool/reelai/

Editorial Take:
Rather than requiring creators to navigate complex prompt engineering, ReelAI streamlines photo-to-video diffusion into turnkey viral motion presets tailored specifically for TikTok and Instagram Reels creators.

Showcase Your Official Radar Badge:
You can embed your official ToolsRadar badge in your website:
[![ToolsRadar](https://lordorange.top/badge/reelai.svg)](https://lordorange.top/tool/reelai/)

HTML:
<a href="https://lordorange.top/tool/reelai/"><img src="https://lordorange.top/badge/reelai.svg" alt="ToolsRadar Featured Badge" /></a>

Best regards,
ToolsRadar Editorial Team
https://lordorange.top/
"""

def send_one(to_email, subject, html, text):
    if not API_KEY:
        print("Error: RESEND_API_KEY not found.")
        return False
    payload = {
        "from": FROM_EMAIL,
        "to": [to_email],
        "subject": subject,
        "html": html,
        "text": text
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
            print(f"Sent to {to_email} - Status {resp.status} - Response: {resp_body}")
            return True
    except urllib.error.HTTPError as e:
        print(f"Error sending to {to_email}: {e.code} - {e.read().decode('utf-8')}")
        return False
    except Exception as e:
        print(f"Exception sending to {to_email}: {e}")
        return False

def main():
    print("1. Sending reply to Cloudbrowser (Zuch Huang <zhihao.huang.1997@gmail.com>)...")
    send_one("zhihao.huang.1997@gmail.com", "Re: Tool submission: Cloudbrowser is now featured on ToolsRadar!", CLOUDBROWSER_HTML, CLOUDBROWSER_TEXT)

    print("2. Sending reply to ReelAI (ReelAI Team <reelai@agentmail.to>)...")
    send_one("reelai@agentmail.to", "Re: Tool submission: ReelAI is now featured on ToolsRadar!", REELAI_HTML, REELAI_TEXT)

if __name__ == "__main__":
    main()
