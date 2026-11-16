# -*- coding: utf-8 -*-
"""
Send polite follow-up emails via Resend API:
1. Tutuo Marketing <marketing@tutuo.ai> (Confirm factual corrections deployed)
2. 陈威廉 <wlain.cwb@gmail.com> (Thank for official README badge in 1.0.5 release)
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

FOLLOWUPS = [
    {
        "to": "marketing@tutuo.ai",
        "subject": "Re: Octuo on ToolsRadar — two small factual corrections",
        "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Editorial Review & Profile Update Confirmation</p>
    </div>

    <p>Hi Tutuo Marketing Team,</p>

    <p>Thank you so much for the swift follow-up and the precise corrections!</p>

    <p>We have updated the <strong>Octuo</strong> listing and technical dossier across ToolsRadar immediately:</p>
    
    <ul style="padding-left: 20px; color: #334155;">
        <li style="margin-bottom: 8px;">
            <strong>Deployment Format:</strong> Changed to <strong>&ldquo;Native macOS desktop app&rdquo;</strong> with local execution. We have also updated the self-hosting FAQ to clarify that Octuo runs 100% on the user's own Mac (zero Docker/server hosting needed), paired with the iOS companion for mobile oversight.
        </li>
        <li style="margin-bottom: 8px;">
            <strong>Free Trial & Pricing:</strong> Updated the FAQ and pricing model to explicitly highlight the <strong>1,000 OC trial credits with no credit card required</strong>, with commercial plans starting at $20/month.
        </li>
    </ul>

    <p>The updated listing is already deployed and live:</p>
    <p style="margin: 16px 0;">
        <a href="https://lordorange.top/tool/octuo/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Updated Octuo Listing &rarr;</a>
    </p>

    <p>We really appreciate your attention to detail. Whenever you ship major version updates or new agent orchestration capabilities, feel free to drop us a note — we'll be glad to keep your technical evaluation and benchmarks updated.</p>

    <p style="margin-top: 24px; font-size: 14px; color: #475569;">
        Best regards,<br>
        <strong>ToolsRadar Editorial Team</strong><br>
        <a href="https://lordorange.top" style="color: #0284c7; text-decoration: none;">ToolsRadar</a> &bull; <a href="mailto:hello@lordorange.top" style="color: #0284c7; text-decoration: none;">hello@lordorange.top</a>
    </p>
</div>
"""
    },
    {
        "to": "wlain.cwb@gmail.com",
        "subject": "Re: [Tool Submission] Kling AI Plugin CLI is now featured on ToolsRadar!",
        "html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 620px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
    <div style="border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #0f172a; font-size: 20px;">ToolsRadar Developer Radar</h2>
        <p style="margin: 4px 0 0; color: #64748b; font-size: 13px;">Official Listing & Partnership Confirmation</p>
    </div>

    <p>Hi William,</p>

    <p>That is fantastic news — thank you so much for adding the <strong>Featured on ToolsRadar</strong> badge to the official Kling AI Plugin README and the 1.0.5 release!</p>

    <p>We are thrilled to feature <strong>Kling AI Plugin CLI</strong>. Bringing state-of-the-art Kling 4.0 video synthesis directly into terminal workflows and agentic tool-calling (via MCP) is a major milestone for AI developer velocity.</p>

    <p>Your official dossier and live profile remain permanently featured at:</p>
    <p style="margin: 16px 0;">
        <a href="https://lordorange.top/tool/kling-ai-plugin-cli/" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; font-size: 14px;">View Kling AI Plugin CLI Profile &rarr;</a>
    </p>

    <p>Whenever your team ships new major releases, model checkpoints, or new MCP capabilities, feel free to reach out — we will be delighted to keep your technical evaluation and benchmarks updated.</p>

    <p style="margin-top: 24px; font-size: 14px; color: #475569;">
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

    for item in FOLLOWUPS:
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
