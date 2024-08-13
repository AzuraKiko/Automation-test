#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

# test push1


import unittest
from test_utils import *

import time

BASE_URL_OPERATOR = f"https://dev1-operator-api.equix.app/v1/"
BASE_URL_RETAIl = f"https://dev1-retail-api.equix.app/v1/"

STOCK = "ACB"


def get_fee(VOLUME, PRICE):
    url = f"{BASE_URL_OPERATOR}/fee"

    headers = {
        "Authorization": f"Bearer {CurlTest.access_token}",
    }

    data = {
        "data": {
            "code": STOCK,
            "volume": VOLUME,
            "exchange": "AUSIEXBEST",
            "order_type": "LIMIT_ORDER",
            "is_buy": True,
            "account_id": "A.50000099",
            "duration": "DAY",
            "limit_price": PRICE,
        }
    }
    status_code, response_data = send_request(
        url=url, method="POST", headers=headers, data=data
    )
    return response_data["estimated_fees"]


def caculate_fee(vol, price, percent, min_fee):
    fee = vol * price * percent
    return max(fee, min_fee)


class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        refresh_token = read_refresh_token_config(file_name="config_dev1.ini")
        time.sleep(2)
        cls.access_token = refresh_access_token(refresh_token)

    def setUp(self):
        # This method will be run before each test case
        pass

    def test_TC1(self):
        """TC1: fee< fee tối thiểu"""
        estimate_fee = get_fee(100, 10)
        cacul_fee = caculate_fee(100, 10, 0.005, 60)
        self.assertEqual(estimate_fee, cacul_fee)

    def test_TC2(self):
        """TC2: fee = fee tối thiểu"""
        estimate_fee = get_fee(1200, 1000)
        cacul_fee = caculate_fee(1200, 1000, 0.00005, 60)
        self.assertEqual(estimate_fee, cacul_fee)

    def test_TC3(self):
        """TC3: fee > fee tối thiểu"""
        estimate_fee = get_fee(1300, 1000)
        cacul_fee = caculate_fee(1300, 1000, 0.00005, 60)
        self.assertEqual(estimate_fee, cacul_fee)


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
