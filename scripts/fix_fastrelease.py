import json
import os
import datetime

def update_fastrelease_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    all_tools_file = os.path.join(base_dir, "data", "all_tools.json")
    daily_file = os.path.join(base_dir, "data", "tools", "2026-10-27.json")

    # Update in all_tools.json
    with open(all_tools_file, "r", encoding="utf-8") as f:
        all_tools = json.load(f)

    for tool in all_tools:
        if tool["id"] == "fastrelease":
            tool["starting_price"] = "199"
            tool["key_features"] = [
                {
                    "title": "Built-in Stripe & Tiered Billing",
                    "description": "Pre-configured checkout flows, recurring subscriptions, and webhook handlers out of the box."
                },
                {
                    "title": "Docker & Multi-Tenant Architecture",
                    "description": "Full containerized environment with data isolation across organizations and teams using PostgreSQL."
                },
                {
                    "title": "Commercial Source Code License",
                    "description": "Access to commercial source code under license terms for self-hosted deployment on your own infrastructure."
                }
            ]
            tool["pros"] = [
                "Single-project perpetual license option ($199) or annual unlimited-project tiers ($249/yr, $299/yr)",
                "Comprehensive multi-tenancy and Dockerized setup ready for production VPS deployments",
                "Clean Node.js architecture with mature PostgreSQL backing and Stripe billing"
            ]
            tool["cons"] = [
                "Commercial licensed codebase (no free tier or trial license; unlimited projects require active annual license)",
                "Requires Node.js and Docker server operational familiarity"
            ]
            tool["summary"] = "Fastrelease is a commercial Node.js codebase engineered for developers building self-hosted, multi-tenant SaaS web applications. It packages user authentication, multi-tenant workspace isolation, Stripe subscription billing, PostgreSQL persistence, and Docker orchestration into a unified architecture, eliminating months of boilerplate infrastructure setup."

    with open(all_tools_file, "w", encoding="utf-8") as f:
        json.dump(all_tools, f, indent=2, ensure_ascii=False)
    print("Updated fastrelease in all_tools.json")

    # Update in daily_file
    if os.path.exists(daily_file):
        with open(daily_file, "r", encoding="utf-8") as f:
            daily_tools = json.load(f)
        for tool in daily_tools:
            if tool["id"] == "fastrelease":
                tool["starting_price"] = "199"
                tool["key_features"] = [
                    {
                        "title": "Built-in Stripe & Tiered Billing",
                        "description": "Pre-configured checkout flows, recurring subscriptions, and webhook handlers out of the box."
                    },
                    {
                        "title": "Docker & Multi-Tenant Architecture",
                        "description": "Full containerized environment with data isolation across organizations and teams using PostgreSQL."
                    },
                    {
                        "title": "Commercial Source Code License",
                        "description": "Access to commercial source code under license terms for self-hosted deployment on your own infrastructure."
                    }
                ]
                tool["pros"] = [
                    "Single-project perpetual license option ($199) or annual unlimited-project tiers ($249/yr, $299/yr)",
                    "Comprehensive multi-tenancy and Dockerized setup ready for production VPS deployments",
                    "Clean Node.js architecture with mature PostgreSQL backing and Stripe billing"
                ]
                tool["cons"] = [
                    "Commercial licensed codebase (no free tier or trial license; unlimited projects require active annual license)",
                    "Requires Node.js and Docker server operational familiarity"
                ]
                tool["summary"] = "Fastrelease is a commercial Node.js codebase engineered for developers building self-hosted, multi-tenant SaaS web applications. It packages user authentication, multi-tenant workspace isolation, Stripe subscription billing, PostgreSQL persistence, and Docker orchestration into a unified architecture, eliminating months of boilerplate infrastructure setup."
        with open(daily_file, "w", encoding="utf-8") as f:
            json.dump(daily_tools, f, indent=2, ensure_ascii=False)
        print("Updated fastrelease in 2026-10-27.json")

def update_slug_astro():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    slug_file = os.path.join(base_dir, "site", "src", "pages", "tool", "[slug].astro")
    with open(slug_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update jsonLd price
    old_jsonld = """const jsonLd = {
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": tool.name,
  "description": tool.summary,
  "applicationCategory": categoryInfo.name,
  "operatingSystem": "All",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  },
  "url": tool.url
};"""

    new_jsonld = """const priceValue = (tool.pricing_model === 'Paid' || tool.pricing_model === 'Usage-based')
  ? (tool.starting_price || (tool.id === 'fastrelease' ? '199' : '1'))
  : '0';

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": tool.name,
  "description": tool.summary,
  "applicationCategory": categoryInfo.name,
  "operatingSystem": "All",
  "offers": {
    "@type": "Offer",
    "price": priceValue,
    "priceCurrency": "USD"
  },
  "url": tool.url
};"""

    if old_jsonld in content:
        content = content.replace(old_jsonld, new_jsonld)
        print("Replaced jsonLd")
    else:
        print("WARN: old_jsonld not found")

    # 2. Update Hands-on Benchmark pill
    old_pill = """<span>🔬 Hands-on Benchmark</span>"""
    new_pill = """<span>📋 Editorial Architecture Analysis</span>"""
    if old_pill in content:
        content = content.replace(old_pill, new_pill)
        print("Replaced Hands-on Benchmark pill")

    # 3. Update Metric 3 traction subtext
    old_metric3 = """{tool.signal_score >= 80 ? "High ecosystem traction with frequent community releases." : "Steady release pace and active maintenance."}"""
    new_metric3 = """{tool.pricing_model === 'Open Source' ? (tool.signal_score >= 80 ? "High open-source community velocity and active releases." : "Steady release pace and active maintenance.") : "Active project maintenance and verified public documentation."}"""
    if old_metric3 in content:
        content = content.replace(old_metric3, new_metric3)
        print("Replaced metric 3 subtext")

    # 4. Update Metric 4 cost subtext
    old_metric4 = """{tool.pricing_model === 'Open Source' ? "Zero licensing fees with unlimited self-hosting capabilities." : "Accessible free usage tier without mandatory subscription."}"""
    new_metric4 = """{tool.pricing_model === 'Open Source' ? "Zero licensing fees with unlimited self-hosting capabilities." : (tool.pricing_model === 'Paid' ? "Commercial software licensing terms for project-based deployments." : (tool.pricing_model === 'Usage-based' ? "Usage-based consumption billing based on actual API/job volume." : "Accessible free usage tier without mandatory subscription."))}"""
    if old_metric4 in content:
        content = content.replace(old_metric4, new_metric4)
        print("Replaced metric 4 subtext")

    # 5. Update timestamp
    timestamp_file = os.path.join(base_dir, "site", "src", "data-timestamp.json")
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(timestamp_file, "w", encoding="utf-8") as f:
        json.dump({"updated_at": now_iso}, f, indent=2)

    with open(slug_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Saved updated [slug].astro")

if __name__ == "__main__":
    update_fastrelease_data()
    update_slug_astro()
