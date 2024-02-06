#!/usr/bin/python3
"""Defines a append write function."""


def append_write(filename="", text=""):
    """Append a string of a UTF8 text file.

    Args:
        filename : name of the file must be string.
        text : The text to be in  file. (string)
    Returns:
        The number of elements appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
