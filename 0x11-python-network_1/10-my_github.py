#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    response = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                            auth=HTTPBasicAuth(argv[1], argv[2]))

    data = response.json()
    print(data["id"])
