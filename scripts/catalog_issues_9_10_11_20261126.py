# -*- coding: utf-8 -*-
"""
Catalog GitHub Issues #9, #10, and #11 into all_tools.json and editorial_reviews.json:
- #9: WebDecoy Node SDK (webdecoy-node)
- #10: WebDecoy for WordPress (webdecoy-wordpress)
- #11: Website Speed Test (website-speed-test)
"""

import json
import os

BASE_DIR = r"d:\_projectsTYweb\tools-radar"
all_tools_file = os.path.join(BASE_DIR, "data", "all_tools.json")
editorial_file = os.path.join(BASE_DIR, "data", "editorial_reviews.json")

WEBDECOY_NODE_TOOL = {
    "id": "webdecoy-node",
    "name": "WebDecoy Node SDK",
    "tagline": "MIT-licensed TypeScript bot detection, local tripwire rules, and AI agent verification SDK for Node.js and edge runtimes",
    "summary": "WebDecoy Node SDK (@webdecoy/node) is an open-source TypeScript library providing local honeypot tripwires, rate limiting, AI crawler policies, and signed-agent verification for Node.js and edge frameworks including Express, Fastify, Next.js, Hono, and native fetch or node:http handlers. Developers can test and enforce local detection rules in monitor or enforce modes without a WebDecoy account or API key, while optionally connecting an API key to send verdicts to the hosted WebDecoy dashboard.",
    "url": "https://webdecoy.com/product/sdks/node/",
    "github_url": "https://github.com/WebDecoy/node",
    "source": "github_issue",
    "category": "frameworks-libraries",
    "tags": [
        "TypeScript",
        "Node.js",
        "Bot Detection",
        "AI Crawlers",
        "Middleware",
        "Security",
        "Open Source"
    ],
    "pricing_model": "Open Source",
    "stars": 5,
    "primary_alternative": "",
    "is_self_hostable": True,
    "no_signup_required": True,
    "signal_score": 86,
    "verdict": "A clean, modular MIT-licensed middleware toolkit that lets Node.js teams inspect bot traffic and test honeypot tripwires locally in monitor mode before introducing external API keys or enforcement.",
    "deployment_format": "npm Package & TypeScript SDK",
    "extensibility": "Express, Fastify, Next.js, Hono & Generic Fetch Adapters",
    "install_command": "npm install @webdecoy/node",
    "architecture_summary": "WebDecoy Node SDK operates directly inside the application's HTTP middleware layer across Node.js, Cloudflare Workers, Bun, and Deno runtimes. Using programmable honeypot tripwires, local rate-limit rules, and Web Bot Auth agent checks, it evaluates requests that reach the application middleware—complementing upstream CDN or WAF rules rather than replacing them.",
    "architecture_note": "Because the TypeScript monorepo (@webdecoy/node and framework packages) is MIT-licensed on GitHub, teams can inspect every detection rule, run the StackBlitz/local Express playground in monitor mode without an API key, and optionally wire up server-side keys for hosted reporting.",
    "date_added": "2026-11-26",
    "featured": False,
    "key_features": [
        {
            "title": "Honeypot Tripwires & Scanner-Bait Paths",
            "description": "Generates hidden rel=\"nofollow\" honeytoken paths and watches common scanner probes (such as /.env, /.git/config, and /wp-config.php) locally."
        },
        {
            "title": "Monitor-First Enforcement Boundaries",
            "description": "Starts in monitor mode to log and inspect local verdicts without blocking real visitors until developers explicitly turn on enforcement."
        },
        {
            "title": "Multi-Framework & Edge Adapters",
            "description": "Provides tailored middleware for Express, Fastify, Next.js, Hono (Cloudflare Workers, Bun, Deno), createFetchGuard(), and createNodeHttpGuard()."
        },
        {
            "title": "Keyless Local Workflow & Signed-Agent Checks",
            "description": "Supports local tripwires, rate limiting, AI crawler rules, and Web Bot Auth verification without an account or API key; dashboard reporting is optional."
        }
    ],
    "use_cases": [
        "Express or Next.js engineers evaluating honeypot tripwire decisions interactively via the runnable StackBlitz or local playground before deploying rules.",
        "API teams protecting Node.js endpoints against aggressive scraper probes without adding mandatory third-party cloud latency.",
        "TypeScript applications defining explicit AI crawler policies and verifying signed agent identities while preserving full local fallback."
    ],
    "pros": [
        "100% open-source MIT codebase in TypeScript with included type definitions and CI checks",
        "Zero account or API key required for local rules, rate limiting, and the Express playground",
        "Broad framework coverage including Express, Fastify, Next.js, Hono, Astro/SvelteKit/Remix fetch handlers, and node:http",
        "Honest visibility scope: clearly documents that middleware only sees requests reaching the app after upstream CDN caches"
    ],
    "cons": [
        "Middleware cannot observe or score traffic already blocked or served from cache upstream by a CDN before reaching Node.js",
        "Relatively young public repository with early community star count; hosted analytics require a separate WebDecoy API key"
    ],
    "target_audience": "Node.js, TypeScript, Next.js, and edge-runtime developers implementing local bot mitigation and AI crawler governance.",
    "comparison_vs_alt": "",
    "faqs": [
        {
            "q": "Does WebDecoy Node SDK require an API key to use?",
            "a": "No. Local tripwires, rate limits, AI crawler rules, and the Express playground operate locally in both monitor and enforce modes without a WebDecoy account or API key. An API key is only needed if you want to send detections to the hosted WebDecoy dashboard."
        },
        {
            "q": "Which JavaScript and TypeScript frameworks are supported?",
            "a": "WebDecoy provides dedicated packages and adapters for Express, Fastify, Next.js, and Hono (supporting Cloudflare Workers, Bun, and Deno), along with createFetchGuard() for Astro/SvelteKit/Remix and createNodeHttpGuard() for native node:http servers."
        },
        {
            "q": "What happens by default when I install the middleware?",
            "a": "The middleware defaults to monitor mode, recording verdicts cleanly without blocking requests so developers can inspect detections safely before enabling enforcement."
        },
        {
            "q": "What license is WebDecoy Node SDK released under?",
            "a": "The entire WebDecoy/node monorepo is licensed under the permissive MIT License."
        }
    ]
}

