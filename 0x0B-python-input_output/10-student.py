#!/usr/bin/python3
"""function for a class Student."""


class Student:
    """class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function to get dictionary representing the Student."""
        try:
            for att in attrs:
                if type(att) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dict = dict()
        for k, val in self.__dict__.items():
            if k in attrs:
                new_dict[k] = val
        return new_dict
