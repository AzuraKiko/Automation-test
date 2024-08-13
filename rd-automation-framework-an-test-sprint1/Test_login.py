import unittest
import requests


class TestLoginAPI(unittest.TestCase):
    BASE_URL = "https://your-api-url.com/login"

    def setUp(self):
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }

    def send_rest_api(self, method, url, headers, data=None):
        response = requests.request(method, url, headers=headers, json=data)
        return response.status_code, response.json()

    # check trường username require
    def test_username_required(self):
        """Test case ID 001: Username is required"""
        data = {"password": "Password1"}
        code, res = self.send_rest_api(
            "POST", self.BASE_URL, headers=self.headers, data=data
        )
        self.assertNotEqual(int(code), 200)
        self.assertIn("username is required", res["message"])

    # check trường password  require
    def test_password_required(self):
        """Test case ID 002: Password is required"""
        data = {"username": "testuser"}
        code, res = self.send_rest_api(
            "POST", self.BASE_URL, headers=self.headers, data=data
        )
        self.assertNotEqual(int(code), 200)
        self.assertIn("password is required", res["message"])

    # check trường username maxlength
    def test_username_max_length(self):
        """Test case ID 003: Username max length is 20 characters"""
        data = {"username": "a" * 21, "password": "Password1"}
        code, res = self.send_rest_api(
            "POST", self.BASE_URL, headers=self.headers, data=data
        )
        self.assertNotEqual(int(code), 200)
        self.assertIn("username must be at most 20 characters", res["message"])

    # check trường password maxlength
    def test_password_max_length(self):
        """Test case ID 004: Password max length is 8 characters"""
        data = {"username": "testuser", "password": "Password123"}
        code, res = self.send_rest_api(
            "POST", self.BASE_URL, headers=self.headers, data=data
        )
        self.assertNotEqual(int(code), 200)
        self.assertIn("password must be at most 8 characters", res["message"])

    # check case login thành công
    def test_valid_login(self):
        """Test case ID 005: Valid login"""
        data = {"username": "validuser", "password": "Passw1"}
        code, res = self.send_rest_api(
            "POST", self.BASE_URL, headers=self.headers, data=data
        )
        self.assertEqual(int(code), 200)
        self.assertIn("token", res)


if __name__ == "__main__":
    unittest.main()
