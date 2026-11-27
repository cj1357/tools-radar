# -*- coding: utf-8 -*-
"""
Catalog Base USDC Receipt Audit into all_tools.json and editorial_reviews.json.
"""

import json
import os

BASE_DIR = r"d:\_projectsTYweb\tools-radar"
all_tools_file = os.path.join(BASE_DIR, "data", "all_tools.json")
editorial_file = os.path.join(BASE_DIR, "data", "editorial_reviews.json")

TOOL_DATA = {
    "id": "base-usdc-receipt-audit",
    "name": "Base USDC Receipt Audit",
    "tagline": "Python 3.9+ CLI that verifies Base mainnet USDC payout CSV hashes against two public RPCs",
    "summary": "Base USDC Receipt Audit is a lightweight Python 3.9+ command-line utility built for operators and contractors who need to reconcile payout CSVs against onchain settlements on Base mainnet. Given a CSV containing item_id, tx, and an optional expected amount, the CLI queries two read-only public RPC endpoints without requiring a wallet connection or API key. It verifies the recipient address, native Base USDC contract, and receipt finality, deduplicates shared transaction hashes so each hash counts once, flags amount mismatches or transfers sent to another address, and writes a structured JSON audit report.",
    "url": "https://github.com/eddiezhan/task-deliveries/tree/main/base-usdc-receipt-audit",
    "github_url": "",
    "source": "submission",
    "category": "developer-tools",
    "tags": [
        "Python",
        "CLI",
        "Base",
        "USDC",
        "Web3",
        "Receipt Audit",
        "Developer Tools"
    ],
    "pricing_model": "Paid",
    "starting_price": "2",
    "stars": 0,
    "primary_alternative": "",
    "is_self_hostable": False,
    "no_signup_required": False,
    "signal_score": 82,
    "verdict": "A focused, zero-API-key Python CLI for cross-checking batch Base USDC payout CSVs across two public RPC nodes—backed by free inspectable sample inputs/outputs and an honest 100-hash-per-run scope.",
    "deployment_format": "Python 3.9+ CLI Bundle (ZIP)",
    "extensibility": "CSV Input Schema, Dual Public RPC Endpoints & JSON Audit Report Output",
    "install_command": "# Free sample CSV/JSON available on the product page; full Python 3.9+ ZIP bundle is 2 USDC on Base:\n# https://github.com/eddiezhan/task-deliveries/tree/main/base-usdc-receipt-audit",
    "architecture_summary": "Base USDC Receipt Audit runs locally as a Python 3.9+ CLI script packaged in a downloadable ZIP bundle alongside sample CSV data, setup instructions, and eight offline tests. Rather than trusting a single node or requiring browser wallet signatures, it checks each transaction hash against two read-only Base mainnet RPC endpoints (such as mainnet.base.org and base-rpc.publicnode.com) and outputs a deterministic JSON ledger.",
    "architecture_note": "Executes locally on Python 3.9+ with read-only public RPC calls—requiring no wallet connection, personal accounts, or external API keys. Available as a one-time 2 USDC download on Base via Payaion.",
    "date_added": "2026-11-27",
    "featured": False,
    "key_features": [
        {
            "title": "Dual Public RPC Finality Cross-Check",
            "description": "Queries two read-only Base mainnet RPC endpoints to verify receipt status and confirm whether both nodes have reached finalized height."
        },
        {
            "title": "Native Base USDC & Recipient Verification",
            "description": "Validates transfers against the native Base USDC contract and target recipient address, distinguishing finalized credits from transfers sent elsewhere."
        },
        {
            "title": "Transaction Hash Deduplication & Mismatch Flags",
            "description": "Counts each shared transaction hash once across multiple CSV rows while reporting amount differences and verification errors."
        },
        {
            "title": "Zero-Wallet, Zero-API-Key JSON Output",
            "description": "Produces a structured JSON audit report locally without requiring browser wallet connections, private keys, or paid RPC API subscriptions."
        }
    ],
    "use_cases": [
        "Contractors and task-platform operators auditing batch USDC payout CSVs instead of checking transaction hashes manually in a block explorer.",
        "Finance or operations teams verifying whether shared transaction hashes across multiple payout rows represent a single settled transfer.",
        "Teams needing verifiable dual-RPC JSON evidence distinguishing finalized Base USDC receipts from pending or unfinalized confirmations."
    ],
    "pros": [
        "Requires no wallet connection, private keys, or paid RPC API keys",
        "Free sample CSV input and sample JSON output are publicly inspectable before purchasing",
        "Includes Python 3.9+ source code, setup guide, and eight offline tests inside the one-time 2 USDC bundle",
        "Honest, well-bounded scope: handles up to 100 unique hashes per run and clearly avoids unrelated accounting claims"
    ],
    "cons": [
        "Commercial ZIP download (2 USDC on Base via Payaion; free preview covers sample data only)",
        "Scoped strictly to native Base mainnet USDC up to 100 unique hashes per run—does not calculate gas fees, wallet balances, or net profit"
    ],
    "target_audience": "Crypto operators, contractors, and Base ecosystem builders reconciling batch USDC payout CSVs locally.",
    "comparison_vs_alt": "",
    "faqs": [
        {
            "q": "What does Base USDC Receipt Audit check?",
            "a": "It reads a payout CSV (item_id, tx, and optional expected amount), checks the recipient, native Base USDC contract, and receipt status across two public RPC endpoints, deduplicates shared hashes, and outputs a JSON audit report."
        },
        {
            "q": "Does it require a wallet connection or API key?",
            "a": "No. The Python 3.9+ CLI uses read-only public Base RPC endpoints and requires no wallet connection, private keys, or API key."
        },
        {
            "q": "How is Base USDC Receipt Audit priced?",
            "a": "The full Python 3.9+ ZIP bundle (source, example CSV, setup guide, and eight offline tests) is a one-time 2 USDC download on Base via Payaion. Sample inputs and JSON output are free to inspect on the product page."
        },
        {
            "q": "What are the tool's limits?",
            "a": "Each run checks up to 100 unique user-provided hashes for native USDC on Base mainnet. It does not compute fees, wallet balances, or net profit."
        }
    ]
}

