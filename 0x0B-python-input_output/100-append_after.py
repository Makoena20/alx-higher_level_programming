#!/usr/bin/python3
"""
Module for append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The string to insert after each line containing the search_string.

    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
