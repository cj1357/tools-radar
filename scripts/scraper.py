"""
Tools Radar - Automated Trending Scraper & Structurer
Fetches trending products and repositories from GitHub Trending, Hacker News Show, and Product Hunt.
Supports AI-powered classification and feature extraction via New API / OpenAI-compatible LLM
with automatic rate limiting (15 RPM / 4.2s delay) and seamless heuristic fallback.
"""

import os
import sys
import re
import json
import time
import datetime
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

# Ensure proper stdout encoding on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
TOOLS_DIR = os.path.join(DATA_DIR, "tools")
os.makedirs(TOOLS_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=3)
session.mount("https://", adapter)
session.mount("http://", adapter)
session.headers.update({"User-Agent": USER_AGENT})

def load_dotenv(env_path=None):
    """Loads environment variables from .env file if present."""
    if env_path is None:
        env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
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

load_dotenv()

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")[:60]

def fetch_github_trending(limit=10):
    print("Fetching GitHub Trending...")
    items = []
    try:
        url = "https://github.com/trending?since=daily"
        resp = session.get(url, timeout=15)
        resp.raise_for_status()
        html = resp.text
        
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.select("article.Box-row")
        print(f"  GitHub Trending found {len(articles)} repositories.")
        
        for art in articles[:limit]:
            h2 = art.select_one("h2 a")
            if not h2:
                continue
            repo_path = h2.get("href", "").strip().lstrip("/")
            repo_name = repo_path.split("/")[-1] if "/" in repo_path else repo_path
            full_repo_url = f"https://github.com/{repo_path}"
            
            p = art.select_one("p")
            description = p.get_text(strip=True) if p else "No description provided."
            
            # Stars
            star_elem = art.select_one("a[href$='/stargazers']")
            stars = 0
            if star_elem:
                star_text = star_elem.get_text(strip=True).replace(",", "")
                if "k" in star_text.lower():
                    try:
                        stars = int(float(star_text.lower().replace("k", "")) * 1000)
                    except ValueError:
                        stars = 0
                else:
                    try:
                        stars = int(star_text)
                    except ValueError:
                        stars = 0
                        
            # Language
            lang_elem = art.select_one("span[itemprop='programmingLanguage']")
            lang = lang_elem.get_text(strip=True) if lang_elem else None
            
            items.append({
                "raw_name": repo_name,
                "title": repo_name.replace("-", " ").replace("_", " ").title(),
                "url": full_repo_url,
                "github_url": full_repo_url,
                "raw_description": description,
                "source": "github_trending",
                "stars": stars,
                "language": lang
            })
    except Exception as e:
        print(f"  Error fetching GitHub Trending: {e}")
    return items

def fetch_hackernews_show(limit=10):
    print("Fetching Hacker News Show HN...")
    items = []
    try:
        url = "https://hacker-news.firebaseio.com/v0/showstories.json"
        resp = session.get(url, timeout=15)
        story_ids = resp.json()
        print(f"  Hacker News found {len(story_ids)} show stories.")
        
        for sid in story_ids[:limit]:
            try:
                item_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
                item_resp = session.get(item_url, timeout=8)
                data = item_resp.json()
                
                if not data or "title" not in data:
                    continue
                    
                title = data.get("title", "")
                clean_title = re.sub(r"^Show HN:\s*", "", title, flags=re.IGNORECASE).strip()
                out_url = data.get("url") or f"https://news.ycombinator.com/item?id={sid}"
                score = data.get("score", 0)
                
                items.append({
                    "raw_name": clean_title,
                    "title": clean_title,
                    "url": out_url,
                    "github_url": out_url if "github.com" in out_url else None,
                    "raw_description": f"{clean_title} — newly launched project showcased by indie creators on Hacker News with {score} community upvotes.",
                    "source": "hackernews",
                    "stars": score,
                    "language": None
                })
                time.sleep(0.1)
            except Exception:
                continue
    except Exception as e:
        print(f"  Error fetching Hacker News: {e}")
    return items