WEBDECOY_NODE_REVIEW = {
    "article_title": "WebDecoy Node SDK Architecture: Keyless Honeypot Tripwires, Monitor Mode, and Middleware Bot Governance",
    "reading_time": "5 min read",
    "editorial_verdict_callout": "WebDecoy Node SDK stands out for its pragmatic local-first security design: MIT-licensed TypeScript rules that run in monitor mode without an API key, backed by an immediately testable Express playground.",
    "chapters": [
        {
            "id": "server-middleware-blind-spots",
            "number": "01",
            "title": "The Application-Layer Blind Spot: Non-JS Crawlers Beyond Browser Analytics",
            "content": "Automated scrapers, vulnerability scanners, and AI crawlers frequently hit backend routes without executing client-side JavaScript tags—leaving standard frontend analytics completely blind to their activity. While edge WAFs handle network-level filtering, application teams often lack inspectable, framework-native visibility inside their own route handlers. WebDecoy Node SDK targets this exact layer by running inside Express, Fastify, Next.js, Hono, and generic fetch middleware, giving developers direct programmatic inspection of requests that reach their Node.js or edge runtime."
        },
        {
            "id": "honeypot-tripwires-and-monitor-architecture",
            "number": "02",
            "title": "Architectural Mechanics: Honeypot Tripwires, Signed-Agent Checks, and Keyless Rules",
            "content": "Built cleanly in TypeScript as an open MIT monorepo, @webdecoy/node constructs its local defense around honeypot tripwires, rate-limiting primitives, and Web Bot Auth verification. Developers can inject hidden rel=\"nofollow\" honeytoken paths into HTML responses—links ordinary human users never follow—alongside detection rules for scanner-bait endpoints like /.env, /.git/config, and /wp-config.php. Crucially, middleware starts in monitor mode by default: it generates verifiable verdicts without blocking traffic, allowing teams to compare real vs. decoy requests locally or via the browser-based StackBlitz Express playground without creating an account or provisioning an API key."
        },
        {
            "id": "runtime-portability-and-cdn-boundaries",
            "number": "03",
            "title": "Runtime Portability and Honest Upstream Visibility Boundaries",
            "content": "Rather than locking engineering teams into a single web framework, the repository ships lightweight packages and check:edge-verified adapters spanning Express, Fastify, Next.js, Hono (including Cloudflare Workers, Bun, and Deno), Astro/SvelteKit/Remix via createFetchGuard(), and native node:http servers. Equally commendable is the project's technical transparency: its documentation explicitly clarifies that server middleware only observes requests reaching the application runtime, meaning traffic served directly by upstream CDN caches sits outside middleware visibility unless paired with an edge sensor, and claimed user-agent strings require verification."
        },
        {
            "id": "developer-ergonomics-and-verdict",
            "number": "04",
            "title": "Operational Verdict: Low-Risk Integration for TypeScript Stacks",
            "content": "For TypeScript and Node.js teams evaluating application-level bot awareness and AI crawler policies, WebDecoy Node SDK provides an accessible, low-risk starting point. The MIT license ensures complete source auditability, the keyless monitor mode removes deployment anxiety, and optional dashboard reporting keeps commercial adoption purely additive. Whether testing rules in the 30-second Express playground or hardening production APIs, WebDecoy Node SDK delivers transparent security tooling grounded in verifiable behavior."
        }
    ],
    "tool_id": "webdecoy-node",
    "model_used": "editorial-team",
    "generated_at": "2026-11-26T14:50:00.000000+00:00"
}

