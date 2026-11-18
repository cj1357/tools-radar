# -*- coding: utf-8 -*-
"""
Process three updates for 2026-11-18:
1. Update existing listing: Revenue Scout (Akii Technologies, GitHub Issue #4)
2. Catalog new tool: OrdoGrid (Innovaplus, contact@ordogrid.com)
3. Catalog new tool: Bitpont (Elizabeth Oricha, partnerships@bitpont.com)
"""

import json
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
all_tools_path = os.path.join(root_dir, "data", "all_tools.json")
reviews_path = os.path.join(root_dir, "data", "editorial_reviews.json")

# -------------------------------------------------------------
# 1. ORDOGRID
# -------------------------------------------------------------
ORDOGRID_TOOL = {
    "id": "ordogrid",
    "name": "OrdoGrid",
    "tagline": "Belgian invoicing and Peppol e-invoicing platform with nine free browser utilities",
    "summary": "OrdoGrid (developed by Innovaplus in Incourt, Belgium) is a compliant invoicing and Peppol e-invoicing management platform engineered for Belgian and European businesses, freelancers, and accounting workflows. It provides native Peppol access point integration for sending and receiving structured e-invoices, complemented by nine public browser utilities (for invoice and quote drafts, Belgian VAT verification, UBL XML parsing, payment QR/OGM generation, and Peppol participant lookup) that require zero account registration. Paid tiers unlock recurring invoicing, time tracking, reviewed bank-file reconciliation, API access, and human-in-the-loop AI metadata extraction from readable supplier PDFs.",
    "url": "https://ordogrid.com/en",
    "github_url": "",
    "source": "submission",
    "category": "productivity",
    "tags": [
        "Invoicing",
        "Peppol",
        "Belgium",
        "E-Invoicing",
        "Browser Utilities",
        "VAT",
        "UBL",
        "Accounting"
    ],
    "pricing_model": "Freemium",
    "stars": 0,
    "primary_alternative": "Bonsai",
    "is_self_hostable": False,
    "no_signup_required": False,
    "signal_score": 86,
    "verdict": "A transparent, compliance-focused European invoicing and Peppol hub pairing robust automated business workflows with nine completely free client-side utilities.",
    "deployment_format": "Cloud SaaS & Web Utilities",
    "install_command": "Access web portal at https://ordogrid.com/en",
    "date_added": "2026-11-18",
    "featured": True,
    "key_features": [
        {
            "title": "Nine Public Browser Invoicing & VAT Utilities",
            "description": "Free, no-account web tools for invoice/quote drafting, Belgian VAT computation, UBL parsing, payment QR/OGM generation, due dates, and Peppol directory lookups."
        },
        {
            "title": "Native Peppol E-Invoicing Network Integration",
            "description": "Direct Peppol access point connectivity enabling automated reception of structured B2B/B2G electronic invoices and compliant outbound delivery."
        },
        {
            "title": "Recurring Invoicing, Projects & Time Tracking",
            "description": "Streamlined operational suite with automated scheduled billing, project hour logging, and bank statement reconciliation."
        },
        {
            "title": "Human-in-the-Loop AI Supplier-PDF Ingestion",
            "description": "Extracts proposed dates, parties, amounts, and references from readable supplier PDFs for manual verification against original documents."
        }
    ],
    "use_cases": [
        "Belgian small businesses, freelancers, and agencies transitioning to mandatory Peppol B2B electronic invoicing.",
        "European accounting professionals needing quick, client-side UBL document validation and Peppol participant lookups without software installation.",
        "Growing businesses automating recurring client billings, project time tracking, and bank reconciliation."
    ],
    "pros": [
        "Nine genuinely free public browser utilities accessible without registration or credit card",
        "Permanent Free tier includes unlimited inbound Peppol invoices and 1 outgoing invoice/month with 1 GB storage",
        "Strict European data residency and transparent compliance alignment for Belgian tax regulations",
        "Human-in-the-loop AI invoice ingestion avoids unchecked autonomous accounting errors"
    ],
    "cons": [
        "Proprietary cloud platform without on-premises self-hosted Docker packages",
        "AI invoice import requires text-readable PDFs (no textless image scan OCR or automated line-item bookkeeping approval)"
    ],
    "target_audience": "Belgian and European business owners, independent consultants, freelancers, and accounting teams managing e-invoicing and Peppol compliance.",
    "comparison_vs_alt": "Unlike generic US-centric invoicing tools like Bonsai or Wave that lack European Peppol network integration and localized Belgian VAT/OGM tooling, OrdoGrid is built from the ground up for EU electronic invoicing standards.",
    "faqs": [
        {
            "q": "What is OrdoGrid and what does it do?",
            "a": "OrdoGrid is a Belgian invoicing and Peppol e-invoicing platform designed for European freelancers, companies, and accountants. It facilitates structured e-invoice delivery through the international Peppol network, automates recurring billing and bank reconciliation, and offers nine free browser-based financial utilities."
        },
        {
            "q": "What free utilities does OrdoGrid provide without an account?",
            "a": "OrdoGrid hosts nine public, registration-free browser tools at https://ordogrid.com/en/tools, including invoice and quote drafters, Belgian VAT validators, UBL XML readers, payment QR/OGM generators, due date calculators, and Peppol directory participant lookups."
        },
        {
            "q": "How does OrdoGrid support the Peppol e-invoicing standard?",
            "a": "OrdoGrid integrates directly with the Peppol electronic delivery network. Even on the permanent Free plan, users can receive an unlimited volume of inbound Peppol invoices and transmit one outgoing invoice per month."
        },
        {
            "q": "What are the pricing tiers and limits?",
            "a": "The permanent Free tier includes unlimited Peppol inbound invoices, 1 outbound invoice/month, 1 user, and 1 GB storage. Paid tiers include Starter (EUR 9/month excluding VAT for recurring invoicing) and Business (EUR 59/month excluding VAT for time tracking, bank reconciliation, and API access)."
        },
        {
            "q": "How does the AI supplier-PDF invoice ingestion work?",
            "a": "On the Business plan, OrdoGrid's AI scans readable text from supplier PDFs to propose vendor names, dates, amounts, and payment references. To ensure complete auditability, the system requires human verification against the original document and does not automatically approve bookkeeping records."
        }
    ]
}

