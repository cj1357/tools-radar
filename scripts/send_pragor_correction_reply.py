# -*- coding: utf-8 -*-
import urllib.request
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Load from .env if present
env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
if os.path.exists(env_file):
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("RESEND_API_KEY="):
                os.environ["RESEND_API_KEY"] = line.strip().split("=", 1)[1].strip()

API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = "ToolsRadar Editorial Team <hello@lordorange.top>"

EMAIL_DATA = {
    "to": "outreach@pragor.net",
    "subject": "Re: Factual corrections to the Pragor listing",
    "text": """Hello Pragor Community,

Thank you for your constructive, detailed feedback and for helping us keep ToolsRadar's technical directory strictly accurate.

We have reviewed your official documentation (pragor.net/documentation) and pricing page (pragor.net/pricing), and updated the Pragor listing and 4-chapter engineering dossier across all points:

1. Deployment Flexibility (Self-Hosted / On-Premise):
   - Updated our index metadata to reflect self-hosting support.
   - Clarified in both the profile and dossier that self-hosted / on-premise deployment is offered as a scoped pilot early access program rather than an exclusively managed cloud platform.

2. Pricing Structure & Tier Differentiation:
   - Explicitly separated the Free Public Beta (3 projects, 10 agents, unlimited activity events during beta) from the standard Free tier (1 project, 3 agents, 100 activity events/mo at €0).
   - Noted the staged rollout for upcoming commercial tiers shown on your pricing page.

3. Softened & Factual Architectural Claims:
   - Recalibrated the dossier to strictly mirror your published documentation.
   - Replaced claims regarding cryptographic immutability, universal synchronous auto-pauses, and external code audits with accurate descriptions of attributable activity logs, configurable human-in-the-loop approval checkpoints, and workspace-scoped security perimeters.

The updated dossier is already live on production:
👉 https://lordorange.top/tool/pragor/

We deeply appreciate founders and teams proactively keeping technical directory facts precise while respecting our independent editorial assessment. If anything else evolves as Pragor expands its feature set, please don't hesitate to reach out!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
    "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello Pragor Community,</p>
  <p>Thank you for your constructive, detailed feedback and for helping us keep ToolsRadar's technical directory strictly accurate.</p>
  <p>We have reviewed your official documentation (<a href="https://pragor.net/documentation" style="color: #0284c7; text-decoration: none;">pragor.net/documentation</a>) and pricing page (<a href="https://pragor.net/pricing" style="color: #0284c7; text-decoration: none;">pragor.net/pricing</a>), and updated the Pragor listing and 4-chapter engineering dossier across all points:</p>
  
  <ol style="padding-left: 20px; margin-bottom: 20px;">
    <li style="margin-bottom: 10px;">
      <strong>Deployment Flexibility (Self-Hosted / On-Premise):</strong><br>
      Updated our index metadata to reflect self-hosting support, clarifying that self-hosted / on-premise deployment is offered as a scoped pilot early access program rather than an exclusively managed cloud service.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Pricing Structure & Tier Differentiation:</strong><br>
      Explicitly separated the <em>Free Public Beta</em> (3 projects, 10 agents, unlimited activity events during beta) from the standard <em>Free plan</em> (1 project, 3 agents, 100 activity events/month at €0), and noted staged rollout for commercial tiers.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Softened & Factual Architectural Claims:</strong><br>
      Recalibrated the 4-chapter dossier to strictly mirror your published documentation. Replaced claims regarding cryptographic immutability, universal synchronous auto-pauses, and third-party code audits with accurate descriptions of attributable activity records, configurable human approval checkpoints, and workspace isolation perimeters.
    </li>
  </ol>

  <p>The updated dossier is already live on production:<br>
  👉 <a href="https://lordorange.top/tool/pragor/" style="color: #0284c7; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/pragor/</a></p>

  <p>We deeply appreciate teams proactively keeping technical directory facts precise while respecting our independent editorial assessment. If anything else evolves as Pragor expands its feature set, please don't hesitate to reach out!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
}

def send_email():
    if not API_KEY:
        print("[Dry Run / No API Key] Skipping live sending.")
        return

    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "ToolsRadar-Notifier/1.0"
    }
    payload = {
        "from": FROM_EMAIL,
        "to": [EMAIL_DATA["to"]],
        "subject": EMAIL_DATA["subject"],
        "text": EMAIL_DATA["text"],
        "html": EMAIL_DATA["html"]
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            print(f"[SUCCESS] Email successfully sent to {EMAIL_DATA['to']}: {body}")
            return json.loads(body)
    except Exception as e:
        print(f"[ERROR] Failed to send email to {EMAIL_DATA['to']}: {e}")
        return None

if __name__ == "__main__":
    print("Sending factual correction acknowledgment to Pragor Community...")
    send_email()
