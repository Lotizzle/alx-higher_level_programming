#!/usr/bin/python3
"""
This script sends a request to a URL
and displays the value of a custom header variable
"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print(request_id)