ORDOGRID_REVIEW = {
    "article_title": "OrdoGrid Architecture & Compliance Dossier: Peppol E-Invoicing, Belgian VAT Synthesis, and Client-Side Financial Utilities",
    "reading_time": "6 min read",
    "editorial_verdict_callout": "OrdoGrid delivers an exceptionally grounded, transparent accounting platform: bridging modern Belgian and EU Peppol compliance with high-utility client-side browser tools and audit-safe human-in-the-loop AI invoice parsing.",
    "chapters": [
        {
            "id": "european-peppol-mandate-operational-shift",
            "number": "01",
            "title": "The European Peppol Mandate: Navigating the Structural Shift from PDFs to Structured XML",
            "content": "Across the European Union—and specifically within Belgium—business-to-business (B2B) and business-to-government (B2G) transactions are undergoing an unprecedented regulatory transformation: the statutory mandate of structured electronic invoicing via the Pan-European Public Procurement On-Line (Peppol) network. For decades, small businesses and independent contractors relied on unstructured email attachments, primarily static PDF files and scanned paper documents. While readable by humans, PDFs require fragile OCR routines or manual data entry to ingest into ERP software. The Peppol standard mandates structured Universal Business Language (UBL) XML documents transmitted through certified Access Points, ensuring instantaneous machine readability and cryptographic non-repudiation. OrdoGrid was engineered specifically to abstract this protocol complexity, providing Belgian enterprises with native Access Point routing without requiring enterprise-grade middleware."
        },
        {
            "id": "ordogrid-architecture-nine-client-utilities",
            "number": "02",
            "title": "OrdoGrid Dual-Layer Architecture: SaaS Business Core and Nine Zero-Friction Web Utilities",
            "content": "Architecturally, OrdoGrid adopts a dual-layer product model. At its base layer, it offers a suite of nine public, completely unauthenticated browser utilities hosted at ordogrid.com/en/tools. These micro-tools address localized compliance bottlenecks: validating Belgian enterprise numbers (BCE/KBO), computing localized VAT schedules, parsing and validating UBL XML invoice trees, formatting Belgian structured communication (OGM/VCS) codes, and querying the central Peppol Directory for recipient participant identifiers. Crucially, these utilities process sensitive business identifiers on the client side, serving as a zero-barrier trust anchor. Above this public utility layer sits OrdoGrid's secure multi-tenant cloud application, handling stateful workflows including recurring invoice schedules, project time attribution, bank statement reconciliation, and REST API access."
        },
        {
            "id": "human-in-the-loop-ai-invoice-ingestion",
            "number": "03",
            "title": "Pragmatic Machine Intelligence: Human-in-the-Loop Document Parsing vs Autonomous Bookkeeping Pitfalls",
            "content": "A prominent failure mode in modern fintech SaaS is over-promising on autonomous artificial intelligence—purporting to replace accountants with unchecked autonomous bookkeeping bots. In reality, accounting standards and tax audits demand absolute zero-tolerance for hallucinated line items, misplaced decimal points, or misattributed VAT exemptions. OrdoGrid's approach to machine learning is refreshingly pragmatic: its Business-tier AI import engine parses readable text layers from supplier PDF invoices to suggest candidate metadata (supplier entities, transaction dates, total amounts, and structured payment references). Crucially, the system requires mandatory side-by-side human inspection against the original document, refusing to post automatic ledger approvals. By explicitly acknowledging the boundaries of optical extraction—omitting brittle textless OCR for degraded scans—OrdoGrid guarantees that human accountants retain definitive compliance authority."
        },
        {
            "id": "cost-economics-compliance-verdict",
            "number": "04",
            "title": "Cost Economics, Peppol Access Point Guarantees & Production Deployment Verdict",
            "content": "From an economic standpoint, OrdoGrid's pricing structure lowers the barrier to regulatory compliance. The permanent Free account guarantees that even micro-enterprises can receive unlimited inbound Peppol invoices and issue one outbound e-invoice monthly at zero software licensing cost. For growing teams, the Starter tier (EUR 9/month excl. VAT) and Business tier (EUR 59/month excl. VAT) scale predictably without per-invoice transaction tax penalties. Bootstrapped in Incourt, Belgium, the vendor operates with complete European data residency, adhering to strict GDPR obligations. In conclusion, OrdoGrid provides an exemplary regional software solution: combining uncompromised Peppol compliance, ergonomic browser tools, and disciplined, audit-ready AI workflows."
        }
    ],
    "tool_id": "ordogrid",
    "model_used": "editorial-team",
    "generated_at": "2026-11-18T03:00:00.000000+00:00"
}

