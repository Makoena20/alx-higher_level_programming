#!/usr/bin/python3
"""
Module for writing a string to a text file and returning the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            return f.write(text)
    except Exception:
        return 0


if __name__ == "__main__":
    write_file("my_first_file.txt", "This School is so cool!\n")
