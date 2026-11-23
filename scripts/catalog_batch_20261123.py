# -*- coding: utf-8 -*-
"""
Catalog TinyCommand and ImageSVG into all_tools.json and editorial_reviews.json.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
all_tools_file = os.path.join(BASE_DIR, 'data', 'all_tools.json')
editorial_file = os.path.join(BASE_DIR, 'data', 'editorial_reviews.json')

TOOLS_TO_ADD = [
    {
        "id": "tinycommand",
        "name": "TinyCommand",
        "tagline": "All-in-one forms, tables, visual workflows, and custom AI agents for agile teams",
        "summary": "TinyCommand is a unified low-code automation and operational workbench that consolidates dynamic form collection, relational data tables, visual workflow pipelines, and custom AI agents into a single managed platform. Designed as a lean, all-in-one alternative to fragmented SaaS stacks (such as juggling Airtable, Typeform, and Zapier), TinyCommand allows small teams and developers to capture data, trigger multi-step integration sequences with embedded AI intelligence steps, and deploy autonomous agents without writing boilerplate orchestration code. The platform offers a free-forever tier with 1,000 monthly execution credits alongside transparent usage-based scaling for custom agent execution.",
        "url": "https://tinycommand.com/",
        "github_url": "",
        "source": "submission",
        "category": "ai-tools",
        "tags": [
            "AI Agents",
            "Automation",
            "Workflow",
            "No-Code",
            "Forms",
            "Tables",
            "Productivity"
        ],
        "pricing_model": "Freemium",
        "stars": 0,
        "primary_alternative": "Zapier",
        "is_self_hostable": False,
        "no_signup_required": False,
        "signal_score": 86,
        "verdict": "A cohesive, low-code operational engine uniting forms, relational tables, and AI-augmented automation pipelines into an accessible, unified interface for modern businesses.",
        "deployment_format": "Managed Cloud SaaS",
        "extensibility": "Visual Workflow Canvas, REST Integrations & MCP Protocol Support",
        "install_command": "Access free tier and documentation at https://tinycommand.com/docs",
        "date_added": "2026-11-23",
        "featured": False,
        "key_features": [
            {
                "title": "Unified Forms & Relational Tables",
                "description": "Build branded intake forms and route structured responses directly into connected relational database tables with zero manual export friction."
            },
            {
                "title": "Visual Workflow Engine with AI Steps",
                "description": "Connect multi-app logic and execution triggers with native generative AI steps embedded directly within workflow pipelines across all tiers."
            },
            {
                "title": "Custom Autonomous AI Agents",
                "description": "Deploy dedicated conversational and task-oriented agents configured with team context, knowledge bases, and actionable tooling on Professional plans."
            },
            {
                "title": "Generous Public Free Tier",
                "description": "Get started immediately with 1,000 monthly execution credits and 1 seat under published transparent limits without requiring an upfront credit card."
            }
        ],
        "use_cases": [
            "Small product and marketing teams building end-to-end customer onboarding funnels, automated data enrichment, and email response campaigns.",
            "Operations teams consolidating disparate subscriptions into a single manageable workspace for client intake, CRM tracking, and project triage.",
            "Indie founders automating recurring operational processes with customized AI agents handling document analysis and web scraping steps."
        ],
        "pros": [
            "Unifies data collection (forms), data management (tables), and execution (workflows/agents) into a single subscription",
            "Embedded AI processing steps are accessible across all workflow plans without complex external API gateway setup",
            "Permanent free tier offering 1,000 credits/month enables thorough evaluation before commercial scaling",
            "Clean, intuitive user experience designed to eliminate SaaS sprawl for agile teams"
        ],
        "cons": [
            "Proprietary hosted platform without self-hosted on-premise deployment or open-source core",
            "Building fully autonomous custom agents requires upgrading to the Professional plan tier"
        ],
        "target_audience": "Small business operators, startup founders, agile marketing teams, and developers seeking unified workflow automation.",
        "comparison_vs_alt": "While Zapier focuses strictly on point-to-point app integrations requiring third-party forms and databases, TinyCommand combines native intake forms, relational tables, and AI workflow steps into one tightly coupled workspace.",
        "faqs": [
            {
                "q": "What is TinyCommand and what problem does it solve?",
                "a": "TinyCommand is a multi-function automation platform combining forms, tables, workflows, and AI agents. It eliminates SaaS subscription fragmentation by providing an all-in-one environment where captured data automatically triggers AI-augmented actions."
            },
            {
                "q": "How does the pricing and free tier work?",
                "a": "TinyCommand provides a public free tier with 1,000 monthly credits and 1 seat under documented rate limits. Custom agent building and higher execution quotas start on the Professional plan, detailed transparently at https://tinycommand.com/pricing."
            },
            {
                "q": "Can I integrate AI steps into automated workflows?",
                "a": "Yes. TinyCommand natively embeds AI processing steps (such as text synthesis, content enrichment, and data extraction) directly inside visual workflow sequences across all plan tiers."
            },
            {
                "q": "Is TinyCommand available as an open-source or self-hosted tool?",
                "a": "No, TinyCommand is a proprietary managed cloud platform designed for zero-maintenance operation and rapid team onboarding."
            }
        ]
    },
    {
        "id": "imagesvg",
        "name": "ImageSVG",
        "tagline": "Precision raster-to-vector tracing engine converting logos, icons, and illustrations into editable SVG paths",
        "summary": "ImageSVG is an algorithmic vectorization and design utility tailored for frontend engineers, UI/UX designers, and digital artists. The platform transforms raster artwork—spanning PNG, JPG, WebP, GIF, and BMP formats up to 20 MB—into clean, scalable, and fully editable SVG vector paths. Utilizing specialized curve tracing algorithms optimized for different graphic modalities (including logos, app icons, digital stickers, and black-and-white line art), ImageSVG enables users to balance node density, inspect side-by-side zoom comparisons, and export production-ready vector assets directly to desktop illustration suites or web source trees. The platform provides a freemium model with daily free conversion allowances.",
        "url": "https://imagesvg.com/en/",
        "github_url": "",
        "source": "submission",
        "category": "design",
        "tags": [
            "SVG",
            "Vectorization",
            "Raster to Vector",
            "Design Tools",
            "Frontend",
            "Graphics",
            "Icons"
        ],
        "pricing_model": "Freemium",
        "stars": 0,
        "primary_alternative": "Vector Magic",
        "is_self_hostable": False,
        "no_signup_required": False,
        "signal_score": 85,
        "verdict": "A specialized, high-fidelity vector tracing utility that simplifies converting low-resolution raster imagery into clean, mathematically scalable SVG paths for modern web development.",
        "deployment_format": "Web Application & Developer Utility",
        "extensibility": "Web Vector Inspector, SVG Path Exports & MCP Connectivity",
        "install_command": "Try interactive conversions online at https://imagesvg.com/en/",
        "date_added": "2026-11-23",
        "featured": False,
        "key_features": [
            {
                "title": "Multi-Modal Vector Tracing Engines",
                "description": "Applies customized contour and Bézier fitting algorithms tailored specifically for icons, flat illustrations, photos, and high-contrast line art."
            },
            {
                "title": "Tunable Node Density & Curve Controls",
                "description": "Choose between balanced path fitting, simplified low-node silhouettes, or high-fidelity detailed paths to optimize file weight and render performance."
            },
            {
                "title": "Interactive Real-Time Vector Inspection",
                "description": "Directly compare original raster pixels against synthesized SVG vector paths with high-magnification split-view zooming before downloading."
            },
            {
                "title": "Wide Raster Format Ingestion",
                "description": "Accepts PNG, JPG, WebP, GIF, and BMP graphics up to 20 MB with immediate browser-side preview and downloadable vector assets."
            }
        ],
        "use_cases": [
            "Frontend developers converting legacy raster app icons and brand logos into responsive, infinite-resolution SVGs for web bundles.",
            "UI/UX designers restoring vector assets from low-resolution mockups, pitch deck screenshots, or legacy client exports.",
            "Digital crafters and graphic illustrators generating clean vector cutting paths (DXF/SVG) for laser cutters, plotters, and digital print."
        ],
        "pros": [
            "Specialized curve-fitting modes produce cleaner SVG code with fewer redundant control points than generic auto-trace tools",
            "High-magnification comparison viewer allows precision inspection of path alignment before export",
            "Free daily conversion allowance enables regular casual and staging-level design usage",
            "Supports large raster files up to 20 MB across modern formats including WebP"
        ],
        "cons": [
            "Continuous high-volume batch vectorization requires paid plan subscriptions",
            "Photographic conversions naturally produce complex, multi-layered vector meshes with larger SVG payloads"
        ],
        "target_audience": "Frontend engineers, graphic designers, UI/UX specialists, digital illustrators, and makers working with vector assets.",
        "comparison_vs_alt": "While legacy desktop tools like Vector Magic and Adobe Illustrator require heavyweight local software or steep licensing fees, ImageSVG provides instantaneous browser-based vector tracing with dedicated icon/logo optimization presets.",
        "faqs": [
            {
                "q": "What is ImageSVG and how does it convert raster images?",
                "a": "ImageSVG is an algorithmic vector conversion tool that traces raster graphics (PNG, JPG, WebP, BMP, GIF) into scalable SVG vector paths by calculating optimal Bézier curves and color boundaries."
            },
            {
                "q": "What image formats and file sizes are supported?",
                "a": "ImageSVG supports input files up to 20 MB across PNG, JPG, WebP, GIF, and BMP formats, outputting standard W3C-compliant SVG markup."
            },
            {
                "q": "How can I control the complexity and file size of the resulting SVG?",
                "a": "ImageSVG provides curve style presets: 'Balanced' for standard logos, 'Fewer nodes' for simplified shapes with minimal file size, and 'More detail' for intricate artwork requiring high point fidelity."
            },
            {
                "q": "Is ImageSVG free to use?",
                "a": "Yes, ImageSVG operates on a freemium model offering a daily free conversion allowance with a user account, alongside paid plans for high-volume conversion needs."
            }
        ]
    }
]

REVIEWS_TO_ADD = {
    "tinycommand": {
        "article_title": "TinyCommand Architecture & Workflow Dossier: Unified Data Intakes, Embedded AI Pipelines, and Low-Code Team Automation",
        "reading_time": "5 min read",
        "editorial_verdict_callout": "TinyCommand elegantly solves the SaaS tax of juggling separate form builders, spreadsheet databases, and automation tools—bundling them into a high-ergonomics engine with embedded AI capabilities.",
        "chapters": [
            {
                "id": "the-saas-sprawl-and-integration-friction",
                "number": "01",
                "title": "The SaaS Tax: Fragmentation Between Forms, Relational Databases, and Workflow Automation",
                "content": "For growing startups and agile operations teams, constructing routine business workflows has traditionally required knitting together multiple independent software-as-a-service (SaaS) products. A standard intake pipeline routinely involves Typeform for front-facing data capture, Zapier or Make for orchestrating webhook triggers, Airtable for maintaining tabular relational records, and SendGrid for transactional email dispatches. While each standalone platform is competent within its silo, this architectural sprawl imposes substantial recurring subscription expenses, introduces multiple authentication points of failure, and demands continuous maintenance of brittle webhook payload mappings. TinyCommand was engineered to eliminate this operational friction by unifying data intake forms, relational tables, visual execution graphs, and email campaigns into a coherent, low-code operational plane."
            },
            {
                "id": "unified-architecture-and-embedded-ai-execution",
                "number": "02",
                "title": "Unified Runtime Architecture: Native Tables, Visual Pipelines, and Embedded AI Ingestion",
                "content": "At the core of TinyCommand's system design is the seamless continuum between passive data storage and active workflow execution. Rather than treating databases and trigger webhooks as decoupled endpoints, TinyCommand integrates form definitions directly against table schemas. When a user submits an intake response, the data instantly populates relational records without intermediary sync delays. Furthermore, TinyCommand distinguishes itself by embedding artificial intelligence steps directly into visual workflow pipelines across all tiers. Workflow nodes can execute dynamic text generation, sentiment classification, lead qualification, and document data extraction without requiring developers to manage bespoke OpenAI API keys, token rate limits, or retry backoff queues. This immediate availability of AI logic dramatically shortens iteration cycles for automated triage."
            },
            {
                "id": "autonomous-agents-and-mcp-extensibility",
                "number": "03",
                "title": "From Linear Automations to Autonomous AI Agents: Professional Workflows and Extensibility",
                "content": "Beyond deterministic if-this-then-that automation sequences, TinyCommand provides higher-order agentic capabilities on its Professional tiers. Users can configure and deploy autonomous AI agents endowed with specific system instructions, persistent working memory, and tool invocation access. These agents can autonomously execute research tasks, perform targeted web scraping, and draft synthesized customer responses grounded in team knowledge bases. In alignment with modern open agent standards, TinyCommand is also architecting compatibility for the Model Context Protocol (MCP), enabling external AI assistants and client environments to interface with TinyCommand's underlying databases and workflows as standardized toolkits."
            },
            {
                "id": "production-verdict-and-operational-guidance",
                "number": "04",
                "title": "Production Readiness Verdict: TCO Optimization for Growing Teams vs. Enterprise Sprawl",
                "content": "In evaluating total operational utility, TinyCommand delivers compelling cost and efficiency advantages for small businesses, bootstrapped founders, and lean cross-functional teams. With a permanent free tier providing 1,000 monthly execution credits and single-seat access without credit card barriers, teams can rigorously prototype real-world automation funnels before committing budget. While large-scale global enterprises with rigid compliance controls may still require self-hosted on-premise engines, for the vast majority of digital businesses seeking to eliminate fragmented software bloat, TinyCommand represents an exceptionally balanced, highly productive modern automation engine."
            }
        ],
        "tool_id": "tinycommand",
        "model_used": "editorial-team",
        "generated_at": "2026-11-23T10:18:00.000000+00:00"
    },
    "imagesvg": {
        "article_title": "ImageSVG Architecture & Vectorization Dossier: Bézier Curve Fitting, Modality Optimization, and Modern Frontend Vector Assets",
        "reading_time": "5 min read",
        "editorial_verdict_callout": "ImageSVG bridges the gap between raster legacy graphics and scalable SVG production—giving frontend teams an intuitive, browser-based tracer with surgical control over node density.",
        "chapters": [
            {
                "id": "the-raster-vector-impedance-mismatch",
                "number": "01",
                "title": "The Raster-Vector Dilemma: Resolution Independence and Legacy Asset Debt",
                "content": "In modern responsive web development and high-density retina displays, raster image formats (such as JPEG, PNG, and WebP) suffer from inherent resolution constraints. When scaled across diverse viewports, raster graphics exhibit pixelation, artifact blurring, and inflated asset weight that degrades Core Web Vitals (specifically Largest Contentful Paint). Conversely, Scalable Vector Graphics (SVG) define visual paths through mathematical formulas, rendering with infinite clarity at minimal bandwidth footprint. However, engineering and design teams routinely inherit legacy raster brand marks, app icons, and client sketches without original vector master files. Re-drawing these assets manually inside vector design software is a tedious, labor-intensive chore. ImageSVG was developed to automate this conversion pipeline with deterministic algorithmic fidelity."
            },
            {
                "id": "contour-tracing-and-bezier-curve-optimization",
                "number": "02",
                "title": "Algorithmic Vectorization: Contour Tracing, Edge Detection, and Bézier Curve Fitting",
                "content": "The fundamental engineering challenge in automated vectorization lies in edge detection and path simplification. Naive auto-trace algorithms frequently generate chaotic zigzag polygon meshes with thousands of redundant anchor points, resulting in bloated SVG files that trigger high DOM rendering overhead. ImageSVG implements an advanced multi-pass contour tracing pipeline that detects color boundaries, filters optical raster noise, and fits continuous cubic and quadratic Bézier curves against pixel gradients. By calculating optimal curve tangents rather than plotting dense point clouds, the engine synthesizes sleek, mathematically elegant outlines that mirror the original artwork with surgical precision."
            },
            {
                "id": "modality-tuning-and-node-density-economics",
                "number": "03",
                "title": "Modality-Specific Optimization: Node Density Tuning and SVG Performance Economics",
                "content": "Visual graphics exhibit fundamentally divergent characteristics based on their domain: a minimalist company logo demands razor-sharp geometry with minimal anchor nodes, while a hand-drawn illustration requires expressive curve variations. ImageSVG addresses this diversity by offering modality-specific presets—including Icon/Logo, Illustration, Photo, and Black-and-White Line Art. Crucially, the platform gives developers granular control over curve style and node density: 'Fewer nodes' optimizes assets for ultra-lightweight frontend web embeds, while 'More detail' preserves intricate structural contours. The built-in interactive comparison viewer allows split-view high-magnification verification, ensuring path integrity prior to asset export."
            },
            {
                "id": "production-verdict-and-frontend-workflow-guidance",
                "number": "04",
                "title": "Production Workflow Verdict: Streamlining Web Asset Preparation and Desktop Integration",
                "content": "From an operational workflow perspective, ImageSVG delivers exceptional velocity for frontend developers, UI/UX engineers, and digital crafters. Accepting large files up to 20 MB across PNG, JPG, WebP, GIF, and BMP formats, it eliminates the necessity of launching bulky desktop suites like Adobe Illustrator or Vector Magic for everyday vector conversion tasks. The resulting clean, standard W3C-compliant SVG markup is immediately inspectable, easily styleable via CSS, and ready for deployment in modern component frameworks (such as React, Vue, or Astro). With daily free conversions available to registered users, ImageSVG serves as an indispensable utility for teams maintaining high visual standards across digital interfaces."
            }
        ],
        "tool_id": "imagesvg",
        "model_used": "editorial-team",
        "generated_at": "2026-11-23T10:18:00.000000+00:00"
    }
}

def catalog():
    # 1. Update all_tools.json
    with open(all_tools_file, 'r', encoding='utf-8') as f:
        tools = json.load(f)

    # Filter out existing if any
    new_ids = [t['id'] for t in TOOLS_TO_ADD]
    tools = [t for t in tools if t.get('id') not in new_ids]

    # Prepend at top
    for t in reversed(TOOLS_TO_ADD):
        tools.insert(0, t)

    with open(all_tools_file, 'w', encoding='utf-8') as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: Cataloged {len(TOOLS_TO_ADD)} tools into all_tools.json (Total tools: {len(tools)})")

    # 2. Update editorial_reviews.json
    with open(editorial_file, 'r', encoding='utf-8') as f:
        reviews = json.load(f)

    for k, v in REVIEWS_TO_ADD.items():
        reviews[k] = v

    with open(editorial_file, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: Added {len(REVIEWS_TO_ADD)} 4-chapter architectural dossiers into editorial_reviews.json (Total reviews: {len(reviews)})")

if __name__ == '__main__':
    catalog()
