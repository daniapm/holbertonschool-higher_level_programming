#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    response = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                            auth=HTTPBasicAuth(argv[1], argv[2]))

    data = response.json()
    print(data["id"])
