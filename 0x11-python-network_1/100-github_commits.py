#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""

import requests
from sys import argv


if __name__ == '__main__':
    user = argv[2]
    pw = argv[1]
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                            .format(user, pw))
    data = response.json()
    firt_ten = data[:10]
    for commit in firt_ten:
        comm = commit.get('sha')
        print(comm, end=': ')
        print(commit.get('commit').get('author').get('name '))
