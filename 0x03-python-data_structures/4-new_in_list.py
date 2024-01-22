#!/usr/bin/python3
"""
Module that defines a function new_in_list.
"""


def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position.

    Parameters:
    - my_list (list): The original list.
    - idx (int): The index at which the element should be replaced.
    - element: The new element to be inserted.

    Returns:
    - A new list with the element replaced at the specified index.
    - If idx is negative or out of range, a copy of the original list is returned.
    """
    new_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element
    return new_list

# Uncomment the following lines to test the function
# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_element = 9
# new_list = new_in_list(my_list, idx, new_element)
# print(new_list)
# print(my_list)

