#!/usr/bin/python3
"""
Module to send a POST request with a letter as parameter to search for a user.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

