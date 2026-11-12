# -*- coding: utf-8 -*-
"""
Add MySafeInfo Test Data Generator to all_tools.json and editorial_reviews.json
Submitted by Matt Pavey <paveymk@gmail.com> on 2026-11-12
"""

import json
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
all_tools_path = os.path.join(root_dir, "data", "all_tools.json")
reviews_path = os.path.join(root_dir, "data", "editorial_reviews.json")

MYSAFEINFO_TOOL = {
    "id": "mysafeinfo-test-data-generator",
    "name": "MySafeInfo Test Data Generator",
    "tagline": "Generate repeatable relational test data and linked tables in your browser (CSV, Excel, JSON, SQL)",
    "summary": "MySafeInfo Test Data Generator is a zero-friction browser-based developer utility designed to generate realistic, coordinated mock datasets with relational integrity across multiple tables. Built specifically to eliminate the friction of writing throwaway seed scripts or manually synchronizing mock spreadsheets, it automatically creates linked records across Customers, Orders, Order Lines, and Products with consistent IDs, correct mathematical totals, and configurable schemas. Developers and QA engineers can export up to 5,000 rows per table for free without an account into multi-sheet Excel workbooks, zipped CSV files, structured JSON, or DDL-compliant SQL scripts, with optional dirty data injection to stress-test data ingestion and cleansing pipelines.",
    "url": "https://mysafeinfo.com/tools/test-data-generator",
    "github_url": "",
    "source": "submission",
    "category": "testing-qa",
    "tags": [
        "Test Data",
        "Mock Data",
        "Database Testing",
        "SQL Generation",
        "CSV Export",
        "Excel Export",
        "QA Tooling",
        "Developer Tools"
    ],
    "pricing_model": "Freemium",
    "stars": 0,
    "primary_alternative": "Mockaroo",
    "is_self_hostable": False,
    "no_signup_required": True,
    "signal_score": 84,
    "verdict": "An exceptional browser-native mock data generator that solves the multi-table relational consistency problem, providing up to 5,000 rows per table with zero signup friction and versatile SQL, Excel, and JSON exports.",
    "key_features": [
        {
            "title": "Linked Multi-Table Relational Integrity",
            "description": "Coordinated generation across Customers, Orders, Order Lines, and Products with consistent primary/foreign keys, calculated order totals, and quantity alignment."
        },
        {
            "title": "Versatile Multi-Format Export",
            "description": "Download datasets as multi-sheet Excel workbooks (.xlsx), zipped CSV bundles, structured JSON, or executable SQL scripts complete with table schemas and constraints."
        },
        {
            "title": "Dirty Data Injection & Answer Key",
            "description": "Optionally introduce controlled messy data into CSV/Excel exports with an answer key to stress-test data ingestion parsers, sanitizers, and ETL validation pipelines."
        }
    ],
    "use_cases": [
        "Database administrators and backend engineers needing populated development and staging databases with valid relational foreign keys.",
        "QA engineers and software testers evaluating data import routines, ETL transformations, and edge-case handling against realistic data with intentional anomalies.",
        "Product managers, UX designers, and sales engineers seeking believable demo datasets and multi-sheet Excel workbooks for client walkthroughs."
    ],
    "pros": [
        "Generates up to 5,000 rows per table completely free in the browser with zero account creation required",
        "Solves the relational synchronization problem between parent and child tables (e.g. Customers -> Orders -> Line Items)",
        "Exports clean SQL DDL and INSERT statements alongside multi-sheet Excel and zipped CSVs",
        "Includes optional messy data injection specifically tailored for testing data cleansing and validation logic"
    ],
    "cons": [
        "Proprietary client-side web application without open-source self-hosting options for air-gapped CI environments",
        "High-volume enterprise datasets exceeding 5,000 rows per table require purchasing a paid Data Pass"
    ],
    "target_audience": "QA engineers, full-stack developers, database architects, and data engineers looking for fast, coherent, and repeatable mock relational datasets without writing custom seed scripts.",
    "comparison_vs_alt": "While Mockaroo limits free generation to 1,000 rows and requires complex custom formulas to link multiple tables, MySafeInfo provides 5,000 free rows per table with out-of-the-box relational coherence and built-in dirty data testing capabilities.",
    "install_command": "Generate test datasets online at https://mysafeinfo.com/tools/test-data-generator",
    "date_added": "2026-11-12",
    "featured": False,
    "faqs": [
        {
            "q": "What is MySafeInfo Test Data Generator?",
            "a": "MySafeInfo Test Data Generator is a browser-based developer tool that generates realistic, relational test data across linked tables (Customers, Orders, Products, and Line Items) with consistent IDs and mathematical totals."
        },
        {
            "q": "What export formats are supported?",
            "a": "Datasets can be exported as multi-sheet Excel workbooks (.xlsx), a ZIP file containing individual CSVs, structured JSON, or SQL scripts containing CREATE TABLE DDL and INSERT statements."
        },
        {
            "q": "Is MySafeInfo Test Data Generator free to use?",
            "a": "Yes. It offers a generous free tier allowing developers to generate up to 5,000 rows per table directly in their browser without creating an account. Higher limits and additional data sources are available via a paid Data Pass."
        },
        {
            "q": "How does it handle relational data between multiple tables?",
            "a": "Unlike basic generators that produce independent rows, MySafeInfo coordinates entity relationships: Customer IDs link to Orders, Order lines reference valid Product IDs, and item prices sum up to matched order totals."
        }
    ]
}

