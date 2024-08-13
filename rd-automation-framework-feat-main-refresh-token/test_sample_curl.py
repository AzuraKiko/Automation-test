#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import subprocess
import unittest
from test_utils import *
import requests

BASE_URL_OPERATOR=f"https://dev1-operator-api.equix.app/v1/"
BASE_URL_RETAIl=f"https://dev1-retail-api.equix.app/v1/"

class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        refresh_token = read_refresh_token_config()
        cls.access_token = refresh_access_token(refresh_token)

    def setUp(self):
        # This method will be run before each test case
        pass

    #@unittest.skip("skipped")
    def test_01(self):
        """ Test case ID 001: Test case name """
        url = BASE_URL_RETAIl+"portfolio/total/A.50000156"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # Send POST request
        status_code, response_data = send_request(
            url=url,
            method="GET",
            headers=headers)
        
        # print(f"response: {response_data}")

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200 )

    #@unittest.skip("skipped")
    def test_02(self):
        """ Test case ID 002: Test case name """
        url = BASE_URL_RETAIl+"portfolio/total/A.50000166"

        # Headers
        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # Send POST request
        status_code, response_data = send_request(
            url=url,
            method="GET",
            headers=headers)
        
        # print(f"response: {response_data}")

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200 )
    
    #@unittest.skip("skipped")
    def test_03(self):
        """ Test case ID 003: Test case name """
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
                        {
                            "wildcard": {
                                "symbol": {
                                    "wildcard": "*ANZ*"
                                }
                            }
                        },
                        {
                            "range": {
                                "updated": {
                                    "from": 1721656800000,
                                    "to": 1722261599999
                                }
                            }
                        }
                    ]
                }
            },
            "sort": [
                {
                    "updated": {
                        "order": "desc"
                    }
                }
            ]
        }
        
        # Send POST request
        status_code, response_data = send_request(
            url=url,
            method="POST",
            headers=headers,
            data=data)

        # print(f"response: {response_data}")
        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200 )

if __name__ == '__main__':
    from argparse import ArgumentParser
    print("Running Test Suite")

    script = ArgumentParser(description=TEST_SUITE_NAME,
                            epilog="Note: any note here")
    #script.add_argument("Config", type=str, help="Config file")
    args, unittest_args = script.parse_known_args()

    from test_utils import testcase_sort_func
    unittest.defaultTestLoader.sortTestMethodsUsing = testcase_sort_func
    from framework import CustomTestRunner
    unittest.main(argv=[__file__] + unittest_args, testRunner=CustomTestRunner)