#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    params = ""
    if len(sys.argv) < 2:
        params = ""
    else:
        params = sys.argv[1]
    try:
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data={'q': params}).json()
        if ("name" in respose) and ("id" in response):
            print("[{}] {} ".format(response['id'], response['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")