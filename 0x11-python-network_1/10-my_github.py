#!/usr/bin/python3

"""
A script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    addr = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    response = requests.get(addr, auth=auth)
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
