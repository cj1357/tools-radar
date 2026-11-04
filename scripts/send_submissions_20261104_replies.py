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

EMAILS = [
    {
        "to": "dunkydd7@gmail.com",
        "subject": "Re: [Tool Submission] PixelArtHive — free browser-based pixel art tools",
        "text": """Hello Jam,

Thank you for submitting PixelArtHive to ToolsRadar!

We've reviewed PixelArtHive and appreciate your focused, pragmatic approach. Providing instant, zero-latency image-to-pixel-art quantization and nearest-neighbor upscaling directly in the browser via HTML5 Canvas—without mandatory account signups, telemetry beacons, or server-side image uploads—is an ideal, privacy-respecting workflow for indie game developers and digital artists preparing retro 2D assets.

Your tool is now live with an authoritative 4-chapter technical dossier on ToolsRadar:
👉 https://lordorange.top/tool/pixelarthive/

We've indexed PixelArtHive under our Design & Frontend category as a 100% Free client-side web utility, accurately noting its nearest-neighbor scaling fidelity and local in-browser processing.

Feel free to link to your dossier page or share it with the pixel art community!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hello Jam,</p>
  <p>Thank you for submitting <strong>PixelArtHive</strong> to ToolsRadar!</p>
  <p>We've reviewed PixelArtHive and appreciate your focused, pragmatic approach. Providing instant, zero-latency image-to-pixel-art quantization and nearest-neighbor upscaling directly in the browser via HTML5 Canvas—without mandatory account signups, telemetry beacons, or server-side image uploads—is an ideal, privacy-respecting workflow for indie game developers and digital artists preparing retro 2D assets.</p>
  <p>Your tool is now live with an authoritative 4-chapter technical dossier on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/pixelarthive/" style="color: #38bdf8; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/pixelarthive/</a></p>
  <p>We've indexed PixelArtHive under our <strong>Design & Frontend</strong> category as a 100% Free client-side web utility, accurately noting its nearest-neighbor scaling fidelity and local in-browser processing.</p>
  <p>Feel free to link to your dossier page or share it with the pixel art community!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    }
]

def send_email(email_data):
    if not API_KEY:
        print(f"[Dry Run / No API Key] Skipping live sending for: {email_data['to']}")
        return {"status": "dry-run", "to": email_data["to"]}

    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "ToolsRadar-Notifier/1.0"
    }
    payload = {
        "from": FROM_EMAIL,
        "to": [email_data["to"]],
        "subject": email_data["subject"],
        "text": email_data["text"],
        "html": email_data["html"]
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            print(f"[SUCCESS] Email successfully sent to {email_data['to']}: {body}")
            return json.loads(body)
    except Exception as e:
        print(f"[ERROR] Failed to send email to {email_data['to']}: {e}")
        return None

if __name__ == "__main__":
    print(f"Processing delivery to Jam (PixelArtHive)...")
    for item in EMAILS:
        print("--------------------------------------------------")
        print(f"To: {item['to']}")
        print(f"Subject: {item['subject']}")
        send_email(item)
    print("--------------------------------------------------")
    print("Done!")
