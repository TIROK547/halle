# F-02 — Channel capability preflight

Checked **13 November 2026 (Asia/Tehran)**. Status: **documentation reviewed; no development-account test performed; F-02 remains open**. The required milestone is three bots sharing one Go backend. No mini-app substitution has been approved.

## Evidence matrix

“Documented” means the official reference describes the capability; it does not prove account access, reachability from the intended host, or the complete Halle journey.

| Required capability | Telegram | Bale | Eita |
| --- | --- | --- | --- |
| Receive private text/photo | Documented: `Update.message`, `text`, `photo`; retrieve image with `getFile` | Documented: `Update.message`, `text`, `photo`; `getFile` | **Not established** for private-chat bot messages |
| Identify the interacting user | `Message.from.id` / `CallbackQuery.from.id` through trusted API transport | Same documented fields through trusted API transport | Signed web-app `initData` documented; this is a different interaction surface |
| Reply | `sendMessage` | `sendMessage` | Opt-in outbound app messaging documented |
| Handle an action | Inline `callback_data` → `callback_query` → `answerCallbackQuery` | Same documented sequence, with client-version caveat below | Web-app interaction documented; native bot callback receipt not established |
| Receive updates | `getUpdates` or HTTPS `setWebhook` | `getUpdates` or HTTPS `setWebhook` | Neither equivalent inbound bot method established by reviewed docs |
| Live acceptance | Pending | Pending | Blocked on identifying a supported inbound interface |

Sources: [Telegram Bot API](https://core.telegram.org/bots/api), [Bale Bot API](https://docs.bale.ai/), [Eita architecture](https://developer.eitaa.com/docs/ArchitectureOverview/), [Eita identity validation](https://developer.eitaa.com/docs/Develop/AuthorizationViaHash/), [Eita outbound messages](https://developer.eitaa.com/docs/Develop/SendMassage/).

## Constraints that affect the spike

- **Telegram:** polling and webhooks are mutually exclusive; updates expire after 24 hours. Default hosted `getFile` downloads are limited to 20 MB, with download links valid for at least one hour. `setWebhook.secret_token` supplies a header to validate. Platform user IDs require 64-bit storage. [Official API](https://core.telegram.org/bots/api)
- **Bale:** retains the last 2,000 updates for 24 hours. `getFile` documents a 20 MB limit and one-hour link validity. `setWebhook` documents only `url` and ports 443/88; Telegram's `secret_token` parameter is **not documented** here. Old clients may lack callback acknowledgement support; the reference flags callback IDs beginning with `1` and suggests a message fallback. Do not assume Telegram parameter parity. [Official API](https://docs.bale.ai/)
- **Eita:** the reviewed architecture is an HTTPS app loaded in a WebView/iframe. Its outbound API requires user permission and consumes message credits allocated according to interaction. These features do not establish inbound private-chat text/photo delivery. This is an evidence gap, **not a claim that no such interface can exist**. [Architecture](https://developer.eitaa.com/docs/ArchitectureOverview/), [outbound messaging and credits](https://developer.eitaa.com/docs/Develop/SendMassage/)
- **Eita identity, if a future scope change is chosen:** validate `initData` server-side and enforce freshness; the optional additional hash-verification service documents one-minute, single-use validation and a 20-request/second ceiling. Never trust a browser-supplied user ID alone. [Hash validation](https://developer.eitaa.com/docs/Develop/AuthorizationViaHash/), [additional verification](https://developer.eitaa.com/docs/Develop/ValidateHash/)
- **Payments:** keep Telegram free in this baseline; digital-service purchases inside Telegram require Stars. This preflight does not establish any merchant or settlement route. [Official payment requirements](https://core.telegram.org/bots/payments-stars)

Bale retrieval note: the web research fetch failed, but direct HTTPS retrieval of the official HTML succeeded. The findings above were read from that response, not a third-party SDK.

## Manual development-account acceptance procedure

Owner prerequisites: dedicated development bots, two consenting adult test accounts, a small synthetic Persian text/photo fixture, and an API client that keeps tokens and raw responses private. No student material or AI provider is needed. Use polling first; do not alter an existing production bot's webhook.

Run separately for Telegram and Bale. The official request bases are `https://api.telegram.org/bot<TOKEN>/` and `https://tapi.bale.ai/bot<TOKEN>/` respectively. Replace placeholders only in the private API client; never save a token-bearing URL in Git, logs, screenshots, or shared evidence.

| Step | Request / user action | Required observation |
| --- | --- | --- |
| 1 | `POST getMe`, then `POST getWebhookInfo` | Correct development bot; empty webhook URL before polling. If occupied, stop and resolve the development-account configuration. |
| 2 | Account A starts the bot and sends `F02 text A`; call `POST getUpdates` with `{"timeout":20,"limit":10}` | A private message with stable sender/chat IDs and the exact text. |
| 3 | Account A sends the fixture as a photo; poll again | A photo message; call `POST getFile` with its `file_id` and privately download the returned path. Confirm the image is readable. |
| 4 | `POST sendMessage` with `{"chat_id":<CHAT_ID>,"text":"F02 received","reply_markup":{"inline_keyboard":[[{"text":"Continue","callback_data":"f02:continue"}]]}}` | A visible reply and button in the same private chat. |
| 5 | Tap Continue, poll, then `POST answerCallbackQuery` with `{"callback_query_id":"<CALLBACK_ID>"}` | Callback belongs to account A, contains `f02:continue`, and produces appropriate client feedback. Check Bale's older-client fallback if encountered. |
| 6 | Repeat text/photo/action with account B | Distinct sender identity and responses confined to the correct chat. |
| 7 | Preserve a sanitized record, then advance polling `offset` to highest handled `update_id + 1`; repeat poll | Handled events no longer reappear. Record any duplicates or unexpected ordering; this does not prove application idempotency. |
| 8 | Repeat from the intended host/network once selected | Record connection, download, reply and callback results independently of laptop success. |

These are bounded spike steps, not production code. Polling offsets advance only after the observation is recorded. A production receiver will need durable acceptance and duplicate handling under B-04. Before a webhook-based deployment, separately demonstrate request authentication and retry behavior for that channel; Bale's undocumented secret-header support remains an explicit question.

## Eita stop condition and next evidence

Within F-02's six-hour total timebox, obtain an official supported interface reference or development-account access that demonstrates **private-chat text + photo receipt → sender identity → reply → action receipt**. Outbound channel posting, an app-open button, and a web upload form do not satisfy this bot requirement.

Prepared question for official developer support (not sent):

> Does Eita support receiving a user's private-chat text and photo messages through a bot API? Please provide the official receive/update interface, authentication method, file retrieval, stable sender identifier, interactive action callbacks, account eligibility, and delivery limits. The requirement is a chat bot, rather than a hosted mini-app or outbound channel publisher.

If unproven by the timebox, record **BLOCKED** and ask the owner to choose waiting, a two-bot scope, or a separately estimated Eita mini-app. Until that decision, the requested three-bot milestone remains unresolved.

## Evidence to attach before closing F-02

For each channel, record the test date/time, operator, pseudonymous development-bot/account labels, client versions, host/network, steps passed/failed, sanitized request/response shapes, image readability, action outcome, limitations, and private evidence location. Keep raw tokens, personal account IDs and token-bearing download URLs out of this repository. Assign an owner and next date to every failure. Documentation review alone cannot close this task.
