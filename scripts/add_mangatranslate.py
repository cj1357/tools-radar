import json
import os
import datetime

NEW_TOOL = {
    "id": "mangatranslate",
    "name": "MangaTranslate",
    "tagline": "AI-powered manga and comic translation for images and PDFs with editable typesetting",
    "summary": "MangaTranslate is a specialized multimodal AI utility engineered to detect, OCR, translate, and re-typeset dialogue within manga, comics, and graphic PDFs. Featuring source-to-target language pairing, automated text balloon inpainting, and an interactive browser-based canvas editor for manual font adjustments and dialogue repositioning, it streamlines comic localization for scanlation teams and international readers.",
    "url": "https://www.mangatranslate.com/",
    "github_url": None,
    "source": "github_issue",
    "category": "ai-tools",
    "tags": [
        "Manga Translation",
        "Comic OCR",
        "AI Vision",
        "Typesetting",
        "Image Translation",
        "PDF"
    ],
    "pricing_model": "Freemium",
    "stars": 0,
    "primary_alternative": "Manual OCR & Photoshop Typesetting",
    "is_self_hostable": False,
    "no_signup_required": True,
    "signal_score": 85,
    "verdict": "A remarkably well-executed vertical AI translation application that solves the notoriously difficult scanlation workflow by pairing vision OCR with automatic balloon inpainting and an editable canvas typesetter.",
    "key_features": [
        {
            "title": "Automated Manga OCR & Inpainting",
            "description": "Detects vertical and horizontal dialogue bubbles, removes original Japanese/Korean/Chinese text, and inpaints backgrounds."
        },
        {
            "title": "Interactive Typesetting Canvas",
            "description": "Drag-and-drop web editor allowing manual dialogue tweaks, font resizing, line wrapping, and balloon repositioning before export."
        },
        {
            "title": "Batch Image & PDF Pipeline",
            "description": "Process whole chapters in bulk across multiple source and target language pairs with developer API integration."
        }
    ],
    "use_cases": [
        "Localizing manga chapters and independent webtoons from Japanese/Korean into English or Spanish",
        "Translating technical graphic documentation and illustrated guides in PDF format",
        "Accelerating community scanlation workflows by automating the tedious bubble cleaning and typesetting phases"
    ],
    "pros": [
        "5 Free daily credits for guests without requiring account creation",
        "Built-in interactive canvas editor avoids needing external editing tools like Photoshop",
        "Supports both image batches and multi-page PDF documents"
    ],
    "cons": [
        "Complex hand-lettered SFX (sound effects) outside speech bubbles may require manual retouching",
        "High-volume batch translation requires paid subscription or API credits"
    ],
    "target_audience": "Manga readers, webtoon creators, digital comic publishers, scanlation groups, and localization teams.",
    "comparison_vs_alt": "Unlike generic machine translators that only return raw text, MangaTranslate handles the end-to-end comic localization loop, from bubble segmentation to automated typographic redrawing.",
    "install_command": None,
    "date_added": "2026-10-28",
    "featured": False
}

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    master_file = os.path.join(data_dir, "all_tools.json")
    daily_file = os.path.join(data_dir, "tools", "2026-10-28.json")
    timestamp_file = os.path.join(base_dir, "site", "src", "data-timestamp.json")

    # 1. Update daily file
    daily_tools = []
    if os.path.exists(daily_file):
        with open(daily_file, "r", encoding="utf-8") as f:
            daily_tools = json.load(f)
    
    daily_map = {t["id"]: t for t in daily_tools}
    daily_map[NEW_TOOL["id"]] = NEW_TOOL
    
    with open(daily_file, "w", encoding="utf-8") as f:
        json.dump(list(daily_map.values()), f, indent=2, ensure_ascii=False)
    print(f"Updated {daily_file}")

    # 2. Update master all_tools.json
    with open(master_file, "r", encoding="utf-8") as f:
        all_tools = json.load(f)

    tools_map = {t["id"]: t for t in all_tools}
    tools_map[NEW_TOOL["id"]] = NEW_TOOL

    sorted_tools = sorted(tools_map.values(), key=lambda x: x.get("date_added", ""), reverse=True)

    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(sorted_tools, f, indent=2, ensure_ascii=False)
    print(f"Updated master {master_file} with {len(sorted_tools)} tools")

    # 3. Update timestamp
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(timestamp_file, "w", encoding="utf-8") as f:
        json.dump({"updated_at": now_iso}, f, indent=2)
    print(f"Updated timestamp in {timestamp_file} to {now_iso}")

if __name__ == "__main__":
    main()
