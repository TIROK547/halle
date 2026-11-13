# F-01 — Initial product contract

Version: **0.1, 13 November 2026 (Asia/Tehran)**. Status: **partially decided; not frozen**.

## Decisions confirmed by the owner in session 1

| Decision | Selected scope |
| --- | --- |
| Subject and chapters | Grade-12 biology, the first two chapters of the book |
| Audience | Learners aged 15 and older, including 15–17-year-olds and adults |
| Minimum supported age | 15; younger learners are outside the initial release |
| Initial free allowance | 5 completed questions per Halle account/day, plus 2–3 reviewed follow-up exercises per answer; failed, unsupported and unanswered requests do not consume it |
| Operator | Iran |
| Reviewer | Not yet recruited; prepare the [reviewer brief](reviewer-brief.md) |
| Provider and hosting | Not selected |

Working chapter labels in the research vocabulary are **۱ — مولکول‌های اطلاعاتی** and **۲ — جریان اطلاعات در یاخته**. These labels were initially taken from `tools/halle_experiments/curriculum.zist12.txt` and now match the [recovered 1405 textbook](textbook-recovery.md). Its chapter boundaries and pagination are recorded; permission, authenticity comparison and reviewer approval remain pending. No particular edition or exam cohort has been selected. Chapters outside 1–2 are out of scope, including chapter 3 inheritance problems from the research experiments.

The requested delivery remains Telegram, Bale, and Eita bots using a shared Go backend. F-02 has not established an Eita inbound bot route. This contract does not silently substitute a mini-app or reduce the channel count.

## Proposed input and output contract

These are concrete defaults for owner/reviewer review, not settled release promises:

- One Persian biology question per submission: typed text or a clear photo of printed text, with all answer options visible for multiple-choice questions. Short-answer questions are allowed within the reviewed chapter boundaries.
- A photo may contain incidental drawings, but questions that require interpreting a diagram, handwriting, a full exam sheet, or cropped/missing text remain unsupported until separately evaluated. Chapter membership alone does not guarantee an answer.
- For uncertain OCR, show the extracted question/options and ask for confirmation or a replacement photo. Do not silently invent missing text.
- Return an answer and bounded explanation with references to stored, versioned textbook evidence. Display actual edition/page references from the source registry; never model-invented citations.
- Ask for the student's attempted answer or reasoning before describing a mistake. Distinguish an observed mismatch from an uncertain hypothesis about the cause.
- Offer 2–3 exercises from the approved practice bank when available, save attempts, and allow later retrieval. Do not generate unreviewed authoritative practice on demand.
- When no supported answer can be justified, return an explicit unresolved state and correction/reporting action. No promise of a human answer unless reviewer support is separately staffed.

## Three student journeys

| Journey | Exact sequence | Visible success | Failure behavior |
| --- | --- | --- | --- |
| 1. Ask and understand | Start → see supported chapters → submit one text/photo question → confirm extraction if necessary → receive progress → open sourced answer | Student can read the solution and identify its book edition/page references | Outside scope: explain supported input. Unreadable: request clearer photo/text. Uncertain/provider unavailable: explicit terminal state, no fabricated answer. |
| 2. Understand an attempt and practice | From a supported answer → enter attempted answer/reasoning → receive bounded feedback → try 2–3 reviewed exercises → receive checked feedback | Attempt and practice results are saved with source/answer versions | Insufficient reasoning: ask one clarification rather than assert a cause. No reviewed practice: say so, do not fabricate exercises. |
| 3. Return and continue | Open history → select a past attempt → read the saved answer/feedback → choose a simple next-practice suggestion → submit a new attempt | The user's own history survives restart; suggestion follows explicit recent-topic/mistake evidence | Empty history: invite first question. Corrected answer: show the newer version. No account can retrieve another user's records. |

Initial onboarding asks only the information required for supported study scope. A phone number is not compulsory. Account linking later requires proof of control on both channels; matching usernames is insufficient.

## Selected free allowance and proposed resource behavior

Owner-selected allowance: **5 successfully answered new questions per Halle account per day**, plus **2–3 reviewed follow-up exercises per answer**; failed, unsupported and unanswered requests do not consume it. Proposed counting details for review: reset by Asia/Tehran calendar day and offer at most one practice set per answered question. Reading history and submitting answers to that offered practice set do not consume another question allowance. Duplicate delivery must not double-count. Repeating a new solve request does consume allowance, even if its canonical answer is cached.

