#!/usr/bin/python3
"""Module for inherits from class"""


def inherits_from(obj, a_class):
    """shows if the object is a child of the parent class"""
    return isinstance(obj, a_class) and type(obj) != a_class
