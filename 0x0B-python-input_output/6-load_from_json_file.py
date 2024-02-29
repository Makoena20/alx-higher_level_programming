#!/usr/bin/python3
"""
Module for loading object from JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file.
    
    Args:
        filename (str): The filename of the JSON file.
        
    Returns:
        The Python object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    pass
