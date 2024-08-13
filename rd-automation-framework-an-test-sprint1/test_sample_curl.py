#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import subprocess
import unittest
from test_utils import *
import requests
import time

BASE_URL_OPERATOR = f"https://dev1-operator-api.equix.app/v1/"
BASE_URL_RETAIl = f"https://dev1-retail-api.equix.app/v1/"


class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        refresh_token = read_refresh_token_config()
        time.sleep(2)
        cls.access_token = refresh_access_token(refresh_token)

    def setUp(self):
        # This method will be run before each test case
        pass

    # @unittest.skip("skipped")
    def test_01(self):
        """Test case ID 001: Test case name"""
        url = BASE_URL_RETAIl + "portfolio/total/A.50000156"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        self.assertEqual(status_code, 200)

        # self.assertEqual(response_data["total_market_value"], 9641808.7875)
        # self.assertEqual(response_data["cash_balance"], 999999)
        # self.assertEqual(response_data["status"]["sod_cash"], True)
        # self.assertEqual(response_data["positions"][0]["account_id"], "A.50000156")
        # self.assertEqual(response_data["positions"][0]["symbol"], "BHP")
        # self.assertEqual(response_data["positions"][0]["exchange"], "ASX")
        # self.assertEqual(response_data["positions"][0]["currency"], "AUD")
        # self.assertEqual(response_data["positions"][0]["style"], "Equity")
        # self.assertEqual(response_data["positions"][0]["volume"], 1059)
        # self.assertEqual(response_data["positions"][0]["updated"],)

        # status_code, response_data = send_request(
        #     url=url,
        #     method="GET",
        #     headers=headers)
        # new_cash_balance = response_data["cash_balance"]
        # self.assertEqual(new - old, 50)

    @unittest.skip("skipped")
    def test_02(self):
        """Test case ID 002: Test case name"""
        url = BASE_URL_RETAIl + "portfolio/total/A.50000166"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        # print(f"response: {response_data}")

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)

    # @unittest.skip("skipped")
    def test_03(self):
        """Test case ID 003: check"""
        url = f"{BASE_URL_RETAIl}/search/news?page_id=1&page_size=50"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = {
            "query": {
                "bool": {
                    "must": [
                        {"query_string": {"query": "*notificat*"}},
                        {"wildcard": {"symbol": {"wildcard": "*ANZ*"}}},
                        {
                            "range": {
                                "updated": {"from": 1721743200000, "to": 1722347999999}
                            }
                        },
                    ]
                }
            },
            "sort": [{"updated": {"order": "desc"}}],
        }

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)

        # @unittest.skip("skipped")

    def test_04(self):
        """Test case ID 004: check all user"""
        url = f"{BASE_URL_RETAIl}/search/user?page_id=1&page_size=15"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = {"query": {"bool": {"must": []}}, "sort": [{"updated": "DESC"}]}

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
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
