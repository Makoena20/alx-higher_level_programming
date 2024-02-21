#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.
    Args:
        obj: the object to check
        a_class: the specified class
    Returns:
        True if the object is an instance of, or if the object is an instance of a class that inherited from,
        the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
