#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import unittest
from test_utils import *
import time

BASE_URL_OPERATOR = f"https://dev1-operator-api.equix.app/v1/"
BASE_URL_RETAIl = f"https://dev1-retail-api.equix.app/v1/"

ACCOUNT = "A.50000099"
ACCOUNT_INVALID = "A.50000417"
VALID_TOKEN = "valid_token"
INVALID_TOKEN = "5453453"
EXPIRED_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0aHUtYW4ubmd1eWVuQG5vdnVzLWZpbnRlY2guY29tIiwic3ViIjoiZXExNzE4NjkyODM0ODU1IiwiZXhwIjoxNzIyNTg0MDA0LjQ3OCwiZGV2aWNlX2lkIjoiYjViMmVmNzAtMjVjMy00MzZhLWI3YWItNzZjNjIyZWJmNGQyIiwiaWF0IjoxNzIyNTgyODA0fQ.obsnPc8zlJ6q1aPCMuTVj-lpXwyfcR8Oq-aNitmLiOj48JF5LAvIDnkBkh3z2y3CQMXC-hAxnXopPMxNQWKyugamvIBWXPRgQqLN0g985rjPPxLn-kZLhk7gfCRnxMbr2Bmv_pgRRVS62FnKS45t_Ywau3FCDyVfjT2u4UcWTgyPrichSNk2-zmJ8w6Gns2lLkWprgyqP6CK98tyUoDZVBpgWKeo_D9w7HlWYt6aG9uvKisEBOOQp2mZ3xGmQcAoYForbQxtbHxshoxF3Css54BV3HIbvww7bPetCp1LS8RjLJljMxoyPmOGdR7Ed16aG3TvQKTwWcyQNes-k33tZFcX2ON3ibr6xA6Hb3GRkdliT3GOvleZSyTq_b2EqDvQx2A0k2Fk0YGM7UJ-n7-5dptbxWbcRToAGo7rsiqC9p4pheEwTMQzVYalIMHvLbhfU7p9AJaS7DzF9cQJiWMk1j8bynfYd1GYEA9Tm1B_gzh9TCJiyMSiTTprsbZBt5u_ahNpd4pFAQ8nT8A-eb7owcbDvgwvbuEsXcfAUMvD_U5uh3JV4P-6-lzW8EtqWVaXHcD98TskLkuNRdn8agCTWQBtEcRXWl90vDAPkvLsiueDcOgGn32AefqobYwkNscT6ZLmoUMvxxYXy_h0XXNPyU3ow-1sJ9QWVBB7w-7umOA"


class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        refresh_token = read_refresh_token_config(file_name="config_dev1.ini")
        time.sleep(2)
        cls.access_token = refresh_access_token(refresh_token)

    def setUp(self):
        # This method will be run before each test case
        pass

    # comment 1

    def test_01(self):
        """ORD.11: Test valid token"""
        url = BASE_URL_RETAIl + "portfolio/total/" + ACCOUNT

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )
        # check respose / đang đợi đọc file SOD
        # self.assertNotEqual(response_data["account_id"], "fileSOD"["account _id "] )

        self.assertEqual(status_code, 200)
        # self.assertNotEqual(response_data["account_id"], "A.50000099")
        # self.assertNotEqual(response_data["total_market_value"], "{{}}")
        # self.assertNotEqual(response_data["cash_balance"], "{{}}")
        # self.assertNotEqual(response_data["securities_at_cost"], "{{}}")
        # self.assertNotEqual(response_data["total_profit_amount"], "{{}}")
        # self.assertNotEqual(response_data["total_profit_percent"], "{{}}")
        # self.assertNotEqual(response_data["available_balance"], "{{}}")
        # self.assertNotEqual(response_data["cash_balance_after_settlement"], ""{{}}"")

        # self.assetEqual()

    def test_02(self):
        """ORD.10: Test invalid  token"""
        url = BASE_URL_RETAIl + "portfolio/total/" + ACCOUNT

        # Headers
        headers = {
            "Authorization": f"Bearer {INVALID_TOKEN}",
        }

        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        self.assertEqual(status_code, 401)

    def test_03(self):
        """ORD.12: Test expired token"""
        url = BASE_URL_RETAIl + "portfolio/total/" + ACCOUNT

        # Headers
        headers = {
            "Authorization": f"Bearer {EXPIRED_TOKEN}",
        }

        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        self.assertEqual(status_code, 401)
        # gfgfgf

    def test_04(self):
        """ORD.14: Test accoun not exist"""
        url = BASE_URL_RETAIl + "portfolio/total/" + ACCOUNT_INVALID

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        self.assertEqual(status_code, 200)

    def test_10(self):
        """ORD.15: Test accoun not exist"""
        url = BASE_URL_RETAIl + "portfolio/total/" + ACCOUNT_INVALID

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    from argparse import ArgumentParser

    print("Running Test Suite")

    script = ArgumentParser(description=TEST_SUITE_NAME, epilog="Note: any note here")
    # script.add_argument("Config", type=str, help="Config file")
    args, unittest_args = script.parse_known_args()

    from test_utils import testcase_sort_func

    unittest.defaultTestLoader.sortTestMethodsUsing = testcase_sort_func
    from framework import CustomTestRunner

    unittest.main(argv=[__file__] + unittest_args, testRunner=CustomTestRunner)
