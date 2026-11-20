# -*- coding: utf-8 -*-
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
editorial_file = os.path.join(BASE_DIR, 'data', 'editorial_reviews.json')
all_tools_file = os.path.join(BASE_DIR, 'data', 'all_tools.json')

# 1. Update editorial_reviews.json
with open(editorial_file, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

bp_review = reviews.get('bitpont')
if bp_review and 'chapters' in bp_review:
    # Chapter 2 correction
    bp_review['chapters'][1]['content'] = (
        "From a security and compliance perspective, the central tenet of Bitpont's system design is strict non-custodial integrity. "
        "Centralized exchange blowups throughout crypto history have repeatedly demonstrated the existential hazards of vendor asset custody. "
        "Bitpont never manages deposit accounts, holds private keys, or operates internal offchain balance sheets. When a user initiates a "
        "transaction—whether an asset swap, a cross-chain liquidity bridge, or a collateralized borrowing position—Bitpont compiles the required "
        "calldata and routes it directly to the user's connected Web3 wallet. Users control wallet signing directly through their hardware or "
        "software signature enclave before authorizing any onchain transaction. However, while self-custody wallet signing removes custodial "
        "operator risk, protocol, bridge, liquidation, and execution risks remain; deposited assets and open positions can be held by the relevant "
        "protocol smart contracts, and users should not assume every integrated contract is immutable."
    )

    # Chapter 3 correction
    bp_review['chapters'][2]['content'] = (
        "Beyond its end-user web dashboard, Bitpont provides dedicated infrastructure for quantitative developers and automated financial agents "
        "through its developer portal at bitpont.com/developers/. Rather than relying on proprietary, closed SDKs, Bitpont publishes an OpenAPI "
        "specification that allows engineering teams to generate typed client libraries across TypeScript, Python, and Go in seconds. Developers "
        "can query public market-data read endpoints—including token pair pricing, liquidity depth, routing quotes, and historical pool yields—under "
        "generous, documented rate limits without upfront commercial contracts. Higher API limits and scoped partner access can be requested at "
        "support@bitpont.com; availability and terms are agreed for the use case."
    )

    # Chapter 4 correction
    bp_review['chapters'][3]['content'] = (
        "In assessing total operational utility, Bitpont distinguishes itself through fee transparency. The platform documents transaction "
        "costs—including provider routing spreads, interface fees, and onchain network gas charges—upfront at bitpont.com/fees/, though "
        "network costs, price impact, slippage, and execution risk still apply. For crypto-native foundations, decentralized autonomous "
        "organizations (DAOs), and Web3 startups, Bitpont's consolidated treasury dashboard provides holistic visibility into multi-chain assets, "
        "active borrow ratios, and yield accrual from a unified vantage point. While users remain accountable for underlying smart contract and "
        "execution dynamics across integrated protocols, Bitpont delivers a premier non-custodial control plane and developer API gateway that "
        "significantly elevates the standard of onchain financial software. (Note: ToolsRadar editorial scores reflect independent software "
        "utility evaluations and remain clearly distinguished from independent third-party security audits of Bitpont)."
    )

    with open(editorial_file, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print("SUCCESS: updated editorial_reviews.json")
else:
    print("ERROR: bitpont not found in editorial_reviews.json")

# 2. Update all_tools.json
with open(all_tools_file, 'r', encoding='utf-8') as f:
    tools = json.load(f)

updated = False
for tool in tools:
    if tool.get('id') == 'bitpont':
        tool['extensibility'] = 'REST APIs, SDK Tooling & Supported Agent Workflows'
        tool['cons'] = [
            'Onchain protocol operations remain subject to underlying smart contract, bridge, slippage, and execution risks',
            'Higher API limits and scoped partner access can be requested at support@bitpont.com'
        ]
        for faq in tool.get('faqs', []):
            if 'fees structured' in faq.get('q', '').lower():
                faq['a'] = (
                    'Limited public market-data reads are free under documented access limits. Execution operations may incur '
                    'provider routing spreads, interface, and network gas costs as detailed at https://www.bitpont.com/fees/, '
                    'with network costs, price impact, slippage, and execution risk still applying. Higher API limits and '
                    'scoped partner access can be requested at support@bitpont.com.'
                )
        updated = True
        break

if updated:
    with open(all_tools_file, 'w', encoding='utf-8') as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print("SUCCESS: updated all_tools.json")
else:
    print("ERROR: bitpont not found in all_tools.json")
