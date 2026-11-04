# -*- coding: utf-8 -*-
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "pages", "index.astro")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update searchIndex to include dateAdded and orderIndex
old_search_index = """const searchIndex = allTools.map(t => ({
  id: t.id,
  name: t.name,
  tagline: t.tagline,
  category: t.category,
  stars: t.stars || 0,
  signal: t.signal_score || 0,
  pricing: t.pricing_model || 'Free',
  source: t.source || 'github_trending',
  alt: t.primary_alternative || null,
  selfHost: !!t.is_self_hostable,
  noSignup: !!t.no_signup_required,
  tags: t.tags || [],
  url: t.url || '',
  github_url: t.github_url || '',
  iconUrl: getToolIcon(t.url, t.github_url),
  corpus: `${t.name} ${t.tagline} ${t.category} ${(t.tags || []).join(' ')} ${t.primary_alternative || ''}`.toLowerCase()
}));"""

new_search_index = """const searchIndex = allTools.map((t, index) => ({
  id: t.id,
  name: t.name,
  tagline: t.tagline,
  category: t.category,
  stars: t.stars || 0,
  signal: t.signal_score || 0,
  pricing: t.pricing_model || 'Free',
  source: t.source || 'github_trending',
  alt: t.primary_alternative || null,
  selfHost: !!t.is_self_hostable,
  noSignup: !!t.no_signup_required,
  tags: t.tags || [],
  url: t.url || '',
  github_url: t.github_url || '',
  iconUrl: getToolIcon(t.url, t.github_url),
  dateAdded: t.date_added || '',
  orderIndex: index,
  corpus: `${t.name} ${t.tagline} ${t.category} ${(t.tags || []).join(' ')} ${t.primary_alternative || ''}`.toLowerCase()
}));"""

assert old_search_index in content, "old_search_index not found"
content = content.replace(old_search_index, new_search_index)

# 2. Update select dropdown options
old_select = """          <select id="sort-select" class="sort-dropdown-select" aria-label="Sort tools">
            <option value="signal" selected>⚡ Highest Traction Score</option>
            <option value="stars">★ Most GitHub Stars</option>
            <option value="newest">🆕 Recently Added</option>
          </select>"""

new_select = """          <select id="sort-select" class="sort-dropdown-select" aria-label="Sort tools">
            <option value="newest" selected>🆕 Recently Added</option>
            <option value="signal">⚡ Highest Traction Score</option>
            <option value="stars">★ Most GitHub Stars</option>
          </select>"""

assert old_select in content, "old_select not found"
content = content.replace(old_select, new_select)

# 3. Update activeSort variable initialization
old_active_sort = "let activeSort = 'signal';"
new_active_sort = "let activeSort = 'newest';"
assert old_active_sort in content, "old_active_sort not found"
content = content.replace(old_active_sort, new_active_sort, 1)

# 4. Update applyFilters sorting logic
old_sort_logic = """    // Sorting
    if (activeSort === 'stars') {
      filteredTools.sort((a, b) => b.stars - a.stars);
    } else if (activeSort === 'signal') {
      filteredTools.sort((a, b) => b.signal - a.signal);
    }"""

new_sort_logic = """    // Sorting
    if (activeSort === 'stars') {
      filteredTools.sort((a, b) => (b.stars || 0) - (a.stars || 0));
    } else if (activeSort === 'signal') {
      filteredTools.sort((a, b) => (b.signal || 0) - (a.signal || 0));
    } else if (activeSort === 'newest') {
      filteredTools.sort((a, b) => {
        const dateA = a.dateAdded || '';
        const dateB = b.dateAdded || '';
        if (dateB !== dateA) {
          return dateB.localeCompare(dateA);
        }
        return (a.orderIndex || 0) - (b.orderIndex || 0);
      });
    }"""

assert old_sort_logic in content, "old_sort_logic not found"
content = content.replace(old_sort_logic, new_sort_logic)

# 5. Update reset filters button logic
old_reset = """      activeSort = 'signal';
      document.querySelectorAll('.category-pill-btn').forEach(b => b.classList.remove('active'));
      document.querySelector('.category-pill-btn[data-category="all"]')?.classList.add('active');
      document.querySelectorAll('.filter-toggle-chip').forEach(c => c.classList.remove('active'));
      document.querySelector('.filter-toggle-chip[data-filter="all"]')?.classList.add('active');
      if (sortSelect) sortSelect.value = 'signal';"""

new_reset = """      activeSort = 'newest';
      document.querySelectorAll('.category-pill-btn').forEach(b => b.classList.remove('active'));
      document.querySelector('.category-pill-btn[data-category="all"]')?.classList.add('active');
      document.querySelectorAll('.filter-toggle-chip').forEach(c => c.classList.remove('active'));
      document.querySelector('.filter-toggle-chip[data-filter="all"]')?.classList.add('active');
      if (sortSelect) sortSelect.value = 'newest';"""

assert old_reset in content, "old_reset not found"
content = content.replace(old_reset, new_reset)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated index.astro default sorting to 'Recently Added' (newest)!")
