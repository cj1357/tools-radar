# -*- coding: utf-8 -*-
"""
Send tool acceptance & featured notification email to Matt Pavey <paveymk@gmail.com> for MySafeInfo Test Data Generator.
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

TO_EMAIL = "paveymk@gmail.com"
FROM_EMAIL = "ToolsRadar Editorial Team <hello@lordorange.top>"
SUBJECT = "Re: Tool submission: MySafeInfo Test Data Generator is now featured on ToolsRadar!"

TOOL_URL = "https://lordorange.top/tool/mysafeinfo-test-data-generator/"
BADGE_URL = "https://lordorange.top/badge/mysafeinfo-test-data-generator.svg"

HTML_CONTENT = f"""
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; max-width: 620px; margin: 0 auto; line-height: 1.6; padding: 24px;">
  <div style="border-bottom: 2px solid #06b6d4; padding-bottom: 16px; margin-bottom: 24px;">
    <h1 style="color: #0f172a; font-size: 22px; margin: 0 0 6px 0; letter-spacing: -0.02em;">ToolsRadar Developer Radar</h1>
    <p style="color: #64748b; font-size: 14px; margin: 0;">Editorial Review & Tool Cataloging Confirmation</p>
  </div>

  <p>Hi Matthew,</p>

  <p>Thank you for submitting <strong>MySafeInfo Test Data Generator</strong> to ToolsRadar! Our editorial engineering team has reviewed your tool, and we are delighted to inform you that it is now officially cataloged and featured on ToolsRadar.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">1. Live Tool Profile & 4-Chapter Technical Dossier</h3>
  <p>Your dedicated profile and in-depth architectural review are now live across our global index:</p>
  <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 6px; padding: 14px 18px; margin: 16px 0;">
    <a href="{TOOL_URL}" style="color: #0284c7; font-size: 15px; font-weight: 600; text-decoration: underline; word-break: break-all;">{TOOL_URL}</a>
    <p style="margin: 6px 0 0 0; color: #475569; font-size: 13px;">
      Signal Score: <strong>84/100</strong> &bull; Category: <strong>Testing & QA</strong> &bull; Free Tier: <strong>5,000 rows/table (No signup)</strong>
    </p>
  </div>

  <p>Our review highlights MySafeInfo's client-side coordinated generation engine, solving the multi-table relational foreign key consistency problem (Customers &rarr; Orders &rarr; Line Items &rarr; Products) without brittle seed scripts, along with your versatile export options (multi-sheet Excel, zipped CSVs, clean SQL DDL) and the dirty data injection feature for ETL validation.</p>

  <h3 style="color: #0f172a; font-size: 16px; margin: 24px 0 10px 0;">2. Official ToolsRadar Featured Badge</h3>
  <p>You can embed your dynamic ToolsRadar badge directly in your tool documentation, website footer, or marketing pages:</p>
  <div style="margin: 16px 0;">
    <img src="{BADGE_URL}" alt="Featured on ToolsRadar" style="height: 32px; display: block; margin-bottom: 12px;" />
    <pre style="background: #0f172a; color: #e2e8f0; padding: 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; white-space: pre-wrap;">&lt;a href="{TOOL_URL}" target="_blank" rel="noopener"&gt;
  &lt;img src="{BADGE_URL}" alt="Featured on ToolsRadar" /&gt;
&lt;/a&gt;</pre>
  </div>

  <p>Markdown format:</p>
  <pre style="background: #0f172a; color: #e2e8f0; padding: 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; white-space: pre-wrap;">[![Featured on ToolsRadar]({BADGE_URL})]({TOOL_URL})</pre>

  <p style="margin-top: 24px;">Thank you for building such a useful, friction-free utility for the developer and QA community. If you ever update major features or introduce new data models, feel free to reply directly to this email to update your listing!</p>

  <p style="margin-top: 24px;">
    Best regards,<br />
    <strong>ToolsRadar Editorial Team</strong><br />
    <span style="color: #64748b; font-size: 13px;">Radar: <a href="https://lordorange.top/" style="color: #0284c7;">https://lordorange.top/</a></span>
  </p>
</div>
"""

TEXT_CONTENT = f"""Hi Matthew,

Thank you for submitting MySafeInfo Test Data Generator to ToolsRadar! Our editorial engineering team has reviewed your tool, and we are delighted to inform you that it is now officially cataloged and featured on ToolsRadar.

1. Live Tool Profile & 4-Chapter Technical Dossier:
{TOOL_URL}
(Signal Score: 84/100 | Category: Testing & QA | Up to 5,000 rows/table free without signup)

Our review highlights MySafeInfo's client-side coordinated generation engine, solving the multi-table relational consistency problem across Customers, Orders, and Products, along with your versatile export options (multi-sheet Excel, zipped CSV, clean SQL DDL) and the dirty data injection feature for testing data ingestion pipelines.

2. Official ToolsRadar Featured Badge:
Direct SVG: {BADGE_URL}

HTML snippet:
<a href="{TOOL_URL}" target="_blank" rel="noopener">
  <img src="{BADGE_URL}" alt="Featured on ToolsRadar" />
</a>

Markdown snippet:
[![Featured on ToolsRadar]({BADGE_URL})]({TOOL_URL})

Thank you for building such a useful, friction-free utility for the developer and QA community. Feel free to keep us updated as you add new capabilities!

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
