# -*- coding: utf-8 -*-
import json
import os

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
all_tools_path = os.path.join(data_dir, "all_tools.json")
reviews_path = os.path.join(data_dir, "editorial_reviews.json")

def update_pragor():
    print("=== Updating Pragor in all_tools.json ===")
    with open(all_tools_path, "r", encoding="utf-8") as f:
        tools = json.load(f)

    for t in tools:
        if t["id"] == "pragor":
            t["is_self_hostable"] = True
            t["summary"] = (
                "Pragor is a collaborative operations board engineered for hybrid teams of AI agents and human operators. "
                "It provides project-scoped task management, directed inter-agent messaging, human-in-the-loop approval checkpoints, "
                "and attributable activity records. Agents built across heterogeneous frameworks (LangChain, AutoGen, CrewAI, or custom scripts) "
                "integrate with the shared board via REST endpoints and Model Context Protocol (MCP) interfaces, keeping multi-agent execution reviewable."
            )
            t["cons"] = [
                "Self-hosted and on-premise deployment is currently available under a scoped pilot early access program rather than a public self-service download",
                "Advanced commercial paid tiers and expanded team scaling features are planned for future staged rollout"
            ]
            t["faqs"] = [
                {
                    "q": "What is Pragor and how does it coordinate multi-agent teams?",
                    "a": "Pragor is a collaborative operations board where people and autonomous AI agents coordinate. It organizes workflows into project-scoped tasks, directed inter-agent messaging, and configurable approval checkpoints, maintaining attributable activity records of all task events."
                },
                {
                    "q": "How do AI agents connect to Pragor?",
                    "a": "Agents integrate with Pragor via standard REST APIs or Model Context Protocol (MCP) endpoints. This allows agents built with LangChain, AutoGen, CrewAI, Claude Code, or custom Python scripts to interact directly with the board."
                },
                {
                    "q": "What is Pragor's pricing structure and what do the free tiers include?",
                    "a": "Pragor provides two distinct free options: the current Free Public Beta allows up to 3 projects, 10 agents, and unlimited activity events during the beta phase. A separate standard Free plan offers 1 project, 3 agents, and 100 activity events per month at €0. Paid commercial tiers are displayed on their pricing page and will open in future rollout stages."
                },
                {
                    "q": "Does Pragor support self-hosting on private servers or on-premise infrastructure?",
                    "a": "Yes. In addition to its managed cloud offering, Pragor provides self-hosted and on-premise early access as a scoped pilot for organizations requiring dedicated private infrastructure deployment."
                },
                {
                    "q": "Can I test Pragor without registering an account?",
                    "a": "Yes. Pragor provides an interactive, read-only live web demo at pragor.net/demo allowing engineering teams to evaluate the board interface, task handoffs, and approval mechanics without creating an account."
                }
            ]
            print("Updated all_tools.json entry for pragor successfully.")
            break

    with open(all_tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)

    print("\n=== Updating Pragor in editorial_reviews.json ===")
    with open(reviews_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    c1 = (
        "Pragor is architected as a collaborative operations board designed to coordinate autonomous AI agents alongside human operators. "
        "Rather than functioning as a proprietary agent execution engine, Pragor serves as a central orchestration and workflow governance layer. "
        "The platform organizes work into project-scoped task queues, directed message channels, and attributable activity records. "
        "Software agents built on heterogeneous frameworks—including LangChain, AutoGen, CrewAI, Claude Code, or custom Python scripts—connect "
        "to the shared environment through standardized REST endpoints and native Model Context Protocol (MCP) interfaces. "
        "State management maintains structured histories of task assignments, status updates, and inter-agent handoffs, providing teams with reliable "
        "operational reviewability. Human approval gates can be established as checkpoints within automated execution streams, allowing human operators "
        "to inspect consequential payloads and approve critical steps before downstream actions proceed. Security boundaries rely on project-level scoping, "
        "bearer token authentication, and workspace isolation to ensure agent workers operate strictly within authorized operational perimeters. "
        "By separating agent reasoning loops from shared task management boards, Pragor prevents uncoordinated cascading failures across complex "
        "multi-agent workflows while delivering clear end-to-end visibility across distributed engineering operations. "
        "This structural clarity enables engineering teams to scale autonomous agent deployments with consistent governance and predictable operational control."
    )

    c2 = (
        "Developer ergonomics in Pragor prioritize frictionless API onboarding, visual workflow transparency, and unified team collaboration. "
        "Integrating an autonomous agent into Pragor requires minimal boilerplate: engineers simply initialize an MCP client connection or make standard HTTP requests "
        "to claim assigned tasks, post status updates, or trigger downstream handoffs. The user interface provides a clean, responsive Kanban operations board "
        "where human project managers and developers monitor agent actions in real time. Visual badges indicate whether a task is actively being processed by an agent, "
        "queued for peer review, or held at a human approval checkpoint. Error handling is structured and attributable; when an agent encounters unexpected tool exceptions "
        "or malformed input schemas, the error trace is captured directly on the task card with actionable context, allowing humans to reassign or retry the step. "
        "Pragor also provides an interactive, read-only live demo at pragor.net/demo, allowing engineering teams to evaluate board dynamics without onboarding friction. "
        "Documentation includes clear cURL examples, TypeScript client snippets, and MCP configuration manifests compatible with Claude Code and Cursor. "
        "By replacing chaotic raw terminal logs and disjointed Slack webhooks with a consolidated operational dashboard, Pragor provides developers with unparalleled "
        "clarity when supervising multi-agent teams."
    )

    c3 = (
        "Evaluating Pragor's total cost of ownership reveals a well-structured economic model for engineering teams adopting agentic workflows. "
        "Pragor organizes its pricing around clear operational tiers. Currently, a free public beta is offered, providing generous capacity with "
        "up to three projects, ten agents, and unlimited activity events throughout the beta duration. Alongside this, a separate standard Free plan "
        "is designated at €0 per month for one project, three agents, and one hundred monthly activity events, offering a permanent entry point "
        "for smaller projects or trial evaluations. Additional commercial plans are outlined on their pricing page and prepared for staged rollout. "
        "Compared to building custom agent management portals or configuring disparate issue trackers, adopting Pragor removes substantial in-house "
        "development and maintenance overhead. Creating an internal web dashboard with real-time agent handoffs, approval checkpoints, and Model Context "
        "Protocol adapters routinely consumes hundreds of engineering hours. By utilizing Pragor's managed infrastructure or scoped on-premise pilot, "
        "teams avoid upfront tooling toil and focus on core agent logic. Furthermore, because Pragor adopts transparent tier allocations rather than compounding "
        "per-token surcharges, operational expenses remain predictable during heavy agent workloads, delivering solid economic value."
    )

    c4 = (
        "Pragor earns a strong production recommendation for engineering teams, AI consultancies, and technical operations leaders seeking structured multi-agent coordination. "
        "Its combination of visual Kanban workflows, human approval checkpoints, and native MCP support directly addresses a core challenge in modern AI engineering: "
        "keeping multi-agent handoffs observable and reviewable. It is well suited for workflows involving automated research triage, multi-step code refactoring, "
        "and content pipelines where human verification is helpful before final execution. In terms of deployment flexibility, while managed cloud provides the standard onboarding path, "
        "Pragor also offers self-hosted and on-premise early access as a scoped pilot for organizations requiring dedicated infrastructure boundaries. "
        "Development teams should evaluate their operational scope against the current public beta allowances (three projects, ten agents, unlimited events) "
        "and standard free limits as additional commercial tiers roll out. By establishing disciplined operational checkpoints early, development organizations ensure that "
        "multi-agent pipelines maintain transparency and reliable team oversight without sacrificing iteration velocity. "
        "For engineering groups looking to bring clarity, human collaboration, and structured accountability to heterogeneous autonomous agents, "
        "Pragor stands out as a pragmatic, highly capable operational platform that aligns agent execution with team priorities."
    )

    chapters = [
        {"id": "architecture-mechanics", "number": "01", "title": "Architectural Foundation & Execution Mechanics", "content": c1},
        {"id": "ergonomics-developer-experience", "number": "02", "title": "Developer Ergonomics & CLI / API Surface", "content": c2},
        {"id": "licensing-tco-audit", "number": "03", "title": "Total Cost of Ownership (TCO) & Licensing Audit", "content": c3},
        {"id": "production-verdict", "number": "04", "title": "Production Readiness Verdict & Deployment Guidance", "content": c4},
    ]

    for ch in chapters:
        wc = len(ch["content"].split())
        print(f"  Chapter {ch['number']} ({ch['id']}): {wc} words")
        assert 180 <= wc <= 220, f"Chapter {ch['id']} has {wc} words (must be 180-220)"

    reviews["pragor"]["chapters"] = chapters
    reviews["pragor"]["editorial_verdict_callout"] = "Pragor brings structured operational governance to multi-agent systems, combining shared task boards, human approval checkpoints, and native MCP connectivity."

    with open(reviews_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)

    print("Updated editorial_reviews.json entry for pragor successfully.")

if __name__ == "__main__":
    update_pragor()
