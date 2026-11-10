# -*- coding: utf-8 -*-
"""
Add submissions from GitHub Issues #3, #4, #5, #6 to all_tools.json and editorial_reviews.json:
- YouTranscripts (Issue #6)
- Orkas (Issue #5)
- Revenue Scout (Issue #4)
- Akii: SEO & AI Search Optimizer (Issue #3)
"""

import json
import os
import sys

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
all_tools_path = os.path.join(data_dir, "all_tools.json")
reviews_path = os.path.join(data_dir, "editorial_reviews.json")

TOOLS = [
    {
        "id": "youtranscripts",
        "name": "YouTranscripts",
        "tagline": "Fast YouTube video caption extractor, AI summarizer, and multi-language subtitle translator",
        "summary": "YouTranscripts is a streamlined multimedia transcription and research tool that extracts captions from supported YouTube videos without manual transcription or complex API configurations. The platform enables creators, academic researchers, and professionals to export clean, formatted transcripts in TXT, DOCX, PDF, SRT, and CSV formats. Beyond raw transcript extraction, YouTranscripts integrates neural AI summarization for rapid content synthesis and supports direct translation into 17 global languages, all accessible via a free account with no credit card required.",
        "url": "https://www.youtranscripts.com/",
        "github_url": "",
        "source": "submission",
        "category": "ai-tools",
        "tags": [
            "YouTube",
            "Transcription",
            "AI Summarizer",
            "Translation",
            "Content Creation",
            "Productivity",
            "Subtitles"
        ],
        "pricing_model": "Freemium",
        "stars": 0,
        "primary_alternative": "Otter.ai / NoteGPT",
        "is_self_hostable": False,
        "no_signup_required": False,
        "signal_score": 81,
        "verdict": "A fast and dependable web utility for converting long-form YouTube video audio into downloadable transcripts, actionable AI summaries, and multi-language subtitles.",
        "key_features": [
            {
                "title": "Multi-Format Transcript Export",
                "description": "Download clean, timestamped or plain text transcripts in TXT, DOCX, PDF, SRT, or CSV formats for research and video editing."
            },
            {
                "title": "Dual-Mode AI Summarization",
                "description": "Generate quick bulleted takeaways or detailed thematic summaries from long-form lectures, interviews, and tutorials."
            },
            {
                "title": "17-Language Neural Translation",
                "description": "Instantly translate extracted transcripts into 17 supported global languages, expanding cross-border research and subtitle distribution."
            }
        ],
        "use_cases": [
            "Content creators and video editors extracting precise SRT subtitle files from YouTube videos for localized re-publishing.",
            "Students, academic researchers, and analysts summarizing 2-hour conference keynotes and technical lectures into structured markdown digests.",
            "Cross-border media professionals translating overseas foreign-language interviews into native reference materials."
        ],
        "pros": [
            "Clean export options covering both plain text documents (DOCX, PDF) and subtitle files (SRT, CSV)",
            "Generous free tier with no credit card required for starter usage",
            "Fast web extraction without requiring local Python scripts or FFmpeg dependencies"
        ],
        "cons": [
            "Dependent on YouTube's public caption availability for source extraction",
            "Advanced high-volume batch processing requires fair-use account tiering"
        ],
        "target_audience": "Content creators, researchers, video editors, students, and media professionals needing quick YouTube transcript extraction and multilingual translation.",
        "comparison_vs_alt": "While general meeting transcription tools like Otter.ai focus on live speech-to-text recording, YouTranscripts is purpose-built for zero-friction web-based YouTube video caption extraction and instant SRT subtitle conversion.",
        "install_command": "Web service at https://www.youtranscripts.com/",
        "date_added": "2026-11-10",
        "featured": True,
        "faqs": [
            {
                "q": "What is YouTranscripts?",
                "a": "YouTranscripts is a web utility that reads captions from supported YouTube videos and provides transcript downloads, AI summaries, and 17-language translations."
            },
            {
                "q": "What export formats are supported?",
                "a": "Transcripts can be downloaded in TXT, DOCX, PDF, SRT (for video subtitles), and CSV formats."
            },
            {
                "q": "Is a credit card required to use YouTranscripts?",
                "a": "No, core tools are available under a free account without requiring a credit card, subject to fair use."
            },
            {
                "q": "Does YouTranscripts support translation?",
                "a": "Yes, extracted video transcripts can be translated into 17 supported global languages directly in the web app."
            }
        ]
    },
    {
        "id": "orkas",
        "name": "Orkas",
        "tagline": "Local-first desktop AI team coordinating specialist agents for reports and editable slides",
        "summary": "Orkas is an open-source, local-first multi-agent desktop application that transforms raw project materials and business briefs into comprehensive analytical reports and fully editable presentation slides. Engineered around a hierarchical Commander agent pattern, Orkas breaks complex objectives into actionable workflows and delegates them across 16 built-in specialist agents (covering research, office documentation, slide design, coding, and media). Built with strict data privacy at its core, Orkas ensures all project files, history, and embeddings remain strictly on the user's desktop, offering complete flexibility to connect local model runtimes (Ollama/vLLM) or commercial LLM providers.",
        "url": "https://orkas.ai/",
        "github_url": "https://github.com/Orkas-AI/Orkas",
        "source": "submission",
        "category": "ai-agents",
        "tags": [
            "AI Agents",
            "Local-First",
            "Presentation",
            "Reports",
            "Open Source",
            "Desktop App",
            "Productivity",
            "Multi-Agent"
        ],
        "pricing_model": "Open Source",
        "stars": 9155,
        "primary_alternative": "Gamma / Tome",
        "is_self_hostable": True,
        "no_signup_required": True,
        "signal_score": 94,
        "verdict": "An outstanding open-source desktop AI suite: 9,000+ GitHub stars, MIT license, hierarchical Commander multi-agent coordination, and local-first document synthesis.",
        "key_features": [
            {
                "title": "Hierarchical Commander Agent",
                "description": "Translates high-level project goals into executable workstreams, coordinating 16 specialist agents while maintaining end-to-end project context."
            },
            {
                "title": "Editable Slide & Report Generation",
                "description": "Analyzes raw documents and workbooks to generate formatted research reports and native, fully editable presentations in a single unified workspace."
            },
            {
                "title": "Local-First Privacy & BYOM Inference",
                "description": "Project files remain local by default. Connect seamlessly to local model endpoints (Ollama/vLLM) or enterprise API keys without vendor lock-in."
            }
        ],
        "use_cases": [
            "Product managers and executives turning raw spreadsheets, meeting transcripts, and project specs into polished investor or executive slide decks.",
            "Consultants and analysts compiling multi-source research dossiers into formatted analytical reports with citations.",
            "Privacy-conscious enterprises requiring high-capability agentic intelligence without uploading confidential IP to third-party cloud SaaS."
        ],
        "pros": [
            "100% free and open-source under the permissive MIT license with 9,100+ GitHub community stars",
            "Local-first data architecture guarantees confidential documents and prompts never leave your hardware",
            "Produces real, editable presentation slides rather than locked static screenshots or flattened PDFs"
        ],
        "cons": [
            "Local model inference requires modern desktop hardware with decent GPU/unified memory (e.g., Apple Silicon or RTX GPU)",
            "Linux packaging currently requires building from source repository"
        ],
        "target_audience": "Product managers, strategy consultants, researchers, developers, and privacy-focused teams requiring autonomous agent orchestration for document synthesis.",
        "comparison_vs_alt": "While cloud-hosted presentation generators like Gamma or Tome require uploading sensitive documents to proprietary cloud servers, Orkas runs locally on your desktop with open-source MIT code, supporting local Ollama models and direct file system workflows.",
        "install_command": "git clone https://github.com/Orkas-AI/Orkas.git # or download macOS/Windows app at https://orkas.ai/download/",
        "date_added": "2026-11-10",
        "featured": True,
        "faqs": [
            {
                "q": "What is Orkas?",
                "a": "Orkas is an open-source, local-first desktop application that coordinates an autonomous AI team to turn project files into structured reports and editable slide decks."
            },
            {
                "q": "How does Orkas protect data privacy?",
                "a": "Orkas operates local-first: project files and history remain on your device by default. You can run local LLMs (via Ollama or vLLM) so zero data leaves your machine."
            },
            {
                "q": "Is Orkas free and open source?",
                "a": "Yes, the core Orkas desktop app is 100% free and open-source under the MIT license, with packaged downloads for macOS and Windows, and Linux source builds."
            },
            {
                "q": "Can I edit the generated slides?",
                "a": "Yes, unlike tools that generate flattened PDF or image slides, Orkas outputs native, fully editable presentation structures that can be refined in the workspace."
            }
        ]
    },
    {
        "id": "revenue-scout",
        "name": "Revenue Scout",
        "tagline": "AI social listening and inbound lead discovery across Reddit, LinkedIn, X, and 4 major platforms",
        "summary": "Revenue Scout is an AI-powered social listening and revenue intelligence platform that monitors public posts across 7 major networks: Reddit, LinkedIn, X, Facebook, Instagram, TikTok, and YouTube. Moving beyond blunt keyword scraping, Revenue Scout utilizes semantic understanding to evaluate buyer intent against a business's specific value proposition, explaining why a conversation represents a high-probability commercial opportunity. The platform drafts tailored, human-in-the-loop replies, ensuring sales and marketing teams maintain complete editorial authority while accelerating pipeline generation.",
        "url": "https://revenuescout.ai/",
        "github_url": "",
        "source": "submission",
        "category": "ai-tools",
        "tags": [
            "Lead Generation",
            "Social Listening",
            "AI Marketing",
            "Reddit",
            "LinkedIn",
            "Sales",
            "B2B",
            "Growth"
        ],
        "pricing_model": "Freemium",
        "stars": 0,
        "primary_alternative": "Brand24 / Syften",
        "is_self_hostable": False,
        "no_signup_required": False,
        "signal_score": 85,
        "verdict": "An effective social intelligence engine that bridges public organic social chatter and sales pipelines across 7 major platforms with semantic intent scoring.",
        "key_features": [
            {
                "title": "7-Platform Omnichannel Monitoring",
                "description": "Continuously indexes public discussions across Reddit, LinkedIn, X, Facebook, Instagram, TikTok, and YouTube in a unified feed."
            },
            {
                "title": "Semantic Intent & Opportunity Matching",
                "description": "Evaluates user intent against your specific product catalog, detailing exactly why a social thread matches your commercial offering."
            },
            {
                "title": "Human-in-the-Loop Reply Synthesis",
                "description": "Generates contextual response drafts that users can inspect, modify, and dispatch, preventing robotic or off-brand automated spam."
            }
        ],
        "use_cases": [
            "B2B SaaS founders and marketing teams identifying organic buyer queries on Reddit and LinkedIn (e.g., 'Looking for a tool that does X').",
            "E-commerce brands discovering consumer recommendations and product dissatisfaction mentions across TikTok and Instagram.",
            "Growth agencies scaling multi-channel social engagement without manual keyword scouring across disparate search tabs."
        ],
        "pros": [
            "Monitors 7 major social channels in one unified interface, eliminating siloed platform monitoring",
            "2,000 free starter credits upon verification with no credit card required and non-expiring purchased credits",
            "Emphasizes human-in-the-loop review, preserving brand reputation and community authenticity"
        ],
        "cons": [
            "Paid subscriptions start at $49/month for higher volume monitoring and team features",
            "Requires careful onboarding prompt definition to avoid surfacing adjacent low-intent mentions"
        ],
        "target_audience": "Founders, B2B sales teams, growth marketers, and digital agencies seeking organic inbound lead discovery across social channels.",
        "comparison_vs_alt": "While legacy social listeners like Brand24 or Mention focus on brand mention volume and sentiment graphs, Revenue Scout specifically isolates commercial buying intent and drafts actionable conversion replies.",
        "install_command": "Web SaaS at https://revenuescout.ai/",
        "date_added": "2026-11-10",
        "featured": True,
        "faqs": [
            {
                "q": "What is Revenue Scout?",
                "a": "Revenue Scout is an AI social listening tool that finds public posts matching what you sell across 7 platforms and drafts replies for your review."
            },
            {
                "q": "Which social platforms are covered?",
                "a": "Revenue Scout indexes public discussions across Reddit, LinkedIn, X, Facebook, Instagram, TikTok, and YouTube."
            },
            {
                "q": "Does Revenue Scout post automatically without review?",
                "a": "No, it drafts proposed replies for human review, giving you full control to inspect, edit, and post manually or approve follow-ups."
            },
            {
                "q": "What is the pricing model?",
                "a": "Each verified customer receives 2,000 free credits with no credit card required. Monthly plans start at $49, with non-expiring credit top-ups starting at $15."
            }
        ]
    },
    {
        "id": "akii-seo-ai-search-optimizer",
        "name": "Akii: SEO & AI Search Optimizer",
        "tagline": "Open-source Claude Code terminal plugin for technical SEO, broken link auditing, and GEO/AEO optimization",
        "summary": "Akii: SEO & AI Search Optimizer is a free, MIT-licensed terminal extension engineered specifically for the Claude Code CLI environment. Packing 12 specialized skills, 5 autonomous subagents, and 3 slash commands, the plugin equips software engineers and technical SEO professionals to conduct comprehensive in-terminal audits—identifying broken links, analyzing competitor site structures, planning content architectures, and auto-generating valid Schema.org JSON-LD graph metadata. Furthermore, Akii pioneers Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO), evaluating how search engines and LLM answer systems perceive domain authority.",
        "url": "https://akii.com/portfolio#search-optimizer",
        "github_url": "https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer",
        "source": "submission",
        "category": "developer-tools",
        "tags": [
            "Claude Code",
            "SEO",
            "GEO",
            "AEO",
            "CLI",
            "Open Source",
            "Developer Tools",
            "Schema Markup"
        ],
        "pricing_model": "Open Source",
        "stars": 79,
        "primary_alternative": "Screaming Frog / Sitebulb",
        "is_self_hostable": True,
        "no_signup_required": True,
        "signal_score": 90,
        "verdict": "A groundbreaking open-source Claude Code plugin bringing technical SEO auditing, link validation, and AI search visibility (GEO/AEO) directly into terminal developer workflows.",
        "key_features": [
            {
                "title": "Comprehensive Terminal Site Audits",
                "description": "Inspect web pages, detect 404 broken links, audit header tags, and extract competitive ranking signals directly from your Claude Code session."
            },
            {
                "title": "Automated Schema & JSON-LD Generation",
                "description": "Generate valid, rich-result-ready Schema.org JSON-LD graphs for organizations, software apps, and articles to boost Google rich snippet capture."
            },
            {
                "title": "GEO & AI Search Visibility Estimation",
                "description": "Evaluate domain positioning for generative AI search engines (ChatGPT Search, Perplexity, Google AI Overviews) using public signals and optional Ahrefs telemetry."
            }
        ],
        "use_cases": [
            "Developers using Claude Code to audit production websites and generate correct Schema.org JSON-LD metadata during CI/CD or staging builds.",
            "Technical SEO consultants investigating competitor link architectures and content structures from command-line terminals.",
            "Web engineering teams preparing static sites and applications for Answer Engine Optimization (AEO) and AI overview citations."
        ],
        "pros": [
            "100% free and open-source under MIT license, designed natively for the Claude Code plugin ecosystem",
            "Comprehensive suite containing 12 skills, 5 autonomous agents, and 3 slash commands in one package",
            "Zero hosted service dependency—runs locally within the Claude Code terminal session without telemetry"
        ],
        "cons": [
            "Requires an active Claude Code environment on macOS or Linux",
            "Advanced external ranking metrics (Ahrefs Brand Radar) require optional third-party service credentials"
        ],
        "target_audience": "Software engineers, technical SEO professionals, devops practitioners, and site builders working in Claude Code terminal environments.",
        "comparison_vs_alt": "Unlike desktop GUI crawlers like Screaming Frog that operate outside developer coding environments, Akii embeds directly into the Claude Code terminal, allowing agents to audit code, fix issues, and commit JSON-LD schema in a continuous workflow.",
        "install_command": "claude plugin add akii-technologies-ltd/akii-seo-ai-search-optimizer",
        "date_added": "2026-11-10",
        "featured": True,
        "faqs": [
            {
                "q": "What is Akii: SEO & AI Search Optimizer?",
                "a": "Akii is a free, MIT-licensed Claude Code terminal plugin that audits websites, checks broken links, plans content, generates JSON-LD schema, and estimates AI search visibility."
            },
            {
                "q": "Where does Akii run?",
                "a": "Akii runs directly inside the Claude Code CLI terminal session on macOS and Linux. It does not run a hosted SaaS backend."
            },
            {
                "q": "What are GEO and AEO?",
                "a": "GEO (Generative Engine Optimization) and AEO (Answer Engine Optimization) focus on structuring site data so AI models (like Perplexity, ChatGPT Search, and Google AI Overviews) accurately cite and surface your pages."
            },
            {
                "q": "Is Akii free to use?",
                "a": "Yes, Akii is 100% free and open-source under the MIT license, including 12 skills, 5 agents, and 3 commands."
            }
        ]
    }
]

