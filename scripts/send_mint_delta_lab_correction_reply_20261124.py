# -*- coding: utf-8 -*-
"""
Send factual correction confirmation email to Shunya Masaki <shunyamer@gmail.com> (Mint Delta Lab)
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
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 640px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 8px;">
  <div style="border-bottom: 2px solid #0ea5e9; padding-bottom: 12px; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Editorial Team</h2>
    <p style="margin: 4px 0 0; color: #64748b; font-size: 14px;">Editorial Verification & Factual Alignment Confirmation</p>
  </div>

  <p>Hi Shunya,</p>

  <p>Thank you for the prompt and thorough feedback. Accuracy is the cornerstone of our directory and architectural reviews, and we have updated both the live profile and our 4-chapter long-form dossier to reflect your exact product specifications:</p>

  <ol style="padding-left: 20px; margin-bottom: 20px;">
    <li style="margin-bottom: 10px;">
      <strong>Implementation Stack Clarification:</strong> We removed all references to WebAssembly in Chapter 02 and the metadata. The dossier now explicitly specifies that Mint Delta Lab is implemented entirely in client-side JavaScript running within the visitor's browser memory sandbox.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Token Supply & Concentration Terminology:</strong> We replaced "circulating supply" with <em>"raw token mint supply"</em> as reported in the two user-supplied snapshots. Additionally, we clarified that the top-10 concentration metric reflects percentage point distribution across <em>token accounts</em> rather than beneficial owners or verified "whales."
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Operational Boundaries:</strong> We reinforced the strict scope limits in the summary, FAQs, and Chapter 04: Mint Delta Lab does not retrieve live Solana RPC data, does not continuously track tokens, and does not conduct security or investment audits. All claims are strictly bounded to comparative differential analysis of the two JSON records supplied by the user.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Optional Future API Survey:</strong> We added a clearly labeled note and FAQ entry clarifying that while the project hosts an optional survey for exploring developer interest in a potential future API beta, no paid product exists today and no payments are collected. The existing web comparator remains 100% free with no account required.
    </li>
  </ol>

  <p>The revised profile and dossier have been rebuilt and deployed across our global edge network:</p>
  <p style="margin: 20px 0;">
    <a href="https://lordorange.top/tool/mint-delta-lab/" style="background-color: #0ea5e9; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: 600; display: inline-block;">View Updated Mint Delta Lab Profile &rarr;</a>
  </p>

  <p>Thank you once again for helping us uphold rigorous technical accuracy for the developer community.</p>

  <div style="border-top: 1px solid #e2e8f0; padding-top: 16px; margin-top: 32px; font-size: 13px; color: #64748b;">
    <p style="margin: 0;">Best regards,</p>
    <p style="margin: 4px 0 0; font-weight: 600; color: #334155;">ToolsRadar Editorial & Review Team</p>
    <p style="margin: 2px 0 0;"><a href="https://lordorange.top" style="color: #0ea5e9; text-decoration: none;">lordorange.top</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0ea5e9; text-decoration: none;">hello@lordorange.top</a></p>
  </div>
</div>
""",
    "text": """ToolsRadar Developer Radar
Editorial Verification & Factual Alignment Confirmation

Hi Shunya,

Thank you for the prompt and thorough feedback. Accuracy is the cornerstone of our directory and architectural reviews, and we have updated both the live profile and our 4-chapter long-form dossier to reflect your exact product specifications:

1. Implementation Stack Clarification: We removed all references to WebAssembly in Chapter 02 and the metadata. The dossier now explicitly specifies that Mint Delta Lab is implemented entirely in client-side JavaScript running within the visitor's browser memory sandbox.
2. Token Supply & Concentration Terminology: We replaced "circulating supply" with "raw token mint supply" as reported in the two user-supplied snapshots. Additionally, we clarified that the top-10 concentration metric reflects percentage point distribution across token accounts rather than beneficial owners or verified "whales."
3. Operational Boundaries: We reinforced the strict scope limits in the summary, FAQs, and Chapter 04: Mint Delta Lab does not retrieve live Solana RPC data, does not continuously track tokens, and does not conduct security or investment audits. All claims are strictly bounded to comparative differential analysis of the two JSON records supplied by the user.
4. Optional Future API Survey: We added a clearly labeled note and FAQ entry clarifying that while the project hosts an optional survey for exploring developer interest in a potential future API beta, no paid product exists today and no payments are collected. The existing web comparator remains 100% free with no account required.

The revised profile and dossier have been rebuilt and deployed across our global edge network:
https://lordorange.top/tool/mint-delta-lab/

Thank you once again for helping us uphold rigorous technical accuracy for the developer community.

Best regards,
ToolsRadar Editorial & Review Team
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
