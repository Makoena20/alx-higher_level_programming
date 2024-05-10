#!/usr/bin/python3
"""
This script takes GitHub credentials (username and password) and uses the GitHub API to display the user id.
"""

import sys
import requests

def get_github_id(username, password):
    """
    Function to retrieve GitHub user id using GitHub API.
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('id')
    else:
        return None

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    github_id = get_github_id(username, password)
    print(github_id)

