#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    
    Args:
        obj: An object whose attributes and methods need to be looked up.
        
    Returns:
        A list containing the attributes and methods of the object.
    """
    return dir(obj)

