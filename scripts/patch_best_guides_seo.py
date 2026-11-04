# -*- coding: utf-8 -*-
import os

# 1. Patch best/[slug].astro
best_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "pages", "best", "[slug].astro")
best_content = open(best_path, "r", encoding="utf-8").read()

target_best = """    {
      "@type": "FAQPage",
      "@id": `${canonical}#faq`,
      "mainEntity": topic.faqs.map(f => ({
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

replacement_best = """    {
      "@type": "FAQPage",
      "@id": `${canonical}#faq`,
      "mainEntity": topic.faqs.map(f => ({
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
          "name": "Best Tools",
          "item": "https://lordorange.top/best"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": topic.title,
          "item": canonical
        }
      ]
    }
  ]
};"""

assert target_best in best_content, "target_best not found"
best_content = best_content.replace(target_best, replacement_best)
open(best_path, "w", encoding="utf-8").write(best_content)

# 2. Patch guides/[slug].astro
guide_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "pages", "guides", "[slug].astro")
guide_content = open(guide_path, "r", encoding="utf-8").read()

target_guide = """const jsonLd = {
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": guide.title,
  "description": guide.description,
  "datePublished": guide.publishedAt,
  "dateModified": guide.updatedAt,
  "author": {
    "@type": "Person",
    "name": guide.author.name,
    "jobTitle": guide.author.role
  },
  "publisher": {
    "@type": "Organization",
    "name": "ToolsRadar",
    "url": "https://lordorange.top",
    "logo": "https://lordorange.top/favicon.svg"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": `https://lordorange.top/guides/${guide.slug}`
  }
};"""

replacement_guide = """const jsonLd = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "TechArticle",
      "headline": guide.title,
      "description": guide.description,
      "datePublished": guide.publishedAt,
      "dateModified": guide.updatedAt,
      "author": {
        "@type": "Person",
        "name": guide.author.name,
        "jobTitle": guide.author.role
      },
      "publisher": {
        "@type": "Organization",
        "name": "ToolsRadar",
        "url": "https://lordorange.top",
        "logo": "https://lordorange.top/favicon.svg"
      },
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": `https://lordorange.top/guides/${guide.slug}`
      }
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
          "name": "Guides",
          "item": "https://lordorange.top/guides"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": guide.title,
          "item": `https://lordorange.top/guides/${guide.slug}`
        }
      ]
    }
  ]
};"""

assert target_guide in guide_content, "target_guide not found"
guide_content = guide_content.replace(target_guide, replacement_guide)
open(guide_path, "w", encoding="utf-8").write(guide_content)

print("Successfully patched best/[slug].astro and guides/[slug].astro with BreadcrumbList JSON-LD!")
