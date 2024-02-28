#!/usr/bin/python3
def read_file(filename=""):
    """
    Read and print the content of a text file to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

# Test cases
read_file("my_file_0.txt")
