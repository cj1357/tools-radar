import urllib.request
import json
import os
import sys

# Load from .env if present
env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
if os.path.exists(env_file):
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("RESEND_API_KEY="):
                os.environ["RESEND_API_KEY"] = line.strip().split("=", 1)[1].strip()

API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = "ToolsRadar Team <hello@lordorange.top>"

EMAILS = [
    {
        "to": "admin@uncensoredlabs.dev",
        "subject": "Re: [Tool Submission] UncensoredLabs",
        "text": """Hello UncensoredLabs Team,

Thank you for submitting UncensoredLabs to ToolsRadar!

We've reviewed your submission and appreciate the focused developer utility. Providing drop-in OpenAI-compatible endpoints powered by unaligned, abliterated open-weight models solves a real friction point for researchers and developers building AI applications without corporate safety filter refusals.

Your tool is now live and featured on ToolsRadar:
👉 https://lordorange.top/tool/uncensoredlabs/

We've indexed it under our AI & Machine Learning section, highlighting its OpenAI SDK drop-in compatibility, prepaid pay-as-you-go billing model, and granular model allowlists.

Feel free to link to your dossier page or mention ToolsRadar when sharing updates with your developer community!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello UncensoredLabs Team,</p>
  <p>Thank you for submitting <strong>UncensoredLabs</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and appreciate the focused developer utility. Providing drop-in OpenAI-compatible endpoints powered by unaligned, abliterated open-weight models solves a real friction point for researchers and developers building AI applications without corporate safety filter refusals.</p>
  <p>Your tool is now live and featured on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/uncensoredlabs/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/uncensoredlabs/</a></p>
  <p>We've indexed it under our <strong>AI & Machine Learning</strong> section, highlighting its OpenAI SDK drop-in compatibility, prepaid pay-as-you-go billing model, and granular model allowlists.</p>
  <p>Feel free to link to your dossier page or mention ToolsRadar when sharing updates with your developer community!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "promotions@agentweb.live",
        "subject": "Re: [Tool Submission] AgentWeb: business and web data over REST/MCP",
        "text": """Hello AgentWeb Team (and Assistant),

Thank you for submitting AgentWeb to ToolsRadar!

We've reviewed your submission and appreciate the agent-centric approach. Offering both traditional REST endpoints and a hosted Model Context Protocol (MCP) server across 130M+ structured business entities—backed by a frictionless zero-signup developer sandbox and free tier—is a great asset for the autonomous agent ecosystem.

Your tool is now live and featured on ToolsRadar:
👉 https://lordorange.top/tool/agentweb/

We've indexed it under our AI Agents & Autonomous section, spotlighting its hosted MCP integration, business directory depth, and zero-friction developer onboarding.

Feel free to link to your dossier page or mention ToolsRadar when sharing with the AI agent and MCP developer community!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello AgentWeb Team (and Assistant),</p>
  <p>Thank you for submitting <strong>AgentWeb</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and appreciate the agent-centric approach. Offering both traditional REST endpoints and a hosted Model Context Protocol (MCP) server across 130M+ structured business entities—backed by a frictionless zero-signup developer sandbox and free tier—is a great asset for the autonomous agent ecosystem.</p>
  <p>Your tool is now live and featured on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/agentweb/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/agentweb/</a></p>
  <p>We've indexed it under our <strong>AI Agents & Autonomous</strong> section, spotlighting its hosted MCP integration, business directory depth, and zero-friction developer onboarding.</p>
  <p>Feel free to link to your dossier page or mention ToolsRadar when sharing with the AI agent and MCP developer community!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    }
]

def send_all():
    if not API_KEY:
        print("ERROR: RESEND_API_KEY is not set.")
        return []

    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "ToolsRadar-Notifier/1.0"
    }

    results = []
    for item in EMAILS:
        payload = {
            "from": FROM_EMAIL,
            "to": [item["to"]],
            "subject": item["subject"],
            "text": item["text"],
            "html": item["html"]
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req) as resp:
                body = resp.read().decode("utf-8")
                res_json = json.loads(body)
                print(f"SUCCESS: Reply sent to {item['to']} -> Email ID: {res_json.get('id')}")
                results.append((True, item["to"], res_json.get("id")))
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8")
            print(f"FAILED: Send to {item['to']} HTTP {e.code}: {err_msg}")
            results.append((False, item["to"], err_msg))
        except Exception as e:
            print(f"ERROR: Send to {item['to']}: {str(e)}")
            results.append((False, item["to"], str(e)))

    return results

if __name__ == "__main__":
    send_all()
