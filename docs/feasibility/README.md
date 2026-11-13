# F — Feasibility and scope

Session 1: **13 November 2026 (Asia/Tehran)**. Baseline phase budget: **30 owner hours**; decision gate **26 November**. The plan's proposed start was 14 November; preparation started one day earlier. No downstream dates have been advanced. Actual owner hours are **not yet reported**; AI time does not substitute for them.

## Confirmed decisions

- Start with **grade-12 biology, chapters 1 and 2**.
- Serve learners **aged 15 and older**, including minors and adults.
- Offer **5 completed questions per Halle account per day**, with **2–3 reviewed follow-up exercises per answer**; failed, unsupported and unanswered requests do not consume the allowance.
- The operator is based in **Iran**.
- No reviewer is arranged; the owner requested a reviewer brief.
- No AI/OCR provider or hosting arrangement is selected yet.
- Retain the plan's requested **Telegram, Bale and Eita bots with one Go backend**. No two-bot scope or Eita mini-app substitution was chosen.

## Task status

Every F checkbox in the implementation checklist remains open. This table records partial progress without claiming that its acceptance conditions have passed.

| Task | Current evidence | Remaining condition / next action | Accountable owner | Baseline due |
| --- | --- | --- | --- | --- |
| F-01 | [Contract v0.1](product-contract.md) records selected chapters, ages 15+ and free allowance; drafts three journeys, wording and resource limits | Owner/reviewer agree formats/journeys/counting/resource limits; confirm edition/cohort; freeze contract | Project owner + future reviewer | 16 Nov |
| F-02 | [Official channel preflight and test steps](channel-capabilities.md) | Dedicated development accounts and live text/photo/identity/reply/action evidence; Eita inbound route unproven | Project owner; AI-assisted spike | 20 Nov |
| F-03 | [Provider assessment](provider-eligibility.md): direct Gemini mismatch; two unqualified domestic candidates | Written route eligibility, hosting and billing details, spending ceiling, then representative operational test | Project owner + provider contact | 24 Nov |
| F-04 | [Sanitized research audit](research-handoff.md), clean repository, exclusion rules | Owner records research/account/source ownership and accepts missing-source inventory | Project owner | 24 Nov |
| F-05 | [Reviewer brief](reviewer-brief.md), deliverables and unsent outreach draft | Recruit reviewer, agree 60–90 hours/dates/fee, source permissions and 20–50-person pilot recruitment path | Project owner + future reviewer | 25 Nov |
| F-06 | [Launch prerequisites record](launch-prerequisites.md) | Select merchant/domain, ask gateway/host, confirm official edition and exam/cohort timing | Project owner + external contacts | 25 Nov |
| F-07 | [Architecture and spending proposal](../decisions/0001-initial-architecture.md) | Resolve F-01–F-06; set numeric spending ceilings, owners and revised dates; accept ADR | Project owner | 26 Nov |

“Project owner” is the user directing this repository; external contact/account identities remain unrecorded. Baseline dates are planning targets, not promises. In particular, F-01's reviewer-dependent freeze on 16 November requires a reviewer earlier than F-05's 25 November recruitment deadline; bring recruitment forward or revise F-01 openly. F-03's operational host test similarly needs a host earlier than F-06's initial quote deadline. Neither conflict is silently treated as resolved.

## First-session deliverables

The implementation plan was brought into `docs/IMPLEMENTATION_TODO.md`; obsolete absolute research links were replaced with the handoff reference. The original package remains separate and unchanged. Added repository guidance/exclusions, the product contract, channel/provider evidence, research inventory, reviewer brief, launch coordination record and proposed architecture.

No production application, Go module, platform/provider account, deployment, payment, message to a third party, or paid AI run was created. This session advances F and does not claim B-01 completion.

## Next work, in dependency order

1. Review the concrete contract with a reviewer. The owner has selected ages 15+ and five completed new solves/day with 2–3 reviewed follow-ups per solve; formats, counting details, resource limits and Persian wording still need agreement.
2. Start reviewer recruitment using the prepared brief, and recover the official textbook edition for chapters 1–2 with provenance/permissions. Preserve the original research and record ownership handling.
3. Arrange dedicated Telegram/Bale development bots and Eita official interface evidence. Then run the bounded live spike and store sanitized results; tokens stay outside Git/chat.
4. Obtain written provider-route answers and hosting quote/region. Set the test budget before paid sample calls. Any uncertainty on minors/geography stays open.
5. Fill the launch-prerequisite records, set spending caps, resolve or explicitly reschedule remaining blockers, then accept F-07 before B-01.

If Eita or provider access fails, record the owner's choice and revised estimate before changing release scope. Independent domain work can continue only under that recorded plan; the requested release is not yet settled.

## Verification record

Checks run during this session:

- All 59 original task definitions preserved, with no F task marked complete.
- All 21 relative documentation links resolve across 12 repository files.
- Whitespace/final-newline checks passed for every new file (`git diff --no-index --check` per file).
- `git check-ignore --no-index --stdin`: 33 sensitive/generated example paths excluded, 10 intended source/example paths allowed; no private fixture files created.
- Common credential-signature scan passed without displaying values. No full external secret scanner was available; reviewed Git exclusions are not a guarantee against future secret commits.
- Independent review identified minimum-age and cross-channel quota ambiguity; the age decision and account/linking semantics are now explicit.

No application tests were applicable because no application code was added. Live channel/provider tests, human content review and owner-hour accounting remain pending; documentation cannot stand in for these results. Changes remain uncommitted and have not been pushed.

## Session 2 — F-02 preparation, 13 November 2026

The owner confirmed **both dedicated Telegram and Bale development bots are ready**. Added a [read-only channel diagnostic](../../tools/feasibility/README.md) for bot identity, webhook conflict detection and sanitized pending text/photo/action observations. This is temporary feasibility tooling; production remains Go.

Five offline tests passed using fake responses, including webhook refusal, privacy filtering and sanitized token-bearing failures. No live bot API request, message, provider request or account change was performed. Tokens remain with the owner. Next evidence needed: owner runs the diagnostic locally, then the documented reply/action/file-download checks and intended-host repetition. F-02 remains open; account readiness alone does not demonstrate interaction support. Owner hours have not been reported.

## Session 3 — Textbook recovery, 13 November 2026

Recovered the publisher-linked Biology 3 textbook for 1405–1406, inspected its imprint/contents/rights pages, and recorded chapter 1–2 page boundaries in a [source manifest and recovery record](textbook-recovery.md). PDF and review artifacts remain in ignored local storage. The publisher's HTTPS certificate failed verification; HTTP retrieval is explicitly recorded and requires independent authenticity confirmation. The rights notice requires permission, which has not been obtained. This advances F-06/source discovery without claiming F-05, F-06 or K-01 completion. No provider, bot or payment calls were made.
