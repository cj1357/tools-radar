# -*- coding: utf-8 -*-
"""
Send correction confirmation email to ImageSVG Team <support@imagesvg.com>
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
    "to": ["support@imagesvg.com"],
    "subject": "Re: Correction request for the ImageSVG directory profile",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 640px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 8px;">
  <div style="border-bottom: 2px solid #0ea5e9; padding-bottom: 12px; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Directory Team</h2>
    <p style="margin: 4px 0 0; color: #64748b; font-size: 14px;">Profile Correction & Standard Listing Confirmation</p>
  </div>

  <p>Hello ImageSVG Team,</p>

  <p>Thank you for reviewing the listing and letting us know. We have updated the ImageSVG directory profile and rebuilt the live page to match your approved description and preferences:</p>

  <ol style="padding-left: 20px; margin-bottom: 20px;">
    <li style="margin-bottom: 10px;">
      <strong>Concise Approved Description:</strong> We replaced the previous descriptive copy with your exact wording:<br/>
      <em>"ImageSVG is an online raster-to-SVG converter for logos, icons, and illustrations. It focuses on high-quality vector results and offers a daily free allowance. Please visit https://imagesvg.com/en/ for current supported formats, features, and pricing."</em>
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Unsupported Technical Claims Removed:</strong> We removed all claims and template sections referencing CLI installation, API/CI/CD integration, local execution/data sovereignty, browser-side conversion, a 20 MB upload limit, specific tracing engines or preset behavior, MCP connectivity, and automated competitor comparisons.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Standard Directory Entry & No Reciprocal Badge Request:</strong> The entry is maintained strictly as a standard listing under Design &amp; Frontend (not featured), and we removed the verification badge embed box from the profile page.
    </li>
  </ol>

  <p>You can inspect the updated live profile here:</p>
  <p style="margin: 18px 0;">
    <a href="https://lordorange.top/tool/imagesvg/" style="background-color: #0ea5e9; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: 600; display: inline-block;">View Updated ImageSVG Profile &rarr;</a>
  </p>

  <p>We appreciate your feedback and apologize for the earlier template-generated details.</p>

  <div style="border-top: 1px solid #e2e8f0; padding-top: 16px; margin-top: 32px; font-size: 13px; color: #64748b;">
    <p style="margin: 0;">Best regards,</p>
    <p style="margin: 4px 0 0; font-weight: 600; color: #334155;">ToolsRadar Editorial Team</p>
    <p style="margin: 2px 0 0;"><a href="https://lordorange.top" style="color: #0ea5e9; text-decoration: none;">lordorange.top</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0ea5e9; text-decoration: none;">hello@lordorange.top</a></p>
  </div>
</div>
""",
    "text": """ToolsRadar Directory Team
Profile Correction & Standard Listing Confirmation

Hello ImageSVG Team,

Thank you for reviewing the listing and letting us know. We have updated the ImageSVG directory profile and rebuilt the live page to match your approved description and preferences:

1. Concise Approved Description: We replaced the previous descriptive copy with your exact wording:
"ImageSVG is an online raster-to-SVG converter for logos, icons, and illustrations. It focuses on high-quality vector results and offers a daily free allowance. Please visit https://imagesvg.com/en/ for current supported formats, features, and pricing."

2. Unsupported Technical Claims Removed: We removed all claims and template sections referencing CLI installation, API/CI/CD integration, local execution/data sovereignty, browser-side conversion, a 20 MB upload limit, specific tracing engines or preset behavior, MCP connectivity, and automated competitor comparisons.

3. Standard Directory Entry & No Reciprocal Badge Request: The entry is maintained strictly as a standard listing under Design & Frontend (not featured), and we removed the verification badge embed box from the profile page.

You can inspect the updated live profile here:
https://lordorange.top/tool/imagesvg/

We appreciate your feedback and apologize for the earlier template-generated details.

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
