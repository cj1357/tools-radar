import json

fastrelease_faqs = [
    {
        "q": "How is Fastrelease licensed and delivered?",
        "a": "Fastrelease is a commercial Node.js codebase. After purchasing a single-project perpetual license ($199) or annual unlimited-project tier ($249/yr, $299/yr), the buyer receives repository access to the complete source code under commercial license terms."
    },
    {
        "q": "What external integrations are required to run Fastrelease?",
        "a": "Fastrelease is configured directly by the buyer. It is pre-wired for external service integrations including Stripe for payment processing and Mailgun for transactional emails, backed by a self-managed PostgreSQL database and Docker orchestration."
    },
    {
        "q": "Does Fastrelease offer an API-key trial or online product demo?",
        "a": "No. Fastrelease does not offer an online demo, API-key trial, or free tier. Opening the homepage allows buyers to purchase a license, after which source code repository access is granted."
    },
    {
        "q": "What level of technical expertise is required to deploy Fastrelease?",
        "a": "Because Fastrelease is purchased source code rather than a managed SaaS, buyers are responsible for configuring environment variables, running Docker Compose, and deploying to their own VPS or server infrastructure."
    },
    {
        "q": "Has Fastrelease undergone an independent third-party security audit?",
        "a": "No third-party code audit has been supplied. Fastrelease provides the source code for buyers to configure, audit, and host within their own environments according to their organizational standards."
    }
]

install_cmd = "# 1. Purchase commercial license on fastrelease.net to receive repository access\n# 2. Clone your licensed repository & configure environment variables (Stripe, PostgreSQL, Mailgun)\ncp .env.example .env\ndocker compose up -d"

# 1. Update data/all_tools.json
with open("data/all_tools.json", "r", encoding="utf-8") as f:
    tools = json.load(f)

for t in tools:
    if t["id"] == "fastrelease":
        t["primary_alternative"] = None
        t["comparison_vs_alt"] = None
        t["install_command"] = install_cmd
        t["faqs"] = fastrelease_faqs
        print("Updated Fastrelease in all_tools.json")
        break

with open("data/all_tools.json", "w", encoding="utf-8") as f:
    json.dump(tools, f, indent=2, ensure_ascii=False)

# 2. Update data/tools/2026-10-27.json
with open("data/tools/2026-10-27.json", "r", encoding="utf-8") as f:
    daily_tools = json.load(f)

for t in daily_tools:
    if t["id"] == "fastrelease":
        t["primary_alternative"] = None
        t["comparison_vs_alt"] = None
        t["install_command"] = install_cmd
        t["faqs"] = fastrelease_faqs
        print("Updated Fastrelease in 2026-10-27.json")
        break

with open("data/tools/2026-10-27.json", "w", encoding="utf-8") as f:
    json.dump(daily_tools, f, indent=2, ensure_ascii=False)
