#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"
# test push 2

import subprocess
import unittest
from test_utils import *

# import requests
import time

BASE_URL_OPERATOR = f"https://dev1-operator-api.equix.app/v1/"
BASE_URL_RETAIl = f"https://dev1-retail-api.equix.app/v1/"

ACCOUNT = "A.50000099"
FROMDATE = "1722952800000"
TODATE = "1723039199999"
PAYLOAD = {
    "query": {
        "bool": {
            "must": [
                {
                    "bool": {
                        "should": [
                            {"term": {"order_tag.keyword": {"value": "stoploss"}}},
                            {"term": {"order_tag.keyword": {"value": "open"}}},
                            {
                                "bool": {
                                    "must": [
                                        {
                                            "term": {
                                                "order_tag.keyword": {"value": "filled"}
                                            }
                                        },
                                        {
                                            "range": {
                                                "updated": {
                                                    "from": FROMDATE,
                                                    "to": TODATE,
                                                }
                                            }
                                        },
                                    ]
                                }
                            },
                            {
                                "bool": {
                                    "must": [
                                        {
                                            "term": {
                                                "order_tag.keyword": {
                                                    "value": "cancelled"
                                                }
                                            }
                                        },
                                        {
                                            "range": {
                                                "updated": {
                                                    "from": FROMDATE,
                                                    "to": TODATE,
                                                }
                                            }
                                        },
                                    ]
                                }
                            },
                        ]
                    }
                },
                {"term": {"account_id.keyword": {"value": ACCOUNT}}},
                {
                    "script": {
                        "script": "if(doc['origin_broker_order_id.keyword'].size()!=0)doc['origin_broker_order_id.keyword'].value==doc['broker_order_id.keyword'].value"
                    }
                },
            ]
        }
    },
    "sort": [{"updated": "desc"}],
}


class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        refresh_token = read_refresh_token_config(file_name="config_dev1.ini")
        time.sleep(2)
        cls.access_token = refresh_access_token(refresh_token)

    def setUp(self):
        # This method will be run before each test case
        pass

    # 1. Check với DAY
    # 1.1 Check all status
    def test_getOpenBuy1(self):
        """ "GOL1: Get all status"""
        url = f"{BASE_URL_OPERATOR}/search/order?page_id=1&page_size=50"
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertEqual(response_data["total_pages"], 1)
        self.assertEqual(response_data["current_page"], 1)
        self.assertEqual(response_data["total_count"], 48)
        self.assertEqual(response_data["data"][0]["account_id"], "A.50000099")

    def test_getOpenBuy2(self):
        """ "GOL2: Get orderlist success khi không truyền account"""
        url = f"{BASE_URL_OPERATOR}/search/order?page_id=1&page_size=50"
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }
        PAYLOAD["query"]["bool"]["must"][1]["term"]["account_id.keyword"]["value"] = ""

        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertEqual(response_data, [])

    # 1.2 Check status = "working"
    def test_getOpenBuy3(self):
        """ "GOL3: Get orderlist success -working"""
        url = f"{BASE_URL_OPERATOR}/search/order?page_id=1&page_size=50"
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["query"]["bool"]["must"][0]["bool"]["should"] = [
            {"term": {"order_tag.keyword": {"value": "open"}}}
        ]

        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)

    def test_getOpenBuy4(self):
        """ "GOL4: Get orderlist success -stoploss"""
        url = f"{BASE_URL_OPERATOR}/search/order?page_id=1&page_size=50"
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["query"]["bool"]["must"][0]["bool"]["should"] = [
            {"term": {"order_tag.keyword": {"value": "stoploss"}}}
        ]

        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)

    def test_getOpenBuy5(self):
        """ "GOL4: Get orderlist success -filled"""
        url = f"{BASE_URL_OPERATOR}/search/order?page_id=1&page_size=50"
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["query"]["bool"]["must"][0]["bool"]["should"] = [
            {"term": {"order_tag.keyword": {"value": "filled"}}}
        ]

        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
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
