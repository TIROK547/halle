# ADR 0001 — Proposed initial architecture and spending control

Date: **13 November 2026 (Asia/Tehran)**. Task: **F-07**. Status: **proposed; dependencies F-01–F-06 remain open**.

## Context

Halle starts with Iranian grade-12 biology chapters 1–2 and an audience aged 15+, including minors and adults. One Go backend should serve Telegram, Bale and Eita. Eita inbound bot access and an eligible AI/OCR route are unresolved. This record translates the implementation plan into a reviewable proposal; it does not approve a provider, spending, or a reduced channel scope.

## Proposed boundaries

| Area | Initial approach | Decision still needed |
| --- | --- | --- |
| Go module/deployment | One module for this repository, proposed path `github.com/TIROK547/halle`; modular application and workers from the same codebase | Confirm repository/module ownership; pin tool versions in B-01 |
| Domain modules | Identity, curriculum/content, learning, workflows, billing, channels, operations | Concrete packages/contracts in B-02 |
| Transactional state | PostgreSQL as source of truth; migrations; pgvector for initial retrieval | Host/version/backup quote and restore targets |
| Files | Private object storage, app-owned object IDs, bounded uploads, expiring access and deletion | Provider, region, retention policy; no public student buckets |
| Jobs/delivery | Small Postgres-backed durable queue; transactional acceptance/outbox; bounded attempts/timeouts; delivery state separate from computation | Choose maintained implementation in B-04; duplicate delivery is expected |
| Identity | Stable Halle user ID; platform/account mapping in adapters; authenticated interactions; proof of control for linking | Channel transport evidence in F-02; never link on display name alone |
| Provider boundaries | Separate extraction, retrieval/embedding and solve contracts with typed validated outputs; record provider/model/prompt/content versions and full usage | An eligible, tested route in F-03; fallback must meet the same gates |
| Canonical answers | Source-bound versioned answers independent of rendering and student-specific feedback | Curriculum/source registry and correction rules in K/S |
| Operator access | Private minimum interface with strong authentication, least privilege and audit trail; no unauthenticated admin endpoint | Operator identity/authentication and support coverage |
| Infrastructure | Small reproducible staging and production; monitoring, recovery and local essential web assets | F-06 quotes/reachability; no Redis or Kubernetes without an actual need |

## Spending proposal — no numeric ceiling approved

User-facing free allowances are separate from internal monetary spend. The owner selected five completed solves per Halle account/day, with 2–3 reviewed follow-ups per answer. Detailed quota counting and resource limits remain proposed in the product contract. This allowance does not itself authorize provider spending.

Before paid provider use, the owner must fill in **currency, maximum cost per run/user/day, global daily and monthly caps, concurrency ceiling, and total authorized spike budget**. Account for extraction, routing, embeddings, generation, verification, retries and failed calls. Estimate the full run before reserving budget; settle recorded actual usage once; enforce a hard stop before another request when a limit cannot cover it. Unknown pricing/usage must not mean unlimited access.

No paid run is authorized by this ADR. Missing monetary caps mean paid work remains disabled. A temporary provider failure may deliver an appropriate saved verified answer or an unavailable state; it cannot activate an unevaluated provider or raw-model fallback.

## Preconditions for acceptance

- F-01 frozen with owner and reviewer: chapters/formats/journeys/limits/edition.
- F-02 live evidence for each proposed channel, or explicit owner scope decision with revised estimates.
- F-03 eligible and operational AI/OCR/embedding route for the actual operator and audience.
- F-04 ownership/handling recorded, research separated, missing-source inventory accepted.
- F-05 reviewer capacity, sources and pilot recruitment path confirmed.
- F-06 merchant/domain/hosting prerequisites, curriculum/cohort and contacts recorded.
- Numeric spend ceiling, responsible owners, blockers and revised dates explicitly recorded.

Until then, independent documentation, content inventory, and bounded feasibility spikes can continue. B-01 and production adapters are not reported as started. The [F status](../feasibility/README.md) carries blocker owners and baseline deadlines; no revised dates have been accepted in this session.
