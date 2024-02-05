#!/usr/bin/python3
"""a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """function adds a new attribute to an object.

    Args:
        obj : The object.
        att : the attribute to add to object.
        value : The value of the attribute.
    Raises:
        TypeError: If the attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
