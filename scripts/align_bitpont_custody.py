# -*- coding: utf-8 -*-
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
all_tools_file = os.path.join(BASE_DIR, 'data', 'all_tools.json')

with open(all_tools_file, 'r', encoding='utf-8') as f:
    tools = json.load(f)

updated = False
for tool in tools:
    if tool.get('id') == 'bitpont':
        # 1. Align summary
        tool['summary'] = (
            "Bitpont is a non-custodial onchain finance interface and market-data platform that unifies "
            "decentralized swaps, cross-chain bridges, borrowing, yield management, and treasury workflows "
            "into a single dashboard. Users authorize supported financial actions through wallet signatures "
            "or approved permissions. Assets and positions may be held by the underlying protocol contracts, "
            "and protocol, bridge, liquidation and execution risks remain. Complementing the retail interface, "
            "Bitpont provides developer documentation, an OpenAPI specification, and a free public market-data "
            "REST API with documented access limits, enabling developers and automated financial applications "
            "to programmatically query asset pricing, liquidity pools, and yield telemetry."
        )

        # 2. Align Key Advantages (pros)
        tool['pros'] = [
            "Free public market-data API access available under documented rate limits with standard OpenAPI specifications",
            "Non-custodial architecture where users authorize actions via wallet signatures or approved permissions without centralized exchange custody",
            "Consolidates multiple disparate DeFi primitives (swap, bridge, lend, yield) into a coherent interface",
            "Transparent fee schedule detailing interface, provider, and onchain network costs upfront"
        ]

        # 3. Align key_features
        for feat in tool.get('key_features', []):
            if 'wallet' in feat.get('title', '').lower() or 'custod' in feat.get('title', '').lower():
                feat['title'] = "Non-Custodial Authorization & Permissions"
                feat['description'] = (
                    "Supported financial operations are authorized directly through wallet signatures "
                    "or approved permissions against underlying protocol contracts."
                )

        # 4. Align FAQs
        for faq in tool.get('faqs', []):
            if 'protect user funds' in faq.get('q', '').lower() or 'non-custodial' in faq.get('q', '').lower():
                faq['a'] = (
                    "Bitpont never takes centralized custody of user assets or private keys. Users authorize "
                    "supported financial actions through wallet signatures or approved permissions directly "
                    "against underlying protocol contracts. Assets and positions may be held by the relevant "
                    "protocol smart contracts, and protocol, bridge, liquidation, and execution risks remain."
                )

        updated = True
        break

if updated:
    with open(all_tools_file, 'w', encoding='utf-8') as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)
    print("SUCCESS: Aligned Bitpont summary, Key Advantages, key_features, and FAQs in all_tools.json")
else:
    print("ERROR: Bitpont not found in all_tools.json")
