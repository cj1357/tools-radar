# -*- coding: utf-8 -*-
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "src", "layouts", "Layout.astro")
content = open(path, "r", encoding="utf-8").read()

old_head = """interface Props {
  title: string;
  description: string;
  canonicalUrl?: string;
  jsonLd?: Record<string, any>;
}

const { title, description, canonicalUrl, jsonLd } = Astro.props;
const siteName = "ToolsRadar";
const fullTitle = title.includes(siteName) ? title : `${title} | ${siteName}`;
const gaId = import.meta.env.PUBLIC_GA_ID || "G-FZ1SQCCJTE";"""

new_head = """interface Props {
  title: string;
  description: string;
  canonicalUrl?: string;
  jsonLd?: Record<string, any>;
  image?: string;
}

const { title, description, canonicalUrl, jsonLd, image } = Astro.props;
const siteName = "ToolsRadar";
const fullTitle = title.includes(siteName) ? title : `${title} | ${siteName}`;
const gaId = import.meta.env.PUBLIC_GA_ID || "G-FZ1SQCCJTE";
const resolvedImage = image 
  ? (image.startsWith('http') ? image : `https://lordorange.top${image.startsWith('/') ? '' : '/'}${image}`)
  : "https://lordorange.top/og-default.png";"""

assert old_head in content, "old_head not found"
content = content.replace(old_head, new_head)

old_meta = """    <!-- Open Graph -->
    <meta property="og:type" content="website" />
    <meta property="og:title" content={fullTitle} />
    <meta property="og:description" content={description} />
    <meta property="og:site_name" content={siteName} />

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content={fullTitle} />
    <meta name="twitter:description" content={description} />"""

new_meta = """    <!-- Open Graph -->
    <meta property="og:type" content="website" />
    <meta property="og:title" content={fullTitle} />
    <meta property="og:description" content={description} />
    <meta property="og:site_name" content={siteName} />
    <meta property="og:image" content={resolvedImage} />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content={fullTitle} />

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content={fullTitle} />
    <meta name="twitter:description" content={description} />
    <meta name="twitter:image" content={resolvedImage} />
    <meta name="twitter:image:alt" content={fullTitle} />"""

assert old_meta in content, "old_meta not found"
content = content.replace(old_meta, new_meta)

open(path, "w", encoding="utf-8").write(content)
print("Successfully patched Layout.astro with OpenGraph & Twitter Card images!")
