#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except:
        print("Error code: {}".format(response.status_code()))
