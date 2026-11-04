# -*- coding: utf-8 -*-
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "pages", "vs", "[pair].astro")
content = open(path, "r", encoding="utf-8").read()

target = """    {
      "@type": "FAQPage",
      "@id": `${canonical}#faq`,
      "mainEntity": faqs.map(f => ({
        "@type": "Question",
        "name": f.q,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": f.a
        }
      }))
    }
  ]
};"""

replacement = """    {
      "@type": "FAQPage",
      "@id": `${canonical}#faq`,
      "mainEntity": faqs.map(f => ({
        "@type": "Question",
        "name": f.q,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": f.a
        }
      }))
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
          "name": "Comparisons",
          "item": "https://lordorange.top/vs"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": `${toolA.name} vs ${toolB.name}`,
          "item": canonical
        }
      ]
    }
  ]
};"""

assert target in content, "target not found in vs/[pair].astro"
content = content.replace(target, replacement)
open(path, "w", encoding="utf-8").write(content)
print("Successfully patched vs/[pair].astro with BreadcrumbList JSON-LD!")
