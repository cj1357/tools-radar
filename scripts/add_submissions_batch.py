# -*- coding: utf-8 -*-
"""
Add submissions Cloudbrowser and ReelAI to all_tools.json and editorial_reviews.json
Submitted on 2026-11-09
"""

import json
import os
import sys

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
all_tools_path = os.path.join(data_dir, "all_tools.json")
reviews_path = os.path.join(data_dir, "editorial_reviews.json")

CLOUDBROWSER_TOOL = {
    "id": "cloudbrowser",
    "name": "Cloudbrowser",
    "tagline": "Persistent cloud Chrome sessions that AI agents control over Chrome DevTools Protocol (CDP)",
    "summary": "Cloudbrowser is a cloud-native browser infrastructure engineered for autonomous AI agents and automated workflows. It provides isolated, persistent Chrome browser environments accessible via the Chrome DevTools Protocol (CDP), allowing frameworks like Playwright, Puppeteer, and Stagehand to interact seamlessly without local resource overhead. With built-in session state persistence (cookies, logins, local storage), session forking, pause/resume lifecycles, and a low-latency Live View for real-time human observation and debugging, Cloudbrowser eliminates the fragility and IP ban friction of running local headless browsers.",
    "url": "https://cloudbrowser.tv",
    "github_url": "",
    "source": "submission",
    "category": "ai-agents",
    "tags": [
        "AI Agents",
        "Cloud Browser",
        "CDP",
        "Browser Automation",
        "Playwright",
        "Puppeteer",
        "Headless Chrome"
    ],
    "pricing_model": "Freemium",
    "stars": 0,
    "primary_alternative": "Browserbase / Steel",
    "is_self_hostable": False,
    "no_signup_required": False,
    "signal_score": 88,
    "verdict": "An essential cloud browser substrate for AI agents, providing persistent Chrome sessions over CDP with instant live viewing and lifecycle control.",
    "key_features": [
        {
            "title": "Isolated Cloud Browser Sessions",
            "description": "Run sandboxed Chrome instances in the cloud with persistent user profiles, preserving logins and state across tasks."
        },
        {
            "title": "Direct CDP & Automation Connectivity",
            "description": "Connect instantly using Chrome DevTools Protocol (CDP) from Playwright, Puppeteer, Selenium, or custom agent drivers."
        },
        {
            "title": "Live View & Lifecycle Controls",
            "description": "Observe agent actions in real time via low-latency interactive Live View, with capabilities to pause, inspect, and resume execution."
        }
    ],
    "use_cases": [
        "Autonomous web-browsing AI agents performing multi-step research, booking, or data extraction without managing local headless Chrome processes.",
        "Long-running scraping and automation pipelines requiring persistent session logins without re-authenticating every execution.",
        "Human-in-the-loop debugging of complex browser workflows using real-time Live View and session forking."
    ],
    "pros": [
        "Native CDP compatibility works out-of-the-box with Playwright, Puppeteer, and agent frameworks",
        "Persistent profiles retain session cookies and authentication states across agent runs",
        "Live View provides low-latency visual observability for debugging agent reasoning"
    ],
    "cons": [
        "Cloud-hosted service requires external network calls compared to fully local headless Chrome",
        "High-concurrency usage requires scaling into paid plans"
    ],
    "target_audience": "AI agent engineers, browser automation developers, data scraping teams, and autonomous assistant creators.",
    "comparison_vs_alt": "Compared to generic headless browser cloud providers or managing self-hosted Puppeteer clusters, Cloudbrowser specifically targets AI agent workflows with persistent session memory, session forking, and interactive live debugging.",
    "install_command": "npm install playwright # connect via cdpEndpoint: wss://connect.cloudbrowser.tv",
    "date_added": "2026-11-09",
    "featured": True,
    "faqs": [
        {
            "q": "What is Cloudbrowser and how does it assist AI agents?",
            "a": "Cloudbrowser provides managed, persistent Chrome browser sessions in the cloud that AI agents control over Chrome DevTools Protocol (CDP). It allows agents to navigate, click, fill forms, and maintain logins across sessions without local browser setup."
        },
        {
            "q": "Which browser automation frameworks are supported?",
            "a": "Any tool supporting CDP can connect directly to Cloudbrowser, including Playwright, Puppeteer, Selenium, Stagehand, and custom LLM agent drivers."
        },
        {
            "q": "Does Cloudbrowser offer a free tier?",
            "a": "Yes, Cloudbrowser offers a free plan with starter compute, alongside scalable paid plans for higher concurrency and extended session persistence."
        },
        {
            "q": "What is the Live View feature?",
            "a": "Live View allows human operators or developers to watch the agent's browser screen in real time, inspect DOM states, and pause or take manual control if an agent encounters a CAPTCHA or blocking dialog."
        }
    ]
}

