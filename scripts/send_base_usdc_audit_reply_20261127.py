# -*- coding: utf-8 -*-
"""
Send cataloging confirmation email to Eddie Zhan <nianyi234@gmail.com> (Base USDC Receipt Audit)
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
    "to": ["nianyi234@gmail.com"],
    "subject": "Re: ToolsRadar submission: Base USDC Receipt Audit",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 640px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 8px;">
  <div style="border-bottom: 2px solid #0ea5e9; padding-bottom: 12px; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
    <p style="margin: 4px 0 0; color: #64748b; font-size: 14px;">Editorial Review &amp; Tool Cataloging Confirmation</p>
  </div>

  <p>Hi Eddie,</p>

  <p>Thank you for submitting <strong>Base USDC Receipt Audit</strong> to ToolsRadar! Our editorial team has reviewed your product page and sample CSV/JSON reports, and the tool is now officially cataloged under <strong>DevTools &amp; CLI</strong>.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; margin-bottom: 8px;">1. Live Tool Profile &amp; Technical Dossier</h3>
  <p>Your dedicated profile and 4-chapter technical overview are live across our directory:</p>
  <p style="margin: 16px 0;">
    <a href="https://lordorange.top/tool/base-usdc-receipt-audit/" style="background-color: #0ea5e9; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: 600; display: inline-block;">View Live Base USDC Receipt Audit Profile &rarr;</a>
  </p>

  <p>Our listing accurately covers:</p>
  <ul style="padding-left: 20px; color: #334155;">
    <li><strong>Dual-RPC Verification &amp; Deduplication:</strong> Highlights Python 3.9+ local execution querying two read-only Base mainnet public RPCs without wallet connections or API keys, deduplicating shared hashes, and separating finalized credits from unfinalized or non-matching transfers.</li>
    <li><strong>Pricing &amp; Free Samples:</strong> Lists the one-time 2 USDC download on Base while noting that the example CSV input and JSON audit report are free to inspect on the product page.</li>
    <li><strong>Clear Scope Boundaries:</strong> Explicitly notes the 100-unique-hash-per-run cap and that the tool checks native Base USDC transfers without computing gas fees, wallet balances, or net profit.</li>
    <li><strong>Initial Signal Score:</strong> Rated <strong>82/100</strong> for clean operational focus and transparent scope.</li>
  </ul>

  <h3 style="color: #0f172a; font-size: 16px; margin-top: 28px; margin-bottom: 8px;">2. Optional "Featured on ToolsRadar" Badge</h3>
  <p>If helpful, you can embed our dynamic SVG verification badge in your product README or documentation (entirely optional):</p>

  <p style="margin-bottom: 6px; font-size: 13px; font-weight: 600; color: #475569;">Markdown Snippet:</p>
  <pre style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; color: #0f172a;"><code>[![Featured on ToolsRadar](https://lordorange.top/badge/base-usdc-receipt-audit.svg)](https://lordorange.top/tool/base-usdc-receipt-audit/)</code></pre>

  <p style="margin-top: 14px; margin-bottom: 6px; font-size: 13px; font-weight: 600; color: #475569;">HTML Snippet:</p>
  <pre style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; color: #0f172a;"><code>&lt;a href="https://lordorange.top/tool/base-usdc-receipt-audit/" target="_blank" rel="noopener"&gt;&lt;img src="https://lordorange.top/badge/base-usdc-receipt-audit.svg" alt="Featured on ToolsRadar" /&gt;&lt;/a&gt;</code></pre>

  <p style="margin-top: 20px;">Feel free to reply directly to this thread if any pricing, download link, or scope details change.</p>

  <div style="border-top: 1px solid #e2e8f0; padding-top: 16px; margin-top: 32px; font-size: 13px; color: #64748b;">
    <p style="margin: 0;">Best regards,</p>
    <p style="margin: 4px 0 0; font-weight: 600; color: #334155;">ToolsRadar Editorial Team</p>
    <p style="margin: 2px 0 0;"><a href="https://lordorange.top" style="color: #0ea5e9; text-decoration: none;">lordorange.top</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0ea5e9; text-decoration: none;">hello@lordorange.top</a></p>
  </div>
</div>
""",
    "text": """ToolsRadar Developer Radar
Editorial Review & Tool Cataloging Confirmation

Hi Eddie,

Thank you for submitting Base USDC Receipt Audit to ToolsRadar! Our editorial team has reviewed your product page and sample CSV/JSON reports, and the tool is now officially cataloged under DevTools & CLI.

1. Live Tool Profile & Technical Dossier
https://lordorange.top/tool/base-usdc-receipt-audit/

Our listing accurately covers:
- Dual-RPC Verification & Deduplication: Highlights Python 3.9+ local execution querying two read-only Base mainnet public RPCs without wallet connections or API keys, deduplicating shared hashes, and separating finalized credits from unfinalized or non-matching transfers.
- Pricing & Free Samples: Lists the one-time 2 USDC download on Base while noting that the example CSV input and JSON audit report are free to inspect on the product page.
- Clear Scope Boundaries: Explicitly notes the 100-unique-hash-per-run cap and that the tool checks native Base USDC transfers without computing gas fees, wallet balances, or net profit.
- Initial Signal Score: Rated 82/100 for clean operational focus and transparent scope.

2. Optional "Featured on ToolsRadar" Badge

Markdown Snippet:
[![Featured on ToolsRadar](https://lordorange.top/badge/base-usdc-receipt-audit.svg)](https://lordorange.top/tool/base-usdc-receipt-audit/)

HTML Snippet:
<a href="https://lordorange.top/tool/base-usdc-receipt-audit/" target="_blank" rel="noopener"><img src="https://lordorange.top/badge/base-usdc-receipt-audit.svg" alt="Featured on ToolsRadar" /></a>

Feel free to reply directly to this thread if any pricing, download link, or scope details change.

Best regards,
ToolsRadar Editorial Team
https://lordorange.top • hello@lordorange.top
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
