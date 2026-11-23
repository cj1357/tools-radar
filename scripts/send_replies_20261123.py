# -*- coding: utf-8 -*-
"""
Send acceptance emails via Resend API to:
1. ankit solanki <ankit@tinycommand.com> (TinyCommand)
2. ImageSVG Team <support@imagesvg.com> (ImageSVG)
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
        "to": "ankit@tinycommand.com",
        "subject": "Re: [Tool Submission] TinyCommand - free editorial consideration",
        "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Editorial Review &amp; Tool Cataloging Confirmation</p>
    </div>

    <p>Hi Ankit,</p>

    <p>Thank you for submitting <strong>TinyCommand</strong> to ToolsRadar! Our editorial team has evaluated your platform, and we are delighted to inform you that <strong>TinyCommand</strong> is now officially cataloged and featured under <strong>AI Agents &amp; Workflows / Automation</strong>.</p>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">1. Live Tool Profile &amp; 4-Chapter Technical Dossier</h3>
    <p>Your dedicated profile and in-depth architectural evaluation are live across our global directory:</p>
    <p style="margin: 16px 0;">
        <a href="https://lordorange.top/tool/tinycommand/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Live TinyCommand Profile &rarr;</a>
    </p>

    <p>Our review highlights:</p>
    <ul style="padding-left: 20px; color: #334155;">
        <li style="margin-bottom: 8px;"><strong>Unified Operational Plane:</strong> Seamlessly bridges intake forms, relational database tables, visual pipelines, and email dispatches into a cohesive low-code workspace.</li>
        <li style="margin-bottom: 8px;"><strong>Native Embedded AI Steps:</strong> Enables intelligent text generation, data extraction, and lead triage directly inside workflow sequences across all plan tiers.</li>
        <li style="margin-bottom: 8px;"><strong>Autonomous Agent Extensibility:</strong> Support for dedicated goal-driven AI agents on Professional plans, alongside forward-looking MCP (Model Context Protocol) compatibility.</li>
        <li style="margin-bottom: 8px;"><strong>Initial Signal Score:</strong> Rated <strong>86/100</strong> for architecture integration, lean ergonomics, and transparent freemium limits.</li>
    </ul>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">2. Official &ldquo;Featured on ToolsRadar&rdquo; Badge</h3>
    <p>You can embed our official dynamic SVG badge on your website, marketing pages, or documentation:</p>

    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; margin: 16px 0;">
        <p style="margin: 0 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Markdown Snippet (for Docs / GitHub):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>[![Featured on ToolsRadar](https://lordorange.top/badge/tinycommand.svg)](https://lordorange.top/tool/tinycommand/)</code></pre>

        <p style="margin: 14px 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">HTML Snippet (for Website / Marketing Pages):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>&lt;a href="https://lordorange.top/tool/tinycommand/" target="_blank" rel="noopener"&gt;&lt;img src="https://lordorange.top/badge/tinycommand.svg" alt="Featured on ToolsRadar" /&gt;&lt;/a&gt;</code></pre>
    </div>

    <p style="margin-top: 20px; font-size: 13px; color: #64748b;">
        <em>Note: As requested, your contact email remains private for review correspondence, with all public attribution credited directly to TinyCommand.</em>
    </p>

    <p style="margin-top: 28px; font-size: 14px; color: #475569;">
        Best regards,<br>
        <strong>ToolsRadar Editorial Team</strong><br>
        <a href="https://lordorange.top" style="color: #0284c7; text-decoration: none;">ToolsRadar</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0284c7; text-decoration: none;">hello@lordorange.top</a>
    </p>
</div>
"""
    },
    {
        "to": "support@imagesvg.com",
        "subject": "Re: ToolsRadar submission: ImageSVG (Design & Frontend)",
        "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Editorial Review &amp; Tool Cataloging Confirmation</p>
    </div>

    <p>Hello ImageSVG Team,</p>

    <p>Thank you for submitting <strong>ImageSVG</strong> to ToolsRadar! Our editorial team has evaluated your vector tracing suite, and we are pleased to inform you that <strong>ImageSVG</strong> is now officially cataloged and featured under <strong>Design &amp; Frontend</strong>.</p>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">1. Live Tool Profile &amp; 4-Chapter Technical Dossier</h3>
    <p>Your dedicated profile and in-depth architectural evaluation are live across our global directory:</p>
    <p style="margin: 16px 0;">
        <a href="https://lordorange.top/tool/imagesvg/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Live ImageSVG Profile &rarr;</a>
    </p>

    <p>Our review highlights:</p>
    <ul style="padding-left: 20px; color: #334155;">
        <li style="margin-bottom: 8px;"><strong>Precision Bézier Curve Fitting:</strong> Transforms raster artwork (PNG, JPG, WebP, BMP, GIF up to 20 MB) into clean, scalable SVG paths without redundant point bloat.</li>
        <li style="margin-bottom: 8px;"><strong>Modality-Specific Tracing Presets:</strong> Tailored curve algorithms optimized for icons &amp; logos, flat illustrations, photos, and black &amp; white line art.</li>
        <li style="margin-bottom: 8px;"><strong>Real-Time Split-View Inspection:</strong> Interactive high-magnification comparison viewer allowing precise path verification before downloading.</li>
        <li style="margin-bottom: 8px;"><strong>Initial Signal Score:</strong> Rated <strong>85/100</strong> for frontend ergonomics, format support, and clean vector DOM outputs.</li>
    </ul>

    <h3 style="color: #0f172a; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">2. Official &ldquo;Featured on ToolsRadar&rdquo; Badge</h3>
    <p>You can embed our official dynamic SVG badge on your website, converter pages, or documentation:</p>

    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; margin: 16px 0;">
        <p style="margin: 0 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Markdown Snippet (for Docs / GitHub):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>[![Featured on ToolsRadar](https://lordorange.top/badge/imagesvg.svg)](https://lordorange.top/tool/imagesvg/)</code></pre>

        <p style="margin: 14px 0 8px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">HTML Snippet (for Website / Marketing Pages):</p>
        <pre style="margin: 0; background: #0f172a; color: #e2e8f0; padding: 10px; border-radius: 4px; font-size: 12px; overflow-x: auto; font-family: monospace;"><code>&lt;a href="https://lordorange.top/tool/imagesvg/" target="_blank" rel="noopener"&gt;&lt;img src="https://lordorange.top/badge/imagesvg.svg" alt="Featured on ToolsRadar" /&gt;&lt;/a&gt;</code></pre>
    </div>

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