def fetch_producthunt_feed(limit=10):
    print("Fetching Product Hunt Atom Feed...")
    items = []
    try:
        url = "https://www.producthunt.com/feed"
        resp = session.get(url, timeout=15)
        resp.raise_for_status()
        xml_data = resp.content
        
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entries = root.findall("atom:entry", ns)
        if not entries:
            entries = root.findall(".//entry")
            
        print(f"  Product Hunt found {len(entries)} Atom entries.")
        
        for entry in entries[:limit]:
            title_elem = entry.find("atom:title", ns) if ns else entry.find(".//title")
            link_elem = entry.find("atom:link", ns) if ns else entry.find(".//link")
            content_elem = entry.find("atom:content", ns) if ns else entry.find(".//content")
            
            title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
            link = link_elem.attrib.get("href", "") if link_elem is not None else ""
            
            raw_desc = ""
            if content_elem is not None and content_elem.text:
                soup = BeautifulSoup(content_elem.text, "html.parser")
                raw_desc = soup.get_text(strip=True)
                raw_desc = re.sub(r"Discussion\|Link$", "", raw_desc).strip()
                
            if title and link:
                items.append({
                    "raw_name": title,
                    "title": title,
                    "url": link,
                    "github_url": None,
                    "raw_description": raw_desc or f"{title} is a newly launched tool on Product Hunt.",
                    "source": "producthunt",
                    "stars": 0,
                    "language": None
                })
    except Exception as e:
        print(f"  Error fetching Product Hunt: {e}")
    return items

def infer_alternative_and_features(text: str, url: str, github_url: str | None, stars: int, source: str):
    """Infers commercial alternatives, self-hostable status, and signal score."""
    combined = text.lower() + " " + url.lower() + " " + (github_url or "").lower()
    
    # 1. Commercial Alternatives Detection
    alt = None
    if any(k in combined for k in ["sheet", "spreadsheet", "airtable", "univer", "excel"]):
        alt = "Google Sheets / Airtable"
    elif any(k in combined for k in ["agentic", "agent runtime", "orchestration", "langchain", "crewai", "autogen"]):
        alt = "LangChain / CrewAI"
    elif any(k in combined for k in ["claude code", "copilot", "cursor", "coding agent", "code assistant"]):
        alt = "Cursor / Copilot"
    elif any(k in combined for k in ["sandbox", "gvisor", "rootless", "container", "isolation"]):
        alt = "Docker / Firecracker"
    elif any(k in combined for k in ["posthog", "telemetry", "observability", "session"]):
        alt = "PostHog / Datadog"
    elif any(k in combined for k in ["manufacturing erp", "mes", "qms", "erp"]):
        alt = "SAP / Odoo"
    elif any(k in combined for k in ["architecture diagram", "diagram", "canvas", "system design"]):
        alt = "Figma / Excalidraw"
    elif any(k in combined for k in ["encryption", "air-gapped", "decrypting", "password", "vault"]):
        alt = "1Password / Bitwarden"
    elif any(k in combined for k in ["dbeaver", "datagrip", "sql client", "database gui", "postgres"]):
        alt = "DBeaver / DataGrip"
    elif any(k in combined for k in ["notion", "notes", "knowledge base"]):
        alt = "Notion / Obsidian"
    elif any(k in combined for k in ["zapier", "make.com", "workflow automation"]):
        alt = "Zapier / Make"
    elif any(k in combined for k in ["analytics", "google analytics"]):
        alt = "Google Analytics"

    # 2. Self-Hostable Check
    is_self_host = any(k in combined for k in [
        "self-hosted", "self-host", "docker", "kubernetes", "compose", "on-premise", "local", "rootless"
    ]) or ("github.com" in combined and any(k in combined for k in ["server", "backend", "deploy"]))

    # 3. No Sign-up Required Check
    no_signup = any(k in combined for k in [
        "no sign-up", "no signup", "no account", "client-side", "air-gapped", "html page", "offline", "wasm", "cli tool"
    ]) or (github_url is not None and any(k in combined for k in ["cli", "library", "sdk", "kernel"]))

    # 4. Signal Score (60 - 99)
    base_score = 65
    if stars > 10000:
        base_score += 25
    elif stars > 1000:
        base_score += 18
    elif stars > 100:
        base_score += 10
    elif stars > 20:
        base_score += 5
        
    if source == "hackernews":
        base_score += 6
    elif source == "github_trending":
        base_score += 5
        
    signal_score = min(base_score, 99)
    
    return alt, is_self_host, no_signup, signal_score

