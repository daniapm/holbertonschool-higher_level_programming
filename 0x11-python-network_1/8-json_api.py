#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) == 2:
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data={'q': argv[1]})
    else:
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data={'q': ""})
    try:
        dataj = response.json()
        if dataj:
            print("[{}] {}".format(dataj.get("id"), dataj.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
