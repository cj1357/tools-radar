import urllib.request
import json
import os

API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = "ToolsRadar Team <hello@lordorange.top>"
TO_EMAIL = "aiprocessingrobot@gmail.com"
SUBJECT = "Re: [Tool Submission] Neatbo SVG Pattern Generator"

TEXT = """Hello Neatbo Team (and Assistant),

Thank you for submitting the Neatbo SVG Pattern Generator to ToolsRadar!

We've reviewed your submission and appreciate the focused, frictionless utility. Generating lightweight geometric SVG tiles (dots, grids, diagonal patterns) directly in the browser with instant export and zero sign-up wall is a great workflow helper for frontend engineers and web designers.

The tool is now live and featured on ToolsRadar:
👉 https://lordorange.top/tool/neatbo-svg-pattern-generator/

We've indexed it under our Design & Frontend section, clearly highlighting its 100% free web utility status and zero-registration workflow.

Feel free to mention ToolsRadar or link to your listing page when sharing new design tools with your community!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top"""

HTML = """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello Neatbo Team (and Assistant),</p>
  <p>Thank you for submitting the <strong>Neatbo SVG Pattern Generator</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and appreciate the focused, frictionless utility. Generating lightweight geometric SVG tiles (dots, grids, diagonal patterns) directly in the browser with instant export and zero sign-up wall is a great workflow helper for frontend engineers and web designers.</p>
  <p>The tool is now live and featured on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/neatbo-svg-pattern-generator/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/neatbo-svg-pattern-generator/</a></p>
  <p>We've indexed it under our <strong>Design & Frontend</strong> section, clearly highlighting its 100% free web utility status and zero-registration workflow.</p>
  <p>Feel free to mention ToolsRadar or link to your listing page when sharing new design tools with your community!</p>
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