REVIEW_DATA = {
    "article_title": "Base USDC Receipt Audit Analysis: Dual-RPC Finality Verification, Hash Deduplication, and Batch Payout Reconciliation",
    "reading_time": "4 min read",
    "editorial_verdict_callout": "Base USDC Receipt Audit turns tedious block-explorer clicking into a clean, repeatable Python CLI workflow—giving Base operators dual-RPC finality proof and hash deduplication for a flat 2 USDC.",
    "chapters": [
        {
            "id": "batch-payout-reconciliation-friction",
            "number": "01",
            "title": "The Payout CSV Problem: Why Explorer Spot-Checks Break Down at Scale",
            "content": "Contractors, bounty earners, and task-platform operators paid in USDC on Base frequently receive spreadsheets listing dozens of line items marked 'paid' alongside transaction hashes. Checking those rows one by one in a web block explorer is slow and error-prone: two rows may reference the same transaction hash, a hash might transfer USDC to an unrelated address, or an unfinalized receipt might still be subject to reorg risk. Base USDC Receipt Audit automates this reconciliation loop in a single local Python 3.9+ CLI pass."
        },
        {
            "id": "dual-rpc-verification-and-deduplication",
            "number": "02",
            "title": "Verification Mechanics: Dual Public RPCs, Contract Filtering, and Shared-Hash Deduplication",
            "content": "Rather than connecting a hot wallet or subscribing to commercial indexer APIs, the CLI reads an input CSV (`item_id`, `tx`, and optional `amount`) and queries two read-only Base mainnet RPC endpoints (such as `mainnet.base.org` and `base-rpc.publicnode.com`). For every unique hash, it checks the native Base USDC contract (`0x833589fcd6edb6e08f4c7c32d4f71b54bda02913`), confirms the target recipient address, verifies receipt status against both nodes' finalized heights, and flags amount mismatches. When multiple CSV rows share one transaction hash, the auditor counts that transfer once—separating finalized credits from `no_transfer` or `unfinalized` items inside a structured JSON report."
        },
        {
            "id": "packaging-offline-tests-and-boundaries",
            "number": "03",
            "title": "Packaging, Offline Test Coverage, and Honest Scope Boundaries",
            "content": "The tool ships as a lightweight one-time 2 USDC ZIP download on Base containing the Python 3.9+ source code, an example CSV, a setup guide, and eight offline tests, while the product page exposes `sample-input.csv` and `sample-report.json` openly so engineers can inspect the exact schema before purchasing. Its documented limits are equally clear: up to 100 unique hashes per run, strictly native Base mainnet USDC, and zero computation of gas fees, total wallet balances, or net profit."
        },
        {
            "id": "operational-verdict-base-operators",
            "number": "04",
            "title": "Operational Verdict: Practical Local Auditing Without Key or Wallet Exposure",
            "content": "For anyone regularly reconciling Base USDC payout spreadsheets, Base USDC Receipt Audit delivers focused, verifiable utility at a negligible one-time cost. By pairing read-only dual-RPC cross-checks with deterministic JSON output and zero wallet or API-key requirements, it provides clean audit evidence ready for bookkeeping or dispute checks."
        }
    ],
    "tool_id": "base-usdc-receipt-audit",
    "model_used": "editorial-team",
    "generated_at": "2026-11-27T10:15:00.000000+00:00"
}

def run():
    with open(all_tools_file, "r", encoding="utf-8") as f:
        tools = json.load(f)

    tools = [t for t in tools if t.get("id") != "base-usdc-receipt-audit"]
    tools.insert(0, TOOL_DATA)

    with open(all_tools_file, "w", encoding="utf-8") as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: all_tools.json saved with {len(tools)} tools.")

    with open(editorial_file, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    reviews["base-usdc-receipt-audit"] = REVIEW_DATA

    with open(editorial_file, "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: editorial_reviews.json saved with {len(reviews)} reviews.")

if __name__ == "__main__":
    run()
