**Halle — AI-assisted implementation checklist for an Iran release**

Working copy imported on **13 November 2026**. See [F session status](feasibility/README.md) for decisions and partial progress. Original task completion conditions and baseline dates remain unchanged; no F task is complete yet.

Prepared 11 November 2026. Owner: one developer, assisted by AI, available **15 focused hours/week**. All deadlines below use the Gregorian calendar and **Asia/Tehran** time. Proposed start: **Saturday, 14 November 2026**. This file is a plan; no implementation or external registration has been performed.

The requested final milestone is **production Bale, Eita, and Telegram bots using one Go backend**. Independent mobile and web applications follow later. Eita bot feasibility is an unresolved dependency, not an assumed capability.

**Capacity, estimates, and the release promise**

- Planned owner work: **375 hours**. Protected contingency: **45 hours**. Planning total: **420 hours**.
- Capacity: 28 active weeks at 15 hours/week, plus a proposed two-week break/deployment freeze from **20 March through 2 April 2027**. These are planning dates around Nowruz, not a claim about the official holiday calendar.
- Conditional public launch target: **9 June 2027**; initial stabilization through **11 June**.
- If the work fits the 375-hour plan with no contingency consumed, the earliest corresponding launch window is **19–21 May**. A 510-hour outcome moves the window to **21–23 July**. These are effort scenarios, not statistical confidence intervals.
- Estimates include your requirements work, AI supervision, implementation review, debugging, meaningful tests, deployment, and documentation. AI generation time is not a substitute for owner review time.
- The baseline assumes you can review ordinary Go/SQL changes and operate a small server with assistance. If those are new skills, add a separate **60–120-hour learning/rework allowance** (about 4–8 active weeks); do not hide that time inside the AI estimate.
- Allow **60–90 additional hours from a qualified subject reviewer**, spread across content preparation, evaluation, and pilot review. This is separate from the 420 owner hours. If you perform that work yourself, add roughly **4–6 active weeks**, assuming you have the subject expertise.
- Platform approvals, account eligibility, content permissions, and provider contracting have unconfirmed lead times. Book their prerequisites early. Elapsed approval time can delay the calendar even when it adds little coding effort.
- Dates depend on the gates below. Do not advertise a guaranteed three-bot launch before Eita and provider access are proven.
- The project documents target the 1406 cohort. This research did not establish an authoritative 1406 exam timetable. Verify the relevant exam dates in task F-06; a June launch may be late for parts of that cohort's preparation. Decide early whether the first cohort is 1406 revision users, the following cohort, or a smaller earlier free pilot. Do not speed up by removing correctness or payment checks.

**Keep the first release small enough to complete**

Recommended starting slice: **one or two selected grade-12 biology chapters**, chosen with a teacher. Existing assets make this cheaper to validate than starting a new subject, but the current genetics results do not justify treating genetics as the easiest launch chapter. Confirm the choice in F-01. Do not promise the whole biology course or all subjects.

Included: text/photo questions in that slice; curriculum-based explanation with traceable citations; the student's attempted answer and a bounded explanation of a mistake; 2–3 reviewed follow-up exercises; saved attempts and history; a simple next-practice suggestion; clear unsupported/uncertain states; minimal operator tools; usage limits; one approved domestic purchase route where permitted; support and recovery procedures.

Use free Telegram access initially unless a supported Stars purchase/settlement route is separately approved. Paid access rules across linked accounts must be checked against each platform's terms. A paid product on one platform does not automatically authorize payment links or sales in another.

Defer: full exam-sheet grading, predictive ranks, adaptive weekly scheduling, advanced mastery percentages, full spaced-repetition algorithms, social feeds, public user content, private messaging, live rooms, transferable coins, host payouts, marketplaces, parent/teacher dashboards, all-subject coverage, independent web/mobile apps, fine-tuning, and a full concept graph.

A small HTTPS page for legal information/payment callbacks is infrastructure for the bot product. An Eita mini-app, if necessary, would be a **scope change requiring your explicit choice**, not an undisclosed substitute for the requested bot.

**Three findings that change the original project assumptions**

