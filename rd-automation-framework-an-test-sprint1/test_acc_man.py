#!/usr/bin/env python3

TEST_SUITE_NAME = "test account managerment"

import subprocess
import unittest
from test_utils import *
import time


BASE_URL_OPERATOR = f"https://dev1-operator-api.equix.app/v1/"
BASE_URL_RETAIl = f"https://dev1-retail-api.equix.app/v1/"


class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        refresh_token = read_refresh_token_config(file_name="config_dev1.ini")
        time.sleep(2)
        cls.access_token = refresh_access_token(refresh_token)

    def setUp(self):
        # This method will be run before each test case
        pass

    def accountman(self):
        url = f"{BASE_URL_OPERATOR}/search/account?page_id=1&page_size=15"

        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        data = {"query": {"bool": {"must": []}}, "sort": [{"last_update": "DESC"}]}
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data=data
        )

        # Validate HTTP response code, fail if not 200
        if status_code == 200:
            return response_data
        else:
            return None

    def test001(self):
        res = self.accountman()
        print(res)
        self.assertEqual({{"filde_API"}}, {{"File_SOD"}})


# check mapping API với file SOD --> đang đợi framework đọc file sod
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
