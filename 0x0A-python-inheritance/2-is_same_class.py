#!/usr/bin/python3
"""Module for a class function that does checking"""


def is_same_class(obj, a_class):
    """Checks if the object is an instance of a the class"""
    if type(obj) == a_class:
        return True
    return False
