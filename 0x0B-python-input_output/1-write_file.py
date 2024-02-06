#!/usr/bin/python3
"""Defines a function to write text to a UTF-8 encoded file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters written to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """ Returns the number of characters written to a file."""
        return f.write(text)