WEBDECOY_WP_TOOL = {
    "id": "webdecoy-wordpress",
    "name": "WebDecoy for WordPress",
    "tagline": "GPL-licensed WordPress plugin for local AI crawler analytics, bot protection, robots.txt controls, and opt-in llms.txt",
    "summary": "WebDecoy for WordPress (listed as WebDecoy Bot Detection on WordPress.org) is a GPL-licensed plugin that helps site owners inspect AI crawler traffic vs. AI assistant visits inside wp-admin, configure optional robots.txt crawler rules, generate an opt-in llms.txt file without overwriting existing providers, and protect WordPress forms, logins, and WooCommerce checkout. Local analytics and monitor mode run directly in WordPress with no WebDecoy account or API key required, while optional connectivity adds hosted dashboard reporting.",
    "url": "https://wordpress.org/plugins/webdecoy/",
    "github_url": "https://github.com/WebDecoy/wordpress-plugin",
    "source": "github_issue",
    "category": "open-source",
    "tags": [
        "WordPress",
        "AI Crawlers",
        "Bot Protection",
        "llms.txt",
        "WooCommerce",
        "Open Source",
        "PHP"
    ],
    "pricing_model": "Open Source",
    "stars": 1,
    "primary_alternative": "",
    "is_self_hostable": True,
    "no_signup_required": True,
    "signal_score": 85,
    "verdict": "A well-scoped, GPL-licensed WordPress plugin that brings AI crawler visibility, opt-in llms.txt management, and WooCommerce checkout bot protection into wp-admin without forcing external accounts or CAPTCHAs.",
    "deployment_format": "WordPress Plugin (PHP 7.4+ / WP 6.1+)",
    "extensibility": "WordPress Admin Reports, robots.txt & llms.txt Controls, Optional Cloud Sync",
    "install_command": "# Install directly via WordPress Admin -> Plugins > Add New -> search 'WebDecoy Bot Detection'\n# Or clone source for Composer PHPCS/PHPStan development:\ngit clone https://github.com/WebDecoy/wordpress-plugin.git",
    "architecture_summary": "Built for WordPress 6.1+ and PHP 7.4+, WebDecoy for WordPress executes server-side path inspection (including MITRE ATT&CK probe patterns), rate limiting, reverse-DNS verification for legitimate crawlers, and invisible browser/proof-of-work checks directly inside your WordPress installation.",
    "architecture_note": "Released under GPL v2+ with full source on GitHub and Composer-based phpcs/phpstan quality checks. Local AI Traffic & Analytics operates without a WebDecoy account; note that full-page upstream caches can bypass PHP logging unless paired with cache exceptions or the bundled AJAX scanner.",
    "date_added": "2026-11-26",
    "featured": False,
    "key_features": [
        {
            "title": "Separate AI Crawler & AI Assistant Reporting",
            "description": "Displays which AI crawlers hit your WordPress installation and which visits arrive from AI assistants inside dedicated wp-admin AI Traffic & Analytics views."
        },
        {
            "title": "Crawler-Category robots.txt & Opt-In llms.txt",
            "description": "Offers optional robots.txt rule controls grouped by crawler category and an opt-in llms.txt generator designed to preserve an existing provider."
        },
        {
            "title": "Monitor-Mode Bot & WooCommerce Protection",
            "description": "Combines invisible proof-of-work checks, rate limiting, reverse-DNS verification, and WooCommerce classic/Blocks checkout defenses—testable in monitor mode before enforcing."
        },
        {
            "title": "Keyless Local Workflow",
            "description": "All local detection, crawler analytics, and blocking controls function cleanly without a WebDecoy account or external API key."
        }
    ],
    "use_cases": [
        "WordPress publishers and SaaS blogs measuring AI crawler hits versus AI assistant referral visits directly from wp-admin without external SaaS fees.",
        "Site administrators testing crawler policies, rate limits, and MITRE ATT&CK path protections safely in monitor mode on a staging site before enforcing.",
        "WooCommerce store owners defending classic and Blocks checkout flows against automated carding bursts without forcing customer image puzzles."
    ],
    "pros": [
        "Officially reviewed and available on WordPress.org under GPL v2+ with full PHP source on GitHub",
        "Zero WebDecoy account or API key required for local reporting, monitor mode, or WooCommerce protection",
        "Thoughtful WordPress integration: opt-in llms.txt generator preserves existing providers instead of clobbering SEO plugins",
        "Transparent documentation detailing full-page cache behavior and non-cache AJAX scanner considerations"
    ],
    "cons": [
        "Upstream full-page caches answer requests before PHP runs unless configured alongside cache rules or AJAX reporting",
        "Optional hosted dashboard aggregation requires linking an external WebDecoy account"
    ],
    "target_audience": "WordPress site owners, WooCommerce store maintainers, technical SEO managers, and PHP developers seeking local AI crawler analytics and bot mitigation.",
    "comparison_vs_alt": "",
    "faqs": [
        {
            "q": "Do I need a WebDecoy account or API key for the WordPress plugin?",
            "a": "No. The GPL-licensed plugin runs local AI Traffic & Analytics, robots.txt/llms.txt tools, monitor mode, and protection rules directly inside WordPress without an account or API key. Connecting to WebDecoy's hosted dashboard is strictly optional."
        },
        {
            "q": "Will WebDecoy interfere with my existing llms.txt or SEO plugin?",
            "a": "According to the maintainers, the llms.txt generator is strictly opt-in and preserves any existing llms.txt provider configured on the site."
        },
        {
            "q": "How should I deploy protection without blocking real visitors?",
            "a": "Install the plugin in monitor mode first (recommended on a staging site or non-blocking setup) to review AI Traffic & Analytics and bot detections before turning on active enforcement rules."
        },
        {
            "q": "Does page caching affect crawler reporting?",
            "a": "Yes. If an upstream cache serves HTML before PHP runs, WordPress PHP detection does not execute for that cached hit. Browser scanner signals can still report via non-cached wp-admin/admin-ajax.php requests, or upstream edge sensors can be used."
        }
    ]
}

