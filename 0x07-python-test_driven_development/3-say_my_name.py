#!/usr/bin/python3
"""module for say_my_name method."""


def say_my_name(first_name, last_name=""):
    """function for printing first and last name.

    Args:
        first_name: a string for first name.
        last_name: a string for last name.

    Raises:
        TypeError: if firstname or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
