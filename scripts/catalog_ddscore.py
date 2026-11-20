# -*- coding: utf-8 -*-
"""
Catalog DDScore (Issue #8) into all_tools.json and editorial_reviews.json.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
all_tools_file = os.path.join(BASE_DIR, 'data', 'all_tools.json')
editorial_file = os.path.join(BASE_DIR, 'data', 'editorial_reviews.json')

DDSCORE_TOOL = {
    "id": "ddscore",
    "name": "DDScore",
    "tagline": "AI-powered first-pass due diligence and multi-document cross-checker for investors and founders",
    "summary": "DDScore is an AI-powered first-pass due diligence platform engineered for venture capital funds, angel investors, family offices, and startup founders. The platform cross-checks submitted pitch decks, operational spreadsheets, financial models, and supporting documents against both internal consistency standards and external market intelligence. Evaluating private companies across 12 analytical dimensions—from team pedigree and unit economics to competitive moat and exit viability—DDScore produces an empirical 0–100 investment readiness score alongside targeted diligence questions derived from conflicting or absent evidentiary claims.",
    "url": "https://www.ddscore.ai/",
    "github_url": "",
    "source": "submission",
    "category": "ai-tools",
    "tags": [
        "Due Diligence",
        "Venture Capital",
        "Financial Analysis",
        "AI Agents",
        "Document Intelligence",
        "Fundraising",
        "Startup Tools"
    ],
    "pricing_model": "Paid",
    "stars": 0,
    "primary_alternative": "PitchBook",
    "is_self_hostable": False,
    "no_signup_required": False,
    "signal_score": 86,
    "verdict": "A rigorous, multi-document due diligence intelligence engine that transforms manual investor document review into a structured, evidence-audited risk evaluation.",
    "deployment_format": "Web Application & Cloud Service",
    "extensibility": "Web Dashboard & Exportable Diligence Dossiers",
    "install_command": "Explore live sample reports and plans at https://www.ddscore.ai/",
    "date_added": "2026-11-20",
    "featured": False,
    "key_features": [
        {
            "title": "Multi-Document Evidentiary Cross-Checking",
            "description": "Reconciles pitch deck projections, financial models, cap tables, and legal disclosures against each other and public registry benchmarks to detect anomalies."
        },
        {
            "title": "12-Dimension Quantitative Risk Scoring",
            "description": "Calculates an empirical 0–100 score evaluating unit economics, TAM credibility, competitive moats, governance, and exit liquidity scenarios."
        },
        {
            "title": "Gap-Driven Diligence Question Generation",
            "description": "Automatically formulates targeted interrogation questions for founder interviews based on missing disclosures or conflicting metrics."
        },
        {
            "title": "Accelerated First-Pass Screening",
            "description": "Compresses 20+ hours of initial document triage into structured executive dossiers, allowing investment committees to focus human time on high-conviction deals."
        }
    ],
    "use_cases": [
        "Venture capital analysts and angel syndicates conducting fast, objective first-pass triage across inbound pitch decks and financial disclosures.",
        "Startup founders stress-testing their fundraising decks and financial assumptions before presenting to institutional investors.",
        "Accelerators and M&A advisory teams verifying private company claims and operational metrics against external market research."
    ],
    "pros": [
        "Deep multi-document cross-referencing identifies hidden discrepancies between decks, models, and public records",
        "12-pillar quantitative methodology standardizes first-pass deal screening across investment committees",
        "Concrete audit trail flags specific missing evidence and generates surgical diligence questions",
        "Significantly accelerates document analysis without relying on brittle, single-prompt LLM wrappers"
    ],
    "cons": [
        "Paid enterprise utility geared toward professional investors, accelerators, and active fundraising founders",
        "Proprietary cloud platform without self-hosted local model deployment"
    ],
    "target_audience": "Venture capital firms, angel investors, family offices, M&A teams, accelerators, and startup founders seeking structured due diligence.",
    "comparison_vs_alt": "While legacy platforms like PitchBook provide retrospective market data and general LLMs offer superficial text summaries, DDScore combines multi-model reasoning to cross-examine specific company documents, reconcile conflicting claims, and benchmark against live market evidence.",
    "faqs": [
        {
            "q": "What is DDScore and how does it assist private equity due diligence?",
            "a": "DDScore is an automated first-pass due diligence engine designed for investors and founders. It analyzes pitch decks, financial models, cap tables, and external data across 12 dimensions to produce a 0–100 readiness score, risk heatmaps, and evidence-gap inquiries."
        },
        {
            "q": "How does DDScore cross-check documents?",
            "a": "DDScore utilizes specialized analytical models alongside frontier LLMs to cross-verify claims made in pitch decks against spreadsheets, financial statements, and external public sources, isolating irreconcilable metrics or unbacked assertions."
        },
        {
            "q": "Is DDScore intended to replace human due diligence?",
            "a": "No. DDScore is built to augment human investment teams by handling initial document triage and flagging evidence gaps, allowing investors and founders to focus their diligence meetings on critical, high-risk points."
        },
        {
            "q": "What pricing options are available?",
            "a": "DDScore operates on a paid plan tier structured around analysis volume and report depth, with details published at https://app.ddscore.ai/pricing."
        }
    ]
}

DDSCORE_REVIEW = {
    "article_title": "DDScore Architectural Dossier: Multi-Document Cross-Verification, 12-Dimensional Risk Modeling, and Augmented Venture Diligence",
    "reading_time": "6 min read",
    "editorial_verdict_callout": "DDScore demonstrates how domain-specialized AI orchestration can transcend generic chatbot summaries—synthesizing complex private company disclosures into structured, evidence-audited investment dossiers.",
    "chapters": [
        {
            "id": "the-diligence-bottleneck-and-information-asymmetry",
            "number": "01",
            "title": "The Venture Diligence Bottleneck: Information Asymmetry and the Friction of Manual First-Pass Screening",
            "content": "Early-stage private company investing has historically suffered from acute information asymmetry and high operational friction. An investment team evaluating an inbound deal must dissect narrative claims in pitch decks, reconcile dynamic assumptions across spreadsheet financial models, verify cap table distributions, and cross-reference competitor trajectories. In high-velocity venture funds reviewing hundreds of inbound decks per quarter, analysts are often constrained to superficial 15-minute deck scans, leaving subtle inconsistencies between pitch narratives and cash-flow spreadsheets undiscovered until late-stage confirmatory audits. Conversely, early-stage founders frequently enter high-stakes fundraising rounds without objective feedback regarding which evidence gaps or metric discrepancies will trigger immediate investor hesitation. DDScore was built to eliminate this initial friction through automated, evidence-grounded first-pass diligence."
        },
        {
            "id": "algorithmic-multi-document-cross-checking",
            "number": "02",
            "title": "Algorithmic Cross-Verification: Reconciling Pitch Decks, Financial Spreadsheets, and Public Records",
            "content": "A fundamental vulnerability of generic frontier large language models (such as raw ChatGPT or Claude prompts) in financial analysis is hallucination and the inability to maintain multi-document relational coherence. Generic models can summarize individual PDF decks competently, but they struggle to systematically cross-examine a narrative customer acquisition claim against a multi-tab Excel cohort schedule. DDScore addresses this challenge by coupling specialized analytical parsing models with frontier LLM orchestration. When a company's data room materials are ingested, the system extracts claims into structured semantic and numerical nodes, evaluating internal coherence across documents while simultaneously pinging live external business registers, industry benchmarks, and competitive intelligence databases. If a pitch deck claims an $80M ARR target while the operating model shows flat net revenue retention and contradictory headcount hiring assumptions, DDScore flags the divergence with exact citation boundaries."
        },
        {
            "id": "twelve-pillar-quantitative-scoring",
            "number": "03",
            "title": "The 12-Pillar Analytical Framework: Quantitative Risk Scoring and Gap-Driven Inquiry Generation",
            "content": "To deliver standardized, comparable evaluations across diverse market sectors, DDScore evaluates every company across twelve rigorous structural dimensions: business model clarity, founder pedigree and team balance, market size and TAM defensibility, competitive positioning, unit economics, go-to-market velocity, financial projections, customer validation, technological defensibility, regulatory risks, cap table hygiene, and potential exit liquidity pathways. The platform aggregates these findings into an empirical 0–100 DDScore calibrated against stage-specific benchmarks (such as Pre-Seed, Seed, or Series A). Crucially, the platform does not merely output a scalar grade; it synthesizes a comprehensive audit trail of findings categorized by severity and automatically compiles surgical question sets tied to unbacked assertions. Investment analysts and partner committees can directly integrate these generated inquiries into subsequent founder partner meetings."
        },
        {
            "id": "human-in-the-loop-verdict-and-production-utility",
            "number": "04",
            "title": "Augmented Diligence Verdict: Integrating First-Pass Algorithmic Audits with Human Investment Committees",
            "content": "In assessing production viability for venture capital funds, angel syndicates, accelerators, and corporate M&A advisors, DDScore establishes a well-defined boundary between automated triage and final fiduciary judgment. The tool is designed explicitly as an augmented intelligence layer rather than an autonomous decision-maker: it automates the laborious 15-to-20 hours of initial document cross-referencing so human partners can concentrate their qualitative time on founder psychology, vision, and strategic instinct. For early-stage founders, running a pre-emptive DDScore report offers an indispensable pre-flight diagnostic to discover narrative flaws before formal investor roadshows. As private markets increasingly embrace institutional data-driven operations, DDScore exemplifies how specialized multi-document intelligence significantly elevates the baseline rigor of capital allocation."
        }
    ],
    "tool_id": "ddscore",
    "model_used": "editorial-team",
    "generated_at": "2026-11-20T17:08:00.000000+00:00"
}

def catalog():
    # 1. Update all_tools.json
    with open(all_tools_file, 'r', encoding='utf-8') as f:
        tools = json.load(f)

    # Remove existing if any
    tools = [t for t in tools if t.get('id') != 'ddscore']
    # Insert at top (position 0 or 1)
    tools.insert(0, DDSCORE_TOOL)

    with open(all_tools_file, 'w', encoding='utf-8') as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: Cataloged DDScore into all_tools.json (Total tools: {len(tools)})")

    # 2. Update editorial_reviews.json
    with open(editorial_file, 'r', encoding='utf-8') as f:
        reviews = json.load(f)

    reviews['ddscore'] = DDSCORE_REVIEW

    with open(editorial_file, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: Added DDScore 4-chapter architectural dossier into editorial_reviews.json")

if __name__ == '__main__':
    catalog()