WEBDECOY_WP_REVIEW = {
    "article_title": "WebDecoy for WordPress Analysis: Local AI Crawler Analytics, Opt-In llms.txt Governance, and WooCommerce Checkout Defense",
    "reading_time": "5 min read",
    "editorial_verdict_callout": "By putting AI crawler analytics, non-destructive llms.txt generation, and monitor-first bot checks inside a GPL WordPress plugin with zero API-key lock-in, WebDecoy fills a practical gap for publishers and WooCommerce stores.",
    "chapters": [
        {
            "id": "wordpress-ai-crawler-visibility",
            "number": "01",
            "title": "Seeing Behind the Cache: Tracking AI Crawlers vs. AI Assistant Referrals in WordPress",
            "content": "Standard web analytics scripts capture human browser sessions, yet leave WordPress site owners in the dark about automated AI scrapers harvesting posts or referrals arriving from AI assistants. WebDecoy for WordPress brings visibility directly into wp-admin via dedicated AI Traffic & Analytics reporting, separating AI crawler requests that reach WordPress from AI assistant visitor sessions—all computed locally on the host without shipping raw site logs to third-party SaaS platforms."
        },
        {
            "id": "non-destructive-robots-and-llms-control",
            "number": "02",
            "title": "Policy Architecture: Category-Based robots.txt, Opt-In llms.txt, and Multi-Layer Checks",
            "content": "Beyond passive observation, the GPL-licensed plugin offers pragmatic governance tools tailored to WordPress operations. Administrators can manage optional robots.txt directives grouped by crawler category and enable an opt-in llms.txt generator explicitly built to respect and preserve existing llms.txt providers. On the security front, WebDecoy layers reverse-DNS verification for legitimate bots (such as Googlebot and Bingbot), MITRE ATT&CK path probe analysis, configurable rate limiting, IP/CIDR blocks, and invisible browser proof-of-work checks—eschewing annoying visual CAPTCHAs."
        },
        {
            "id": "woocommerce-protection-and-cache-reality",
            "number": "03",
            "title": "Monitor-First Ergonomics, WooCommerce Checkout, and Page-Caching Realities",
            "content": "Rather than forcing aggressive blocking out of the box, WebDecoy encourages teams to install on a staging or live site in monitor mode, inspect captured detection evidence, and verify behavior prior to enabling enforcement—including specialized protections tested against rapid failed-order patterns on both classic and Blocks WooCommerce checkouts. Equally important is the project's candor regarding WordPress caching: documentation clearly highlights that upstream full-page caches serve responses before PHP detection fires, detailing how the AJAX scanner and cache exclusions preserve signal accuracy."
        },
        {
            "id": "operational-verdict-wp-ecosystem",
            "number": "04",
            "title": "Operational Suitability Verdict: Self-Contained Governance for WP 6.1+",
            "content": "Available directly through the official WordPress.org plugin directory and backed by clean Composer-checked (phpcs and phpstan) PHP code on GitHub, WebDecoy for WordPress is an authentic, self-contained utility for site administrators. Its commitment to keeping local analytics and form/checkout protections completely free and keyless makes it easy to adopt and audit, with hosted dashboard reporting reserved purely for teams wanting multi-site cloud aggregation."
        }
    ],
    "tool_id": "webdecoy-wordpress",
    "model_used": "editorial-team",
    "generated_at": "2026-11-26T14:50:00.000000+00:00"
}