def classify_and_structure_heuristic(raw_item: dict) -> dict:
    """Heuristic fallback for categorizing and structuring without requiring LLM API."""
    text = (raw_item["title"] + " " + raw_item["raw_description"]).lower()
    
    category = "productivity"
    tags = []
    
    ai_keywords = ["ai", "llm", "gpt", "agent", "deepseek", "claude", "gemini", "embedding", "model", "rag", "vision", "chat"]
    dev_keywords = ["cli", "compiler", "library", "framework", "api", "sdk", "rust", "python", "typescript", "golang", "sql", "debugger", "kernel"]
    devops_keywords = ["docker", "kubernetes", "cloud", "aws", "cloudflare", "monitoring", "server", "deploy", "ci/cd", "sandbox"]
    design_keywords = ["ui", "css", "icon", "figma", "tailwind", "design", "canvas", "font", "component", "diagram", "chart"]
    
    if any(k in text for k in ai_keywords):
        category = "ai-tools"
        tags.append("AI")
    elif any(k in text for k in devops_keywords):
        category = "security-devops"
        tags.append("DevOps")
    elif any(k in text for k in dev_keywords):
        category = "developer-tools"
        tags.append("DevTools")
    elif any(k in text for k in design_keywords):
        category = "design-ui"
        tags.append("Design")
    elif raw_item.get("github_url"):
        category = "open-source"
        tags.append("Open Source")
        
    if raw_item.get("language"):
        tags.append(raw_item["language"])
        
    pricing = "Open Source" if raw_item.get("github_url") else "Free"
    
    clean_desc = raw_item["raw_description"]
    clean_desc = re.sub(r"\s+", " ", clean_desc).strip()
    tagline = clean_desc[:110] + ("..." if len(clean_desc) > 110 else "")
    
    slug = slugify(raw_item["raw_name"])
    
    alt, is_self_host, no_signup, signal_score = infer_alternative_and_features(
        raw_item["title"] + " " + clean_desc,
        raw_item["url"],
        raw_item.get("github_url"),
        raw_item.get("stars", 0),
        raw_item["source"]
    )
    
    return {
        "id": slug,
        "name": raw_item["title"],
        "tagline": tagline,
        "summary": clean_desc if len(clean_desc) > 30 else f"{raw_item['title']} is a modern solution designed to improve developer workflow and productivity.",
        "url": raw_item["url"],
        "github_url": raw_item.get("github_url"),
        "source": raw_item["source"],
        "category": category,
        "tags": list(set(tags))[:5],
        "pricing_model": pricing,
        "stars": raw_item.get("stars", 0),
        "primary_alternative": alt,
        "is_self_hostable": is_self_host,
        "no_signup_required": no_signup,
        "signal_score": signal_score,
        "date_added": datetime.date.today().isoformat(),
        "featured": False
    }

