import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = "ToolsRadar Team <hello@lordorange.top>"
TO_EMAIL = "sascha@blueapps.pro"
SUBJECT = "Re: [Tool Submission] Fastrelease — commercial Node.js SaaS starter"

TEXT = """Hi Sascha,

Thank you for following up and pointing out those specific discrepancies in our automated FAQ and structured data. You are completely right, and we appreciate your clear feedback.

We have addressed each item and deployed the updates directly to production:

1. Removed Unsupported Privacy/Security Claims:
   Completely eliminated all references to "guaranteed air-gapped security" and "direct binary builds". The infrastructure assessment now accurately notes "Self-Hosted (Buyer Infrastructure)", reflecting that the buyer configures and hosts the purchased code on their selected servers.

2. Removed Competitor Comparisons:
   Removed comparisons against ShipFast across the dossier and excluded Fastrelease from head-to-head comparison modules.

3. Replaced Quickstart with Post-Purchase Workflow:
   Removed the generic browser-opening fallback command. The setup section now explicitly describes the post-purchase repository flow:
   - Acquiring the commercial license on fastrelease.net
   - Accessing and cloning the private repository
   - Configuring environment variables for external integrations (Stripe, PostgreSQL, Mailgun)
   - Running via Docker Compose

4. Updated FAQ & Schema.org FAQPage Structured Data:
   Replaced the automated template with 5 tailored questions and answers that explicitly confirm:
   - Fastrelease is purchased source code under commercial license ($199 single perpetual / $249-$299 annual unlimited).
   - Stripe and Mailgun are external services configured directly by the buyer.
   - Opening the homepage is for license purchase; there is no API-key trial, free tier, or online product demo.
   - Buyers are responsible for configuring and running the code on their own infrastructure.
   - No third-party code audit has been supplied.

You can inspect the updated dossier and Schema.org metadata here:
👉 https://lordorange.top/tool/fastrelease/

Thank you again for helping us maintain absolute factual accuracy on ToolsRadar.

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top"""

HTML = """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Sascha,</p>
  <p>Thank you for following up and pointing out those specific discrepancies in our automated FAQ and structured data. You are completely right, and we appreciate your clear feedback.</p>
  <p>We have addressed each item and deployed the updates directly to production:</p>
  <ol style="padding-left: 20px; margin: 16px 0;">
    <li style="margin-bottom: 10px;">
      <strong>Removed Unsupported Privacy/Security Claims:</strong><br>
      Completely eliminated all references to "guaranteed air-gapped security" and "direct binary builds". The infrastructure assessment now accurately notes <em>"Self-Hosted (Buyer Infrastructure)"</em>, reflecting that the buyer configures and hosts the purchased code on their selected servers.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Removed Competitor Comparisons:</strong><br>
      Removed comparisons against ShipFast across the dossier and excluded Fastrelease from head-to-head comparison modules.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Replaced Quickstart with Post-Purchase Workflow:</strong><br>
      Removed the generic browser-opening fallback command. The setup section now explicitly describes the post-purchase repository flow:
      <ul style="margin: 6px 0; padding-left: 20px; color: #4b5563;">
        <li>Acquiring the commercial license on fastrelease.net to receive repository access</li>
        <li>Cloning the licensed repository</li>
        <li>Configuring environment variables for external integrations (Stripe, PostgreSQL, Mailgun)</li>
        <li>Launching via Docker Compose</li>
      </ul>
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Updated FAQ &amp; Schema.org FAQPage Structured Data:</strong><br>
      Replaced the automated template with 5 tailored questions and answers that explicitly confirm:
      <ul style="margin: 6px 0; padding-left: 20px; color: #4b5563;">
        <li>Fastrelease is purchased source code under commercial license ($199 single perpetual / $249–$299 annual unlimited tiers).</li>
        <li>Stripe and Mailgun are external services configured directly by the buyer.</li>
        <li>Opening the homepage is for license purchase; there is no API-key trial, free tier, or online product demo.</li>
        <li>Buyers are responsible for configuring and running the code on their own infrastructure.</li>
        <li>No third-party code audit has been supplied.</li>
      </ul>
    </li>
  </ol>
  <p>You can inspect the updated dossier and Schema.org metadata here:<br>
  👉 <a href="https://lordorange.top/tool/fastrelease/" style="color: #0284c7; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/fastrelease/</a></p>
  <p>Thank you again for helping us maintain absolute factual accuracy on ToolsRadar.</p>
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
