#!/usr/bin/python3
"""
This script sends a POST request to the provided URL with the email as a parameter
Usage: ./2-post_email.py <URL> <email>
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email for POST request
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    # Send POST request and retrieve the response
    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))

