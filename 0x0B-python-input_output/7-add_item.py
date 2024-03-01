#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"

    # Check if file exists
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, filename)

