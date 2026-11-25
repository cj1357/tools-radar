# -*- coding: utf-8 -*-
"""
Send cataloging confirmation email to Stefan Gol <help@waiver.com> (Waiver.com)
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
    "to": ["help@waiver.com"],
    "subject": "Re: [Tool Submission] Waiver.com | Guest waiver drafting and check-in",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 640px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 8px;">
  <div style="border-bottom: 2px solid #0ea5e9; padding-bottom: 12px; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer &amp; Workflow Radar</h2>
    <p style="margin: 4px 0 0; color: #64748b; font-size: 14px;">Editorial Review &amp; Tool Cataloging Confirmation</p>
  </div>

  <p>Hi Stefan,</p>

  <p>Thank you for submitting <strong>Waiver.com</strong> to ToolsRadar! Our editorial team has reviewed your product and walkthrough documentation, and Waiver.com is now officially cataloged under <strong>Productivity &amp; Workflow</strong>.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; margin-bottom: 8px;">1. Live Tool Profile &amp; Operational Dossier</h3>
  <p>Your dedicated profile and 4-chapter product evaluation are live across our directory:</p>
  <p style="margin: 16px 0;">
    <a href="https://lordorange.top/tool/waiver-com/" style="background-color: #0ea5e9; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: 600; display: inline-block;">View Live Waiver.com Profile &rarr;</a>
  </p>

  <p>Key facts accurately covered in our listing:</p>
  <ul style="padding-left: 20px; color: #334155;">
    <li><strong>AI Drafting With Clear Boundaries:</strong> Highlights editable AI-assisted activity and form sections kept distinct from organization-approved release wording and controlled template versions.</li>
    <li><strong>Pre-Arrival &amp; Lobby Check-In:</strong> Covers link, SMS, QR code, and kiosk signing, minor/guardian grouping, photo/ID capture, repeat per-booking signatures, and front-desk participant-name search.</li>
    <li><strong>Transparent Pricing:</strong> Accurately details Starter ($9/month, 1 location, 200 SMS) and Growth ($14/month, unlimited locations, 500 SMS), unlimited waivers across plans, extra SMS rates ($0.02), and the 7-day trial terms.</li>
    <li><strong>Initial Signal Score:</strong> Rated <strong>86/100</strong> for straightforward venue ergonomics and disciplined AI boundaries.</li>
  </ul>

  <h3 style="color: #0f172a; font-size: 16px; margin-top: 28px; margin-bottom: 8px;">2. Optional "Featured on ToolsRadar" Badge</h3>
  <p>If helpful, you are welcome to embed our dynamic SVG status badge in your documentation or website (entirely optional):</p>

  <p style="margin-bottom: 6px; font-size: 13px; font-weight: 600; color: #475569;">Markdown Snippet:</p>
  <pre style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; color: #0f172a;"><code>[![Featured on ToolsRadar](https://lordorange.top/badge/waiver-com.svg)](https://lordorange.top/tool/waiver-com/)</code></pre>

  <p style="margin-top: 14px; margin-bottom: 6px; font-size: 13px; font-weight: 600; color: #475569;">HTML Snippet:</p>
  <pre style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; color: #0f172a;"><code>&lt;a href="https://lordorange.top/tool/waiver-com/" target="_blank" rel="noopener"&gt;&lt;img src="https://lordorange.top/badge/waiver-com.svg" alt="Featured on ToolsRadar" /&gt;&lt;/a&gt;</code></pre>

  <p style="margin-top: 20px;">Please feel free to reply to this thread anytime if pricing, plan limits, or features change and require a factual update.</p>

  <div style="border-top: 1px solid #e2e8f0; padding-top: 16px; margin-top: 32px; font-size: 13px; color: #64748b;">
    <p style="margin: 0;">Best regards,</p>
    <p style="margin: 4px 0 0; font-weight: 600; color: #334155;">ToolsRadar Editorial Team</p>
    <p style="margin: 2px 0 0;"><a href="https://lordorange.top" style="color: #0ea5e9; text-decoration: none;">lordorange.top</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0ea5e9; text-decoration: none;">hello@lordorange.top</a></p>
  </div>
</div>
""",
    "text": """ToolsRadar Developer & Workflow Radar
Editorial Review & Tool Cataloging Confirmation

Hi Stefan,

Thank you for submitting Waiver.com to ToolsRadar! Our editorial team has reviewed your product and walkthrough documentation, and Waiver.com is now officially cataloged under Productivity & Workflow.

1. Live Tool Profile & Operational Dossier
https://lordorange.top/tool/waiver-com/

Key facts accurately covered in our listing:
- AI Drafting With Clear Boundaries: Highlights editable AI-assisted activity and form sections kept distinct from organization-approved release wording and controlled template versions.
- Pre-Arrival & Lobby Check-In: Covers link, SMS, QR code, and kiosk signing, minor/guardian grouping, photo/ID capture, repeat per-booking signatures, and front-desk participant-name search.
- Transparent Pricing: Accurately details Starter ($9/month, 1 location, 200 SMS) and Growth ($14/month, unlimited locations, 500 SMS), unlimited waivers across plans, extra SMS rates ($0.02), and the 7-day trial terms.
- Initial Signal Score: Rated 86/100 for straightforward venue ergonomics and disciplined AI boundaries.

2. Optional "Featured on ToolsRadar" Badge

Markdown Snippet:
[![Featured on ToolsRadar](https://lordorange.top/badge/waiver-com.svg)](https://lordorange.top/tool/waiver-com/)

HTML Snippet:
<a href="https://lordorange.top/tool/waiver-com/" target="_blank" rel="noopener"><img src="https://lordorange.top/badge/waiver-com.svg" alt="Featured on ToolsRadar" /></a>

Please feel free to reply to this thread anytime if pricing, plan limits, or features change and require a factual update.

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
