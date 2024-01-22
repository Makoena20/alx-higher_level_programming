#!/usr/bin/python3
"""
Deletes the item at a specific position in a list.
"""


def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the element to be deleted.

    Returns:
        list: The updated list.

    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:idx] + my_list[idx + 1:]
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)

