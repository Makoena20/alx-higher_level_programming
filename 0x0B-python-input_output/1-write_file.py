#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except Exception as e:
        return 0
