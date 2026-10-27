import urllib.request
import json
import os
import time

API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = "ToolsRadar Team <hello@lordorange.top>"

EMAILS = [
    {
        "to": "yanbo900720@gmail.com",
        "subject": "Re: [Tool Submission] API Crest — AI API platform for developers",
        "name": "API Crest",
        "text": """Hi Yanbo (and the API Crest team),

Thanks for submitting API Crest to ToolsRadar!

We really appreciate your transparent, documentation-first approach—especially providing verified, offline-checked Python and Node.js examples for complex asynchronous generative tasks and multipart payloads.

API Crest has been reviewed and is now live on ToolsRadar:
👉 https://lordorange.top/tool/api-crest/

We've categorized it under our APIs & Developer Tools section, highlighting your Anthropic-compatible routing, defensive integration guidelines, and public GitHub SDK patterns.

If you find the listing helpful, feel free to mention ToolsRadar on X or link to your listing page—it helps more engineers discover practical developer utilities!

Keep up the great work with API Crest!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Yanbo (and the API Crest team),</p>
  <p>Thanks for submitting <strong>API Crest</strong> to ToolsRadar!</p>
  <p>We really appreciate your transparent, documentation-first approach—especially providing verified, offline-checked Python and Node.js examples for complex asynchronous generative tasks and multipart payloads.</p>
  <p>API Crest has been reviewed and is now live on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/api-crest/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/api-crest/</a></p>
  <p>We've categorized it under our <strong>APIs & Developer Tools</strong> section, highlighting your Anthropic-compatible routing, defensive integration guidelines, and public GitHub SDK patterns.</p>
  <p>If you find the listing helpful, feel free to mention ToolsRadar on X or link to your listing page—it helps more engineers discover practical developer utilities!</p>
  <p>Keep up the great work with API Crest!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "sascha@blueapps.pro",
        "subject": "Re: [Tool Submission] Fastrelease — commercial Node.js SaaS starter",
        "name": "Fastrelease",
        "text": """Hi Sascha,

Thanks for submitting Fastrelease to ToolsRadar!

We've reviewed Fastrelease and appreciate your clean, backend-focused architecture. Having pre-configured Docker containers, PostgreSQL schemas, multi-tenant workspace isolation, and native Stripe billing in a dedicated Node.js stack solves a massive pain point for developers building self-hosted SaaS.

Fastrelease is now officially live on ToolsRadar:
👉 https://lordorange.top/tool/fastrelease/

We've categorized it under our Developer Tools directory and clearly reflected your commercial licensing model ($199 single / $249+ unlimited).

If you find the listing helpful, feel free to mention ToolsRadar on X or link back to your listing page from BlueApps!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Sascha,</p>
  <p>Thanks for submitting <strong>Fastrelease</strong> to ToolsRadar!</p>
  <p>We've reviewed Fastrelease and appreciate your clean, backend-focused architecture. Having pre-configured Docker containers, PostgreSQL schemas, multi-tenant workspace isolation, and native Stripe billing in a dedicated Node.js stack solves a massive pain point for developers building self-hosted SaaS.</p>
  <p>Fastrelease is now officially live on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/fastrelease/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/fastrelease/</a></p>
  <p>We've categorized it under our <strong>Developer Tools</strong> directory and clearly reflected your commercial licensing model ($199 single / $249+ unlimited).</p>
  <p>If you find the listing helpful, feel free to mention ToolsRadar on X or link back to your listing page from BlueApps!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "support@mkclip.com",
        "subject": "Re: [Tool Submission] MKClip – screenshot-based product showcase videos",
        "name": "MKClip",
        "text": """Hi MKClip Team,

Thanks for reaching out and submitting MKClip to ToolsRadar!

We've reviewed your tool and love the focused browser-first workflow. Turning existing UI screenshots into smooth animated showcase clips with client-side MP4/WebM rendering is a fantastic superpower for makers announcing releases on Product Hunt and X.

MKClip is now published on ToolsRadar:
👉 https://lordorange.top/tool/mkclip/

We've categorized it under our Design & Frontend section, highlighting your zero-friction browser editor and deterministic motion templates.

Thank you for sharing your project with our community! Feel free to share your listing or link to ToolsRadar when launching new showcase templates.

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi MKClip Team,</p>
  <p>Thanks for reaching out and submitting <strong>MKClip</strong> to ToolsRadar!</p>
  <p>We've reviewed your tool and love the focused browser-first workflow. Turning existing UI screenshots into smooth animated showcase clips with client-side MP4/WebM rendering is a fantastic superpower for makers announcing releases on Product Hunt and X.</p>
  <p>MKClip is now published on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/mkclip/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/mkclip/</a></p>
  <p>We've categorized it under our <strong>Design & Frontend</strong> section, highlighting your zero-friction browser editor and deterministic motion templates.</p>
  <p>Thank you for sharing your project with our community! Feel free to share your listing or link to ToolsRadar when launching new showcase templates.</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    }
]

def send_all():
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "ToolsRadar-Notifier/1.0"
    }
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
                print(f"SUCCESS: Sent to {item['to']} ({item['name']}) -> Email ID: {res_json.get('id')}")
        except Exception as e:
            print(f"ERROR: {item['name']}: {str(e)}")
        time.sleep(0.5)

if __name__ == "__main__":
    send_all()