# -------------------------------------------------------------
# 2. BITPONT
# -------------------------------------------------------------
BITPONT_TOOL = {
    "id": "bitpont",
    "name": "Bitpont",
    "tagline": "Wallet-connected onchain finance interface and public market-data API",
    "summary": "Bitpont is a non-custodial onchain finance interface and market-data platform that unifies decentralized swaps, cross-chain bridges, borrowing, yield management, and treasury workflows into a single dashboard. Users authorize all operations directly through their own self-custody Web3 wallets, maintaining complete asset sovereignty. Complementing the retail interface, Bitpont provides developer documentation, an OpenAPI specification, and a free public market-data REST API with documented access limits, enabling developers and automated financial applications to programmatically query asset pricing, liquidity pools, and yield telemetry.",
    "url": "https://www.bitpont.com/",
    "github_url": "",
    "source": "submission",
    "category": "developer-tools",
    "tags": [
        "Onchain Finance",
        "Public API",
        "DeFi",
        "Web3",
        "Market Data",
        "OpenAPI",
        "Developer Tools",
        "Treasury"
    ],
    "pricing_model": "Freemium",
    "stars": 0,
    "primary_alternative": "DeFiLlama",
    "is_self_hostable": False,
    "no_signup_required": True,
    "signal_score": 87,
    "verdict": "A transparent, non-custodial financial gateway and market-data API bringing unified asset execution and telemetry to Web3 developers and treasury operators.",
    "deployment_format": "Web Application & Public REST API",
    "install_command": "Explore API specs at https://www.bitpont.com/developers/",
    "date_added": "2026-11-18",
    "featured": True,
    "key_features": [
        {
            "title": "Unified Onchain Financial Operations",
            "description": "Integrates swaps, cross-chain bridging, collateralized borrowing, yield strategies, and portfolio tracking into one dashboard."
        },
        {
            "title": "Non-Custodial Wallet Authorization",
            "description": "All transactions and contract interactions are signed and authorized exclusively by the user's self-custody wallet."
        },
        {
            "title": "Public Market-Data API & OpenAPI Spec",
            "description": "Documented REST endpoints providing public market reads, asset telemetry, and developer integration specs."
        },
        {
            "title": "Multi-Protocol Yield & Treasury Workflows",
            "description": "Tracks treasury balances, protocol health, and decentralized liquidity across supported blockchain networks."
        }
    ],
    "use_cases": [
        "DeFi developers and algorithmic builders integrating live market data, swap rates, and yield telemetry via Bitpont's OpenAPI specification.",
        "Web3 treasury managers and crypto-native organizations monitoring collateralized positions, yield generation, and multi-asset rebalancing.",
        "Onchain finance users seeking an all-in-one wallet-connected terminal for swaps and bridging without juggling disparate dApp frontends."
    ],
    "pros": [
        "Free public market-data API access available under documented rate limits with standard OpenAPI specifications",
        "Strictly non-custodial architecture ensures private keys and funds remain in user control",
        "Consolidates multiple disparate DeFi primitives (swap, bridge, lend, yield) into a coherent interface",
        "Transparent fee schedule detailing interface, provider, and onchain network costs upfront"
    ],
    "cons": [
        "Onchain protocol operations remain subject to underlying decentralized smart contract risks and network gas fees",
        "High-throughput commercial API consumers must establish custom partner configurations beyond public tiers"
    ],
    "target_audience": "Web3 developers, decentralized financial engineers, crypto treasury managers, and onchain asset operators.",
    "comparison_vs_alt": "While platforms like DeFiLlama focus primarily on macro analytics without native transaction execution, and aggregators like 1inch focus narrowly on DEX swaps, Bitpont combines interactive wallet-executed DeFi workflows with developer-accessible market-data APIs.",
    "faqs": [
        {
            "q": "What is Bitpont and how does it work?",
            "a": "Bitpont is a wallet-connected onchain finance interface and public developer API. It unifies decentralized token swaps, cross-chain bridges, borrowing, yield vaults, and portfolio management into a consolidated interface, while exposing public market-data endpoints for developers."
        },
        {
            "q": "How does the non-custodial wallet model protect user funds?",
            "a": "Bitpont never takes custody of user assets or private keys. Every transaction (such as a swap, bridge transfer, or collateral deposit) is cryptographically signed and executed directly through the user's connected Web3 wallet against underlying onchain protocols."
        },
        {
            "q": "What is included in Bitpont's public developer API?",
            "a": "Bitpont provides developer documentation, an OpenAPI specification, and free public market-data read endpoints at https://www.bitpont.com/developers/. Developers can inspect supported networks, token prices, liquidity metrics, and route parameters."
        },
        {
            "q": "How are fees structured for operations and API access?",
            "a": "Limited public market-data reads are free under documented access limits. Execution operations may incur standard provider routing, interface, and onchain blockchain network gas fees, detailed transparently at https://www.bitpont.com/fees/. Extended enterprise API quotas are configured on a partner basis."
        },
        {
            "q": "What onchain workflows are supported?",
            "a": "Bitpont supports decentralized token swaps, cross-chain asset bridging, collateralized lending/borrowing, staking/yield strategies, and multi-wallet treasury balance tracking across major EVM and supported blockchain networks."
        }
    ]
}

