#!/usr/bin/env python3

import os
import subprocess
import json
import requests
import configparser
import requests

def run_command(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res

def testcase_sort_func(a,b):
    names = [a,b]
    names.sort(reverse=True)
    return [1,-1][names[0] == b]

def read_refresh_token_config(file_name="config.ini"):
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = current_path+ "/" + file_name

    config = configparser.ConfigParser()
    config.read(file_path)
    
    section = 'DEFAULT'
    key = 'refresh-token'

    refresh_token = config.get(section, key)
    return refresh_token

def refresh_access_token(refresh_token):
    url = "https://dev1-retail-api.equix.app/v1/auth/refresh"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "environment": "equix",
    }

    data = {
        "data": {
            "refreshToken": refresh_token,
            "deviceID": "aa55f78b-9de9-4593-93e0-a71d2a1c2de7",
            "stay_sign_in": True
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        data = response.json()
        new_access_token = data.get("accessToken")
        return new_access_token
    else:
        print(f"Error refreshing access token: {response.status_code}")
        print(response.text)
        return None

def send_request(url, method, headers, data=None):
    status_code = None
    response_data = None

    if method == "GET":
        response = requests.get(url, headers=headers)

        status_code = response.status_code 
        response_data =  response.json()
    elif method == "POST":
        response = requests.post(url, json=data, headers=headers)

        status_code = response.status_code 
        response_data =  response.json()
    
    return [status_code, response_data]
