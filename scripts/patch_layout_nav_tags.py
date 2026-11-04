# -*- coding: utf-8 -*-
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "layouts", "Layout.astro")
content = open(path, "r", encoding="utf-8").read()

# 1. Desktop Nav
old_nav = """        <ul class="nav-desktop-links">
          <li><a href="/">Radar</a></li>
          <li><a href="/guides">Guides</a></li>
          <li><a href="/vs">Comparisons</a></li>
          <li><a href="/best">Best Lists</a></li>
          <li><a href="/category/ai-agents">AI Agents</a></li>"""

new_nav = """        <ul class="nav-desktop-links">
          <li><a href="/">Radar</a></li>
          <li><a href="/guides">Guides</a></li>
          <li><a href="/vs">Comparisons</a></li>
          <li><a href="/best">Best Lists</a></li>
          <li><a href="/tag">Tags</a></li>
          <li><a href="/category/ai-agents">AI Agents</a></li>"""

if old_nav in content:
    content = content.replace(old_nav, new_nav)

# 2. Mobile Nav
old_mobile = """        <a href="/vs" class="mobile-nav-item" style="color: #38bdf8; font-weight: 600;">⚡ Head-to-Head Comparisons</a>
        <a href="/best" class="mobile-nav-item" style="color: #facc15; font-weight: 600;">🏆 Best Software Rankings</a>
        <a href="/guides" class="mobile-nav-item" style="color: #c084fc; font-weight: 600;">📚 Technical Guides</a>"""

new_mobile = """        <a href="/vs" class="mobile-nav-item" style="color: #38bdf8; font-weight: 600;">⚡ Head-to-Head Comparisons</a>
        <a href="/best" class="mobile-nav-item" style="color: #facc15; font-weight: 600;">🏆 Best Software Rankings</a>
        <a href="/guides" class="mobile-nav-item" style="color: #c084fc; font-weight: 600;">📚 Technical Guides</a>
        <a href="/tag" class="mobile-nav-item" style="color: #38bdf8; font-weight: 600;">🏷️ Tags & Taxonomy Directory</a>"""

assert old_mobile in content, "old_mobile not found"
content = content.replace(old_mobile, new_mobile)

# 3. Footer Links
old_footer = """              <li><a href="/">All Tools Feed</a></li>
              <li><a href="/category/ai-agents">AI Agents & Workflows</a></li>
              <li><a href="/category/developer-tools">DevTools & CLI</a></li>
              <li><a href="/category/open-source">Open Source Alternatives</a></li>
              <li><a href="/submit">+ Submit a Tool</a></li>"""

new_footer = """              <li><a href="/">All Tools Feed</a></li>
              <li><a href="/tag">Tags & Taxonomy Directory</a></li>
              <li><a href="/category/ai-agents">AI Agents & Workflows</a></li>
              <li><a href="/category/developer-tools">DevTools & CLI</a></li>
              <li><a href="/category/open-source">Open Source Alternatives</a></li>
              <li><a href="/submit">+ Submit a Tool</a></li>"""

assert old_footer in content, "old_footer not found"
content = content.replace(old_footer, new_footer)

open(path, "w", encoding="utf-8").write(content)
print("Successfully added Tags link to navigation and footer!")
