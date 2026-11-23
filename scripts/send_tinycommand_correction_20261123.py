# -*- coding: utf-8 -*-
"""
Send correction confirmation email to Ankit Solanki <ankit@tinycommand.com>
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
    "to": ["ankit@tinycommand.com"],
    "subject": "Re: [Tool Submission] TinyCommand - free editorial consideration",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Factual Corrections &amp; Profile Update Confirmation</p>
    </div>

    <p>Hi Ankit,</p>

    <p>Thank you for pointing these out—factual accuracy is our highest priority, and we appreciate your prompt feedback.</p>

    <p>We have updated the live TinyCommand profile (<a href="https://lordorange.top/tool/tinycommand/" style="color: #0284c7; text-decoration: none; font-weight: 600;">https://lordorange.top/tool/tinycommand/</a>) across both points:</p>

    <ul style="padding-left: 20px; color: #334155;">
        <li style="margin-bottom: 10px;">
            <strong>1. Scorecard Onboarding Note:</strong> Removed the generic CLI installation note. The evaluation scorecard now accurately reflects TinyCommand's hosted, no-code architecture as <em>&ldquo;Cloud-hosted web onboarding via official documentation,&rdquo;</em> and direct web navigation is specified with no installation requirements.
        </li>
        <li style="margin-bottom: 10px;">
            <strong>2. MCP Compatibility Status:</strong> Corrected all mentions across the profile, extensibility tags, and technical dossier (Chapter 3) to explicitly describe Model Context Protocol (MCP) support as an <em>&ldquo;announced upcoming capability&rdquo;</em> rather than an active present feature.
        </li>
    </ul>

    <p style="margin: 20px 0;">
        <a href="https://lordorange.top/tool/tinycommand/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Updated TinyCommand Profile &rarr;</a>
    </p>

    <p>The revised build has been compiled and deployed across our global edge network. Thank you again for helping us maintain exact, factual coverage of your product.</p>

    <p style="margin-top: 28px; font-size: 14px; color: #475569;">
        Best regards,<br>
        <strong>ToolsRadar Editorial Team</strong><br>
        <a href="https://lordorange.top" style="color: #0284c7; text-decoration: none;">ToolsRadar</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0284c7; text-decoration: none;">hello@lordorange.top</a>
    </p>
</div>
"""
}

def send_reply():
    if not API_KEY:
        print("ERROR: RESEND_API_KEY not found!")
        return

    data = json.dumps(PAYLOAD).encode("utf-8")
    req = urllib.request.Request(API_URL, data=data, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "ToolsRadar-Notifier/1.0"
    })

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            print(f"SUCCESS to {PAYLOAD['to'][0]}: ID = {result.get('id')}")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        print(f"FAILED to {PAYLOAD['to'][0]}: {e.code} - {err_body}")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    send_reply()
