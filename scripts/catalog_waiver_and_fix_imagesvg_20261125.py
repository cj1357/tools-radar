# -*- coding: utf-8 -*-
"""
1. Update ImageSVG with official concise directory profile & remove unverified technical claims.
2. Catalog Waiver.com with verified facts from official submission, pricing, and walkthrough docs.
"""

import json
import os

BASE_DIR = r"d:\_projectsTYweb\tools-radar"
all_tools_file = os.path.join(BASE_DIR, "data", "all_tools.json")
editorial_file = os.path.join(BASE_DIR, "data", "editorial_reviews.json")

IMAGESVG_TOOL_UPDATE = {
    "name": "ImageSVG",
    "tagline": "Online raster-to-SVG converter for logos, icons, and illustrations",
    "summary": "ImageSVG is an online raster-to-SVG converter for logos, icons, and illustrations. It focuses on high-quality vector results and offers a daily free allowance. Please visit https://imagesvg.com/en/ for current supported formats, features, and pricing.",
    "url": "https://imagesvg.com/en/",
    "github_url": "",
    "source": "submission",
    "category": "design-ui",
    "tags": [
        "SVG",
        "Raster to Vector",
        "Design Tools",
        "Logos",
        "Icons",
        "Illustrations"
    ],
    "pricing_model": "Freemium",
    "stars": 0,
    "primary_alternative": "",
    "is_self_hostable": False,
    "no_signup_required": False,
    "signal_score": 82,
    "verdict": "",
    "deployment_format": "Online Web Application",
    "extensibility": "",
    "install_command": "",
    "featured": False,
    "concise_profile": True,
    "key_features": [],
    "use_cases": [],
    "pros": [],
    "cons": [],
    "target_audience": "Designers, developers, and users seeking an online raster-to-SVG converter for logos, icons, and illustrations.",
    "comparison_vs_alt": "",
    "faqs": []
}

