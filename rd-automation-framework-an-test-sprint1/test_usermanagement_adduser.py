#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import subprocess
import unittest
from test_utils import *
import requests
import time

BASE_URL_OPERATOR = f"https://dev1-operator-api.equix.app/v1/"
BASE_URL_RETAIl = f"https://dev1-retail-api.equix.app/v1/"

PAYLOAD = {
    "phone": "AU|1111111111",
    "full_name": "dddd",
    "user_login_id": "ausiex2.demo@novus-fintech.com",
    "email": "ausiex3.demo@novus-fintech.com",
    "password": "",
    "role_group": "RG0",
    "email_template": "E1",
    "status": 2,
    "note": "",
    "access_method": 0,
    "user_type": "operation",
    "user_group": 3,
    "send_password": 1,
    "change_password": 1,
    "member_infor": "none",
}


def update_payload(base_payload: dict, **kwargs):
    """
    truyền payload là tham số đầu tiên, tiếp theo là các cặp giá trị
    ví dụ:

    data = update_payload(
            PAYLOAD, full_name="nghia", phone="45323",
        )
    """
    payload = base_payload

    # update payloda theo các cặp key và value truyền vào
    for key, val in kwargs.items():
        payload[key] = val
    return payload


def del_payload(base_payload: dict, *args):
    """
    truyền các keys để xóa trong field trong payload
    ví dụ
    data = del_payload(
            PAYLOAD, "full_name", "phone",
        )
    """
    payload = base_payload

    return {k: v for k, v in payload.items() if k not in args}


class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        refresh_token = read_refresh_token_config()
        time.sleep(2)
        cls.access_token = refresh_access_token(refresh_token)

    def setUp(self):
        # This method will be run before each test case
        pass

    def test_01(self):
        """Test case ID 001: check require Fullname"""
        url = f"{BASE_URL_RETAIl}/user/user-details"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = del_payload(PAYLOAD, "full_name")

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertNotEqual(int(status_code), 200)
        print(f'("response_data["errorCode"]")')
        self.assertIn(2000, response_data["errorCode"])

    def test_02(self):
        """Test case ID 002: check require User Login"""
        url = f"{BASE_URL_RETAIl}/user/user-details"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = del_payload(PAYLOAD, "user_login_id")

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertNotEqual(int(status_code), 200)
        print(f'("response_data["errorCode"]")')
        # self.assertIn(2000, response_data["errorCode"])

    def test_03(self):
        """Test case ID 003: check require Role Group"""
        url = f"{BASE_URL_RETAIl}/user/user-details"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = del_payload(PAYLOAD, "role_group")

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertNotEqual(int(status_code), 200)
        print(f'("response_data["errorCode"]")')
        # self.assertIn(2000, response_data["errorCode"])

    def test_04(self):
        """Test case ID 004: check require Email template"""
        url = f"{BASE_URL_RETAIl}/user/user-details"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = del_payload(PAYLOAD, "email_template")

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertNotEqual(int(status_code), 200)
        print(f'("response_data["errorCode"]")')
        # self.assertIn(2000, response_data["errorCode"])

    def test_05(self):
        """Test case ID 005: check require access_method"""
        url = f"{BASE_URL_RETAIl}/user/user-details"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = del_payload(PAYLOAD, "access_method")

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertNotEqual(int(status_code), 200)
        print(f'("response_data["errorCode"]")')
        # self.assertIn(2000, response_data["errorCode"])

    def test_06(self):
        """Test case ID 006: check require user_group"""
        url = f"{BASE_URL_RETAIl}/user/user-details"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = del_payload(PAYLOAD, "user_group")

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertNotEqual(int(status_code), 200)
        print(f'("response_data["errorCode"]")')
        # self.assertIn(2000, response_data["errorCode"])

    def test_07(self):
        """Test case ID 007: check require user_type"""
        url = f"{BASE_URL_RETAIl}/user/user-details"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = del_payload(PAYLOAD, "user_type")

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertNotEqual(int(status_code), 200)
        print(f'("response_data["errorCode"]")')
        # self.assertIn(2000, response_data["errorCode"])

    def test_08(self):
        """Test case ID 008: check add new user thành công"""
        url = f"{BASE_URL_RETAIl}/user/user-details"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # data
        data = PAYLOAD

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertNotEqual(int(status_code), 200)
        print(f'("response_data["errorCode"]")')
        # self.assertIn(2000, response_data["errorCode"])


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
