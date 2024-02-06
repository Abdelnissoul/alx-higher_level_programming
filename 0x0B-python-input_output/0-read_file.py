#!/usr/bin/python3
"""Defines a read file function."""


def read_file(filename=""):
    """reads the contents of a UTF8 text and print it."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
