# -*- coding: utf-8 -*-
"""
Send acceptance email to Shunya Masaki <shunyamer@gmail.com> (Mint Delta Lab)
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
    "to": ["shunyamer@gmail.com"],
    "subject": "Re: Free developer tool submission | Mint Delta Lab (browser-based Solana JSON comparator)",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Editorial Review &amp; Tool Cataloging Confirmation</p>
    </div>

    <p>Hi Shunya,</p>

    <p>Thank you for submitting <strong>Mint Delta Lab</strong> to ToolsRadar! Our editorial team has evaluated your utility, and we are pleased to inform you that <strong>Mint Delta Lab</strong> is now officially cataloged and featured under <strong>Developer Tools / Solana / Web3</strong>.</p>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">1. Live Tool Profile &amp; 4-Chapter Technical Dossier</h3>
    <p>Your dedicated profile and in-depth architectural evaluation are live across our global directory:</p>
    <p style="margin: 16px 0;">
        <a href="https://lordorange.top/tool/mint-delta-lab/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Live Mint Delta Lab Profile &rarr;</a>
    </p>

    <p>Our review highlights:</p>
    <ul style="padding-left: 20px; color: #334155;">
        <li style="margin-bottom: 8px;"><strong>Zero-Telemetry Client-Side Execution:</strong> Evaluates snapshot differential logic strictly inside browser memory without wallet connections or server-side data retention.</li>
        <li style="margin-bottom: 8px;"><strong>Critical Solana Risk Vectors:</strong> Accurate tracking of circulating token supply shifts, mint and freeze authority rotations, and top-10 account concentration metrics.</li>
        <li style="margin-bottom: 8px;"><strong>Structured Machine-Readable Output:</strong> Standardized JSON diff generation enabling immediate programmatic export for offline audit workflows.</li>
        <li style="margin-bottom: 8px;"><strong>Initial Signal Score:</strong> Rated <strong>84/100</strong> for honest developer ergonomics, zero signup barriers, and clear privacy boundaries.</li>
    </ul>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">2. Official &ldquo;Featured on ToolsRadar&rdquo; Badge</h3>
    <p>You can embed our official dynamic SVG badge on your website, documentation portal, or GitHub repository:</p>

    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; margin: 16px 0;">
        <p style="margin: 0 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Markdown Snippet (for Docs / GitHub):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>[![Featured on ToolsRadar](https://lordorange.top/badge/mint-delta-lab.svg)](https://lordorange.top/tool/mint-delta-lab/)</code></pre>

        <p style="margin: 14px 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">HTML Snippet (for Website / Marketing Pages):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>&lt;a href="https://lordorange.top/tool/mint-delta-lab/" target="_blank" rel="noopener"&gt;&lt;img src="https://lordorange.top/badge/mint-delta-lab.svg" alt="Featured on ToolsRadar" /&gt;&lt;/a&gt;</code></pre>
    </div>

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
