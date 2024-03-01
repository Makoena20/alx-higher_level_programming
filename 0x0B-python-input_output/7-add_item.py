#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file in JSON format.
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists, if not, initialize an empty list
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Append arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the list to a file in JSON format
save_to_json_file(my_list, filename)

