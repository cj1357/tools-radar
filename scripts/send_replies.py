import os
import urllib.request
import json
import time

API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = "ToolsRadar Team <hello@lordorange.top>"

EMAILS = [
    {
        "to": "carlbrownsonxyz@gmail.com",
        "subject": "Re: [Tool Submission] HyperGSC — Free Curation",
        "name": "HyperGSC",
        "text": """Hi Carl,

Thanks for submitting HyperGSC to ToolsRadar!

We've reviewed your submission and love the hosted MCP approach—connecting Google Search Console directly to AI coding assistants like Claude and Cursor solves a real workflow headache for technical founders and SEOs.

Your tool is now officially listed on ToolsRadar:
👉 https://lordorange.top/tool/hypergsc/

We've categorized it under AI Agents & Autonomous and highlighted its read-only architecture and zero-friction MCP compatibility.

If you find the listing helpful, feel free to mention ToolsRadar on X or link to your listing page—it helps more developers and founders discover independent AI tools like yours!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Carl,</p>
  <p>Thanks for submitting <strong>HyperGSC</strong> to ToolsRadar!</p>
  <p>We've reviewed your submission and love the hosted MCP approach—connecting Google Search Console directly to AI coding assistants like Claude and Cursor solves a real workflow headache for technical founders and SEOs.</p>
  <p>Your tool is now officially listed on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/hypergsc/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/hypergsc/</a></p>
  <p>We've categorized it under <strong>AI Agents & Autonomous</strong> and highlighted its read-only architecture and zero-friction MCP compatibility.</p>
  <p>If you find the listing helpful, feel free to mention ToolsRadar on X or link to your listing page—it helps more developers and founders discover independent AI tools like yours!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "carlbrownsonxyz@gmail.com",
        "subject": "Re: Free directory submission: SoundClean",
        "name": "SoundClean",
        "text": """Hi Carl,

Thanks for submitting SoundClean to ToolsRadar!

We've reviewed SoundClean and appreciated the instant 10-second preview feature and the pay-as-you-go pricing model, which makes it super accessible for creators and podcasters.

Your tool is now live on our platform:
👉 https://lordorange.top/tool/soundclean/

It is featured under our AI & Machine Learning audio utilities section. Thank you for sharing your project with our community!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Carl,</p>
  <p>Thanks for submitting <strong>SoundClean</strong> to ToolsRadar!</p>
  <p>We've reviewed SoundClean and appreciated the instant 10-second preview feature and the pay-as-you-go pricing model, which makes it super accessible for creators and podcasters.</p>
  <p>Your tool is now live on our platform:<br>
  👉 <a href="https://lordorange.top/tool/soundclean/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/soundclean/</a></p>
  <p>It is featured under our <strong>AI & Machine Learning</strong> audio utilities section. Thank you for sharing your project with our community!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "zongsm@gmail.com",
        "subject": "Re: [Tool Submission] Askoure Business Tool Chooser — free Arabic-first guided tool",
        "name": "Askoure Business Tool Chooser",
        "text": """Hi Mhamed,

Thank you for reaching out and submitting the Askoure Business Tool Chooser to ToolsRadar!

We appreciate focused, workflow-driven utilities—especially those designed Arabic-first with native RTL support to serve regional entrepreneurs and freelancers effectively. The open prototype reference on GitHub was also great for verifying provenance.

Your tool is now live on ToolsRadar:
👉 https://lordorange.top/tool/askoure-business-tool-chooser/

It has been indexed under our Productivity & Workflow directory. Wishing you continuous success with your tools and advisory work!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Mhamed,</p>
  <p>Thank you for reaching out and submitting the <strong>Askoure Business Tool Chooser</strong> to ToolsRadar!</p>
  <p>We appreciate focused, workflow-driven utilities—especially those designed Arabic-first with native RTL support to serve regional entrepreneurs and freelancers effectively. The open prototype reference on GitHub was also great for verifying provenance.</p>
  <p>Your tool is now live on ToolsRadar:<br>
  👉 <a href="https://lordorange.top/tool/askoure-business-tool-chooser/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/askoure-business-tool-chooser/</a></p>
  <p>It has been indexed under our <strong>Productivity & Workflow</strong> directory. Wishing you continuous success with your tools and advisory work!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    },
    {
        "to": "shiqicao@gmail.com",
        "subject": "Re: [Tool Submission] gh-pull — local GitHub pull-request dashboard",
        "name": "gh-pull",
        "text": """Hi Shiqi (and Codex),

Thanks for submitting gh-pull to ToolsRadar!

As developers who frequently juggle pull requests across multiple repositories, we really appreciate tools built on top of the native GitHub CLI (`gh`). The stacked PR dependency visualization and unresolved thread counters are fantastic additions for terminal-first workflows.

gh-pull is now featured in our DevTools & CLI section:
👉 https://lordorange.top/tool/gh-pull/

We've highlighted your MIT open-source license and the quick installation command (`gh extension install shiqicao/gh-pull`).

If you'd like to help spread the word, adding a small badge or link to ToolsRadar in your GitHub README would be greatly appreciated!

Keep up the great work!

Best regards,
The ToolsRadar Editorial Team
https://lordorange.top""",
        "html": """<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 20px;">
  <p>Hi Shiqi (and Codex),</p>
  <p>Thanks for submitting <strong>gh-pull</strong> to ToolsRadar!</p>
  <p>As developers who frequently juggle pull requests across multiple repositories, we really appreciate tools built on top of the native GitHub CLI (<code>gh</code>). The stacked PR dependency visualization and unresolved thread counters are fantastic additions for terminal-first workflows.</p>
  <p>gh-pull is now featured in our <strong>DevTools & CLI</strong> section:<br>
  👉 <a href="https://lordorange.top/tool/gh-pull/" style="color: #f97316; font-weight: 600; text-decoration: none;">https://lordorange.top/tool/gh-pull/</a></p>
  <p>We've highlighted your MIT open-source license and the quick installation command (<code>gh extension install shiqicao/gh-pull</code>).</p>
  <p>If you'd like to help spread the word, adding a small badge or link to ToolsRadar in your GitHub README would be greatly appreciated!</p>
  <br>
  <p style="margin-bottom: 4px;">Best regards,</p>
  <p style="font-weight: 600; margin: 0; color: #111827;">The ToolsRadar Editorial Team</p>
  <p style="margin: 0;"><a href="https://lordorange.top" style="color: #6b7280; text-decoration: none;">lordorange.top</a></p>
</div>"""
    }
]

def send_email(item):
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "ToolsRadar-Notifier/1.0"
    }
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
            return True, res_json
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"FAILED: Send to {item['to']} ({item['name']}) HTTP {e.code}: {err_msg}")
        return False, err_msg
    except Exception as e:
        print(f"ERROR: Send to {item['to']} ({item['name']}): {str(e)}")
        return False, str(e)

def main():
    print("Starting email dispatch via Resend API...")
    results = []
    for item in EMAILS:
        ok, res = send_email(item)
        results.append((item["name"], item["to"], ok, res))
        time.sleep(0.5)
    print("\nSummary:")
    for name, to, ok, res in results:
        status = "SENT" if ok else "FAILED"
        print(f"- [{status}] {name} -> {to}")

if __name__ == "__main__":
    main()
