# -*- coding: utf-8 -*-
"""
Send acceptance email via Resend API to:
API.market team <hey@api.market>
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

EMAIL_PAYLOAD = {
    "to": "hey@api.market",
    "subject": "Re: Free ToolsRadar submission — API.market MCP Gateway is now featured!",
    "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Editorial Review &amp; Tool Cataloging Confirmation</p>
    </div>

    <p>Hi API.market Team,</p>

    <p>Thank you for submitting <strong>API.market MCP Gateway</strong> to ToolsRadar! Our technical editorial board has evaluated your platform, and we are delighted to inform you that <strong>API.market MCP Gateway</strong> is now officially cataloged and featured under <strong>AI Agents &amp; Workflows</strong>.</p>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">1. Live Tool Profile &amp; 4-Chapter Technical Dossier</h3>
    <p>Your dedicated profile and in-depth architectural evaluation are live across our global directory:</p>
    <p style="margin: 16px 0;">
        <a href="https://lordorange.top/tool/api-market-mcp-gateway/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Live API.market MCP Gateway Profile &rarr;</a>
    </p>

    <p>Our review highlights:</p>
    <ul style="padding-left: 20px; color: #334155;">
        <li><strong>Single Streamable HTTP Endpoint:</strong> Consolidates 3,410+ API tools across 44 categories via <code>https://api.market/api/mcp/gateway</code>, drastically mitigating MCP server configuration sprawl in developer workstations.</li>
        <li><strong>Turnkey OAuth &amp; API Key Handshakes:</strong> Seamless client authentication across Claude Desktop, ChatGPT, Cursor, and VS Code with automatic OAuth registration.</li>
        <li><strong>Dynamic Schema Exploration:</strong> Employs meta-discovery tools so AI agents query schemas on demand without saturating LLM context windows.</li>
        <li><strong>Initial Signal Score:</strong> Rated <strong>88/100</strong> for architectural utility, developer ergonomics, and multi-vendor billing consolidation.</li>
    </ul>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">2. Official &ldquo;Featured on ToolsRadar&rdquo; Badge</h3>
    <p>You can embed our official dynamic SVG badge on your website, documentation portal, or GitHub repository:</p>
    
    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; margin: 16px 0;">
        <p style="margin: 0 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Markdown Snippet (for GitHub README / Docs):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>[![Featured on ToolsRadar](https://lordorange.top/badge/api-market-mcp-gateway.svg)](https://lordorange.top/tool/api-market-mcp-gateway/)</code></pre>

        <p style="margin: 14px 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">HTML Snippet (for Website / Marketing Pages):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>&lt;a href="https://lordorange.top/tool/api-market-mcp-gateway/" target="_blank" rel="noopener"&gt;&lt;img src="https://lordorange.top/badge/api-market-mcp-gateway.svg" alt="Featured on ToolsRadar" /&gt;&lt;/a&gt;</code></pre>
    </div>

    <p style="margin-top: 28px; font-size: 14px; color: #475569;">
        Best regards,<br>
        <strong>ToolsRadar Editorial Team</strong><br>
        <a href="https://lordorange.top" style="color: #0284c7; text-decoration: none;">ToolsRadar</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0284c7; text-decoration: none;">hello@lordorange.top</a>
    </p>
</div>
"""
}

def send_email():
    if not API_KEY:
        print("ERROR: RESEND_API_KEY not found!")
        return

    payload_data = json.dumps({
        "from": FROM_EMAIL,
        "to": [EMAIL_PAYLOAD["to"]],
        "subject": EMAIL_PAYLOAD["subject"],
        "html": EMAIL_PAYLOAD["html"]
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload_data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "ToolsRadar-Notifier/1.0"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"SUCCESS to {EMAIL_PAYLOAD['to']}: ID = {data.get('id')}")
    except urllib.error.HTTPError as e:
        print(f"ERROR to {EMAIL_PAYLOAD['to']}: {e.code} - {e.read().decode('utf-8')}")

if __name__ == "__main__":
    send_email()
