import unittest
import os
from wotdash.services import PlayerQuery


class TestPlayerQuery(unittest.TestCase):
    def test_json_parse(self):
        s = """{
            "status": "ok",
            "meta": {
                "count": 1
            },
            "data": [
                {
                    "nickname": "%s",
                    "account_id": %s
                }
            ]
        }""" % (os.environ['WOT_NICKNAME'], os.environ['WOT_ACCOUNT_ID'])

        pq = PlayerQuery(s)
        self.assertEqual(pq.status, "ok")
        self.assertEqual(pq.count, 1)


class TestPlayerData(unittest.TestCase):
    def test_json_parse(self):
        self.assertEquals(True, False)


if __name__ == '__main__':
    unittest.main()