BITPONT_REVIEW = {
    "article_title": "Bitpont Architecture & Financial Engineering Dossier: Non-Custodial Multi-Protocol Execution, OpenAPI Infrastructure, and Treasury Workflows",
    "reading_time": "6 min read",
    "editorial_verdict_callout": "Bitpont brings disciplined software engineering and transparent API telemetry to onchain finance: unifying fragmented DeFi primitives behind self-custody wallet signatures and documented OpenAPI specifications.",
    "chapters": [
        {
            "id": "onchain-fragmentation-and-developer-interface",
            "number": "01",
            "title": "Onchain Fragmentation: The Operational Cost of Disparate DeFi Protocols and Isolated Interfaces",
            "content": "The decentralized finance (DeFi) ecosystem has produced remarkably resilient liquidity primitives—from automated market maker (AMM) decentralized exchanges to collateralized debt markets and cross-chain message-passing bridges. However, this hyper-specialization has inflicted severe operational fragmentation upon both end users and software developers. A treasury manager seeking to rebalance capital must routinely navigate half a dozen disparate decentralized application (dApp) frontends, reconcile incompatible user interfaces, manage separate slippage settings, and track assets across non-interoperable analytics dashboards. For developers building financial automations, the friction is compounded by inconsistent RPC endpoints, disparate indexing schemas, and undocumented payload formats. Bitpont was architected to resolve this friction by unifying onchain finance workflows into a single interface backed by standard OpenAPI developer specifications."
        },
        {
            "id": "non-custodial-security-execution-model",
            "number": "02",
            "title": "Non-Custodial Architecture: Self-Custody Signature Enclaves and Smart Contract Direct Routing",
            "content": "From a security and compliance perspective, the central tenet of Bitpont's system design is strict non-custodial integrity. Centralized exchange blowups throughout crypto history have repeatedly demonstrated the existential hazards of vendor asset custody. Bitpont never manages deposit accounts, holds private keys, or operates internal offchain balance sheets. When a user initiates a transaction—whether an asset swap, a cross-chain liquidity bridge, or a collateralized borrowing position—Bitpont compiles the required calldata and routes it directly to the user's connected Web3 wallet. The user reviews network fees, contract allowances, and execution payloads within their hardware or software signature enclave before authorizing the onchain transaction. By keeping execution direct to immutable protocol smart contracts, Bitpont ensures counterparty risk remains entirely contained."
        },
        {
            "id": "openapi-specification-and-market-data-telemetry",
            "number": "03",
            "title": "Developer Telemetry: Public Market-Data Reads and the Bitpont OpenAPI Specification",
            "content": "Beyond its end-user web dashboard, Bitpont provides dedicated infrastructure for quantitative developers and automated financial agents through its developer portal at bitpont.com/developers/. Rather than relying on proprietary, closed SDKs, Bitpont publishes an OpenAPI specification that allows engineering teams to generate typed client libraries across TypeScript, Python, and Go in seconds. Developers can query public market-data read endpoints—including token pair pricing, liquidity depth, routing quotes, and historical pool yields—under generous, documented rate limits without upfront commercial contracts. For enterprise partners, algorithmic liquidity aggregators, and fintech backends, Bitpont provides extended throughput tiers with dedicated telemetry channels."
        },
        {
            "id": "treasury-workflows-and-strategic-verdict",
            "number": "04",
            "title": "Treasury Portfolio Operations, Fee Transparency & Enterprise Production Verdict",
            "content": "In assessing total operational utility, Bitpont distinguishes itself through fee transparency. The platform documents all transaction costs—including provider routing spreads, interface fees, and onchain network gas charges—upfront at bitpont.com/fees/, eliminating the hidden slippage that plagues opaque aggregators. For crypto-native foundations, decentralized autonomous organizations (DAOs), and Web3 startups, Bitpont's consolidated treasury dashboard provides holistic visibility into multi-chain assets, active borrow ratios, and yield accrual from a unified vantage point. While users remain accountable for underlying smart contract vulnerabilities in third-party protocols, Bitpont delivers a premier non-custodial control plane and developer API gateway that significantly elevates the standard of onchain financial software."
        }
    ],
    "tool_id": "bitpont",
    "model_used": "editorial-team",
    "generated_at": "2026-11-18T03:15:00.000000+00:00"
}