WEBSITE_SPEED_TEST_TOOL = {
    "id": "website-speed-test",
    "name": "Website Speed Test",
    "tagline": "Free browser-based server response time, returned HTML, and basic on-page SEO checker",
    "summary": "Website Speed Test is a free browser utility built and maintained by Hand On Web Ltd that inspects any publicly accessible URL for server response time (TTFB), returned HTML, and basic on-page SEO elements such as title tags and meta descriptions. It generates an instant diagnostic summary with actionable recommendations without requiring signup or storing submitted data, while noting that 28-day real-user Core Web Vitals data is available separately via Google PageSpeed Insights.",
    "url": "https://www.handonweb.com/tools/website-speed-test",
    "github_url": "",
    "source": "github_issue",
    "category": "testing-qa",
    "tags": [
        "Testing",
        "Speed Test",
        "TTFB",
        "On-Page SEO",
        "HTML Checker",
        "Free Tool"
    ],
    "pricing_model": "Free",
    "stars": 0,
    "primary_alternative": "",
    "is_self_hostable": False,
    "no_signup_required": True,
    "signal_score": 75,
    "verdict": "A straightforward, zero-signup browser checker for quick server response and basic HTML/on-page SEO sanity checks—useful as a lightweight first pass alongside dedicated lab or field tools like PageSpeed Insights.",
    "deployment_format": "Hosted Web Page (Browser Utility)",
    "extensibility": "Browser Form Input (No Package, CLI, or Public API)",
    "install_command": "",
    "architecture_summary": "Website Speed Test is delivered purely as a hosted web page operated by Hand On Web Ltd. Visitors enter any public URL into the browser interface to inspect server response timing and returned HTML metadata without local installation.",
    "architecture_note": "Strictly a hosted browser tool—no installable package, CLI binary, or public source repository is offered. According to the tool page, it evaluates publicly available URL data only and does not store user test records.",
    "date_added": "2026-11-26",
    "featured": False,
    "key_features": [
        {
            "title": "Public URL Server Response Inspection",
            "description": "Measures initial server response time (TTFB) and inspects HTTP compression/HTML output for any publicly reachable web page."
        },
        {
            "title": "Basic On-Page SEO Audit",
            "description": "Evaluates foundational HTML metadata including page title length, meta description, heading tags, canonical tags, and HTTPS status."
        },
        {
            "title": "Actionable Quick Recommendations",
            "description": "Presents immediate prioritized suggestions covering image optimization, render-blocking resources, compression, and caching."
        },
        {
            "title": "No Account & No Data Storage",
            "description": "Runs free of charge in any standard browser with zero login walls; the tool page states that test inputs are not stored."
        }
    ],
    "use_cases": [
        "Developers and marketers running a fast post-deploy sanity check on a page's TTFB response, HTML headers, title, and meta description.",
        "Small business owners reviewing common speed fundamentals (compression, caching, image weight) without setting up CLI audit tools.",
        "Quick pre-launch verification of public landing pages prior to running full field-data checks in Google PageSpeed Insights."
    ],
    "pros": [
        "Completely free with zero account registration or usage gating",
        "Clear statement that only publicly available data is inspected and no data is stored",
        "Honest scope boundaries: explicitly points users to Google PageSpeed Insights for 28-day real-user Core Web Vitals field metrics"
    ],
    "cons": [
        "Hosted single-page web utility with no public source repository, CLI binary, or automated CI/CD integration",
        "Does not capture 28-day CrUX real-user Core Web Vitals field datasets or replace full multi-step browser performance profiling"
    ],
    "target_audience": "Web developers, SEO practitioners, and small website owners looking for a fast, signup-free check of server response time and basic HTML/SEO tags.",
    "comparison_vs_alt": "",
    "faqs": [
        {
            "q": "Does Website Speed Test require signup or store tested URLs?",
            "a": "No. It is free to run directly in a web browser without creating an account, and the tool page states that it analyzes publicly available data only and stores no data."
        },
        {
            "q": "Does it measure real-user Core Web Vitals like PageSpeed Insights?",
            "a": "No. Website Speed Test reports server response time, returned HTML, and basic on-page SEO checks with recommendations. Real-user 28-day Core Web Vitals field metrics are referenced separately in Google PageSpeed Insights."
        },
        {
            "q": "Is there a CLI package or open-source repository for self-hosting?",
            "a": "No. Per the maintainers (Hand On Web Ltd), Website Speed Test is strictly a hosted web tool with no installable package or public source repository."
        },
        {
            "q": "Who maintains this tool?",
            "a": "It is built and maintained by Hand On Web Ltd, a web design and SEO agency based in Chester, UK."
        }
    ]
}

