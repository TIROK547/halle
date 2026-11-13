# Halle implementation guidance

Read `docs/IMPLEMENTATION_TODO.md`, `docs/feasibility/README.md`, and the relevant decision before changing implementation. The current phase is F; do not treat draft decisions or documentation evidence as completed access tests.

- Preserve one Go production backend. Python research remains offline and separate.
- Initial content scope: grade-12 biology chapters 1 and 2; ages 15+, including minors and adults; operator in Iran. The owner selected 5 completed questions per Halle account/day and 2–3 reviewed follow-ups per answer. Monetary spend caps and resource limits remain open.
- Keep canonical learning records independent of channel formatting and provider APIs.
- Follow the plan's F exit gate: no substantial channel/provider implementation before that access route is proven. A small dedicated feasibility spike is distinct from production integration.
- Eita mini-apps and outbound publishers do not satisfy the requested inbound bot scope. Record a user-approved scope change before substituting a different surface.
- Preserve original research; never import personal account sessions, credential defaults, raw inventories, or machine-specific deployment commands.
- Never run personal-account harvesting scripts as setup or CI. Do not reuse another project's proxy/server as an implicit project dependency.
- Keep secrets and student data out of Git and logs. Ignoring a filename is not a substitute for reviewing its content.
- Future workflows need durable acceptance, bounded retries, idempotent effects, separate delivery state, user isolation, and versioned sources/answers.
- Providers cannot authorize roles, payments, account merges, deletion, or arbitrary retrieved commands. Those decisions belong to deterministic application code.
- Mark tasks complete only with the stated acceptance evidence. Keep draft, documented, live-tested, reviewer-approved, and blocked states distinct.
- At session end update F status or the relevant later-phase record with actual checks and remaining dependencies. Do not invent owner hours, credentials, quotes, approvals, or test results.
