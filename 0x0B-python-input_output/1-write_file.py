#!/usr/bin/python3
"""Defines a write file function."""


def write_file(filename="", text=""):
    """returning a string to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
