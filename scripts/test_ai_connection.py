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
    model = os.environ.get("AI_MODEL", "google/gemini-3.1-flash-lite").strip()

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
        "You are a senior tech analyst and product architect curating top developer tools, open-source repositories, and AI apps.\n"
        "Analyze the product info and return ONLY a valid JSON object with the following fields:\n"
        "{\n"
        '  "name": "Clean canonical product or project name",\n'
        '  "tagline": "A punchy, compelling English one-liner (max 80 chars)",\n'
        '  "summary": "2 informative sentences explaining the core value, problem solved, and technical edge",\n'
        '  "category": "Must be exactly ONE of: developer-tools, ai-tools, productivity, open-source, security-devops, design-ui",\n'
        '  "tags": ["3 to 5 concise tags like TypeScript, AI Agents, Canvas, Headless"],\n'
        '  "pricing_model": "One of: Open Source, Free, Freemium, Paid",\n'
        '  "primary_alternative": "A well-known commercial SaaS alternative it competes with or replaces (e.g. Google Workspace, Airtable, Notion, Linear, Cursor, PostHog), or null",\n'
        '  "is_self_hostable": true or false,\n'
        '  "no_signup_required": true or false,\n'
        '  "key_features": [\n'
        '    {"title": "Feature 1 Title", "description": "Concise 1-sentence feature explanation"},\n'
        '    {"title": "Feature 2 Title", "description": "Concise 1-sentence feature explanation"},\n'
        '    {"title": "Feature 3 Title", "description": "Concise 1-sentence feature explanation"}\n'
        '  ],\n'
        '  "target_audience": "1 sentence describing exactly who will benefit most from using this tool",\n'
        '  "comparison_vs_alt": "1-2 sentences comparing it directly to primary_alternative, highlighting advantages like open-source control, data privacy, extensibility, or cost savings"\n'
        "}\n"
        "Return ONLY pure JSON without markdown backticks or commentary."
    )

    models_to_try = [model]
    if not model.startswith("google/") and "gemini" in model.lower():
        models_to_try.append(f"google/{model}")
    elif model.startswith("google/"):
        models_to_try.append(model.replace("google/", ""))

    for attempt_model in models_to_try:
        test_payload = {
            "model": attempt_model,
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
                        "Stars: 20700"
                    )
                }
            ]
        }

        print(f"\n[*] Sending test request using model: '{attempt_model}' to: {endpoint}")
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
                print(f"\n[SUCCESS] Deep AI Extraction Succeeded with model: {attempt_model}!")
                print("-" * 60)
                print(json.dumps(parsed_data, indent=2, ensure_ascii=False))
                print("-" * 60)
                return True
            elif "model_not_found" in resp.text and attempt_model != models_to_try[-1]:
                print(f"[Notice] Model '{attempt_model}' not found in channel, auto-trying '{models_to_try[-1]}'...")
                continue
            else:
                print(f"\n[FAIL] Request failed with HTTP {resp.status_code}:")
                print(resp.text)
                return False
        except Exception as e:
            print(f"\n[FAIL] Unexpected error: {e}")
            return False

    return False

if __name__ == "__main__":
    test_connection()
