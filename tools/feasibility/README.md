# F-02 channel diagnostic

Temporary Python standard-library tooling for the feasibility spike; this is not a production service or a replacement for the planned Go backend. Requires Python 3.10+ and no installed packages.

The owner confirmed dedicated Telegram and Bale development bots are ready on 13 November 2026. Credentials have not been supplied or inspected. Run only against dedicated development bots with synthetic messages from consenting adult testers.

1. In each bot's private chat, send a synthetic text and a clear photo of printed sample text from each of two test accounts.
2. Run from the repository root in a local terminal:

   ```sh
   python3 tools/feasibility/channel_probe.py telegram
   python3 tools/feasibility/channel_probe.py bale
   ```

3. Paste the corresponding token into the hidden terminal prompt. Do not paste it into chat or put it in command-line arguments.
4. Inspect the sanitized JSON. It reports bot authentication and private text/photo/action observations with ephemeral tester labels. No message text, usernames, platform IDs, file IDs, callback contents or credentials are printed or saved.

The probe calls only `getMe`, `getWebhookInfo` and a single `getUpdates` snapshot. It refuses an existing webhook rather than changing it. It does not advance polling offsets, so repeated runs may see the same pending events. Stop other pollers while testing; only the first 100 pending updates are inspected. Labels are local to one response and cannot be compared across runs/channels. Network/API failures are sanitized, response size is bounded, and redirects are refused.

This check does **not** establish freshness, durable processing, file download/readability, replies, button creation/acknowledgement, host reachability, or full channel parity. Existing callbacks may be observed, but the tool does not create them. Continue with the [manual acceptance procedure](../../docs/feasibility/channel-capabilities.md) to prove those remaining interactions. F-02 stays open and Eita inbound support remains unresolved.

No retry loop or background process runs. Exit code 0 means this snapshot was read successfully, not that the integration passed. Exit 1 indicates a refused/failed probe; exit 130 indicates cancellation. Do not share raw network traces containing token URLs.

Offline verification:

```sh
python3 -m unittest discover -s tools/feasibility -v
```

Tests use fake API responses only. They cover webhook refusal, account distinction, content redaction, no offset advancement, mutation refusal, malformed responses and token-bearing network failures.