CLOUDBROWSER_REVIEW = {
    "article_title": "Cloudbrowser Architecture & Engineering Dossier: Persistent Cloud Chrome Sessions & CDP Substrate for AI Agents",
    "reading_time": "6 min read",
    "editorial_verdict_callout": "Cloudbrowser delivers the missing cloud execution substrate for browser-using AI agents: persistent Chrome profiles, native CDP endpoints, and low-latency Live View observation.",
    "chapters": [
        {
            "id": "browser-agent-dilemma",
            "number": "01",
            "title": "The Cloud Browser Shift: Solving Headless Fragility for Autonomous Agents",
            "content": (
                "As AI agents evolve from code generation and chat interfaces to autonomous web actors (pioneered by Claude Computer Use, Stagehand, and browser-use frameworks), "
                "the infrastructure layer that hosts these browsers has become a primary bottleneck. Running headless Chrome locally introduces severe limitations: local memory leaks, "
                "heavy resource consumption, ephemeral session states that lose login tokens upon restart, and frequent IP/bot detection blocks. Autonomous agents require browser environments "
                "that behave like human desktops—persisting authentication cookies, remembering browser configurations, and enabling seamless background execution. "
                "Cloudbrowser addresses this architectural gap by offloading browser virtualization entirely to an elastic cloud fabric engineered specifically for agentic consumption."
            )
        },
        {
            "id": "cdp-engine-architecture",
            "number": "02",
            "title": "CDP Native Connectivity & Playwright/Puppeteer Interoperability",
            "content": (
                "At the core of Cloudbrowser is zero-friction compatibility with the Chrome DevTools Protocol (CDP). Rather than requiring proprietary SDK wrappers or invasive client libraries, "
                "Cloudbrowser exposes secure WebSocket CDP endpoints. Developers and AI agent runtimes can point existing Playwright, Puppeteer, or Selenium scripts directly to Cloudbrowser "
                "with a single connection URL (e.g., playwright.chromium.connectOverCDP(endpoint)). This architectural decision ensures instantaneous integration with modern agent stacks "
                "such as LangChain, CrewAI, AutoGen, or custom TypeScript/Python runners. The cloud runtime manages browser lifecycle, headless-to-headful rendering transitions, and network routing transparently."
            )
        },
        {
            "id": "persistent-profiles-liveview",
            "number": "03",
            "title": "Persistent State Profiles, Session Forking, and Human-in-the-Loop Live View",
            "content": (
                "What distinguishes Cloudbrowser from generic scraping proxies is its deep session state management. Sessions can be created with persistent profiles that store local storage, "
                "cookies, and authenticated states across distinct task runs. If an agent logs into a SaaS dashboard or e-commerce platform during Session A, Session B resumes with identical credentials "
                "without triggering re-authentication challenges or 2FA hurdles. Furthermore, Cloudbrowser incorporates an interactive 'Live View' stream: developers and operators can visually monitor "
                "the agent's real-time viewport, inspect executed DOM interactions, and even pause or intervene manually when edge cases arise—providing critical observability for production deployments."
            )
        },
        {
            "id": "production-tradeoffs",
            "number": "04",
            "title": "Production Evaluation, Competitive Landscape & Editorial Verdict",
            "content": (
                "In the rapidly maturing landscape of cloud browser infrastructure (competing alongside Browserbase, Steel, and Browserless), Cloudbrowser positions itself with an accessible freemium model "
                "and an intuitive balance between raw CDP speed and human-in-the-loop debugging controls. While self-hosted headless clusters remain viable for simple static scrapers, agentic workflows with dynamic "
                "multi-step goals overwhelmingly benefit from managed persistent environments. For teams building autonomous AI assistants, automated QA pipelines, or high-reliability research agents, Cloudbrowser "
                "delivers a robust, production-ready foundation that accelerates time-to-market."
            )
        }
    ]
}

