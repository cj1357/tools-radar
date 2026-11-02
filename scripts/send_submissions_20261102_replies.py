# -*- coding: utf-8 -*-
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
FROM_EMAIL = "ToolsRadar Editorial Team <hello@lordorange.top>"

EMAILS = [
    {
        "to": "seifip@gmail.com",
        "subject": "Re: Tool submission: Kilobat CLI",
        "text": """Hello Philip,

Thank you for submitting Kilobat CLI to ToolsRadar!

We've reviewed your submission and appreciate the focused utility. Bringing granular Darwin per-application network accounting to the terminal while embedding a native Model Context Protocol (MCP) server is a fantastic architectural decision. It empowers autonomous developer assistants like Claude Code and Cursor to self-diagnose network drops and socket timeouts during active builds.

Your tool is now live with an authoritative 4-chapter technical dossier on ToolsRadar:
👉 https://lordorange.top/tool/kilobat-cli/

We've indexed it under our Developer Tools & Terminal section, spotlighting its per-app traffic attribution, hotspot diagnostics, and seamless MCP integration.

Feel free to link to your dossier page or showcase ToolsRadar in your project README!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello Philip,</p>
  <p>Thank you for submitting <strong>Kilobat CLI</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and appreciate the focused utility. Bringing granular Darwin per-application network accounting to the terminal while embedding a native Model Context Protocol (MCP) server is a fantastic architectural decision. It empowers autonomous developer assistants like Claude Code and Cursor to self-diagnose network drops and socket timeouts during active builds.</p>
  <p>Your tool is now live with an authoritative 4-chapter technical dossier on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/kilobat-cli/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/kilobat-cli/</a></p>
  <p>We've indexed it under our <strong>Developer Tools & Terminal</strong> section, spotlighting its per-app traffic attribution, hotspot diagnostics, and seamless MCP integration.</p>
  <p>Feel free to link to your dossier page or showcase ToolsRadar in your project README!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "info@szcomo.com",
        "subject": "Re: [Tool Submission] SensorCatalog — free calculation utilities",
        "text": """Hello Walter,

Thank you for submitting SensorCatalog to ToolsRadar!

We've reviewed your submission and appreciate the pragmatic engineering utility. Providing free, formula-transparent browser calculators for industrial 4–20 mA current loop scaling, PT100/PT1000 Callendar-Van Dusen conversions, and lead-wire voltage drop calculations solves a real daily headache for instrumentation and embedded hardware technicians.

Your tool is now live with a comprehensive technical dossier on ToolsRadar:
👉 https://lordorange.top/tool/sensorcatalog/

We've indexed it under our Developer Tools & Hardware Engineering utilities, highlighting its zero-signup accessibility and transparent mathematical formulations.

Feel free to link to your dossier page or share it with fellow hardware and instrumentation engineers!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello Walter,</p>
  <p>Thank you for submitting <strong>SensorCatalog</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and appreciate the pragmatic engineering utility. Providing free, formula-transparent browser calculators for industrial 4–20 mA current loop scaling, PT100/PT1000 Callendar-Van Dusen conversions, and lead-wire voltage drop calculations solves a real daily headache for instrumentation and embedded hardware technicians.</p>
  <p>Your tool is now live with a comprehensive technical dossier on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/sensorcatalog/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/sensorcatalog/</a></p>
  <p>We've indexed it under our <strong>Developer Tools & Hardware Engineering</strong> utilities, highlighting its zero-signup accessibility and transparent mathematical formulations.</p>
  <p>Feel free to link to your dossier page or share it with fellow hardware and instrumentation engineers!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "michael@hol.org",
        "subject": "Re: [Tool Submission] HOL Guard (open-source AI-agent security)",
        "text": """Hello Michael,

Thank you for submitting HOL Guard to ToolsRadar!

We've reviewed your submission and appreciate the timely approach to agentic developer security. Providing a local, open-source pre-execution policy engine that catches destructive shell commands and credential exfiltration before code runs is an indispensable safeguard as autonomous agents take over daily programming workflows.

Your tool is now live with an authoritative 4-chapter technical dossier on ToolsRadar:
👉 https://lordorange.top/tool/hol-guard/

We've featured it under our Security & DevOps and AI Agents sections, emphasizing its pre-execution AST command inspection, credential path protection, and zero-latency local execution.

Feel free to link to your dossier or reference ToolsRadar when sharing updates with the open-source security community!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello Michael,</p>
  <p>Thank you for submitting <strong>HOL Guard</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and appreciate the timely approach to agentic developer security. Providing a local, open-source pre-execution policy engine that catches destructive shell commands and credential exfiltration before code runs is an indispensable safeguard as autonomous agents take over daily programming workflows.</p>
  <p>Your tool is now live with an authoritative 4-chapter technical dossier on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/hol-guard/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/hol-guard/</a></p>
  <p>We've featured it under our <strong>Security & DevOps</strong> and <strong>AI Agents</strong> sections, emphasizing its pre-execution AST command inspection, credential path protection, and zero-latency local execution.</p>
  <p>Feel free to link to your dossier or reference ToolsRadar when sharing updates with the open-source security community!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "hello.brightwickstudio@gmail.com",
        "subject": "Re: [Tool Submission] RowPocket JSON Table — offline JSON/NDJSON to CSV",
        "text": """Hello Remy,

Thank you for submitting RowPocket JSON Table to ToolsRadar!

We've reviewed your submission and appreciate the clean, local-first engineering. Resolving nested hierarchies into unambiguous RFC 6901 JSON Pointer column headers while preserving inner arrays as intact values elegantly eliminates the row-explosion trap typical of naive JSON converters.

Your tool is now live with an in-depth 4-chapter technical review on ToolsRadar:
👉 https://lordorange.top/tool/rowpocket-json-table/

We've indexed it under our Developer Tools & Data Transformation section, highlighting its client-side privacy guarantees, standalone CLI bundling, and novel 1 USDC Base micro-payment distribution model.

Feel free to link to your dossier page or mention ToolsRadar in your product documentation!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello Remy,</p>
  <p>Thank you for submitting <strong>RowPocket JSON Table</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and appreciate the clean, local-first engineering. Resolving nested hierarchies into unambiguous RFC 6901 JSON Pointer column headers while preserving inner arrays as intact values elegantly eliminates the row-explosion trap typical of naive JSON converters.</p>
  <p>Your tool is now live with an in-depth 4-chapter technical review on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/rowpocket-json-table/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/rowpocket-json-table/</a></p>
  <p>We've indexed it under our <strong>Developer Tools & Data Transformation</strong> section, highlighting its client-side privacy guarantees, standalone CLI bundling, and novel 1 USDC Base micro-payment distribution model.</p>
  <p>Feel free to link to your dossier page or mention ToolsRadar in your product documentation!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "bellocchio23@gmail.com",
        "subject": "Re: [Tool Submission] LocaleCheck — offline JSON translation handoff checks",
        "text": """Hello Marco,

Thank you for submitting LocaleCheck to ToolsRadar!

We've reviewed your submission and appreciate the focused QA problem it solves. Catching missing translation keys, empty strings, and broken interpolation variable syntax (like {name} mismatches) before client handoffs directly prevents costly runtime UI crashes in localized software.

Your tool is now live with a complete 4-chapter technical dossier on ToolsRadar:
👉 https://lordorange.top/tool/localecheck/

We've indexed it under our Developer Tools & Testing/QA section, spotlighting its offline-first comparison workspace, zero-dependency Python CLI, and fair one-time purchase model.

Feel free to link to your dossier page or feature ToolsRadar on your product page and GitHub resources!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello Marco,</p>
  <p>Thank you for submitting <strong>LocaleCheck</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and appreciate the focused QA problem it solves. Catching missing translation keys, empty strings, and broken interpolation variable syntax (like {name} mismatches) before client handoffs directly prevents costly runtime UI crashes in localized software.</p>
  <p>Your tool is now live with a complete 4-chapter technical dossier on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/localecheck/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/localecheck/</a></p>
  <p>We've indexed it under our <strong>Developer Tools & Testing/QA</strong> section, spotlighting its offline-first comparison workspace, zero-dependency Python CLI, and fair one-time purchase model.</p>
  <p>Feel free to link to your dossier page or feature ToolsRadar on your product page and GitHub resources!</p>
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
                res_body = resp.read().decode("utf-8")
                res_json = json.loads(res_body)
                print(f"[SUCCESS] Sent to {item['to']} -> Email ID: {res_json.get('id')}")
                results.append((item['to'], res_json.get('id')))
        except Exception as e:
            print(f"[ERROR] Failed to send to {item['to']}: {e}")
            if hasattr(e, 'read'):
                print("Response:", e.read().decode('utf-8'))
    return results

if __name__ == "__main__":
    send_all()
