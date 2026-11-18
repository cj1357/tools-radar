# -*- coding: utf-8 -*-
"""
Send reply email via Resend API to:
Codex Quota Overlay maintainer <chen1511@foxmail.com>
Subject: Re: Factual correction for Codex Quota Overlay listing
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

EMAIL_PAYLOAD = {
    "to": "chen1511@foxmail.com",
    "subject": "Re: Factual correction for Codex Quota Overlay listing",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Editorial Listing Update Confirmation</p>
    </div>

    <p>Hello Codex Quota Overlay Maintainer,</p>

    <p>Thank you very much for flagging this! We completely agree and have updated the live profile and technical dossier to reflect that <strong>Codex Quota Overlay is a companion utility</strong> that works alongside Codex Desktop, rather than an alternative or replacement.</p>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">Summary of Factual Adjustments Made</h3>
    <ul style="padding-left: 20px; color: #334155;">
        <li><strong>Title &amp; Meta Description:</strong> Updated page title and metadata to <code>Codex Quota Overlay - Windows Quota Overlay Companion for Codex Desktop</code>, with the tagline refreshed to <em>&ldquo;Windows quota overlay companion for Codex Desktop&rdquo;</em>.</li>
        <li><strong>Removed Alternative Labels:</strong> Completely removed the <code>Alt to Codex Desktop</code> badge and comparison headers. The profile now displays an authentic <code>🧩 Companion for Codex Desktop</code> badge, and the ecosystem role is explicitly marked as <code>Companion for Codex Desktop</code>.</li>
        <li><strong>Companion Integration Callout:</strong> Added a dedicated companion integration section explaining that Codex Quota Overlay hooks directly into the local App Server RPC socket to project ambient telemetry without replacing the primary host application.</li>
        <li><strong>v0.4.0 Distribution Clarification:</strong> Updated the summary, trade-offs, FAQs, and architectural dossier to state that v0.4.0 precompiled assets (Setup EXE and Portable ZIP) are distributed exclusively for Windows 10/11 x64, explicitly clarifying that while macOS source code and CI validation exist in the repository, there is no precompiled macOS installer package attached to v0.4.0.</li>
    </ul>

    <p style="margin: 20px 0;">
        <a href="https://lordorange.top/tool/codex-quota-overlay/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Updated Live Profile &rarr;</a>
    </p>

    <p>Thank you again for helping us keep the listing accurate and faithful to your project&rsquo;s architecture!</p>

    <p style="margin-top: 28px; font-size: 14px; color: #475569;">
        Best regards,<br>
        <strong>ToolsRadar Editorial Team</strong><br>
        <a href="https://lordorange.top" style="color: #0284c7; text-decoration: none;">ToolsRadar</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0284c7; text-decoration: none;">hello@lordorange.top</a>
    </p>
</div>
"""
}

def send_email():
    if not API_KEY:
        print("ERROR: RESEND_API_KEY not found!")
        return
        
    payload_data = json.dumps({
        "from": FROM_EMAIL,
        "to": [EMAIL_PAYLOAD["to"]],
        "subject": EMAIL_PAYLOAD["subject"],
        "html": EMAIL_PAYLOAD["html"]
    }).encode("utf-8")
    
    req = urllib.request.Request(
        API_URL,
        data=payload_data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "ToolsRadar-Notifier/1.0"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"SUCCESS to {EMAIL_PAYLOAD['to']}: ID = {data.get('id')}")
    except urllib.error.HTTPError as e:
        print(f"ERROR to {EMAIL_PAYLOAD['to']}: {e.code} - {e.read().decode('utf-8')}")

if __name__ == "__main__":
    send_email()