1. **Eita integration is not yet proven.** Its public documentation describes a hosted mini-app plus opt-in outbound messages. This review did not establish a Telegram-equivalent inbound private-chat/photo API. Prove the exact interaction with an official supported interface in F-02. If it cannot be proven, the strict three-bot milestone has no credible delivery date. Options to decide are an approved Eita mini-app, a changed two-bot release scope, or waiting for a supported bot interface. [Official Eita overview](https://developer.eitaa.com/docs/Home/), [architecture](https://developer.eitaa.com/docs/ArchitectureOverview/), [message sending](https://developer.eitaa.com/docs/Develop/SendMassage/).
2. **The experimental Gemini setup cannot be assumed suitable for launch.** The current Gemini API terms exclude clients directed toward or likely accessed by under-18s, and restrict availability geographically; Iran is absent from the published region list. Select and document a deployment/provider arrangement eligible for the intended operator and student population. A foreign proxy alone does not resolve these requirements. F-03 is a production blocker. [Gemini terms](https://aistudio.google.com/docs/terms), [available regions](https://aistudio.google.com/docs/available-regions).
3. **Payments must differ by channel.** Telegram requires Stars for digital-service sales inside Telegram. Do not copy a domestic checkout link into its bot as the assumed purchase path. Bale and an approved Eita surface need their own verified purchase behavior. [Telegram digital payments](https://core.telegram.org/bots/payments-stars).

**Milestones and the critical path**

| Phase | Calendar window | Owner hours | Deadline / demonstrable outcome |
|---|---|---:|---|
| F — Feasibility and scope | 14–27 Nov 2026 | 30 | **26 Nov:** Eita/provider decisions and bounded release specification |
| B — Go foundation and first working path | 28 Nov–18 Dec | 45 | **17 Dec:** persisted Telegram workflow returning a known test answer |
| K — Knowledge and evaluation foundation | 19 Dec–15 Jan 2027 | 60 | **14 Jan:** versioned content and first grounded answer through the backend |
| S — Solver, diagnosis, and practice | 16 Jan–5 Feb | 45 | **4 Feb:** complete learning loop in staging |
| C — Three channel adapters | 6–26 Feb | 45 | **25 Feb:** equivalent supported workflows across all three, conditional on F-02 |
| L — Learning history and operator control | 27 Feb–19 Mar | 45 | **18 Mar:** internal alpha with correction, deletion, and recovery tools |
| Planned break | 20 Mar–2 Apr | 0 feature hours | No new user enrollment or planned production deployment |
| I — Iran operations and payment readiness | 3–23 Apr | 45 | **22 Apr:** release-candidate infrastructure and verified domestic payment flow |
| P — Controlled pilot and acceptance | 24 Apr–14 May | 45 | **13 May:** pilot findings, locked evaluation, and launch recommendation |
| R — Contingency and production release | 15 May–11 Jun | 15 + 45 reserve | **9 Jun:** staged public launch; **11 Jun:** initial stabilization |
| **Total** | **30 calendar weeks** | **420** | **375 planned + 45 contingency** |

Critical path: **F-02/F-03 → B foundation → K verified knowledge/provider baseline → S dependable learning loop → C supported channels → L/I readiness → P evidence → R launch**.

Start reviewer recruitment, payment applications, content permissions, and platform approval work in F. These can wait externally while engineering continues. One person's 15 hours cannot simultaneously fund two full engineering tracks: parallelize independent AI drafts or external review, then integrate serially.

Each task below has a target owner-hour budget, deadline, dependencies, and a concrete completion condition. Split a task larger than four hours into several AI work sessions. An unchecked task is not completed merely because AI generated code for it.

**F — Resolve the expensive unknowns first. Budget: 30 hours. Gate: 26 November.**

- [ ] **F-01 — Freeze the initial product contract. 4h. Due 16 Nov.** Choose chapter(s), supported question formats, age group, free limits, and the three exact student journeys. Record excluded features and unsupported-input wording. Done when you and the reviewer can describe the same release without referring to the full feature catalog.
- [ ] **F-02 — Prove all three integration surfaces. 6h, timeboxed. Due 20 Nov.** Using official documentation and development accounts, demonstrate receive text/photo → identify user → reply → handle an action. Record actual capabilities and limitations per channel. Do not assume Bale accepts every Telegram parameter. For Eita, require evidence of supported inbound interactions; outbound channel posting is insufficient. If blocked, stop the spike and record the scope decision required. [Telegram API](https://core.telegram.org/bots/api), [Bale API](https://docs.bale.ai/), [Eita architecture](https://developer.eitaa.com/docs/ArchitectureOverview/).
- [ ] **F-03 — Select an eligible AI/OCR route. 6h, timeboxed. Due 24 Nov.** Check operator location, Iranian end users, under-18 use, retention, billing, access from the intended host, and commercial rights. Test only eligible candidates on a small representative sample. Obtain written clarification where terms are unclear. Done when one route is eligible and operational and its limitations are recorded. If self-hosting is necessary, re-estimate infrastructure and evaluation; it is not included as a free substitute.
- [ ] **F-04 — Clean the research handoff and agree ownership. 3h. Due 24 Nov.** Identify private session files/account defaults for secure handling; keep them out of future source control. Start a clean implementation repository preserving research separately. Inventory missing source PDFs and machine-specific paths. Do not delete the original research or rotate unrelated accounts automatically.
- [ ] **F-05 — Secure human review and content access. 4h owner coordination. Due 25 Nov.** Confirm a qualified reviewer, 60–90 review hours, deliverable dates, source/permission records, and 20–50 potential pilot participants. Reviewer time is additional. No teacher availability means the evaluated-content milestone must move.
- [ ] **F-06 — Start Iran launch prerequisites. 3h owner effort; external waiting separate. Due 25 Nov.** Choose the merchant identity/domain, ask the selected gateway for its current KYC/tax/eNAMAD/business requirements, identify suitable hosting/support contacts, and verify official curriculum editions and exam dates. Record requirements rather than relying on the old project's legal/market assumptions.
- [ ] **F-07 — Approve the architecture and spending ceiling. 4h. Due 26 Nov.** After F-01–F-06, write a short decision record for Go modules, storage, jobs, identity, provider interfaces, minimum operator access, and per-user/global spending caps. Done when unresolved blockers, owners, and revised dates are explicit.

**F exit:** no substantial channel-specific or provider-specific implementation until its access path is proven. If Eita or the provider fails, continue independent domain work only with a recorded plan; do not report the requested release scope as settled.

**B — Build one usable path early. Budget: 45 hours. Gate: 17 December.**

- [ ] **B-01 — Create the Go project and repeatable development setup. 5h. Due 30 Nov. Depends F-07.** Pin tool versions, configuration validation, migrations, local database, test commands, and secret placeholders. A fresh checkout must start without copying personal credentials or Mac-specific paths.
- [ ] **B-02 — Define contracts and core records. 7h. Due 3 Dec. Depends B-01.** Model Halle users, platform accounts, messages, uploads, workflows/runs, answer artifacts, curriculum versions, and timestamps. Keep platform IDs in adapters/account mappings. Define structured API input/output and versioning for later apps.
- [ ] **B-03 — Implement transport-independent identity and access checks. 7h. Due 7 Dec. Depends B-02.** Create a Halle user from an authenticated platform interaction; scope every read/write to that user. Test that one account cannot read another's uploads, attempts, or result IDs. Avoid compulsory phone collection at initial onboarding.
- [ ] **B-04 — Build durable jobs and result delivery. 8h. Due 10 Dec. Depends B-02.** Persist queued/running/completed/failed states, retry limits, timeouts, attempts, and delivery state. Use a maintained Go-compatible queue approach; a Postgres-backed queue can keep the first deployment simple. Demonstrate crash recovery and duplicate-event handling.
- [ ] **B-05 — Implement the Telegram vertical slice. 7h. Due 14 Dec. Depends B-03/B-04 and F-02.** Accept a test question, persist it, run a deterministic job, and deliver a known answer card. User-visible progress survives a restart. Keep AI mocked here to isolate workflow errors.
- [ ] **B-06 — Add safe upload handling. 6h. Due 16 Dec. Depends B-03/B-04.** Enforce content type/size/time limits, private object access, expiring URLs, metadata stripping where appropriate, and deletion policy. Block arbitrary server-side fetching of untrusted URLs. Demonstrate rejected oversized/malformed input.
- [ ] **B-07 — Establish CI and a staging deployment. 5h. Due 17 Dec. Depends B-01–B-06.** Run formatting, compilation, focused tests, migration checks, secret detection, and vulnerability checks. Deploy staging with health checks and sanitized logs. Save the first full user-flow demonstration.

**B exit:** a real channel can carry a persistent workflow through the Go backend. This is a demonstrable foundation, not evidence of answer quality.

**K — Build trustworthy knowledge before scaling it. Budget: 60 hours. Gate: 14 January.**

- [ ] **K-01 — Recover and register the actual sources. 8h. Due 21 Dec. Depends F-05/B-02.** Obtain the selected textbook edition and permitted questions/keys. Record source IDs, file hashes, edition/year, page numbering, provenance, and permitted uses. The 11,525-row file inventory is discovery metadata, not a production question bank.
- [ ] **K-02 — Build the small curriculum tree and review schema. 8h. Due 24 Dec. Depends K-01.** Define stable topic IDs, source-page references, question options/key, explanation, difficulty tags, and verification status. Keep ambiguous keys out of approved material until adjudicated. Have the teacher review topic boundaries.
- [ ] **K-03 — Implement reproducible ingestion. 10h. Due 31 Dec. Depends K-02.** Extract text or OCR as needed, correct Persian reading order, preserve diagrams separately, segment by meaning, and attach provenance. Save extraction and embedding versions. Run the pipeline again and obtain an explainable equivalent index without duplicate source records.
- [ ] **K-04 — Build the evaluation dataset and runner. 10h owner tooling/coordination. Due 5 Jan. Depends K-02/F-05.** Target 350 distinct question families: 100 development, 50 validation, 200 locked holdout. Keep paraphrases, rephotographs, and numeric variants in the same split. Include at least 100 real phone-photo cases across the splits; these do not inflate the unique-question denominator. Human labeling is reviewer work. Keep holdout labels away from generation/tuning agents.
- [ ] **K-05 — Connect the eligible provider behind a Go interface. 8h. Due 7 Jan. Depends F-03/B-04.** Implement structured output validation, request timeouts, bounded retries, cancellation, provider/model version records, and complete usage accounting. Reuse research findings, not unexamined CLI behavior. Do not carry the unconditional check-mark output into production.
- [ ] **K-06 — Implement retrieval and validated citation assembly. 8h. Due 12 Jan. Depends K-03/K-05.** Filter by supported curriculum/book edition, retrieve candidate passages, and assemble citations from stored source IDs. Do not let the model invent page references. Keep the index's embedding model/dimension recorded and compatible with query embeddings.
- [ ] **K-07 — Establish a baseline and choose the final launch slice. 8h. Due 14 Jan. Depends K-04–K-06.** Evaluate development/validation data end to end, including routing/OCR; log correctness, citation support, abstention, latency, and total cost. Use the result to narrow chapters, tune routing, or change eligible providers. The locked holdout remains unopened.

**K exit:** an actual question can become a sourced answer through the shared backend, and the reviewer has approved the content used. Poor quality triggers scope reduction or more evaluation, not a larger prompt alone.

**S — Complete the useful learning loop. Budget: 45 hours. Gate: 4 February.**

- [ ] **S-01 — Implement the full solve workflow. 8h. Due 19 Jan. Depends K-07.** Text/photo → extraction → supported-topic decision → retrieval → answer artifact → delivery. Persist versioned intermediate outcomes needed for debugging without logging unnecessary student data. Test interrupted and resumed runs.
- [ ] **S-02 — Add OCR confirmation and unsupported-input behavior. 7h. Due 21 Jan. Depends S-01.** Ask for clarification when options, diagrams, or text are unreadable. Handle multiple questions, handwriting, unsupported chapters, and empty messages explicitly. Never silently guess cropped options or accept a fabricated reading.
- [ ] **S-03 — Implement verification and abstention. 8h. Due 26 Jan. Depends S-01/K-07.** Prefer verified keys for known problems; check citation support and output structure; use evaluated escalation rules for novel questions. Model agreement is one signal, not proof. Unresolved jobs end clearly, release reserved quota, and offer correction/reporting or bounded human review only if staffed.
- [ ] **S-04 — Add correct solution reuse. 6h. Due 28 Jan. Depends S-01/S-03.** Cache verified canonical solutions using source/question identity, normalized stem and options, numerical values, curriculum edition, and solution version. Semantic similarity may suggest a candidate but must not authorize answer reuse alone. Keep student-specific explanations separate.
- [ ] **S-05 — Implement bounded mistake explanation. 7h. Due 1 Feb. Depends S-03.** Ask for the student's answer or reasoning. Explain the observed mismatch and a relevant concept; treat inferred error categories as provisional. Do not infer a permanent weakness from a single photo or assert psychological reasons. Reviewer checks representative cases.
- [ ] **S-06 — Deliver reviewed follow-up practice. 5h. Due 3 Feb. Depends K-02/S-05.** Select 2–3 exercises from at least 60 approved practice items inside the development/content bank, never the holdout. Store answers and feedback. Defer automatically publishing novel AI-generated exercises until a separate validation path exists.
- [ ] **S-07 — Demonstrate the complete loop and meter its real cost. 4h. Due 4 Feb. Depends S-01–S-06.** Save reproducible examples covering correct answer, wrong attempt, practice, unreadable photo, uncertainty, and retry. Include routing, OCR, embedding, generation, verification, failed calls, storage/delivery, and support estimates in economics.

**S exit:** a small group of internal testers can complete solve → explanation → practice. A failure does not silently consume credit, invent a citation, or strand a job.

**C — Add the channel differences explicitly. Budget: 45 hours. Gate: 25 February.**

- [ ] **C-01 — Harden the Telegram adapter. 8h. Due 9 Feb. Depends B-05/S-07.** Validate webhook requests where supported, deduplicate update IDs, handle callbacks/expired actions/media downloads, and respect retries/rate limits. Preserve polling as an operational alternative where appropriate. Do not expose secrets in logs or URLs shown to users.
- [ ] **C-02 — Implement and test the Bale adapter. 8h. Due 15 Feb. Depends F-02/C-01.** Reuse common transport abstractions while testing actual Bale differences, authentication options, files, actions, and formatting. The documented webhook parameters differ from Telegram's; do not assume `secret_token` exists. Choose a supported transport/authentication strategy and test it. [Bale documentation](https://docs.bale.ai/).
- [ ] **C-03 — Implement the proven Eita bot interface. 10h base adapter allowance. Due 18 Feb. Depends successful F-02.** This task is valid only after a supported inbound bot route is demonstrated. Do not substitute a channel broadcaster or mini-app and mark it complete. If you approve a mini-app instead, replace this task and explicitly add **30–45 owner hours** for the surface, signed-session verification, uploads, navigation, compatibility, and review; platform review wait is extra. The release name/scope must change accordingly.
- [ ] **C-04 — Implement common conversation state and presentation. 7h. Due 22 Feb. Depends C-01–C-03.** Store workflow state in the backend, use opaque expiring action IDs, format Persian/Latin math safely, split long messages, and provide plain-text fallbacks. Every adapter renders the same canonical answer artifact.
- [ ] **C-05 — Complete onboarding and safe account linking. 6h. Due 24 Feb. Depends C-04/B-03.** Ask only essential grade/track/scope information. Link two accounts through proof of control on both sides, with expiring one-time codes. Never link by matching names/usernames or by unverified phone strings. Test replay, wrong account, unlinking, and quota behavior.
- [ ] **C-06 — Run the channel parity matrix. 6h. Due 25 Feb. Depends C-01–C-05.** Exercise new/returning user, text/photo, uncertain answer, practice, history, duplicate delivery, blocked bot, expired action, and restart on every supported channel. Record platform-specific limitations and final delivery success separately from job success.

**C exit:** all three requested bots actually complete the supported workflows. An unresolved Eita interface blocks this milestone; passing two platforms does not complete it.

**L — Make learning state and operations dependable. Budget: 45 hours. Gate: 18 March.**

- [ ] **L-01 — Record learning events and attempts. 8h. Due 2 Mar. Depends S-07/C-05.** Separate question exposure, self-reported understanding, attempted answers, corrected answers, and practice results. Make event writes idempotent and retain links to topic/content/run versions. Reprocessing a job must not duplicate learning credit.
- [ ] **L-02 — Build history and modest progress summaries. 7h. Due 4 Mar. Depends L-01.** Let a student retrieve prior answers, mistakes, and practice. Show observed counts and recent topic performance with sample sizes. Avoid invented mastery percentages, ranks, or promised score gains.
- [ ] **L-03 — Implement a simple next-practice rule. 7h. Due 9 Mar. Depends L-01/L-02.** Prioritize recently missed supported topics and allow the student to choose another topic. Keep rules explicit and testable. This does not require a full adaptive planner or forgetting model.
- [ ] **L-04 — Build the minimum operator console. 7h. Due 11 Mar. Depends B-03/L-01.** Protect operator access with strong authentication. Inspect failed runs, source versions, disputed answers, usage, and delivery state. Retry safely, disable a problematic item/provider, correct a source, and record an audit entry. An internal basic interface is enough.
- [ ] **L-05 — Implement correction and data lifecycle. 6h. Due 15 Mar. Depends L-04.** Version corrections, invalidate affected cache entries, and support user deletion/export. Propose raw image deletion after seven days and operational log retention of 30 days; confirm the actual policy before pilot enrollment. Keep deletion/audit exceptions explicit and reviewed.
- [ ] **L-06 — Add quota reservations and spending limits. 5h. Due 17 Mar. Depends B-04/S-07.** Reserve before costly work, settle once, release on failure/abstention according to the agreed policy, and cap user/global spend and concurrency. Test duplicate settlement and retry paths. Keep commercial entitlements separate from internal provider cost.
- [ ] **L-07 — Run internal-alpha acceptance. 5h. Due 18 Mar. Depends L-01–L-06/C-06.** Complete cross-user isolation, correction, deletion, quota race, queue restart, and graceful-failure scenarios. Freeze features before the planned break; do not enroll an unattended public pilot.

**Planned break — 20 March through 2 April.** Keep staging stopped or under a minimal maintenance arrangement. If you choose to operate an active service during this period, explicitly budget support time and adjust capacity. Do not treat these two weeks as hidden development hours.

**I — Prepare the Iranian production environment. Budget: 45 hours. Gate: 22 April.**

- [ ] **I-01 — Provision reproducible production infrastructure. 6h. Due 6 Apr. Depends F-03/F-06/B-07.** Deploy Go API/workers, Postgres/pgvector, private object storage, TLS, secrets, and monitoring. Keep staging isolated. Confirm actual domestic/international reachability and approved provider access. Choose a small deployment that you can restore; Kubernetes and multi-region orchestration are outside this release.
- [ ] **I-02 — Prove backup, recovery, and rollback. 8h. Due 8 Apr. Depends I-01.** Enable encrypted backups and database point-in-time recovery where available; restore into a clean environment. Proposed targets: recovery-point loss ≤1 hour for learning data and recovery time ≤4 hours. Payment events must be recoverable/reconcilable from durable records and the gateway. Verify migration rollback/forward-repair procedures.
- [ ] **I-03 — Build one approved domestic purchase flow. 9h. Due 13 Apr. Depends F-06/L-06/I-01.** Use the chosen gateway's documented flow and a registered merchant domain. Store integer amounts with explicit currency; normalize accounting consistently and display clearly in toman. Verify server-side before granting entitlement; callbacks alone are insufficient. Implement one-off purchase of a fixed-duration plan, with manual renewal. [ZarinPal integration example](https://www.zarinpal.com/docs/paymentGateway/connectToGateway), [currency handling](https://www.zarinpal.com/docs/paymentGateway/moreFeatures/currency).
- [ ] **I-04 — Test money and channel-specific purchase rules. 8h. Due 15 Apr. Depends I-03/C-06.** Test duplicate/forged callbacks, wrong amount/currency, canceled/late payment, network timeout after charge, reconciliation, refund, and single entitlement grant. Keep Telegram purchases disabled in this baseline. A later Telegram sale requires an approved Stars route and refund/support behavior. If Eita becomes an approved mini-app, follow its eNAMAD, external checkout, and publication requirements. [Telegram Stars](https://core.telegram.org/bots/payments-stars), [Eita publication requirements](https://developer.eitaa.com/docs/PublishingRequirements/).
- [ ] **I-05 — Test the experience on Iranian networks and devices. 5h. Due 19 Apr. Depends I-01/C-06.** Test real devices on MCI, Irancell, and at least one fixed connection where available; distinguish backend, messenger, and upstream-provider failure. Exercise slow upload, disconnect, duplicate retry, DNS/TLS failure, and provider outage. For any owned web pages, serve essential fonts/assets locally and avoid unnecessary foreign runtime dependencies. Store UTC; display Asia/Tehran and tested Jalali dates where relevant.
- [ ] **I-06 — Complete student-facing terms and support paths. 5h. Due 21 Apr. Depends F-06/L-05/I-04.** Publish concise Persian scope, prices/renewal terms, privacy/retention, limitations, refunds, contact and response hours, and deletion instructions. Review the intended minor-user consent/data handling and content permissions with appropriate local expertise. Do not present these tasks as a complete legal determination.
- [ ] **I-07 — Rehearse the production failure modes. 4h. Due 22 Apr. Depends I-01–I-06.** Disable the provider, restart a worker, delay outbound delivery, and simulate database/payment unavailability. Return clear temporary-unavailability states. Offer saved/verified content only where appropriate; never replace an unavailable grounded workflow with unapproved raw-model guessing. Confirm alerts reach the owner.

**I exit:** production infrastructure, support, approved purchase routes, recovery, and network behavior have evidence. Merchant approval is required before enabling paid access; a free pilot can proceed if its other gates pass.

**P — Run a bounded, observed pilot. Budget: 45 hours. Gate: 13 May.**

- [ ] **P-01 — Recruit and onboard a controlled pilot. 5h. Due 27 Apr. Depends I-07/L-07 and reviewer availability.** Start with 20 students, grow toward 50 only if support and spending permit. Obtain appropriate permissions and explain supported chapters and support hours. Ensure each channel has real testers. Invite explicitly; no unsolicited mass messaging.
- [ ] **P-02 — Operate the pilot and triage daily. 8h across the pilot. Due 29 Apr for first review; continue through 13 May.** Observe two full weeks, cap daily usage, record critical failures, and respond during stated hours. Owner support time is part of the 15-hour budget. If support exceeds the allocation, pause expansion and revise estimates.
- [ ] **P-03 — Run the frozen end-to-end holdout. 7h owner effort; teacher scoring separate. Due 4 May. Depends frozen S/K versions.** Run all 200 locked question families through real routing and the relevant text/photo path. Score final answer, explanation, citation, abstention, latency, and cost. Publish denominators and intervals; do not omit failed calls or disputed keys. Separate text, photo, known-problem, and novel-question results.
- [ ] **P-04 — Validate error explanation and practice. 6h owner coordination. Due 6 May. Depends P-02/P-03.** Have the reviewer inspect at least 50 diagnosis/feedback examples across correct attempts, conceptual errors, arithmetic errors, and ambiguous reasoning. Verify every selectable practice answer key; no unreviewed generated exercise should be delivered as authoritative.
- [ ] **P-05 — Measure practical value and economics. 7h. Due 10 May. Depends pilot activity.** Report onboarding-to-first-result completion, practice participation, repeat usage, unresolved-question rate, support time, and full per-answer cost. Review with five students and the teacher. Set paid limits using observed usage plus FX/provider-price stress; remove old unsupported margin/cache assumptions.
- [ ] **P-06 — Repair release blockers and rerun affected checks. 7h. Due 12 May. Depends P-02–P-05.** Prioritize wrong answers/citations, duplicate charge/entitlement, account leaks, stuck jobs, and channel failures. After a substantive model/content change, the exposed holdout is a regression set: arrange a fresh independent holdout or rebaseline the schedule. Do not repeatedly tune against the same test and call it independent.
- [ ] **P-07 — Hold the release decision. 5h. Due 13 May. Depends P-06.** Review every release gate below and record GO, NARROW SCOPE, or DELAY with named blockers. Record the actual supported chapters, cohort, platform surfaces, model/content versions, prices, and support capacity. Obtain your explicit scope choice if Eita behavior differs from the original bot request.

**R — Use the reserve for uncertainty, then release gradually. Budget: 15 planned hours + 45 protected hours.**

- [ ] **R-01 — Resolve overruns and external blockers. Reserve: up to 45h. Target window 15 May–4 Jun.** Use only for defects, fresh evaluation, platform approval work, or recovery failures. Record consumption by task. This reserve cannot justify a new subject, full app, or social feature. External waiting may still require a revised date.
- [ ] **R-02 — Freeze the release candidate and confirm the runbook. 5h. Due 3 Jun. Depends all gates and R-01 blockers cleared.** Pin versions, refresh source/terms checks, verify production backups, confirm responder availability, and prepare rollback and feature switches. Schedule deployment during supported daytime hours in Tehran.
- [ ] **R-03 — Deploy to a small canary group. 5h. Due 7 Jun. Depends R-02.** Start with roughly 10% of the intended cohort, under a fixed spend/concurrency cap. Observe for at least 48 hours with support staffed. Pause on wrong charges, data exposure, systematic answer errors, or delivery failure. Re-run a smoke flow on every channel.
- [ ] **R-04 — Open the public release and stabilize. 5h. Launch 9 Jun; review 11 Jun. Depends R-03 passing.** Open in controlled batches, publish honest supported scope, enable only approved sales surfaces, and monitor quality/cost/support. If any strict three-bot dependency remains unresolved, do not announce that all three bots shipped. Record the remaining backlog and the next two weeks' operational owner schedule.

**Release gates — proposed targets to validate, not current performance claims**

| Gate | Required evidence before public launch |
|---|---|
| Platform scope | All three requested bots demonstrate supported inbound interaction and the full approved user journey. Any mini-app substitution has an explicit revised scope. |
| Provider eligibility | Documented eligibility for the operator, geography, age group, data handling, and commercial use; working access from production. |
| Answer quality | On the frozen 200-question holdout: at least **95% correct among answered supported questions**, and at least **70% coverage** of eligible readable supported questions. Report n, uncertainty intervals, and results by text/photo and chapter. This is a proposed limited-scope release gate, not a claim of 95% accuracy on all student questions. |
| Honest coverage accounting | Show total submissions, eligible/readable supported items, answered items, abstentions, and failures. Determine readability/scope independently of solver success. An unanswered eligible question remains in the coverage denominator. |
| Source support | All emitted citations resolve to stored sources and versions; at least **95%** of reviewed answer explanations are supported by their cited evidence. Unsupported/misleading citations are corrected before release. |
| Mistake feedback | On at least 50 reviewed cases, at least **90%** are rated educationally useful and free of an asserted unsupported diagnosis. Ambiguous evidence is acknowledged. |
| Photo handling | Real phone-photo cases included; ambiguous extraction asks for clarification. Printed-input support is explicit. Handwriting/complex diagrams remain unsupported unless separately validated. |
| Runtime | Proposed staging/pilot targets: event acknowledgment p95 ≤2 seconds from server receipt; ordinary supported solve p95 ≤30 seconds from receipt to available result; a terminal result/failure by 90 seconds under documented normal load. Track delivery latency separately. Adjust public expectations to measured behavior. |
| Reliability | ≥99% of pilot jobs reach a recorded terminal state; zero known duplicate charges or quota settlements; no permanently lost accepted jobs in crash/retry tests. Track successful useful delivery separately from terminal-state completion. |
| Access and privacy | Cross-user access tests pass, secrets absent from outputs/logs, upload retention/deletion verified, account linking resists replay, and operator actions are audited. |
| Payment | Duplicate/forged callbacks and currency/amount mismatches cannot grant extra access. Cancellation, reconciliation, refunds, and user support are tested. Paid channels comply with their current rules. |
| Recovery | A clean restore and rollback rehearsal meets the chosen RPO/RTO targets; payment reconciliation is demonstrated. |
| Iran operation | Reachability and behavior recorded across the selected Iranian networks; provider outage and slow uploads handled without misleading success. |
| Pilot value and support | At least 20 participants with two weeks of observation; evidence of completing the solve/practice journey; critical feedback addressed; support fits the owner's available hours. Numbers describe the pilot, not proven market demand. |
| Costs | Daily/monthly spend caps enabled; measured cost/answered question and support burden fit the chosen free/paid limits under a documented stress scenario. |

If a quality gate fails, narrow the supported slice, improve/review content, or change the evaluated implementation and test again. Never raise apparent accuracy by hiding unanswered or difficult cases. If a locked set is used for fixes, retain it as regression coverage and budget fresh independent release evidence.

**Architecture boundaries to give every coding AI**

- Production application logic and orchestration are **Go**. Existing Python research may remain offline reference/tooling; it is not the production service API.
- Start with a modular application and workers from the same codebase. Domain boundaries: identity, curriculum/content, learning, workflows, billing, channel adapters, and operations.
- Use Postgres as transactional truth; pgvector for initial retrieval; private object storage for files. Prefer a small reliable job system. Add Redis only for a concrete queue/cache/rate-limit need, rather than because a diagram contains it.
- A job's accepted state, durable effects, and outbound delivery state must survive failure. Use transactional handoff/outbox patterns where needed; design for duplicate delivery rather than claiming exactly-once behavior from external platforms.
- Store canonical answers independently from their channel formatting and student-specific explanation. Version source, prompt, model, and answer data so a correction can invalidate the right cache entries.
- Persist learning evidence before attempting advanced personalization. A simple explicit topic-practice rule is sufficient for the first release.
- Keep provider selection behind interfaces. Any fallback must meet the same eligibility and minimum quality requirements; an outage does not authorize an unchecked provider/model.
- The LLM cannot authorize a payment, grant a role, merge accounts, delete data, or execute arbitrary retrieved instructions. Those decisions remain in deterministic backend code.
- Build only the operator functions needed to run this release. Public community content is deferred, so do not promise an automatic human/community answer queue that nobody staffs.
- Future apps should reuse stable user IDs, versioned API contracts, answer/history records, and entitlements. No separate mobile backend should be necessary.

**How to execute this with AI at 15 hours/week**

Use roughly **9 hours for small implementation tasks, 3 hours for review/testing, and 3 hours for integration, user/reviewer coordination, and planning**. These total 15 hours and are already included in task estimates. During the pilot, support displaces feature development.

Work in 2–4-hour batches. Give one coding agent a narrow deliverable. A second agent may inspect the diff, design an independent failure test, or review a different module. Keep schema/auth/payment changes under one integrating owner. More generated code is not the completion metric.

For each task, give AI this brief:

> Implement task [ID] from this plan. Read the existing code and relevant domain decision first. The goal is [observable behavior]. Dependencies are [IDs]. Stay within [specific files/module]. Preserve the Go/shared-backend requirement. Handle [failure cases]. Add only the tests needed to verify the behavior and its risks. Do not change pricing, expand product scope, access production accounts, run paid bulk jobs, or publish anything. Return the diff, commands actually run, results, remaining risks, and a short demonstration procedure.

Before accepting a task:

- [ ] Read the changed behavior and sensitive code yourself, especially auth, money, concurrency, and deletion.
- [ ] Run the relevant tests; do not accept an agent's claim without output/evidence.
- [ ] Exercise the happy path and one meaningful failure in staging.
- [ ] Review migrations and rollback/repair behavior when data changes.
- [ ] Record estimated versus actual hours, provider/content versions, and the demonstrated acceptance result.
- [ ] Check the task off only when its completion condition holds. Keep blocked work visibly blocked.

At each weekly review: select the next 15 hours by dependency, account for support, and update the forecast. If a task exceeds its estimate by more than 50%, stop expanding it and diagnose the cause. If cumulative delay exceeds one week, consume the named reserve or move dates visibly. Unused reserve can bring launch forward only after all release gates pass.

AI can draft code, schemas, fixtures, extraction candidates, test cases, and support copy. You remain responsible for merchant/identity submissions, account ownership, spending decisions, scope changes, publication, and reviewing the final implementation. Qualified humans must adjudicate answer keys and educational explanations; a model cannot be the sole judge of its own correctness.

**External effort and cash planning**

| Item | Estimate / action | Deadline |
|---|---|---|
| Subject reviewer | 60–90 expert hours, separate from owner time; agree hourly/project fee | Recruit by 25 Nov; initial content through Jan; evaluation/pilot through May |
| Gateway/business setup | Owner coordination is budgeted; fees and approval time require a current quote | Start by 25 Nov; usable approval before I-03 |
| Hosting/database/storage/backups | Obtain a monthly quote for staging + a small production deployment and a tested recovery option | First quote by 26 Nov; refresh before 6 Apr |
| AI/OCR/embeddings | Quote only eligible routes; measure actual full-pipeline cost during K/S | Baseline by 14 Jan; launch limits by 10 May |
| Legal/content review | Confirm necessary local review and source permissions; obtain a scoped quote | Initial requirements by 25 Nov; resolved before pilot |
| Domain/TLS/optional SMS | Avoid making SMS mandatory for initial account creation; price any recovery/OTP service actually needed | Before the corresponding integration |
| Pilot/support | Owner allocation is already included; arrange backup coverage if unavailable | Before 24 Apr |

Do not reuse the old documents' AI-price or margin estimates. A working launch cash estimate is: **one-time setup + reviewer hours × agreed rate + months of fixed hosting + measured expected requests × full variable cost + support/payment fees + an explicitly chosen cash reserve**. Keep foreign-currency exposure separate from toman revenue and rerun the model at a higher exchange rate/provider price. No current vendor quote or exchange rate has been assumed in this plan.

**If you need an earlier release**

The safe acceleration is a smaller, clearly named pilot: one chapter, reviewed problem bank, no payment, no generated practice, and limited enrollment. It still requires an eligible provider, trustworthy sources, identity isolation, and demonstrated channel support. Additional reviewers or a second developer can shorten particular tasks; adding more AI agents alone does not remove integration or verification work. A two-bot pilot or an Eita mini-app would require an explicit change to your current three-bot scope.

**After this release — estimates only, not part of the June commitment**

| Follow-on | Owner effort after stable bots | Entry condition |
|---|---:|---|
| Expand to another reviewed chapter | 12–24h plus subject-review effort | Existing quality/cost targets hold |
| Independent web/PWA client | 60–100h | Stable API, account linking/recovery, and proven retention |
| Mobile application | 100–180h plus store/review lead time | Reuse proven API; verify distribution/payment policies for intended stores |
| Exam-sheet analysis | 50–90h plus a separate labeled evaluation set | Reliable answer/question mapping and operational capacity |
| Adaptive planning/review | 40–70h plus learning-method validation | Sufficient trustworthy attempt history |
| Community or live rooms | Separate plan and staffing estimate | Moderation/support model and economics established |

At 15 hours/week, ongoing operations reduce the capacity available for these additions. Re-estimate after the pilot rather than attaching all future features to a fixed calendar now.

**Planning evidence and maintenance**

The local research package establishes intent and experimental starting points: system architecture, feature anatomy, corpus plan, subject strategy, and the experiment README. See the [research handoff](feasibility/research-handoff.md) for their external location, availability, and handling requirements. The existing solve demo, small evaluation sets, static mockups, and file inventories are inputs to development; they are not production-readiness evidence.

External capabilities and policy findings above were checked on **11 November 2026** and are linked beside the affected decisions. Recheck before implementation and again at release freeze. This plan proposes engineering targets and effort budgets; it does not certify regulatory compliance, API approval, model accuracy, market demand, or a guaranteed launch date.