REELAI_TOOL = {
    "id": "reelai",
    "name": "ReelAI",
    "tagline": "Turn photos into viral short AI videos with trending TikTok and Instagram motion presets",
    "summary": "ReelAI is a specialized AI video creation platform built for short-form video creators, marketers, and social media influencers. By combining state-of-the-art image-to-video generative models (such as MiniMax H3 and Seedance motion architectures) with a curated catalog of viral TikTok and Instagram Reel presets, ReelAI enables creators to transform static portraits or product photography into engaging cinematic clips in seconds. Output videos include full commercial licensing rights and zero watermarks, catering specifically to creators looking to capitalize on trending social video formats without learning complex 3D or VFX software.",
    "url": "https://tryreelai.com/",
    "github_url": "",
    "source": "submission",
    "category": "ai-tools",
    "tags": [
        "AI Video",
        "Generative AI",
        "Social Media",
        "TikTok",
        "Instagram Reels",
        "Photo to Video",
        "Creator Tools"
    ],
    "pricing_model": "Paid",
    "stars": 0,
    "primary_alternative": "Runway Gen-3 / Pika",
    "is_self_hostable": False,
    "no_signup_required": False,
    "signal_score": 82,
    "verdict": "A focused AI photo-to-video generator that lowers the barrier for creators to produce viral TikTok and Instagram Reel trends with pre-engineered motion presets.",
    "key_features": [
        {
            "title": "Photo-to-Video Synthesis",
            "description": "Transforms static images into dynamic high-frame-rate video clips powered by advanced generative video models."
        },
        {
            "title": "Viral Preset Catalog",
            "description": "Offers one-click motion templates mirroring trending TikTok and Instagram Reels effects (e.g., Rumpelstiltskin, Window Peeper, Moonwalk)."
        },
        {
            "title": "Commercial Licensing & Watermark-Free Export",
            "description": "Delivers ready-to-publish video exports suitable for commercial social media ads and content distribution."
        }
    ],
    "use_cases": [
        "Social media content creators and affiliate marketers quickly producing trending short videos to boost engagement.",
        "E-commerce brands animating product stills into dynamic video advertisements for TikTok, Instagram, and Shorts.",
        "Creative agencies scaling high-volume short-form content variants across client accounts without dedicated VFX teams."
    ],
    "pros": [
        "Pre-engineered viral effect templates eliminate prompt engineering friction for social creators",
        "Commercial usage rights and watermark-free exports across paid plans",
        "Fast generation speed with optimized motion transitions"
    ],
    "cons": [
        "Primarily designed for template-driven short clips rather than open-ended cinematic storyboard generation",
        "Paid subscription model without a permanent unlimited free tier"
    ],
    "target_audience": "Content creators, social media managers, affiliate marketers, and e-commerce brands producing short-form video content.",
    "comparison_vs_alt": "While generic video synthesis platforms like Runway or Kling require detailed camera motion prompts and trial-and-error fine-tuning, ReelAI focuses specifically on one-click viral preset templates optimized for vertical short-form platforms.",
    "install_command": "Web-based SaaS at https://tryreelai.com/",
    "date_added": "2026-11-09",
    "featured": True,
    "faqs": [
        {
            "q": "What is ReelAI?",
            "a": "ReelAI is an AI-powered photo-to-video creation tool that applies viral short-form motion presets to photos, producing high-impact videos for TikTok and Instagram."
        },
        {
            "q": "How does ReelAI differ from general video generation tools like Runway or Pika?",
            "a": "Instead of requiring complex camera control prompts or physics parameters, ReelAI provides turnkey effect presets specifically modeled after viral social media trends."
        },
        {
            "q": "Can I use ReelAI videos for commercial purposes?",
            "a": "Yes, videos generated on ReelAI include full commercial licensing rights with no watermarks."
        },
        {
            "q": "What kind of effects are available in the preset catalog?",
            "a": "The catalog includes popular motion effects such as Rumpelstiltskin, Window Peeper, Moonwalk, Dolphin Ride, and dynamic camera zoom transitions."
        }
    ]
}

