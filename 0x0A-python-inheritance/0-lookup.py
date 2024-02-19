#!/usr/bin/python3

def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to look up.

    Returns:
        A list containing the available attributes and methods of the object.
    """
    return dir(obj)

