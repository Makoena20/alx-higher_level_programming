#!/usr/bin/python3
"""
Module to convert JSON string to Python data structure.
"""

def from_json_string(my_str):
    """
    Function to convert a JSON string to a Python data structure.

    Args:
        my_str (str): JSON string to convert.

    Returns:
        object: Python data structure converted from the JSON string.
    """
    import json

    with open('temp.json', 'w') as f:
        f.write(my_str)

    with open('temp.json', 'r') as f:
        data = json.load(f)

    return data
