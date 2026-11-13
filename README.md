# Halle

A Persian learning assistant being built for Telegram, Bale, and Eita with one Go backend. The initial content scope is **grade-12 biology, chapters 1 and 2**, for learners **aged 15 and older**, including minors and adults. The operator is based in Iran. The selected initial free allowance is **5 completed questions per Halle account per day**, with 2–3 reviewed follow-up exercises per answer.

## Current state

First building session: **13 November 2026, Asia/Tehran**. We are in **F — feasibility and scope**. This repository contains the implementation plan and working decisions; there is no application runtime yet. The three-bot release remains conditional on supported Eita inbound interactions and an eligible AI/OCR route.

- [Implementation checklist](docs/IMPLEMENTATION_TODO.md): phase budgets, dependencies, and completion conditions.
- [F status and next actions](docs/feasibility/README.md): what is decided, demonstrated, or still open.
- [Initial product contract](docs/feasibility/product-contract.md): chapter scope, three journeys, and proposed limits.
- [Channel capabilities](docs/feasibility/channel-capabilities.md): official documentation and live spike procedure.
- [Provider eligibility](docs/feasibility/provider-eligibility.md): route assessment and required evidence.
- [Research handoff](docs/feasibility/research-handoff.md): available assets, private material, and missing sources.
- [Reviewer brief](docs/feasibility/reviewer-brief.md): role, deliverables, and content access.
- [Launch prerequisites](docs/feasibility/launch-prerequisites.md): F-06 owner actions.
- [Architecture proposal](docs/decisions/0001-initial-architecture.md): F-07 draft; not approved for implementation.

## Working rules

Keep the original research package separate. Do not copy its personal Telegram session, account defaults, raw inventories, PDFs, generated embeddings, or virtual environment into this repository. The [handoff](docs/feasibility/research-handoff.md) records paths relative to the external research root. Secrets belong in local ignored configuration, never documentation or chat.

Use the checklist's acceptance conditions. A draft, documentation lookup, or generated code does not complete a live integration, reviewer, or operational gate. Record actual owner time separately from AI execution time; the owner-hour budget has not been consumed by assumption.

The first Go setup task is **B-01**, after F-07. No provider or bot account is configured here. F-02's bounded development-account spike can establish platform access before a production adapter exists.