MYSAFEINFO_REVIEW = {
    "article_title": "MySafeInfo Test Data Generator Engineering Dossier: Relational Coherence, Dirty Data Injection, and Client-Side Synthesis",
    "reading_time": "5 min read",
    "editorial_verdict_callout": "MySafeInfo replaces brittle, throwaway database seed scripts with an instant browser-native generation studio that guarantees relational coherence across parent-child entities without signup gates.",
    "chapters": [
        {
            "id": "relational-coherence-architecture",
            "number": "01",
            "title": "The Relational Coherence Bottleneck in Modern Test Data Synthesis",
            "content": (
                "Modern application development demands rich, representative datasets for local development, staging environments, "
                "and automated integration suites. However, traditional mock data generators (such as standard Faker libraries or generic "
                "column-based online generators) suffer from an inherent isolation problem: each row or column is synthesized independently. "
                "When building e-commerce, ERP, or SaaS applications, realistic testing requires complex entity relationships—a Customer record "
                "must link to multiple Orders, each Order must contain valid Order Lines pointing to existing Products, and the mathematical totals "
                "must accurately reflect unit prices multiplied by quantities plus tax. Writing one-off Python, SQL, or Node.js seed scripts to "
                "maintain these relational foreign keys is tedious, error-prone, and frequently abandoned during rapid sprint cycles. MySafeInfo "
                "Test Data Generator directly addresses this bottleneck by embedding coordinated multi-table relational logic directly within "
                "a browser-native synthesis engine, producing structurally sound, interconnected datasets in seconds."
            )
        },
        {
            "id": "multi-format-export-pipeline",
            "number": "02",
            "title": "Multi-Format Export Pipelines: From Multi-Sheet Workbooks to DDL-Compliant SQL",
            "content": (
                "Engineering teams rarely consume test data in a single format. Frontend engineers evaluating client-side state management "
                "prefer structured JSON payloads; business analysts and QA leads reviewing user journeys rely on multi-sheet Excel (.xlsx) workbooks; "
                "and backend developers initializing local Docker or PostgreSQL containers require executable SQL scripts. MySafeInfo provides "
                "a versatile export architecture that generates synchronized artifacts across all four formats from a single configuration. "
                "Its SQL generation is notably robust, emitting complete CREATE TABLE Data Definition Language (DDL) declarations with appropriate "
                "PRIMARY KEY and FOREIGN KEY constraints before emitting bulk INSERT statements in topological dependency order. For file-based "
                "workflows, CSV exports are neatly packaged into an organized ZIP archive where foreign key columns strictly agree across tables, "
                "allowing immediate drag-and-drop ingestion into database administration GUIs (such as DBeaver, TablePlus, or pgAdmin)."
            )
        },
        {
            "id": "dirty-data-chaos-engineering",
            "number": "03",
            "title": "Dirty Data Injection & Ingestion Resilience: Chaos Engineering for ETL Pipelines",
            "content": (
                "One of MySafeInfo's most distinctive architectural capabilities is its optional 'dirty data' injection mode. In real-world "
                "production environments, data arriving from legacy migrations, third-party webhooks, or user uploads is rarely immaculate—it contains "
                "malformed phone numbers, inconsistent casing, whitespace anomalies, and missing optional fields. Standard mock generators create "
                "an artificial sense of security by generating exclusively pristine records, leaving applications vulnerable to edge-case crashes "
                "when confronted with real-world inputs. MySafeInfo allows QA engineers to deliberately inject controlled anomalies into CSV and Excel "
                "exports while providing a corresponding 'answer key' mapping intended clean values against dirty counterparts. This feature transforms "
                "the tool from a passive mock data creator into an active verification utility for testing ETL pipeline resilience, data sanitizers, "
                "and schema validation boundaries. Importantly, SQL exports remain strictly clean to ensure schema initialization remains deterministic."
            )
        },
        {
            "id": "tco-freemium-verdict",
            "number": "04",
            "title": "Total Cost of Ownership & Architectural Verdict: Frictionless Utility for Agile Teams",
            "content": (
                "From a total cost of ownership (TCO) and developer experience perspective, MySafeInfo establishes an exceptionally high standard "
                "for utility freemium tools. While established competitors like Mockaroo restrict free users to 1,000 rows and force account "
                "creation behind credit card or subscription paywalls for multi-table relationships, MySafeInfo offers up to 5,000 rows per table "
                "completely free with zero account registration. Because synthesis runs client-side in the user's browser, there is zero data "
                "leakage to external servers—making it safe for teams operating under stringent security policies. For massive enterprise-scale "
                "datasets exceeding 5,000 rows, a paid Data Pass provides straightforward access to expanded volume without locking developers into "
                "predatory recurring commitments. In conclusion, MySafeInfo Test Data Generator is an indispensable asset for developers, QA engineers, "
                "and data architects seeking believable, mathematically consistent relational test datasets without the overhead of custom scripting."
            )
        }
    ],
    "tool_id": "mysafeinfo-test-data-generator",
    "model_used": "editorial-team",
    "generated_at": "2026-11-12T02:20:00.000000+00:00"
}

def main():
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # Check if tool already exists
    existing_idx = next((i for i, t in enumerate(tools) if t.get("id") == MYSAFEINFO_TOOL["id"]), None)
    tool_entry = dict(MYSAFEINFO_TOOL)
    tool_entry["editorial_review"] = MYSAFEINFO_REVIEW

    if existing_idx is not None:
        print(f"Updating existing tool at index {existing_idx}")
        tools[existing_idx] = tool_entry
    else:
        print(f"Appending new tool: {MYSAFEINFO_TOOL['id']}")
        tools.append(tool_entry)

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print(f"all_tools.json saved. Total tools: {len(tools)}")

    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews[MYSAFEINFO_TOOL["id"]] = MYSAFEINFO_REVIEW

    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"editorial_reviews.json saved. Total reviews: {len(reviews)}")

if __name__ == "__main__":
    main()
