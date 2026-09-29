"""
Tools Radar - New API / LLM Connectivity Test Script
Tests connectivity, authentication, and enriched structured output response from your New API instance.
"""

import os
import sys
import json
import time
import requests

# Ensure proper stdout encoding on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def load_dotenv(env_path=None):
    if env_path is None:
        env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
        print(f"[Info] Found .env file at: {os.path.abspath(env_path)}")
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip("'\"")
                if k and k not in os.environ:
                    os.environ[k] = v
    else:
        print(f"[Notice] No .env file found at {os.path.abspath(env_path)}.")

def test_connection():
    load_dotenv()

    api_base = os.environ.get("AI_API_BASE", "").strip()
    api_key = os.environ.get("AI_API_KEY", "").strip() or os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get("AI_MODEL", "google/gemini-3.5-flash-lite").strip()

    print("=" * 60)
    print(" Tools Radar - AI Configuration & Deep Extraction Tester")
    print("=" * 60)
    print(f"  AI_API_BASE: {api_base or '(Not set - will default to https://api.openai.com/v1)'}")
    print(f"  AI_API_KEY : {'*' * 8 + api_key[-4:] if len(api_key) > 8 else '(Not set / Empty)'}")
    print(f"  AI_MODEL   : {model}")
    print("-" * 60)

    if not api_key:
        print("\n[!] Error: AI_API_KEY is not set!")
        sys.exit(1)

    # Normalize endpoint
    base = api_base.rstrip("/") if api_base else "https://api.openai.com/v1"
    if not base.endswith("/v1"):
        endpoint = f"{base}/v1/chat/completions"
    else:
        endpoint = f"{base}/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    system_prompt = (
        "You are a senior tech analyst, software architect, and product scout curating top developer tools, open-source repositories, and AI apps.\n"
        "Analyze the provided product info and return ONLY a valid JSON object matching the exact schema below.\n\n"
        "JSON Schema:\n"
        "{\n"
        '  "name": "Clean canonical product name (e.g. Univer, Supabase, LangChain)",\n'
        '  "tagline": "A punchy, compelling English one-liner (max 80 chars) describing its superpower",\n'
        '  "summary": "2 informative sentences explaining the core value, problem solved, and technical edge",\n'
        '  "category": "Must be exactly ONE of: ai-agents, ai-tools, developer-tools, open-source, frameworks-libraries, database-storage, security-devops, cybersecurity-reverse, productivity, design-ui, testing-qa, web-scraping-apis",\n'
        '  "tags": ["3 to 5 concise tags like TypeScript, AI Agents, Canvas, Headless"],\n'
        '  "pricing_model": "One of: Open Source, Free, Freemium, Paid",\n'
        '  "primary_alternative": "A well-known commercial SaaS alternative it competes with or replaces, or null",\n'
        '  "is_self_hostable": true or false,\n'
        '  "no_signup_required": true or false,\n'
        '  "verdict": "1-2 authoritative sentences providing an expert verdict on who should adopt this tool and why it stands out",\n'
        '  "key_features": [\n'
        '    {"title": "Feature 1 Title", "description": "Concise 1-sentence feature explanation"},\n'
        '    {"title": "Feature 2 Title", "description": "Concise 1-sentence feature explanation"},\n'
        '    {"title": "Feature 3 Title", "description": "Concise 1-sentence feature explanation"}\n'
        '  ],\n'
        '  "use_cases": [\n'
        '    "Specific realistic engineering or business use case 1",\n'
        '    "Specific realistic engineering or business use case 2",\n'
        '    "Specific realistic engineering or business use case 3"\n'
        '  ],\n'
        '  "pros": [\n'
        '    "Specific unique advantage or technical moat (not generic)",\n'
        '    "Specific developer experience or cost/privacy benefit",\n'
        '    "Specific architectural flexibility or performance highlight"\n'
        '  ],\n'
        '  "cons": [\n'
        '    "Genuine technical limitation or steeper learning curve",\n'
        '    "Trade-off compared to established commercial giants"\n'
        '  ],\n'
        '  "target_audience": "1 sentence describing exactly who will benefit most from using this tool",\n'
        '  "comparison_vs_alt": "1-2 sentences comparing it directly to primary_alternative, highlighting open-source control, privacy, or pricing advantages",\n'
        '  "install_command": "Best realistic CLI command to install or run (e.g. npm install ..., pip install ..., docker run ..., or curl ...), or null"\n'
        "}\n\n"
        "Constraints:\n"
        "- Return pure JSON only, without markdown fences or additional text.\n"
        "- Pros and cons must be specific to this tool's actual nature, avoiding repetitive boilerplate."
    )

    test_payload = {
        "model": model,
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": (
                    "Product: Univer\n"
                    "Description: The Office Harness for AI Agents — Spreadsheets, Docs, Slides, Canvas, Relational Tables, and PDF in one runtime.\n"
                    "URL: https://github.com/dream-num/univer\n"
                    "GitHub: https://github.com/dream-num/univer\n"
                    "Stars: 21500"
                )
            }
        ]
    }

    print(f"\n[*] Sending test request using model: '{model}' to: {endpoint}")
    start_time = time.time()

    try:
        resp = requests.post(endpoint, json=test_payload, headers=headers, timeout=25)
        duration = round((time.time() - start_time) * 1000, 2)

        print(f"Status Code: {resp.status_code} (took {duration} ms)")

        if resp.status_code == 200:
            res_json = resp.json()
            raw_content = res_json["choices"][0]["message"]["content"].strip()
            
            cleaned = raw_content
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            cleaned = cleaned.strip()

            parsed_data = json.loads(cleaned)
            print(f"\n[SUCCESS] Deep AI Extraction Succeeded with model: {model}!")
            print("-" * 60)
            print(json.dumps(parsed_data, indent=2, ensure_ascii=False))
            print("-" * 60)
            return True
        else:
            print(f"\n[FAIL] Request failed with HTTP {resp.status_code}:")
            print(resp.text)
            return False
    except Exception as e:
        print(f"\n[FAIL] Unexpected error: {e}")
        return False

if __name__ == "__main__":
    test_connection()
