# -*- coding: utf-8 -*-
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "pages", "category", "[category].astro")
content = open(path, "r", encoding="utf-8").read()

target = """const { category } = Astro.props;
const categoryTools = allTools.filter(t => t.category === category.id);
---

<Layout 
  title={`Best ${category.name} in 2026: Curated Directory & Reviews`}
  description={`Browse the top curated list of ${category.name}. Discover free, open source, and innovative tools updated daily on ToolsRadar.`}
  canonicalUrl={`https://lordorange.top/category/${category.id}`}
>"""

replacement = """const { category } = Astro.props;
const categoryTools = allTools.filter(t => t.category === category.id);

const jsonLd = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "CollectionPage",
      "name": `Top ${category.name} Developer Tools & Software (2026)`,
      "description": category.description,
      "url": `https://lordorange.top/category/${category.id}`
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://lordorange.top"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Categories",
          "item": "https://lordorange.top/#radar-feed"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": category.name,
          "item": `https://lordorange.top/category/${category.id}`
        }
      ]
    }
  ]
};
---

<Layout 
  title={`Best ${category.name} in 2026: Curated Directory & Reviews`}
  description={`Browse the top curated list of ${category.name}. Discover free, open source, and innovative tools updated daily on ToolsRadar.`}
  canonicalUrl={`https://lordorange.top/category/${category.id}`}
  jsonLd={jsonLd}
>"""

assert target in content, "target not found in category/[category].astro"
content = content.replace(target, replacement)
open(path, "w", encoding="utf-8").write(content)
print("Successfully patched category/[category].astro with BreadcrumbList JSON-LD!")