REELAI_REVIEW = {
    "article_title": "ReelAI Product & Workflow Dossier: Turnkey Viral Short-Form Video Generation with Generative Motion Presets",
    "reading_time": "5 min read",
    "editorial_verdict_callout": "ReelAI translates cutting-edge photo-to-video diffusion into one-click viral presets, bridging the gap between frontier AI video models and daily social media content production.",
    "chapters": [
        {
            "id": "short-form-video-explosion",
            "number": "01",
            "title": "The Evolution of Short-Form Video: From Manual Editing to Generative Presets",
            "content": (
                "Short-form vertical video platforms (TikTok, Instagram Reels, YouTube Shorts) thrive on rapid meme turnover and algorithmic visual trends. "
                "Traditionally, capitalizing on a visual effect trend required either hours in motion graphics software like After Effects or extensive prompt engineering "
                "in frontier generative video sandboxes. For independent creators, e-commerce dropshippers, and agile growth marketers, this friction often means missing "
                "the critical algorithmic window. ReelAI was created to compress that production cycle from hours to seconds by pairing image-to-video diffusion engines "
                "with an actively curated registry of viral motion presets."
            )
        },
        {
            "id": "generative-pipeline",
            "number": "02",
            "title": "Under the Hood: Diffusion Architecture and Motion Vector Guidance",
            "content": (
                "Behind ReelAI's interface lies an ensemble of state-of-the-art video foundation models, integrating MiniMax H3 video synthesis and Seedance motion guidance. "
                "When a user uploads a photo, the pipeline segments foreground subjects from background scene depth. Rather than applying generic camera pans, the preset engine "
                "injects pre-computed motion latent trajectories (such as the viral Rumpelstiltskin effect, Window Peeper jump-cuts, or character Moonwalks). "
                "This ensures anatomical coherence and fluid temporal consistency across output frames, dramatically reducing the morphing artifacts typical of unconstrained video prompting."
            )
        },
        {
            "id": "creator-workflow-commercialization",
            "number": "03",
            "title": "Creator Economics: Commercial Licensing, Watermark-Free Export, and Monetization",
            "content": (
                "A significant hurdle in current consumer AI video tools is restrictive licensing and intrusive watermarking on entry tiers. ReelAI addresses commercial creators directly: "
                "exports are delivered at crisp vertical resolutions without watermarks, accompanied by full commercial exploitation rights. For marketing agencies running paid ads, "
                "this enables instant testing of multiple visual hooks for product photos. Creators can test several motion variants against the same static asset to discover which visual cadence "
                "delivers optimal click-through rates and watch-time retention."
            )
        },
        {
            "id": "market-positioning",
            "number": "04",
            "title": "Competitive Positioning vs Runway/Pika & Editorial Verdict",
            "content": (
                "In comparison with general-purpose cinematic generators such as Runway Gen-3 or Pika, ReelAI intentionally trades open-ended text prompting for hyper-focused preset speed. "
                "It does not aim to replace full-length cinematic film creation suites; rather, it provides a purpose-built tactical tool for short-form velocity. For digital creators and brands "
                "whose revenue depends on consistent social engagement and rapid trend responsiveness, ReelAI offers a streamlined, high-utility pipeline that turns static visuals into dynamic engagement drivers."
            )
        }
    ]
}

def main():
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # 1. Update Cloudbrowser
    c_idx = next((i for i, t in enumerate(tools) if t.get("id") == "cloudbrowser"), None)
    if c_idx is not None:
        tools[c_idx] = CLOUDBROWSER_TOOL
    else:
        tools.insert(0, CLOUDBROWSER_TOOL)

    # 2. Update ReelAI
    r_idx = next((i for i, t in enumerate(tools) if t.get("id") == "reelai"), None)
    if r_idx is not None:
        tools[r_idx] = REELAI_TOOL
    else:
        tools.insert(1, REELAI_TOOL)

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    print(f"all_tools.json updated successfully. Total tools: {len(tools)}")

    # 3. Update editorial_reviews.json
    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews["cloudbrowser"] = CLOUDBROWSER_REVIEW
    reviews["reelai"] = REELAI_REVIEW

    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)
    print("editorial_reviews.json updated successfully with Cloudbrowser and ReelAI reviews.")

if __name__ == "__main__":
    main()
