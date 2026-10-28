import json
import os
import datetime

NEW_TOOL = {
    "id": "neatbo-svg-pattern-generator",
    "name": "Neatbo SVG Pattern Generator",
    "tagline": "Generate customizable repeating SVG background tiles directly in your browser",
    "summary": "Neatbo SVG Pattern Generator is a frictionless, browser-based design utility for creating lightweight repeating SVG background textures. Designers and frontend developers can rapidly select dot, grid, or diagonal motifs, tweak tile dimensions, customize color schemes, and export clean SVG tile assets with zero account registration.",
    "url": "https://neatbo.com/color/svg-pattern-generator",
    "github_url": None,
    "source": "submission",
    "category": "design-ui",
    "tags": [
        "SVG",
        "Pattern Generator",
        "Backgrounds",
        "Design Tools",
        "Frontend",
        "Vector Graphics"
    ],
    "pricing_model": "Free",
    "stars": 0,
    "primary_alternative": "Hero Patterns",
    "is_self_hostable": False,
    "no_signup_required": True,
    "signal_score": 82,
    "verdict": "A delightfully straightforward, zero-friction SVG pattern generator that solves the exact micro-need of crafting repeating geometric background textures without bloat or mandatory logins.",
    "key_features": [
        {
            "title": "Geometric Pattern Presets",
            "description": "Quickly switch between clean dots, architectural grids, and dynamic diagonal line textures."
        },
        {
            "title": "Real-Time Color & Scale Tweak",
            "description": "Interactively adjust tile proportions, stroke weights, and foreground/background hex colors."
        },
        {
            "title": "Frictionless Instant Export",
            "description": "Download clean, lightweight SVG tiles ready to embed into CSS background-image declarations."
        }
    ],
    "use_cases": [
        "Adding subtle decorative SVG mesh patterns to landing page hero sections",
        "Creating lightweight vector background tiles for dark-mode web applications",
        "Prototyping UI card textures without opening heavy graphic software like Figma"
    ],
    "pros": [
        "100% Free with zero registration or email sign-up required",
        "Generates ultra-lightweight vector SVG code with near-zero page weight impact",
        "Instant live preview reflects color and scaling tweaks in real-time"
    ],
    "cons": [
        "Focused specifically on repeating patterns rather than complex organic illustrations",
        "Closed-core web tool without an open-source self-hostable repository"
    ],
    "target_audience": "Frontend engineers, web designers, UI developers, and makers building modern websites.",
    "comparison_vs_alt": "Unlike heavy graphic suites or paywalled pattern libraries, Neatbo delivers an unbloated, single-purpose workflow to grab repeating SVG tiles in seconds.",
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
