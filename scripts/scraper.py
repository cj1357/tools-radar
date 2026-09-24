"""
Tools Radar - Automated Trending Scraper & Structurer
Fetches trending products and repositories from GitHub Trending, Hacker News Show, and Product Hunt.
Extracts alternatives, self-hostable badges, no-signup tags, and signal score.
"""

import os
import re
import json
import time
import datetime
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
TOOLS_DIR = os.path.join(DATA_DIR, "tools")
os.makedirs(TOOLS_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=3)
session.mount("https://", adapter)
session.mount("http://", adapter)
session.headers.update({"User-Agent": USER_AGENT})

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")[:60]

def fetch_github_trending(limit=15):
    print("Fetching GitHub Trending...")
    items = []
    try:
        url = "https://github.com/trending?since=daily"
        resp = session.get(url, timeout=15)
        resp.raise_for_status()
        html = resp.text
        
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.select("article.Box-row")
        print(f"GitHub Trending found {len(articles)} articles.")
        
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
        print(f"Error fetching GitHub Trending: {e}")
    return items

def fetch_hackernews_show(limit=15):
    print("Fetching Hacker News Show HN...")
    items = []
    try:
        url = "https://hacker-news.firebaseio.com/v0/showstories.json"
        resp = session.get(url, timeout=15)
        story_ids = resp.json()
        print(f"Hacker News found {len(story_ids)} show stories.")
        
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
            except Exception as item_err:
                continue
    except Exception as e:
        print(f"Error fetching Hacker News: {e}")
    return items

def fetch_producthunt_feed(limit=15):
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
            
        print(f"Product Hunt found {len(entries)} Atom entries.")
        
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
        print(f"Error fetching Product Hunt: {e}")
    return items

def infer_alternative_and_features(text: str, url: str, github_url: str | None, stars: int, source: str):
    """Infers commercial alternatives, self-hostable status, and no-signup attributes."""
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

def run_scraper():
    print("=" * 50)
    print(f"Tools Radar Scraper - Starting at {datetime.datetime.now().isoformat()}")
    print("=" * 50)
    
    all_raw = []
    all_raw.extend(fetch_github_trending(limit=10))
    all_raw.extend(fetch_hackernews_show(limit=10))
    all_raw.extend(fetch_producthunt_feed(limit=10))
    
    print(f"Total raw items collected across all sources: {len(all_raw)}")
    
    seen_slugs = set()
    structured_tools = []
    source_counts = {}
    
    for raw in all_raw:
        structured = classify_and_structure_heuristic(raw)
        if not structured["id"] or structured["id"] in seen_slugs:
            continue
        if len(structured["name"]) < 2 or len(structured["summary"]) < 10:
            continue
            
        seen_slugs.add(structured["id"])
        structured_tools.append(structured)
        src = structured["source"]
        source_counts[src] = source_counts.get(src, 0) + 1
        
    print(f"Processed tools by source: {source_counts}")
    
    today_str = datetime.date.today().isoformat()
    daily_file = os.path.join(TOOLS_DIR, f"{today_str}.json")
    
    with open(daily_file, "w", encoding="utf-8") as f:
        json.dump(structured_tools, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(structured_tools)} tools to {daily_file}")
    
    # Update master all_tools.json
    master_file = os.path.join(DATA_DIR, "all_tools.json")
    master_data = {}
    if os.path.exists(master_file):
        try:
            with open(master_file, "r", encoding="utf-8") as f:
                master_list = json.load(f)
                for t in master_list:
                    master_data[t["id"]] = t
        except Exception:
            master_data = {}
            
    for t in structured_tools:
        master_data[t["id"]] = t
        
    sorted_tools = sorted(master_data.values(), key=lambda x: x.get("date_added", ""), reverse=True)
    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(sorted_tools, f, indent=2, ensure_ascii=False)
        
    print(f"Master index updated: {len(sorted_tools)} total unique tools recorded.")
    print("Done!")

if __name__ == "__main__":
    run_scraper()
