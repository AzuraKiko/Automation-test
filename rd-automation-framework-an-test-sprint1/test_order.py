#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import unittest
from test_utils import *
import time

BASE_URL_OPERATOR = f"https://dev1-operator-api.equix.app/v1/"
BASE_URL_RETAIl = f"https://dev1-retail-api.equix.app/v1/"

TOKEN_ADVISOR: "123"
TOKEN_RETAIL: "456"

ACCOUNT = "A.50000099"

PAYLOAD = {
    "data": {
        "code": "BHP",
        "volume": 100,
        "order_type": "LIMIT_ORDER",
        "note": '{"order_state":"UserPlace","modify_action":"null","exchange":"AUSIEXBEST","data":{"side":"BUY","volume":100,"limit_price":42},"order_type":"LIMIT_ORDER"}',
        "is_buy": True,
        "account_id": ACCOUNT,
        "duration": "DAY",
        "exchange": "AUSIEXBEST",
        "limit_price": 42,
    }
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

    # check code require
    def test_require_code(self):
        """Testcase 01 : check require code"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["code"] = ""
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_require_volume(self):
        """Testcase 02 : check require volume"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["volume"] = ""
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_require_price(self):
        """Testcase 03 : check require price"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["limit_price"] = ""
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_require_account(self):
        """Testcase 04 : check require account_id"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["account_id"] = ""
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_require_duration(self):
        """Testcase 05 : check require duration"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["duration"] = ""
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_require_exchange(self):
        """Testcase 06 : check require exchange"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["exchange"] = ""
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_input_invalid_code(self):
        """Testcase 07 : check input invalid code"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["code"] = "111"
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertEqual(response_data["errorCode"], [1100])

    def test_input_invalid_order_type(self):
        """Testcase 08 : check input invalid order_type"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["order_type"] = "111"
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_input_invalid_volume(self):
        """Testcase 09 : check input invalid order_type"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["volume"] = "volume"
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_input_invalid_duration(self):
        """Testcase 10 : check input invalid order_type"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["duration"] = "volume"
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_input_invalid_note(self):
        """Testcase 11 : check input invalid note"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["note"] = "note"
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_input_invalid_exchange(self):
        """Testcase 12 : check input invalid exchange"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["note"] = "note"
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    # check vetting rule

    def test_check_cash_vetting(self):  # acc không đủ tièn để đặt lệnh
        """Testcase 13 : check cash vetting"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["account_id"] = {{"acc không đủ tiền đặt lệnh"}}

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_check_daily_trading_vetting(
        self,
    ):  # value> max net trading- giá trị giao dịch trong ngày
        """Testcase 14 : check daily trading vetting"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["account_id"] = ACCOUNT
        PAYLOAD["data"]["volume"] = "2000"
        PAYLOAD["data"]["Price"] = "100"

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_check_maximum_value_amount_BUY(self):  # số tiền tối đa/ 1 lệnh mua
        """Testcase 15 : check maximum vakue amount"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["account_id"] = {{"acc"}}
        PAYLOAD["data"]["volume"] = "2000"
        PAYLOAD["data"]["Price"] = "1000"

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    def test_check_minimum_value_amount_Buy(self):  # số tiền tối thiểu lệnh mua
        """Testcase 16 : check minimum value amount"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD["data"]["account_id"] = {{"acc"}}
        PAYLOAD["data"]["volume"] = "100"
        PAYLOAD["data"]["Price"] = "100"

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    # Check quyền advisor: Chekc đặt lệnh với account không thuộc organiation code
    def test_check_placeorder_advisor(self):
        """Testcase 17 : check place order with advisor"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {TOKEN_ADVISOR}",
        }

        PAYLOAD["data"]["account_id"] = {
            {"acc"}
        }  # account không thuộc quyền của advisor

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    # check quyền đặt lệnh retail : check đặt lệnh với account không đc gán với retail
    def test_check_placeorder_retail(self):  # số tiền tối thiểu lệnh mua
        """Testcase 18 : check place order with user deatil"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {TOKEN_RETAIL}",
        }

        PAYLOAD["data"]["account_id"] = {{"acc"}}  # acc không được gán với user retail

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response_data["errorCode"], "INVALID_ORDER")

    # check các type với các class
    # 1. Đặt lệnh class = Euity
    # 1.1. Đặt lệnh với duration = Day only
    def test_check_placeorder_Dayonly_equity_limit(self):
        """Testcase 19 : check place order - equity- Limit"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertNotEqual(response_data, None)

    def test_check_placeorder_Dayonly_equity_MTL(self):
        """Testcase 20 : check place order - equity- MTL"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertNotEqual(response_data, None)

    def test_check_placeorder__equity_stop_limit(self):
        """Testcase 21 : check place order - equity- stoplimit"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertNotEqual(response_data, None)

    # 1.2 Good still date
    # 1.2.1. limit
    def test_check_placeorder_equity_limit(self):
        """Testcase 22 : check place order-Good stil date- equity- limit"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertNotEqual(response_data, None)

    # 1.2.2. MTL
    def test_check_placeorder_equity_MTL(self):
        """Testcase 23 : check placeorder -Good stil date - equity- MTL"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD  # thay đổi payload

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertNotEqual(response_data, None)

    # 1.2.3. Stoplimit
    def test_check_placeorder_equity_stoplimit(self):
        """Testcase 24 : check place order - equity- MTL"""
        url = f"{BASE_URL_OPERATOR}/order"
        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        PAYLOAD  # thay đổi payload

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=PAYLOAD
        )

        self.assertEqual(status_code, 200)
        self.assertNotEqual(response_data, None)


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
