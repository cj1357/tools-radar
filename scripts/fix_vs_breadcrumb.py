# -*- coding: utf-8 -*-
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "pages", "vs", "[pair].astro")
lines = open(path, "r", encoding="utf-8").readlines()

found = False
for i, line in enumerate(lines):
    if "vs ${toolB.name}" in line:
        print(f"Replacing at line {i+1}: {line.strip()}")
        lines[i] = '          "name": `${toolA.name} vs ${toolBName}`,\n'
        found = True

assert found, "Target line with toolB.name not found"
open(path, "w", encoding="utf-8").writelines(lines)
print("Successfully fixed toolBName in vs/[pair].astro!")
