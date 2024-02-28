#!/usr/bin/python3
"""
Module for converting objects to JSON strings.
"""


def to_json_string(my_obj):
    """
    Function to convert an object to a JSON string.

    Args:
        my_obj: Object to be converted.

    Returns:
        JSON representation of the object.
    """
    import json

    with open('file.json', 'w') as file:
        json.dump(my_obj, file)

    with open('file.json', 'r') as file:
        return file.read()
