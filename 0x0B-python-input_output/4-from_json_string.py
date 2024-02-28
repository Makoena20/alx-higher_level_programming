#!/usr/bin/python3

def from_json_string(my_str):
    """
    Function to convert a JSON string to a Python object.

    Args:
        my_str (str): A JSON string representing an object.

    Returns:
        obj: Python object represented by the JSON string.
    """
    import json

    with open('temp.json', 'w') as f:
        f.write(my_str)

    with open('temp.json', 'r') as f:
        obj = json.load(f)

    return obj
