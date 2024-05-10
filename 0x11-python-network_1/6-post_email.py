#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email parameter,
then displays the body of the response.
"""

import requests
import sys

def main():
    """
    Main function to send POST request with email parameter
    and display response body.
    """
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)

if __name__ == "__main__":
    main()