For enforcement, the quota belongs to the authenticated **Halle user account**, not a verified natural person. Unlinked platform accounts may initially have separate Halle identities; the product does not claim to recognize the same person across them. Verified linking must combine the day's consumed/reserved usage into a shared allowance without granting an extra reset. Identity/linking behavior will be implemented and tested in B-03/C-05.

Proposed resource defaults: one active solve per learner; one JPEG/PNG photo up to 5 MiB; typed question text up to 8,000 Unicode code points. These are application proposals, not assertions about every channel's API limits. Test each adapter before freezing them.

Reserve allowance before costly work; settle once after a supported answer artifact is ready; release on unreadable, unsupported, failed, or abstained requests. A delivery retry must not charge again. Separate abuse/rate controls still bound repeated failed requests. F-07 must choose daily/monthly global monetary caps and stop behavior before any paid provider use; this proposal does not authorize spending.

Telegram access is free in the baseline. A domestic fixed-duration purchase route is a later, conditional release feature on approved channels; no prices, checkout links, merchant, or paid entitlement rules are set in this session.

## Persian messages for review

| State | Draft student-facing wording |
| --- | --- |
| Welcome/scope | «فعلاً سؤال‌های فصل‌های ۱ و ۲ زیست‌شناسی دوازدهم را بررسی می‌کنم. هر بار یک سؤال تایپ‌شده یا عکس واضح از متن چاپی بفرست.» |
| Outside chapter scope | «این سؤال خارج از فصل‌های ۱ و ۲ زیست‌شناسی دوازدهم است. فعلاً نمی‌توانم پاسخ مستند و قابل اتکایی برایش ارائه کنم.» |
| Several questions | «لطفاً هر بار فقط یک سؤال بفرست و اگر تستی است، همهٔ گزینه‌ها را هم در عکس یا متن بیاور.» |
| Unreadable/missing options | «متن سؤال یا بعضی از گزینه‌ها واضح نیست. لطفاً عکس واضح‌تر و کامل‌تری بفرست یا سؤال و گزینه‌ها را تایپ کن.» |
| Handwriting/diagram required | «فعلاً خواندن دست‌خط یا تحلیل شکل این سؤال را پشتیبانی نمی‌کنم. اگر سؤال بدون شکل قابل پاسخ است، متن کامل آن را بفرست.» |
| Uncertain answer | «با منابع فعلی نتوانستم پاسخ قابل اتکایی پیدا کنم. این تلاش از سهمیهٔ سؤال‌هایت کم نمی‌شود.» |
| Missing reasoning | «کدام پاسخ را انتخاب کردی و چطور به آن رسیدی؟ برای توضیح اشتباه، به همین تلاش تو نیاز دارم.» |
| No reviewed practice | «برای این موضوع هنوز تمرین تأییدشده‌ای آماده نیست. می‌توانی پاسخ ذخیره‌شده را مرور کنی یا سؤال دیگری بفرستی.» |
| Temporary failure | «پردازش این سؤال فعلاً انجام نشد. این تلاش از سهمیهٔ سؤال‌هایت کم نمی‌شود؛ لطفاً کمی بعد دوباره امتحان کن.» |

## Excluded from this release

Other chapters/subjects; whole-sheet grading; rank or score predictions; advanced mastery percentages; adaptive weekly planning and full spaced repetition; social feeds, chat, live rooms and marketplaces; generated unreviewed practice; parent/teacher dashboards; transferable currency/payouts; independent mobile/web apps; fine-tuning and full concept graphs. An infrastructure page for legal information/payment callbacks is not a student web application.

## Freeze checklist

- [x] Owner selected chapters 1–2, ages 15+, and the five-question daily free allowance with reviewed follow-ups.
- [ ] Owner and reviewer confirm question formats, diagram exclusions, and the three journeys.
- [ ] Owner/reviewer confirm quota counting details and proposed resource limits, or record replacements.
- [ ] Confirm official textbook edition and target cohort with F-06.
- [ ] Reviewer approves Persian wording and scope boundaries.
- [ ] Record owner/reviewer names or private role references and approval date.

F-01 remains unchecked until owner and reviewer can describe the same bounded release. A complete draft is not a frozen contract.
