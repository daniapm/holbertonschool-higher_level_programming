#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a
POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    params = ""
    if len(sys.argv) == 2:
        params = sys.argv[1]
    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data={q: params}).json()
        if ("name" in respose) and ("id" in response):
            print("[{}] {} ".format(response["id"], response["name"])
        else:
            print("No result")
        except:
            print("Not a valid JSON")
