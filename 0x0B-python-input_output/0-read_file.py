#!/usr/bin/python3
"""
Module for read_file
"""


def read_file(filename=""):
    """
    Function to read a text file (UTF8) and print it to stdout
    Args:
        filename: the file to read
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")

