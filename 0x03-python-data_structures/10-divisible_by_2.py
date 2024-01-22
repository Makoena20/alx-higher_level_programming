#!/usr/bin/python3
"""
Module to find multiples of 2 in a list
"""


def divisible_by_2(my_list=[]):
    """
    Find multiples of 2 in a list

    Args:
        my_list (list): List of integers

    Returns:
        list: New list with True or False indicating if the integer at the
        same position in the original list is a multiple of 2
    """
    return [True if i % 2 == 0 else False for i in my_list]

if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(
            my_list[i], "is" if list_result[i] else "is not"))
        i += 1

