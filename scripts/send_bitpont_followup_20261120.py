# -*- coding: utf-8 -*-
"""
Send follow-up confirmation email to Elizabeth Oricha | Bitpont <partnerships@bitpont.com>
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
    "to": ["partnerships@bitpont.com"],
    "subject": "Re: Tool submission: Bitpont onchain-finance interface and public API is now featured!",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Custody &amp; Permission Alignment Confirmation</p>
    </div>

    <p>Hi Elizabeth,</p>

    <p>Thank you for pointing that out—the distinction regarding approved permissions and protocol-held positions is very important for technical and regulatory clarity.</p>

    <p>We have updated the summary, Key Advantages, feature highlights, and FAQs on the live profile (<a href="https://lordorange.top/tool/bitpont/" style="color: #0284c7; text-decoration: none; font-weight: 600;">https://lordorange.top/tool/bitpont/</a>) to align completely with your suggested wording:</p>

    <ul style="padding-left: 20px; color: #334155;">
        <li style="margin-bottom: 10px;">
            <strong>Summary:</strong> Adopted your exact wording: <em>&ldquo;Users authorize supported financial actions through wallet signatures or approved permissions. Assets and positions may be held by the underlying protocol contracts, and protocol, bridge, liquidation and execution risks remain.&rdquo;</em> Removed all references to absolute asset sovereignty.
        </li>
        <li style="margin-bottom: 10px;">
            <strong>Key Advantages (Pros):</strong> Replaced claims about funds remaining entirely in user control with: <em>&ldquo;Non-custodial architecture where users authorize actions via wallet signatures or approved permissions without centralized exchange custody.&rdquo;</em>
        </li>
        <li style="margin-bottom: 10px;">
            <strong>Features &amp; FAQs:</strong> Clarified that authorization encompasses both direct wallet signatures and pre-approved contract allowances/permissions, with underlying protocol contracts holding active deposits and positions.
        </li>
    </ul>

    <p style="margin: 20px 0;">
        <a href="https://lordorange.top/tool/bitpont/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Updated Live Profile &rarr;</a>
    </p>

    <p>The revised build has been deployed across our global edge network. We truly appreciate your proactive collaboration in keeping the documentation exact and accurate.</p>

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