WAIVER_COM_TOOL = {
    "id": "waiver-com",
    "name": "Waiver.com",
    "tagline": "Digital waiver drafting, guest link and QR signing, and front-desk check-in lookup software",
    "summary": "Waiver.com is a hosted digital waiver platform designed for activity venues, gyms, fitness studios, camps, and rental operations to manage guest releases from initial drafting through lobby check-in. Every subscription tier includes unlimited waivers, templates, staff access, storage, and AI-assisted drafting for editable activity and form sections—while keeping approved legal release text strictly separated for human review. Guests can sign ahead of arrival via links and SMS invitations or on-site via QR codes and kiosks, and staff can search signed adult or guardian records instantaneously at check-in.",
    "url": "https://www.waiver.com",
    "github_url": "",
    "source": "submission",
    "category": "productivity",
    "tags": [
        "Digital Waivers",
        "Forms",
        "QR Check-in",
        "AI Drafting",
        "Productivity",
        "Workflow",
        "Venue Management"
    ],
    "pricing_model": "Paid",
    "starting_price": "9",
    "stars": 0,
    "primary_alternative": "",
    "is_self_hostable": False,
    "no_signup_required": False,
    "signal_score": 86,
    "verdict": "A focused, operations-first digital waiver platform that pairs unlimited waiver volume at $9/month with disciplined AI-drafting guardrails—isolating generated activity sections from reviewed legal agreements.",
    "deployment_format": "Cloud Web Application",
    "extensibility": "CSV & PDF Exports, Multi-Location Workspaces, API & Webhooks",
    "install_command": "",
    "architecture_note": "Delivered as a hosted web application with browser-based form building, mobile link/QR/kiosk signing, SMS invitations, CSV/PDF record exports, and documented API and webhook endpoints for connecting existing venue systems.",
    "date_added": "2026-11-25",
    "featured": False,
    "key_features": [
        {
            "title": "Editable AI-Assisted Waiver Sections",
            "description": "Generates structured, editable activity descriptions and intake sections for adult or family audiences while keeping organization-approved agreement wording in a dedicated field."
        },
        {
            "title": "Link, SMS & On-Site QR/Kiosk Signing",
            "description": "Supports pre-arrival signing via web links or monthly SMS allowances as well as on-site QR code and lobby kiosk flows across multiple signing languages."
        },
        {
            "title": "Participant & Guardian Check-In Lookup",
            "description": "Front-desk search resolves signed records by participant, child, guardian name, or booking, supporting fresh per-booking signatures for repeat visits."
        },
        {
            "title": "Photos, ID Capture, Exports & APIs",
            "description": "Attaches photo or ID captures directly to signed documents, manages multiple venue locations consistently, exports CSV/PDF archives, and integrates via APIs and webhooks."
        }
    ],
    "use_cases": [
        "Climbing gyms, trampoline parks, outfitters, and equipment rental venues speeding up busy lobby check-ins via pre-arrival links and QR kiosks.",
        "Fitness studios, martial arts programs, and youth camps collecting structured guardian/minor waivers and verifying child records at arrival.",
        "Multi-location recreational operators managing version-controlled waiver templates, PDF/Word imports, and per-booking repeat-visit signatures."
    ],
    "pros": [
        "Unlimited waivers, templates, staff accounts, devices, and record storage on every plan (Starter from $9/month, Growth $14/month)",
        "Pragmatic AI-drafting workflow explicitly refuses to invent legal releases or silently overwrite signed template versions",
        "Built-in minor/guardian grouping, photo/ID capture, multi-location consistency, and CSV/PDF exports",
        "Free manual import service offered for teams migrating historical waivers from PDF or Word files"
    ],
    "cons": [
        "No permanent free tier (every plan begins with a 7-day trial requiring a credit card upfront)",
        "AI drafting produces activity and form structure drafts only; organizations must still supply and review approved legal terms"
    ],
    "target_audience": "Climbing gyms, trampoline parks, ranches and outfitters, tours, fitness and martial arts studios, camps, spas, and equipment rental businesses.",
    "comparison_vs_alt": "",
    "faqs": [
        {
            "q": "How does Waiver.com pricing work?",
            "a": "Waiver.com offers a 7-day free trial (credit card required). Starter is $9/month for 1 location and 200 monthly SMS messages; Growth is $14/month for unlimited locations and 500 monthly SMS messages (extra SMS are $0.02 each; annual plans include 2 months free). Both include unlimited waivers, templates, staff, and AI drafting."
        },
        {
            "q": "Does Waiver.com AI automatically generate legally binding agreements?",
            "a": "No. Per Waiver.com's documentation, the AI assistant drafts activity explanations and intake form sections for review in the builder, and is designed not to write releases, indemnities, arbitration clauses, or legal conclusions. Venues place their approved legal wording separately and review drafts before publishing."
        },
        {
            "q": "Can staff find guardian-signed minor waivers and handle repeat visits?",
            "a": "Yes. Family forms keep guardians and children grouped together, and front-desk search retrieves records by participant name, guardian, or booking. Venues can also collect per-booking signatures when guests return for additional activities."
        },
        {
            "q": "Can we bring existing PDF or Word waivers into Waiver.com?",
            "a": "Yes. Teams can import PDF or Word waivers (with optional free manual setup assistance from Waiver.com), and imported historical waivers count for validity without adding to billing."
        }
    ]
}

