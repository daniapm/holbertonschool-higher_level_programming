#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    try:
        response.raise_for_status().text
        print(response)
    except:
        print("Error code: {}".format(response.status_code()))