def classify_and_structure_ai(raw_item: dict) -> dict | None:
    """Uses LLM (via New API / OpenAI-compatible endpoint) to extract structured features."""
    api_key = os.environ.get("AI_API_KEY", "").strip() or os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        return None

    api_base = os.environ.get("AI_API_BASE", "").strip() or "https://api.openai.com/v1"
    model = os.environ.get("AI_MODEL", "gemini-2.5-flash-lite").strip()

    base = api_base.rstrip("/")
    if not base.endswith("/v1"):
        endpoint = f"{base}/v1/chat/completions"
    else:
        endpoint = f"{base}/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    clean_raw_title = raw_item.get("title", "")
    clean_raw_desc = raw_item.get("raw_description", "")
    url = raw_item.get("url", "")
    github_url = raw_item.get("github_url")
    stars = raw_item.get("stars", 0)
    source = raw_item.get("source", "")

    system_prompt = (
        "You are a senior tech analyst curating top developer tools, open-source projects, and AI software.\n"
        "Analyze the provided tool information and return ONLY a valid JSON object with the following fields:\n"
        "{\n"
        '  "name": "Clean canonical product or project name (strip \'Show HN:\', repo owner prefixes, etc.)",\n'
        '  "tagline": "A punchy, concise English one-liner (max 80 chars) describing what it does",\n'
        '  "summary": "1-2 informative sentences explaining the core value, target users, and why it matters",\n'
        '  "category": "Must be exactly ONE of: developer-tools, ai-tools, productivity, open-source, security-devops, design-ui",\n'
        '  "tags": ["3 to 5 relevant concise tags, e.g. Python, AI, Agent, CLI, Database"],\n'
        '  "pricing_model": "One of: Open Source, Free, Freemium, Paid",\n'
        '  "primary_alternative": "A well-known commercial SaaS alternative it competes with or replaces (e.g. Notion, Airtable, Linear, Cursor, PostHog, Figma, Supabase, Zapier), or null if none",\n'
        '  "is_self_hostable": true or false (can developers run or deploy it locally/on-premise via Docker or source),\n'
        '  "no_signup_required": true or false (can it be used without registering an account, e.g. open source repo, CLI, local-first app)\n'
        "}\n"
        "Return ONLY pure JSON without markdown backticks or extra commentary."
    )

    user_prompt = (
        f"Product: {clean_raw_title}\n"
        f"Source: {source}\n"
        f"URL: {url}\n"
        f"GitHub: {github_url or 'N/A'}\n"
        f"Stars/Upvotes: {stars}\n"
        f"Description: {clean_raw_desc}"
    )

    payload = {
        "model": model,
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    max_retries = 2
    for attempt in range(max_retries):
        try:
            resp = requests.post(endpoint, json=payload, headers=headers, timeout=25)
            if resp.status_code == 429:
                print(f"    [Rate Limit 429] Waiting 10s before retry (attempt {attempt+1}/{max_retries})...")
                time.sleep(10)
                continue
            if resp.status_code != 200:
                print(f"    [AI API Error] HTTP {resp.status_code}: {resp.text[:120]}")
                return None

            res_json = resp.json()
            content = res_json["choices"][0]["message"]["content"].strip()

            cleaned = content
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            cleaned = cleaned.strip()

            ai_data = json.loads(cleaned)

            valid_cats = ["developer-tools", "ai-tools", "productivity", "open-source", "security-devops", "design-ui"]
            cat = ai_data.get("category", "")
            if cat not in valid_cats:
                cat = "open-source" if github_url else "productivity"

            name = ai_data.get("name") or clean_raw_title
            slug = slugify(name if len(name) > 2 else raw_item["raw_name"])
            tagline = ai_data.get("tagline") or clean_raw_desc[:80]
            summary = ai_data.get("summary") or clean_raw_desc
            tags = ai_data.get("tags") or []
            if raw_item.get("language") and raw_item["language"] not in tags:
                tags.append(raw_item["language"])

            pricing = ai_data.get("pricing_model") or ("Open Source" if github_url else "Free")
            alt = ai_data.get("primary_alternative")
            is_self_host = bool(ai_data.get("is_self_hostable", False))
            no_signup = bool(ai_data.get("no_signup_required", False))

            _, _, _, signal_score = infer_alternative_and_features(
                name + " " + summary,
                url,
                github_url,
                stars,
                source
            )

            return {
                "id": slug,
                "name": name,
                "tagline": tagline,
                "summary": summary,
                "url": url,
                "github_url": github_url,
                "source": source,
                "category": cat,
                "tags": [t for t in tags if isinstance(t, str)][:5],
                "pricing_model": pricing,
                "stars": stars,
                "primary_alternative": alt,
                "is_self_hostable": is_self_host,
                "no_signup_required": no_signup,
                "signal_score": signal_score,
                "date_added": datetime.date.today().isoformat(),
                "featured": False
            }

        except requests.exceptions.RequestException as e:
            print(f"    [AI Request Failed]: {e}")
            return None
        except (json.JSONDecodeError, KeyError) as e:
            print(f"    [AI Parse Error]: {e}")
            return None
        except Exception as e:
            print(f"    [AI Unexpected Error]: {e}")
            return None

    return None

def run_scraper():
    print("=" * 60)
    print(f"Tools Radar Scraper - Starting at {datetime.datetime.now().isoformat()}")
    print("=" * 60)

    # 1. Load Master Tools Database
    master_file = os.path.join(DATA_DIR, "all_tools.json")
    master_data = {}
    if os.path.exists(master_file):
        try:
            with open(master_file, "r", encoding="utf-8") as f:
                master_list = json.load(f)
                for t in master_list:
                    master_data[t["id"]] = t
        except Exception as e:
            print(f"Warning: Failed to load master file: {e}")
            master_data = {}

    print(f"Database currently holds {len(master_data)} existing tools.")

    # 2. Check AI Configuration
    api_key = os.environ.get("AI_API_KEY", "").strip() or os.environ.get("OPENAI_API_KEY", "").strip()
    use_ai = bool(api_key)
    if use_ai:
        api_base = os.environ.get("AI_API_BASE", "https://api.openai.com/v1")
        model = os.environ.get("AI_MODEL", "gemini-2.5-flash-lite")
        print(f"[AI Mode Active] Base: {api_base} | Model: {model} | RateLimit: 4.2s delay (15 RPM safe)")
    else:
        print("[Rule-Based Mode] No AI_API_KEY detected. Using fast heuristic extraction.")

    # 3. Fetch from all sources
    all_raw = []
    all_raw.extend(fetch_github_trending(limit=10))
    all_raw.extend(fetch_hackernews_show(limit=10))
    all_raw.extend(fetch_producthunt_feed(limit=10))
    
    print(f"\nTotal raw items collected across all sources: {len(all_raw)}")
    
    seen_slugs = set()
    structured_tools = []
    source_counts = {}
    ai_enrichment_count = 0
    reused_count = 0
    fallback_count = 0
    
    for i, raw in enumerate(all_raw):
        candidate_slug = slugify(raw["raw_name"])
        prefix = f"[{i+1}/{len(all_raw)}] {raw.get('source')}: {raw.get('title')[:30]}"

        # Optimization: Check if already in master database to save AI tokens/quota
        if candidate_slug in master_data:
            existing = master_data[candidate_slug]
            existing["stars"] = max(existing.get("stars", 0), raw.get("stars", 0))
            if candidate_slug not in seen_slugs:
                seen_slugs.add(candidate_slug)
                structured_tools.append(existing)
                src = existing.get("source", raw.get("source"))
                source_counts[src] = source_counts.get(src, 0) + 1
                reused_count += 1
            print(f"{prefix} -> Reused from DB (saved AI quota)")
            continue

        structured = None
        if use_ai:
            print(f"{prefix} -> Calling AI...")
            structured = classify_and_structure_ai(raw)
            if structured:
                ai_enrichment_count += 1
                # Enforce safe delay for Google AI Studio Free Tier (15 RPM = ~4.0s minimum)
                time.sleep(4.2)

        if not structured:
            structured = classify_and_structure_heuristic(raw)
            fallback_count += 1
            if not use_ai:
                print(f"{prefix} -> Rule heuristic applied")
            else:
                print(f"{prefix} -> AI failed/skipped, fallback applied")
            
        if not structured["id"] or structured["id"] in seen_slugs:
            continue
        if len(structured["name"]) < 2 or len(structured["summary"]) < 10:
            continue
            
        seen_slugs.add(structured["id"])
        structured_tools.append(structured)
        src = structured["source"]
        source_counts[src] = source_counts.get(src, 0) + 1
        
    print("\n" + "-" * 50)
    print(f"Processing Summary:")
    print(f"  • Total items processed : {len(structured_tools)}")
    print(f"  • AI Enriched           : {ai_enrichment_count}")
    print(f"  • DB Reused (0 tokens)  : {reused_count}")
    print(f"  • Rule-based Fallback   : {fallback_count}")
    print(f"  • Source Breakdown      : {source_counts}")
    print("-" * 50)
    
    today_str = datetime.date.today().isoformat()
    daily_file = os.path.join(TOOLS_DIR, f"{today_str}.json")
    
    with open(daily_file, "w", encoding="utf-8") as f:
        json.dump(structured_tools, f, indent=2, ensure_ascii=False)
    print(f"Saved daily snapshot to: {daily_file}")
    
    # Update master all_tools.json
    for t in structured_tools:
        master_data[t["id"]] = t
        
    sorted_tools = sorted(master_data.values(), key=lambda x: x.get("date_added", ""), reverse=True)
    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(sorted_tools, f, indent=2, ensure_ascii=False)
        
    print(f"Master index updated: {len(sorted_tools)} total unique tools recorded.")
    print("Done!")

if __name__ == "__main__":
    run_scraper()
