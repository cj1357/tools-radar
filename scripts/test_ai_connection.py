"""
Tools Radar - New API / LLM Connectivity Test Script
Tests connectivity, authentication, and structured output response from your New API instance.
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
        print("         You can create one or export environment variables directly.")

def test_connection():
    load_dotenv()

    api_base = os.environ.get("AI_API_BASE", "").strip()
    api_key = os.environ.get("AI_API_KEY", "").strip() or os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get("AI_MODEL", "gemini-2.5-flash-lite").strip()

    print("=" * 60)
    print(" Tools Radar - AI Configuration & Connectivity Tester")
    print("=" * 60)
    print(f"  AI_API_BASE: {api_base or '(Not set - will default to https://api.openai.com/v1)'}")
    print(f"  AI_API_KEY : {'*' * 8 + api_key[-4:] if len(api_key) > 8 else '(Not set / Empty)'}")
    print(f"  AI_MODEL   : {model}")
    print("-" * 60)

    if not api_key:
        print("\n[!] Error: AI_API_KEY is not set!")
        print("\nPlease create a .env file in the root directory (tools-radar/.env) with:")
        print("  AI_API_BASE=https://your-new-api-domain.com/v1")
        print("  AI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx")
        print("  AI_MODEL=gemini-2.5-flash-lite")
        print("\nOr configure it directly in your environment variables.")
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

    test_payload = {
        "model": model,
        "temperature": 0.2,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a tech analyst curating developer tools. "
                    "Analyze the product info and output ONLY a JSON object with: "
                    "name (str), tagline (max 80 chars), summary (1-2 sentences), "
                    "category (one of: developer-tools, ai-tools, productivity, open-source, security-devops, design-ui), "
                    "tags (list of 3-5 strings), primary_alternative (string or null), "
                    "is_self_hostable (bool), no_signup_required (bool)."
                )
            },
            {
                "role": "user",
                "content": (
                    "Tool: Univer\n"
                    "Description: The Office Harness for AI Agents — Spreadsheets, Docs, Slides, Canvas, Relational Tables, and PDF in one runtime.\n"
                    "URL: https://github.com/dream-num/univer"
                )
            }
        ]
    }

    print(f"\n[*] Sending test request to: {endpoint}")
    start_time = time.time()

    try:
        resp = requests.post(endpoint, json=test_payload, headers=headers, timeout=25)
        duration = round((time.time() - start_time) * 1000, 2)

        print(f"Status Code: {resp.status_code} (took {duration} ms)")

        if resp.status_code == 200:
            res_json = resp.json()
            raw_content = res_json["choices"][0]["message"]["content"].strip()
            
            # Clean markdown code block wraps if present
            cleaned = raw_content
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            cleaned = cleaned.strip()

            parsed_data = json.loads(cleaned)
            print("\n[SUCCESS] Connection & Model Inference Succeeded!")
            print("-" * 60)
            print(json.dumps(parsed_data, indent=2, ensure_ascii=False))
            print("-" * 60)
            print("[Verified items]:")
            print(f"  - Product Name       : {parsed_data.get('name')}")
            print(f"  - Punchy Tagline     : {parsed_data.get('tagline')}")
            print(f"  - Category           : {parsed_data.get('category')}")
            print(f"  - Commercial Alt     : {parsed_data.get('primary_alternative')}")
            print(f"  - Self Hostable      : {parsed_data.get('is_self_hostable')}")
            print(f"  - No Signup Required : {parsed_data.get('no_signup_required')}")
            print("\nAll systems go! You are ready to run the automated scraper with AI enrichment.")
            return True
        else:
            print(f"\n[FAIL] Request failed with HTTP {resp.status_code}:")
            print(resp.text)
            print("\nTroubleshooting tips:")
            if resp.status_code in [401, 403]:
                print("  - Check if your AI_API_KEY (token) is correct and has quota in New API.")
            elif resp.status_code == 404:
                print("  - Check your AI_API_BASE URL. Make sure it points to your New API host.")
            elif resp.status_code == 429:
                print("  - Rate limit exceeded (RPM/RPD) on the upstream provider.")
            else:
                print("  - Check New API channel configuration to ensure model mapping is active.")
            return False

    except requests.exceptions.ConnectionError as e:
        print(f"\n[FAIL] Network / Connection Error: Unable to reach {endpoint}")
        print(f"Details: {e}")
        print("\nTroubleshooting:")
        print("  - Make sure your New API server is running and accessible from your network.")
        print("  - If using https, verify SSL certificate or try http if local.")
        return False
    except json.JSONDecodeError:
        print(f"\n[WARN] Response received but failed to parse as JSON:")
        print(raw_content)
        return False
    except Exception as e:
        print(f"\n[FAIL] Unexpected error: {e}")
        return False

if __name__ == "__main__":
    test_connection()