WEBSITE_SPEED_TEST_REVIEW = {
    "article_title": "Website Speed Test Overview: Server Response Timing, Basic On-Page SEO Checks, and Scope vs. Field Telemetry",
    "reading_time": "4 min read",
    "editorial_verdict_callout": "Maintained by Hand On Web Ltd as a free, no-signup utility, Website Speed Test works best as an instant first-pass check for TTFB and HTML meta hygiene before deeper Lighthouse or PageSpeed profiling.",
    "chapters": [
        {
            "id": "instant-ttfb-and-html-triage",
            "number": "01",
            "title": "Lightweight Pre-Audit Triage: Instant Server Response & Metadata Checks",
            "content": "Before spinning up heavy multi-minute browser profiling traces or configuring enterprise monitoring pipelines, developers and site maintainers frequently just want an immediate check: how fast did the server answer with the first byte of HTML, and are basic on-page SEO tags intact? Website Speed Test answers that narrow need by letting any visitor paste a public URL and inspect server response timing alongside returned HTML elements—all inside a zero-signup browser form."
        },
        {
            "id": "on-page-seo-and-fundamentals",
            "number": "02",
            "title": "What the Checker Inspects: TTFB, Compression Signals, and Essential HTML Elements",
            "content": "Rather than burying users in complex waterfall graphs, the utility focuses on foundational web health vectors: initial server response (TTFB), Gzip/Brotli compression clues, caching readiness, and core HTML metadata including title tags, meta descriptions, heading structure, canonical URLs, and HTTPS compliance. Each report pairs detected findings with plain-language recommendations—making it straightforward for non-specialist editors or small-business site owners to spot missing descriptions or slow origin responses."
        },
        {
            "id": "explicit-scope-vs-core-web-vitals",
            "number": "03",
            "title": "Honest Diagnostic Boundaries: Server Checks vs. 28-Day Real-User Field Data",
            "content": "One refreshing aspect of Website Speed Test is its transparent scope boundary. The tool makes no claim to replace real-user telemetry datasets (such as Google's Chrome User Experience Report) or provide an installable CLI/API auditing suite. Instead, its page and submission explicitly direct users to Google PageSpeed Insights whenever 28-day field Core Web Vitals (LCP, INP, CLS) are required, and confirm that no user account is needed and no tested URL records are stored."
        },
        {
            "id": "operational-verdict-agency-utility",
            "number": "04",
            "title": "Operational Verdict: A Simple, No-Friction Bookmark for Quick Sanity Checks",
            "content": "As a free hosted web utility offered by UK web design and SEO agency Hand On Web Ltd, Website Speed Test occupies a modest, practical niche. While engineering teams automating performance regressions in CI will want dedicated CLI/Lighthouse tooling, anyone seeking a fast, privacy-respecting, no-login browser check on TTFB and basic HTML SEO tags will find it clean and dependable."
        }
    ],
    "tool_id": "website-speed-test",
    "model_used": "editorial-team",
    "generated_at": "2026-11-26T14:50:00.000000+00:00"
}

def run():
    with open(all_tools_file, "r", encoding="utf-8") as f:
        tools = json.load(f)

    new_ids = {"webdecoy-node", "webdecoy-wordpress", "website-speed-test"}
    tools = [t for t in tools if t.get("id") not in new_ids]

    # Insert in order #11, #10, #9 so #9 sits near top
    tools.insert(0, WEBSITE_SPEED_TEST_TOOL)
    tools.insert(0, WEBDECOY_WP_TOOL)
    tools.insert(0, WEBDECOY_NODE_TOOL)

    with open(all_tools_file, "w", encoding="utf-8") as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: all_tools.json saved with {len(tools)} tools.")

    with open(editorial_file, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews["webdecoy-node"] = WEBDECOY_NODE_REVIEW
    reviews["webdecoy-wordpress"] = WEBDECOY_WP_REVIEW
    reviews["website-speed-test"] = WEBSITE_SPEED_TEST_REVIEW

    with open(editorial_file, "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: editorial_reviews.json saved with {len(reviews)} reviews.")

if __name__ == "__main__":
    run()