WAIVER_COM_REVIEW = {
    "article_title": "Waiver.com Operational Dossier: Human-Reviewed AI Waiver Drafting, QR Check-In, and Unlimited-Volume Venue Economics",
    "reading_time": "5 min read",
    "editorial_verdict_callout": "Waiver.com avoids common AI hype by scoping its drafting tool strictly to activity briefs and form structure—delivering unlimited waivers from $9/month alongside fast guardian search at check-in.",
    "chapters": [
        {
            "id": "front-desk-arrival-and-waiver-bottlenecks",
            "number": "01",
            "title": "The Front-Desk Arrival Bottleneck: Minor Grouping, Repeat Bookings, and Paper Overhead",
            "content": "For high-throughput recreational businesses—such as climbing gyms, trampoline parks, martial arts academies, tours, and equipment rental counters—guest check-in friction routinely backs up the lobby. Managing paper waivers or fragmented PDF attachments breaks down quickly when parents arrive with multiple children, when booking rules require a fresh per-booking signature on repeat visits, or when reception staff must verify guardian authorization in seconds. Waiver.com streamlines this operational pipeline into a unified hosted workflow: guests receive links or SMS invitations ahead of arrival (or scan QR codes and kiosks on-site), complete structured adult or family forms, optionally provide photo or ID capture attachments, and become immediately searchable by participant or guardian name at check-in."
        },
        {
            "id": "human-in-the-loop-ai-drafting-and-versioning",
            "number": "02",
            "title": "Disciplined Workflow Architecture: AI Section Drafting vs. Approved Release Control",
            "content": "Unlike generic form builders that treat AI text generation as a black-box legal replacement, Waiver.com documents strict engineering boundaries around its drafting assistant. As outlined in its pre-publication review guide, the AI generator is built to organize activity explanations and intake questions for adult or family audiences without generating legal releases, indemnities, arbitration clauses, or enforceability claims. Approved organizational agreement copy resides in a distinct field in the waiver builder so reviewers can audit edits cleanly without rewriting legal obligations. Crucially, publishing updates creates a controlled template version rather than silently mutating historical agreements attached to already-signed guest records."
        },
        {
            "id": "unit-economics-unlimited-waivers-and-sms",
            "number": "03",
            "title": "Unit Economics: Predictable Flat Pricing vs. Per-Waiver Tax Models",
            "content": "Many digital signature and venue SaaS platforms penalize seasonal peaks with per-envelope charges or restrictive document caps. Waiver.com structures pricing around locations and messaging allowances rather than document volume: both the Starter tier ($9/month for one location, 200 SMS) and the Growth tier ($14/month for unlimited locations, 500 SMS) include unlimited waivers, templates, devices, staff seats, and storage—with overage texts billed transparently at $0.02 per message and annual billing waiving two months. Moreover, AI drafting is included across every tier with no paid AI add-on, and businesses switching from legacy paper or PDF files can request free manual setup assistance without imported records counting toward quotas."
        },
        {
            "id": "operational-verdict-and-venue-suitability",
            "number": "04",
            "title": "Operational Suitability Verdict: Pragmatic Venue Operations Without Bloated Upcharge",
            "content": "From a practical standpoint, Waiver.com fits businesses that prioritize fast lobby check-in, clean minor-guardian linking, multi-location template consistency, and straightforward CSV/PDF exports or API/webhook connectivity. Prospective teams should note two clear boundaries: plans begin with a 7-day trial requiring a credit card upfront (with no permanent free plan), and AI drafting serves solely as a structured brief-to-form helper rather than a substitute for counsel-approved release wording. Within those honest parameters, Waiver.com delivers high operational value at an accessible price point."
        }
    ],
    "tool_id": "waiver-com",
    "model_used": "editorial-team",
    "generated_at": "2026-11-25T11:50:00.000000+00:00"
}

def run():
    with open(all_tools_file, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # 1. Update ImageSVG cleanly
    img_updated = False
    for idx, t in enumerate(tools):
        if t.get("id") == "imagesvg":
            t_new = dict(t)
            t_new.update(IMAGESVG_TOOL_UPDATE)
            tools[idx] = t_new
            img_updated = True
            break
    print(f"ImageSVG updated in all_tools.json: {img_updated}")

    # 2. Insert Waiver.com
    tools = [t for t in tools if t.get("id") != "waiver-com"]
    tools.insert(0, WAIVER_COM_TOOL)

    with open(all_tools_file, "w", encoding="utf-8") as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: all_tools.json saved with {len(tools)} tools.")

    # 3. Update editorial_reviews.json
    with open(editorial_file, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    removed_img_rev = reviews.pop("imagesvg", None) is not None
    print(f"Removed long-form editorial review for imagesvg: {removed_img_rev}")

    reviews["waiver-com"] = WAIVER_COM_REVIEW
    with open(editorial_file, "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: editorial_reviews.json saved with {len(reviews)} reviews.")

if __name__ == "__main__":
    run()
