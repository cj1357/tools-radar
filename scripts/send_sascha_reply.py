import urllib.request
import json
import os

API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = "ToolsRadar Team <hello@lordorange.top>"
TO_EMAIL = "sascha@blueapps.pro"
SUBJECT = "Re: [Tool Submission] Fastrelease — commercial Node.js SaaS starter"

TEXT = """Hi Sascha,

Thank you for the prompt and thorough feedback. We really appreciate you taking the time to review the listing and help us keep ToolsRadar precise and legally accurate.

We have addressed all points and deployed the corrections to production immediately:

1. Pricing & Structured Data: Corrected the Schema.org JSON-LD metadata from $0 to the accurate starting price of $199 USD. The evaluation scorecard now reflects commercial licensing terms instead of a free tier.
2. Licensing Terms vs. Ownership: Updated the codebase description from "codebase ownership transfer" to "Commercial Source Code License" under your official terms (https://fastrelease.net/terms.html). We also updated the pricing notes to accurately distinguish the single-project perpetual license ($199) from the annual unlimited-project tiers ($249/yr, $299/yr).
3. Editorial Assessment Distinction: Renamed the evaluation header from "Hands-on Benchmark" to "Editorial Architecture Analysis" and removed generalized traction claims to ensure readers understand this is an independent editorial analysis of public specifications rather than a verified code audit.

You can inspect the updated live page here:
👉 https://lordorange.top/tool/fastrelease/

Thank you again for holding directories to a high standard of accuracy. Wishing BlueApps and Fastrelease continuous success!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top"""

HTML = """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Sascha,</p>
  <p>Thank you for the prompt and thorough feedback. We really appreciate you taking the time to review the listing and help us keep ToolsRadar precise and legally accurate.</p>
  <p>We have addressed all points and deployed the corrections to production immediately:</p>
  <ol style="padding-left: 20px; margin: 16px 0;">
    <li style="margin-bottom: 8px;"><strong>Pricing & Structured Data:</strong> Corrected the Schema.org JSON-LD metadata from $0 to the accurate starting price of $199 USD. The evaluation scorecard now reflects commercial licensing terms instead of a free tier.</li>
    <li style="margin-bottom: 8px;"><strong>Licensing Terms vs. Ownership:</strong> Updated the codebase description from "codebase ownership transfer" to "Commercial Source Code License" under your official terms (<a href="https://fastrelease.net/terms.html" style="color: #f97316; text-decoration: none;">terms.html</a>). We also updated the pricing notes to accurately distinguish the single-project perpetual license ($199) from the annual unlimited-project tiers ($249/yr, $299/yr).</li>
    <li style="margin-bottom: 8px;"><strong>Editorial Assessment Distinction:</strong> Renamed the evaluation header from "Hands-on Benchmark" to "Editorial Architecture Analysis" and removed generalized traction claims to ensure readers understand this is an independent editorial analysis of public specifications rather than a verified code audit.</li>
  </ol>
  <p>You can inspect the updated live page here:<br>
  👉 <a href="https://lordorange.top/tool/fastrelease/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/fastrelease/</a></p>
  <p>Thank you again for holding directories to a high standard of accuracy. Wishing BlueApps and Fastrelease continuous success!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""

def send():
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "ToolsRadar-Notifier/1.0"
    }
    payload = {
        "from": FROM_EMAIL,
        "to": [TO_EMAIL],
        "subject": SUBJECT,
        "text": TEXT,
        "html": HTML
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            res_json = json.loads(body)
            print(f"SUCCESS: Reply sent to {TO_EMAIL} -> Email ID: {res_json.get('id')}")
            return True, res_json
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"FAILED: Send to {TO_EMAIL} HTTP {e.code}: {err_msg}")
        return False, err_msg
    except Exception as e:
        print(f"ERROR: Send to {TO_EMAIL}: {str(e)}")
        return False, str(e)

if __name__ == "__main__":
    send()