# -------------------------------------------------------------
# 3. REVENUE SCOUT UPDATE
# -------------------------------------------------------------
def update_revenue_scout(tools, reviews):
    found = False
    for t in tools:
        if t.get("id") == "revenue-scout":
            # Refresh tagline as requested
            t["tagline"] = "Your Agentic Coworker for sales prospecting"
            
            # Refresh summary with workflow details
            t["summary"] = (
                "Revenue Scout is your AI-powered agentic coworker for sales prospecting that monitors public posts "
                "across 7 major networks: Reddit, LinkedIn, X, Facebook, Instagram, TikTok, and YouTube. Moving beyond "
                "blunt keyword scraping, Scout utilizes semantic understanding to evaluate buyer intent against your specific "
                "product catalog. When a customer asks for a reply draft, Scout uses that lead and related search results to explore "
                "better search phrases, keeping enabled saved phrases active. Customers review, edit, and post social replies manually, "
                "while Gmail sends require separate approval. Every plan, including Free, includes all features, team collaboration, "
                "and all seven platforms, differing solely by credit capacity."
            )
            
            # Update cons to correct paid team features note
            t["cons"] = [
                "Paid plans start at $49/month for higher credit capacity; all tiers (including Free) include team collaboration and all 7 platforms",
                "Requires careful onboarding prompt definition to avoid surfacing adjacent low-intent mentions"
            ]
            
            # Update FAQs
            t["faqs"] = [
                {
                    "q": "What is Revenue Scout?",
                    "a": "Revenue Scout is an AI-powered agentic coworker for sales prospecting that monitors discussions across Reddit, LinkedIn, X, Facebook, Instagram, TikTok, and YouTube to find high-intent buyers and draft personalized replies."
                },
                {
                    "q": "How does the search phrase exploration and reply workflow work?",
                    "a": "When you ask for a reply draft, Scout uses that lead and related search results to explore better search phrases, keeping enabled saved phrases continuously active. Customers review, edit, and post social replies manually, and Gmail outreach sends require separate approval."
                },
                {
                    "q": "Which social platforms are covered?",
                    "a": "Revenue Scout indexes public discussions across all 7 major platforms: Reddit, LinkedIn, X, Facebook, Instagram, TikTok, and YouTube."
                },
                {
                    "q": "What is the pricing model and plan differences?",
                    "a": "Every plan, including Free, includes all features, team collaboration, and access to all seven platforms. Each verified customer receives 2,000 free welcome credits once with no credit card required. Paid plans start at $49/month for higher credit capacity, with non-expiring credit top-ups starting at $15."
                }
            ]
            found = True
            break
            
    if found:
        print("Updated Revenue Scout in all_tools.json")
    else:
        print("Warning: revenue-scout not found in all_tools.json")

def main():
    # Load all_tools.json
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # 1. Update Revenue Scout
    update_revenue_scout(tools, None)

    # 2. Add OrdoGrid and Bitpont (insert at top, positions 1 and 2)
    tools = [t for t in tools if t.get("id") not in ["ordogrid", "bitpont"]]
    tools.insert(1, ORDOGRID_TOOL)
    tools.insert(2, BITPONT_TOOL)

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    print(f"Catalog updated. Total tools in all_tools.json: {len(tools)}")

    # Load editorial_reviews.json
    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews["ordogrid"] = ORDOGRID_REVIEW
    reviews["bitpont"] = BITPONT_REVIEW

    # Also update revenue-scout review callout/title if needed
    if "revenue-scout" in reviews:
        reviews["revenue-scout"]["editorial_verdict_callout"] = (
            "Revenue Scout establishes an authentic agentic coworker for sales prospecting: transforming multi-platform "
            "social discussions across 7 networks into actionable pipeline with human-in-the-loop reply verification."
        )

    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)
    print(f"Reviews updated. Total reviews in editorial_reviews.json: {len(reviews)}")

if __name__ == "__main__":
    main()
