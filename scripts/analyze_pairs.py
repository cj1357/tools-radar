import json
import re

tools = json.load(open("data/all_tools.json", encoding="utf-8"))
tools_by_id = {t["id"]: t for t in tools}
tools_by_name = {t["name"].lower(): t for t in tools}

pairs = []
seen_slugs = set()

for t in tools:
    alt = t.get("primary_alternative")
    if not alt or len(alt.strip()) < 2:
        continue
    comp = t.get("comparison_vs_alt", "")
    alt_clean = alt.strip()
    alt_slug = re.sub(r"[^a-z0-9]+", "-", alt_clean.lower()).strip("-")
    tool_slug = t["id"]
    if not alt_slug or tool_slug == alt_slug:
        continue
    pair_slug = f"{tool_slug}-vs-{alt_slug}"
    if pair_slug in seen_slugs:
        continue
    seen_slugs.add(pair_slug)
    
    internal_b = tools_by_id.get(alt_slug) or tools_by_name.get(alt_clean.lower())
    pairs.append({
        "pair_slug": pair_slug,
        "tool_a_id": tool_slug,
        "tool_a_name": t["name"],
        "tool_b_name": alt_clean,
        "tool_b_is_internal": internal_b is not None,
        "tool_b_id": internal_b["id"] if internal_b else None,
        "category": t.get("category", "developer-tools"),
        "has_comp_text": len(comp) > 20
    })

print(f"Total valid pairs: {len(pairs)}")
print(f"Pairs with rich comparison text: {sum(1 for p in pairs if p['has_comp_text'])}")
print(f"Pairs where both tools are in directory: {sum(1 for p in pairs if p['tool_b_is_internal'])}")
print("\nTop 15 High-Signal Pairs:")
for p in pairs[:15]:
    status = "both-in-db" if p["tool_b_is_internal"] else "db-vs-market-leader"
    print(f"  /vs/{p['pair_slug']} -> {p['tool_a_name']} vs {p['tool_b_name']} ({status})")
