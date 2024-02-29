#!/usr/bin/python3
"""
Module for saving Python objects to a text file using JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file in JSON format.

    Args:
        my_obj (any): Python object to be serialized.
        filename (str): Name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