REVIEWS = {
    "youtranscripts": {
        "article_title": "YouTranscripts Architecture & Utility Dossier: Caption Extraction, Subtitle Formats, and Multilingual AI Summarization",
        "reading_time": "5 min read",
        "editorial_verdict_callout": "YouTranscripts fills an essential productivity niche: zero-friction extraction of YouTube captions into structured research documents, SRT subtitle files, and 17-language AI digests.",
        "chapters": [
            {
                "id": "video-text-bottleneck",
                "number": "01",
                "title": "The Video Knowledge Bottleneck: Extracting Text from Streaming Media",
                "content": (
                    "Video has become the dominant medium for technical tutorials, academic seminars, and executive presentations. "
                    "However, streaming video presents a persistent operational friction for knowledge workers: video content is fundamentally unsearchable, "
                    "difficult to skim, and resistant to automated indexing. Traditional workarounds—running local Whisper transcription models or downloading bloated video binaries—"
                    "impose heavy compute overhead and bandwidth friction. YouTranscripts solves this challenge by interfacing directly with streaming caption tracks, "
                    "retrieving time-coded transcripts within seconds without client-side media downloads."
                )
            },
            {
                "id": "export-formats-srt",
                "number": "02",
                "title": "Multi-Format Ingestion & Subtitle Timing Sync (SRT/PDF/DOCX)",
                "content": (
                    "A critical engineering strength of YouTranscripts is its flexible multi-format export pipeline. Rather than delivering a raw, unformatted text dump, "
                    "the engine parses timestamp metadata into standardized subtitle formats (such as SRT and CSV) suitable for video editors and localization pipelines. "
                    "For researchers and students, the platform formats the transcript into clean document layouts (DOCX, PDF, and plain TXT), stripping redundant conversational fillers "
                    "while preserving logical paragraph breaks and speaker progression."
                )
            },
            {
                "id": "ai-summarization-translation",
                "number": "03",
                "title": "AI Summarization & 17-Language Neural Translation Workflows",
                "content": (
                    "Beyond raw text extraction, YouTranscripts incorporates specialized AI processing routines. Users can trigger dual-mode summaries: quick bulleted takeaways "
                    "for high-level review, or in-depth thematic outlines that synthesize multi-hour discussions into structured sections. Coupled with neural translation across "
                    "17 supported global languages, the platform breaks linguistic boundaries, allowing researchers to ingest and analyze foreign-language educational content with native-level clarity."
                )
            },
            {
                "id": "operational-verdict",
                "number": "04",
                "title": "Practical Workflows for Researchers and Creators & Editorial Verdict",
                "content": (
                    "For independent researchers, digital creators, and students, YouTranscripts provides a high-signal, zero-friction utility that dramatically accelerates video research. "
                    "By combining free core access, multi-format export flexibility, and instant AI summarization, it transforms YouTube from a passive viewing platform into an actionable, "
                    "queryable knowledge library."
                )
            }
        ]
    },
    "orkas": {
        "article_title": "Orkas Architecture & Engineering Dossier: Hierarchical Multi-Agent Teams, Local-First Data Sovereignty, and Document Synthesis",
        "reading_time": "7 min read",
        "editorial_verdict_callout": "Orkas demonstrates the future of desktop AI productivity: a 9,000-star open-source framework where an autonomous Commander orchestrates 16 specialist agents to produce real reports and editable slides without cloud lock-in.",
        "chapters": [
            {
                "id": "multi-agent-workspace",
                "number": "01",
                "title": "The Multi-Agent Workspace: Why Document Synthesis Demands Agent Orchestration",
                "content": (
                    "Single-turn LLM chat interfaces have hit an architectural ceiling when tasked with complex document synthesis. Generating a comprehensive 20-page market analysis "
                    "or an executive slide deck from heterogeneous source materials requires multiple distinct cognitive capabilities: data extraction, statistical verification, "
                    "narrative structuring, visual layout design, and citation management. Forcing a single prompt to execute all these roles invariably results in hallucinations and superficial generalities. "
                    "Orkas addresses this systemic limitation by introducing a modular, desktop-native multi-agent architecture where specialist agents collaborate within a unified workspace."
                )
            },
            {
                "id": "commander-topology",
                "number": "02",
                "title": "The Commander Pattern: Hierarchical Delegation Across 16 Specialist Subagents",
                "content": (
                    "At the core of Orkas is the 'Commander' orchestration engine. When a user presents a high-level goal and project materials (spreadsheets, briefs, research PDFs), "
                    "the Commander decomposes the objective into an interdependent dependency graph. It dynamically delegates subtasks to 16 built-in specialist agents—including Office agents "
                    "for document analysis, Presentation agents for slide generation, and auxiliary coding and media agents for asset processing. Crucially, the Commander maintains global project context "
                    "across iterations, ensuring that data insights identified by research agents directly inform the narrative arguments in generated presentation decks."
                )
            },
            {
                "id": "local-first-data-boundary",
                "number": "03",
                "title": "Local-First Privacy Architecture & Bring-Your-Own-Model (BYOM) Flexibility",
                "content": (
                    "In an era where enterprise data privacy and IP protection are non-negotiable, Orkas stands out through its strict local-first data boundary. By default, all project files, "
                    "intermediate scratchpads, and vector indices reside exclusively on the user's local filesystem. Orkas decouples the desktop client from proprietary cloud backends: "
                    "users can configure local inference runtimes such as Ollama or vLLM to achieve complete offline, air-gapped agentic workflows. For teams desiring frontier cloud intelligence, "
                    "Orkas supports direct API key configuration for commercial providers without routing confidential payloads through intermediate third-party brokers."
                )
            },
            {
                "id": "production-verdict",
                "number": "04",
                "title": "Production Evaluation, Slide Export Fidelity & Editorial Verdict",
                "content": (
                    "Orkas represents a monumental milestone in open-source generative productivity software. With over 9,100 GitHub stars and an active developer community, "
                    "its MIT-licensed architecture provides genuine desktop sovereignty. By outputting fully editable presentations rather than static image renders, Orkas empowers professionals "
                    "to refine and customize AI-generated materials seamlessly. For organizations, researchers, and creators seeking autonomous agent teamwork without compromising data confidentiality, "
                    "Orkas is an essential, high-conviction recommendation."
                )
            }
        ]
    },
    "revenue-scout": {
        "article_title": "Revenue Scout Architecture & Growth Dossier: Omnichannel Social Listening and Semantic Intent Scoring Across 7 Networks",
        "reading_time": "6 min read",
        "editorial_verdict_callout": "Revenue Scout transforms social media noise into qualified sales pipeline by monitoring 7 major networks and matching buyer intent directly to product capabilities.",
        "chapters": [
            {
                "id": "social-selling-shift",
                "number": "01",
                "title": "The Social Selling Shift: From Outbound Spam to Intent-Driven Social Listening",
                "content": (
                    "Cold outbound email and automated LinkedIn connection spam face declining response rates and aggressive spam filtering. Conversely, organic discussions where prospective buyers "
                    "actively seek tool recommendations on Reddit, LinkedIn, and X represent the highest-intent commercial opportunities in modern digital marketing. "
                    "However, manually monitoring hundreds of subreddits, hashtags, and social feeds is operationally unsustainable. Revenue Scout automates this discovery phase, "
                    "operating as an intelligent social listening radar that indexes public conversations across 7 platforms."
                )
            },
            {
                "id": "omnichannel-semantic-matching",
                "number": "02",
                "title": "7-Platform Omnichannel Crawling & Semantic Fit Analysis",
                "content": (
                    "Unlike traditional monitoring tools that rely on crude keyword substring alerts (triggering endless false positives), Revenue Scout employs semantic intent scoring. "
                    "The system indexes public posts from Reddit, LinkedIn, X, Facebook, Instagram, TikTok, and YouTube. When evaluating a thread, the engine cross-references the author's stated problem "
                    "against the subscriber's configured product offerings. It presents the sales team with a synthesized rationale explaining exactly why the discussion constitutes an actionable lead."
                )
            },
            {
                "id": "human-in-the-loop-synthesis",
                "number": "03",
                "title": "Human-in-the-Loop AI Reply Synthesis and Opportunity Scoring",
                "content": (
                    "To prevent brand damage and community alienation caused by automated bot replies, Revenue Scout enforces a strict human-in-the-loop workflow. The platform drafts proposed responses "
                    "tailored to the conversational context of the source thread. Operators can inspect, adjust, and approve drafts before posting manually, ensuring brand authenticity and community compliance. "
                    "With non-expiring credit pools and a generous 2,000-credit free trial, the platform provides risk-free onboarding for early-stage teams."
                )
            },
            {
                "id": "growth-verdict",
                "number": "04",
                "title": "Unit Economics, Lead Conversion Best Practices & Editorial Verdict",
                "content": (
                    "Revenue Scout delivers a pragmatic and commercially viable solution for modern inbound pipeline generation. By consolidating 7 platforms into a single unified stream "
                    "and filtering out irrelevant noise through semantic intent scoring, it enables founders and growth marketers to engage prospects at the exact moment of demand. "
                    "For B2B software and high-value consumer products, it serves as a high-ROI social discovery asset."
                )
            }
        ]
    },
    "akii-seo-ai-search-optimizer": {
        "article_title": "Akii Architecture & Engineering Dossier: Terminal-Native SEO Auditing, JSON-LD Schema Generation, and GEO/AEO Optimization for Claude Code",
        "reading_time": "6 min read",
        "editorial_verdict_callout": "Akii brings technical SEO and modern AI search optimization directly into developer terminal workflows with an open-source Claude Code plugin.",
        "chapters": [
            {
                "id": "terminal-first-seo",
                "number": "01",
                "title": "Terminal-First Optimization: Bringing SEO Auditing into the Claude Code Agent Runtime",
                "content": (
                    "Traditionally, technical SEO auditing and site health verification have lived in isolated GUI desktop applications (such as Screaming Frog) or cloud SaaS dashboards. "
                    "This separation creates significant friction for engineering teams: findings from an external audit must be manually transcribed into developer issue trackers, "
                    "context-switched into IDEs, and resolved days or weeks after initial deployment. Akii eliminates this barrier by packaging comprehensive SEO intelligence "
                    "as an open-source plugin designed natively for the Claude Code CLI environment."
                )
            },
            {
                "id": "plugin-topology",
                "number": "02",
                "title": "Plugin Topology: 12 Skills, 5 Autonomous Agents, and Native Slash Commands",
                "content": (
                    "Akii's architecture leverages the full power of Claude Code's plugin framework. The bundle incorporates 12 modular skills, 5 specialized autonomous agents, "
                    "and 3 ergonomic slash commands. When invoked in a repository, Akii can crawl local staging servers or production domains, detect 404 broken links, inspect canonicalization, "
                    "audit document hierarchies, and analyze competitor page structures. Because it executes within the active coding session, Claude Code can autonomously write the fixes, "
                    "refactor missing metadata, and generate Schema.org compliant JSON-LD graph objects directly into source files."
                )
            },
            {
                "id": "geo-aeo-paradigm",
                "number": "03",
                "title": "The GEO/AEO Paradigm: Preparing Modern Web Architectures for AI-Powered Search",
                "content": (
                    "As generative AI search engines—including Perplexity, ChatGPT Search, and Google AI Overviews—transform how users discover software and technical solutions, "
                    "traditional keyword density strategies are becoming obsolete. Akii addresses the emerging disciplines of Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO). "
                    "The plugin analyzes how LLM synthesis models extract factual entities from a website's semantic markup, providing actionable recommendations to optimize entity graph clarity, "
                    "structured JSON-LD references, and brand citation authority."
                )
            },
            {
                "id": "developer-verdict",
                "number": "04",
                "title": "Open Source Extensibility, Performance Footprint & Editorial Verdict",
                "content": (
                    "Akii: SEO & AI Search Optimizer represents an exemplary developer utility for modern AI agent environments. By delivering 100% free, MIT-licensed source code with zero external telemetry "
                    "or mandatory cloud subscriptions, it respects developer autonomy. For software engineers building Astro, Next.js, or static web architectures who want continuous SEO and GEO verification "
                    "without leaving their command line, Akii is an indispensable addition to the Claude Code toolkit."
                )
            }
        ]
    }
}

def main():
    # 1. Update all_tools.json
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)

    for new_tool in reversed(TOOLS):
        existing_idx = next((i for i, t in enumerate(tools) if t.get("id") == new_tool["id"]), None)
        if existing_idx is not None:
            print(f"Updating existing tool: {new_tool['id']}")
            tools[existing_idx] = new_tool
        else:
            print(f"Prepending new tool: {new_tool['id']}")
            tools.insert(0, new_tool)

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    print(f"all_tools.json updated successfully. Total tools: {len(tools)}")

    # 2. Update editorial_reviews.json
    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    for tool_id, review_data in REVIEWS.items():
        reviews[tool_id] = review_data
        print(f"Added review for: {tool_id}")

    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)
    print("editorial_reviews.json updated successfully.")

if __name__ == "__main__":
    main()
