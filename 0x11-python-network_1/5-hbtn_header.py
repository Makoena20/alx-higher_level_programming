#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL, and displays
the value of the variable X-Request-Id in the response header."""

import requests
import sys

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id', None))

if __name__ == "__main__":
    main()

