#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(HTTPBasicAuth(str(sys.argv[1]),
                                  str(sys.argv[2]))))

    try:
        data = response.json()
        print(data["id"])
    except:
        print("None")
