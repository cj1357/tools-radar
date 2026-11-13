# -*- coding: utf-8 -*-
"""
Remove SkillPi backlink from global footer in Layout.astro and set featured=False in all_tools.json.
Reason: Counter-measure against non-reciprocal outreach link building.
"""

import os
import json

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
layout_path = os.path.join(root_dir, "site", "src", "layouts", "Layout.astro")
tools_path = os.path.join(root_dir, "data", "all_tools.json")

# 1. Update Layout.astro
with open(layout_path, "r", encoding="utf-8") as f:
    layout = f.read()

lines = layout.splitlines(keepends=True)
new_lines = []
removed = False
for line in lines:
    if "skillpi.com" in line:
        removed = True
        continue
    new_lines.append(line)

if removed:
    with open(layout_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("SkillPi removed from Layout.astro successfully.")
else:
    print("Warning: skillpi.com line not found in Layout.astro.")

# 2. Update all_tools.json
with open(tools_path, "r", encoding="utf-8") as f:
    tools = json.load(f)

updated = False
for t in tools:
    if t.get("id") == "skillpi":
        t["featured"] = False
        t["signal_score"] = 72  # Lower signal score
        updated = True
        break

if updated:
    with open(tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print("SkillPi featured set to False and signal score lowered in all_tools.json.")
else:
    print("Warning: SkillPi not found in all_tools.json.")
