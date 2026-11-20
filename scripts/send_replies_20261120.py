# -*- coding: utf-8 -*-
"""
Send reply emails via Resend API to:
1. Elizabeth Oricha | Bitpont <partnerships@bitpont.com> (Factual corrections confirmed)
2. XM Yang <xm@sweetai.work> (Sweetcraft catalog confirmation, badge code, and backlink exchange)
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

EMAILS = [
    {
        "to": "partnerships@bitpont.com",
        "subject": "Re: Tool submission: Bitpont onchain-finance interface and public API is now featured!",
        "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Editorial Review &amp; Profile Update Confirmation</p>
    </div>

    <p>Hi Elizabeth,</p>

    <p>Thank you for reviewing the live profile and providing these precise factual clarifications.</p>

    <p>We have updated the live Bitpont profile and architectural evaluation (<a href="https://lordorange.top/tool/bitpont/" style="color: #0284c7; text-decoration: none; font-weight: 600;">https://lordorange.top/tool/bitpont/</a>) across all five points:</p>

    <ul style="padding-left: 20px; color: #334155;">
        <li style="margin-bottom: 10px;">
            <strong>1. Risk &amp; Custody Demarcation:</strong> Removed statements asserting that counterparty risk is entirely contained, as well as assumptions regarding immutable smart contracts. Updated Chapter 2 to accurately reflect self-custody wallet signing alongside underlying protocol, bridging, liquidation, and execution dynamics.
        </li>
        <li style="margin-bottom: 10px;">
            <strong>2. Extensibility Specifications:</strong> Removed Webhooks from the architecture specification; the profile now reflects Bitpont's published integration surface: <em>REST APIs, SDK Tooling &amp; Supported Agent Workflows</em>.
        </li>
        <li style="margin-bottom: 10px;">
            <strong>3. Enterprise Access Guidance:</strong> Updated Chapter 3 and FAQ entries with your official partner guidance: <em>&ldquo;Higher API limits and scoped partner access can be requested at support@bitpont.com; availability and terms are agreed for the use case.&rdquo;</em>
        </li>
        <li style="margin-bottom: 10px;">
            <strong>4. Fees &amp; Execution Dynamics:</strong> Removed any implication that fee disclosure eliminates slippage, explicitly noting that network gas, liquidity price impact, slippage, and execution risk still apply.
        </li>
        <li style="margin-bottom: 10px;">
            <strong>5. Independent Editorial Boundary:</strong> Affirmed the clear distinction that our Signal Score represents an independent editorial assessment of software ergonomics and utility, strictly distinguished from third-party code security audits of Bitpont or integrated protocol contracts.
        </li>
    </ul>

    <p style="margin: 20px 0;">
        <a href="https://lordorange.top/tool/bitpont/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Updated Bitpont Profile &rarr;</a>
    </p>

    <p>All updates are live across our global edge network. Thank you for helping us keep the public description rigorous and accurate.</p>

    <p style="margin-top: 28px; font-size: 14px; color: #475569;">
        Best regards,<br>
        <strong>ToolsRadar Editorial Team</strong><br>
        <a href="https://lordorange.top" style="color: #0284c7; text-decoration: none;">ToolsRadar</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0284c7; text-decoration: none;">hello@lordorange.top</a>
    </p>
</div>
"""
    },
    {
        "to": "xm@sweetai.work",
        "subject": "Re: Follow-up: 2nd PDF test for readers — Lordorange",
        "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Tool Cataloging &amp; Collaboration Confirmation</p>
    </div>

    <p>Hi XM,</p>

    <p>Thank you for following up and sharing the second test!</p>

    <p>Your note definitely was not buried—in fact, our editorial team was so impressed by Sweetcraft's client-side, zero-upload architecture and 126-utility suite that we cataloged it earlier this week alongside an in-depth 4-chapter technical dossier:</p>

    <p style="margin: 18px 0;">
        <a href="https://lordorange.top/tool/sweetcraft-pdf/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Live Sweetcraft Profile &amp; Dossier &rarr;</a>
    </p>

    <p>Our review highlights Sweetcraft's client-side WebAssembly execution, zero-registration policy, and the complete elimination of cloud document ingestion risks. Your practical test (splitting a 40-page PDF down to 3 pages locally) illustrates that exact utility for our readers.</p>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">1. Official &ldquo;Featured on ToolsRadar&rdquo; Badge</h3>
    <p>You can embed our official dynamic SVG badge on Sweetcraft, your documentation, or your GitHub repository:</p>

    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; margin: 16px 0;">
        <p style="margin: 0 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Markdown Snippet (for GitHub / Docs):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>[![Featured on ToolsRadar](https://lordorange.top/badge/sweetcraft-pdf.svg)](https://lordorange.top/tool/sweetcraft-pdf/)</code></pre>

        <p style="margin: 14px 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">HTML Snippet (for Website / Marketing Pages):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>&lt;a href="https://lordorange.top/tool/sweetcraft-pdf/" target="_blank" rel="noopener"&gt;&lt;img src="https://lordorange.top/badge/sweetcraft-pdf.svg" alt="Featured on ToolsRadar" /&gt;&lt;/a&gt;</code></pre>
    </div>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">2. Cross-Promotion &amp; Backlinks</h3>
    <p>We would be delighted to have ToolsRadar mentioned to your readers on <strong>SweetTools</strong> and <strong>IELTS Prep</strong> as a curated directory for developer and productivity tools (linking to <a href="https://lordorange.top" style="color: #0284c7; text-decoration: none;">https://lordorange.top</a>). That kind of mutual discovery between indie utilities is exactly what we love supporting.</p>

    <p>Thanks again for building great client-side software and helping share ToolsRadar with your community!</p>

    <p style="margin-top: 28px; font-size: 14px; color: #475569;">
        Best regards,<br>
        <strong>ToolsRadar Editorial Team</strong><br>
        <a href="https://lordorange.top" style="color: #0284c7; text-decoration: none;">ToolsRadar</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0284c7; text-decoration: none;">hello@lordorange.top</a>
    </p>
</div>
"""
    }
]

def send_all():
    if not API_KEY:
        print("ERROR: RESEND_API_KEY not found!")
        return

    for item in EMAILS:
        payload = {
            "from": FROM_EMAIL,
            "to": [item["to"]],
            "subject": item["subject"],
            "html": item["html"]
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(API_URL, data=data, headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "ToolsRadar-Notifier/1.0"
        })

        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                print(f"SUCCESS to {item['to']}: ID = {result.get('id')}")
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            print(f"FAILED to {item['to']}: {e.code} - {err_body}")
        except Exception as e:
            print(f"ERROR to {item['to']}: {str(e)}")

if __name__ == "__main__":
    send_all()
