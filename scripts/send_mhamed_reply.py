import urllib.request
import json
import os

API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = "ToolsRadar Team <hello@lordorange.top>"
TO_EMAIL = "zongsm@gmail.com"
SUBJECT = "Re: Correction request — published Askoure Business Tool Chooser listing"

TEXT = """Hi Mhamed,

Thank you for your sharp eye and constructive feedback!

We've deployed all the requested adjustments to your listing right away:

1. Direct Tool Routing: Both the CTA buttons and the browser mockup address bar now explicitly reflect the exact tool destination: https://askoure-systems.floot.app/tools/choose-business-tool .
2. Git Command Correction: We have removed the automated `git clone` block for the subfolder prototype and updated it to direct web execution, with a clean link to inspect the open prototype files on GitHub without implying a self-hostable setup.
3. Editorial Rating Clarification: We updated the badge to "Editorial Signal" and added a clear disclaimer to the evaluation scorecard stating that all ratings reflect internal ToolsRadar benchmark analysis rather than vendor-provided financial or conversion statistics. We've also updated the page meta to "Free Alternative" instead of "Open-Source Alternative".

You can verify the updated live listing here:
👉 https://lordorange.top/tool/askoure-business-tool-chooser/

Thank you again for helping us keep ToolsRadar accurate and developer-friendly. Wishing you continued growth with Askoure Systems!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top"""

HTML = """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Mhamed,</p>
  <p>Thank you for your sharp eye and constructive feedback!</p>
  <p>We've deployed all the requested adjustments to your listing right away:</p>
  <ol style="padding-left: 20px; margin: 16px 0;">
    <li style="margin-bottom: 8px;"><strong>Direct Tool Routing:</strong> Both the CTA buttons and the browser mockup address bar now explicitly reflect the exact tool destination: <a href="https://askoure-systems.floot.app/tools/choose-business-tool" style="color: #f97316; text-decoration: none;">https://askoure-systems.floot.app/tools/choose-business-tool</a>.</li>
    <li style="margin-bottom: 8px;"><strong>Git Command Correction:</strong> We have removed the automated <code>git clone</code> block for the subfolder prototype and updated it to direct web execution, with a clean link to inspect the open prototype files on GitHub without implying a self-hostable setup.</li>
    <li style="margin-bottom: 8px;"><strong>Editorial Rating Clarification:</strong> We updated the badge to "Editorial Signal" and added a clear disclaimer to the evaluation scorecard stating that all ratings reflect internal ToolsRadar benchmark analysis rather than vendor-provided financial or conversion statistics. We've also updated the page meta to "Free Alternative" instead of "Open-Source Alternative".</li>
  </ol>
  <p>You can verify the updated live listing here:<br>
  👉 <a href="https://lordorange.top/tool/askoure-business-tool-chooser/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/askoure-business-tool-chooser/</a></p>
  <p>Thank you again for helping us keep ToolsRadar accurate and developer-friendly. Wishing you continued growth with Askoure Systems!</p>
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
