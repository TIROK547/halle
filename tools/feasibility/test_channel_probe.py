import json
import unittest
from unittest.mock import Mock
from channel_probe import API, ProbeError, probe


class ProbeTests(unittest.TestCase):
    def test_existing_webhook_prevents_polling(self):
        api = Mock()
        api.call.side_effect = [{"is_bot": True}, {"url": "https://private.example/webhook"}]
        with self.assertRaises(ProbeError):
            probe(api)
        self.assertEqual(api.call.call_count, 2)

    def test_private_events_are_sanitized_and_offsets_are_not_advanced(self):
        api = Mock()
        def message(user, **fields):
            return {"from": {"id": user}, "chat": {"type": "private"}, **fields}
        api.call.side_effect = [
            {"is_bot": True}, {"url": ""}, [
                {"message": message(12345, text="PRIVATE TEXT")},
                {"message": message(23456, photo=[{"file_id": "PRIVATE FILE"}])},
                {"callback_query": {"from": {"id": 12345}, "data": "PRIVATE ACTION", "message": {"chat": {"type": "private"}}}},
                {"message": {"from": {"id": 34567}, "chat": {"type": "group"}, "text": "GROUP"}},
            ]]
        result = probe(api)
        self.assertEqual(result["private_testers_observed"], 2)
        self.assertEqual([x["kind"] for x in result["observations"]], ["text", "photo", "action"])
        self.assertFalse(result["f02_complete"])
        self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertNotIn("12345", json.dumps(result))
        api.call.assert_called_with("getUpdates", {"timeout": 0, "limit": 100})

    def test_token_bearing_network_error_is_suppressed(self):
        api = API("telegram", "test-token")
        api.opener = Mock()
        api.opener.open.side_effect = RuntimeError("https://api.telegram.org/bottest-token/getMe")
        with self.assertRaises(ProbeError) as error:
            api.call("getMe")
        self.assertNotIn("test-token", str(error.exception))

    def test_mutating_methods_refused(self):
        api = API("bale", "test-token")
        with self.assertRaises(ProbeError):
            api.call("sendMessage")

    def test_malformed_response_fails(self):
        api = Mock()
        api.call.side_effect = [{"is_bot": True}, {}]
        with self.assertRaises(ProbeError):
            probe(api)


if __name__ == "__main__":
    unittest.main()
