#!/usr/bin/python3

def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj: Object to be saved.
        filename: Name of the file to save the object to.
    """
    import json

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
