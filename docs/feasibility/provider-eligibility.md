# F-03 — AI/OCR route eligibility

Checked **13 November 2026 (Asia/Tehran)**. Status: **no eligible operational route selected; F-03 remains open**. This is engineering procurement evidence, not a complete legal determination.

## Actual intended use

The owner confirmed an **Iran-based operator** and **Iranian learners aged 15 and older, including 15–17-year-olds and adults**, starting with grade-12 biology chapters 1–2. Provider and host are not selected. The route must support commercial delivery, Persian text and printed-photo extraction, grounded explanations and embeddings/retrieval as needed. Each component, including OCR, must meet the access and data requirements; permission for one model does not cover the rest of the pipeline.

The owner selected a minimum age of **15**. Do not describe the application as adult-only or infer provider permission for minors from the product's chosen age range.

## Current route assessment

| Route | Evidence | Status for this project |
| --- | --- | --- |
| Direct Gemini API / AI Studio research setup | Published terms exclude API clients directed toward or likely accessed by under-18s and restrict availability to listed regions. Iran is absent from the list. [Terms](https://aistudio.google.com/docs/terms), [regions](https://aistudio.google.com/docs/available-regions) | **Do not select under these published terms** for the stated audience/location. No live test run. The research proxy setup does not resolve this mismatch. |
| Liara AI | Text/image inputs and consumption accounting documented. Its FAQ says prompt/response contents are not stored; operational-log retention is separately documented by plan, and the general privacy policy allows international transfers. [Inputs](https://docs.liara.ir/ai/foundations/prompts/), [usage](https://docs.liara.ir/ai/details/full-log-request/), [FAQ](https://docs.liara.ir/ai/faq/), [logs](https://docs.liara.ir/ai/details/logs/), [privacy](https://liara.ir/privacy-policy/) | **Candidate only.** Reviewed [terms](https://liara.ir/terms/) do not establish permission for this operator, mixed-age audience and exact upstream model route. Obtain written clarification, upstream data terms and a quote. |
| AvalAI | Text/image support and settled-usage accounting documented. Vendor policy distinguishes its handling of content/metadata from upstream policies; retention depends on route/provider/contract. [Vision](https://docs.avalai.org/fa/guides/vision), [pricing/accounting](https://docs.avalai.org/fa/pricing), [content policy](https://docs.avalai.org/fa/safety/content-policy), [data controls](https://docs.avalai.org/fa/guides/data-controls) | **Candidate only.** Iranian operator/end users, minors, commercial use and exact upstream permissions are not established by the reviewed documentation. No account or test run. |
| Self-hosted model/OCR | No model, license, GPU host, quality evidence or cost quote selected | **Unassessed alternative.** Requires separate licensing/access review, operations and quality work, and an explicit estimate/scope update. Not a free fallback. |

The candidate list is a small first-session preflight, not an exhaustive market survey or approval of either intermediary. Gateway reachability and domestic billing do not by themselves establish permission from the underlying provider. A gateway forwarding to the same restricted route cannot be marked eligible without applicable evidence.

## Qualification record required before a test

For each candidate capture:

1. Contracting operator/entity and country; intended Iranian end users; supported ages and relevant consent requirements. Do not change the declared population to fit an account form.
2. Exact provider, model/version, OCR/vision and embedding route, host/processing regions and upstream/subprocessor arrangement. Record which terms govern each component.
3. Written clarification of commercial educational use for the actual operator and audience, including any age/geography ambiguity. Keep private correspondence outside Git; reference a sanitized evidence ID/date here.
4. Prompt/image/output retention; metadata and abuse logs; training use; deletion and backup behavior; human access; subprocessors. A claim about gateway storage must not be generalized to upstream storage.
5. Account/billing eligibility, currency, conversion and settlement basis, quota/rate limits, price per component, timeout/retry charges, support contact and outage terms. No quote has been obtained.
6. Access from the intended production host and networks. No production host has been chosen and no reachability test was performed.

All required items must pass or have a justified, recorded resolution before the candidate is tested on data. Written answers and terms must agree; a working API response is not eligibility evidence. Costs require an owner-selected spike ceiling before paid calls.

## Vendor clarification draft (not sent)

We are building a commercial Persian educational assistant operated from Iran for Iranian learners aged 15 and older, including 15–17-year-olds and adults. It receives text and printed-question photos and returns textbook-grounded explanations through messenger bots. Please confirm whether your exact proposed model/OCR/embedding route permits this operator, location, age group and commercial use, including the underlying provider's terms. Please identify the upstream provider/hosting arrangement, applicable contracts, processing locations, training use, prompt/image/output and metadata retention, deletion behavior, billing/access requirements, and a current cost/rate-limit quote. If any part is unsupported, please state the limitation explicitly.

The project owner decides whether and where to send this request. No vendor has been contacted in this session.

## Bounded operational spike after qualification

Within F-03's **six-hour owner timebox**, use a small permissioned development sample (proposed 8 cases: two typed questions, two clean printed photos, one low-quality photo, one cropped-options photo, one out-of-scope question, one ambiguous question). Do not use locked holdout data or live student identifiers. Have the reviewer establish expected extraction/scope/key outcomes first.

Record host/route/model/version, request outcome, extraction of stem/options, structured-output behavior, abstention/clarification, latency and full settled cost including failures. Exercise timeout/cancellation and a low account limit. Demonstrate OCR, solving and embeddings if separate routes are selected. This is an access/viability sample, not a quality or launch accuracy claim.

If no route can be qualified within the timebox, record **blocked**, owner and next clarification date. Re-estimate self-hosting or continue independent domain work only under a recorded plan. Do not silently activate the historical proxy or fallback model.

## To close F-03

- [ ] Select a route with the documented eligibility, data handling, billing and commercial evidence above.
- [ ] Confirm intended host and owner-authorized test spending limit.
- [ ] Run the representative operational sample and record limitations, versions and costs.
- [ ] Record an accountable owner, evidence date and a recheck before release.

Owner: project owner for vendor/contract/spend decisions; AI assistance for evidence and bounded tooling. Baseline deadline: **24 November 2026**. No revised deadline or owner hours have been recorded yet.
