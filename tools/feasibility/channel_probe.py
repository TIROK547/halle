"""Read-only F-02 diagnostic; temporary tooling, not the production backend."""
import argparse
import getpass
import json
import re
import sys
import urllib.request

HOSTS = {"telegram": "api.telegram.org", "bale": "tapi.bale.ai"}
LIMIT = 2 * 1024 * 1024


class ProbeError(Exception):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise ProbeError("Redirect refused")


class API:
    def __init__(self, channel, token):
        if not re.fullmatch(r"[A-Za-z0-9_:-]+", token):
            raise ProbeError("Invalid token format")
        self.base = f"https://{HOSTS[channel]}/bot{token}/"
        self.opener = urllib.request.build_opener(NoRedirect())

    def call(self, method, payload=None):
        if method not in {"getMe", "getWebhookInfo", "getUpdates"}:
            raise ProbeError("Method not allowed by read-only probe")
        req = urllib.request.Request(
            self.base + method,
            data=json.dumps(payload or {}).encode(),
            headers={"Content-Type": "application/json"},
        )
        try:
            with self.opener.open(req, timeout=30) as response:
                body = response.read(LIMIT + 1)
            if len(body) > LIMIT:
                raise ProbeError("Response exceeded diagnostic size limit")
            result = json.loads(body)
            if not isinstance(result, dict) or result.get("ok") is not True:
                raise ProbeError("API rejected request; inspect credentials/account privately")
            return result["result"]
        except ProbeError:
            raise
        except Exception:
            # Exceptions and API descriptions may contain token-bearing URLs.
            raise ProbeError("Request failed; check network, credentials and API availability") from None


def probe(api):
    me = api.call("getMe")
    if not isinstance(me, dict) or me.get("is_bot") is not True:
        raise ProbeError("Account is not a bot")
    webhook = api.call("getWebhookInfo")
    if not isinstance(webhook, dict) or "url" not in webhook:
        raise ProbeError("Unexpected webhook response")
    if webhook["url"]:
        raise ProbeError("Webhook is configured; polling refused without changing it")
    updates = api.call("getUpdates", {"timeout": 0, "limit": 100})
    if not isinstance(updates, list):
        raise ProbeError("Unexpected updates response")
    # Ephemeral labels prove distinction only within this response; no IDs leave memory.
    users = {}
    observations = []
    for update in updates:
        callback = update.get("callback_query")
        event = callback or update.get("message") or {}
        message = event.get("message", {}) if callback else event
        sender = event.get("from", {}).get("id")
        if message.get("chat", {}).get("type") != "private" or not isinstance(sender, int):
            continue
        label = users.setdefault(sender, f"tester-{len(users) + 1}")
        observations.append({
            "tester": label,
            "kind": "action" if callback else "photo" if message.get("photo") else "text" if "text" in message else "other",
        })
    return {"bot_authenticated": True, "webhook_configured": False,
            "private_testers_observed": len(users), "observations": observations,
            "scope": "Single pending-update snapshot; no offsets advanced, files downloaded or replies sent",
            "f02_complete": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("channel", choices=HOSTS)
    args = parser.parse_args()
    if not sys.stdin.isatty():
        parser.error("Run in a local interactive terminal; token input must be hidden")
    try:
        token = getpass.getpass("Dedicated development bot token (hidden): ")
        print(json.dumps(probe(API(args.channel, token)), indent=2))
    except ProbeError as error:
        print(f"Probe stopped: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Probe canceled", file=sys.stderr)
        return 130
    except Exception:
        print("Probe stopped: unexpected response shape (details suppressed)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
