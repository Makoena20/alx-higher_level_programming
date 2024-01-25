#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replace or add key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to replace or add.
        value (any): The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary

